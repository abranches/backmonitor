import unittest
import random
from datetime import datetime

from ..event import Event, _Event, EventType
from ..utilslib.strings import random_bytes, random_string

def random_timestamp():
    return datetime.fromtimestamp(
            random.randrange(0,2000000000) + random.random())

class EventTestCase(unittest.TestCase):
    FIELDS = ["type", "name", "timestamp", "args", "kwargs"]

    def fill_event(self):
        for f in  self.FIELDS:
            setattr(self.event, f, getattr(self, f))

    def setUp(self):
        self.type = EventType.BASIC
        self.name = "MyBasicEvent"
        self.timestamp = datetime.fromtimestamp(0)
        self.args = ["arg1", "arg2 123 123 123"]
        self.kwargs = {"errors": "kabooooomm!!!"}
        self.event = Event()
        self.fill_event()

    def test_eq_after_load_serialized_event(self):
        proto_raw = self.event.serialize()
        new_event = Event(protobuf=proto_raw)
        self.assertEqual(new_event, self.event)

    def test_raw_eq_after_load_serialized_event(self):
        proto_raw = self.event.serialize()
        new_event = Event(protobuf=proto_raw)
        for f in self.FIELDS:
            self.assertEqual(getattr(new_event, f), getattr(self.event, f))
        for f in self.FIELDS:
            self.assertEqual(getattr(new_event, f), getattr(self, f))


class RandomEventTestCase(EventTestCase):
    MAX_NAME_SIZE = 255
    MAX_ARG_VALUE_SIZE = 1024
    MAX_ARG_NAME_SIZE = 255
    MAX_ARGS = 16

    def setUp(self):
        self.type = random.choice(EventType.values())
        self.name = random_string(random.randrange(self.MAX_NAME_SIZE))
        self.timestamp = random_timestamp()
        self.args = []
        self.kwargs = {}
        for i in range(self.MAX_ARGS):
            arg_name = random_string(random.randrange(self.MAX_ARG_NAME_SIZE))
            arg_value = random_bytes(random.randrange(self.MAX_ARG_VALUE_SIZE))
            if random.choice((True, False)):
                self.args.append(arg_value)
            else:
                self.kwargs[arg_name] = arg_value
        self.event = Event()
        self.fill_event()
