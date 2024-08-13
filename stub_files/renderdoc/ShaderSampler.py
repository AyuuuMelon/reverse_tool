# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ShaderSampler(): # skipped bases: <class 'SwigPyObject'>
    """
    Contains the information for a separate sampler in a shader. If the API doesn't have
    the concept of separate samplers, this struct will be unused and only :class:`ShaderResource` is
    relevant.
    
    .. note:: that constant blocks will not have a shader resource entry, see :class:`ConstantBlock`.
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
    def bindArraySize(self) -> int:
        """
If this binding is natively arrayed, how large is the array size. If not arrayed, this
will be set to 1.

This value may be set to a very large number if the array is unbounded in the shader.

:type: int

"""
        pass

    @bindArraySize.setter
    def bindArraySize(self, value: int):
        pass

    @property
    def fixedBindNumber(self) -> int:
        """
The fixed binding number for this binding. The interpretation of this is API-specific
and it is provided purely for informational purposes and has no bearing on how data is accessed or
described. Similarly some bindings don't have a fixed bind number and the value here should not be
relied on.

For OpenGL only, this value is not used as bindings are dynamic and cannot be determined by the
shader reflection. Bindings must be determined only by the descriptor mapped to.

Generally speaking sorting by this number will give a reasonable ordering by binding if it exists.

.. note::
  Because this number is API-specific, there is no guarantee that it will be unique across all
  resources, though generally it will be unique within all binds of the same type. It should be used
  only within contexts that can interpret it API-specifically, or else for purely
  informational/non-semantic purposes like sorting.

:type: int

"""
        pass

    @fixedBindNumber.setter
    def fixedBindNumber(self, value: int):
        pass

    @property
    def fixedBindSetOrSpace(self) -> int:
        """
The fixed binding set or space for this binding. This is API-specific, on Vulkan this
gives the set and on D3D12 this gives the register space.
It is provided purely for informational purposes and has no bearing on how data is accessed or
described.

Generally speaking sorting by this number before :data:`fixedBindNumber` will give a reasonable
ordering by binding if it exists.

:type: int

"""
        pass

    @fixedBindSetOrSpace.setter
    def fixedBindSetOrSpace(self, value: int):
        pass

    @property
    def name(self):
        """The name of this sampler."""
        pass

    @name.setter
    def name(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is 'mappingproxy({\'this\': <attribute \'this\' of \'SwigPyObject\' objects>, \'thisown\': <attribute \'thisown\' of \'SwigPyObject\' objects>, \'__new__\': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188A4930>, \'__hash__\': <slot wrapper \'__hash__\' of \'renderdoc.ShaderSampler\' objects>, \'__lt__\': <slot wrapper \'__lt__\' of \'renderdoc.ShaderSampler\' objects>, \'__le__\': <slot wrapper \'__le__\' of \'renderdoc.ShaderSampler\' objects>, \'__eq__\': <slot wrapper \'__eq__\' of \'renderdoc.ShaderSampler\' objects>, \'__ne__\': <slot wrapper \'__ne__\' of \'renderdoc.ShaderSampler\' objects>, \'__gt__\': <slot wrapper \'__gt__\' of \'renderdoc.ShaderSampler\' objects>, \'__ge__\': <slot wrapper \'__ge__\' of \'renderdoc.ShaderSampler\' objects>, \'__init__\': <slot wrapper \'__init__\' of \'renderdoc.ShaderSampler\' objects>, \'bindArraySize\': <attribute \'bindArraySize\' of \'renderdoc.ShaderSampler\' objects>, \'name\': <attribute \'name\' of \'renderdoc.ShaderSampler\' objects>, \'fixedBindNumber\': <attribute \'fixedBindNumber\' of \'renderdoc.ShaderSampler\' objects>, \'__dict__\': <attribute \'__dict__\' of \'renderdoc.ShaderSampler\' objects>, \'fixedBindSetOrSpace\': <attribute \'fixedBindSetOrSpace\' of \'renderdoc.ShaderSampler\' objects>, \'__doc__\': "\\nContains the information for a separate sampler in a shader. If the API doesn\'t have\\nthe concept of separate samplers, this struct will be unused and only :class:`ShaderResource` is\\nrelevant.\\n\\n.. note:: that constant blocks will not have a shader resource entry, see :class:`ConstantBlock`.\\n\\n"})'


