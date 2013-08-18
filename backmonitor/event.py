from datetime import datetime

from utilslib.enum import IntEnum
from proto_classes.event_pb2 import Event as _Event

EventType = IntEnum("BASIC",
                    "EXCEPTION",
                    "STACKTRACE",
                    )

class Event(object):
    def __init__(self, protobuf=None):
        self.type = EventType.BASIC
        self.name = ""
        self.timestamp = datetime.fromtimestamp(0)
        self.args = []
        self.kwargs = {}

        self._protobuf = _Event()
        if protobuf:
            self._load_protobuf(protobuf)
        
    def _load_protobuf(self, raw_protobuf):
        self._protobuf.ParseFromString(raw_protobuf)
        self.type = self._protobuf.type
        self.name = self._protobuf.name
        self.timestamp = datetime.fromtimestamp(self._protobuf.timestamp)
        self.args = []
        self.kwargs = {}
        for arg in self._protobuf.arg:
            if arg.name:
                self.kwargs[arg.name] = arg.value
            else:
                self.args.append(arg.value)

    def _update_protobuf_fields(self):
        self._protobuf.type = self.type
        self._protobuf.name = self.name
        self._protobuf.timestamp = float(datetime.strftime(self.timestamp, 
                                                           "%s.%f"))

        # clear argument fields in protobuf structure
        while len(self._protobuf.arg) != 0:
            del self._protobuf.arg[0]

        # reassign them
        for value in self.args:
            a = self._protobuf.arg.add()
            a.value = value
        for name, value in self.kwargs.items():
            a = self._protobuf.arg.add()
            a.name = name
            a.value = value

    def serialize(self):
        self._update_protobuf_fields()
        return self._protobuf.SerializeToString()

    def __repr__(self):
        return "Event(%s, %r, %r, args=%s, kwargs=%s)" % \
                (EventType.key_of(self.type), self.name, self.timestamp,
                 self.args, self.kwargs)

    def __str__(self):
        return "Event(%s, %r, %s)" % (EventType.key_of(self.type), self.name,
                                      self.timestamp)

    def __eq__(self, o):
        return self.type == o.type and self.name == o.name and \
               self.timestamp == o.timestamp and self.args == o.args and \
               self.kwargs == o.kwargs
