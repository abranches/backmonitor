# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='node_data.proto',
  package='',
  serialized_pb='\n\x0fnode_data.proto\"j\n\x08NodeData\x12\x10\n\x08language\x18\x01 \x02(\t\x12\x18\n\x10language_version\x18\x02 \x01(\t\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\r\n\x05uname\x18\x04 \x01(\t\x12\x11\n\texec_path\x18\x05 \x01(\t')




_NODEDATA = _descriptor.Descriptor(
  name='NodeData',
  full_name='NodeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='NodeData.language', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_version', full_name='NodeData.language_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='NodeData.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uname', full_name='NodeData.uname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exec_path', full_name='NodeData.exec_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=19,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['NodeData'] = _NODEDATA

class NodeData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NODEDATA

  # @@protoc_insertion_point(class_scope:NodeData)


# @@protoc_insertion_point(module_scope)