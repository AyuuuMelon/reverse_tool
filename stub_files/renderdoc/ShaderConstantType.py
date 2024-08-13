# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderVariableFlags import ShaderVariableFlags
from .ShaderConstant import ShaderConstant

class ShaderConstantType(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the type and members of a :class:`ShaderConstant`. """
    def ColMajor(self) -> bool: # real signature unknown; restored from __doc__
        """
        ColMajor()
        
        Helper function for checking if :data:`flags` *does not* have
        :data:`ShaderVariableFlags.RowMajorMatrix` set. This is entirely equivalent to checking that flag
        manually, but since it is common this helper is provided.
        
        .. note::
          Vectors and scalars will be marked as row-major by convention for convenience.
        
        :return: If the storage is column-major order in memory
        :rtype: bool
        """
        pass

    def RowMajor(self) -> bool: # real signature unknown; restored from __doc__
        """
        RowMajor()
        
        Helper function for checking if :data:`flags` has
        :data:`ShaderVariableFlags.RowMajorMatrix` set. This is entirely equivalent to checking that flag
        manually, but since it is common this helper is provided.
        
        .. note::
          Vectors and scalars will be marked as row-major by convention for convenience.
        
        :return: If the storage is row-major order in memory
        :rtype: bool
        """
        pass

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
    def arrayByteStride(self):
        """The number of bytes between the start of one element in the array and the next."""
        pass

    @arrayByteStride.setter
    def arrayByteStride(self, value):
        pass

    @property
    def baseType(self):
        """The base :class:`VarType` of this constant."""
        pass

    @baseType.setter
    def baseType(self, value):
        pass

    @property
    def columns(self):
        """The number of columns in this matrix."""
        pass

    @columns.setter
    def columns(self, value):
        pass

    @property
    def elements(self):
        """The number of elements in the array, or 1 if it's not an array."""
        pass

    @elements.setter
    def elements(self, value):
        pass

    @property
    def flags(self) -> ShaderVariableFlags:
        """
The flags controlling how this constant is interpreted and displayed.

:type: ShaderVariableFlags

"""
        pass

    @flags.setter
    def flags(self, value: ShaderVariableFlags):
        pass

    @property
    def matrixByteStride(self):
        """The number of bytes between the start of one column/row in a matrix and the next."""
        pass

    @matrixByteStride.setter
    def matrixByteStride(self, value):
        pass

    @property
    def members(self) -> List[ShaderConstant]:
        """
Any members that this constant may contain.

:type: List[ShaderConstant]

"""
        pass

    @members.setter
    def members(self, value: List[ShaderConstant]):
        pass

    @property
    def name(self):
        """The name of the type of this constant, e.g. a ``struct`` name."""
        pass

    @name.setter
    def name(self, value):
        pass

    @property
    def pointerTypeID(self):
        """The index in :data:`ShaderReflection.pointerTypes` of the pointee type."""
        pass

    @pointerTypeID.setter
    def pointerTypeID(self, value):
        pass

    @property
    def rows(self):
        """The number of rows in this matrix."""
        pass

    @rows.setter
    def rows(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188A9040>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ShaderConstantType' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ShaderConstantType' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ShaderConstantType' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ShaderConstantType' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ShaderConstantType' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ShaderConstantType' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ShaderConstantType' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ShaderConstantType' objects>, 'RowMajor': <method 'RowMajor' of 'renderdoc.ShaderConstantType' objects>, 'ColMajor': <method 'ColMajor' of 'renderdoc.ShaderConstantType' objects>, 'baseType': <attribute 'baseType' of 'renderdoc.ShaderConstantType' objects>, 'name': <attribute 'name' of 'renderdoc.ShaderConstantType' objects>, 'members': <attribute 'members' of 'renderdoc.ShaderConstantType' objects>, 'rows': <attribute 'rows' of 'renderdoc.ShaderConstantType' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.ShaderConstantType' objects>, 'elements': <attribute 'elements' of 'renderdoc.ShaderConstantType' objects>, 'arrayByteStride': <attribute 'arrayByteStride' of 'renderdoc.ShaderConstantType' objects>, 'matrixByteStride': <attribute 'matrixByteStride' of 'renderdoc.ShaderConstantType' objects>, 'flags': <attribute 'flags' of 'renderdoc.ShaderConstantType' objects>, 'pointerTypeID': <attribute 'pointerTypeID' of 'renderdoc.ShaderConstantType' objects>, 'columns': <attribute 'columns' of 'renderdoc.ShaderConstantType' objects>, '__doc__': 'Describes the type and members of a :class:`ShaderConstant`.'})"


