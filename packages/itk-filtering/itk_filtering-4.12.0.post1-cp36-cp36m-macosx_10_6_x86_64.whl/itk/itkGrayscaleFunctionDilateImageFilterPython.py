# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGrayscaleFunctionDilateImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGrayscaleFunctionDilateImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGrayscaleFunctionDilateImageFilterPython')
    _itkGrayscaleFunctionDilateImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGrayscaleFunctionDilateImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkGrayscaleFunctionDilateImageFilterPython
            return _itkGrayscaleFunctionDilateImageFilterPython
        try:
            _mod = imp.load_module('_itkGrayscaleFunctionDilateImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGrayscaleFunctionDilateImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGrayscaleFunctionDilateImageFilterPython
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
import itkGrayscaleFunctionErodeImageFilterPython
import itkFlatStructuringElementPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkNeighborhoodPython
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageBoundaryConditionPython

def itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_New():
  return itkGrayscaleFunctionDilateImageFilterIF3IF3SE3.New()


def itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_New():
  return itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3.New()


def itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_New():
  return itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3.New()


def itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_New():
  return itkGrayscaleFunctionDilateImageFilterIF2IF2SE2.New()


def itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_New():
  return itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2.New()


def itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_New():
  return itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2.New()

class itkGrayscaleFunctionDilateImageFilterIF2IF2SE2(itkGrayscaleFunctionErodeImageFilterPython.itkGrayscaleFunctionErodeImageFilterIF2IF2SE2_Superclass):
    """Proxy of C++ itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Pointer":
        """__New_orig__() -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Pointer":
        """Clone(itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 self) -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Clone(self)

    SameDimensionCheck1 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_SameDimensionCheck1
    SameDimensionCheck2 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_SameDimensionCheck2
    InputConvertibleToOutputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_InputConvertibleToOutputCheck
    KernelConvertibleToInputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_KernelConvertibleToInputCheck
    InputAdditiveOperatorsCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_InputAdditiveOperatorsCheck
    InputGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_InputGreaterThanComparableCheck
    KernelGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_KernelGreaterThanComparableCheck
    __swig_destroy__ = _itkGrayscaleFunctionDilateImageFilterPython.delete_itkGrayscaleFunctionDilateImageFilterIF2IF2SE2

    def cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 *":
        """cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 *":
        """GetPointer(itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 self) -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2

        Create a new object of the class itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFunctionDilateImageFilterIF2IF2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFunctionDilateImageFilterIF2IF2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFunctionDilateImageFilterIF2IF2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGrayscaleFunctionDilateImageFilterIF2IF2SE2.Clone = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Clone, None, itkGrayscaleFunctionDilateImageFilterIF2IF2SE2)
itkGrayscaleFunctionDilateImageFilterIF2IF2SE2.GetPointer = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_GetPointer, None, itkGrayscaleFunctionDilateImageFilterIF2IF2SE2)
itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_swigregister = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_swigregister
itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_swigregister(itkGrayscaleFunctionDilateImageFilterIF2IF2SE2)

def itkGrayscaleFunctionDilateImageFilterIF2IF2SE2___New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Pointer":
    """itkGrayscaleFunctionDilateImageFilterIF2IF2SE2___New_orig__() -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_Pointer"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2___New_orig__()

def itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIF2IF2SE2 *":
    """itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIF2IF2SE2"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF2IF2SE2_cast(obj)

class itkGrayscaleFunctionDilateImageFilterIF3IF3SE3(itkGrayscaleFunctionErodeImageFilterPython.itkGrayscaleFunctionErodeImageFilterIF3IF3SE3_Superclass):
    """Proxy of C++ itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Pointer":
        """__New_orig__() -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Pointer":
        """Clone(itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 self) -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Clone(self)

    SameDimensionCheck1 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_SameDimensionCheck1
    SameDimensionCheck2 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_SameDimensionCheck2
    InputConvertibleToOutputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_InputConvertibleToOutputCheck
    KernelConvertibleToInputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_KernelConvertibleToInputCheck
    InputAdditiveOperatorsCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_InputAdditiveOperatorsCheck
    InputGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_InputGreaterThanComparableCheck
    KernelGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_KernelGreaterThanComparableCheck
    __swig_destroy__ = _itkGrayscaleFunctionDilateImageFilterPython.delete_itkGrayscaleFunctionDilateImageFilterIF3IF3SE3

    def cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 *":
        """cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 *":
        """GetPointer(itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 self) -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3

        Create a new object of the class itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFunctionDilateImageFilterIF3IF3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFunctionDilateImageFilterIF3IF3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFunctionDilateImageFilterIF3IF3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGrayscaleFunctionDilateImageFilterIF3IF3SE3.Clone = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Clone, None, itkGrayscaleFunctionDilateImageFilterIF3IF3SE3)
itkGrayscaleFunctionDilateImageFilterIF3IF3SE3.GetPointer = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_GetPointer, None, itkGrayscaleFunctionDilateImageFilterIF3IF3SE3)
itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_swigregister = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_swigregister
itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_swigregister(itkGrayscaleFunctionDilateImageFilterIF3IF3SE3)

def itkGrayscaleFunctionDilateImageFilterIF3IF3SE3___New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Pointer":
    """itkGrayscaleFunctionDilateImageFilterIF3IF3SE3___New_orig__() -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_Pointer"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3___New_orig__()

def itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIF3IF3SE3 *":
    """itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIF3IF3SE3"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIF3IF3SE3_cast(obj)

class itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2(itkGrayscaleFunctionErodeImageFilterPython.itkGrayscaleFunctionErodeImageFilterISS2ISS2SE2_Superclass):
    """Proxy of C++ itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Pointer":
        """__New_orig__() -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Pointer":
        """Clone(itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 self) -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Clone(self)

    SameDimensionCheck1 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_SameDimensionCheck1
    SameDimensionCheck2 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_SameDimensionCheck2
    InputConvertibleToOutputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_InputConvertibleToOutputCheck
    KernelConvertibleToInputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_KernelConvertibleToInputCheck
    InputAdditiveOperatorsCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_InputAdditiveOperatorsCheck
    InputGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_InputGreaterThanComparableCheck
    KernelGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_KernelGreaterThanComparableCheck
    __swig_destroy__ = _itkGrayscaleFunctionDilateImageFilterPython.delete_itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2

    def cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 *":
        """cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 *":
        """GetPointer(itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 self) -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2

        Create a new object of the class itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2.Clone = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Clone, None, itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2)
itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2.GetPointer = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_GetPointer, None, itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2)
itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_swigregister = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_swigregister
itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_swigregister(itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2)

def itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2___New_orig__() -> "itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Pointer":
    """itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2___New_orig__() -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_Pointer"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2___New_orig__()

def itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2 *":
    """itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS2ISS2SE2_cast(obj)

class itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3(itkGrayscaleFunctionErodeImageFilterPython.itkGrayscaleFunctionErodeImageFilterISS3ISS3SE3_Superclass):
    """Proxy of C++ itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Pointer":
        """__New_orig__() -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Pointer":
        """Clone(itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 self) -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Clone(self)

    SameDimensionCheck1 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_SameDimensionCheck1
    SameDimensionCheck2 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_SameDimensionCheck2
    InputConvertibleToOutputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_InputConvertibleToOutputCheck
    KernelConvertibleToInputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_KernelConvertibleToInputCheck
    InputAdditiveOperatorsCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_InputAdditiveOperatorsCheck
    InputGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_InputGreaterThanComparableCheck
    KernelGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_KernelGreaterThanComparableCheck
    __swig_destroy__ = _itkGrayscaleFunctionDilateImageFilterPython.delete_itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3

    def cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 *":
        """cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 *":
        """GetPointer(itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 self) -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3

        Create a new object of the class itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3.Clone = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Clone, None, itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3)
itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3.GetPointer = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_GetPointer, None, itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3)
itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_swigregister = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_swigregister
itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_swigregister(itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3)

def itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3___New_orig__() -> "itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Pointer":
    """itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3___New_orig__() -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_Pointer"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3___New_orig__()

def itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3 *":
    """itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterISS3ISS3SE3_cast(obj)

class itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2(itkGrayscaleFunctionErodeImageFilterPython.itkGrayscaleFunctionErodeImageFilterIUC2IUC2SE2_Superclass):
    """Proxy of C++ itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Pointer":
        """__New_orig__() -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Pointer":
        """Clone(itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 self) -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Clone(self)

    SameDimensionCheck1 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_SameDimensionCheck1
    SameDimensionCheck2 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_SameDimensionCheck2
    InputConvertibleToOutputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_InputConvertibleToOutputCheck
    KernelConvertibleToInputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_KernelConvertibleToInputCheck
    InputAdditiveOperatorsCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_InputAdditiveOperatorsCheck
    InputGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_InputGreaterThanComparableCheck
    KernelGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_KernelGreaterThanComparableCheck
    __swig_destroy__ = _itkGrayscaleFunctionDilateImageFilterPython.delete_itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2

    def cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 *":
        """cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 *":
        """GetPointer(itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 self) -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2

        Create a new object of the class itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2.Clone = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Clone, None, itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2)
itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2.GetPointer = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_GetPointer, None, itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2)
itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_swigregister = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_swigregister
itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_swigregister(itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2)

def itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2___New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Pointer":
    """itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2___New_orig__() -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_Pointer"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2___New_orig__()

def itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2 *":
    """itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC2IUC2SE2_cast(obj)

class itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3(itkGrayscaleFunctionErodeImageFilterPython.itkGrayscaleFunctionErodeImageFilterIUC3IUC3SE3_Superclass):
    """Proxy of C++ itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Pointer":
        """__New_orig__() -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Pointer":
        """Clone(itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 self) -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Pointer"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Clone(self)

    SameDimensionCheck1 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_SameDimensionCheck1
    SameDimensionCheck2 = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_SameDimensionCheck2
    InputConvertibleToOutputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_InputConvertibleToOutputCheck
    KernelConvertibleToInputCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_KernelConvertibleToInputCheck
    InputAdditiveOperatorsCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_InputAdditiveOperatorsCheck
    InputGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_InputGreaterThanComparableCheck
    KernelGreaterThanComparableCheck = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_KernelGreaterThanComparableCheck
    __swig_destroy__ = _itkGrayscaleFunctionDilateImageFilterPython.delete_itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3

    def cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 *":
        """cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 *":
        """GetPointer(itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 self) -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3"""
        return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3

        Create a new object of the class itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3.Clone = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Clone, None, itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3)
itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3.GetPointer = new_instancemethod(_itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_GetPointer, None, itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3)
itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_swigregister = _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_swigregister
itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_swigregister(itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3)

def itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3___New_orig__() -> "itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Pointer":
    """itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3___New_orig__() -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_Pointer"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3___New_orig__()

def itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_cast(obj: 'itkLightObject') -> "itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3 *":
    """itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_cast(itkLightObject obj) -> itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3"""
    return _itkGrayscaleFunctionDilateImageFilterPython.itkGrayscaleFunctionDilateImageFilterIUC3IUC3SE3_cast(obj)



