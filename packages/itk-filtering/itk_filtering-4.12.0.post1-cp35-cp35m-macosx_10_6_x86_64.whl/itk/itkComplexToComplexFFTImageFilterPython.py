# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkComplexToComplexFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkComplexToComplexFFTImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkComplexToComplexFFTImageFilterPython')
    _itkComplexToComplexFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkComplexToComplexFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkComplexToComplexFFTImageFilterPython
            return _itkComplexToComplexFFTImageFilterPython
        try:
            _mod = imp.load_module('_itkComplexToComplexFFTImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkComplexToComplexFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkComplexToComplexFFTImageFilterPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import ITKCommonBasePython
import pyBasePython
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

def itkComplexToComplexFFTImageFilterICF3_New():
  return itkComplexToComplexFFTImageFilterICF3.New()


def itkComplexToComplexFFTImageFilterICF2_New():
  return itkComplexToComplexFFTImageFilterICF2.New()

class itkComplexToComplexFFTImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    """Proxy of C++ itkComplexToComplexFFTImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToComplexFFTImageFilterICF2_Pointer":
        """__New_orig__() -> itkComplexToComplexFFTImageFilterICF2_Pointer"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)
    FORWARD = _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_FORWARD
    INVERSE = _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_INVERSE

    def SetTransformDirection(self, _arg: 'itkComplexToComplexFFTImageFilterICF2::TransformDirectionType const') -> "void":
        """SetTransformDirection(itkComplexToComplexFFTImageFilterICF2 self, itkComplexToComplexFFTImageFilterICF2::TransformDirectionType const _arg)"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_SetTransformDirection(self, _arg)


    def GetTransformDirection(self) -> "itkComplexToComplexFFTImageFilterICF2::TransformDirectionType":
        """GetTransformDirection(itkComplexToComplexFFTImageFilterICF2 self) -> itkComplexToComplexFFTImageFilterICF2::TransformDirectionType"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_GetTransformDirection(self)

    __swig_destroy__ = _itkComplexToComplexFFTImageFilterPython.delete_itkComplexToComplexFFTImageFilterICF2

    def cast(obj: 'itkLightObject') -> "itkComplexToComplexFFTImageFilterICF2 *":
        """cast(itkLightObject obj) -> itkComplexToComplexFFTImageFilterICF2"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToComplexFFTImageFilterICF2 *":
        """GetPointer(itkComplexToComplexFFTImageFilterICF2 self) -> itkComplexToComplexFFTImageFilterICF2"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToComplexFFTImageFilterICF2

        Create a new object of the class itkComplexToComplexFFTImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToComplexFFTImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToComplexFFTImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToComplexFFTImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToComplexFFTImageFilterICF2.SetTransformDirection = new_instancemethod(_itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_SetTransformDirection, None, itkComplexToComplexFFTImageFilterICF2)
itkComplexToComplexFFTImageFilterICF2.GetTransformDirection = new_instancemethod(_itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_GetTransformDirection, None, itkComplexToComplexFFTImageFilterICF2)
itkComplexToComplexFFTImageFilterICF2.GetPointer = new_instancemethod(_itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_GetPointer, None, itkComplexToComplexFFTImageFilterICF2)
itkComplexToComplexFFTImageFilterICF2_swigregister = _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_swigregister
itkComplexToComplexFFTImageFilterICF2_swigregister(itkComplexToComplexFFTImageFilterICF2)

def itkComplexToComplexFFTImageFilterICF2___New_orig__() -> "itkComplexToComplexFFTImageFilterICF2_Pointer":
    """itkComplexToComplexFFTImageFilterICF2___New_orig__() -> itkComplexToComplexFFTImageFilterICF2_Pointer"""
    return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2___New_orig__()

def itkComplexToComplexFFTImageFilterICF2_cast(obj: 'itkLightObject') -> "itkComplexToComplexFFTImageFilterICF2 *":
    """itkComplexToComplexFFTImageFilterICF2_cast(itkLightObject obj) -> itkComplexToComplexFFTImageFilterICF2"""
    return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2_cast(obj)

class itkComplexToComplexFFTImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    """Proxy of C++ itkComplexToComplexFFTImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToComplexFFTImageFilterICF3_Pointer":
        """__New_orig__() -> itkComplexToComplexFFTImageFilterICF3_Pointer"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)
    FORWARD = _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_FORWARD
    INVERSE = _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_INVERSE

    def SetTransformDirection(self, _arg: 'itkComplexToComplexFFTImageFilterICF3::TransformDirectionType const') -> "void":
        """SetTransformDirection(itkComplexToComplexFFTImageFilterICF3 self, itkComplexToComplexFFTImageFilterICF3::TransformDirectionType const _arg)"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_SetTransformDirection(self, _arg)


    def GetTransformDirection(self) -> "itkComplexToComplexFFTImageFilterICF3::TransformDirectionType":
        """GetTransformDirection(itkComplexToComplexFFTImageFilterICF3 self) -> itkComplexToComplexFFTImageFilterICF3::TransformDirectionType"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_GetTransformDirection(self)

    __swig_destroy__ = _itkComplexToComplexFFTImageFilterPython.delete_itkComplexToComplexFFTImageFilterICF3

    def cast(obj: 'itkLightObject') -> "itkComplexToComplexFFTImageFilterICF3 *":
        """cast(itkLightObject obj) -> itkComplexToComplexFFTImageFilterICF3"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToComplexFFTImageFilterICF3 *":
        """GetPointer(itkComplexToComplexFFTImageFilterICF3 self) -> itkComplexToComplexFFTImageFilterICF3"""
        return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToComplexFFTImageFilterICF3

        Create a new object of the class itkComplexToComplexFFTImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToComplexFFTImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToComplexFFTImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToComplexFFTImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToComplexFFTImageFilterICF3.SetTransformDirection = new_instancemethod(_itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_SetTransformDirection, None, itkComplexToComplexFFTImageFilterICF3)
itkComplexToComplexFFTImageFilterICF3.GetTransformDirection = new_instancemethod(_itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_GetTransformDirection, None, itkComplexToComplexFFTImageFilterICF3)
itkComplexToComplexFFTImageFilterICF3.GetPointer = new_instancemethod(_itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_GetPointer, None, itkComplexToComplexFFTImageFilterICF3)
itkComplexToComplexFFTImageFilterICF3_swigregister = _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_swigregister
itkComplexToComplexFFTImageFilterICF3_swigregister(itkComplexToComplexFFTImageFilterICF3)

def itkComplexToComplexFFTImageFilterICF3___New_orig__() -> "itkComplexToComplexFFTImageFilterICF3_Pointer":
    """itkComplexToComplexFFTImageFilterICF3___New_orig__() -> itkComplexToComplexFFTImageFilterICF3_Pointer"""
    return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3___New_orig__()

def itkComplexToComplexFFTImageFilterICF3_cast(obj: 'itkLightObject') -> "itkComplexToComplexFFTImageFilterICF3 *":
    """itkComplexToComplexFFTImageFilterICF3_cast(itkLightObject obj) -> itkComplexToComplexFFTImageFilterICF3"""
    return _itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3_cast(obj)



