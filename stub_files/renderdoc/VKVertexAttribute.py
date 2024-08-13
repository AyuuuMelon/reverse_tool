# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceFormat import ResourceFormat

class VKVertexAttribute(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the configuration of a single vertex attribute. """
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
    def binding(self):
        """The vertex binding where data will be sourced from."""
        pass

    @binding.setter
    def binding(self, value):
        pass

    @property
    def byteOffset(self):
        """The byte offset from the start of each vertex data in the :data:`binding` to this attribute."""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def format(self) -> ResourceFormat:
        """
The format describing how the input element is interpreted.

:type: ResourceFormat

"""
        pass

    @format.setter
    def format(self, value: ResourceFormat):
        pass

    @property
    def location(self):
        """The location in the shader that is bound to this attribute."""
        pass

    @location.setter
    def location(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188D1740>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKVertexAttribute' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKVertexAttribute' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKVertexAttribute' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKVertexAttribute' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKVertexAttribute' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKVertexAttribute' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKVertexAttribute' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKVertexAttribute' objects>, 'binding': <attribute 'binding' of 'renderdoc.VKVertexAttribute' objects>, 'location': <attribute 'location' of 'renderdoc.VKVertexAttribute' objects>, 'format': <attribute 'format' of 'renderdoc.VKVertexAttribute' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKVertexAttribute' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.VKVertexAttribute' objects>, '__doc__': 'Describes the configuration of a single vertex attribute.'})"


