# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .Offset import Offset

class VKRenderPass(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the setup of a renderpass and subpasses. """
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
    def colorAttachments(self) -> List[int]:
        """
The color attachments for the current subpass, as indices into the framebuffer
attachments.

:type: List[int]

"""
        pass

    @colorAttachments.setter
    def colorAttachments(self, value: List[int]):
        pass

    @property
    def depthstencilAttachment(self):
        """
An index into the framebuffer attachments for the depth-stencil attachment.

If there is no depth-stencil attachment, this index is ``-1``.

"""
        pass

    @depthstencilAttachment.setter
    def depthstencilAttachment(self, value):
        pass

    @property
    def depthstencilResolveAttachment(self):
        """
An index into the framebuffer attachments for the depth-stencil resolve attachment.

If there is no depth-stencil resolve attachment, this index is ``-1``.

"""
        pass

    @depthstencilResolveAttachment.setter
    def depthstencilResolveAttachment(self, value):
        pass

    @property
    def dynamic(self):
        """Whether or not dynamic rendering is in use (no render pass or framebuffer objects)."""
        pass

    @dynamic.setter
    def dynamic(self, value):
        pass

    @property
    def feedbackLoop(self):
        """Whether or not there is a potential feedback loop."""
        pass

    @feedbackLoop.setter
    def feedbackLoop(self, value):
        pass

    @property
    def fragmentDensityAttachment(self):
        """
An index into the framebuffer attachments for the fragment density attachment.

If there is no fragment density attachment, this index is ``-1``.

.. note::
  Only one at most of :data:`fragmentDensityAttachment` and :data:`shadingRateAttachment` will be
  set.

"""
        pass

    @fragmentDensityAttachment.setter
    def fragmentDensityAttachment(self, value):
        pass

    @property
    def fragmentDensityOffsets(self) -> List[Offset]:
        """
If VK_QCOM_fragment_density_map_offset is enabled, contains a list of offsets applied 
to the fragment density map during rendering.

If the list is empty, fdm_offset is disabled and rendering is as normal.

:type: List[Offset]

"""
        pass

    @fragmentDensityOffsets.setter
    def fragmentDensityOffsets(self, value: List[Offset]):
        pass

    @property
    def inputAttachments(self) -> List[int]:
        """
The input attachments for the current subpass, as indices into the framebuffer
attachments.

:type: List[int]

"""
        pass

    @inputAttachments.setter
    def inputAttachments(self, value: List[int]):
        pass

    @property
    def multiviews(self) -> List[int]:
        """
If multiview is enabled, contains a list of view indices to be broadcast to during
rendering.

If the list is empty, multiview is disabled and rendering is as normal.

:type: List[int]

"""
        pass

    @multiviews.setter
    def multiviews(self, value: List[int]):
        pass

    @property
    def resolveAttachments(self) -> List[int]:
        """
The resolve attachments for the current subpass, as indices into the framebuffer
attachments.

:type: List[int]

"""
        pass

    @resolveAttachments.setter
    def resolveAttachments(self, value: List[int]):
        pass

    @property
    def resourceId(self):
        """The :class:`ResourceId` of the render pass."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    @property
    def shadingRateAttachment(self):
        """
An index into the framebuffer attachments for the fragment shading rate attachment.

If there is no fragment shading rate attachment, this index is ``-1``.

.. note::
  Only one at most of :data:`fragmentDensityAttachment` and :data:`shadingRateAttachment` will be
  set.

"""
        pass

    @shadingRateAttachment.setter
    def shadingRateAttachment(self, value):
        pass

    @property
    def shadingRateTexelSize(self) -> Tuple[int,int]:
        """
The size of the framebuffer region represented by each texel in
:data:`shadingRateAttachment`.

For example if this is (2,2) then every texel in the attachment gives the shading rate of a 2x2
block in the framebuffer so the shading rate attachment is half the size of the other attachments in
each dimension.

If no attachment is set in :data:`shadingRateAttachment` this will be (1,1).

:type: Tuple[int,int]

"""
        pass

    @shadingRateTexelSize.setter
    def shadingRateTexelSize(self, value: Tuple[int,int]):
        pass

    @property
    def subpass(self):
        """The index of the current active subpass."""
        pass

    @subpass.setter
    def subpass(self, value):
        pass

    @property
    def suspended(self):
        """Whether or not dynamic rendering is currently suspended."""
        pass

    @suspended.setter
    def suspended(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def tileOnlyMSAASampleCount(self):
        """
If VK_EXT_multisampled_render_to_single_sampled is enabled, contains the number of
samples used to render this subpass.

If the subpass is not internally multisampled, tileOnlyMSAASampleCount is set to 0.

"""
        pass

    @tileOnlyMSAASampleCount.setter
    def tileOnlyMSAASampleCount(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18891AB0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKRenderPass' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKRenderPass' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKRenderPass' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKRenderPass' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKRenderPass' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKRenderPass' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKRenderPass' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKRenderPass' objects>, 'inputAttachments': <attribute 'inputAttachments' of 'renderdoc.VKRenderPass' objects>, 'colorAttachments': <attribute 'colorAttachments' of 'renderdoc.VKRenderPass' objects>, 'resolveAttachments': <attribute 'resolveAttachments' of 'renderdoc.VKRenderPass' objects>, 'multiviews': <attribute 'multiviews' of 'renderdoc.VKRenderPass' objects>, 'subpass': <attribute 'subpass' of 'renderdoc.VKRenderPass' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.VKRenderPass' objects>, 'shadingRateTexelSize': <attribute 'shadingRateTexelSize' of 'renderdoc.VKRenderPass' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKRenderPass' objects>, 'fragmentDensityOffsets': <attribute 'fragmentDensityOffsets' of 'renderdoc.VKRenderPass' objects>, 'depthstencilAttachment': <attribute 'depthstencilAttachment' of 'renderdoc.VKRenderPass' objects>, 'depthstencilResolveAttachment': <attribute 'depthstencilResolveAttachment' of 'renderdoc.VKRenderPass' objects>, 'fragmentDensityAttachment': <attribute 'fragmentDensityAttachment' of 'renderdoc.VKRenderPass' objects>, 'shadingRateAttachment': <attribute 'shadingRateAttachment' of 'renderdoc.VKRenderPass' objects>, 'tileOnlyMSAASampleCount': <attribute 'tileOnlyMSAASampleCount' of 'renderdoc.VKRenderPass' objects>, 'dynamic': <attribute 'dynamic' of 'renderdoc.VKRenderPass' objects>, 'suspended': <attribute 'suspended' of 'renderdoc.VKRenderPass' objects>, 'feedbackLoop': <attribute 'feedbackLoop' of 'renderdoc.VKRenderPass' objects>, '__doc__': 'Describes the setup of a renderpass and subpasses.'})"


