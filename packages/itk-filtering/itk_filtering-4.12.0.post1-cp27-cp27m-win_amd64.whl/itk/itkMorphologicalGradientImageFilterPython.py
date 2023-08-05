# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMorphologicalGradientImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMorphologicalGradientImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMorphologicalGradientImageFilterPython')
    _itkMorphologicalGradientImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMorphologicalGradientImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMorphologicalGradientImageFilterPython
            return _itkMorphologicalGradientImageFilterPython
        try:
            _mod = imp.load_module('_itkMorphologicalGradientImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMorphologicalGradientImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMorphologicalGradientImageFilterPython
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


import itkFlatStructuringElementPython
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
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkNeighborhoodPython

def itkMorphologicalGradientImageFilterIF3IF3SE3_New():
  return itkMorphologicalGradientImageFilterIF3IF3SE3.New()


def itkMorphologicalGradientImageFilterIUC3IUC3SE3_New():
  return itkMorphologicalGradientImageFilterIUC3IUC3SE3.New()


def itkMorphologicalGradientImageFilterISS3ISS3SE3_New():
  return itkMorphologicalGradientImageFilterISS3ISS3SE3.New()


def itkMorphologicalGradientImageFilterIF2IF2SE2_New():
  return itkMorphologicalGradientImageFilterIF2IF2SE2.New()


def itkMorphologicalGradientImageFilterIUC2IUC2SE2_New():
  return itkMorphologicalGradientImageFilterIUC2IUC2SE2.New()


def itkMorphologicalGradientImageFilterISS2ISS2SE2_New():
  return itkMorphologicalGradientImageFilterISS2ISS2SE2.New()

class itkMorphologicalGradientImageFilterIF2IF2SE2(itkFlatStructuringElementPython.itkKernelImageFilterIF2IF2SE2):
    """Proxy of C++ itkMorphologicalGradientImageFilterIF2IF2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMorphologicalGradientImageFilterIF2IF2SE2_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMorphologicalGradientImageFilterIF2IF2SE2 self) -> itkMorphologicalGradientImageFilterIF2IF2SE2_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_Clone(self)


    def SetAlgorithm(self, algo):
        """SetAlgorithm(itkMorphologicalGradientImageFilterIF2IF2SE2 self, int algo)"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_SetAlgorithm(self, algo)


    def GetAlgorithm(self):
        """GetAlgorithm(itkMorphologicalGradientImageFilterIF2IF2SE2 self) -> int"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_GetAlgorithm(self)

    BASIC = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_BASIC
    HISTO = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_HISTO
    ANCHOR = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_ANCHOR
    VHGW = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_VHGW
    __swig_destroy__ = _itkMorphologicalGradientImageFilterPython.delete_itkMorphologicalGradientImageFilterIF2IF2SE2

    def cast(obj):
        """cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIF2IF2SE2"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMorphologicalGradientImageFilterIF2IF2SE2 self) -> itkMorphologicalGradientImageFilterIF2IF2SE2"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMorphologicalGradientImageFilterIF2IF2SE2

        Create a new object of the class itkMorphologicalGradientImageFilterIF2IF2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMorphologicalGradientImageFilterIF2IF2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMorphologicalGradientImageFilterIF2IF2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMorphologicalGradientImageFilterIF2IF2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMorphologicalGradientImageFilterIF2IF2SE2.Clone = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_Clone, None, itkMorphologicalGradientImageFilterIF2IF2SE2)
itkMorphologicalGradientImageFilterIF2IF2SE2.SetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_SetAlgorithm, None, itkMorphologicalGradientImageFilterIF2IF2SE2)
itkMorphologicalGradientImageFilterIF2IF2SE2.GetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_GetAlgorithm, None, itkMorphologicalGradientImageFilterIF2IF2SE2)
itkMorphologicalGradientImageFilterIF2IF2SE2.GetPointer = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_GetPointer, None, itkMorphologicalGradientImageFilterIF2IF2SE2)
itkMorphologicalGradientImageFilterIF2IF2SE2_swigregister = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_swigregister
itkMorphologicalGradientImageFilterIF2IF2SE2_swigregister(itkMorphologicalGradientImageFilterIF2IF2SE2)

