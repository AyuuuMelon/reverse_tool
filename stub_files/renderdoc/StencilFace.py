# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class StencilFace(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the details of a stencil operation. """
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
    def compareMask(self):
        """The mask for testing stencil values."""
        pass

    @compareMask.setter
    def compareMask(self, value):
        pass

    @property
    def depthFailOperation(self):
        """the :class:`StencilOperation` to apply if the depth-test fails."""
        pass

    @depthFailOperation.setter
    def depthFailOperation(self, value):
        pass

    @property
    def failOperation(self):
        """The :class:`StencilOperation` to apply if the stencil-test fails."""
        pass

    @failOperation.setter
    def failOperation(self, value):
        pass

    @property
    def function(self):
        """the :class:`CompareFunction` to use for testing stencil values."""
        pass

    @function.setter
    def function(self, value):
        pass

    @property
    def passOperation(self):
        """the :class:`StencilOperation` to apply if the stencil-test passes."""
        pass

    @passOperation.setter
    def passOperation(self, value):
        pass

    @property
    def reference(self):
        """The current stencil reference value."""
        pass

    @reference.setter
    def reference(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def writeMask(self):
        """The mask for writing stencil values."""
        pass

    @writeMask.setter
    def writeMask(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18889950>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.StencilFace' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.StencilFace' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.StencilFace' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.StencilFace' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.StencilFace' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.StencilFace' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.StencilFace' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.StencilFace' objects>, 'reference': <attribute 'reference' of 'renderdoc.StencilFace' objects>, 'function': <attribute 'function' of 'renderdoc.StencilFace' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.StencilFace' objects>, 'compareMask': <attribute 'compareMask' of 'renderdoc.StencilFace' objects>, 'writeMask': <attribute 'writeMask' of 'renderdoc.StencilFace' objects>, 'failOperation': <attribute 'failOperation' of 'renderdoc.StencilFace' objects>, 'depthFailOperation': <attribute 'depthFailOperation' of 'renderdoc.StencilFace' objects>, 'passOperation': <attribute 'passOperation' of 'renderdoc.StencilFace' objects>, '__doc__': 'Describes the details of a stencil operation.'})"


