# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkInverseFFTImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkInverseFFTImageFilterPython')
    _itkInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkInverseFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkInverseFFTImageFilterPython
            return _itkInverseFFTImageFilterPython
        try:
            _mod = imp.load_module('_itkInverseFFTImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkInverseFFTImageFilterPython
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
import itkImageToImageFilterBPython
import itkImagePython
import stdcomplexPython
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
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkInverseFFTImageFilterICF3IF3_New():
  return itkInverseFFTImageFilterICF3IF3.New()


def itkInverseFFTImageFilterICF2IF2_New():
  return itkInverseFFTImageFilterICF2IF2.New()

class itkInverseFFTImageFilterICF2IF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2IF2):
    """Proxy of C++ itkInverseFFTImageFilterICF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkInverseFFTImageFilterICF2IF2_Pointer"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self):
        """GetSizeGreatestPrimeFactor(itkInverseFFTImageFilterICF2IF2 self) -> unsigned long long"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkInverseFFTImageFilterICF2IF2"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkInverseFFTImageFilterICF2IF2 self) -> itkInverseFFTImageFilterICF2IF2"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF2IF2

        Create a new object of the class itkInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseFFTImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseFFTImageFilterICF2IF2.GetSizeGreatestPrimeFactor = new_instancemethod(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor, None, itkInverseFFTImageFilterICF2IF2)
itkInverseFFTImageFilterICF2IF2.GetPointer = new_instancemethod(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetPointer, None, itkInverseFFTImageFilterICF2IF2)
itkInverseFFTImageFilterICF2IF2_swigregister = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_swigregister
itkInverseFFTImageFilterICF2IF2_swigregister(itkInverseFFTImageFilterICF2IF2)

def itkInverseFFTImageFilterICF2IF2___New_orig__():
    """itkInverseFFTImageFilterICF2IF2___New_orig__() -> itkInverseFFTImageFilterICF2IF2_Pointer"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__()

def itkInverseFFTImageFilterICF2IF2_cast(obj):
    """itkInverseFFTImageFilterICF2IF2_cast(itkLightObject obj) -> itkInverseFFTImageFilterICF2IF2"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast(obj)

class itkInverseFFTImageFilterICF3IF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3IF3):
    """Proxy of C++ itkInverseFFTImageFilterICF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkInverseFFTImageFilterICF3IF3_Pointer"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self):
        """GetSizeGreatestPrimeFactor(itkInverseFFTImageFilterICF3IF3 self) -> unsigned long long"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkInverseFFTImageFilterICF3IF3"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkInverseFFTImageFilterICF3IF3 self) -> itkInverseFFTImageFilterICF3IF3"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF3IF3

        Create a new object of the class itkInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseFFTImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseFFTImageFilterICF3IF3.GetSizeGreatestPrimeFactor = new_instancemethod(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor, None, itkInverseFFTImageFilterICF3IF3)
itkInverseFFTImageFilterICF3IF3.GetPointer = new_instancemethod(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetPointer, None, itkInverseFFTImageFilterICF3IF3)
itkInverseFFTImageFilterICF3IF3_swigregister = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_swigregister
itkInverseFFTImageFilterICF3IF3_swigregister(itkInverseFFTImageFilterICF3IF3)

def itkInverseFFTImageFilterICF3IF3___New_orig__():
    """itkInverseFFTImageFilterICF3IF3___New_orig__() -> itkInverseFFTImageFilterICF3IF3_Pointer"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__()

def itkInverseFFTImageFilterICF3IF3_cast(obj):
    """itkInverseFFTImageFilterICF3IF3_cast(itkLightObject obj) -> itkInverseFFTImageFilterICF3IF3"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast(obj)



