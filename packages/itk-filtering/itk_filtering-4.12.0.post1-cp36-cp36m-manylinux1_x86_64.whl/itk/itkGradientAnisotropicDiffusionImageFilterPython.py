# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGradientAnisotropicDiffusionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGradientAnisotropicDiffusionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGradientAnisotropicDiffusionImageFilterPython')
    _itkGradientAnisotropicDiffusionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGradientAnisotropicDiffusionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkGradientAnisotropicDiffusionImageFilterPython
            return _itkGradientAnisotropicDiffusionImageFilterPython
        try:
            _mod = imp.load_module('_itkGradientAnisotropicDiffusionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGradientAnisotropicDiffusionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGradientAnisotropicDiffusionImageFilterPython
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


import itkAnisotropicDiffusionImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkDenseFiniteDifferenceImageFilterPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkSizePython
import itkRGBPixelPython
import itkOffsetPython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython

def itkGradientAnisotropicDiffusionImageFilterIF3IF3_New():
  return itkGradientAnisotropicDiffusionImageFilterIF3IF3.New()


def itkGradientAnisotropicDiffusionImageFilterIF2IF2_New():
  return itkGradientAnisotropicDiffusionImageFilterIF2IF2.New()

class itkGradientAnisotropicDiffusionImageFilterIF2IF2(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF2IF2):
    """Proxy of C++ itkGradientAnisotropicDiffusionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer":
        """Clone(itkGradientAnisotropicDiffusionImageFilterIF2IF2 self) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_Clone(self)

    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_UpdateBufferHasNumericTraitsCheck
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2 *":
        """GetPointer(itkGradientAnisotropicDiffusionImageFilterIF2IF2 self) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientAnisotropicDiffusionImageFilterIF2IF2.Clone = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_Clone, None, itkGradientAnisotropicDiffusionImageFilterIF2IF2)
itkGradientAnisotropicDiffusionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_GetPointer, None, itkGradientAnisotropicDiffusionImageFilterIF2IF2)
itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister
itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister(itkGradientAnisotropicDiffusionImageFilterIF2IF2)

def itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer":
    """itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__()

def itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2 *":
    """itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(obj)

class itkGradientAnisotropicDiffusionImageFilterIF3IF3(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF3IF3):
    """Proxy of C++ itkGradientAnisotropicDiffusionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer":
        """Clone(itkGradientAnisotropicDiffusionImageFilterIF3IF3 self) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_Clone(self)

    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_UpdateBufferHasNumericTraitsCheck
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3 *":
        """GetPointer(itkGradientAnisotropicDiffusionImageFilterIF3IF3 self) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientAnisotropicDiffusionImageFilterIF3IF3.Clone = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_Clone, None, itkGradientAnisotropicDiffusionImageFilterIF3IF3)
itkGradientAnisotropicDiffusionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_GetPointer, None, itkGradientAnisotropicDiffusionImageFilterIF3IF3)
itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister
itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister(itkGradientAnisotropicDiffusionImageFilterIF3IF3)

def itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer":
    """itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__()

def itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3 *":
    """itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(obj)