def itkMorphologicalGradientImageFilterIF2IF2SE2___New_orig__():
    """itkMorphologicalGradientImageFilterIF2IF2SE2___New_orig__() -> itkMorphologicalGradientImageFilterIF2IF2SE2_Pointer"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2___New_orig__()

def itkMorphologicalGradientImageFilterIF2IF2SE2_cast(obj):
    """itkMorphologicalGradientImageFilterIF2IF2SE2_cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIF2IF2SE2"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF2IF2SE2_cast(obj)

class itkMorphologicalGradientImageFilterIF3IF3SE3(itkFlatStructuringElementPython.itkKernelImageFilterIF3IF3SE3):
    """Proxy of C++ itkMorphologicalGradientImageFilterIF3IF3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMorphologicalGradientImageFilterIF3IF3SE3_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMorphologicalGradientImageFilterIF3IF3SE3 self) -> itkMorphologicalGradientImageFilterIF3IF3SE3_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_Clone(self)


    def SetAlgorithm(self, algo):
        """SetAlgorithm(itkMorphologicalGradientImageFilterIF3IF3SE3 self, int algo)"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_SetAlgorithm(self, algo)


    def GetAlgorithm(self):
        """GetAlgorithm(itkMorphologicalGradientImageFilterIF3IF3SE3 self) -> int"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_GetAlgorithm(self)

    BASIC = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_BASIC
    HISTO = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_HISTO
    ANCHOR = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_ANCHOR
    VHGW = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_VHGW
    __swig_destroy__ = _itkMorphologicalGradientImageFilterPython.delete_itkMorphologicalGradientImageFilterIF3IF3SE3

    def cast(obj):
        """cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIF3IF3SE3"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMorphologicalGradientImageFilterIF3IF3SE3 self) -> itkMorphologicalGradientImageFilterIF3IF3SE3"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMorphologicalGradientImageFilterIF3IF3SE3

        Create a new object of the class itkMorphologicalGradientImageFilterIF3IF3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMorphologicalGradientImageFilterIF3IF3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMorphologicalGradientImageFilterIF3IF3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMorphologicalGradientImageFilterIF3IF3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMorphologicalGradientImageFilterIF3IF3SE3.Clone = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_Clone, None, itkMorphologicalGradientImageFilterIF3IF3SE3)
itkMorphologicalGradientImageFilterIF3IF3SE3.SetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_SetAlgorithm, None, itkMorphologicalGradientImageFilterIF3IF3SE3)
itkMorphologicalGradientImageFilterIF3IF3SE3.GetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_GetAlgorithm, None, itkMorphologicalGradientImageFilterIF3IF3SE3)
itkMorphologicalGradientImageFilterIF3IF3SE3.GetPointer = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_GetPointer, None, itkMorphologicalGradientImageFilterIF3IF3SE3)
itkMorphologicalGradientImageFilterIF3IF3SE3_swigregister = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_swigregister
itkMorphologicalGradientImageFilterIF3IF3SE3_swigregister(itkMorphologicalGradientImageFilterIF3IF3SE3)

def itkMorphologicalGradientImageFilterIF3IF3SE3___New_orig__():
    """itkMorphologicalGradientImageFilterIF3IF3SE3___New_orig__() -> itkMorphologicalGradientImageFilterIF3IF3SE3_Pointer"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3___New_orig__()

def itkMorphologicalGradientImageFilterIF3IF3SE3_cast(obj):
    """itkMorphologicalGradientImageFilterIF3IF3SE3_cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIF3IF3SE3"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIF3IF3SE3_cast(obj)

