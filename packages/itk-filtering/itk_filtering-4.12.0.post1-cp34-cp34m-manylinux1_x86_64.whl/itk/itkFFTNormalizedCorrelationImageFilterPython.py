# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFFTNormalizedCorrelationImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFFTNormalizedCorrelationImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFFTNormalizedCorrelationImageFilterPython')
    _itkFFTNormalizedCorrelationImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFFTNormalizedCorrelationImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFFTNormalizedCorrelationImageFilterPython
            return _itkFFTNormalizedCorrelationImageFilterPython
        try:
            _mod = imp.load_module('_itkFFTNormalizedCorrelationImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFFTNormalizedCorrelationImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFFTNormalizedCorrelationImageFilterPython
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


import itkMaskedFFTNormalizedCorrelationImageFilterPython
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
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkFFTNormalizedCorrelationImageFilterIF3IF3_New():
  return itkFFTNormalizedCorrelationImageFilterIF3IF3.New()


def itkFFTNormalizedCorrelationImageFilterIF2IF2_New():
  return itkFFTNormalizedCorrelationImageFilterIF2IF2.New()


def itkFFTNormalizedCorrelationImageFilterIUC3IF3_New():
  return itkFFTNormalizedCorrelationImageFilterIUC3IF3.New()


def itkFFTNormalizedCorrelationImageFilterIUC2IF2_New():
  return itkFFTNormalizedCorrelationImageFilterIUC2IF2.New()


def itkFFTNormalizedCorrelationImageFilterISS3IF3_New():
  return itkFFTNormalizedCorrelationImageFilterISS3IF3.New()


def itkFFTNormalizedCorrelationImageFilterISS2IF2_New():
  return itkFFTNormalizedCorrelationImageFilterISS2IF2.New()

class itkFFTNormalizedCorrelationImageFilterIF2IF2(itkMaskedFFTNormalizedCorrelationImageFilterPython.itkMaskedFFTNormalizedCorrelationImageFilterIF2IF2):
    """Proxy of C++ itkFFTNormalizedCorrelationImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkFFTNormalizedCorrelationImageFilterIF2IF2_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFFTNormalizedCorrelationImageFilterIF2IF2_Pointer":
        """Clone(itkFFTNormalizedCorrelationImageFilterIF2IF2 self) -> itkFFTNormalizedCorrelationImageFilterIF2IF2_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_Clone(self)

    __swig_destroy__ = _itkFFTNormalizedCorrelationImageFilterPython.delete_itkFFTNormalizedCorrelationImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIF2IF2"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFFTNormalizedCorrelationImageFilterIF2IF2 *":
        """GetPointer(itkFFTNormalizedCorrelationImageFilterIF2IF2 self) -> itkFFTNormalizedCorrelationImageFilterIF2IF2"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFFTNormalizedCorrelationImageFilterIF2IF2

        Create a new object of the class itkFFTNormalizedCorrelationImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFFTNormalizedCorrelationImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFFTNormalizedCorrelationImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFFTNormalizedCorrelationImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFFTNormalizedCorrelationImageFilterIF2IF2.Clone = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_Clone, None, itkFFTNormalizedCorrelationImageFilterIF2IF2)
itkFFTNormalizedCorrelationImageFilterIF2IF2.GetPointer = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_GetPointer, None, itkFFTNormalizedCorrelationImageFilterIF2IF2)
itkFFTNormalizedCorrelationImageFilterIF2IF2_swigregister = _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_swigregister
itkFFTNormalizedCorrelationImageFilterIF2IF2_swigregister(itkFFTNormalizedCorrelationImageFilterIF2IF2)

def itkFFTNormalizedCorrelationImageFilterIF2IF2___New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIF2IF2_Pointer":
    """itkFFTNormalizedCorrelationImageFilterIF2IF2___New_orig__() -> itkFFTNormalizedCorrelationImageFilterIF2IF2_Pointer"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2___New_orig__()

def itkFFTNormalizedCorrelationImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIF2IF2 *":
    """itkFFTNormalizedCorrelationImageFilterIF2IF2_cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIF2IF2"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF2IF2_cast(obj)

class itkFFTNormalizedCorrelationImageFilterIF3IF3(itkMaskedFFTNormalizedCorrelationImageFilterPython.itkMaskedFFTNormalizedCorrelationImageFilterIF3IF3):
    """Proxy of C++ itkFFTNormalizedCorrelationImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkFFTNormalizedCorrelationImageFilterIF3IF3_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFFTNormalizedCorrelationImageFilterIF3IF3_Pointer":
        """Clone(itkFFTNormalizedCorrelationImageFilterIF3IF3 self) -> itkFFTNormalizedCorrelationImageFilterIF3IF3_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_Clone(self)

    __swig_destroy__ = _itkFFTNormalizedCorrelationImageFilterPython.delete_itkFFTNormalizedCorrelationImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIF3IF3"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFFTNormalizedCorrelationImageFilterIF3IF3 *":
        """GetPointer(itkFFTNormalizedCorrelationImageFilterIF3IF3 self) -> itkFFTNormalizedCorrelationImageFilterIF3IF3"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFFTNormalizedCorrelationImageFilterIF3IF3

        Create a new object of the class itkFFTNormalizedCorrelationImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFFTNormalizedCorrelationImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFFTNormalizedCorrelationImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFFTNormalizedCorrelationImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFFTNormalizedCorrelationImageFilterIF3IF3.Clone = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_Clone, None, itkFFTNormalizedCorrelationImageFilterIF3IF3)
