# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class BoundVBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Information about a single vertex or index buffer binding. """
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
    def byteOffset(self):
        """The offset in bytes from the start of the buffer to the data."""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def byteSize(self):
        """The size of the buffer binding, or 0xFFFFFFFF if the whole buffer is bound."""
        pass

    @byteSize.setter
    def byteSize(self, value):
        pass

    @property
    def byteStride(self):
        """The stride in bytes between the start of one element and the start of the next."""
        pass

    @byteStride.setter
    def byteStride(self, value):
        pass

    @property
    def resourceId(self):
        """A :class:`~renderdoc.ResourceId` identifying the buffer."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18854580>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.BoundVBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.BoundVBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.BoundVBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.BoundVBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.BoundVBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.BoundVBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.BoundVBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.BoundVBuffer' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.BoundVBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.BoundVBuffer' objects>, 'byteStride': <attribute 'byteStride' of 'renderdoc.BoundVBuffer' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.BoundVBuffer' objects>, 'byteSize': <attribute 'byteSize' of 'renderdoc.BoundVBuffer' objects>, '__doc__': 'Information about a single vertex or index buffer binding.'})"


