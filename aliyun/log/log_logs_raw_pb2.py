# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log_logs_raw.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='log_logs_raw.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12log_logs_raw.proto\"\x81\x01\n\x06LogRaw\x12\x0c\n\x04Time\x18\x01 \x02(\r\x12!\n\x08\x43ontents\x18\x02 \x03(\x0b\x32\x0f.LogRaw.Content\x12\x0e\n\x06values\x18\x03 \x03(\t\x12\x0f\n\x07Time_ns\x18\x04 \x01(\x07\x1a%\n\x07\x43ontent\x12\x0b\n\x03Key\x18\x01 \x02(\t\x12\r\n\x05Value\x18\x02 \x02(\x0c\"\'\n\tLogTagRaw\x12\x0b\n\x03Key\x18\x01 \x02(\t\x12\r\n\x05Value\x18\x02 \x02(\t\"\x87\x01\n\x0bLogGroupRaw\x12\x15\n\x04Logs\x18\x01 \x03(\x0b\x32\x07.LogRaw\x12\x10\n\x08Reserved\x18\x02 \x01(\t\x12\r\n\x05Topic\x18\x03 \x01(\t\x12\x0e\n\x06Source\x18\x04 \x01(\t\x12\x13\n\x0bMachineUUID\x18\x05 \x01(\t\x12\x1b\n\x07LogTags\x18\x06 \x03(\x0b\x32\n.LogTagRaw\"2\n\x0fLogGroupListRaw\x12\x1f\n\tLogGroups\x18\x01 \x03(\x0b\x32\x0c.LogGroupRaw'
)




_LOGRAW_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='LogRaw.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Key', full_name='LogRaw.Content.Key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='LogRaw.Content.Value', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=152,
)

_LOGRAW = _descriptor.Descriptor(
  name='LogRaw',
  full_name='LogRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Time', full_name='LogRaw.Time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Contents', full_name='LogRaw.Contents', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='LogRaw.values', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Time_ns', full_name='LogRaw.Time_ns', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGRAW_CONTENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=152,
)


_LOGTAGRAW = _descriptor.Descriptor(
  name='LogTagRaw',
  full_name='LogTagRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Key', full_name='LogTagRaw.Key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='LogTagRaw.Value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=193,
)


_LOGGROUPRAW = _descriptor.Descriptor(
  name='LogGroupRaw',
  full_name='LogGroupRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Logs', full_name='LogGroupRaw.Logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Reserved', full_name='LogGroupRaw.Reserved', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Topic', full_name='LogGroupRaw.Topic', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Source', full_name='LogGroupRaw.Source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MachineUUID', full_name='LogGroupRaw.MachineUUID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LogTags', full_name='LogGroupRaw.LogTags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=331,
)


_LOGGROUPLISTRAW = _descriptor.Descriptor(
  name='LogGroupListRaw',
  full_name='LogGroupListRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='LogGroups', full_name='LogGroupListRaw.LogGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=383,
)

_LOGRAW_CONTENT.containing_type = _LOGRAW
_LOGRAW.fields_by_name['Contents'].message_type = _LOGRAW_CONTENT
_LOGGROUPRAW.fields_by_name['Logs'].message_type = _LOGRAW
_LOGGROUPRAW.fields_by_name['LogTags'].message_type = _LOGTAGRAW
_LOGGROUPLISTRAW.fields_by_name['LogGroups'].message_type = _LOGGROUPRAW
DESCRIPTOR.message_types_by_name['LogRaw'] = _LOGRAW
DESCRIPTOR.message_types_by_name['LogTagRaw'] = _LOGTAGRAW
DESCRIPTOR.message_types_by_name['LogGroupRaw'] = _LOGGROUPRAW
DESCRIPTOR.message_types_by_name['LogGroupListRaw'] = _LOGGROUPLISTRAW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogRaw = _reflection.GeneratedProtocolMessageType('LogRaw', (_message.Message,), {

  'Content' : _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
    'DESCRIPTOR' : _LOGRAW_CONTENT,
    '__module__' : 'log_logs_raw_pb2'
    # @@protoc_insertion_point(class_scope:LogRaw.Content)
    })
  ,
  'DESCRIPTOR' : _LOGRAW,
  '__module__' : 'log_logs_raw_pb2'
  # @@protoc_insertion_point(class_scope:LogRaw)
  })
_sym_db.RegisterMessage(LogRaw)
_sym_db.RegisterMessage(LogRaw.Content)

LogTagRaw = _reflection.GeneratedProtocolMessageType('LogTagRaw', (_message.Message,), {
  'DESCRIPTOR' : _LOGTAGRAW,
  '__module__' : 'log_logs_raw_pb2'
  # @@protoc_insertion_point(class_scope:LogTagRaw)
  })
_sym_db.RegisterMessage(LogTagRaw)

LogGroupRaw = _reflection.GeneratedProtocolMessageType('LogGroupRaw', (_message.Message,), {
  'DESCRIPTOR' : _LOGGROUPRAW,
  '__module__' : 'log_logs_raw_pb2'
  # @@protoc_insertion_point(class_scope:LogGroupRaw)
  })
_sym_db.RegisterMessage(LogGroupRaw)

LogGroupListRaw = _reflection.GeneratedProtocolMessageType('LogGroupListRaw', (_message.Message,), {
  'DESCRIPTOR' : _LOGGROUPLISTRAW,
  '__module__' : 'log_logs_raw_pb2'
  # @@protoc_insertion_point(class_scope:LogGroupListRaw)
  })
_sym_db.RegisterMessage(LogGroupListRaw)


# @@protoc_insertion_point(module_scope)
