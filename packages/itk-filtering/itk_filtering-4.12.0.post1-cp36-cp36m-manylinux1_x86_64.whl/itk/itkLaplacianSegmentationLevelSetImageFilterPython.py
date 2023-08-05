# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLaplacianSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLaplacianSegmentationLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLaplacianSegmentationLevelSetImageFilterPython')
    _itkLaplacianSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLaplacianSegmentationLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLaplacianSegmentationLevelSetImageFilterPython
            return _itkLaplacianSegmentationLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkLaplacianSegmentationLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLaplacianSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLaplacianSegmentationLevelSetImageFilterPython
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


import itkSegmentationLevelSetImageFilterPython
import ITKCommonBasePython
import pyBasePython
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
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython

def itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_New():
  return itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.New()


def itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_New():
  return itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.New()

class itkLaplacianSegmentationLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    """Proxy of C++ itkLaplacianSegmentationLevelSetImageFilterIF2IF2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """__New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """Clone(itkLaplacianSegmentationLevelSetImageFilterIF2IF2F self) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Clone(self)

    __swig_destroy__ = _itkLaplacianSegmentationLevelSetImageFilterPython.delete_itkLaplacianSegmentationLevelSetImageFilterIF2IF2F

    def cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F *":
        """cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F *":
        """GetPointer(itkLaplacianSegmentationLevelSetImageFilterIF2IF2F self) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F

        Create a new object of the class itkLaplacianSegmentationLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Clone, None, itkLaplacianSegmentationLevelSetImageFilterIF2IF2F)
itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.GetPointer = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_GetPointer, None, itkLaplacianSegmentationLevelSetImageFilterIF2IF2F)
itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_swigregister = _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_swigregister
itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_swigregister(itkLaplacianSegmentationLevelSetImageFilterIF2IF2F)

def itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer":
    """itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

def itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F *":
    """itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

class itkLaplacianSegmentationLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    """Proxy of C++ itkLaplacianSegmentationLevelSetImageFilterIF3IF3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """__New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """Clone(itkLaplacianSegmentationLevelSetImageFilterIF3IF3F self) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Clone(self)

    __swig_destroy__ = _itkLaplacianSegmentationLevelSetImageFilterPython.delete_itkLaplacianSegmentationLevelSetImageFilterIF3IF3F

    def cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F *":
        """cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F *":
        """GetPointer(itkLaplacianSegmentationLevelSetImageFilterIF3IF3F self) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F

        Create a new object of the class itkLaplacianSegmentationLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Clone, None, itkLaplacianSegmentationLevelSetImageFilterIF3IF3F)
itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.GetPointer = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_GetPointer, None, itkLaplacianSegmentationLevelSetImageFilterIF3IF3F)
itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_swigregister = _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_swigregister
itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_swigregister(itkLaplacianSegmentationLevelSetImageFilterIF3IF3F)

def itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer":
    """itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

def itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F *":
    """itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(obj)



