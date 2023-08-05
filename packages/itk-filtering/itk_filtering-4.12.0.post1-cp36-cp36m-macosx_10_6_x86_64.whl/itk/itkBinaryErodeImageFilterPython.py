# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryErodeImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinaryErodeImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinaryErodeImageFilterPython')
    _itkBinaryErodeImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryErodeImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryErodeImageFilterPython
            return _itkBinaryErodeImageFilterPython
        try:
            _mod = imp.load_module('_itkBinaryErodeImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinaryErodeImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryErodeImageFilterPython
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
import itkBinaryDilateImageFilterPython
import itkFlatStructuringElementPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkNeighborhoodPython
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkBinaryErodeImageFilterIF3IF3SE3_New():
  return itkBinaryErodeImageFilterIF3IF3SE3.New()


def itkBinaryErodeImageFilterIUC3IUC3SE3_New():
  return itkBinaryErodeImageFilterIUC3IUC3SE3.New()


def itkBinaryErodeImageFilterISS3ISS3SE3_New():
  return itkBinaryErodeImageFilterISS3ISS3SE3.New()


def itkBinaryErodeImageFilterIF2IF2SE2_New():
  return itkBinaryErodeImageFilterIF2IF2SE2.New()


def itkBinaryErodeImageFilterIUC2IUC2SE2_New():
  return itkBinaryErodeImageFilterIUC2IUC2SE2.New()


def itkBinaryErodeImageFilterISS2ISS2SE2_New():
  return itkBinaryErodeImageFilterISS2ISS2SE2.New()

class itkBinaryErodeImageFilterIF2IF2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIF2IF2SE2_Superclass):
    """Proxy of C++ itkBinaryErodeImageFilterIF2IF2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryErodeImageFilterIF2IF2SE2_Pointer":
        """__New_orig__() -> itkBinaryErodeImageFilterIF2IF2SE2_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryErodeImageFilterIF2IF2SE2_Pointer":
        """Clone(itkBinaryErodeImageFilterIF2IF2SE2 self) -> itkBinaryErodeImageFilterIF2IF2SE2_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_Clone(self)


    def SetErodeValue(self, value: 'float const &') -> "void":
        """SetErodeValue(itkBinaryErodeImageFilterIF2IF2SE2 self, float const & value)"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_SetErodeValue(self, value)


    def GetErodeValue(self) -> "float":
        """GetErodeValue(itkBinaryErodeImageFilterIF2IF2SE2 self) -> float"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_GetErodeValue(self)

    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIF2IF2SE2

    def cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIF2IF2SE2 *":
        """cast(itkLightObject obj) -> itkBinaryErodeImageFilterIF2IF2SE2"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryErodeImageFilterIF2IF2SE2 *":
        """GetPointer(itkBinaryErodeImageFilterIF2IF2SE2 self) -> itkBinaryErodeImageFilterIF2IF2SE2"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIF2IF2SE2

        Create a new object of the class itkBinaryErodeImageFilterIF2IF2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIF2IF2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIF2IF2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIF2IF2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryErodeImageFilterIF2IF2SE2.Clone = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_Clone, None, itkBinaryErodeImageFilterIF2IF2SE2)
itkBinaryErodeImageFilterIF2IF2SE2.SetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_SetErodeValue, None, itkBinaryErodeImageFilterIF2IF2SE2)
itkBinaryErodeImageFilterIF2IF2SE2.GetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_GetErodeValue, None, itkBinaryErodeImageFilterIF2IF2SE2)
itkBinaryErodeImageFilterIF2IF2SE2.GetPointer = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_GetPointer, None, itkBinaryErodeImageFilterIF2IF2SE2)
itkBinaryErodeImageFilterIF2IF2SE2_swigregister = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_swigregister
itkBinaryErodeImageFilterIF2IF2SE2_swigregister(itkBinaryErodeImageFilterIF2IF2SE2)

def itkBinaryErodeImageFilterIF2IF2SE2___New_orig__() -> "itkBinaryErodeImageFilterIF2IF2SE2_Pointer":
    """itkBinaryErodeImageFilterIF2IF2SE2___New_orig__() -> itkBinaryErodeImageFilterIF2IF2SE2_Pointer"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2___New_orig__()

