# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


from .FloatVector import FloatVector

class VKSampleLocations(): # skipped bases: <class 'SwigPyObject'>
    """ Describes state of custom sample locations in the pipeline. """
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
    def customLocations(self) -> List[FloatVector]:
        """
The custom sample locations. Only x and y are valid, z and w are set to 0.0.

If the list is empty then the standard sample pattern is in use.

:type: List[FloatVector]

"""
        pass

    @customLocations.setter
    def customLocations(self, value: List[FloatVector]):
        pass

    @property
    def gridHeight(self):
        """The height in pixels of the region configured."""
        pass

    @gridHeight.setter
    def gridHeight(self, value):
        pass

    @property
    def gridWidth(self):
        """The width in pixels of the region configured."""
        pass

    @gridWidth.setter
    def gridWidth(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE18851300>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.VKSampleLocations' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.VKSampleLocations' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.VKSampleLocations' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.VKSampleLocations' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.VKSampleLocations' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.VKSampleLocations' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.VKSampleLocations' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.VKSampleLocations' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.VKSampleLocations' objects>, 'gridHeight': <attribute 'gridHeight' of 'renderdoc.VKSampleLocations' objects>, 'customLocations': <attribute 'customLocations' of 'renderdoc.VKSampleLocations' objects>, 'gridWidth': <attribute 'gridWidth' of 'renderdoc.VKSampleLocations' objects>, '__doc__': 'Describes state of custom sample locations in the pipeline.'})"


