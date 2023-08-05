# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkInverseDeconvolutionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkInverseDeconvolutionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkInverseDeconvolutionImageFilterPython')
    _itkInverseDeconvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkInverseDeconvolutionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkInverseDeconvolutionImageFilterPython
            return _itkInverseDeconvolutionImageFilterPython
        try:
            _mod = imp.load_module('_itkInverseDeconvolutionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkInverseDeconvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkInverseDeconvolutionImageFilterPython
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


import itkFFTConvolutionImageFilterPython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkOffsetPython
import itkSizePython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import ITKCommonBasePython
import itkRGBAPixelPython
import itkConvolutionImageFilterBasePython
import itkImageBoundaryConditionPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkInverseDeconvolutionImageFilterIF3IF3_New():
  return itkInverseDeconvolutionImageFilterIF3IF3.New()


def itkInverseDeconvolutionImageFilterIF2IF2_New():
  return itkInverseDeconvolutionImageFilterIF2IF2.New()


def itkInverseDeconvolutionImageFilterIUC3IUC3_New():
  return itkInverseDeconvolutionImageFilterIUC3IUC3.New()


def itkInverseDeconvolutionImageFilterIUC2IUC2_New():
  return itkInverseDeconvolutionImageFilterIUC2IUC2.New()


def itkInverseDeconvolutionImageFilterISS3ISS3_New():
  return itkInverseDeconvolutionImageFilterISS3ISS3.New()


def itkInverseDeconvolutionImageFilterISS2ISS2_New():
  return itkInverseDeconvolutionImageFilterISS2ISS2.New()

class itkInverseDeconvolutionImageFilterIF2IF2(itkFFTConvolutionImageFilterPython.itkFFTConvolutionImageFilterIF2IF2):
    """Proxy of C++ itkInverseDeconvolutionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseDeconvolutionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkInverseDeconvolutionImageFilterIF2IF2_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInverseDeconvolutionImageFilterIF2IF2_Pointer":
        """Clone(itkInverseDeconvolutionImageFilterIF2IF2 self) -> itkInverseDeconvolutionImageFilterIF2IF2_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_Clone(self)


    def SetKernelZeroMagnitudeThreshold(self, _arg: 'double const') -> "void":
        """SetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIF2IF2 self, double const _arg)"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_SetKernelZeroMagnitudeThreshold(self, _arg)


    def GetKernelZeroMagnitudeThreshold(self) -> "double":
        """GetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIF2IF2 self) -> double"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_GetKernelZeroMagnitudeThreshold(self)

    __swig_destroy__ = _itkInverseDeconvolutionImageFilterPython.delete_itkInverseDeconvolutionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIF2IF2"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkInverseDeconvolutionImageFilterIF2IF2 *":
        """GetPointer(itkInverseDeconvolutionImageFilterIF2IF2 self) -> itkInverseDeconvolutionImageFilterIF2IF2"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseDeconvolutionImageFilterIF2IF2

        Create a new object of the class itkInverseDeconvolutionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseDeconvolutionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseDeconvolutionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseDeconvolutionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseDeconvolutionImageFilterIF2IF2.Clone = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_Clone, None, itkInverseDeconvolutionImageFilterIF2IF2)
itkInverseDeconvolutionImageFilterIF2IF2.SetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_SetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIF2IF2)
itkInverseDeconvolutionImageFilterIF2IF2.GetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_GetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIF2IF2)
itkInverseDeconvolutionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_GetPointer, None, itkInverseDeconvolutionImageFilterIF2IF2)
itkInverseDeconvolutionImageFilterIF2IF2_swigregister = _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_swigregister
itkInverseDeconvolutionImageFilterIF2IF2_swigregister(itkInverseDeconvolutionImageFilterIF2IF2)

def itkInverseDeconvolutionImageFilterIF2IF2___New_orig__() -> "itkInverseDeconvolutionImageFilterIF2IF2_Pointer":
    """itkInverseDeconvolutionImageFilterIF2IF2___New_orig__() -> itkInverseDeconvolutionImageFilterIF2IF2_Pointer"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2___New_orig__()

def itkInverseDeconvolutionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIF2IF2 *":
    """itkInverseDeconvolutionImageFilterIF2IF2_cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIF2IF2"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2_cast(obj)

class itkInverseDeconvolutionImageFilterIF3IF3(itkFFTConvolutionImageFilterPython.itkFFTConvolutionImageFilterIF3IF3):
    """Proxy of C++ itkInverseDeconvolutionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseDeconvolutionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkInverseDeconvolutionImageFilterIF3IF3_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInverseDeconvolutionImageFilterIF3IF3_Pointer":
        """Clone(itkInverseDeconvolutionImageFilterIF3IF3 self) -> itkInverseDeconvolutionImageFilterIF3IF3_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_Clone(self)


    def SetKernelZeroMagnitudeThreshold(self, _arg: 'double const') -> "void":
        """SetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIF3IF3 self, double const _arg)"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_SetKernelZeroMagnitudeThreshold(self, _arg)


    def GetKernelZeroMagnitudeThreshold(self) -> "double":
        """GetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIF3IF3 self) -> double"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_GetKernelZeroMagnitudeThreshold(self)

    __swig_destroy__ = _itkInverseDeconvolutionImageFilterPython.delete_itkInverseDeconvolutionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIF3IF3"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkInverseDeconvolutionImageFilterIF3IF3 *":
        """GetPointer(itkInverseDeconvolutionImageFilterIF3IF3 self) -> itkInverseDeconvolutionImageFilterIF3IF3"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseDeconvolutionImageFilterIF3IF3

        Create a new object of the class itkInverseDeconvolutionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseDeconvolutionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseDeconvolutionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseDeconvolutionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseDeconvolutionImageFilterIF3IF3.Clone = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_Clone, None, itkInverseDeconvolutionImageFilterIF3IF3)
itkInverseDeconvolutionImageFilterIF3IF3.SetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_SetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIF3IF3)
itkInverseDeconvolutionImageFilterIF3IF3.GetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_GetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIF3IF3)
itkInverseDeconvolutionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_GetPointer, None, itkInverseDeconvolutionImageFilterIF3IF3)
itkInverseDeconvolutionImageFilterIF3IF3_swigregister = _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_swigregister
itkInverseDeconvolutionImageFilterIF3IF3_swigregister(itkInverseDeconvolutionImageFilterIF3IF3)

def itkInverseDeconvolutionImageFilterIF3IF3___New_orig__() -> "itkInverseDeconvolutionImageFilterIF3IF3_Pointer":
    """itkInverseDeconvolutionImageFilterIF3IF3___New_orig__() -> itkInverseDeconvolutionImageFilterIF3IF3_Pointer"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3___New_orig__()

def itkInverseDeconvolutionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIF3IF3 *":
    """itkInverseDeconvolutionImageFilterIF3IF3_cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIF3IF3"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3_cast(obj)

class itkInverseDeconvolutionImageFilterISS2ISS2(itkFFTConvolutionImageFilterPython.itkFFTConvolutionImageFilterISS2ISS2):
    """Proxy of C++ itkInverseDeconvolutionImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseDeconvolutionImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkInverseDeconvolutionImageFilterISS2ISS2_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInverseDeconvolutionImageFilterISS2ISS2_Pointer":
        """Clone(itkInverseDeconvolutionImageFilterISS2ISS2 self) -> itkInverseDeconvolutionImageFilterISS2ISS2_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_Clone(self)


    def SetKernelZeroMagnitudeThreshold(self, _arg: 'double const') -> "void":
        """SetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterISS2ISS2 self, double const _arg)"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_SetKernelZeroMagnitudeThreshold(self, _arg)


    def GetKernelZeroMagnitudeThreshold(self) -> "double":
        """GetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterISS2ISS2 self) -> double"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_GetKernelZeroMagnitudeThreshold(self)

    __swig_destroy__ = _itkInverseDeconvolutionImageFilterPython.delete_itkInverseDeconvolutionImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterISS2ISS2"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkInverseDeconvolutionImageFilterISS2ISS2 *":
        """GetPointer(itkInverseDeconvolutionImageFilterISS2ISS2 self) -> itkInverseDeconvolutionImageFilterISS2ISS2"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseDeconvolutionImageFilterISS2ISS2

        Create a new object of the class itkInverseDeconvolutionImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseDeconvolutionImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseDeconvolutionImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseDeconvolutionImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseDeconvolutionImageFilterISS2ISS2.Clone = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_Clone, None, itkInverseDeconvolutionImageFilterISS2ISS2)
itkInverseDeconvolutionImageFilterISS2ISS2.SetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_SetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterISS2ISS2)
itkInverseDeconvolutionImageFilterISS2ISS2.GetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_GetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterISS2ISS2)
itkInverseDeconvolutionImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_GetPointer, None, itkInverseDeconvolutionImageFilterISS2ISS2)
itkInverseDeconvolutionImageFilterISS2ISS2_swigregister = _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_swigregister
itkInverseDeconvolutionImageFilterISS2ISS2_swigregister(itkInverseDeconvolutionImageFilterISS2ISS2)

def itkInverseDeconvolutionImageFilterISS2ISS2___New_orig__() -> "itkInverseDeconvolutionImageFilterISS2ISS2_Pointer":
    """itkInverseDeconvolutionImageFilterISS2ISS2___New_orig__() -> itkInverseDeconvolutionImageFilterISS2ISS2_Pointer"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2___New_orig__()

def itkInverseDeconvolutionImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterISS2ISS2 *":
    """itkInverseDeconvolutionImageFilterISS2ISS2_cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterISS2ISS2"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2_cast(obj)

class itkInverseDeconvolutionImageFilterISS3ISS3(itkFFTConvolutionImageFilterPython.itkFFTConvolutionImageFilterISS3ISS3):
    """Proxy of C++ itkInverseDeconvolutionImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseDeconvolutionImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkInverseDeconvolutionImageFilterISS3ISS3_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInverseDeconvolutionImageFilterISS3ISS3_Pointer":
        """Clone(itkInverseDeconvolutionImageFilterISS3ISS3 self) -> itkInverseDeconvolutionImageFilterISS3ISS3_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_Clone(self)


    def SetKernelZeroMagnitudeThreshold(self, _arg: 'double const') -> "void":
        """SetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterISS3ISS3 self, double const _arg)"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_SetKernelZeroMagnitudeThreshold(self, _arg)


    def GetKernelZeroMagnitudeThreshold(self) -> "double":
        """GetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterISS3ISS3 self) -> double"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_GetKernelZeroMagnitudeThreshold(self)

    __swig_destroy__ = _itkInverseDeconvolutionImageFilterPython.delete_itkInverseDeconvolutionImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterISS3ISS3"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkInverseDeconvolutionImageFilterISS3ISS3 *":
        """GetPointer(itkInverseDeconvolutionImageFilterISS3ISS3 self) -> itkInverseDeconvolutionImageFilterISS3ISS3"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseDeconvolutionImageFilterISS3ISS3

        Create a new object of the class itkInverseDeconvolutionImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseDeconvolutionImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseDeconvolutionImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseDeconvolutionImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseDeconvolutionImageFilterISS3ISS3.Clone = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_Clone, None, itkInverseDeconvolutionImageFilterISS3ISS3)
itkInverseDeconvolutionImageFilterISS3ISS3.SetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_SetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterISS3ISS3)
itkInverseDeconvolutionImageFilterISS3ISS3.GetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_GetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterISS3ISS3)
itkInverseDeconvolutionImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_GetPointer, None, itkInverseDeconvolutionImageFilterISS3ISS3)
itkInverseDeconvolutionImageFilterISS3ISS3_swigregister = _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_swigregister
itkInverseDeconvolutionImageFilterISS3ISS3_swigregister(itkInverseDeconvolutionImageFilterISS3ISS3)

def itkInverseDeconvolutionImageFilterISS3ISS3___New_orig__() -> "itkInverseDeconvolutionImageFilterISS3ISS3_Pointer":
    """itkInverseDeconvolutionImageFilterISS3ISS3___New_orig__() -> itkInverseDeconvolutionImageFilterISS3ISS3_Pointer"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3___New_orig__()

def itkInverseDeconvolutionImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterISS3ISS3 *":
    """itkInverseDeconvolutionImageFilterISS3ISS3_cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterISS3ISS3"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3_cast(obj)