def itkBinaryErodeImageFilterIF2IF2SE2_cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIF2IF2SE2 *":
    """itkBinaryErodeImageFilterIF2IF2SE2_cast(itkLightObject obj) -> itkBinaryErodeImageFilterIF2IF2SE2"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_cast(obj)

class itkBinaryErodeImageFilterIF3IF3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIF3IF3SE3_Superclass):
    """Proxy of C++ itkBinaryErodeImageFilterIF3IF3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryErodeImageFilterIF3IF3SE3_Pointer":
        """__New_orig__() -> itkBinaryErodeImageFilterIF3IF3SE3_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryErodeImageFilterIF3IF3SE3_Pointer":
        """Clone(itkBinaryErodeImageFilterIF3IF3SE3 self) -> itkBinaryErodeImageFilterIF3IF3SE3_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_Clone(self)


    def SetErodeValue(self, value: 'float const &') -> "void":
        """SetErodeValue(itkBinaryErodeImageFilterIF3IF3SE3 self, float const & value)"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_SetErodeValue(self, value)


    def GetErodeValue(self) -> "float":
        """GetErodeValue(itkBinaryErodeImageFilterIF3IF3SE3 self) -> float"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_GetErodeValue(self)

    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIF3IF3SE3

    def cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIF3IF3SE3 *":
        """cast(itkLightObject obj) -> itkBinaryErodeImageFilterIF3IF3SE3"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryErodeImageFilterIF3IF3SE3 *":
        """GetPointer(itkBinaryErodeImageFilterIF3IF3SE3 self) -> itkBinaryErodeImageFilterIF3IF3SE3"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIF3IF3SE3

        Create a new object of the class itkBinaryErodeImageFilterIF3IF3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIF3IF3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIF3IF3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIF3IF3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryErodeImageFilterIF3IF3SE3.Clone = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_Clone, None, itkBinaryErodeImageFilterIF3IF3SE3)
itkBinaryErodeImageFilterIF3IF3SE3.SetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_SetErodeValue, None, itkBinaryErodeImageFilterIF3IF3SE3)
itkBinaryErodeImageFilterIF3IF3SE3.GetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_GetErodeValue, None, itkBinaryErodeImageFilterIF3IF3SE3)
itkBinaryErodeImageFilterIF3IF3SE3.GetPointer = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_GetPointer, None, itkBinaryErodeImageFilterIF3IF3SE3)
itkBinaryErodeImageFilterIF3IF3SE3_swigregister = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_swigregister
itkBinaryErodeImageFilterIF3IF3SE3_swigregister(itkBinaryErodeImageFilterIF3IF3SE3)

def itkBinaryErodeImageFilterIF3IF3SE3___New_orig__() -> "itkBinaryErodeImageFilterIF3IF3SE3_Pointer":
    """itkBinaryErodeImageFilterIF3IF3SE3___New_orig__() -> itkBinaryErodeImageFilterIF3IF3SE3_Pointer"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3___New_orig__()

def itkBinaryErodeImageFilterIF3IF3SE3_cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIF3IF3SE3 *":
    """itkBinaryErodeImageFilterIF3IF3SE3_cast(itkLightObject obj) -> itkBinaryErodeImageFilterIF3IF3SE3"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_cast(obj)

