# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShadingRateCombiner import ShadingRateCombiner
from .ResourceId import ResourceId

class D3D12RasterizerState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterizer state in the PSO. """
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
    def baseShadingRate(self) -> Tuple[int,int]:
        """
The current base variable shading rate. This will always be 1x1 when variable shading
is disabled.

:type: Tuple[int,int]

"""
        pass

    @baseShadingRate.setter
    def baseShadingRate(self, value: Tuple[int,int]):
        pass

    @property
    def conservativeRasterization(self):
        """The current :class:`ConservativeRaster` mode."""
        pass

    @conservativeRasterization.setter
    def conservativeRasterization(self, value):
        pass

    @property
    def cullMode(self):
        """The polygon :class:`CullMode`."""
        pass

    @cullMode.setter
    def cullMode(self, value):
        pass

    @property
    def depthBias(self):
        """The fixed depth bias value to apply to z-values."""
        pass

    @depthBias.setter
    def depthBias(self, value):
        pass

    @property
    def depthBiasClamp(self):
        """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

"""
        pass

    @depthBiasClamp.setter
    def depthBiasClamp(self, value):
        pass

    @property
    def depthClip(self):
        """``True`` if pixels outside of the near and far depth planes should be clipped."""
        pass

    @depthClip.setter
    def depthClip(self, value):
        pass

    @property
    def fillMode(self):
        """The polygon :class:`FillMode`."""
        pass

    @fillMode.setter
    def fillMode(self, value):
        pass

    @property
    def forcedSampleCount(self):
        """
A sample count to force rasterization to when UAV rendering or rasterizing, or 0 to
not force any sample count.

"""
        pass

    @forcedSampleCount.setter
    def forcedSampleCount(self, value):
        pass

    @property
    def frontCCW(self):
        """
``True`` if counter-clockwise polygons are front-facing.
``False`` if clockwise polygons are front-facing.

"""
        pass

    @frontCCW.setter
    def frontCCW(self, value):
        pass

    @property
    def lineRasterMode(self):
        """The line rasterization mode."""
        pass

    @lineRasterMode.setter
    def lineRasterMode(self, value):
        pass

    @property
    def shadingRateCombiners(self) -> Tuple[ShadingRateCombiner,ShadingRateCombiner]:
        """
The shading rate combiners.

The combiners are applied as follows, according to the D3D spec:

  ``intermediateRate = combiner[0] ( baseShadingRate,  shaderExportedShadingRate )``
  ``finalRate        = combiner[1] ( intermediateRate, imageBasedShadingRate     )``

Where the first input is from :data:`baseShadingRate` and the second is the exported shading rate
from a vertex or geometry shader, which defaults to 1x1 if not exported.

The intermediate result is then used as the first input to the second combiner, together with the
shading rate sampled from the shading rate image.

:type: Tuple[ShadingRateCombiner,ShadingRateCombiner]

"""
        pass

    @shadingRateCombiners.setter
    def shadingRateCombiners(self, value: Tuple[ShadingRateCombiner,ShadingRateCombiner]):
        pass

    @property
    def shadingRateImage(self) -> ResourceId:
        """
The image bound as a shading rate image.

:type: ResourceId

"""
        pass

    @shadingRateImage.setter
    def shadingRateImage(self, value: ResourceId):
        pass

    @property
    def slopeScaledDepthBias(self):
        """The slope-scaled depth bias value to apply to z-values."""
        pass

    @slopeScaledDepthBias.setter
    def slopeScaledDepthBias(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18887B40>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12RasterizerState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12RasterizerState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12RasterizerState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12RasterizerState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12RasterizerState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12RasterizerState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12RasterizerState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12RasterizerState' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.D3D12RasterizerState' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.D3D12RasterizerState' objects>, 'depthBiasClamp': <attribute 'depthBiasClamp' of 'renderdoc.D3D12RasterizerState' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.D3D12RasterizerState' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.D3D12RasterizerState' objects>, 'depthClip': <attribute 'depthClip' of 'renderdoc.D3D12RasterizerState' objects>, 'baseShadingRate': <attribute 'baseShadingRate' of 'renderdoc.D3D12RasterizerState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12RasterizerState' objects>, 'shadingRateCombiners': <attribute 'shadingRateCombiners' of 'renderdoc.D3D12RasterizerState' objects>, 'shadingRateImage': <attribute 'shadingRateImage' of 'renderdoc.D3D12RasterizerState' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.D3D12RasterizerState' objects>, 'forcedSampleCount': <attribute 'forcedSampleCount' of 'renderdoc.D3D12RasterizerState' objects>, 'lineRasterMode': <attribute 'lineRasterMode' of 'renderdoc.D3D12RasterizerState' objects>, 'conservativeRasterization': <attribute 'conservativeRasterization' of 'renderdoc.D3D12RasterizerState' objects>, '__doc__': 'Describes the rasterizer state in the PSO.'})"


