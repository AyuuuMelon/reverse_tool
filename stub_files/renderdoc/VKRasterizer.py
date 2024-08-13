# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .ShadingRateCombiner import ShadingRateCombiner

class VKRasterizer(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterizer state in the pipeline. """
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
    def conservativeRasterization(self):
        """The active conservative rasterization mode."""
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
    def depthBiasEnable(self):
        """Whether depth biasing is enabled."""
        pass

    @depthBiasEnable.setter
    def depthBiasEnable(self, value):
        pass

    @property
    def depthClampEnable(self):
        """
``True`` if pixels outside of the near and far depth planes should be clamped and
to ``0.0`` to ``1.0``.

"""
        pass

    @depthClampEnable.setter
    def depthClampEnable(self, value):
        pass

    @property
    def depthClipEnable(self):
        """
``True`` if pixels outside of the near and far depth planes should be clipped.

.. note::
  In Vulkan 1.0 this value was implicitly set to the opposite of :data:`depthClampEnable`, but with
  later extensions & versions it can be set independently.

"""
        pass

    @depthClipEnable.setter
    def depthClipEnable(self, value):
        pass

    @property
    def extraPrimitiveOverestimationSize(self):
        """
The extra size in pixels to increase primitives by during conservative rasterization,
in the x and y directions in screen space.

See :data:`conservativeRasterizationMode`

"""
        pass

    @extraPrimitiveOverestimationSize.setter
    def extraPrimitiveOverestimationSize(self, value):
        pass

    @property
    def fillMode(self):
        """The polygon :class:`FillMode`."""
        pass

    @fillMode.setter
    def fillMode(self, value):
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
    def lineStippleFactor(self):
        """The line stipple factor, or 0 if line stipple is disabled."""
        pass

    @lineStippleFactor.setter
    def lineStippleFactor(self, value):
        pass

    @property
    def lineStipplePattern(self):
        """The line stipple bit-pattern."""
        pass

    @lineStipplePattern.setter
    def lineStipplePattern(self, value):
        pass

    @property
    def lineWidth(self):
        """The fixed line width in pixels."""
        pass

    @lineWidth.setter
    def lineWidth(self, value):
        pass

    @property
    def pipelineShadingRate(self) -> Tuple[int,int]:
        """
The current pipeline fragment shading rate. This will always be 1x1 when a fragment
shading rate has not been specified.

:type: Tuple[int,int]

"""
        pass

    @pipelineShadingRate.setter
    def pipelineShadingRate(self, value: Tuple[int,int]):
        pass

    @property
    def provokingVertexFirst(self):
        """Whether the provoking vertex is the first one (default behaviour)."""
        pass

    @provokingVertexFirst.setter
    def provokingVertexFirst(self, value):
        pass

    @property
    def rasterizerDiscardEnable(self):
        """``True`` if primitives should be discarded during rasterization."""
        pass

    @rasterizerDiscardEnable.setter
    def rasterizerDiscardEnable(self, value):
        pass

    @property
    def shadingRateCombiners(self) -> Tuple[ShadingRateCombiner,ShadingRateCombiner]:
        """
The fragment shading rate combiners.

The combiners are applied as follows, according to the Vulkan spec:

  ``intermediateRate = combiner[0] ( pipelineShadingRate,  shaderExportedShadingRate )``
  ``finalRate        = combiner[1] ( intermediateRate,     imageBasedShadingRate     )``

Where the first input is from :data:`pipelineShadingRate` and the second is the exported shading
rate from the last pre-rasterization shader stage, which defaults to 1x1 if not exported.

The intermediate result is then used as the first input to the second combiner, together with the
shading rate sampled from the fragment shading rate attachment.

:type: Tuple[ShadingRateCombiner,ShadingRateCombiner]

"""
        pass

    @shadingRateCombiners.setter
    def shadingRateCombiners(self, value: Tuple[ShadingRateCombiner,ShadingRateCombiner]):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188516F0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKRasterizer' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKRasterizer' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKRasterizer' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKRasterizer' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKRasterizer' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKRasterizer' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKRasterizer' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKRasterizer' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.VKRasterizer' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.VKRasterizer' objects>, 'depthBiasClamp': <attribute 'depthBiasClamp' of 'renderdoc.VKRasterizer' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.VKRasterizer' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.VKRasterizer' objects>, 'lineStippleFactor': <attribute 'lineStippleFactor' of 'renderdoc.VKRasterizer' objects>, 'pipelineShadingRate': <attribute 'pipelineShadingRate' of 'renderdoc.VKRasterizer' objects>, 'lineStipplePattern': <attribute 'lineStipplePattern' of 'renderdoc.VKRasterizer' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKRasterizer' objects>, 'provokingVertexFirst': <attribute 'provokingVertexFirst' of 'renderdoc.VKRasterizer' objects>, 'shadingRateCombiners': <attribute 'shadingRateCombiners' of 'renderdoc.VKRasterizer' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.VKRasterizer' objects>, 'extraPrimitiveOverestimationSize': <attribute 'extraPrimitiveOverestimationSize' of 'renderdoc.VKRasterizer' objects>, 'depthBiasEnable': <attribute 'depthBiasEnable' of 'renderdoc.VKRasterizer' objects>, 'lineRasterMode': <attribute 'lineRasterMode' of 'renderdoc.VKRasterizer' objects>, 'depthClampEnable': <attribute 'depthClampEnable' of 'renderdoc.VKRasterizer' objects>, 'depthClipEnable': <attribute 'depthClipEnable' of 'renderdoc.VKRasterizer' objects>, 'rasterizerDiscardEnable': <attribute 'rasterizerDiscardEnable' of 'renderdoc.VKRasterizer' objects>, 'lineWidth': <attribute 'lineWidth' of 'renderdoc.VKRasterizer' objects>, 'conservativeRasterization': <attribute 'conservativeRasterization' of 'renderdoc.VKRasterizer' objects>, '__doc__': 'Describes the rasterizer state in the pipeline.'})"