class itkInverseDeconvolutionImageFilterIUC2IUC2(itkFFTConvolutionImageFilterPython.itkFFTConvolutionImageFilterIUC2IUC2):
    """Proxy of C++ itkInverseDeconvolutionImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseDeconvolutionImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkInverseDeconvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInverseDeconvolutionImageFilterIUC2IUC2_Pointer":
        """Clone(itkInverseDeconvolutionImageFilterIUC2IUC2 self) -> itkInverseDeconvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_Clone(self)


    def SetKernelZeroMagnitudeThreshold(self, _arg: 'double const') -> "void":
        """SetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_SetKernelZeroMagnitudeThreshold(self, _arg)


    def GetKernelZeroMagnitudeThreshold(self) -> "double":
        """GetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIUC2IUC2 self) -> double"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_GetKernelZeroMagnitudeThreshold(self)

    __swig_destroy__ = _itkInverseDeconvolutionImageFilterPython.delete_itkInverseDeconvolutionImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIUC2IUC2"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkInverseDeconvolutionImageFilterIUC2IUC2 *":
        """GetPointer(itkInverseDeconvolutionImageFilterIUC2IUC2 self) -> itkInverseDeconvolutionImageFilterIUC2IUC2"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseDeconvolutionImageFilterIUC2IUC2

        Create a new object of the class itkInverseDeconvolutionImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseDeconvolutionImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseDeconvolutionImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseDeconvolutionImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseDeconvolutionImageFilterIUC2IUC2.Clone = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_Clone, None, itkInverseDeconvolutionImageFilterIUC2IUC2)
itkInverseDeconvolutionImageFilterIUC2IUC2.SetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_SetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIUC2IUC2)
itkInverseDeconvolutionImageFilterIUC2IUC2.GetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_GetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIUC2IUC2)
itkInverseDeconvolutionImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_GetPointer, None, itkInverseDeconvolutionImageFilterIUC2IUC2)
itkInverseDeconvolutionImageFilterIUC2IUC2_swigregister = _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_swigregister
itkInverseDeconvolutionImageFilterIUC2IUC2_swigregister(itkInverseDeconvolutionImageFilterIUC2IUC2)

def itkInverseDeconvolutionImageFilterIUC2IUC2___New_orig__() -> "itkInverseDeconvolutionImageFilterIUC2IUC2_Pointer":
    """itkInverseDeconvolutionImageFilterIUC2IUC2___New_orig__() -> itkInverseDeconvolutionImageFilterIUC2IUC2_Pointer"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2___New_orig__()

def itkInverseDeconvolutionImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIUC2IUC2 *":
    """itkInverseDeconvolutionImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIUC2IUC2"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2_cast(obj)

class itkInverseDeconvolutionImageFilterIUC3IUC3(itkFFTConvolutionImageFilterPython.itkFFTConvolutionImageFilterIUC3IUC3):
    """Proxy of C++ itkInverseDeconvolutionImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseDeconvolutionImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkInverseDeconvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInverseDeconvolutionImageFilterIUC3IUC3_Pointer":
        """Clone(itkInverseDeconvolutionImageFilterIUC3IUC3 self) -> itkInverseDeconvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_Clone(self)


    def SetKernelZeroMagnitudeThreshold(self, _arg: 'double const') -> "void":
        """SetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_SetKernelZeroMagnitudeThreshold(self, _arg)


    def GetKernelZeroMagnitudeThreshold(self) -> "double":
        """GetKernelZeroMagnitudeThreshold(itkInverseDeconvolutionImageFilterIUC3IUC3 self) -> double"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_GetKernelZeroMagnitudeThreshold(self)

    __swig_destroy__ = _itkInverseDeconvolutionImageFilterPython.delete_itkInverseDeconvolutionImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIUC3IUC3"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkInverseDeconvolutionImageFilterIUC3IUC3 *":
        """GetPointer(itkInverseDeconvolutionImageFilterIUC3IUC3 self) -> itkInverseDeconvolutionImageFilterIUC3IUC3"""
        return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkInverseDeconvolutionImageFilterIUC3IUC3

        Create a new object of the class itkInverseDeconvolutionImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseDeconvolutionImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseDeconvolutionImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseDeconvolutionImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseDeconvolutionImageFilterIUC3IUC3.Clone = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_Clone, None, itkInverseDeconvolutionImageFilterIUC3IUC3)
itkInverseDeconvolutionImageFilterIUC3IUC3.SetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_SetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIUC3IUC3)
itkInverseDeconvolutionImageFilterIUC3IUC3.GetKernelZeroMagnitudeThreshold = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_GetKernelZeroMagnitudeThreshold, None, itkInverseDeconvolutionImageFilterIUC3IUC3)
itkInverseDeconvolutionImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_GetPointer, None, itkInverseDeconvolutionImageFilterIUC3IUC3)
itkInverseDeconvolutionImageFilterIUC3IUC3_swigregister = _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_swigregister
itkInverseDeconvolutionImageFilterIUC3IUC3_swigregister(itkInverseDeconvolutionImageFilterIUC3IUC3)

def itkInverseDeconvolutionImageFilterIUC3IUC3___New_orig__() -> "itkInverseDeconvolutionImageFilterIUC3IUC3_Pointer":
    """itkInverseDeconvolutionImageFilterIUC3IUC3___New_orig__() -> itkInverseDeconvolutionImageFilterIUC3IUC3_Pointer"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3___New_orig__()

def itkInverseDeconvolutionImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkInverseDeconvolutionImageFilterIUC3IUC3 *":
    """itkInverseDeconvolutionImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkInverseDeconvolutionImageFilterIUC3IUC3"""
    return _itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3_cast(obj)



