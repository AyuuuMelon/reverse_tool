# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class ResourceId(): # skipped bases: <class 'SwigPyObject'>
    """
    This is an opaque identifier that uniquely locates a resource.
    
    .. note::
      These IDs do not overlap ever - textures, buffers, shaders and samplers will all have unique IDs
      and do not reuse the namespace. Likewise the IDs assigned for resources during capture  are not
      re-used on replay - the corresponding resources created on replay to stand-in for capture-time
      resources are given unique IDs and a mapping is stored to between the capture-time resource and
      the replay-time one.
    """
    @staticmethod
    def Null() -> 'ResourceId': # real signature unknown; restored from __doc__
        """
        Null()
        
        A helper function that explicitly creates an empty/invalid/null :class:`ResourceId`.
        
        :return: an empty/invalid/null :class:`ResourceId`.
        :rtype: ResourceId
        """
        pass

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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18885E10>, '__repr__': <slot wrapper '__repr__' of 'renderdoc.ResourceId' objects>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.ResourceId' objects>, '__str__': <slot wrapper '__str__' of 'renderdoc.ResourceId' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.ResourceId' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.ResourceId' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.ResourceId' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.ResourceId' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.ResourceId' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.ResourceId' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.ResourceId' objects>, '__int__': <slot wrapper '__int__' of 'renderdoc.ResourceId' objects>, 'Null': <staticmethod(<built-in method Null of SwigPyObjectType object at 0x00007FFE18885E10>)>, '__dict__': <attribute '__dict__' of 'renderdoc.ResourceId' objects>, '__doc__': '\\nThis is an opaque identifier that uniquely locates a resource.\\n\\n.. note::\\n  These IDs do not overlap ever - textures, buffers, shaders and samplers will all have unique IDs\\n  and do not reuse the namespace. Likewise the IDs assigned for resources during capture  are not\\n  re-used on replay - the corresponding resources created on replay to stand-in for capture-time\\n  resources are given unique IDs and a mapping is stored to between the capture-time resource and\\n  the replay-time one.\\n\\n'})"


