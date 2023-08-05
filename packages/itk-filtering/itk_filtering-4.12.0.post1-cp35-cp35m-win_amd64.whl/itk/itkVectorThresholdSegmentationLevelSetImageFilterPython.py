# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVectorThresholdSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVectorThresholdSegmentationLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVectorThresholdSegmentationLevelSetImageFilterPython')
    _itkVectorThresholdSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVectorThresholdSegmentationLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkVectorThresholdSegmentationLevelSetImageFilterPython
            return _itkVectorThresholdSegmentationLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkVectorThresholdSegmentationLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVectorThresholdSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVectorThresholdSegmentationLevelSetImageFilterPython
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


import itkVariableSizeMatrixPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import itkSegmentationLevelSetImageFilterPython
import itkSparseFieldLevelSetImageFilterPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkFiniteDifferenceImageFilterPython
import ITKCommonBasePython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython
import itkFiniteDifferenceFunctionPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython

def itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_New():
  return itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.New()


def itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_New():
  return itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.New()

class itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IVF22F):
    """Proxy of C++ itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Pointer":
        """__New_orig__() -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Pointer"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Pointer":
        """Clone(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self) -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Pointer"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Clone(self)


    def SetMean(self, mean: 'double const &') -> "void":
        """SetMean(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self, double const & mean)"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_SetMean(self, mean)


    def GetMean(self) -> "double const &":
        """GetMean(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self) -> double const &"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetMean(self)


    def SetCovariance(self, cov: 'itkVariableSizeMatrixD') -> "void":
        """SetCovariance(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self, itkVariableSizeMatrixD cov)"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_SetCovariance(self, cov)


    def GetCovariance(self) -> "itkVariableSizeMatrixD const &":
        """GetCovariance(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self) -> itkVariableSizeMatrixD"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetCovariance(self)


    def SetThreshold(self, thr: 'float') -> "void":
        """SetThreshold(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self, float thr)"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_SetThreshold(self, thr)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self) -> float"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetThreshold(self)

    __swig_destroy__ = _itkVectorThresholdSegmentationLevelSetImageFilterPython.delete_itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F

    def cast(obj: 'itkLightObject') -> "itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F *":
        """cast(itkLightObject obj) -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F *":
        """GetPointer(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F self) -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F

        Create a new object of the class itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.Clone = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Clone, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.SetMean = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_SetMean, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.GetMean = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetMean, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.SetCovariance = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_SetCovariance, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.GetCovariance = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetCovariance, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.SetThreshold = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_SetThreshold, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.GetThreshold = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetThreshold, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F.GetPointer = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_GetPointer, None, itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_swigregister = _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_swigregister
itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_swigregister(itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F)

def itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F___New_orig__() -> "itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Pointer":
    """itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F___New_orig__() -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_Pointer"""
    return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F___New_orig__()

def itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_cast(obj: 'itkLightObject') -> "itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F *":
    """itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_cast(itkLightObject obj) -> itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F"""
    return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F_cast(obj)

class itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IVF33F):
    """Proxy of C++ itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Pointer":
        """__New_orig__() -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Pointer"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Pointer":
        """Clone(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self) -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Pointer"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Clone(self)


    def SetMean(self, mean: 'double const &') -> "void":
        """SetMean(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self, double const & mean)"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_SetMean(self, mean)


    def GetMean(self) -> "double const &":
        """GetMean(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self) -> double const &"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetMean(self)


    def SetCovariance(self, cov: 'itkVariableSizeMatrixD') -> "void":
        """SetCovariance(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self, itkVariableSizeMatrixD cov)"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_SetCovariance(self, cov)


    def GetCovariance(self) -> "itkVariableSizeMatrixD const &":
        """GetCovariance(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self) -> itkVariableSizeMatrixD"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetCovariance(self)


    def SetThreshold(self, thr: 'float') -> "void":
        """SetThreshold(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self, float thr)"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_SetThreshold(self, thr)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self) -> float"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetThreshold(self)

    __swig_destroy__ = _itkVectorThresholdSegmentationLevelSetImageFilterPython.delete_itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F

    def cast(obj: 'itkLightObject') -> "itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F *":
        """cast(itkLightObject obj) -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F *":
        """GetPointer(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F self) -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F"""
        return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F

        Create a new object of the class itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.Clone = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Clone, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.SetMean = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_SetMean, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.GetMean = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetMean, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.SetCovariance = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_SetCovariance, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.GetCovariance = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetCovariance, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.SetThreshold = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_SetThreshold, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.GetThreshold = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetThreshold, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F.GetPointer = new_instancemethod(_itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_GetPointer, None, itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_swigregister = _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_swigregister
itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_swigregister(itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F)

def itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F___New_orig__() -> "itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Pointer":
    """itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F___New_orig__() -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_Pointer"""
    return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F___New_orig__()

def itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_cast(obj: 'itkLightObject') -> "itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F *":
    """itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_cast(itkLightObject obj) -> itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F"""
    return _itkVectorThresholdSegmentationLevelSetImageFilterPython.itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F_cast(obj)



