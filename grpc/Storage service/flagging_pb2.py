# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flagging.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flagging.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x66lagging.proto\"4\n\x11UserSubmitRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0f\n\x07hashKey\x18\x02 \x01(\t\"4\n\x0fUserSubmitReply\x12\x10\n\x08rejected\x18\x01 \x01(\x08\x12\x0f\n\x07\x65xisted\x18\x02 \x01(\x08\"$\n\x12UserRequestRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\")\n\x10UserRequestReply\x12\x15\n\runflaggedHash\x18\x01 \x03(\t\"%\n\x12\x41\x64minSubmitRequest\x12\x0f\n\x07hashKey\x18\x01 \x01(\t\"<\n\x10\x41\x64minSubmitReply\x12\x13\n\x0bhashKeyList\x18\x01 \x03(\t\x12\x13\n\x0b\x66laggedList\x18\x02 \x03(\x08\"%\n\x13\x41\x64minRequestRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\"=\n\x11\x41\x64minRequestReply\x12\x13\n\x0bhashKeyList\x18\x01 \x03(\t\x12\x13\n\x0b\x66laggedList\x18\x02 \x03(\x08\x32\xf3\x01\n\rPhotoFlagging\x12\x34\n\nUserSubmit\x12\x12.UserSubmitRequest\x1a\x10.UserSubmitReply\"\x00\x12\x37\n\x0bUserRequest\x12\x13.UserRequestRequest\x1a\x11.UserRequestReply\"\x00\x12\x37\n\x0b\x41\x64minSubmit\x12\x13.AdminSubmitRequest\x1a\x11.AdminSubmitReply\"\x00\x12:\n\x0c\x41\x64minRequest\x12\x14.AdminRequestRequest\x1a\x12.AdminRequestReply\"\x00\x62\x06proto3')
)




_USERSUBMITREQUEST = _descriptor.Descriptor(
  name='UserSubmitRequest',
  full_name='UserSubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserSubmitRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashKey', full_name='UserSubmitRequest.hashKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=18,
  serialized_end=70,
)


_USERSUBMITREPLY = _descriptor.Descriptor(
  name='UserSubmitReply',
  full_name='UserSubmitReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rejected', full_name='UserSubmitReply.rejected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='existed', full_name='UserSubmitReply.existed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=72,
  serialized_end=124,
)


_USERREQUESTREQUEST = _descriptor.Descriptor(
  name='UserRequestRequest',
  full_name='UserRequestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserRequestRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=126,
  serialized_end=162,
)


_USERREQUESTREPLY = _descriptor.Descriptor(
  name='UserRequestReply',
  full_name='UserRequestReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unflaggedHash', full_name='UserRequestReply.unflaggedHash', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=164,
  serialized_end=205,
)


_ADMINSUBMITREQUEST = _descriptor.Descriptor(
  name='AdminSubmitRequest',
  full_name='AdminSubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashKey', full_name='AdminSubmitRequest.hashKey', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=207,
  serialized_end=244,
)


_ADMINSUBMITREPLY = _descriptor.Descriptor(
  name='AdminSubmitReply',
  full_name='AdminSubmitReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashKeyList', full_name='AdminSubmitReply.hashKeyList', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flaggedList', full_name='AdminSubmitReply.flaggedList', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=246,
  serialized_end=306,
)


_ADMINREQUESTREQUEST = _descriptor.Descriptor(
  name='AdminRequestRequest',
  full_name='AdminRequestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='AdminRequestRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=308,
  serialized_end=345,
)


_ADMINREQUESTREPLY = _descriptor.Descriptor(
  name='AdminRequestReply',
  full_name='AdminRequestReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashKeyList', full_name='AdminRequestReply.hashKeyList', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flaggedList', full_name='AdminRequestReply.flaggedList', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=347,
  serialized_end=408,
)

