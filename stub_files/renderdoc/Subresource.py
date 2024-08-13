# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class Subresource(): # skipped bases: <class 'SwigPyObject'>
    """ Specifies a subresource within a texture. """
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
    def mip(self):
        """The mip level in the texture."""
        pass

    @mip.setter
    def mip(self, value):
        pass

    @property
    def sample(self):
        """The sample in a multisampled texture."""
        pass

    @sample.setter
    def sample(self, value):
        pass

    @property
    def slice(self):
        """
The slice within the texture. For 3D textures this is a depth slice, for arrays it is
an array slice.

.. note::
  Cubemaps are simply 2D array textures with a special meaning, so the faces of a cubemap are the 2D
  array slices in the standard order: X+, X-, Y+, Y-, Z+, Z-. Cubemap arrays are 2D arrays with
  ``6 * N`` faces, where each cubemap within the array takes up 6 slices in the above order.

"""
        pass

    @slice.setter
    def slice(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188B6C80>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.Subresource' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.Subresource' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.Subresource' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.Subresource' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.Subresource' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.Subresource' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.Subresource' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.Subresource' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.Subresource' objects>, 'slice': <attribute 'slice' of 'renderdoc.Subresource' objects>, 'sample': <attribute 'sample' of 'renderdoc.Subresource' objects>, 'mip': <attribute 'mip' of 'renderdoc.Subresource' objects>, '__doc__': 'Specifies a subresource within a texture.'})"


