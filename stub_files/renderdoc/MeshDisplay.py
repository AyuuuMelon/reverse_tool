# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .AxisMapping import AxisMapping
from .Camera import Camera
from .FloatVector import FloatVector
from .MeshFormat import MeshFormat

class MeshDisplay(): # skipped bases: <class 'SwigPyObject'>
    """
    Describes how to render a mesh preview of one or more meshes. Describes the camera configuration as
    well as what options to use when rendering both the current mesh, and any other auxilliary meshes.
    
    .. data:: NoHighlight
    
      Value for :data:`highlightVert` if no vertex should be highlighted.
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
    def aspect(self):
        """The aspect ratio to use when calculating a perspective projection matrix."""
        pass

    @aspect.setter
    def aspect(self, value):
        pass

    @property
    def axisMapping(self) -> AxisMapping:
        """
The axis mapping to apply to the mesh.

:type: AxisMapping

"""
        pass

    @axisMapping.setter
    def axisMapping(self, value: AxisMapping):
        pass

    @property
    def cam(self) -> Camera:
        """
The camera to use when rendering all of the meshes.

:type: Camera

"""
        pass

    @cam.setter
    def cam(self, value: Camera):
        pass

    @property
    def curInstance(self):
        """The index of the currently selected instance in the drawcall."""
        pass

    @curInstance.setter
    def curInstance(self, value):
        pass

    @property
    def curView(self):
        """The index of the currently selected multiview view in the drawcall."""
        pass

    @curView.setter
    def curView(self, value):
        pass

    @property
    def exploderScale(self):
        """Scales the exploded vertex displacement."""
        pass

    @exploderScale.setter
    def exploderScale(self, value):
        pass

    @property
    def fov(self):
        """The field of view to use when calculating a perspective projection matrix."""
        pass

    @fov.setter
    def fov(self, value):
        pass

    @property
    def highlightVert(self):
        """The index of the vertex to highlight, or :data:`NoHighlight` to select no vertex."""
        pass

    @highlightVert.setter
    def highlightVert(self, value):
        pass

    @property
    def maxBounds(self) -> FloatVector:
        """
The maximum co-ordinates in each axis of the mesh bounding box.

:type: FloatVector

"""
        pass

    @maxBounds.setter
    def maxBounds(self, value: FloatVector):
        pass

    @property
    def minBounds(self) -> FloatVector:
        """
The minimum co-ordinates in each axis of the mesh bounding box.

:type: FloatVector

"""
        pass

    @minBounds.setter
    def minBounds(self, value: FloatVector):
        pass

    @property
    def ortho(self):
        """``True`` if the projection matrix to use when unprojecting vertex positions is orthographic."""
        pass

    @ortho.setter
    def ortho(self, value):
        pass

    @property
    def position(self) -> MeshFormat:
        """
The configuration for the primary mesh's position data.

:type: MeshFormat

"""
        pass

    @position.setter
    def position(self, value: MeshFormat):
        pass

    @property
    def second(self) -> MeshFormat:
        """
The configuration for the primary mesh's secondary data, if used for solid shading.

:type: MeshFormat

"""
        pass

    @second.setter
    def second(self, value: MeshFormat):
        pass

    @property
    def showAllInstances(self):
        """``True`` if all instances in the drawcall should be drawn as secondary meshes."""
        pass

    @showAllInstances.setter
    def showAllInstances(self, value):
        pass

    @property
    def showBBox(self):
        """``True`` if the bounding box around the mesh should be rendered."""
        pass

    @showBBox.setter
    def showBBox(self, value):
        pass

    @property
    def showPrevInstances(self):
        """``True`` if all previous instances in the drawcall should be drawn as secondary meshes."""
        pass

    @showPrevInstances.setter
    def showPrevInstances(self, value):
        pass

    @property
    def showWholePass(self):
        """``True`` if all draws in the current pass up to the current draw should be drawn as secondary meshes."""
        pass

    @showWholePass.setter
    def showWholePass(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def type(self):
        """The :class:`MeshDataStage` where this mesh data comes from."""
        pass

    @type.setter
    def type(self, value):
        pass

    @property
    def visualisationMode(self):
        """The :class:`visualisation mode <Visualisation>` to use when rendering the current mesh."""
        pass

    @visualisationMode.setter
    def visualisationMode(self, value):
        pass

    @property
    def vtxExploderSliderSNorm(self):
        """Displace/explode vertices to help visualise vertex reuse vs disjointedness."""
        pass

    @vtxExploderSliderSNorm.setter
    def vtxExploderSliderSNorm(self, value):
        pass

    @property
    def wireframeDraw(self):
        """``True`` if the wireframe of the mesh should be rendered as well as solid shading."""
        pass

    @wireframeDraw.setter
    def wireframeDraw(self, value):
        pass


    NoHighlight = 4294967295
    __dict__ = None # (!) real value is "mappingproxy({'NoHighlight': 4294967295, 'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE1885D110>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.MeshDisplay' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.MeshDisplay' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.MeshDisplay' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.MeshDisplay' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.MeshDisplay' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.MeshDisplay' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.MeshDisplay' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.MeshDisplay' objects>, 'showBBox': <attribute 'showBBox' of 'renderdoc.MeshDisplay' objects>, 'wireframeDraw': <attribute 'wireframeDraw' of 'renderdoc.MeshDisplay' objects>, 'showPrevInstances': <attribute 'showPrevInstances' of 'renderdoc.MeshDisplay' objects>, 'showAllInstances': <attribute 'showAllInstances' of 'renderdoc.MeshDisplay' objects>, 'curView': <attribute 'curView' of 'renderdoc.MeshDisplay' objects>, 'cam': <attribute 'cam' of 'renderdoc.MeshDisplay' objects>, 'aspect': <attribute 'aspect' of 'renderdoc.MeshDisplay' objects>, 'visualisationMode': <attribute 'visualisationMode' of 'renderdoc.MeshDisplay' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.MeshDisplay' objects>, 'ortho': <attribute 'ortho' of 'renderdoc.MeshDisplay' objects>, 'second': <attribute 'second' of 'renderdoc.MeshDisplay' objects>, 'minBounds': <attribute 'minBounds' of 'renderdoc.MeshDisplay' objects>, 'maxBounds': <attribute 'maxBounds' of 'renderdoc.MeshDisplay' objects>, 'position': <attribute 'position' of 'renderdoc.MeshDisplay' objects>, 'type': <attribute 'type' of 'renderdoc.MeshDisplay' objects>, 'axisMapping': <attribute 'axisMapping' of 'renderdoc.MeshDisplay' objects>, 'vtxExploderSliderSNorm': <attribute 'vtxExploderSliderSNorm' of 'renderdoc.MeshDisplay' objects>, 'curInstance': <attribute 'curInstance' of 'renderdoc.MeshDisplay' objects>, 'exploderScale': <attribute 'exploderScale' of 'renderdoc.MeshDisplay' objects>, 'highlightVert': <attribute 'highlightVert' of 'renderdoc.MeshDisplay' objects>, 'fov': <attribute 'fov' of 'renderdoc.MeshDisplay' objects>, 'showWholePass': <attribute 'showWholePass' of 'renderdoc.MeshDisplay' objects>, '__doc__': '\\n\\nDescribes how to render a mesh preview of one or more meshes. Describes the camera configuration as\\nwell as what options to use when rendering both the current mesh, and any other auxilliary meshes.\\n\\n.. data:: NoHighlight\\n\\n  Value for :data:`highlightVert` if no vertex should be highlighted.\\n\\n'})"


