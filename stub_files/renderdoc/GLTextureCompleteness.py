# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class GLTextureCompleteness(): # skipped bases: <class 'SwigPyObject'>
    """ Describes the a texture completeness issue of a descriptor. """
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
    def completeStatus(self):
        """
The details of the texture's (in)completeness. If this string is empty, the texture is
complete. Otherwise it contains an explanation of why the texture is believed to be incomplete.

"""
        pass

    @completeStatus.setter
    def completeStatus(self, value):
        pass

    @property
    def descriptorByteOffset(self):
        """
The byte offset in the GL descriptor storage of the problematic descriptor

"""
        pass

    @descriptorByteOffset.setter
    def descriptorByteOffset(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def typeConflict(self):
        """
The details of any type conflict on this binding. This can happen if
multiple uniforms are pointing to the same binding but with different types. In this case it is
impossible to disambiguate which binding was used.

If this string is empty, no conflict is present. Otherwise it contains the bindings which are
in conflict and their types.

"""
        pass

    @typeConflict.setter
    def typeConflict(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188612A0>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.GLTextureCompleteness' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.GLTextureCompleteness' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.GLTextureCompleteness' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.GLTextureCompleteness' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.GLTextureCompleteness' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.GLTextureCompleteness' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.GLTextureCompleteness' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.GLTextureCompleteness' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.GLTextureCompleteness' objects>, 'descriptorByteOffset': <attribute 'descriptorByteOffset' of 'renderdoc.GLTextureCompleteness' objects>, 'typeConflict': <attribute 'typeConflict' of 'renderdoc.GLTextureCompleteness' objects>, 'completeStatus': <attribute 'completeStatus' of 'renderdoc.GLTextureCompleteness' objects>, '__doc__': 'Describes the a texture completeness issue of a descriptor.'})"


