# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DebugMessage import DebugMessage
from .FrameStatistics import FrameStatistics

class FrameDescription(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains frame-level global information
    
    .. data:: NoFrameNumber
    
      No frame number is available.
    """
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
    def captureTime(self):
        """The time when the capture was created, as a unix timestamp in UTC."""
        pass

    @captureTime.setter
    def captureTime(self, value):
        pass

    @property
    def compressedFileSize(self):
        """The total file size of the whole capture in bytes, before decompression."""
        pass

    @compressedFileSize.setter
    def compressedFileSize(self, value):
        pass

    @property
    def debugMessages(self) -> List[DebugMessage]:
        """
The debug messages that are not associated with any particular event.

:type: List[DebugMessage]

"""
        pass

    @debugMessages.setter
    def debugMessages(self, value: List[DebugMessage]):
        pass

    @property
    def fileOffset(self):
        """
The offset into the file of the start of the frame.

.. note:: Similarly to :data:`APIEvent.fileOffset` this should only be used as a relative measure,
  as it is not a literal number of bytes from the start of the file on disk.

"""
        pass

    @fileOffset.setter
    def fileOffset(self, value):
        pass

    @property
    def frameNumber(self):
        """
Starting from frame #1 defined as the time from application startup to first present,
this counts the frame number when the capture was made.

.. note:: This value is only accurate if the capture was triggered through the default mechanism, if
  it was triggered from the application API it doesn't correspond to anything and will be set to
  :data:`NoFrameNumber`.

"""
        pass

    @frameNumber.setter
    def frameNumber(self, value):
        pass

    @property
    def initDataSize(self):
        """The byte size of the section of the file that contains frame-initial contents."""
        pass

    @initDataSize.setter
    def initDataSize(self, value):
        pass

    @property
    def persistentSize(self):
        """The byte size of the section of the file that must be kept in memory persistently."""
        pass

    @persistentSize.setter
    def persistentSize(self, value):
        pass

    @property
    def stats(self) -> FrameStatistics:
        """
The frame statistics.

:type: FrameStatistics

"""
        pass

    @stats.setter
    def stats(self, value: FrameStatistics):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def uncompressedFileSize(self):
        """The total file size of the whole capture in bytes, after decompression."""
        pass

    @uncompressedFileSize.setter
    def uncompressedFileSize(self, value):
        pass


    NoFrameNumber = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoFrameNumber': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1886D110>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.FrameDescription' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.FrameDescription' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.FrameDescription' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.FrameDescription' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.FrameDescription' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.FrameDescription' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.FrameDescription' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.FrameDescription' objects>, 'persistentSize': <attribute 'persistentSize' of 'renderdoc.FrameDescription' objects>, 'frameNumber': <attribute 'frameNumber' of 'renderdoc.FrameDescription' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.FrameDescription' objects>, 'captureTime': <attribute 'captureTime' of 'renderdoc.FrameDescription' objects>, 'fileOffset': <attribute 'fileOffset' of 'renderdoc.FrameDescription' objects>, 'stats': <attribute 'stats' of 'renderdoc.FrameDescription' objects>, 'uncompressedFileSize': <attribute 'uncompressedFileSize' of 'renderdoc.FrameDescription' objects>, 'compressedFileSize': <attribute 'compressedFileSize' of 'renderdoc.FrameDescription' objects>, 'initDataSize': <attribute 'initDataSize' of 'renderdoc.FrameDescription' objects>, 'debugMessages': <attribute 'debugMessages' of 'renderdoc.FrameDescription' objects>, '__doc__': '\\nContains frame-level global information\\n\\n.. data:: NoFrameNumber\\n\\n  No frame number is available.\\n\\n'})"


