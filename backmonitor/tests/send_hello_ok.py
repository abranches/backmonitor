import struct

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

from ..network_messages.message_hello_ok_pb2 import MessageHelloOK
from ..message import MessageType

m = MessageHelloOK()
m.sys_id = "OLA teste teste um dois tres"

class P(Protocol):
    def connectionMade(self):
        serial = m.SerializeToString()
        b = struct.pack(">BH", MessageType.GOODBYE_OK, len(serial)) +serial + '\xFE'
        self.transport.write(b)
        self.transport.loseConnection()

endpoint = TCP4ClientEndpoint(reactor, "localhost", 8990)
d = connectProtocol(endpoint, P())
reactor.run()
