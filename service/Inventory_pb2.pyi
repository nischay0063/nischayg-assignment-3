from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishingYear", "title"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    FICTION: Book.Genre
    GENRE_FIELD_NUMBER: _ClassVar[int]
    HISTORY: Book.Genre
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    THRILLER: Book.Genre
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.Genre
    isbn: str
    publishingYear: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.Genre, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class ISBN(_message.Message):
    __slots__ = ["isbnNo"]
    ISBNNO_FIELD_NUMBER: _ClassVar[int]
    isbnNo: str
    def __init__(self, isbnNo: _Optional[str] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ["isbn", "message"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    message: str
    def __init__(self, isbn: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
