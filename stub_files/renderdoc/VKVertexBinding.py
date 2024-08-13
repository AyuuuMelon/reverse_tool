# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class VKVertexBinding(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a vertex binding. """
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
    def instanceDivisor(self):
        """
The instance rate divisor.

If this is ``0`` then every vertex gets the same value.

If it's ``1`` then one element is read for each instance, and for ``N`` greater than ``1`` then
``N`` instances read the same element before advancing.

"""
        pass

    @instanceDivisor.setter
    def instanceDivisor(self, value):
        pass

    @property
    def perInstance(self):
        """``True`` if the vertex data is instance-rate."""
        pass

    @perInstance.setter
    def perInstance(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vertexBufferBinding(self):
        """The vertex binding where data will be sourced from."""
        pass

    @vertexBufferBinding.setter
    def vertexBufferBinding(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18883260>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKVertexBinding' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKVertexBinding' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKVertexBinding' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKVertexBinding' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKVertexBinding' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKVertexBinding' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKVertexBinding' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKVertexBinding' objects>, 'vertexBufferBinding': <attribute 'vertexBufferBinding' of 'renderdoc.VKVertexBinding' objects>, 'instanceDivisor': <attribute 'instanceDivisor' of 'renderdoc.VKVertexBinding' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKVertexBinding' objects>, 'perInstance': <attribute 'perInstance' of 'renderdoc.VKVertexBinding' objects>, '__doc__': 'Describes a vertex binding.'})"


