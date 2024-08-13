# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .StencilFace import StencilFace

class VKDepthStencil(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the pipeline depth-stencil state. """
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
    def backFace(self) -> StencilFace:
        """
The stencil state for back-facing polygons.

:type: StencilFace

"""
        pass

    @backFace.setter
    def backFace(self, value: StencilFace):
        pass

    @property
    def depthBoundsEnable(self):
        """``True`` if depth bounds tests should be applied."""
        pass

    @depthBoundsEnable.setter
    def depthBoundsEnable(self, value):
        pass

    @property
    def depthFunction(self):
        """The :class:`CompareFunction` to use for testing depth values."""
        pass

    @depthFunction.setter
    def depthFunction(self, value):
        pass

    @property
    def depthTestEnable(self):
        """``True`` if depth testing should be performed."""
        pass

    @depthTestEnable.setter
    def depthTestEnable(self, value):
        pass

    @property
    def depthWriteEnable(self):
        """``True`` if depth values should be written to the depth target."""
        pass

    @depthWriteEnable.setter
    def depthWriteEnable(self, value):
        pass

    @property
    def frontFace(self) -> StencilFace:
        """
The stencil state for front-facing polygons.

:type: StencilFace

"""
        pass

    @frontFace.setter
    def frontFace(self, value: StencilFace):
        pass

    @property
    def maxDepthBounds(self):
        """The far plane bounding value."""
        pass

    @maxDepthBounds.setter
    def maxDepthBounds(self, value):
        pass

    @property
    def minDepthBounds(self):
        """The near plane bounding value."""
        pass

    @minDepthBounds.setter
    def minDepthBounds(self, value):
        pass

    @property
    def stencilTestEnable(self):
        """``True`` if stencil operations should be performed."""
        pass

    @stencilTestEnable.setter
    def stencilTestEnable(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1886E800>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKDepthStencil' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKDepthStencil' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKDepthStencil' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKDepthStencil' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKDepthStencil' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKDepthStencil' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKDepthStencil' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKDepthStencil' objects>, 'frontFace': <attribute 'frontFace' of 'renderdoc.VKDepthStencil' objects>, 'backFace': <attribute 'backFace' of 'renderdoc.VKDepthStencil' objects>, 'depthFunction': <attribute 'depthFunction' of 'renderdoc.VKDepthStencil' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKDepthStencil' objects>, 'depthWriteEnable': <attribute 'depthWriteEnable' of 'renderdoc.VKDepthStencil' objects>, 'depthBoundsEnable': <attribute 'depthBoundsEnable' of 'renderdoc.VKDepthStencil' objects>, 'minDepthBounds': <attribute 'minDepthBounds' of 'renderdoc.VKDepthStencil' objects>, 'maxDepthBounds': <attribute 'maxDepthBounds' of 'renderdoc.VKDepthStencil' objects>, 'depthTestEnable': <attribute 'depthTestEnable' of 'renderdoc.VKDepthStencil' objects>, 'stencilTestEnable': <attribute 'stencilTestEnable' of 'renderdoc.VKDepthStencil' objects>, '__doc__': 'Describes the pipeline depth-stencil state.'})"


