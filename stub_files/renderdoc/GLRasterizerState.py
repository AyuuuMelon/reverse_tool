# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GLRasterizerState(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the rasterizer state toggles. """
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
    def alphaToCoverage(self):
        """``True`` if alpha-to-coverage should be used when blending to an MSAA target."""
        pass

    @alphaToCoverage.setter
    def alphaToCoverage(self, value):
        pass

    @property
    def alphaToOne(self):
        """``True`` if alpha-to-one should be used when blending to an MSAA target."""
        pass

    @alphaToOne.setter
    def alphaToOne(self, value):
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
    def depthClamp(self):
        """
``True`` if pixels outside of the near and far depth planes should be clamped and
to ``0.0`` to ``1.0`` and not clipped.

"""
        pass

    @depthClamp.setter
    def depthClamp(self, value):
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
    def lineWidth(self):
        """The fixed line width in pixels."""
        pass

    @lineWidth.setter
    def lineWidth(self, value):
        pass

    @property
    def minSampleShadingRate(self):
        """The minimum sample shading rate."""
        pass

    @minSampleShadingRate.setter
    def minSampleShadingRate(self, value):
        pass

    @property
    def multisampleEnable(self):
        """``True`` if multisampling should be used during rendering."""
        pass

    @multisampleEnable.setter
    def multisampleEnable(self, value):
        pass

    @property
    def offsetClamp(self):
        """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

"""
        pass

    @offsetClamp.setter
    def offsetClamp(self, value):
        pass

    @property
    def pointFadeThreshold(self):
        """The threshold value at which points are clipped if they exceed this size."""
        pass

    @pointFadeThreshold.setter
    def pointFadeThreshold(self, value):
        pass

    @property
    def pointOriginUpperLeft(self):
        """``True`` if the point sprite texture origin is upper-left. ``False`` if lower-left."""
        pass

    @pointOriginUpperLeft.setter
    def pointOriginUpperLeft(self, value):
        pass

    @property
    def pointSize(self):
        """The fixed point size in pixels."""
        pass

    @pointSize.setter
    def pointSize(self, value):
        pass

    @property
    def programmablePointSize(self):
        """``True`` if the point size can be programmably exported from a shader."""
        pass

    @programmablePointSize.setter
    def programmablePointSize(self, value):
        pass

    @property
    def sampleCoverage(self):
        """
``True`` if a temporary mask using :data:`sampleCoverageValue` should be used to
resolve the final output color.

"""
        pass

    @sampleCoverage.setter
    def sampleCoverage(self, value):
        pass

    @property
    def sampleCoverageInvert(self):
        """``True`` if the temporary sample coverage mask should be inverted."""
        pass

    @sampleCoverageInvert.setter
    def sampleCoverageInvert(self, value):
        pass

    @property
    def sampleCoverageValue(self):
        """The sample coverage value used if :data:`sampleCoverage` is ``True``."""
        pass

    @sampleCoverageValue.setter
    def sampleCoverageValue(self, value):
        pass

    @property
    def sampleMask(self):
        """
``True`` if the generated samples should be bitwise ``AND`` masked with
:data:`sampleMaskValue`.

"""
        pass

    @sampleMask.setter
    def sampleMask(self, value):
        pass

    @property
    def sampleMaskValue(self):
        """The sample mask value that should be masked against the generated coverage."""
        pass

    @sampleMaskValue.setter
    def sampleMaskValue(self, value):
        pass

    @property
    def sampleShading(self):
        """``True`` if rendering should happen at sample-rate frequency."""
        pass

    @sampleShading.setter
    def sampleShading(self, value):
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


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18848B20>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLRasterizerState' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLRasterizerState' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLRasterizerState' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLRasterizerState' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLRasterizerState' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLRasterizerState' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLRasterizerState' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLRasterizerState' objects>, 'depthBias': <attribute 'depthBias' of 'renderdoc.GLRasterizerState' objects>, 'slopeScaledDepthBias': <attribute 'slopeScaledDepthBias' of 'renderdoc.GLRasterizerState' objects>, 'sampleShading': <attribute 'sampleShading' of 'renderdoc.GLRasterizerState' objects>, 'sampleCoverageInvert': <attribute 'sampleCoverageInvert' of 'renderdoc.GLRasterizerState' objects>, 'programmablePointSize': <attribute 'programmablePointSize' of 'renderdoc.GLRasterizerState' objects>, 'pointSize': <attribute 'pointSize' of 'renderdoc.GLRasterizerState' objects>, 'fillMode': <attribute 'fillMode' of 'renderdoc.GLRasterizerState' objects>, 'cullMode': <attribute 'cullMode' of 'renderdoc.GLRasterizerState' objects>, 'minSampleShadingRate': <attribute 'minSampleShadingRate' of 'renderdoc.GLRasterizerState' objects>, 'offsetClamp': <attribute 'offsetClamp' of 'renderdoc.GLRasterizerState' objects>, 'sampleMaskValue': <attribute 'sampleMaskValue' of 'renderdoc.GLRasterizerState' objects>, 'alphaToOne': <attribute 'alphaToOne' of 'renderdoc.GLRasterizerState' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLRasterizerState' objects>, 'frontCCW': <attribute 'frontCCW' of 'renderdoc.GLRasterizerState' objects>, 'sampleCoverageValue': <attribute 'sampleCoverageValue' of 'renderdoc.GLRasterizerState' objects>, 'pointOriginUpperLeft': <attribute 'pointOriginUpperLeft' of 'renderdoc.GLRasterizerState' objects>, 'depthClamp': <attribute 'depthClamp' of 'renderdoc.GLRasterizerState' objects>, 'multisampleEnable': <attribute 'multisampleEnable' of 'renderdoc.GLRasterizerState' objects>, 'sampleMask': <attribute 'sampleMask' of 'renderdoc.GLRasterizerState' objects>, 'sampleCoverage': <attribute 'sampleCoverage' of 'renderdoc.GLRasterizerState' objects>, 'alphaToCoverage': <attribute 'alphaToCoverage' of 'renderdoc.GLRasterizerState' objects>, 'lineWidth': <attribute 'lineWidth' of 'renderdoc.GLRasterizerState' objects>, 'pointFadeThreshold': <attribute 'pointFadeThreshold' of 'renderdoc.GLRasterizerState' objects>, '__doc__': 'Describes the rasterizer state toggles.'})"


