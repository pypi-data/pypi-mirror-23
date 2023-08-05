# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkParallelSparseFieldLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkParallelSparseFieldLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkParallelSparseFieldLevelSetImageFilterPython')
    _itkParallelSparseFieldLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkParallelSparseFieldLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkParallelSparseFieldLevelSetImageFilterPython
            return _itkParallelSparseFieldLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkParallelSparseFieldLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkParallelSparseFieldLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkParallelSparseFieldLevelSetImageFilterPython
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


import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkSizePython
import pyBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython

def itkSparseFieldLayerPSFLSNI3_New():
  return itkSparseFieldLayerPSFLSNI3.New()


def itkSparseFieldLayerPSFLSNI2_New():
  return itkSparseFieldLayerPSFLSNI2.New()


def itkParallelSparseFieldLevelSetImageFilterIF3IF3_New():
  return itkParallelSparseFieldLevelSetImageFilterIF3IF3.New()


def itkParallelSparseFieldLevelSetImageFilterIF2IF2_New():
  return itkParallelSparseFieldLevelSetImageFilterIF2IF2.New()

class itkParallelSparseFieldLevelSetImageFilterIF2IF2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF2IF2):
    """Proxy of C++ itkParallelSparseFieldLevelSetImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkParallelSparseFieldLevelSetImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkParallelSparseFieldLevelSetImageFilterIF2IF2_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkParallelSparseFieldLevelSetImageFilterIF2IF2_Pointer":
        """Clone(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self) -> itkParallelSparseFieldLevelSetImageFilterIF2IF2_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_Clone(self)


    def SetNumberOfLayers(self, _arg: 'signed char const') -> "void":
        """SetNumberOfLayers(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self, signed char const _arg)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_SetNumberOfLayers(self, _arg)


    def GetNumberOfLayers(self) -> "signed char":
        """GetNumberOfLayers(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self) -> signed char"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetNumberOfLayers(self)


    def SetIsoSurfaceValue(self, _arg: 'float const') -> "void":
        """SetIsoSurfaceValue(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self, float const _arg)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_SetIsoSurfaceValue(self, _arg)


    def GetIsoSurfaceValue(self) -> "float":
        """GetIsoSurfaceValue(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self) -> float"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetIsoSurfaceValue(self)


    def GetActiveListForIndex(self, index: 'itkIndex2') -> "itkSparseFieldLayerPSFLSNI2_Pointer":
        """GetActiveListForIndex(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self, itkIndex2 index) -> itkSparseFieldLayerPSFLSNI2_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetActiveListForIndex(self, index)

    OutputEqualityComparableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_OutputEqualityComparableCheck
    DoubleConvertibleToOutputCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    OutputOStreamWritableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_OutputOStreamWritableCheck
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkParallelSparseFieldLevelSetImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkParallelSparseFieldLevelSetImageFilterIF2IF2"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkParallelSparseFieldLevelSetImageFilterIF2IF2 *":
        """GetPointer(itkParallelSparseFieldLevelSetImageFilterIF2IF2 self) -> itkParallelSparseFieldLevelSetImageFilterIF2IF2"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkParallelSparseFieldLevelSetImageFilterIF2IF2

        Create a new object of the class itkParallelSparseFieldLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParallelSparseFieldLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParallelSparseFieldLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParallelSparseFieldLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkParallelSparseFieldLevelSetImageFilterIF2IF2.Clone = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_Clone, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2.SetNumberOfLayers = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_SetNumberOfLayers, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2.GetNumberOfLayers = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetNumberOfLayers, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2.SetIsoSurfaceValue = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_SetIsoSurfaceValue, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2.GetIsoSurfaceValue = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetIsoSurfaceValue, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2.GetActiveListForIndex = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetActiveListForIndex, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2.GetPointer = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetPointer, None, itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2_swigregister = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_swigregister
itkParallelSparseFieldLevelSetImageFilterIF2IF2_swigregister(itkParallelSparseFieldLevelSetImageFilterIF2IF2)

def itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__() -> "itkParallelSparseFieldLevelSetImageFilterIF2IF2_Pointer":
    """itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__() -> itkParallelSparseFieldLevelSetImageFilterIF2IF2_Pointer"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__()

def itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkParallelSparseFieldLevelSetImageFilterIF2IF2 *":
    """itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast(itkLightObject obj) -> itkParallelSparseFieldLevelSetImageFilterIF2IF2"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast(obj)