class itkMorphologicalGradientImageFilterISS2ISS2SE2(itkFlatStructuringElementPython.itkKernelImageFilterISS2ISS2SE2):
    """Proxy of C++ itkMorphologicalGradientImageFilterISS2ISS2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMorphologicalGradientImageFilterISS2ISS2SE2_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMorphologicalGradientImageFilterISS2ISS2SE2 self) -> itkMorphologicalGradientImageFilterISS2ISS2SE2_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_Clone(self)


    def SetAlgorithm(self, algo):
        """SetAlgorithm(itkMorphologicalGradientImageFilterISS2ISS2SE2 self, int algo)"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_SetAlgorithm(self, algo)


    def GetAlgorithm(self):
        """GetAlgorithm(itkMorphologicalGradientImageFilterISS2ISS2SE2 self) -> int"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_GetAlgorithm(self)

    BASIC = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_BASIC
    HISTO = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_HISTO
    ANCHOR = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_ANCHOR
    VHGW = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_VHGW
    __swig_destroy__ = _itkMorphologicalGradientImageFilterPython.delete_itkMorphologicalGradientImageFilterISS2ISS2SE2

    def cast(obj):
        """cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterISS2ISS2SE2"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMorphologicalGradientImageFilterISS2ISS2SE2 self) -> itkMorphologicalGradientImageFilterISS2ISS2SE2"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMorphologicalGradientImageFilterISS2ISS2SE2

        Create a new object of the class itkMorphologicalGradientImageFilterISS2ISS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMorphologicalGradientImageFilterISS2ISS2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMorphologicalGradientImageFilterISS2ISS2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMorphologicalGradientImageFilterISS2ISS2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMorphologicalGradientImageFilterISS2ISS2SE2.Clone = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_Clone, None, itkMorphologicalGradientImageFilterISS2ISS2SE2)
itkMorphologicalGradientImageFilterISS2ISS2SE2.SetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_SetAlgorithm, None, itkMorphologicalGradientImageFilterISS2ISS2SE2)
itkMorphologicalGradientImageFilterISS2ISS2SE2.GetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_GetAlgorithm, None, itkMorphologicalGradientImageFilterISS2ISS2SE2)
itkMorphologicalGradientImageFilterISS2ISS2SE2.GetPointer = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_GetPointer, None, itkMorphologicalGradientImageFilterISS2ISS2SE2)
itkMorphologicalGradientImageFilterISS2ISS2SE2_swigregister = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_swigregister
itkMorphologicalGradientImageFilterISS2ISS2SE2_swigregister(itkMorphologicalGradientImageFilterISS2ISS2SE2)

def itkMorphologicalGradientImageFilterISS2ISS2SE2___New_orig__():
    """itkMorphologicalGradientImageFilterISS2ISS2SE2___New_orig__() -> itkMorphologicalGradientImageFilterISS2ISS2SE2_Pointer"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2___New_orig__()

def itkMorphologicalGradientImageFilterISS2ISS2SE2_cast(obj):
    """itkMorphologicalGradientImageFilterISS2ISS2SE2_cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterISS2ISS2SE2"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS2ISS2SE2_cast(obj)

class itkMorphologicalGradientImageFilterISS3ISS3SE3(itkFlatStructuringElementPython.itkKernelImageFilterISS3ISS3SE3):
    """Proxy of C++ itkMorphologicalGradientImageFilterISS3ISS3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMorphologicalGradientImageFilterISS3ISS3SE3_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMorphologicalGradientImageFilterISS3ISS3SE3 self) -> itkMorphologicalGradientImageFilterISS3ISS3SE3_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_Clone(self)


    def SetAlgorithm(self, algo):
        """SetAlgorithm(itkMorphologicalGradientImageFilterISS3ISS3SE3 self, int algo)"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_SetAlgorithm(self, algo)


    def GetAlgorithm(self):
        """GetAlgorithm(itkMorphologicalGradientImageFilterISS3ISS3SE3 self) -> int"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_GetAlgorithm(self)

    BASIC = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_BASIC
    HISTO = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_HISTO
    ANCHOR = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_ANCHOR
    VHGW = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_VHGW
    __swig_destroy__ = _itkMorphologicalGradientImageFilterPython.delete_itkMorphologicalGradientImageFilterISS3ISS3SE3

    def cast(obj):
        """cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterISS3ISS3SE3"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMorphologicalGradientImageFilterISS3ISS3SE3 self) -> itkMorphologicalGradientImageFilterISS3ISS3SE3"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMorphologicalGradientImageFilterISS3ISS3SE3

        Create a new object of the class itkMorphologicalGradientImageFilterISS3ISS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMorphologicalGradientImageFilterISS3ISS3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMorphologicalGradientImageFilterISS3ISS3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMorphologicalGradientImageFilterISS3ISS3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMorphologicalGradientImageFilterISS3ISS3SE3.Clone = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_Clone, None, itkMorphologicalGradientImageFilterISS3ISS3SE3)
