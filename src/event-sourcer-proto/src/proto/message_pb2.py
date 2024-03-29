# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/message.proto',
  package='tutorial',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13proto/message.proto\x12\x08tutorial\"\x9d\x01\n\nLogMessage\x12\x16\n\x0eschema_version\x18\x01 \x01(\t\x12/\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.tutorial.LogMessage.MetaData\x1a\x46\n\x08MetaData\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12\x14\n\x0cmessage_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\tb\x06proto3')
)




_LOGMESSAGE_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='tutorial.LogMessage.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='tutorial.LogMessage.MetaData.unique_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='tutorial.LogMessage.MetaData.message_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='tutorial.LogMessage.MetaData.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=191,
)

_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='tutorial.LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema_version', full_name='tutorial.LogMessage.schema_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tutorial.LogMessage.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOGMESSAGE_METADATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=191,
)

_LOGMESSAGE_METADATA.containing_type = _LOGMESSAGE
_LOGMESSAGE.fields_by_name['metadata'].message_type = _LOGMESSAGE_METADATA
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), dict(

  MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), dict(
    DESCRIPTOR = _LOGMESSAGE_METADATA,
    __module__ = 'proto.message_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.LogMessage.MetaData)
    ))
  ,
  DESCRIPTOR = _LOGMESSAGE,
  __module__ = 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.LogMessage)
  ))
_sym_db.RegisterMessage(LogMessage)
_sym_db.RegisterMessage(LogMessage.MetaData)


# @@protoc_insertion_point(module_scope)
