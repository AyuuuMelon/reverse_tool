# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class SigParameter(): # skipped bases: <class 'SwigPyObject'>
    """
    The information describing an input or output signature element describing the interface
    between shader stages.
    
    .. data:: NoIndex
    
      Value for an index that means it is invalid or not applicable for this parameter.
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
    def channelUsedMask(self):
        """
A bitmask indicating which components in the shader register are actually used by the
shader itself, for APIs that pack signatures together.

"""
        pass

    @channelUsedMask.setter
    def channelUsedMask(self, value):
        pass

    @property
    def compCount(self):
        """The number of components used to store this element. See :data:`varType`."""
        pass

    @compCount.setter
    def compCount(self, value):
        pass

    @property
    def needSemanticIndex(self):
        """A convenience flag - ``True`` if the semantic name is unique and no index is needed."""
        pass

    @needSemanticIndex.setter
    def needSemanticIndex(self, value):
        pass

    @property
    def perPrimitiveRate(self):
        """A flag indicating if this parameter is output at per-primitive rate rather than per-vertex."""
        pass

    @perPrimitiveRate.setter
    def perPrimitiveRate(self, value):
        pass

    @property
    def regChannelMask(self):
        """
A bitmask indicating which components in the shader register are stored, for APIs that
pack signatures together.

"""
        pass

    @regChannelMask.setter
    def regChannelMask(self, value):
        pass

    @property
    def regIndex(self):
        """
The index of the shader register/binding used to store this signature element.

This may be :data:`NoIndex` if the element is system-generated and not consumed by another shader
stage. See :data:`systemValue`.

"""
        pass

    @regIndex.setter
    def regIndex(self, value):
        pass

    @property
    def semanticIdxName(self):
        """The combined semantic name and index."""
        pass

    @semanticIdxName.setter
    def semanticIdxName(self, value):
        pass

    @property
    def semanticIndex(self):
        """The semantic index of this variable - see :data:`semanticName`."""
        pass

    @semanticIndex.setter
    def semanticIndex(self, value):
        pass

    @property
    def semanticName(self):
        """The semantic name of this variable, if the API uses semantic matching for bindings."""
        pass

    @semanticName.setter
    def semanticName(self, value):
        pass

    @property
    def stream(self):
        """Selects a stream for APIs that provide multiple output streams for the same named output."""
        pass

    @stream.setter
    def stream(self, value):
        pass

    @property
    def systemValue(self):
        """The :class:`ShaderBuiltin` value that this element contains."""
        pass

    @systemValue.setter
    def systemValue(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def varName(self):
        """The name of this variable - may not be present in the metadata for all APIs."""
        pass

    @varName.setter
    def varName(self, value):
        pass

    @property
    def varType(self):
        """The :class:`variable type <VarType>` of data that this element stores."""
        pass

    @varType.setter
    def varType(self, value):
        pass


    NoIndex = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoIndex': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188C2A80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SigParameter' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SigParameter' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SigParameter' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SigParameter' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SigParameter' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SigParameter' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SigParameter' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SigParameter' objects>, 'semanticIndex': <attribute 'semanticIndex' of 'renderdoc.SigParameter' objects>, 'needSemanticIndex': <attribute 'needSemanticIndex' of 'renderdoc.SigParameter' objects>, 'channelUsedMask': <attribute 'channelUsedMask' of 'renderdoc.SigParameter' objects>, 'compCount': <attribute 'compCount' of 'renderdoc.SigParameter' objects>, 'perPrimitiveRate': <attribute 'perPrimitiveRate' of 'renderdoc.SigParameter' objects>, 'semanticName': <attribute 'semanticName' of 'renderdoc.SigParameter' objects>, 'stream': <attribute 'stream' of 'renderdoc.SigParameter' objects>, 'regChannelMask': <attribute 'regChannelMask' of 'renderdoc.SigParameter' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SigParameter' objects>, 'varName': <attribute 'varName' of 'renderdoc.SigParameter' objects>, 'systemValue': <attribute 'systemValue' of 'renderdoc.SigParameter' objects>, 'regIndex': <attribute 'regIndex' of 'renderdoc.SigParameter' objects>, 'semanticIdxName': <attribute 'semanticIdxName' of 'renderdoc.SigParameter' objects>, 'varType': <attribute 'varType' of 'renderdoc.SigParameter' objects>, '__doc__': '\\nThe information describing an input or output signature element describing the interface\\nbetween shader stages.\\n\\n.. data:: NoIndex\\n\\n  Value for an index that means it is invalid or not applicable for this parameter.\\n\\n'})"


