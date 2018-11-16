# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/protobuf-spec/mmlogic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.protobuf_spec import messages_pb2 as api_dot_protobuf__spec_dot_messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/protobuf-spec/mmlogic.proto',
  package='api',
  syntax='proto3',
  serialized_options=_b('Z5github.com/GoogleCloudPlatform/open-match/internal/pb'),
  serialized_pb=_b('\n\x1f\x61pi/protobuf-spec/mmlogic.proto\x12\x03\x61pi\x1a api/protobuf-spec/messages.proto2\xf6\x02\n\x07MmLogic\x12<\n\nGetProfile\x12\x15.messages.MatchObject\x1a\x15.messages.MatchObject\"\x00\x12;\n\x0e\x43reateProposal\x12\x15.messages.MatchObject\x1a\x10.messages.Result\"\x00\x12\x33\n\x0bReturnError\x12\x10.messages.Result\x1a\x10.messages.Result\"\x00\x12?\n\rGetPlayerPool\x12\x14.messages.PlayerPool\x1a\x14.messages.PlayerPool\"\x00\x30\x01\x12=\n\x14GetAllIgnoredPlayers\x12\x11.messages.IlInput\x1a\x10.messages.Roster\"\x00\x12;\n\x12ListIgnoredPlayers\x12\x11.messages.IlInput\x1a\x10.messages.Roster\"\x00\x42\x37Z5github.com/GoogleCloudPlatform/open-match/internal/pbb\x06proto3')
  ,
  dependencies=[api_dot_protobuf__spec_dot_messages__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MMLOGIC = _descriptor.ServiceDescriptor(
  name='MmLogic',
  full_name='api.MmLogic',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=75,
  serialized_end=449,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetProfile',
    full_name='api.MmLogic.GetProfile',
    index=0,
    containing_service=None,
    input_type=api_dot_protobuf__spec_dot_messages__pb2._MATCHOBJECT,
    output_type=api_dot_protobuf__spec_dot_messages__pb2._MATCHOBJECT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateProposal',
    full_name='api.MmLogic.CreateProposal',
    index=1,
    containing_service=None,
    input_type=api_dot_protobuf__spec_dot_messages__pb2._MATCHOBJECT,
    output_type=api_dot_protobuf__spec_dot_messages__pb2._RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReturnError',
    full_name='api.MmLogic.ReturnError',
    index=2,
    containing_service=None,
    input_type=api_dot_protobuf__spec_dot_messages__pb2._RESULT,
    output_type=api_dot_protobuf__spec_dot_messages__pb2._RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlayerPool',
    full_name='api.MmLogic.GetPlayerPool',
    index=3,
    containing_service=None,
    input_type=api_dot_protobuf__spec_dot_messages__pb2._PLAYERPOOL,
    output_type=api_dot_protobuf__spec_dot_messages__pb2._PLAYERPOOL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllIgnoredPlayers',
    full_name='api.MmLogic.GetAllIgnoredPlayers',
    index=4,
    containing_service=None,
    input_type=api_dot_protobuf__spec_dot_messages__pb2._ILINPUT,
    output_type=api_dot_protobuf__spec_dot_messages__pb2._ROSTER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListIgnoredPlayers',
    full_name='api.MmLogic.ListIgnoredPlayers',
    index=5,
    containing_service=None,
    input_type=api_dot_protobuf__spec_dot_messages__pb2._ILINPUT,
    output_type=api_dot_protobuf__spec_dot_messages__pb2._ROSTER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MMLOGIC)

DESCRIPTOR.services_by_name['MmLogic'] = _MMLOGIC

# @@protoc_insertion_point(module_scope)