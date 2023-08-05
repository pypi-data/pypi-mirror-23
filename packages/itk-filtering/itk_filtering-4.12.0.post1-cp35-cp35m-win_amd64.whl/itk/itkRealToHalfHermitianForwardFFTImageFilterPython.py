# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRealToHalfHermitianForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRealToHalfHermitianForwardFFTImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRealToHalfHermitianForwardFFTImageFilterPython')
    _itkRealToHalfHermitianForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRealToHalfHermitianForwardFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRealToHalfHermitianForwardFFTImageFilterPython
            return _itkRealToHalfHermitianForwardFFTImageFilterPython
        try:
            _mod = imp.load_module('_itkRealToHalfHermitianForwardFFTImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRealToHalfHermitianForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRealToHalfHermitianForwardFFTImageFilterPython
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


import itkImageToImageFilterBPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkOffsetPython
import itkSizePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkIndexPython
import ITKCommonBasePython
import itkImageRegionPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_New():
  return itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New()


def itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_New():
  return itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New()

class itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2(itkImageToImageFilterBPython.itkImageToImageFilterIF2ICF2):
    """Proxy of C++ itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer":
        """__New_orig__() -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self) -> "unsigned long long":
        """GetSizeGreatestPrimeFactor(itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 self) -> unsigned long long"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor(self)


    def GetActualXDimensionIsOddOutput(self) -> "itkSimpleDataObjectDecoratorB const *":
        """GetActualXDimensionIsOddOutput(itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetActualXDimensionIsOddOutput(self)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 self) -> bool const &"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetActualXDimensionIsOdd(self)

    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2

    def cast(obj: 'itkLightObject') -> "itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 *":
        """cast(itkLightObject obj) -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 *":
        """GetPointer(itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 self) -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.GetSizeGreatestPrimeFactor = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor, None, itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.GetActualXDimensionIsOddOutput = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetActualXDimensionIsOddOutput, None, itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.GetActualXDimensionIsOdd = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetActualXDimensionIsOdd, None, itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.GetPointer = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetPointer, None, itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister(itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2)

def itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__() -> "itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer":
    """itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__() -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer"""
    return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__()

def itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(obj: 'itkLightObject') -> "itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 *":
    """itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(itkLightObject obj) -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2"""
    return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(obj)

class itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3(itkImageToImageFilterBPython.itkImageToImageFilterIF3ICF3):
    """Proxy of C++ itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer":
        """__New_orig__() -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self) -> "unsigned long long":
        """GetSizeGreatestPrimeFactor(itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 self) -> unsigned long long"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor(self)


    def GetActualXDimensionIsOddOutput(self) -> "itkSimpleDataObjectDecoratorB const *":
        """GetActualXDimensionIsOddOutput(itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetActualXDimensionIsOddOutput(self)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 self) -> bool const &"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetActualXDimensionIsOdd(self)

    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3

    def cast(obj: 'itkLightObject') -> "itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 *":
        """cast(itkLightObject obj) -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 *":
        """GetPointer(itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 self) -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3"""
        return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.GetSizeGreatestPrimeFactor = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor, None, itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.GetActualXDimensionIsOddOutput = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetActualXDimensionIsOddOutput, None, itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.GetActualXDimensionIsOdd = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetActualXDimensionIsOdd, None, itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.GetPointer = new_instancemethod(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetPointer, None, itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister(itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3)

def itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__() -> "itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer":
    """itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__() -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer"""
    return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__()

def itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(obj: 'itkLightObject') -> "itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 *":
    """itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(itkLightObject obj) -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3"""
    return _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(obj)



