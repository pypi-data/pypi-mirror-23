# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkForwardFFTImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkForwardFFTImageFilterPython')
    _itkForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkForwardFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkForwardFFTImageFilterPython
            return _itkForwardFFTImageFilterPython
        try:
            _mod = imp.load_module('_itkForwardFFTImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkForwardFFTImageFilterPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkForwardFFTImageFilterIF3ICF3_New():
  return itkForwardFFTImageFilterIF3ICF3.New()


def itkForwardFFTImageFilterIF2ICF2_New():
  return itkForwardFFTImageFilterIF2ICF2.New()

class itkForwardFFTImageFilterIF2ICF2(itkImageToImageFilterBPython.itkImageToImageFilterIF2ICF2):
    """Proxy of C++ itkForwardFFTImageFilterIF2ICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self):
        """GetSizeGreatestPrimeFactor(itkForwardFFTImageFilterIF2ICF2 self) -> unsigned long"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkForwardFFTImageFilterPython.delete_itkForwardFFTImageFilterIF2ICF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkForwardFFTImageFilterIF2ICF2"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkForwardFFTImageFilterIF2ICF2 self) -> itkForwardFFTImageFilterIF2ICF2"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkForwardFFTImageFilterIF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkForwardFFTImageFilterIF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkForwardFFTImageFilterIF2ICF2.GetSizeGreatestPrimeFactor = new_instancemethod(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor, None, itkForwardFFTImageFilterIF2ICF2)
itkForwardFFTImageFilterIF2ICF2.GetPointer = new_instancemethod(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetPointer, None, itkForwardFFTImageFilterIF2ICF2)
itkForwardFFTImageFilterIF2ICF2_swigregister = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_swigregister
itkForwardFFTImageFilterIF2ICF2_swigregister(itkForwardFFTImageFilterIF2ICF2)

def itkForwardFFTImageFilterIF2ICF2___New_orig__():
    """itkForwardFFTImageFilterIF2ICF2___New_orig__() -> itkForwardFFTImageFilterIF2ICF2_Pointer"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2___New_orig__()

def itkForwardFFTImageFilterIF2ICF2_cast(obj):
    """itkForwardFFTImageFilterIF2ICF2_cast(itkLightObject obj) -> itkForwardFFTImageFilterIF2ICF2"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_cast(obj)

class itkForwardFFTImageFilterIF3ICF3(itkImageToImageFilterBPython.itkImageToImageFilterIF3ICF3):
    """Proxy of C++ itkForwardFFTImageFilterIF3ICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self):
        """GetSizeGreatestPrimeFactor(itkForwardFFTImageFilterIF3ICF3 self) -> unsigned long"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkForwardFFTImageFilterPython.delete_itkForwardFFTImageFilterIF3ICF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkForwardFFTImageFilterIF3ICF3"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkForwardFFTImageFilterIF3ICF3 self) -> itkForwardFFTImageFilterIF3ICF3"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkForwardFFTImageFilterIF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkForwardFFTImageFilterIF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkForwardFFTImageFilterIF3ICF3.GetSizeGreatestPrimeFactor = new_instancemethod(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor, None, itkForwardFFTImageFilterIF3ICF3)
itkForwardFFTImageFilterIF3ICF3.GetPointer = new_instancemethod(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetPointer, None, itkForwardFFTImageFilterIF3ICF3)
itkForwardFFTImageFilterIF3ICF3_swigregister = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_swigregister
itkForwardFFTImageFilterIF3ICF3_swigregister(itkForwardFFTImageFilterIF3ICF3)

def itkForwardFFTImageFilterIF3ICF3___New_orig__():
    """itkForwardFFTImageFilterIF3ICF3___New_orig__() -> itkForwardFFTImageFilterIF3ICF3_Pointer"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3___New_orig__()

def itkForwardFFTImageFilterIF3ICF3_cast(obj):
    """itkForwardFFTImageFilterIF3ICF3_cast(itkLightObject obj) -> itkForwardFFTImageFilterIF3ICF3"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_cast(obj)



