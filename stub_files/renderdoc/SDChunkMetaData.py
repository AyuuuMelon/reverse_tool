# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SDChunkMetaData(): # skipped bases: <class 'SwigPyObject'>
    """ The metadata that goes along with a :class:`SDChunk` to detail how it was recorded. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    @property
    def callstack(self):
        """The frames of the CPU-side callstack leading up to the chunk."""
        pass

    @callstack.setter
    def callstack(self, value):
        pass

    @property
    def chunkID(self):
        """The internal chunk ID - unique given a particular driver in use."""
        pass

    @chunkID.setter
    def chunkID(self, value):
        pass

    @property
    def durationMicro(self):
        """
The duration in microseconds that this chunk took. This is the time for the actual
work, not the serialising.
Since 0 is a possible value for this (for extremely fast calls), -1 is the invalid/not present value.

"""
        pass

    @durationMicro.setter
    def durationMicro(self, value):
        pass

    @property
    def flags(self):
        """The :class:`SDChunkFlags` for this chunk."""
        pass

    @flags.setter
    def flags(self, value):
        pass

    @property
    def length(self):
        """
The length in bytes of this chunk - may be longer than the actual sum of the data if a
conservative size estimate was used on creation to avoid seeking to fix-up the stored length.

"""
        pass

    @length.setter
    def length(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def threadID(self):
        """The ID of the thread where this chunk was recorded."""
        pass

    @threadID.setter
    def threadID(self, value):
        pass

    @property
    def timestampMicro(self):
        """The point in time when this chunk was recorded, in microseconds since program start."""
        pass

    @timestampMicro.setter
    def timestampMicro(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1887A350>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SDChunkMetaData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SDChunkMetaData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SDChunkMetaData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SDChunkMetaData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SDChunkMetaData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SDChunkMetaData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SDChunkMetaData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SDChunkMetaData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SDChunkMetaData' objects>, 'durationMicro': <attribute 'durationMicro' of 'renderdoc.SDChunkMetaData' objects>, 'callstack': <attribute 'callstack' of 'renderdoc.SDChunkMetaData' objects>, 'length': <attribute 'length' of 'renderdoc.SDChunkMetaData' objects>, 'flags': <attribute 'flags' of 'renderdoc.SDChunkMetaData' objects>, 'chunkID': <attribute 'chunkID' of 'renderdoc.SDChunkMetaData' objects>, 'threadID': <attribute 'threadID' of 'renderdoc.SDChunkMetaData' objects>, 'timestampMicro': <attribute 'timestampMicro' of 'renderdoc.SDChunkMetaData' objects>, '__doc__': 'The metadata that goes along with a :class:`SDChunk` to detail how it was recorded.'})"