class itkBinaryErodeImageFilterISS2ISS2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterISS2ISS2SE2_Superclass):
    """Proxy of C++ itkBinaryErodeImageFilterISS2ISS2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryErodeImageFilterISS2ISS2SE2_Pointer":
        """__New_orig__() -> itkBinaryErodeImageFilterISS2ISS2SE2_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryErodeImageFilterISS2ISS2SE2_Pointer":
        """Clone(itkBinaryErodeImageFilterISS2ISS2SE2 self) -> itkBinaryErodeImageFilterISS2ISS2SE2_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_Clone(self)


    def SetErodeValue(self, value: 'short const &') -> "void":
        """SetErodeValue(itkBinaryErodeImageFilterISS2ISS2SE2 self, short const & value)"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_SetErodeValue(self, value)


    def GetErodeValue(self) -> "short":
        """GetErodeValue(itkBinaryErodeImageFilterISS2ISS2SE2 self) -> short"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_GetErodeValue(self)

    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterISS2ISS2SE2

    def cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterISS2ISS2SE2 *":
        """cast(itkLightObject obj) -> itkBinaryErodeImageFilterISS2ISS2SE2"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryErodeImageFilterISS2ISS2SE2 *":
        """GetPointer(itkBinaryErodeImageFilterISS2ISS2SE2 self) -> itkBinaryErodeImageFilterISS2ISS2SE2"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterISS2ISS2SE2

        Create a new object of the class itkBinaryErodeImageFilterISS2ISS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterISS2ISS2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterISS2ISS2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterISS2ISS2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryErodeImageFilterISS2ISS2SE2.Clone = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_Clone, None, itkBinaryErodeImageFilterISS2ISS2SE2)
itkBinaryErodeImageFilterISS2ISS2SE2.SetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_SetErodeValue, None, itkBinaryErodeImageFilterISS2ISS2SE2)
itkBinaryErodeImageFilterISS2ISS2SE2.GetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_GetErodeValue, None, itkBinaryErodeImageFilterISS2ISS2SE2)
itkBinaryErodeImageFilterISS2ISS2SE2.GetPointer = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_GetPointer, None, itkBinaryErodeImageFilterISS2ISS2SE2)
itkBinaryErodeImageFilterISS2ISS2SE2_swigregister = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_swigregister
itkBinaryErodeImageFilterISS2ISS2SE2_swigregister(itkBinaryErodeImageFilterISS2ISS2SE2)

def itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__() -> "itkBinaryErodeImageFilterISS2ISS2SE2_Pointer":
    """itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__() -> itkBinaryErodeImageFilterISS2ISS2SE2_Pointer"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__()

def itkBinaryErodeImageFilterISS2ISS2SE2_cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterISS2ISS2SE2 *":
    """itkBinaryErodeImageFilterISS2ISS2SE2_cast(itkLightObject obj) -> itkBinaryErodeImageFilterISS2ISS2SE2"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_cast(obj)

class itkBinaryErodeImageFilterISS3ISS3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterISS3ISS3SE3_Superclass):
    """Proxy of C++ itkBinaryErodeImageFilterISS3ISS3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryErodeImageFilterISS3ISS3SE3_Pointer":
        """__New_orig__() -> itkBinaryErodeImageFilterISS3ISS3SE3_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryErodeImageFilterISS3ISS3SE3_Pointer":
        """Clone(itkBinaryErodeImageFilterISS3ISS3SE3 self) -> itkBinaryErodeImageFilterISS3ISS3SE3_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_Clone(self)


    def SetErodeValue(self, value: 'short const &') -> "void":
        """SetErodeValue(itkBinaryErodeImageFilterISS3ISS3SE3 self, short const & value)"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_SetErodeValue(self, value)


    def GetErodeValue(self) -> "short":
        """GetErodeValue(itkBinaryErodeImageFilterISS3ISS3SE3 self) -> short"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_GetErodeValue(self)

    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterISS3ISS3SE3

    def cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterISS3ISS3SE3 *":
        """cast(itkLightObject obj) -> itkBinaryErodeImageFilterISS3ISS3SE3"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryErodeImageFilterISS3ISS3SE3 *":
        """GetPointer(itkBinaryErodeImageFilterISS3ISS3SE3 self) -> itkBinaryErodeImageFilterISS3ISS3SE3"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterISS3ISS3SE3

        Create a new object of the class itkBinaryErodeImageFilterISS3ISS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterISS3ISS3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterISS3ISS3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterISS3ISS3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryErodeImageFilterISS3ISS3SE3.Clone = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_Clone, None, itkBinaryErodeImageFilterISS3ISS3SE3)
