# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkApproximateSignedDistanceMapImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkApproximateSignedDistanceMapImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkApproximateSignedDistanceMapImageFilterPython')
    _itkApproximateSignedDistanceMapImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkApproximateSignedDistanceMapImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkApproximateSignedDistanceMapImageFilterPython
            return _itkApproximateSignedDistanceMapImageFilterPython
        try:
            _mod = imp.load_module('_itkApproximateSignedDistanceMapImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkApproximateSignedDistanceMapImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkApproximateSignedDistanceMapImageFilterPython
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


import ITKCommonBasePython
import pyBasePython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkApproximateSignedDistanceMapImageFilterIF3IF3_New():
  return itkApproximateSignedDistanceMapImageFilterIF3IF3.New()


def itkApproximateSignedDistanceMapImageFilterIF2IF2_New():
  return itkApproximateSignedDistanceMapImageFilterIF2IF2.New()


def itkApproximateSignedDistanceMapImageFilterISS3ISS3_New():
  return itkApproximateSignedDistanceMapImageFilterISS3ISS3.New()


def itkApproximateSignedDistanceMapImageFilterISS2ISS2_New():
  return itkApproximateSignedDistanceMapImageFilterISS2ISS2.New()

class itkApproximateSignedDistanceMapImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkApproximateSignedDistanceMapImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkApproximateSignedDistanceMapImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkApproximateSignedDistanceMapImageFilterIF2IF2_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkApproximateSignedDistanceMapImageFilterIF2IF2_Pointer":
        """Clone(itkApproximateSignedDistanceMapImageFilterIF2IF2 self) -> itkApproximateSignedDistanceMapImageFilterIF2IF2_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_Clone(self)


    def SetInsideValue(self, _arg: 'float const') -> "void":
        """SetInsideValue(itkApproximateSignedDistanceMapImageFilterIF2IF2 self, float const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_SetInsideValue(self, _arg)


    def GetInsideValue(self) -> "float":
        """GetInsideValue(itkApproximateSignedDistanceMapImageFilterIF2IF2 self) -> float"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetInsideValue(self)


    def SetOutsideValue(self, _arg: 'float const') -> "void":
        """SetOutsideValue(itkApproximateSignedDistanceMapImageFilterIF2IF2 self, float const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_SetOutsideValue(self, _arg)


    def GetOutsideValue(self) -> "float":
        """GetOutsideValue(itkApproximateSignedDistanceMapImageFilterIF2IF2 self) -> float"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetOutsideValue(self)

    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_InputEqualityComparableCheck
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterIF2IF2"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkApproximateSignedDistanceMapImageFilterIF2IF2 *":
        """GetPointer(itkApproximateSignedDistanceMapImageFilterIF2IF2 self) -> itkApproximateSignedDistanceMapImageFilterIF2IF2"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterIF2IF2

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkApproximateSignedDistanceMapImageFilterIF2IF2.Clone = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_Clone, None, itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2.SetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_SetInsideValue, None, itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2.GetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetInsideValue, None, itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2.SetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_SetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2.GetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2.GetPointer = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetPointer, None, itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2_swigregister = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_swigregister
itkApproximateSignedDistanceMapImageFilterIF2IF2_swigregister(itkApproximateSignedDistanceMapImageFilterIF2IF2)

def itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__() -> "itkApproximateSignedDistanceMapImageFilterIF2IF2_Pointer":
    """itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__() -> itkApproximateSignedDistanceMapImageFilterIF2IF2_Pointer"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__()

def itkApproximateSignedDistanceMapImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterIF2IF2 *":
    """itkApproximateSignedDistanceMapImageFilterIF2IF2_cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterIF2IF2"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_cast(obj)

class itkApproximateSignedDistanceMapImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkApproximateSignedDistanceMapImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkApproximateSignedDistanceMapImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkApproximateSignedDistanceMapImageFilterIF3IF3_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkApproximateSignedDistanceMapImageFilterIF3IF3_Pointer":
        """Clone(itkApproximateSignedDistanceMapImageFilterIF3IF3 self) -> itkApproximateSignedDistanceMapImageFilterIF3IF3_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_Clone(self)


    def SetInsideValue(self, _arg: 'float const') -> "void":
        """SetInsideValue(itkApproximateSignedDistanceMapImageFilterIF3IF3 self, float const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_SetInsideValue(self, _arg)


    def GetInsideValue(self) -> "float":
        """GetInsideValue(itkApproximateSignedDistanceMapImageFilterIF3IF3 self) -> float"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetInsideValue(self)


    def SetOutsideValue(self, _arg: 'float const') -> "void":
        """SetOutsideValue(itkApproximateSignedDistanceMapImageFilterIF3IF3 self, float const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_SetOutsideValue(self, _arg)


    def GetOutsideValue(self) -> "float":
        """GetOutsideValue(itkApproximateSignedDistanceMapImageFilterIF3IF3 self) -> float"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetOutsideValue(self)

    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_InputEqualityComparableCheck
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterIF3IF3"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkApproximateSignedDistanceMapImageFilterIF3IF3 *":
        """GetPointer(itkApproximateSignedDistanceMapImageFilterIF3IF3 self) -> itkApproximateSignedDistanceMapImageFilterIF3IF3"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterIF3IF3

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkApproximateSignedDistanceMapImageFilterIF3IF3.Clone = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_Clone, None, itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3.SetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_SetInsideValue, None, itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3.GetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetInsideValue, None, itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3.SetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_SetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3.GetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3.GetPointer = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetPointer, None, itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3_swigregister = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_swigregister
itkApproximateSignedDistanceMapImageFilterIF3IF3_swigregister(itkApproximateSignedDistanceMapImageFilterIF3IF3)

def itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__() -> "itkApproximateSignedDistanceMapImageFilterIF3IF3_Pointer":
    """itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__() -> itkApproximateSignedDistanceMapImageFilterIF3IF3_Pointer"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__()

def itkApproximateSignedDistanceMapImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterIF3IF3 *":
    """itkApproximateSignedDistanceMapImageFilterIF3IF3_cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterIF3IF3"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_cast(obj)

class itkApproximateSignedDistanceMapImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkApproximateSignedDistanceMapImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkApproximateSignedDistanceMapImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkApproximateSignedDistanceMapImageFilterISS2ISS2_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkApproximateSignedDistanceMapImageFilterISS2ISS2_Pointer":
        """Clone(itkApproximateSignedDistanceMapImageFilterISS2ISS2 self) -> itkApproximateSignedDistanceMapImageFilterISS2ISS2_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_Clone(self)


    def SetInsideValue(self, _arg: 'short const') -> "void":
        """SetInsideValue(itkApproximateSignedDistanceMapImageFilterISS2ISS2 self, short const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_SetInsideValue(self, _arg)


    def GetInsideValue(self) -> "short":
        """GetInsideValue(itkApproximateSignedDistanceMapImageFilterISS2ISS2 self) -> short"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetInsideValue(self)


    def SetOutsideValue(self, _arg: 'short const') -> "void":
        """SetOutsideValue(itkApproximateSignedDistanceMapImageFilterISS2ISS2 self, short const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_SetOutsideValue(self, _arg)


    def GetOutsideValue(self) -> "short":
        """GetOutsideValue(itkApproximateSignedDistanceMapImageFilterISS2ISS2 self) -> short"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetOutsideValue(self)

    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_InputEqualityComparableCheck
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterISS2ISS2"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkApproximateSignedDistanceMapImageFilterISS2ISS2 *":
        """GetPointer(itkApproximateSignedDistanceMapImageFilterISS2ISS2 self) -> itkApproximateSignedDistanceMapImageFilterISS2ISS2"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterISS2ISS2

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkApproximateSignedDistanceMapImageFilterISS2ISS2.Clone = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_Clone, None, itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2.SetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_SetInsideValue, None, itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2.GetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetInsideValue, None, itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2.SetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_SetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2.GetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetPointer, None, itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2_swigregister = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_swigregister
itkApproximateSignedDistanceMapImageFilterISS2ISS2_swigregister(itkApproximateSignedDistanceMapImageFilterISS2ISS2)

def itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__() -> "itkApproximateSignedDistanceMapImageFilterISS2ISS2_Pointer":
    """itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__() -> itkApproximateSignedDistanceMapImageFilterISS2ISS2_Pointer"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__()

def itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterISS2ISS2 *":
    """itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterISS2ISS2"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast(obj)

class itkApproximateSignedDistanceMapImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkApproximateSignedDistanceMapImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkApproximateSignedDistanceMapImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkApproximateSignedDistanceMapImageFilterISS3ISS3_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkApproximateSignedDistanceMapImageFilterISS3ISS3_Pointer":
        """Clone(itkApproximateSignedDistanceMapImageFilterISS3ISS3 self) -> itkApproximateSignedDistanceMapImageFilterISS3ISS3_Pointer"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_Clone(self)


    def SetInsideValue(self, _arg: 'short const') -> "void":
        """SetInsideValue(itkApproximateSignedDistanceMapImageFilterISS3ISS3 self, short const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_SetInsideValue(self, _arg)


    def GetInsideValue(self) -> "short":
        """GetInsideValue(itkApproximateSignedDistanceMapImageFilterISS3ISS3 self) -> short"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetInsideValue(self)


    def SetOutsideValue(self, _arg: 'short const') -> "void":
        """SetOutsideValue(itkApproximateSignedDistanceMapImageFilterISS3ISS3 self, short const _arg)"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_SetOutsideValue(self, _arg)


    def GetOutsideValue(self) -> "short":
        """GetOutsideValue(itkApproximateSignedDistanceMapImageFilterISS3ISS3 self) -> short"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetOutsideValue(self)

    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_InputEqualityComparableCheck
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterISS3ISS3"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkApproximateSignedDistanceMapImageFilterISS3ISS3 *":
        """GetPointer(itkApproximateSignedDistanceMapImageFilterISS3ISS3 self) -> itkApproximateSignedDistanceMapImageFilterISS3ISS3"""
        return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterISS3ISS3

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkApproximateSignedDistanceMapImageFilterISS3ISS3.Clone = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_Clone, None, itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3.SetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_SetInsideValue, None, itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3.GetInsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetInsideValue, None, itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3.SetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_SetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3.GetOutsideValue = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetOutsideValue, None, itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetPointer, None, itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3_swigregister = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_swigregister
itkApproximateSignedDistanceMapImageFilterISS3ISS3_swigregister(itkApproximateSignedDistanceMapImageFilterISS3ISS3)

def itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__() -> "itkApproximateSignedDistanceMapImageFilterISS3ISS3_Pointer":
    """itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__() -> itkApproximateSignedDistanceMapImageFilterISS3ISS3_Pointer"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__()

def itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkApproximateSignedDistanceMapImageFilterISS3ISS3 *":
    """itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast(itkLightObject obj) -> itkApproximateSignedDistanceMapImageFilterISS3ISS3"""
    return _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast(obj)



