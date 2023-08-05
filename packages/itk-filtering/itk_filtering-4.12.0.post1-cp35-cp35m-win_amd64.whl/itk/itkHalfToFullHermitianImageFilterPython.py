# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHalfToFullHermitianImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkHalfToFullHermitianImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkHalfToFullHermitianImageFilterPython')
    _itkHalfToFullHermitianImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHalfToFullHermitianImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHalfToFullHermitianImageFilterPython
            return _itkHalfToFullHermitianImageFilterPython
        try:
            _mod = imp.load_module('_itkHalfToFullHermitianImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkHalfToFullHermitianImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHalfToFullHermitianImageFilterPython
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
import itkImageToImageFilterBPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkHalfToFullHermitianImageFilterICF3_New():
  return itkHalfToFullHermitianImageFilterICF3.New()


def itkHalfToFullHermitianImageFilterICF2_New():
  return itkHalfToFullHermitianImageFilterICF2.New()

class itkHalfToFullHermitianImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    """Proxy of C++ itkHalfToFullHermitianImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHalfToFullHermitianImageFilterICF2_Pointer":
        """__New_orig__() -> itkHalfToFullHermitianImageFilterICF2_Pointer"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHalfToFullHermitianImageFilterICF2_Pointer":
        """Clone(itkHalfToFullHermitianImageFilterICF2 self) -> itkHalfToFullHermitianImageFilterICF2_Pointer"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_Clone(self)


    def SetActualXDimensionIsOddInput(self, _arg: 'itkSimpleDataObjectDecoratorB') -> "void":
        """SetActualXDimensionIsOddInput(itkHalfToFullHermitianImageFilterICF2 self, itkSimpleDataObjectDecoratorB _arg)"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOddInput(self, _arg)


    def SetActualXDimensionIsOdd(self, *args) -> "void":
        """
        SetActualXDimensionIsOdd(itkHalfToFullHermitianImageFilterICF2 self, itkSimpleDataObjectDecoratorB _arg)
        SetActualXDimensionIsOdd(itkHalfToFullHermitianImageFilterICF2 self, bool const & _arg)
        """
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOdd(self, *args)


    def GetActualXDimensionIsOddInput(self) -> "itkSimpleDataObjectDecoratorB const *":
        """GetActualXDimensionIsOddInput(itkHalfToFullHermitianImageFilterICF2 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOddInput(self)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkHalfToFullHermitianImageFilterICF2 self) -> bool const &"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOdd(self)


    def ActualXDimensionIsOddOn(self) -> "void":
        """ActualXDimensionIsOddOn(itkHalfToFullHermitianImageFilterICF2 self)"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOn(self)


    def ActualXDimensionIsOddOff(self) -> "void":
        """ActualXDimensionIsOddOff(itkHalfToFullHermitianImageFilterICF2 self)"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOff(self)

    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF2

    def cast(obj: 'itkLightObject') -> "itkHalfToFullHermitianImageFilterICF2 *":
        """cast(itkLightObject obj) -> itkHalfToFullHermitianImageFilterICF2"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHalfToFullHermitianImageFilterICF2 *":
        """GetPointer(itkHalfToFullHermitianImageFilterICF2 self) -> itkHalfToFullHermitianImageFilterICF2"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF2

        Create a new object of the class itkHalfToFullHermitianImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHalfToFullHermitianImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHalfToFullHermitianImageFilterICF2.Clone = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_Clone, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.SetActualXDimensionIsOddInput = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOddInput, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.SetActualXDimensionIsOdd = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOdd, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.GetActualXDimensionIsOddInput = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOddInput, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.GetActualXDimensionIsOdd = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOdd, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.ActualXDimensionIsOddOn = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOn, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.ActualXDimensionIsOddOff = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOff, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2.GetPointer = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetPointer, None, itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2_swigregister = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_swigregister
itkHalfToFullHermitianImageFilterICF2_swigregister(itkHalfToFullHermitianImageFilterICF2)

def itkHalfToFullHermitianImageFilterICF2___New_orig__() -> "itkHalfToFullHermitianImageFilterICF2_Pointer":
    """itkHalfToFullHermitianImageFilterICF2___New_orig__() -> itkHalfToFullHermitianImageFilterICF2_Pointer"""
    return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2___New_orig__()

def itkHalfToFullHermitianImageFilterICF2_cast(obj: 'itkLightObject') -> "itkHalfToFullHermitianImageFilterICF2 *":
    """itkHalfToFullHermitianImageFilterICF2_cast(itkLightObject obj) -> itkHalfToFullHermitianImageFilterICF2"""
    return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_cast(obj)

class itkHalfToFullHermitianImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    """Proxy of C++ itkHalfToFullHermitianImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHalfToFullHermitianImageFilterICF3_Pointer":
        """__New_orig__() -> itkHalfToFullHermitianImageFilterICF3_Pointer"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHalfToFullHermitianImageFilterICF3_Pointer":
        """Clone(itkHalfToFullHermitianImageFilterICF3 self) -> itkHalfToFullHermitianImageFilterICF3_Pointer"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_Clone(self)


    def SetActualXDimensionIsOddInput(self, _arg: 'itkSimpleDataObjectDecoratorB') -> "void":
        """SetActualXDimensionIsOddInput(itkHalfToFullHermitianImageFilterICF3 self, itkSimpleDataObjectDecoratorB _arg)"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOddInput(self, _arg)


    def SetActualXDimensionIsOdd(self, *args) -> "void":
        """
        SetActualXDimensionIsOdd(itkHalfToFullHermitianImageFilterICF3 self, itkSimpleDataObjectDecoratorB _arg)
        SetActualXDimensionIsOdd(itkHalfToFullHermitianImageFilterICF3 self, bool const & _arg)
        """
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOdd(self, *args)


    def GetActualXDimensionIsOddInput(self) -> "itkSimpleDataObjectDecoratorB const *":
        """GetActualXDimensionIsOddInput(itkHalfToFullHermitianImageFilterICF3 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOddInput(self)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkHalfToFullHermitianImageFilterICF3 self) -> bool const &"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOdd(self)


    def ActualXDimensionIsOddOn(self) -> "void":
        """ActualXDimensionIsOddOn(itkHalfToFullHermitianImageFilterICF3 self)"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOn(self)


    def ActualXDimensionIsOddOff(self) -> "void":
        """ActualXDimensionIsOddOff(itkHalfToFullHermitianImageFilterICF3 self)"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOff(self)

    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF3

    def cast(obj: 'itkLightObject') -> "itkHalfToFullHermitianImageFilterICF3 *":
        """cast(itkLightObject obj) -> itkHalfToFullHermitianImageFilterICF3"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHalfToFullHermitianImageFilterICF3 *":
        """GetPointer(itkHalfToFullHermitianImageFilterICF3 self) -> itkHalfToFullHermitianImageFilterICF3"""
        return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF3

        Create a new object of the class itkHalfToFullHermitianImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHalfToFullHermitianImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHalfToFullHermitianImageFilterICF3.Clone = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_Clone, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.SetActualXDimensionIsOddInput = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOddInput, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.SetActualXDimensionIsOdd = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOdd, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.GetActualXDimensionIsOddInput = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOddInput, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.GetActualXDimensionIsOdd = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOdd, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.ActualXDimensionIsOddOn = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOn, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.ActualXDimensionIsOddOff = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOff, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3.GetPointer = new_instancemethod(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetPointer, None, itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3_swigregister = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_swigregister
itkHalfToFullHermitianImageFilterICF3_swigregister(itkHalfToFullHermitianImageFilterICF3)

def itkHalfToFullHermitianImageFilterICF3___New_orig__() -> "itkHalfToFullHermitianImageFilterICF3_Pointer":
    """itkHalfToFullHermitianImageFilterICF3___New_orig__() -> itkHalfToFullHermitianImageFilterICF3_Pointer"""
    return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3___New_orig__()

def itkHalfToFullHermitianImageFilterICF3_cast(obj: 'itkLightObject') -> "itkHalfToFullHermitianImageFilterICF3 *":
    """itkHalfToFullHermitianImageFilterICF3_cast(itkLightObject obj) -> itkHalfToFullHermitianImageFilterICF3"""
    return _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_cast(obj)