class itkParallelSparseFieldLevelSetImageFilterIF3IF3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF3IF3):
    """Proxy of C++ itkParallelSparseFieldLevelSetImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkParallelSparseFieldLevelSetImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkParallelSparseFieldLevelSetImageFilterIF3IF3_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkParallelSparseFieldLevelSetImageFilterIF3IF3_Pointer":
        """Clone(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self) -> itkParallelSparseFieldLevelSetImageFilterIF3IF3_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_Clone(self)


    def SetNumberOfLayers(self, _arg: 'signed char const') -> "void":
        """SetNumberOfLayers(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self, signed char const _arg)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_SetNumberOfLayers(self, _arg)


    def GetNumberOfLayers(self) -> "signed char":
        """GetNumberOfLayers(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self) -> signed char"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetNumberOfLayers(self)


    def SetIsoSurfaceValue(self, _arg: 'float const') -> "void":
        """SetIsoSurfaceValue(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self, float const _arg)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_SetIsoSurfaceValue(self, _arg)


    def GetIsoSurfaceValue(self) -> "float":
        """GetIsoSurfaceValue(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self) -> float"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetIsoSurfaceValue(self)


    def GetActiveListForIndex(self, index: 'itkIndex3') -> "itkSparseFieldLayerPSFLSNI3_Pointer":
        """GetActiveListForIndex(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self, itkIndex3 index) -> itkSparseFieldLayerPSFLSNI3_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetActiveListForIndex(self, index)

    OutputEqualityComparableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_OutputEqualityComparableCheck
    DoubleConvertibleToOutputCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    OutputOStreamWritableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_OutputOStreamWritableCheck
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkParallelSparseFieldLevelSetImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkParallelSparseFieldLevelSetImageFilterIF3IF3"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkParallelSparseFieldLevelSetImageFilterIF3IF3 *":
        """GetPointer(itkParallelSparseFieldLevelSetImageFilterIF3IF3 self) -> itkParallelSparseFieldLevelSetImageFilterIF3IF3"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkParallelSparseFieldLevelSetImageFilterIF3IF3

        Create a new object of the class itkParallelSparseFieldLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParallelSparseFieldLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParallelSparseFieldLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParallelSparseFieldLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkParallelSparseFieldLevelSetImageFilterIF3IF3.Clone = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_Clone, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3.SetNumberOfLayers = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_SetNumberOfLayers, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3.GetNumberOfLayers = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetNumberOfLayers, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3.SetIsoSurfaceValue = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_SetIsoSurfaceValue, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3.GetIsoSurfaceValue = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetIsoSurfaceValue, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3.GetActiveListForIndex = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetActiveListForIndex, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3.GetPointer = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetPointer, None, itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3_swigregister = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_swigregister
itkParallelSparseFieldLevelSetImageFilterIF3IF3_swigregister(itkParallelSparseFieldLevelSetImageFilterIF3IF3)

def itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__() -> "itkParallelSparseFieldLevelSetImageFilterIF3IF3_Pointer":
    """itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__() -> itkParallelSparseFieldLevelSetImageFilterIF3IF3_Pointer"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__()

def itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkParallelSparseFieldLevelSetImageFilterIF3IF3 *":
    """itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast(itkLightObject obj) -> itkParallelSparseFieldLevelSetImageFilterIF3IF3"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast(obj)

class itkParallelSparseFieldLevelSetNodeI2(object):
    """Proxy of C++ itkParallelSparseFieldLevelSetNodeI2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkParallelSparseFieldLevelSetNodeI2 self) -> itkParallelSparseFieldLevelSetNodeI2
        __init__(itkParallelSparseFieldLevelSetNodeI2 self, itkParallelSparseFieldLevelSetNodeI2 arg0) -> itkParallelSparseFieldLevelSetNodeI2
        """
        _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI2_swiginit(self, _itkParallelSparseFieldLevelSetImageFilterPython.new_itkParallelSparseFieldLevelSetNodeI2(*args))
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetNodeI2
itkParallelSparseFieldLevelSetNodeI2_swigregister = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI2_swigregister
itkParallelSparseFieldLevelSetNodeI2_swigregister(itkParallelSparseFieldLevelSetNodeI2)

