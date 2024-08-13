# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderReflection import ShaderReflection

class VKShader(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a Vulkan shader stage. """
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
    def entryPoint(self):
        """The name of the entry point in the shader module that is used."""
        pass

    @entryPoint.setter
    def entryPoint(self, value):
        pass

    @property
    def pushConstantRangeByteOffset(self):
        """The byte offset into the push constant data that is visible to this shader."""
        pass

    @pushConstantRangeByteOffset.setter
    def pushConstantRangeByteOffset(self, value):
        pass

    @property
    def pushConstantRangeByteSize(self):
        """The number of bytes in the push constant data that is visible to this shader."""
        pass

    @pushConstantRangeByteSize.setter
    def pushConstantRangeByteSize(self, value):
        pass

    @property
    def reflection(self) -> ShaderReflection:
        """
The reflection data for this shader.

:type: ShaderReflection

"""
        pass

    @reflection.setter
    def reflection(self, value: ShaderReflection):
        pass

    @property
    def requiredSubgroupSize(self):
        """The required subgroup size specified for this shader at pipeline creation time."""
        pass

    @requiredSubgroupSize.setter
    def requiredSubgroupSize(self, value):
        pass

    @property
    def resourceId(self):
        """The :class:`ResourceId` of the shader module object."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    @property
    def shaderObject(self):
        """Whether the shader is a shader object or shader module."""
        pass

    @shaderObject.setter
    def shaderObject(self, value):
        pass

    @property
    def specializationData(self) -> bytes:
        """
The provided specialization constant data. Shader constants store the byte offset into
this buffer as their byteOffset. This data includes the applied specialization constants over the
top of the default values, so it is safe to read any constant from here and get the correct current
value.

:type: bytes

"""
        pass

    @specializationData.setter
    def specializationData(self, value: bytes):
        pass

    @property
    def specializationIds(self) -> List[int]:
        """
The specialization constant ID for each entry in the specialization constant block of
reflection info. This corresponds to the constantID in VkSpecializationMapEntry, while the offset
and size into specializationData can be obtained from the reflection info.

:type: List[int]

"""
        pass

    @specializationIds.setter
    def specializationIds(self, value: List[int]):
        pass

    @property
    def stage(self):
        """A :class:`ShaderStage` identifying which stage this shader is bound to."""
        pass

    @stage.setter
    def stage(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188CEE00>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKShader' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKShader' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKShader' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKShader' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKShader' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKShader' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKShader' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKShader' objects>, 'reflection': <attribute 'reflection' of 'renderdoc.VKShader' objects>, 'shaderObject': <attribute 'shaderObject' of 'renderdoc.VKShader' objects>, 'requiredSubgroupSize': <attribute 'requiredSubgroupSize' of 'renderdoc.VKShader' objects>, 'specializationData': <attribute 'specializationData' of 'renderdoc.VKShader' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.VKShader' objects>, 'stage': <attribute 'stage' of 'renderdoc.VKShader' objects>, 'entryPoint': <attribute 'entryPoint' of 'renderdoc.VKShader' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKShader' objects>, 'pushConstantRangeByteOffset': <attribute 'pushConstantRangeByteOffset' of 'renderdoc.VKShader' objects>, 'pushConstantRangeByteSize': <attribute 'pushConstantRangeByteSize' of 'renderdoc.VKShader' objects>, 'specializationIds': <attribute 'specializationIds' of 'renderdoc.VKShader' objects>, '__doc__': 'Describes a Vulkan shader stage.'})"


