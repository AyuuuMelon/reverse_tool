# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKDescriptorSet import VKDescriptorSet

class VKPipeline(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the object and descriptor set bindings of a Vulkan pipeline object. """
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
    def descriptorSets(self) -> List[VKDescriptorSet]:
        """
The bound descriptor sets.

:type: List[VKDescriptorSet]

"""
        pass

    @descriptorSets.setter
    def descriptorSets(self, value: List[VKDescriptorSet]):
        pass

    @property
    def flags(self):
        """The flags used to create the pipeline object."""
        pass

    @flags.setter
    def flags(self, value):
        pass

    @property
    def pipelineComputeLayoutResourceId(self):
        """The :class:`ResourceId` of the compute pipeline layout object."""
        pass

    @pipelineComputeLayoutResourceId.setter
    def pipelineComputeLayoutResourceId(self, value):
        pass

    @property
    def pipelineFragmentLayoutResourceId(self):
        """
The :class:`ResourceId` of the fragment pipeline layout object.

When not using pipeline libraries, this will be identical to :data:`pipelinePreRastLayoutResourceId`.

"""
        pass

    @pipelineFragmentLayoutResourceId.setter
    def pipelineFragmentLayoutResourceId(self, value):
        pass

    @property
    def pipelinePreRastLayoutResourceId(self):
        """
The :class:`ResourceId` of the pre-rasterization pipeline layout object.

When not using pipeline libraries, this will be identical to :data:`pipelineFragmentLayoutResourceId`.

"""
        pass

    @pipelinePreRastLayoutResourceId.setter
    def pipelinePreRastLayoutResourceId(self, value):
        pass

    @property
    def pipelineResourceId(self):
        """The :class:`ResourceId` of the pipeline object."""
        pass

    @pipelineResourceId.setter
    def pipelineResourceId(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188C8F50>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKPipeline' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKPipeline' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKPipeline' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKPipeline' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKPipeline' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKPipeline' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKPipeline' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKPipeline' objects>, 'pipelineResourceId': <attribute 'pipelineResourceId' of 'renderdoc.VKPipeline' objects>, 'pipelineComputeLayoutResourceId': <attribute 'pipelineComputeLayoutResourceId' of 'renderdoc.VKPipeline' objects>, 'pipelinePreRastLayoutResourceId': <attribute 'pipelinePreRastLayoutResourceId' of 'renderdoc.VKPipeline' objects>, 'pipelineFragmentLayoutResourceId': <attribute 'pipelineFragmentLayoutResourceId' of 'renderdoc.VKPipeline' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKPipeline' objects>, 'flags': <attribute 'flags' of 'renderdoc.VKPipeline' objects>, 'descriptorSets': <attribute 'descriptorSets' of 'renderdoc.VKPipeline' objects>, '__doc__': 'Describes the object and descriptor set bindings of a Vulkan pipeline object.'})"


