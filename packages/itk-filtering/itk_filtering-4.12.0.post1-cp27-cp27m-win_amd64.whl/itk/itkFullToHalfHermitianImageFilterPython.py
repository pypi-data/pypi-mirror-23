# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFullToHalfHermitianImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFullToHalfHermitianImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFullToHalfHermitianImageFilterPython')
    _itkFullToHalfHermitianImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFullToHalfHermitianImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFullToHalfHermitianImageFilterPython
            return _itkFullToHalfHermitianImageFilterPython
        try:
            _mod = imp.load_module('_itkFullToHalfHermitianImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFullToHalfHermitianImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFullToHalfHermitianImageFilterPython
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


import itkSimpleDataObjectDecoratorPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkArrayPython
import ITKCommonBasePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageToImageFilterBPython
import itkImagePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkFullToHalfHermitianImageFilterICF3_New():
  return itkFullToHalfHermitianImageFilterICF3.New()


def itkFullToHalfHermitianImageFilterICF2_New():
  return itkFullToHalfHermitianImageFilterICF2.New()

class itkFullToHalfHermitianImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    """Proxy of C++ itkFullToHalfHermitianImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkFullToHalfHermitianImageFilterICF2_Pointer"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkFullToHalfHermitianImageFilterICF2 self) -> itkFullToHalfHermitianImageFilterICF2_Pointer"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_Clone(self)


    def GetActualXDimensionIsOddOutput(self):
        """GetActualXDimensionIsOddOutput(itkFullToHalfHermitianImageFilterICF2 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetActualXDimensionIsOddOutput(self)


    def GetActualXDimensionIsOdd(self):
        """GetActualXDimensionIsOdd(itkFullToHalfHermitianImageFilterICF2 self) -> bool const &"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetActualXDimensionIsOdd(self)

    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkFullToHalfHermitianImageFilterICF2"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkFullToHalfHermitianImageFilterICF2 self) -> itkFullToHalfHermitianImageFilterICF2"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICF2

        Create a new object of the class itkFullToHalfHermitianImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFullToHalfHermitianImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFullToHalfHermitianImageFilterICF2.Clone = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_Clone, None, itkFullToHalfHermitianImageFilterICF2)
itkFullToHalfHermitianImageFilterICF2.GetActualXDimensionIsOddOutput = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetActualXDimensionIsOddOutput, None, itkFullToHalfHermitianImageFilterICF2)
itkFullToHalfHermitianImageFilterICF2.GetActualXDimensionIsOdd = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetActualXDimensionIsOdd, None, itkFullToHalfHermitianImageFilterICF2)
itkFullToHalfHermitianImageFilterICF2.GetPointer = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetPointer, None, itkFullToHalfHermitianImageFilterICF2)
itkFullToHalfHermitianImageFilterICF2_swigregister = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_swigregister
itkFullToHalfHermitianImageFilterICF2_swigregister(itkFullToHalfHermitianImageFilterICF2)

def itkFullToHalfHermitianImageFilterICF2___New_orig__():
    """itkFullToHalfHermitianImageFilterICF2___New_orig__() -> itkFullToHalfHermitianImageFilterICF2_Pointer"""
    return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2___New_orig__()

def itkFullToHalfHermitianImageFilterICF2_cast(obj):
    """itkFullToHalfHermitianImageFilterICF2_cast(itkLightObject obj) -> itkFullToHalfHermitianImageFilterICF2"""
    return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_cast(obj)

class itkFullToHalfHermitianImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    """Proxy of C++ itkFullToHalfHermitianImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkFullToHalfHermitianImageFilterICF3_Pointer"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkFullToHalfHermitianImageFilterICF3 self) -> itkFullToHalfHermitianImageFilterICF3_Pointer"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_Clone(self)


    def GetActualXDimensionIsOddOutput(self):
        """GetActualXDimensionIsOddOutput(itkFullToHalfHermitianImageFilterICF3 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetActualXDimensionIsOddOutput(self)


    def GetActualXDimensionIsOdd(self):
        """GetActualXDimensionIsOdd(itkFullToHalfHermitianImageFilterICF3 self) -> bool const &"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetActualXDimensionIsOdd(self)

    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkFullToHalfHermitianImageFilterICF3"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkFullToHalfHermitianImageFilterICF3 self) -> itkFullToHalfHermitianImageFilterICF3"""
        return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICF3

        Create a new object of the class itkFullToHalfHermitianImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFullToHalfHermitianImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFullToHalfHermitianImageFilterICF3.Clone = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_Clone, None, itkFullToHalfHermitianImageFilterICF3)
itkFullToHalfHermitianImageFilterICF3.GetActualXDimensionIsOddOutput = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetActualXDimensionIsOddOutput, None, itkFullToHalfHermitianImageFilterICF3)
itkFullToHalfHermitianImageFilterICF3.GetActualXDimensionIsOdd = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetActualXDimensionIsOdd, None, itkFullToHalfHermitianImageFilterICF3)
itkFullToHalfHermitianImageFilterICF3.GetPointer = new_instancemethod(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetPointer, None, itkFullToHalfHermitianImageFilterICF3)
itkFullToHalfHermitianImageFilterICF3_swigregister = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_swigregister
itkFullToHalfHermitianImageFilterICF3_swigregister(itkFullToHalfHermitianImageFilterICF3)

def itkFullToHalfHermitianImageFilterICF3___New_orig__():
    """itkFullToHalfHermitianImageFilterICF3___New_orig__() -> itkFullToHalfHermitianImageFilterICF3_Pointer"""
    return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3___New_orig__()

def itkFullToHalfHermitianImageFilterICF3_cast(obj):
    """itkFullToHalfHermitianImageFilterICF3_cast(itkLightObject obj) -> itkFullToHalfHermitianImageFilterICF3"""
    return _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_cast(obj)



