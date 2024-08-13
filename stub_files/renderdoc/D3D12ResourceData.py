# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .D3D12ResourceState import D3D12ResourceState

class D3D12ResourceData(): # skipped bases: <class 'SwigPyObject'>
    """ Contains the current state of a given resource. """
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
    def resourceId(self):
        """The :class:`ResourceId` of the resource."""
        pass

    @resourceId.setter
    def resourceId(self, value):
        pass

    @property
    def states(self) -> List[D3D12ResourceState]:
        """
The subresource states in this resource.

:type: List[D3D12ResourceState]

"""
        pass

    @states.setter
    def states(self, value: List[D3D12ResourceState]):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18848100>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.D3D12ResourceData' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.D3D12ResourceData' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.D3D12ResourceData' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.D3D12ResourceData' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.D3D12ResourceData' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.D3D12ResourceData' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.D3D12ResourceData' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.D3D12ResourceData' objects>, 'resourceId': <attribute 'resourceId' of 'renderdoc.D3D12ResourceData' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.D3D12ResourceData' objects>, 'states': <attribute 'states' of 'renderdoc.D3D12ResourceData' objects>, '__doc__': 'Contains the current state of a given resource.'})"


