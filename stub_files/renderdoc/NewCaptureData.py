# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class NewCaptureData(): # skipped bases: <class 'SwigPyObject'>
    """ Information about the a new capture created by the target. """
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
    def api(self):
        """
The API used for this capture, if available.

.. note::
  May be empty if running with an older version of RenderDoc

"""
        pass

    @api.setter
    def api(self, value):
        pass

    @property
    def byteSize(self):
        """The size of the capture, in bytes."""
        pass

    @byteSize.setter
    def byteSize(self, value):
        pass

    @property
    def captureId(self):
        """An identifier to use to refer to this capture."""
        pass

    @captureId.setter
    def captureId(self, value):
        pass

    @property
    def frameNumber(self):
        """The frame number that this capture came from."""
        pass

    @frameNumber.setter
    def frameNumber(self, value):
        pass

    @property
    def local(self):
        """``True`` if the target is running on the local system."""
        pass

    @local.setter
    def local(self, value):
        pass

    @property
    def path(self):
        """The local path on the target system where the capture is saved."""
        pass

    @path.setter
    def path(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def thumbHeight(self):
        """The height of the image contained in :data:`thumbnail`."""
        pass

    @thumbHeight.setter
    def thumbHeight(self, value):
        pass

    @property
    def thumbnail(self):
        """The raw bytes that contain the capture thumbnail, as RGB8 data."""
        pass

    @thumbnail.setter
    def thumbnail(self, value):
        pass

    @property
    def thumbWidth(self):
        """The width of the image contained in :data:`thumbnail`."""
        pass

    @thumbWidth.setter
    def thumbWidth(self, value):
        pass

    @property
    def timestamp(self):
        """The time the capture was created, as a unix timestamp in UTC."""
        pass

    @timestamp.setter
    def timestamp(self, value):
        pass

    @property
    def title(self):
        """The custom title for this capture, if empty a default title can be used."""
        pass

    @title.setter
    def title(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188CC780>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.NewCaptureData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.NewCaptureData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.NewCaptureData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.NewCaptureData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.NewCaptureData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.NewCaptureData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.NewCaptureData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.NewCaptureData' objects>, 'frameNumber': <attribute 'frameNumber' of 'renderdoc.NewCaptureData' objects>, 'title': <attribute 'title' of 'renderdoc.NewCaptureData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.NewCaptureData' objects>, 'thumbHeight': <attribute 'thumbHeight' of 'renderdoc.NewCaptureData' objects>, 'path': <attribute 'path' of 'renderdoc.NewCaptureData' objects>, 'captureId': <attribute 'captureId' of 'renderdoc.NewCaptureData' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.NewCaptureData' objects>, 'local': <attribute 'local' of 'renderdoc.NewCaptureData' objects>, 'thumbWidth': <attribute 'thumbWidth' of 'renderdoc.NewCaptureData' objects>, 'timestamp': <attribute 'timestamp' of 'renderdoc.NewCaptureData' objects>, 'thumbnail': <attribute 'thumbnail' of 'renderdoc.NewCaptureData' objects>, 'api': <attribute 'api' of 'renderdoc.NewCaptureData' objects>, '__doc__': 'Information about the a new capture created by the target.'})"


