# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: replicate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='replicate.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0freplicate.proto\"\"\n\x07Request\x12\x17\n\x0f\x63onnect_request\x18\x01 \x01(\t\"$\n\x08Response\x12\x18\n\x10\x63onnect_response\x18\x01 \x01(\t\"&\n\rStore_Request\x12\x15\n\rstore_request\x18\x01 \x01(\t\"5\n\x04\x44\x61ta\x12\x11\n\topeartion\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t2V\n\tReplicate\x12\'\n\x0e\x63onnect_master\x12\x08.Request\x1a\t.Response\"\x00\x12 \n\x05store\x12\x0e.Store_Request\x1a\x05.Data\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect_request', full_name='Request.connect_request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=53,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect_response', full_name='Response.connect_response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=91,
)


_STORE_REQUEST = _descriptor.Descriptor(
  name='Store_Request',
  full_name='Store_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store_request', full_name='Store_Request.store_request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=131,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opeartion', full_name='Data.opeartion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='Data.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Data.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=186,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Store_Request'] = _STORE_REQUEST
DESCRIPTOR.message_types_by_name['Data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'replicate_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'replicate_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

Store_Request = _reflection.GeneratedProtocolMessageType('Store_Request', (_message.Message,), dict(
  DESCRIPTOR = _STORE_REQUEST,
  __module__ = 'replicate_pb2'
  # @@protoc_insertion_point(class_scope:Store_Request)
  ))
_sym_db.RegisterMessage(Store_Request)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'replicate_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  ))
_sym_db.RegisterMessage(Data)



_REPLICATE = _descriptor.ServiceDescriptor(
  name='Replicate',
  full_name='Replicate',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=188,
  serialized_end=274,
  methods=[
  _descriptor.MethodDescriptor(
    name='connect_master',
    full_name='Replicate.connect_master',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='store',
    full_name='Replicate.store',
    index=1,
    containing_service=None,
    input_type=_STORE_REQUEST,
    output_type=_DATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPLICATE)

DESCRIPTOR.services_by_name['Replicate'] = _REPLICATE

# @@protoc_insertion_point(module_scope)