class itkParallelSparseFieldLevelSetNodeI3(object):
    """Proxy of C++ itkParallelSparseFieldLevelSetNodeI3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkParallelSparseFieldLevelSetNodeI3 self) -> itkParallelSparseFieldLevelSetNodeI3
        __init__(itkParallelSparseFieldLevelSetNodeI3 self, itkParallelSparseFieldLevelSetNodeI3 arg0) -> itkParallelSparseFieldLevelSetNodeI3
        """
        _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI3_swiginit(self, _itkParallelSparseFieldLevelSetImageFilterPython.new_itkParallelSparseFieldLevelSetNodeI3(*args))
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetNodeI3
itkParallelSparseFieldLevelSetNodeI3_swigregister = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI3_swigregister
itkParallelSparseFieldLevelSetNodeI3_swigregister(itkParallelSparseFieldLevelSetNodeI3)

class itkSparseFieldLayerPSFLSNI2(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkSparseFieldLayerPSFLSNI2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSparseFieldLayerPSFLSNI2_Pointer":
        """__New_orig__() -> itkSparseFieldLayerPSFLSNI2_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSparseFieldLayerPSFLSNI2_Pointer":
        """Clone(itkSparseFieldLayerPSFLSNI2 self) -> itkSparseFieldLayerPSFLSNI2_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Clone(self)


    def Front(self, *args) -> "itkParallelSparseFieldLevelSetNodeI2 const *":
        """
        Front(itkSparseFieldLayerPSFLSNI2 self) -> itkParallelSparseFieldLevelSetNodeI2
        Front(itkSparseFieldLayerPSFLSNI2 self) -> itkParallelSparseFieldLevelSetNodeI2
        """
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Front(self, *args)


    def PopFront(self) -> "void":
        """PopFront(itkSparseFieldLayerPSFLSNI2 self)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_PopFront(self)


    def PushFront(self, n: 'itkParallelSparseFieldLevelSetNodeI2') -> "void":
        """PushFront(itkSparseFieldLayerPSFLSNI2 self, itkParallelSparseFieldLevelSetNodeI2 n)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_PushFront(self, n)


    def Unlink(self, n: 'itkParallelSparseFieldLevelSetNodeI2') -> "void":
        """Unlink(itkSparseFieldLayerPSFLSNI2 self, itkParallelSparseFieldLevelSetNodeI2 n)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Unlink(self, n)


    def Empty(self) -> "bool":
        """Empty(itkSparseFieldLayerPSFLSNI2 self) -> bool"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Empty(self)


    def Size(self) -> "unsigned int":
        """Size(itkSparseFieldLayerPSFLSNI2 self) -> unsigned int"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Size(self)


    def SplitRegions(self, num: 'int') -> "std::vector< itkSparseFieldLayerPSFLSNI2::RegionType,std::allocator< itkSparseFieldLayerPSFLSNI2::RegionType > >":
        """SplitRegions(itkSparseFieldLayerPSFLSNI2 self, int num) -> std::vector< itkSparseFieldLayerPSFLSNI2::RegionType,std::allocator< itkSparseFieldLayerPSFLSNI2::RegionType > >"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_SplitRegions(self, num)

    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLayerPSFLSNI2

    def cast(obj: 'itkLightObject') -> "itkSparseFieldLayerPSFLSNI2 *":
        """cast(itkLightObject obj) -> itkSparseFieldLayerPSFLSNI2"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSparseFieldLayerPSFLSNI2 *":
        """GetPointer(itkSparseFieldLayerPSFLSNI2 self) -> itkSparseFieldLayerPSFLSNI2"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSparseFieldLayerPSFLSNI2

        Create a new object of the class itkSparseFieldLayerPSFLSNI2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLayerPSFLSNI2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLayerPSFLSNI2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLayerPSFLSNI2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSparseFieldLayerPSFLSNI2.Clone = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Clone, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.Front = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Front, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.PopFront = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_PopFront, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.PushFront = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_PushFront, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.Unlink = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Unlink, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.Empty = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Empty, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.Size = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Size, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.SplitRegions = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_SplitRegions, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2.GetPointer = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_GetPointer, None, itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2_swigregister = _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_swigregister
itkSparseFieldLayerPSFLSNI2_swigregister(itkSparseFieldLayerPSFLSNI2)

def itkSparseFieldLayerPSFLSNI2___New_orig__() -> "itkSparseFieldLayerPSFLSNI2_Pointer":
    """itkSparseFieldLayerPSFLSNI2___New_orig__() -> itkSparseFieldLayerPSFLSNI2_Pointer"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2___New_orig__()

def itkSparseFieldLayerPSFLSNI2_cast(obj: 'itkLightObject') -> "itkSparseFieldLayerPSFLSNI2 *":
    """itkSparseFieldLayerPSFLSNI2_cast(itkLightObject obj) -> itkSparseFieldLayerPSFLSNI2"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_cast(obj)

class itkSparseFieldLayerPSFLSNI3(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkSparseFieldLayerPSFLSNI3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSparseFieldLayerPSFLSNI3_Pointer":
        """__New_orig__() -> itkSparseFieldLayerPSFLSNI3_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSparseFieldLayerPSFLSNI3_Pointer":
        """Clone(itkSparseFieldLayerPSFLSNI3 self) -> itkSparseFieldLayerPSFLSNI3_Pointer"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Clone(self)


    def Front(self, *args) -> "itkParallelSparseFieldLevelSetNodeI3 const *":
        """
        Front(itkSparseFieldLayerPSFLSNI3 self) -> itkParallelSparseFieldLevelSetNodeI3
        Front(itkSparseFieldLayerPSFLSNI3 self) -> itkParallelSparseFieldLevelSetNodeI3
        """
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Front(self, *args)


    def PopFront(self) -> "void":
        """PopFront(itkSparseFieldLayerPSFLSNI3 self)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_PopFront(self)


    def PushFront(self, n: 'itkParallelSparseFieldLevelSetNodeI3') -> "void":
        """PushFront(itkSparseFieldLayerPSFLSNI3 self, itkParallelSparseFieldLevelSetNodeI3 n)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_PushFront(self, n)


    def Unlink(self, n: 'itkParallelSparseFieldLevelSetNodeI3') -> "void":
        """Unlink(itkSparseFieldLayerPSFLSNI3 self, itkParallelSparseFieldLevelSetNodeI3 n)"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Unlink(self, n)


    def Empty(self) -> "bool":
        """Empty(itkSparseFieldLayerPSFLSNI3 self) -> bool"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Empty(self)


    def Size(self) -> "unsigned int":
        """Size(itkSparseFieldLayerPSFLSNI3 self) -> unsigned int"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Size(self)


    def SplitRegions(self, num: 'int') -> "std::vector< itkSparseFieldLayerPSFLSNI3::RegionType,std::allocator< itkSparseFieldLayerPSFLSNI3::RegionType > >":
        """SplitRegions(itkSparseFieldLayerPSFLSNI3 self, int num) -> std::vector< itkSparseFieldLayerPSFLSNI3::RegionType,std::allocator< itkSparseFieldLayerPSFLSNI3::RegionType > >"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_SplitRegions(self, num)

    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLayerPSFLSNI3

    def cast(obj: 'itkLightObject') -> "itkSparseFieldLayerPSFLSNI3 *":
        """cast(itkLightObject obj) -> itkSparseFieldLayerPSFLSNI3"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSparseFieldLayerPSFLSNI3 *":
        """GetPointer(itkSparseFieldLayerPSFLSNI3 self) -> itkSparseFieldLayerPSFLSNI3"""
        return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSparseFieldLayerPSFLSNI3

        Create a new object of the class itkSparseFieldLayerPSFLSNI3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLayerPSFLSNI3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLayerPSFLSNI3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLayerPSFLSNI3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSparseFieldLayerPSFLSNI3.Clone = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Clone, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.Front = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Front, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.PopFront = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_PopFront, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.PushFront = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_PushFront, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.Unlink = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Unlink, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.Empty = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Empty, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.Size = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Size, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.SplitRegions = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_SplitRegions, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3.GetPointer = new_instancemethod(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_GetPointer, None, itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3_swigregister = _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_swigregister
itkSparseFieldLayerPSFLSNI3_swigregister(itkSparseFieldLayerPSFLSNI3)

def itkSparseFieldLayerPSFLSNI3___New_orig__() -> "itkSparseFieldLayerPSFLSNI3_Pointer":
    """itkSparseFieldLayerPSFLSNI3___New_orig__() -> itkSparseFieldLayerPSFLSNI3_Pointer"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3___New_orig__()

def itkSparseFieldLayerPSFLSNI3_cast(obj: 'itkLightObject') -> "itkSparseFieldLayerPSFLSNI3 *":
    """itkSparseFieldLayerPSFLSNI3_cast(itkLightObject obj) -> itkSparseFieldLayerPSFLSNI3"""
    return _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_cast(obj)



