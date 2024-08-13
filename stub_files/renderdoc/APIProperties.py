# encoding: utf-8
# module renderdoc
# from D:\reverse_plugin\renderdoc_src\x64\Release\pymodules\renderdoc.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum

from typing import List, Tuple, Callable, Any


class APIProperties(): # skipped bases: <class 'SwigPyObject'>
    """ Gives some API-specific information about the capture. """
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
    def degraded(self):
        """
``True`` if the capture was loaded successfully but running in a degraded mode - e.g.
with software rendering, or with some functionality disabled due to lack of support.

"""
        pass

    @degraded.setter
    def degraded(self, value):
        pass

    @property
    def localRenderer(self):
        """
The :class:`GraphicsAPI` used to render the log. For remote replay this could be
different to the above, and lets the UI make decisions e.g. to flip rendering of images.

"""
        pass

    @localRenderer.setter
    def localRenderer(self, value):
        pass

    @property
    def pipelineType(self):
        """The :class:`GraphicsAPI` of the actual log/capture."""
        pass

    @pipelineType.setter
    def pipelineType(self, value):
        pass

    @property
    def pixelHistory(self):
        """(``True`` if the API supports viewing pixel history."""
        pass

    @pixelHistory.setter
    def pixelHistory(self, value):
        pass

    @property
    def remoteReplay(self):
        """
``True`` if the capture is being replayed over a remote connection.

"""
        pass

    @remoteReplay.setter
    def remoteReplay(self, value):
        pass

    @property
    def rgpCapture(self):
        """``True`` if the driver and system are configured to allow creating RGP captures."""
        pass

    @rgpCapture.setter
    def rgpCapture(self, value):
        pass

    @property
    def shaderDebugging(self):
        """(``True`` if the API supports shader debugging."""
        pass

    @shaderDebugging.setter
    def shaderDebugging(self, value):
        pass

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    @property
    def vendor(self):
        """The :class:`GPUVendor` of the active GPU being used."""
        pass

    @vendor.setter
    def vendor(self, value):
        pass


    __dict__ = None # (!) real value is "mappingproxy({'this': <attribute 'this' of 'SwigPyObject' objects>, 'thisown': <attribute 'thisown' of 'SwigPyObject' objects>, '__new__': <built-in method __new__ of SwigPyObjectType object at 0x00007FFE188AAD20>, '__hash__': <slot wrapper '__hash__' of 'renderdoc.APIProperties' objects>, '__lt__': <slot wrapper '__lt__' of 'renderdoc.APIProperties' objects>, '__le__': <slot wrapper '__le__' of 'renderdoc.APIProperties' objects>, '__eq__': <slot wrapper '__eq__' of 'renderdoc.APIProperties' objects>, '__ne__': <slot wrapper '__ne__' of 'renderdoc.APIProperties' objects>, '__gt__': <slot wrapper '__gt__' of 'renderdoc.APIProperties' objects>, '__ge__': <slot wrapper '__ge__' of 'renderdoc.APIProperties' objects>, '__init__': <slot wrapper '__init__' of 'renderdoc.APIProperties' objects>, 'degraded': <attribute 'degraded' of 'renderdoc.APIProperties' objects>, 'rgpCapture': <attribute 'rgpCapture' of 'renderdoc.APIProperties' objects>, 'pixelHistory': <attribute 'pixelHistory' of 'renderdoc.APIProperties' objects>, 'remoteReplay': <attribute 'remoteReplay' of 'renderdoc.APIProperties' objects>, '__dict__': <attribute '__dict__' of 'renderdoc.APIProperties' objects>, 'pipelineType': <attribute 'pipelineType' of 'renderdoc.APIProperties' objects>, 'shaderDebugging': <attribute 'shaderDebugging' of 'renderdoc.APIProperties' objects>, 'vendor': <attribute 'vendor' of 'renderdoc.APIProperties' objects>, 'localRenderer': <attribute 'localRenderer' of 'renderdoc.APIProperties' objects>, '__doc__': 'Gives some API-specific information about the capture.'})"