DESCRIPTOR.message_types_by_name['UserSubmitRequest'] = _USERSUBMITREQUEST
DESCRIPTOR.message_types_by_name['UserSubmitReply'] = _USERSUBMITREPLY
DESCRIPTOR.message_types_by_name['UserRequestRequest'] = _USERREQUESTREQUEST
DESCRIPTOR.message_types_by_name['UserRequestReply'] = _USERREQUESTREPLY
DESCRIPTOR.message_types_by_name['AdminSubmitRequest'] = _ADMINSUBMITREQUEST
DESCRIPTOR.message_types_by_name['AdminSubmitReply'] = _ADMINSUBMITREPLY
DESCRIPTOR.message_types_by_name['AdminRequestRequest'] = _ADMINREQUESTREQUEST
DESCRIPTOR.message_types_by_name['AdminRequestReply'] = _ADMINREQUESTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserSubmitRequest = _reflection.GeneratedProtocolMessageType('UserSubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERSUBMITREQUEST,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:UserSubmitRequest)
  })
_sym_db.RegisterMessage(UserSubmitRequest)

UserSubmitReply = _reflection.GeneratedProtocolMessageType('UserSubmitReply', (_message.Message,), {
  'DESCRIPTOR' : _USERSUBMITREPLY,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:UserSubmitReply)
  })
_sym_db.RegisterMessage(UserSubmitReply)

UserRequestRequest = _reflection.GeneratedProtocolMessageType('UserRequestRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUESTREQUEST,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:UserRequestRequest)
  })
_sym_db.RegisterMessage(UserRequestRequest)

UserRequestReply = _reflection.GeneratedProtocolMessageType('UserRequestReply', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUESTREPLY,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:UserRequestReply)
  })
_sym_db.RegisterMessage(UserRequestReply)

AdminSubmitRequest = _reflection.GeneratedProtocolMessageType('AdminSubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINSUBMITREQUEST,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:AdminSubmitRequest)
  })
_sym_db.RegisterMessage(AdminSubmitRequest)

AdminSubmitReply = _reflection.GeneratedProtocolMessageType('AdminSubmitReply', (_message.Message,), {
  'DESCRIPTOR' : _ADMINSUBMITREPLY,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:AdminSubmitReply)
  })
_sym_db.RegisterMessage(AdminSubmitReply)

AdminRequestRequest = _reflection.GeneratedProtocolMessageType('AdminRequestRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINREQUESTREQUEST,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:AdminRequestRequest)
  })
_sym_db.RegisterMessage(AdminRequestRequest)

AdminRequestReply = _reflection.GeneratedProtocolMessageType('AdminRequestReply', (_message.Message,), {
  'DESCRIPTOR' : _ADMINREQUESTREPLY,
  '__module__' : 'flagging_pb2'
  # @@protoc_insertion_point(class_scope:AdminRequestReply)
  })
_sym_db.RegisterMessage(AdminRequestReply)



_PHOTOFLAGGING = _descriptor.ServiceDescriptor(
  name='PhotoFlagging',
  full_name='PhotoFlagging',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=411,
  serialized_end=654,
  methods=[
  _descriptor.MethodDescriptor(
    name='UserSubmit',
    full_name='PhotoFlagging.UserSubmit',
    index=0,
    containing_service=None,
    input_type=_USERSUBMITREQUEST,
    output_type=_USERSUBMITREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserRequest',
    full_name='PhotoFlagging.UserRequest',
    index=1,
    containing_service=None,
    input_type=_USERREQUESTREQUEST,
    output_type=_USERREQUESTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AdminSubmit',
    full_name='PhotoFlagging.AdminSubmit',
    index=2,
    containing_service=None,
    input_type=_ADMINSUBMITREQUEST,
    output_type=_ADMINSUBMITREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AdminRequest',
    full_name='PhotoFlagging.AdminRequest',
    index=3,
    containing_service=None,
    input_type=_ADMINREQUESTREQUEST,
    output_type=_ADMINREQUESTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PHOTOFLAGGING)

DESCRIPTOR.services_by_name['PhotoFlagging'] = _PHOTOFLAGGING

# @@protoc_insertion_point(module_scope)
