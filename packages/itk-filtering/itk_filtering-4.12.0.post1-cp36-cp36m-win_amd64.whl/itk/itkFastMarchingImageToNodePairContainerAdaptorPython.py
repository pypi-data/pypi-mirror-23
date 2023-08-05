# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingImageToNodePairContainerAdaptorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingImageToNodePairContainerAdaptorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingImageToNodePairContainerAdaptorPython')
    _itkFastMarchingImageToNodePairContainerAdaptorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingImageToNodePairContainerAdaptorPython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingImageToNodePairContainerAdaptorPython
            return _itkFastMarchingImageToNodePairContainerAdaptorPython
        try:
            _mod = imp.load_module('_itkFastMarchingImageToNodePairContainerAdaptorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingImageToNodePairContainerAdaptorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingImageToNodePairContainerAdaptorPython
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import ITKFastMarchingBasePython
import itkImagePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkLevelSetNodePython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkFastMarchingStoppingCriterionBasePython
import itkNodePairPython

def itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_New():
  return itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.New()


def itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_New():
  return itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.New()

class itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Pointer":
        """__New_orig__() -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Pointer"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Pointer":
        """Clone(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self) -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Pointer"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Clone(self)


    def SetAliveImage(self, iImage: 'itkImageF2') -> "void":
        """SetAliveImage(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self, itkImageF2 iImage)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetAliveImage(self, iImage)


    def SetTrialImage(self, iImage: 'itkImageF2') -> "void":
        """SetTrialImage(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self, itkImageF2 iImage)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetTrialImage(self, iImage)


    def SetForbiddenImage(self, iImage: 'itkImageF2') -> "void":
        """SetForbiddenImage(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self, itkImageF2 iImage)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetForbiddenImage(self, iImage)


    def SetIsForbiddenImageBinaryMask(self, _arg: 'bool const') -> "void":
        """SetIsForbiddenImageBinaryMask(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self, bool const _arg)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetIsForbiddenImageBinaryMask(self, _arg)


    def IsForbiddenImageBinaryMaskOn(self) -> "void":
        """IsForbiddenImageBinaryMaskOn(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_IsForbiddenImageBinaryMaskOn(self)


    def IsForbiddenImageBinaryMaskOff(self) -> "void":
        """IsForbiddenImageBinaryMaskOff(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_IsForbiddenImageBinaryMaskOff(self)


    def GetAlivePoints(self) -> "itkVectorContainerULLNPI2F *":
        """GetAlivePoints(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self) -> itkVectorContainerULLNPI2F"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetAlivePoints(self)


    def GetTrialPoints(self) -> "itkVectorContainerULLNPI2F *":
        """GetTrialPoints(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self) -> itkVectorContainerULLNPI2F"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetTrialPoints(self)


    def GetForbiddenPoints(self) -> "itkVectorContainerULLNPI2F *":
        """GetForbiddenPoints(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self) -> itkVectorContainerULLNPI2F"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetForbiddenPoints(self)


    def SetAliveValue(self, _arg: 'float const') -> "void":
        """SetAliveValue(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self, float const _arg)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetAliveValue(self, _arg)


    def SetTrialValue(self, _arg: 'float const') -> "void":
        """SetTrialValue(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self, float const _arg)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetTrialValue(self, _arg)


    def Update(self) -> "void":
        """Update(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Update(self)

    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 *":
        """GetPointer(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 self) -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.Clone = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Clone, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.SetAliveImage = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetAliveImage, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.SetTrialImage = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetTrialImage, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.SetForbiddenImage = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetForbiddenImage, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.SetIsForbiddenImageBinaryMask = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetIsForbiddenImageBinaryMask, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.IsForbiddenImageBinaryMaskOn = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_IsForbiddenImageBinaryMaskOn, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.IsForbiddenImageBinaryMaskOff = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_IsForbiddenImageBinaryMaskOff, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.GetAlivePoints = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetAlivePoints, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.GetTrialPoints = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetTrialPoints, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.GetForbiddenPoints = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetForbiddenPoints, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.SetAliveValue = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetAliveValue, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.SetTrialValue = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetTrialValue, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.Update = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Update, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.GetPointer = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetPointer, None, itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_swigregister = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_swigregister
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_swigregister(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)

def itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__() -> "itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Pointer":
    """itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__() -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Pointer"""
    return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__()

def itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 *":
    """itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast(itkLightObject obj) -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2"""
    return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast(obj)

class itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Pointer":
        """__New_orig__() -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Pointer"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Pointer":
        """Clone(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self) -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Pointer"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Clone(self)


    def SetAliveImage(self, iImage: 'itkImageF3') -> "void":
        """SetAliveImage(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self, itkImageF3 iImage)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetAliveImage(self, iImage)


    def SetTrialImage(self, iImage: 'itkImageF3') -> "void":
        """SetTrialImage(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self, itkImageF3 iImage)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetTrialImage(self, iImage)


    def SetForbiddenImage(self, iImage: 'itkImageF3') -> "void":
        """SetForbiddenImage(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self, itkImageF3 iImage)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetForbiddenImage(self, iImage)


    def SetIsForbiddenImageBinaryMask(self, _arg: 'bool const') -> "void":
        """SetIsForbiddenImageBinaryMask(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self, bool const _arg)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetIsForbiddenImageBinaryMask(self, _arg)


    def IsForbiddenImageBinaryMaskOn(self) -> "void":
        """IsForbiddenImageBinaryMaskOn(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_IsForbiddenImageBinaryMaskOn(self)


    def IsForbiddenImageBinaryMaskOff(self) -> "void":
        """IsForbiddenImageBinaryMaskOff(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_IsForbiddenImageBinaryMaskOff(self)


    def GetAlivePoints(self) -> "itkVectorContainerULLNPI3F *":
        """GetAlivePoints(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self) -> itkVectorContainerULLNPI3F"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetAlivePoints(self)


    def GetTrialPoints(self) -> "itkVectorContainerULLNPI3F *":
        """GetTrialPoints(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self) -> itkVectorContainerULLNPI3F"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetTrialPoints(self)


    def GetForbiddenPoints(self) -> "itkVectorContainerULLNPI3F *":
        """GetForbiddenPoints(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self) -> itkVectorContainerULLNPI3F"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetForbiddenPoints(self)


    def SetAliveValue(self, _arg: 'float const') -> "void":
        """SetAliveValue(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self, float const _arg)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetAliveValue(self, _arg)


    def SetTrialValue(self, _arg: 'float const') -> "void":
        """SetTrialValue(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self, float const _arg)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetTrialValue(self, _arg)


    def Update(self) -> "void":
        """Update(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self)"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Update(self)

    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 *":
        """GetPointer(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 self) -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3"""
        return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.Clone = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Clone, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.SetAliveImage = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetAliveImage, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.SetTrialImage = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetTrialImage, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.SetForbiddenImage = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetForbiddenImage, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.SetIsForbiddenImageBinaryMask = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetIsForbiddenImageBinaryMask, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.IsForbiddenImageBinaryMaskOn = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_IsForbiddenImageBinaryMaskOn, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.IsForbiddenImageBinaryMaskOff = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_IsForbiddenImageBinaryMaskOff, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.GetAlivePoints = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetAlivePoints, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.GetTrialPoints = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetTrialPoints, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.GetForbiddenPoints = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetForbiddenPoints, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.SetAliveValue = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetAliveValue, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.SetTrialValue = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetTrialValue, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.Update = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Update, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.GetPointer = new_instancemethod(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetPointer, None, itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_swigregister = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_swigregister
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_swigregister(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)

def itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__() -> "itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Pointer":
    """itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__() -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Pointer"""
    return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__()

def itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 *":
    """itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast(itkLightObject obj) -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3"""
    return _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast(obj)