itkBinaryErodeImageFilterISS3ISS3SE3.SetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_SetErodeValue, None, itkBinaryErodeImageFilterISS3ISS3SE3)
itkBinaryErodeImageFilterISS3ISS3SE3.GetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_GetErodeValue, None, itkBinaryErodeImageFilterISS3ISS3SE3)
itkBinaryErodeImageFilterISS3ISS3SE3.GetPointer = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_GetPointer, None, itkBinaryErodeImageFilterISS3ISS3SE3)
itkBinaryErodeImageFilterISS3ISS3SE3_swigregister = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_swigregister
itkBinaryErodeImageFilterISS3ISS3SE3_swigregister(itkBinaryErodeImageFilterISS3ISS3SE3)

def itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__() -> "itkBinaryErodeImageFilterISS3ISS3SE3_Pointer":
    """itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__() -> itkBinaryErodeImageFilterISS3ISS3SE3_Pointer"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__()

def itkBinaryErodeImageFilterISS3ISS3SE3_cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterISS3ISS3SE3 *":
    """itkBinaryErodeImageFilterISS3ISS3SE3_cast(itkLightObject obj) -> itkBinaryErodeImageFilterISS3ISS3SE3"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_cast(obj)

class itkBinaryErodeImageFilterIUC2IUC2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIUC2IUC2SE2_Superclass):
    """Proxy of C++ itkBinaryErodeImageFilterIUC2IUC2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryErodeImageFilterIUC2IUC2SE2_Pointer":
        """__New_orig__() -> itkBinaryErodeImageFilterIUC2IUC2SE2_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryErodeImageFilterIUC2IUC2SE2_Pointer":
        """Clone(itkBinaryErodeImageFilterIUC2IUC2SE2 self) -> itkBinaryErodeImageFilterIUC2IUC2SE2_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_Clone(self)


    def SetErodeValue(self, value: 'unsigned char const &') -> "void":
        """SetErodeValue(itkBinaryErodeImageFilterIUC2IUC2SE2 self, unsigned char const & value)"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_SetErodeValue(self, value)


    def GetErodeValue(self) -> "unsigned char":
        """GetErodeValue(itkBinaryErodeImageFilterIUC2IUC2SE2 self) -> unsigned char"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_GetErodeValue(self)

    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIUC2IUC2SE2

    def cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIUC2IUC2SE2 *":
        """cast(itkLightObject obj) -> itkBinaryErodeImageFilterIUC2IUC2SE2"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryErodeImageFilterIUC2IUC2SE2 *":
        """GetPointer(itkBinaryErodeImageFilterIUC2IUC2SE2 self) -> itkBinaryErodeImageFilterIUC2IUC2SE2"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIUC2IUC2SE2

        Create a new object of the class itkBinaryErodeImageFilterIUC2IUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIUC2IUC2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIUC2IUC2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIUC2IUC2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryErodeImageFilterIUC2IUC2SE2.Clone = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_Clone, None, itkBinaryErodeImageFilterIUC2IUC2SE2)
itkBinaryErodeImageFilterIUC2IUC2SE2.SetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_SetErodeValue, None, itkBinaryErodeImageFilterIUC2IUC2SE2)
itkBinaryErodeImageFilterIUC2IUC2SE2.GetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_GetErodeValue, None, itkBinaryErodeImageFilterIUC2IUC2SE2)
itkBinaryErodeImageFilterIUC2IUC2SE2.GetPointer = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_GetPointer, None, itkBinaryErodeImageFilterIUC2IUC2SE2)
itkBinaryErodeImageFilterIUC2IUC2SE2_swigregister = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_swigregister
itkBinaryErodeImageFilterIUC2IUC2SE2_swigregister(itkBinaryErodeImageFilterIUC2IUC2SE2)

def itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__() -> "itkBinaryErodeImageFilterIUC2IUC2SE2_Pointer":
    """itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__() -> itkBinaryErodeImageFilterIUC2IUC2SE2_Pointer"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__()

