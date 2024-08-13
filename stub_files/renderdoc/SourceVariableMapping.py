# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .DebugVariableReference import DebugVariableReference

class SourceVariableMapping(): # skipped bases: <class 'SwigPyObject'>
    """
    Maps the contents of a high-level source variable to one or more shader variables in a
    :class:`ShaderDebugState`, with type information.
    
    A single high-level variable may be represented by multiple mappings but only along regular
    boundaries, typically whole vectors. For example an array may have each element in a different
    mapping, or a matrix may have a mapping per row. The properties such as :data:`rows` and
    :data:`elements` reflect the *parent* object.
    
    .. note::
    
      There is not necessarily a 1:1 mapping from source variable to debug variable, so this can change
      over time.
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
    def columns(self):
        """The number of columns in this variable."""
        pass

    @columns.setter
    def columns(self, value):
        pass

    @property
    def name(self):
        """The name and member of this source variable that's being mapped from."""
        pass

    @name.setter
    def name(self, value):
        pass

    @property
    def offset(self):
        """The offset in the parent source variable, for struct members. Useful for sorting."""
        pass

    @offset.setter
    def offset(self, value):
        pass

    @property
    def rows(self):
        """The number of rows in this variable - 1 for vectors, >1 for matrices."""
        pass

    @rows.setter
    def rows(self, value):
        pass

    @property
    def signatureIndex(self):
        """
The index in the input or output signature of the shader that this variable represents.

The type of signature can be disambiguated by the debug variables referenced - inputs are stored
separately.

This will be set to -1 if the variable is not part of either signature.

"""
        pass

    @signatureIndex.setter
    def signatureIndex(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self):
        """The variable type of the source being mapped from, if the debug variable is untyped."""
        pass

    @type.setter
    def type(self, value):
        pass

    @property
    def variables(self) -> List[DebugVariableReference]:
        """
The debug variables that the components of this high level variable map to. Multiple
ranges could refer to the same variable if a contiguous range is mapped to - the mapping is
component-by-component to greatly simplify algorithms at the expense of a small amount of storage
space.

:type: List[DebugVariableReference]

"""
        pass

    @variables.setter
    def variables(self, value: List[DebugVariableReference]):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18890010>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.SourceVariableMapping' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.SourceVariableMapping' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.SourceVariableMapping' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.SourceVariableMapping' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.SourceVariableMapping' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.SourceVariableMapping' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.SourceVariableMapping' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.SourceVariableMapping' objects>, 'signatureIndex': <attribute 'signatureIndex' of 'renderdoc.SourceVariableMapping' objects>, 'name': <attribute 'name' of 'renderdoc.SourceVariableMapping' objects>, 'rows': <attribute 'rows' of 'renderdoc.SourceVariableMapping' objects>, 'variables': <attribute 'variables' of 'renderdoc.SourceVariableMapping' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.SourceVariableMapping' objects>, 'offset': <attribute 'offset' of 'renderdoc.SourceVariableMapping' objects>, 'type': <attribute 'type' of 'renderdoc.SourceVariableMapping' objects>, 'columns': <attribute 'columns' of 'renderdoc.SourceVariableMapping' objects>, '__doc__': '\\nMaps the contents of a high-level source variable to one or more shader variables in a\\n:class:`ShaderDebugState`, with type information.\\n\\nA single high-level variable may be represented by multiple mappings but only along regular\\nboundaries, typically whole vectors. For example an array may have each element in a different\\nmapping, or a matrix may have a mapping per row. The properties such as :data:`rows` and\\n:data:`elements` reflect the *parent* object.\\n\\n.. note::\\n\\n  There is not necessarily a 1:1 mapping from source variable to debug variable, so this can change\\n  over time.\\n\\n'})"


