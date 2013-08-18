import struct

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

from .. import config
from ..network_messages.message_hello_ok_pb2 import MessageHelloOK
from ..message import MessageType
from ..frame import Frame

m = MessageHelloOK()
m.sys_id = "OLA teste teste um dois tres"

class P(Protocol):
    def connectionMade(self):
        payload = m.SerializeToString()
        frame = Frame(MessageType.HELLO_OK, payload)
        self.transport.write(frame.encode())
        self.transport.loseConnection()

endpoint = TCP4ClientEndpoint(reactor, "localhost", config.LISTEN_PORT)
d = connectProtocol(endpoint, P())
reactor.run()
