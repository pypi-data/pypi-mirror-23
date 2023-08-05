# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCannySegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkCannySegmentationLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkCannySegmentationLevelSetImageFilterPython')
    _itkCannySegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCannySegmentationLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCannySegmentationLevelSetImageFilterPython
            return _itkCannySegmentationLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkCannySegmentationLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkCannySegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCannySegmentationLevelSetImageFilterPython
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


import itkImagePython
import stdcomplexPython
import pyBasePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkSegmentationLevelSetImageFilterPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkCannySegmentationLevelSetImageFilterIF3IF3F_New():
  return itkCannySegmentationLevelSetImageFilterIF3IF3F.New()


def itkCannySegmentationLevelSetImageFilterIF2IF2F_New():
  return itkCannySegmentationLevelSetImageFilterIF2IF2F.New()

class itkCannySegmentationLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    """Proxy of C++ itkCannySegmentationLevelSetImageFilterIF2IF2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkCannySegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkCannySegmentationLevelSetImageFilterIF2IF2F self) -> itkCannySegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_Clone(self)


    def SetThreshold(self, v):
        """SetThreshold(itkCannySegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_SetThreshold(self, v)


    def GetThreshold(self):
        """GetThreshold(itkCannySegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetThreshold(self)


    def SetVariance(self, v):
        """SetVariance(itkCannySegmentationLevelSetImageFilterIF2IF2F self, double v)"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_SetVariance(self, v)


    def GetVariance(self):
        """GetVariance(itkCannySegmentationLevelSetImageFilterIF2IF2F self) -> double"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetVariance(self)


    def GetCannyImage(self):
        """GetCannyImage(itkCannySegmentationLevelSetImageFilterIF2IF2F self) -> itkImageF2"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetCannyImage(self)

    OutputHasNumericTraitsCheck = _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkCannySegmentationLevelSetImageFilterPython.delete_itkCannySegmentationLevelSetImageFilterIF2IF2F

    def cast(obj):
        """cast(itkLightObject obj) -> itkCannySegmentationLevelSetImageFilterIF2IF2F"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkCannySegmentationLevelSetImageFilterIF2IF2F self) -> itkCannySegmentationLevelSetImageFilterIF2IF2F"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCannySegmentationLevelSetImageFilterIF2IF2F

        Create a new object of the class itkCannySegmentationLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCannySegmentationLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCannySegmentationLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCannySegmentationLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCannySegmentationLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_Clone, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F.SetThreshold = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_SetThreshold, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F.GetThreshold = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetThreshold, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F.SetVariance = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_SetVariance, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F.GetVariance = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetVariance, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F.GetCannyImage = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetCannyImage, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F.GetPointer = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_GetPointer, None, itkCannySegmentationLevelSetImageFilterIF2IF2F)
itkCannySegmentationLevelSetImageFilterIF2IF2F_swigregister = _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_swigregister
itkCannySegmentationLevelSetImageFilterIF2IF2F_swigregister(itkCannySegmentationLevelSetImageFilterIF2IF2F)

def itkCannySegmentationLevelSetImageFilterIF2IF2F___New_orig__():
    """itkCannySegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> itkCannySegmentationLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F___New_orig__()

def itkCannySegmentationLevelSetImageFilterIF2IF2F_cast(obj):
    """itkCannySegmentationLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkCannySegmentationLevelSetImageFilterIF2IF2F"""
    return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF2IF2F_cast(obj)

class itkCannySegmentationLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    """Proxy of C++ itkCannySegmentationLevelSetImageFilterIF3IF3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkCannySegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkCannySegmentationLevelSetImageFilterIF3IF3F self) -> itkCannySegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_Clone(self)


    def SetThreshold(self, v):
        """SetThreshold(itkCannySegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_SetThreshold(self, v)


    def GetThreshold(self):
        """GetThreshold(itkCannySegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetThreshold(self)


    def SetVariance(self, v):
        """SetVariance(itkCannySegmentationLevelSetImageFilterIF3IF3F self, double v)"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_SetVariance(self, v)


    def GetVariance(self):
        """GetVariance(itkCannySegmentationLevelSetImageFilterIF3IF3F self) -> double"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetVariance(self)


    def GetCannyImage(self):
        """GetCannyImage(itkCannySegmentationLevelSetImageFilterIF3IF3F self) -> itkImageF3"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetCannyImage(self)

    OutputHasNumericTraitsCheck = _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkCannySegmentationLevelSetImageFilterPython.delete_itkCannySegmentationLevelSetImageFilterIF3IF3F

    def cast(obj):
        """cast(itkLightObject obj) -> itkCannySegmentationLevelSetImageFilterIF3IF3F"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkCannySegmentationLevelSetImageFilterIF3IF3F self) -> itkCannySegmentationLevelSetImageFilterIF3IF3F"""
        return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCannySegmentationLevelSetImageFilterIF3IF3F

        Create a new object of the class itkCannySegmentationLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCannySegmentationLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCannySegmentationLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCannySegmentationLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCannySegmentationLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_Clone, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F.SetThreshold = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_SetThreshold, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F.GetThreshold = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetThreshold, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F.SetVariance = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_SetVariance, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F.GetVariance = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetVariance, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F.GetCannyImage = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetCannyImage, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F.GetPointer = new_instancemethod(_itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_GetPointer, None, itkCannySegmentationLevelSetImageFilterIF3IF3F)
itkCannySegmentationLevelSetImageFilterIF3IF3F_swigregister = _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_swigregister
itkCannySegmentationLevelSetImageFilterIF3IF3F_swigregister(itkCannySegmentationLevelSetImageFilterIF3IF3F)

def itkCannySegmentationLevelSetImageFilterIF3IF3F___New_orig__():
    """itkCannySegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> itkCannySegmentationLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F___New_orig__()

def itkCannySegmentationLevelSetImageFilterIF3IF3F_cast(obj):
    """itkCannySegmentationLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkCannySegmentationLevelSetImageFilterIF3IF3F"""
    return _itkCannySegmentationLevelSetImageFilterPython.itkCannySegmentationLevelSetImageFilterIF3IF3F_cast(obj)



