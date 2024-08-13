# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ResourceFormat import ResourceFormat

class D3D12Layout(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes a single D3D12 input layout element for one vertex input.
    
    .. data:: TightlyPacked
    
      Value for :data:`byteOffset` that indicates this element is tightly packed.
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
    def byteOffset(self):
        """
The byte offset from the start of the vertex data in the vertex buffer from
:data:`inputSlot`.

If the value is :data:`TightlyPacked` then the element is packed tightly after the previous element, or 0
if this is the first element.

"""
        pass

    @byteOffset.setter
    def byteOffset(self, value):
        pass

    @property
    def format(self) -> ResourceFormat:
        """
The format describing how the input data is interpreted.

:type: ResourceFormat

"""
        pass

    @format.setter
    def format(self, value: ResourceFormat):
        pass

    @property
    def inputSlot(self):
        """The vertex buffer input slot where the data is sourced from."""
        pass

    @inputSlot.setter
    def inputSlot(self, value):
        pass

    @property
    def instanceDataStepRate(self):
        """
If :data:`perInstance` is ``True`` then this is how many times each instance data is
used before advancing to the next instance.

E.g. if this value is two, then two instances will be drawn with the first instance data, then two
with the next instance data.

"""
        pass

    @instanceDataStepRate.setter
    def instanceDataStepRate(self, value):
        pass

    @property
    def perInstance(self):
        """``True`` if the vertex data is instance-rate."""
        pass

    @perInstance.setter
    def perInstance(self, value):
        pass

    @property
    def semanticIndex(self):
        """The semantic index for this input."""
        pass

    @semanticIndex.setter
    def semanticIndex(self, value):
        pass

    @property
    def semanticName(self):
        """The semantic name for this input."""
        pass

    @semanticName.setter
    def semanticName(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    TightlyPacked = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'TightlyPacked': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1884C7D0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12Layout' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12Layout' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12Layout' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12Layout' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12Layout' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12Layout' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12Layout' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12Layout' objects>, 'semanticIndex': <attribute 'semanticIndex' of 'renderdoc.D3D12Layout' objects>, 'semanticName': <attribute 'semanticName' of 'renderdoc.D3D12Layout' objects>, 'instanceDataStepRate': <attribute 'instanceDataStepRate' of 'renderdoc.D3D12Layout' objects>, 'format': <attribute 'format' of 'renderdoc.D3D12Layout' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12Layout' objects>, 'inputSlot': <attribute 'inputSlot' of 'renderdoc.D3D12Layout' objects>, 'byteOffset': <attribute 'byteOffset' of 'renderdoc.D3D12Layout' objects>, 'perInstance': <attribute 'perInstance' of 'renderdoc.D3D12Layout' objects>, '__doc__': '\\nDescribes a single D3D12 input layout element for one vertex input.\\n\\n.. data:: TightlyPacked\\n\\n  Value for :data:`byteOffset` that indicates this element is tightly packed.\\n\\n'})"


