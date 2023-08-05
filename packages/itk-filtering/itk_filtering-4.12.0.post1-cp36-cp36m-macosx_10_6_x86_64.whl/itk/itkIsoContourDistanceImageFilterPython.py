# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIsoContourDistanceImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkIsoContourDistanceImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkIsoContourDistanceImageFilterPython')
    _itkIsoContourDistanceImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIsoContourDistanceImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkIsoContourDistanceImageFilterPython
            return _itkIsoContourDistanceImageFilterPython
        try:
            _mod = imp.load_module('_itkIsoContourDistanceImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkIsoContourDistanceImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIsoContourDistanceImageFilterPython
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


import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import ITKNarrowBandBasePython

def itkIsoContourDistanceImageFilterIF3IF3_New():
  return itkIsoContourDistanceImageFilterIF3IF3.New()


def itkIsoContourDistanceImageFilterIF2IF2_New():
  return itkIsoContourDistanceImageFilterIF2IF2.New()

class itkIsoContourDistanceImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkIsoContourDistanceImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoContourDistanceImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkIsoContourDistanceImageFilterIF2IF2_Pointer"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoContourDistanceImageFilterIF2IF2_Pointer":
        """Clone(itkIsoContourDistanceImageFilterIF2IF2 self) -> itkIsoContourDistanceImageFilterIF2IF2_Pointer"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_Clone(self)


    def SetLevelSetValue(self, _arg: 'double const') -> "void":
        """SetLevelSetValue(itkIsoContourDistanceImageFilterIF2IF2 self, double const _arg)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetLevelSetValue(self, _arg)


    def GetLevelSetValue(self) -> "double":
        """GetLevelSetValue(itkIsoContourDistanceImageFilterIF2IF2 self) -> double"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetLevelSetValue(self)


    def SetFarValue(self, _arg: 'float const') -> "void":
        """SetFarValue(itkIsoContourDistanceImageFilterIF2IF2 self, float const _arg)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetFarValue(self, _arg)


    def GetFarValue(self) -> "float":
        """GetFarValue(itkIsoContourDistanceImageFilterIF2IF2 self) -> float"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetFarValue(self)


    def SetNarrowBanding(self, _arg: 'bool const') -> "void":
        """SetNarrowBanding(itkIsoContourDistanceImageFilterIF2IF2 self, bool const _arg)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetNarrowBanding(self, _arg)


    def GetNarrowBanding(self) -> "bool":
        """GetNarrowBanding(itkIsoContourDistanceImageFilterIF2IF2 self) -> bool"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetNarrowBanding(self)


    def NarrowBandingOn(self) -> "void":
        """NarrowBandingOn(itkIsoContourDistanceImageFilterIF2IF2 self)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_NarrowBandingOn(self)


    def NarrowBandingOff(self) -> "void":
        """NarrowBandingOff(itkIsoContourDistanceImageFilterIF2IF2 self)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_NarrowBandingOff(self)


    def SetNarrowBand(self, ptr: 'itkNarrowBandBNI2F') -> "void":
        """SetNarrowBand(itkIsoContourDistanceImageFilterIF2IF2 self, itkNarrowBandBNI2F ptr)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetNarrowBand(self, ptr)


    def GetNarrowBand(self) -> "itkNarrowBandBNI2F_Pointer":
        """GetNarrowBand(itkIsoContourDistanceImageFilterIF2IF2 self) -> itkNarrowBandBNI2F_Pointer"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetNarrowBand(self)

    InputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_InputEqualityComparableCheck
    OutputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_OutputEqualityComparableCheck
    SameDimensionCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SameDimensionCheck
    DoubleConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    InputConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_InputConvertibleToOutputCheck
    OutputAdditiveOperatorsCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_OutputAdditiveOperatorsCheck
    InputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_InputOStreamWritableCheck
    OutputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_OutputOStreamWritableCheck
    __swig_destroy__ = _itkIsoContourDistanceImageFilterPython.delete_itkIsoContourDistanceImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkIsoContourDistanceImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkIsoContourDistanceImageFilterIF2IF2"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoContourDistanceImageFilterIF2IF2 *":
        """GetPointer(itkIsoContourDistanceImageFilterIF2IF2 self) -> itkIsoContourDistanceImageFilterIF2IF2"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoContourDistanceImageFilterIF2IF2

        Create a new object of the class itkIsoContourDistanceImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoContourDistanceImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoContourDistanceImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoContourDistanceImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoContourDistanceImageFilterIF2IF2.Clone = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_Clone, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.SetLevelSetValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetLevelSetValue, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.GetLevelSetValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetLevelSetValue, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.SetFarValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetFarValue, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.GetFarValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetFarValue, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.SetNarrowBanding = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetNarrowBanding, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.GetNarrowBanding = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetNarrowBanding, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.NarrowBandingOn = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_NarrowBandingOn, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.NarrowBandingOff = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_NarrowBandingOff, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.SetNarrowBand = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetNarrowBand, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.GetNarrowBand = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetNarrowBand, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2.GetPointer = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetPointer, None, itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2_swigregister = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_swigregister
itkIsoContourDistanceImageFilterIF2IF2_swigregister(itkIsoContourDistanceImageFilterIF2IF2)

def itkIsoContourDistanceImageFilterIF2IF2___New_orig__() -> "itkIsoContourDistanceImageFilterIF2IF2_Pointer":
    """itkIsoContourDistanceImageFilterIF2IF2___New_orig__() -> itkIsoContourDistanceImageFilterIF2IF2_Pointer"""
    return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2___New_orig__()

def itkIsoContourDistanceImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkIsoContourDistanceImageFilterIF2IF2 *":
    """itkIsoContourDistanceImageFilterIF2IF2_cast(itkLightObject obj) -> itkIsoContourDistanceImageFilterIF2IF2"""
    return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_cast(obj)

class itkIsoContourDistanceImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkIsoContourDistanceImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoContourDistanceImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkIsoContourDistanceImageFilterIF3IF3_Pointer"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoContourDistanceImageFilterIF3IF3_Pointer":
        """Clone(itkIsoContourDistanceImageFilterIF3IF3 self) -> itkIsoContourDistanceImageFilterIF3IF3_Pointer"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_Clone(self)


    def SetLevelSetValue(self, _arg: 'double const') -> "void":
        """SetLevelSetValue(itkIsoContourDistanceImageFilterIF3IF3 self, double const _arg)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetLevelSetValue(self, _arg)


    def GetLevelSetValue(self) -> "double":
        """GetLevelSetValue(itkIsoContourDistanceImageFilterIF3IF3 self) -> double"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetLevelSetValue(self)


    def SetFarValue(self, _arg: 'float const') -> "void":
        """SetFarValue(itkIsoContourDistanceImageFilterIF3IF3 self, float const _arg)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetFarValue(self, _arg)


    def GetFarValue(self) -> "float":
        """GetFarValue(itkIsoContourDistanceImageFilterIF3IF3 self) -> float"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetFarValue(self)


    def SetNarrowBanding(self, _arg: 'bool const') -> "void":
        """SetNarrowBanding(itkIsoContourDistanceImageFilterIF3IF3 self, bool const _arg)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetNarrowBanding(self, _arg)


    def GetNarrowBanding(self) -> "bool":
        """GetNarrowBanding(itkIsoContourDistanceImageFilterIF3IF3 self) -> bool"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetNarrowBanding(self)


    def NarrowBandingOn(self) -> "void":
        """NarrowBandingOn(itkIsoContourDistanceImageFilterIF3IF3 self)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_NarrowBandingOn(self)


    def NarrowBandingOff(self) -> "void":
        """NarrowBandingOff(itkIsoContourDistanceImageFilterIF3IF3 self)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_NarrowBandingOff(self)


    def SetNarrowBand(self, ptr: 'itkNarrowBandBNI3F') -> "void":
        """SetNarrowBand(itkIsoContourDistanceImageFilterIF3IF3 self, itkNarrowBandBNI3F ptr)"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetNarrowBand(self, ptr)


    def GetNarrowBand(self) -> "itkNarrowBandBNI3F_Pointer":
        """GetNarrowBand(itkIsoContourDistanceImageFilterIF3IF3 self) -> itkNarrowBandBNI3F_Pointer"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetNarrowBand(self)

    InputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_InputEqualityComparableCheck
    OutputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_OutputEqualityComparableCheck
    SameDimensionCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SameDimensionCheck
    DoubleConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    InputConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_InputConvertibleToOutputCheck
    OutputAdditiveOperatorsCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_OutputAdditiveOperatorsCheck
    InputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_InputOStreamWritableCheck
    OutputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_OutputOStreamWritableCheck
    __swig_destroy__ = _itkIsoContourDistanceImageFilterPython.delete_itkIsoContourDistanceImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkIsoContourDistanceImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkIsoContourDistanceImageFilterIF3IF3"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoContourDistanceImageFilterIF3IF3 *":
        """GetPointer(itkIsoContourDistanceImageFilterIF3IF3 self) -> itkIsoContourDistanceImageFilterIF3IF3"""
        return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoContourDistanceImageFilterIF3IF3

        Create a new object of the class itkIsoContourDistanceImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoContourDistanceImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoContourDistanceImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoContourDistanceImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoContourDistanceImageFilterIF3IF3.Clone = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_Clone, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.SetLevelSetValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetLevelSetValue, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.GetLevelSetValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetLevelSetValue, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.SetFarValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetFarValue, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.GetFarValue = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetFarValue, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.SetNarrowBanding = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetNarrowBanding, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.GetNarrowBanding = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetNarrowBanding, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.NarrowBandingOn = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_NarrowBandingOn, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.NarrowBandingOff = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_NarrowBandingOff, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.SetNarrowBand = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetNarrowBand, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.GetNarrowBand = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetNarrowBand, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3.GetPointer = new_instancemethod(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetPointer, None, itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3_swigregister = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_swigregister
itkIsoContourDistanceImageFilterIF3IF3_swigregister(itkIsoContourDistanceImageFilterIF3IF3)

def itkIsoContourDistanceImageFilterIF3IF3___New_orig__() -> "itkIsoContourDistanceImageFilterIF3IF3_Pointer":
    """itkIsoContourDistanceImageFilterIF3IF3___New_orig__() -> itkIsoContourDistanceImageFilterIF3IF3_Pointer"""
    return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3___New_orig__()

def itkIsoContourDistanceImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkIsoContourDistanceImageFilterIF3IF3 *":
    """itkIsoContourDistanceImageFilterIF3IF3_cast(itkLightObject obj) -> itkIsoContourDistanceImageFilterIF3IF3"""
    return _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_cast(obj)



