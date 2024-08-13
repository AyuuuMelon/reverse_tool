# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .VKDynamicOffset import VKDynamicOffset

class VKDescriptorSet(): # skipped bases: <class 'SwigPyObject'>
    """ The contents of a descriptor set. """
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
    def descriptorSetResourceId(self):
        """The :class:`ResourceId` of the descriptor set object."""
        pass

    @descriptorSetResourceId.setter
    def descriptorSetResourceId(self, value):
        pass

    @property
    def dynamicOffsets(self) -> List[VKDynamicOffset]:
        """
A list of dynamic offsets to be applied to specific bindings, on top of the contents
of their descriptors.

.. note::
  The returned values from :meth:`PipeState.GetConstantBuffer` already have these offsets applied.

:type: List[VKDynamicOffset]

"""
        pass

    @dynamicOffsets.setter
    def dynamicOffsets(self, value: List[VKDynamicOffset]):
        pass

    @property
    def layoutResourceId(self):
        """The :class:`ResourceId` of the descriptor set layout that matches this set."""
        pass

    @layoutResourceId.setter
    def layoutResourceId(self, value):
        pass

    @property
    def pushDescriptor(self):
        """Indicates if this is a virtual 'push' descriptor set."""
        pass

    @pushDescriptor.setter
    def pushDescriptor(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188507E0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKDescriptorSet' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKDescriptorSet' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKDescriptorSet' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKDescriptorSet' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKDescriptorSet' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKDescriptorSet' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKDescriptorSet' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKDescriptorSet' objects>, 'pushDescriptor': <attribute 'pushDescriptor' of 'renderdoc.VKDescriptorSet' objects>, 'layoutResourceId': <attribute 'layoutResourceId' of 'renderdoc.VKDescriptorSet' objects>, 'descriptorSetResourceId': <attribute 'descriptorSetResourceId' of 'renderdoc.VKDescriptorSet' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKDescriptorSet' objects>, 'dynamicOffsets': <attribute 'dynamicOffsets' of 'renderdoc.VKDescriptorSet' objects>, '__doc__': 'The contents of a descriptor set.'})"