itkFFTNormalizedCorrelationImageFilterIF3IF3.GetPointer = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_GetPointer, None, itkFFTNormalizedCorrelationImageFilterIF3IF3)
itkFFTNormalizedCorrelationImageFilterIF3IF3_swigregister = _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_swigregister
itkFFTNormalizedCorrelationImageFilterIF3IF3_swigregister(itkFFTNormalizedCorrelationImageFilterIF3IF3)

def itkFFTNormalizedCorrelationImageFilterIF3IF3___New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIF3IF3_Pointer":
    """itkFFTNormalizedCorrelationImageFilterIF3IF3___New_orig__() -> itkFFTNormalizedCorrelationImageFilterIF3IF3_Pointer"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3___New_orig__()

def itkFFTNormalizedCorrelationImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIF3IF3 *":
    """itkFFTNormalizedCorrelationImageFilterIF3IF3_cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIF3IF3"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIF3IF3_cast(obj)

class itkFFTNormalizedCorrelationImageFilterISS2IF2(itkMaskedFFTNormalizedCorrelationImageFilterPython.itkMaskedFFTNormalizedCorrelationImageFilterISS2IF2):
    """Proxy of C++ itkFFTNormalizedCorrelationImageFilterISS2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFFTNormalizedCorrelationImageFilterISS2IF2_Pointer":
        """__New_orig__() -> itkFFTNormalizedCorrelationImageFilterISS2IF2_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFFTNormalizedCorrelationImageFilterISS2IF2_Pointer":
        """Clone(itkFFTNormalizedCorrelationImageFilterISS2IF2 self) -> itkFFTNormalizedCorrelationImageFilterISS2IF2_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_Clone(self)

    __swig_destroy__ = _itkFFTNormalizedCorrelationImageFilterPython.delete_itkFFTNormalizedCorrelationImageFilterISS2IF2

    def cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterISS2IF2 *":
        """cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterISS2IF2"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFFTNormalizedCorrelationImageFilterISS2IF2 *":
        """GetPointer(itkFFTNormalizedCorrelationImageFilterISS2IF2 self) -> itkFFTNormalizedCorrelationImageFilterISS2IF2"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFFTNormalizedCorrelationImageFilterISS2IF2

        Create a new object of the class itkFFTNormalizedCorrelationImageFilterISS2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFFTNormalizedCorrelationImageFilterISS2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFFTNormalizedCorrelationImageFilterISS2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFFTNormalizedCorrelationImageFilterISS2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFFTNormalizedCorrelationImageFilterISS2IF2.Clone = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_Clone, None, itkFFTNormalizedCorrelationImageFilterISS2IF2)
itkFFTNormalizedCorrelationImageFilterISS2IF2.GetPointer = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_GetPointer, None, itkFFTNormalizedCorrelationImageFilterISS2IF2)
itkFFTNormalizedCorrelationImageFilterISS2IF2_swigregister = _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_swigregister
itkFFTNormalizedCorrelationImageFilterISS2IF2_swigregister(itkFFTNormalizedCorrelationImageFilterISS2IF2)

def itkFFTNormalizedCorrelationImageFilterISS2IF2___New_orig__() -> "itkFFTNormalizedCorrelationImageFilterISS2IF2_Pointer":
    """itkFFTNormalizedCorrelationImageFilterISS2IF2___New_orig__() -> itkFFTNormalizedCorrelationImageFilterISS2IF2_Pointer"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2___New_orig__()

