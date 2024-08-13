# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D11StreamOutBind import D3D11StreamOutBind

class D3D11StreamOut(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes the stream-out stage bindings.
    
    .. data:: NoRasterization
    
      Value for :data:`rasterizedStream` that indicates no stream is being rasterized.
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
    def outputs(self) -> List[D3D11StreamOutBind]:
        """
The bound stream-out buffer bindings.

:type: List[D3D11StreamOutBind]

"""
        pass

    @outputs.setter
    def outputs(self, value: List[D3D11StreamOutBind]):
        pass

    @property
    def rasterizedStream(self) -> int:
        """
Which stream-out stream is being used for rasterization.

If the value is :data:`NoRasterization` then no stream has been selected for rasterization.

:type: int

"""
        pass

    @rasterizedStream.setter
    def rasterizedStream(self, value: int):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    NoRasterization = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoRasterization': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188994C0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11StreamOut' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11StreamOut' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11StreamOut' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11StreamOut' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11StreamOut' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11StreamOut' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11StreamOut' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11StreamOut' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11StreamOut' objects>, 'rasterizedStream': <attribute 'rasterizedStream' of 'renderdoc.D3D11StreamOut' objects>, 'outputs': <attribute 'outputs' of 'renderdoc.D3D11StreamOut' objects>, '__doc__': '\\nDescribes the stream-out stage bindings.\\n\\n.. data:: NoRasterization\\n\\n  Value for :data:`rasterizedStream` that indicates no stream is being rasterized.\\n\\n'})"


