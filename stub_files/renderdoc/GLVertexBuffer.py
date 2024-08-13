# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GLVertexBuffer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a single OpenGL vertex buffer binding. """
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
        """The byte offset from the start of the buffer to the beginning of the vertex data."""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def byteStride(self):
        """The byte stride between the start of one set of vertex data and the next."""
        pass

    @byteStride.setter
    def byteStride(self, value):
        pass

    @property
    def instanceDivisor(self):
        """
The instance rate divisor.

If this is ``0`` then the vertex buffer is read at vertex rate.

If it's ``1`` then one element is read for each instance, and for ``N`` greater than ``1`` then
``N`` instances read the same element before advancing.

"""
        pass

    @instanceDivisor.setter
    def instanceDivisor(self, value):
        pass

    @property
    def resourceId(self):
        """The :class:`ResourceId` of the buffer bound to this slot."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188A9960>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLVertexBuffer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLVertexBuffer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLVertexBuffer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLVertexBuffer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLVertexBuffer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLVertexBuffer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLVertexBuffer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLVertexBuffer' objects>, 'instanceDivisor': <attribute 'instanceDivisor' of 'renderdoc.GLVertexBuffer' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.GLVertexBuffer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLVertexBuffer' objects>, 'byteStride': <attribute 'byteStride' of 'renderdoc.GLVertexBuffer' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.GLVertexBuffer' objects>, '__doc__': 'Describes a single OpenGL vertex buffer binding.'})"


