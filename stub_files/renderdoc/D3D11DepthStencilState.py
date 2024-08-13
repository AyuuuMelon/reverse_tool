# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .StencilFace import StencilFace

class D3D11DepthStencilState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a depth-stencil state object. """
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
    def depthEnable(self):
        """``True`` if depth testing should be performed."""
        pass

    @depthEnable.setter
    def depthEnable(self, value):
        pass

    @property
    def depthFunction(self):
        """The :class:`CompareFunction` to use for testing depth values."""
        pass

    @depthFunction.setter
    def depthFunction(self, value):
        pass

    @property
    def depthWrites(self):
        """``True`` if depth values should be written to the depth target."""
        pass

    @depthWrites.setter
    def depthWrites(self, value):
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
    def resourceId(self):
        """The :class:`ResourceId` of the depth-stencil state object."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    @property
    def stencilEnable(self):
        """``True`` if stencil operations should be performed."""
        pass

    @stencilEnable.setter
    def stencilEnable(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18879A20>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11DepthStencilState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11DepthStencilState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11DepthStencilState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11DepthStencilState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11DepthStencilState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11DepthStencilState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11DepthStencilState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11DepthStencilState' objects>, 'frontFace': <attribute 'frontFace' of 'renderdoc.D3D11DepthStencilState' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D11DepthStencilState' objects>, 'backFace': <attribute 'backFace' of 'renderdoc.D3D11DepthStencilState' objects>, 'depthFunction': <attribute 'depthFunction' of 'renderdoc.D3D11DepthStencilState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11DepthStencilState' objects>, 'depthEnable': <attribute 'depthEnable' of 'renderdoc.D3D11DepthStencilState' objects>, 'depthWrites': <attribute 'depthWrites' of 'renderdoc.D3D11DepthStencilState' objects>, 'stencilEnable': <attribute 'stencilEnable' of 'renderdoc.D3D11DepthStencilState' objects>, '__doc__': 'Describes a depth-stencil state object.'})"


