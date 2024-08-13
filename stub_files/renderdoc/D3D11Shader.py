# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShaderReflection import ShaderReflection

class D3D11Shader(): # skipped bases: <class 'SwigPyObject'>
    """ Describes a D3D11 shader stage. """
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
    def classInstances(self) -> List[str]:
        """
The bound class instance names.

:type: List[str]

"""
        pass

    @classInstances.setter
    def classInstances(self, value: List[str]):
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
    def resourceId(self):
        """The :class:`ResourceId` of the shader itself."""
        pass

    @resourceId.setter
    def resourceId(self, value):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18858BF0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D11Shader' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D11Shader' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D11Shader' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D11Shader' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D11Shader' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D11Shader' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D11Shader' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D11Shader' objects>, 'reflection': <attribute 'reflection' of 'renderdoc.D3D11Shader' objects>, 'classInstances': <attribute 'classInstances' of 'renderdoc.D3D11Shader' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D11Shader' objects>, 'stage': <attribute 'stage' of 'renderdoc.D3D11Shader' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D11Shader' objects>, '__doc__': 'Describes a D3D11 shader stage.'})"