itkMorphologicalGradientImageFilterISS3ISS3SE3.SetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_SetAlgorithm, None, itkMorphologicalGradientImageFilterISS3ISS3SE3)
itkMorphologicalGradientImageFilterISS3ISS3SE3.GetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_GetAlgorithm, None, itkMorphologicalGradientImageFilterISS3ISS3SE3)
itkMorphologicalGradientImageFilterISS3ISS3SE3.GetPointer = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_GetPointer, None, itkMorphologicalGradientImageFilterISS3ISS3SE3)
itkMorphologicalGradientImageFilterISS3ISS3SE3_swigregister = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_swigregister
itkMorphologicalGradientImageFilterISS3ISS3SE3_swigregister(itkMorphologicalGradientImageFilterISS3ISS3SE3)

def itkMorphologicalGradientImageFilterISS3ISS3SE3___New_orig__():
    """itkMorphologicalGradientImageFilterISS3ISS3SE3___New_orig__() -> itkMorphologicalGradientImageFilterISS3ISS3SE3_Pointer"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3___New_orig__()

def itkMorphologicalGradientImageFilterISS3ISS3SE3_cast(obj):
    """itkMorphologicalGradientImageFilterISS3ISS3SE3_cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterISS3ISS3SE3"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterISS3ISS3SE3_cast(obj)

class itkMorphologicalGradientImageFilterIUC2IUC2SE2(itkFlatStructuringElementPython.itkKernelImageFilterIUC2IUC2SE2):
    """Proxy of C++ itkMorphologicalGradientImageFilterIUC2IUC2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMorphologicalGradientImageFilterIUC2IUC2SE2_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMorphologicalGradientImageFilterIUC2IUC2SE2 self) -> itkMorphologicalGradientImageFilterIUC2IUC2SE2_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_Clone(self)


    def SetAlgorithm(self, algo):
        """SetAlgorithm(itkMorphologicalGradientImageFilterIUC2IUC2SE2 self, int algo)"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_SetAlgorithm(self, algo)


    def GetAlgorithm(self):
        """GetAlgorithm(itkMorphologicalGradientImageFilterIUC2IUC2SE2 self) -> int"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_GetAlgorithm(self)

    BASIC = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_BASIC
    HISTO = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_HISTO
    ANCHOR = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_ANCHOR
    VHGW = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_VHGW
    __swig_destroy__ = _itkMorphologicalGradientImageFilterPython.delete_itkMorphologicalGradientImageFilterIUC2IUC2SE2

    def cast(obj):
        """cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIUC2IUC2SE2"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMorphologicalGradientImageFilterIUC2IUC2SE2 self) -> itkMorphologicalGradientImageFilterIUC2IUC2SE2"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMorphologicalGradientImageFilterIUC2IUC2SE2

        Create a new object of the class itkMorphologicalGradientImageFilterIUC2IUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMorphologicalGradientImageFilterIUC2IUC2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMorphologicalGradientImageFilterIUC2IUC2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMorphologicalGradientImageFilterIUC2IUC2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMorphologicalGradientImageFilterIUC2IUC2SE2.Clone = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_Clone, None, itkMorphologicalGradientImageFilterIUC2IUC2SE2)
itkMorphologicalGradientImageFilterIUC2IUC2SE2.SetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_SetAlgorithm, None, itkMorphologicalGradientImageFilterIUC2IUC2SE2)
itkMorphologicalGradientImageFilterIUC2IUC2SE2.GetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_GetAlgorithm, None, itkMorphologicalGradientImageFilterIUC2IUC2SE2)
itkMorphologicalGradientImageFilterIUC2IUC2SE2.GetPointer = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_GetPointer, None, itkMorphologicalGradientImageFilterIUC2IUC2SE2)
itkMorphologicalGradientImageFilterIUC2IUC2SE2_swigregister = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_swigregister
itkMorphologicalGradientImageFilterIUC2IUC2SE2_swigregister(itkMorphologicalGradientImageFilterIUC2IUC2SE2)

