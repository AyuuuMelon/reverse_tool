# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKXFBBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a single transform feedback binding. """
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
    def active(self):
        """A flag indicating if this buffer is active or not."""
        pass

    @active.setter
    def active(self, value):
        pass

    @property
    def bufferResourceId(self):
        """The :class:`ResourceId` of the bound data buffer."""
        pass

    @bufferResourceId.setter
    def bufferResourceId(self, value):
        pass

    @property
    def byteOffset(self):
        """The offset in bytes to the start of the data in the :data:`bufferResourceId`."""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def byteSize(self):
        """The size in bytes of the data buffer."""
        pass

    @byteSize.setter
    def byteSize(self, value):
        pass

    @property
    def counterBufferOffset(self):
        """The offset in bytes to the counter in the :data:`counterBufferResourceId`."""
        pass

    @counterBufferOffset.setter
    def counterBufferOffset(self, value):
        pass

    @property
    def counterBufferResourceId(self):
        """The :class:`ResourceId` of the buffer storing the counter value (if set)."""
        pass

    @counterBufferResourceId.setter
    def counterBufferResourceId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18894440>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKXFBBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKXFBBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKXFBBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKXFBBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKXFBBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKXFBBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKXFBBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKXFBBuffer' objects>, 'active': <attribute 'active' of 'renderdoc.VKXFBBuffer' objects>, 'bufferResourceId': <attribute 'bufferResourceId' of 'renderdoc.VKXFBBuffer' objects>, 'counterBufferResourceId': <attribute 'counterBufferResourceId' of 'renderdoc.VKXFBBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKXFBBuffer' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.VKXFBBuffer' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.VKXFBBuffer' objects>, 'counterBufferOffset': <attribute 'counterBufferOffset' of 'renderdoc.VKXFBBuffer' objects>, '__doc__': 'Describes a single transform feedback binding.'})"