def itkBinaryErodeImageFilterIUC2IUC2SE2_cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIUC2IUC2SE2 *":
    """itkBinaryErodeImageFilterIUC2IUC2SE2_cast(itkLightObject obj) -> itkBinaryErodeImageFilterIUC2IUC2SE2"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_cast(obj)

class itkBinaryErodeImageFilterIUC3IUC3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIUC3IUC3SE3_Superclass):
    """Proxy of C++ itkBinaryErodeImageFilterIUC3IUC3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryErodeImageFilterIUC3IUC3SE3_Pointer":
        """__New_orig__() -> itkBinaryErodeImageFilterIUC3IUC3SE3_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryErodeImageFilterIUC3IUC3SE3_Pointer":
        """Clone(itkBinaryErodeImageFilterIUC3IUC3SE3 self) -> itkBinaryErodeImageFilterIUC3IUC3SE3_Pointer"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_Clone(self)


    def SetErodeValue(self, value: 'unsigned char const &') -> "void":
        """SetErodeValue(itkBinaryErodeImageFilterIUC3IUC3SE3 self, unsigned char const & value)"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_SetErodeValue(self, value)


    def GetErodeValue(self) -> "unsigned char":
        """GetErodeValue(itkBinaryErodeImageFilterIUC3IUC3SE3 self) -> unsigned char"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_GetErodeValue(self)

    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIUC3IUC3SE3

    def cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIUC3IUC3SE3 *":
        """cast(itkLightObject obj) -> itkBinaryErodeImageFilterIUC3IUC3SE3"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryErodeImageFilterIUC3IUC3SE3 *":
        """GetPointer(itkBinaryErodeImageFilterIUC3IUC3SE3 self) -> itkBinaryErodeImageFilterIUC3IUC3SE3"""
        return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIUC3IUC3SE3

        Create a new object of the class itkBinaryErodeImageFilterIUC3IUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIUC3IUC3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIUC3IUC3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIUC3IUC3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryErodeImageFilterIUC3IUC3SE3.Clone = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_Clone, None, itkBinaryErodeImageFilterIUC3IUC3SE3)
itkBinaryErodeImageFilterIUC3IUC3SE3.SetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_SetErodeValue, None, itkBinaryErodeImageFilterIUC3IUC3SE3)
itkBinaryErodeImageFilterIUC3IUC3SE3.GetErodeValue = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_GetErodeValue, None, itkBinaryErodeImageFilterIUC3IUC3SE3)
itkBinaryErodeImageFilterIUC3IUC3SE3.GetPointer = new_instancemethod(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_GetPointer, None, itkBinaryErodeImageFilterIUC3IUC3SE3)
itkBinaryErodeImageFilterIUC3IUC3SE3_swigregister = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_swigregister
itkBinaryErodeImageFilterIUC3IUC3SE3_swigregister(itkBinaryErodeImageFilterIUC3IUC3SE3)

def itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__() -> "itkBinaryErodeImageFilterIUC3IUC3SE3_Pointer":
    """itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__() -> itkBinaryErodeImageFilterIUC3IUC3SE3_Pointer"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__()

def itkBinaryErodeImageFilterIUC3IUC3SE3_cast(obj: 'itkLightObject') -> "itkBinaryErodeImageFilterIUC3IUC3SE3 *":
    """itkBinaryErodeImageFilterIUC3IUC3SE3_cast(itkLightObject obj) -> itkBinaryErodeImageFilterIUC3IUC3SE3"""
    return _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_cast(obj)