def itkMorphologicalGradientImageFilterIUC2IUC2SE2___New_orig__():
    """itkMorphologicalGradientImageFilterIUC2IUC2SE2___New_orig__() -> itkMorphologicalGradientImageFilterIUC2IUC2SE2_Pointer"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2___New_orig__()

def itkMorphologicalGradientImageFilterIUC2IUC2SE2_cast(obj):
    """itkMorphologicalGradientImageFilterIUC2IUC2SE2_cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIUC2IUC2SE2"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC2IUC2SE2_cast(obj)

class itkMorphologicalGradientImageFilterIUC3IUC3SE3(itkFlatStructuringElementPython.itkKernelImageFilterIUC3IUC3SE3):
    """Proxy of C++ itkMorphologicalGradientImageFilterIUC3IUC3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMorphologicalGradientImageFilterIUC3IUC3SE3_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMorphologicalGradientImageFilterIUC3IUC3SE3 self) -> itkMorphologicalGradientImageFilterIUC3IUC3SE3_Pointer"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_Clone(self)


    def SetAlgorithm(self, algo):
        """SetAlgorithm(itkMorphologicalGradientImageFilterIUC3IUC3SE3 self, int algo)"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_SetAlgorithm(self, algo)


    def GetAlgorithm(self):
        """GetAlgorithm(itkMorphologicalGradientImageFilterIUC3IUC3SE3 self) -> int"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_GetAlgorithm(self)

    BASIC = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_BASIC
    HISTO = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_HISTO
    ANCHOR = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_ANCHOR
    VHGW = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_VHGW
    __swig_destroy__ = _itkMorphologicalGradientImageFilterPython.delete_itkMorphologicalGradientImageFilterIUC3IUC3SE3

    def cast(obj):
        """cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIUC3IUC3SE3"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMorphologicalGradientImageFilterIUC3IUC3SE3 self) -> itkMorphologicalGradientImageFilterIUC3IUC3SE3"""
        return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMorphologicalGradientImageFilterIUC3IUC3SE3

        Create a new object of the class itkMorphologicalGradientImageFilterIUC3IUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMorphologicalGradientImageFilterIUC3IUC3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMorphologicalGradientImageFilterIUC3IUC3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMorphologicalGradientImageFilterIUC3IUC3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMorphologicalGradientImageFilterIUC3IUC3SE3.Clone = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_Clone, None, itkMorphologicalGradientImageFilterIUC3IUC3SE3)
itkMorphologicalGradientImageFilterIUC3IUC3SE3.SetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_SetAlgorithm, None, itkMorphologicalGradientImageFilterIUC3IUC3SE3)
itkMorphologicalGradientImageFilterIUC3IUC3SE3.GetAlgorithm = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_GetAlgorithm, None, itkMorphologicalGradientImageFilterIUC3IUC3SE3)
itkMorphologicalGradientImageFilterIUC3IUC3SE3.GetPointer = new_instancemethod(_itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_GetPointer, None, itkMorphologicalGradientImageFilterIUC3IUC3SE3)
itkMorphologicalGradientImageFilterIUC3IUC3SE3_swigregister = _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_swigregister
itkMorphologicalGradientImageFilterIUC3IUC3SE3_swigregister(itkMorphologicalGradientImageFilterIUC3IUC3SE3)

def itkMorphologicalGradientImageFilterIUC3IUC3SE3___New_orig__():
    """itkMorphologicalGradientImageFilterIUC3IUC3SE3___New_orig__() -> itkMorphologicalGradientImageFilterIUC3IUC3SE3_Pointer"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3___New_orig__()

def itkMorphologicalGradientImageFilterIUC3IUC3SE3_cast(obj):
    """itkMorphologicalGradientImageFilterIUC3IUC3SE3_cast(itkLightObject obj) -> itkMorphologicalGradientImageFilterIUC3IUC3SE3"""
    return _itkMorphologicalGradientImageFilterPython.itkMorphologicalGradientImageFilterIUC3IUC3SE3_cast(obj)



