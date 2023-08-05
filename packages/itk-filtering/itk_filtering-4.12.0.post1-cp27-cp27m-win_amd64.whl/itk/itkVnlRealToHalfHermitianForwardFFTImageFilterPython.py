# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVnlRealToHalfHermitianForwardFFTImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVnlRealToHalfHermitianForwardFFTImageFilterPython')
    _itkVnlRealToHalfHermitianForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVnlRealToHalfHermitianForwardFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkVnlRealToHalfHermitianForwardFFTImageFilterPython
            return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython
        try:
            _mod = imp.load_module('_itkVnlRealToHalfHermitianForwardFFTImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVnlRealToHalfHermitianForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVnlRealToHalfHermitianForwardFFTImageFilterPython
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


import itkRealToHalfHermitianForwardFFTImageFilterPython
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
import itkImageToImageFilterBPython
import itkImagePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_New():
  return itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New()


def itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_New():
  return itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New()

class itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2(itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2):
    """Proxy of C++ itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2 self) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Clone(self)

    ImageDimensionsMatchCheck = _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_ImageDimensionsMatchCheck
    __swig_destroy__ = _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.delete_itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2 self) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2.Clone = new_instancemethod(_itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Clone, None, itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2.GetPointer = new_instancemethod(_itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetPointer, None, itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister = _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister
itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister(itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2)

def itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__():
    """itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__() -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_Pointer"""
    return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__()

def itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(obj):
    """itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(itkLightObject obj) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2"""
    return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast(obj)

class itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3(itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3):
    """Proxy of C++ itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3 self) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Clone(self)

    ImageDimensionsMatchCheck = _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_ImageDimensionsMatchCheck
    __swig_destroy__ = _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.delete_itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3 self) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3"""
        return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3.Clone = new_instancemethod(_itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Clone, None, itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3.GetPointer = new_instancemethod(_itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetPointer, None, itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister = _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister
itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister(itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3)

def itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__():
    """itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__() -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_Pointer"""
    return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__()

def itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(obj):
    """itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(itkLightObject obj) -> itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3"""
    return _itkVnlRealToHalfHermitianForwardFFTImageFilterPython.itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast(obj)



