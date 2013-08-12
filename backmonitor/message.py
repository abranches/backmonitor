from .exceptions import MessageException
from utilslib.enum import IntEnum
from network_messages.message_hello_pb2 import MessageHello as _MessageHello
from network_messages.message_hello_ok_pb2 import MessageHelloOK as _MessageHelloOK
from network_messages.message_event_pb2 import MessageEvent as _MessageEvent

MessageType = IntEnum(HELLO=10,
                      HELLO_OK=11,
                      EVENT=20,
                      EVENT_OK=21,
                      GOODBYE=30,
                      GOODBYE_OK=31,
                      )

MessageHello = _MessageHello
MessageHello.type = MessageType.HELLO

MessageHelloOK = _MessageHelloOK
MessageHelloOK.type = MessageType.HELLO_OK
#def s(self):
#    return "Message(%s, %s)" % (MessageType.key_of(self.type),
#                                super(MessageHelloOK, self).__str__())
#MessageHelloOK.__str__ = s

MessageEvent = _MessageEvent
MessageEvent.type = MessageType.EVENT

_message_handlers = [MessageHello, MessageHelloOK, MessageEvent]

def decode_message(frame):
    for mclass in _message_handlers:
        if mclass.type == frame.msg_type:
            msg_class = mclass
            break
    else:
        # this is raised if the for terminates without a break
        raise MessageException("Unknown message handler for %s" % frame)

    message = msg_class.FromString(frame.payload)
    return message
