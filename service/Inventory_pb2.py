# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fInventory.proto\"\x98\x01\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1a\n\x05genre\x18\x04 \x01(\x0e\x32\x0b.Book.Genre\x12\x16\n\x0epublishingYear\x18\x05 \x01(\x05\"/\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\x0c\n\x08THRILLER\x10\x01\x12\x0b\n\x07HISTORY\x10\x02\"\x16\n\x04ISBN\x12\x0e\n\x06isbnNo\x18\x01 \x01(\t\"\'\n\x06Result\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2M\n\x10InventoryService\x12\x1e\n\nCreateBook\x12\x05.Book\x1a\x07.Result\"\x00\x12\x19\n\x07GetBook\x12\x05.ISBN\x1a\x05.Book\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=20
  _BOOK._serialized_end=172
  _BOOK_GENRE._serialized_start=125
  _BOOK_GENRE._serialized_end=172
  _ISBN._serialized_start=174
  _ISBN._serialized_end=196
  _RESULT._serialized_start=198
  _RESULT._serialized_end=237
  _INVENTORYSERVICE._serialized_start=239
  _INVENTORYSERVICE._serialized_end=316
# @@protoc_insertion_point(module_scope)