def itkFFTNormalizedCorrelationImageFilterISS2IF2_cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterISS2IF2 *":
    """itkFFTNormalizedCorrelationImageFilterISS2IF2_cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterISS2IF2"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS2IF2_cast(obj)

class itkFFTNormalizedCorrelationImageFilterISS3IF3(itkMaskedFFTNormalizedCorrelationImageFilterPython.itkMaskedFFTNormalizedCorrelationImageFilterISS3IF3):
    """Proxy of C++ itkFFTNormalizedCorrelationImageFilterISS3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFFTNormalizedCorrelationImageFilterISS3IF3_Pointer":
        """__New_orig__() -> itkFFTNormalizedCorrelationImageFilterISS3IF3_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFFTNormalizedCorrelationImageFilterISS3IF3_Pointer":
        """Clone(itkFFTNormalizedCorrelationImageFilterISS3IF3 self) -> itkFFTNormalizedCorrelationImageFilterISS3IF3_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_Clone(self)

    __swig_destroy__ = _itkFFTNormalizedCorrelationImageFilterPython.delete_itkFFTNormalizedCorrelationImageFilterISS3IF3

    def cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterISS3IF3 *":
        """cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterISS3IF3"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFFTNormalizedCorrelationImageFilterISS3IF3 *":
        """GetPointer(itkFFTNormalizedCorrelationImageFilterISS3IF3 self) -> itkFFTNormalizedCorrelationImageFilterISS3IF3"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFFTNormalizedCorrelationImageFilterISS3IF3

        Create a new object of the class itkFFTNormalizedCorrelationImageFilterISS3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFFTNormalizedCorrelationImageFilterISS3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFFTNormalizedCorrelationImageFilterISS3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFFTNormalizedCorrelationImageFilterISS3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFFTNormalizedCorrelationImageFilterISS3IF3.Clone = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_Clone, None, itkFFTNormalizedCorrelationImageFilterISS3IF3)
itkFFTNormalizedCorrelationImageFilterISS3IF3.GetPointer = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_GetPointer, None, itkFFTNormalizedCorrelationImageFilterISS3IF3)
itkFFTNormalizedCorrelationImageFilterISS3IF3_swigregister = _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_swigregister
itkFFTNormalizedCorrelationImageFilterISS3IF3_swigregister(itkFFTNormalizedCorrelationImageFilterISS3IF3)

def itkFFTNormalizedCorrelationImageFilterISS3IF3___New_orig__() -> "itkFFTNormalizedCorrelationImageFilterISS3IF3_Pointer":
    """itkFFTNormalizedCorrelationImageFilterISS3IF3___New_orig__() -> itkFFTNormalizedCorrelationImageFilterISS3IF3_Pointer"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3___New_orig__()

def itkFFTNormalizedCorrelationImageFilterISS3IF3_cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterISS3IF3 *":
    """itkFFTNormalizedCorrelationImageFilterISS3IF3_cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterISS3IF3"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterISS3IF3_cast(obj)

class itkFFTNormalizedCorrelationImageFilterIUC2IF2(itkMaskedFFTNormalizedCorrelationImageFilterPython.itkMaskedFFTNormalizedCorrelationImageFilterIUC2IF2):
    """Proxy of C++ itkFFTNormalizedCorrelationImageFilterIUC2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIUC2IF2_Pointer":
        """__New_orig__() -> itkFFTNormalizedCorrelationImageFilterIUC2IF2_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFFTNormalizedCorrelationImageFilterIUC2IF2_Pointer":
        """Clone(itkFFTNormalizedCorrelationImageFilterIUC2IF2 self) -> itkFFTNormalizedCorrelationImageFilterIUC2IF2_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_Clone(self)

    __swig_destroy__ = _itkFFTNormalizedCorrelationImageFilterPython.delete_itkFFTNormalizedCorrelationImageFilterIUC2IF2

    def cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIUC2IF2 *":
        """cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIUC2IF2"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFFTNormalizedCorrelationImageFilterIUC2IF2 *":
        """GetPointer(itkFFTNormalizedCorrelationImageFilterIUC2IF2 self) -> itkFFTNormalizedCorrelationImageFilterIUC2IF2"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFFTNormalizedCorrelationImageFilterIUC2IF2

        Create a new object of the class itkFFTNormalizedCorrelationImageFilterIUC2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFFTNormalizedCorrelationImageFilterIUC2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFFTNormalizedCorrelationImageFilterIUC2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFFTNormalizedCorrelationImageFilterIUC2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFFTNormalizedCorrelationImageFilterIUC2IF2.Clone = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_Clone, None, itkFFTNormalizedCorrelationImageFilterIUC2IF2)
itkFFTNormalizedCorrelationImageFilterIUC2IF2.GetPointer = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_GetPointer, None, itkFFTNormalizedCorrelationImageFilterIUC2IF2)
itkFFTNormalizedCorrelationImageFilterIUC2IF2_swigregister = _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_swigregister
itkFFTNormalizedCorrelationImageFilterIUC2IF2_swigregister(itkFFTNormalizedCorrelationImageFilterIUC2IF2)

def itkFFTNormalizedCorrelationImageFilterIUC2IF2___New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIUC2IF2_Pointer":
    """itkFFTNormalizedCorrelationImageFilterIUC2IF2___New_orig__() -> itkFFTNormalizedCorrelationImageFilterIUC2IF2_Pointer"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2___New_orig__()

