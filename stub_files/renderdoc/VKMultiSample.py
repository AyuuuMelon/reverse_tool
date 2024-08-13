# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKSampleLocations import VKSampleLocations

class VKMultiSample(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the multisampling state in the pipeline. """
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
    def minSampleShading(self):
        """The minimum sample shading rate."""
        pass

    @minSampleShading.setter
    def minSampleShading(self, value):
        pass

    @property
    def rasterSamples(self):
        """How many samples to use when rasterizing."""
        pass

    @rasterSamples.setter
    def rasterSamples(self, value):
        pass

    @property
    def sampleLocations(self) -> VKSampleLocations:
        """
The custom sample locations configuration.

:type: VKSampleLocations

"""
        pass

    @sampleLocations.setter
    def sampleLocations(self, value: VKSampleLocations):
        pass

    @property
    def sampleMask(self):
        """A mask that generated samples should be masked with using bitwise ``AND``."""
        pass

    @sampleMask.setter
    def sampleMask(self, value):
        pass

    @property
    def sampleShadingEnable(self):
        """``True`` if rendering should happen at sample-rate frequency."""
        pass

    @sampleShadingEnable.setter
    def sampleShadingEnable(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188B9C90>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKMultiSample' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKMultiSample' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKMultiSample' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKMultiSample' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKMultiSample' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKMultiSample' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKMultiSample' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKMultiSample' objects>, 'minSampleShading': <attribute 'minSampleShading' of 'renderdoc.VKMultiSample' objects>, 'rasterSamples': <attribute 'rasterSamples' of 'renderdoc.VKMultiSample' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKMultiSample' objects>, 'sampleShadingEnable': <attribute 'sampleShadingEnable' of 'renderdoc.VKMultiSample' objects>, 'sampleMask': <attribute 'sampleMask' of 'renderdoc.VKMultiSample' objects>, 'sampleLocations': <attribute 'sampleLocations' of 'renderdoc.VKMultiSample' objects>, '__doc__': 'Describes the multisampling state in the pipeline.'})"


