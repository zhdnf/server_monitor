# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systeminfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='systeminfo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10systeminfo.proto\"\x1a\n\x08Response\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\">\n\x07Process\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x63pu\x18\x03 \x01(\x02\x12\x0b\n\x03mem\x18\x04 \x01(\x02\"\x18\n\tSysstatus\x12\x0b\n\x03\x63pu\x18\x01 \x01(\x02\x32Y\n\x07Sysinfo\x12%\n\nGetSysInfo\x12\n.Sysstatus\x1a\t.Response\"\x00\x12\'\n\x0cGetProcesses\x12\x08.Process\x1a\t.Response\"\x00(\x01\x62\x06proto3')
)




_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Response.action', index=0,
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
  serialized_start=20,
  serialized_end=46,
)


_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Process.pid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Process.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='Process.cpu', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mem', full_name='Process.mem', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=48,
  serialized_end=110,
)


_SYSSTATUS = _descriptor.Descriptor(
  name='Sysstatus',
  full_name='Sysstatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='Sysstatus.cpu', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=112,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Process'] = _PROCESS
DESCRIPTOR.message_types_by_name['Sysstatus'] = _SYSSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'systeminfo_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), dict(
  DESCRIPTOR = _PROCESS,
  __module__ = 'systeminfo_pb2'
  # @@protoc_insertion_point(class_scope:Process)
  ))
_sym_db.RegisterMessage(Process)

Sysstatus = _reflection.GeneratedProtocolMessageType('Sysstatus', (_message.Message,), dict(
  DESCRIPTOR = _SYSSTATUS,
  __module__ = 'systeminfo_pb2'
  # @@protoc_insertion_point(class_scope:Sysstatus)
  ))
_sym_db.RegisterMessage(Sysstatus)



_SYSINFO = _descriptor.ServiceDescriptor(
  name='Sysinfo',
  full_name='Sysinfo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=138,
  serialized_end=227,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSysInfo',
    full_name='Sysinfo.GetSysInfo',
    index=0,
    containing_service=None,
    input_type=_SYSSTATUS,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetProcesses',
    full_name='Sysinfo.GetProcesses',
    index=1,
    containing_service=None,
    input_type=_PROCESS,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYSINFO)

DESCRIPTOR.services_by_name['Sysinfo'] = _SYSINFO

# @@protoc_insertion_point(module_scope)