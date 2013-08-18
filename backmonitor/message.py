import logging

from .exceptions import MessageException
from utilslib.enum import IntEnum
from proto_classes.message_hello_pb2 import MessageHello
from proto_classes.message_hello_ok_pb2 import MessageHelloOK
from proto_classes.message_event_pb2 import MessageEvent

log = logging.getLogger(__name__)

MessageType = IntEnum(HELLO=10,
                      HELLO_OK=11,
                      EVENT=20,
                      EVENT_OK=21,
                      GOODBYE=30,
                      GOODBYE_OK=31,
                      )

_message_handlers = [(MessageType.HELLO,    MessageHello),
                     (MessageType.HELLO_OK, MessageHelloOK),
                     (MessageType.EVENT,    MessageEvent)
                    ]

def _message__str__(self):
    return "MessageProtobuf(%s)" % MessageType.key_of(self.type)

for mtype, mclass in _message_handlers:
    mclass.type = mtype
    mclass.__str__ = _message__str__

def decode_message(frame):
    for mtype, mclass in _message_handlers:
        if frame.msg_type == mtype:
            msg_class = mclass
            break
    else:
        # this is raised if the for terminates without a break
        raise MessageException("Unknown message handler for %s" % frame)

    message = msg_class.FromString(frame.payload)
    return message