def itkFFTNormalizedCorrelationImageFilterIUC2IF2_cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIUC2IF2 *":
    """itkFFTNormalizedCorrelationImageFilterIUC2IF2_cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIUC2IF2"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC2IF2_cast(obj)

class itkFFTNormalizedCorrelationImageFilterIUC3IF3(itkMaskedFFTNormalizedCorrelationImageFilterPython.itkMaskedFFTNormalizedCorrelationImageFilterIUC3IF3):
    """Proxy of C++ itkFFTNormalizedCorrelationImageFilterIUC3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIUC3IF3_Pointer":
        """__New_orig__() -> itkFFTNormalizedCorrelationImageFilterIUC3IF3_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFFTNormalizedCorrelationImageFilterIUC3IF3_Pointer":
        """Clone(itkFFTNormalizedCorrelationImageFilterIUC3IF3 self) -> itkFFTNormalizedCorrelationImageFilterIUC3IF3_Pointer"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_Clone(self)

    __swig_destroy__ = _itkFFTNormalizedCorrelationImageFilterPython.delete_itkFFTNormalizedCorrelationImageFilterIUC3IF3

    def cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIUC3IF3 *":
        """cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIUC3IF3"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFFTNormalizedCorrelationImageFilterIUC3IF3 *":
        """GetPointer(itkFFTNormalizedCorrelationImageFilterIUC3IF3 self) -> itkFFTNormalizedCorrelationImageFilterIUC3IF3"""
        return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFFTNormalizedCorrelationImageFilterIUC3IF3

        Create a new object of the class itkFFTNormalizedCorrelationImageFilterIUC3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFFTNormalizedCorrelationImageFilterIUC3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFFTNormalizedCorrelationImageFilterIUC3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFFTNormalizedCorrelationImageFilterIUC3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFFTNormalizedCorrelationImageFilterIUC3IF3.Clone = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_Clone, None, itkFFTNormalizedCorrelationImageFilterIUC3IF3)
itkFFTNormalizedCorrelationImageFilterIUC3IF3.GetPointer = new_instancemethod(_itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_GetPointer, None, itkFFTNormalizedCorrelationImageFilterIUC3IF3)
itkFFTNormalizedCorrelationImageFilterIUC3IF3_swigregister = _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_swigregister
itkFFTNormalizedCorrelationImageFilterIUC3IF3_swigregister(itkFFTNormalizedCorrelationImageFilterIUC3IF3)

def itkFFTNormalizedCorrelationImageFilterIUC3IF3___New_orig__() -> "itkFFTNormalizedCorrelationImageFilterIUC3IF3_Pointer":
    """itkFFTNormalizedCorrelationImageFilterIUC3IF3___New_orig__() -> itkFFTNormalizedCorrelationImageFilterIUC3IF3_Pointer"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3___New_orig__()

def itkFFTNormalizedCorrelationImageFilterIUC3IF3_cast(obj: 'itkLightObject') -> "itkFFTNormalizedCorrelationImageFilterIUC3IF3 *":
    """itkFFTNormalizedCorrelationImageFilterIUC3IF3_cast(itkLightObject obj) -> itkFFTNormalizedCorrelationImageFilterIUC3IF3"""
    return _itkFFTNormalizedCorrelationImageFilterPython.itkFFTNormalizedCorrelationImageFilterIUC3IF3_cast(obj)



