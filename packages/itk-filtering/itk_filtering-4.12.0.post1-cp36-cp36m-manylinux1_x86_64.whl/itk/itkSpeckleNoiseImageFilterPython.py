# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSpeckleNoiseImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSpeckleNoiseImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSpeckleNoiseImageFilterPython')
    _itkSpeckleNoiseImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSpeckleNoiseImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSpeckleNoiseImageFilterPython
            return _itkSpeckleNoiseImageFilterPython
        try:
            _mod = imp.load_module('_itkSpeckleNoiseImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSpeckleNoiseImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSpeckleNoiseImageFilterPython
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


import itkNoiseBaseImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import pyBasePython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
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
import ITKCommonBasePython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython

def itkSpeckleNoiseImageFilterIF3IF3_New():
  return itkSpeckleNoiseImageFilterIF3IF3.New()


def itkSpeckleNoiseImageFilterIF2IF2_New():
  return itkSpeckleNoiseImageFilterIF2IF2.New()


def itkSpeckleNoiseImageFilterIUC3IUC3_New():
  return itkSpeckleNoiseImageFilterIUC3IUC3.New()


def itkSpeckleNoiseImageFilterIUC2IUC2_New():
  return itkSpeckleNoiseImageFilterIUC2IUC2.New()


def itkSpeckleNoiseImageFilterISS3ISS3_New():
  return itkSpeckleNoiseImageFilterISS3ISS3.New()


def itkSpeckleNoiseImageFilterISS2ISS2_New():
  return itkSpeckleNoiseImageFilterISS2ISS2.New()

class itkSpeckleNoiseImageFilterIF2IF2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF2IF2):
    """Proxy of C++ itkSpeckleNoiseImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpeckleNoiseImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSpeckleNoiseImageFilterIF2IF2_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpeckleNoiseImageFilterIF2IF2_Pointer":
        """Clone(itkSpeckleNoiseImageFilterIF2IF2 self) -> itkSpeckleNoiseImageFilterIF2IF2_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_Clone(self)


    def GetStandardDeviation(self) -> "double":
        """GetStandardDeviation(itkSpeckleNoiseImageFilterIF2IF2 self) -> double"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_GetStandardDeviation(self)


    def SetStandardDeviation(self, _arg: 'double const') -> "void":
        """SetStandardDeviation(itkSpeckleNoiseImageFilterIF2IF2 self, double const _arg)"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_SetStandardDeviation(self, _arg)

    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIF2IF2"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpeckleNoiseImageFilterIF2IF2 *":
        """GetPointer(itkSpeckleNoiseImageFilterIF2IF2 self) -> itkSpeckleNoiseImageFilterIF2IF2"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIF2IF2

        Create a new object of the class itkSpeckleNoiseImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpeckleNoiseImageFilterIF2IF2.Clone = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_Clone, None, itkSpeckleNoiseImageFilterIF2IF2)
itkSpeckleNoiseImageFilterIF2IF2.GetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_GetStandardDeviation, None, itkSpeckleNoiseImageFilterIF2IF2)
itkSpeckleNoiseImageFilterIF2IF2.SetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_SetStandardDeviation, None, itkSpeckleNoiseImageFilterIF2IF2)
itkSpeckleNoiseImageFilterIF2IF2.GetPointer = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_GetPointer, None, itkSpeckleNoiseImageFilterIF2IF2)
itkSpeckleNoiseImageFilterIF2IF2_swigregister = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_swigregister
itkSpeckleNoiseImageFilterIF2IF2_swigregister(itkSpeckleNoiseImageFilterIF2IF2)

def itkSpeckleNoiseImageFilterIF2IF2___New_orig__() -> "itkSpeckleNoiseImageFilterIF2IF2_Pointer":
    """itkSpeckleNoiseImageFilterIF2IF2___New_orig__() -> itkSpeckleNoiseImageFilterIF2IF2_Pointer"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2___New_orig__()

def itkSpeckleNoiseImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIF2IF2 *":
    """itkSpeckleNoiseImageFilterIF2IF2_cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIF2IF2"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_cast(obj)

class itkSpeckleNoiseImageFilterIF3IF3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF3IF3):
    """Proxy of C++ itkSpeckleNoiseImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpeckleNoiseImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSpeckleNoiseImageFilterIF3IF3_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpeckleNoiseImageFilterIF3IF3_Pointer":
        """Clone(itkSpeckleNoiseImageFilterIF3IF3 self) -> itkSpeckleNoiseImageFilterIF3IF3_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_Clone(self)


    def GetStandardDeviation(self) -> "double":
        """GetStandardDeviation(itkSpeckleNoiseImageFilterIF3IF3 self) -> double"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_GetStandardDeviation(self)


    def SetStandardDeviation(self, _arg: 'double const') -> "void":
        """SetStandardDeviation(itkSpeckleNoiseImageFilterIF3IF3 self, double const _arg)"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_SetStandardDeviation(self, _arg)

    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIF3IF3"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpeckleNoiseImageFilterIF3IF3 *":
        """GetPointer(itkSpeckleNoiseImageFilterIF3IF3 self) -> itkSpeckleNoiseImageFilterIF3IF3"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIF3IF3

        Create a new object of the class itkSpeckleNoiseImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpeckleNoiseImageFilterIF3IF3.Clone = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_Clone, None, itkSpeckleNoiseImageFilterIF3IF3)
itkSpeckleNoiseImageFilterIF3IF3.GetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_GetStandardDeviation, None, itkSpeckleNoiseImageFilterIF3IF3)
itkSpeckleNoiseImageFilterIF3IF3.SetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_SetStandardDeviation, None, itkSpeckleNoiseImageFilterIF3IF3)
itkSpeckleNoiseImageFilterIF3IF3.GetPointer = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_GetPointer, None, itkSpeckleNoiseImageFilterIF3IF3)
itkSpeckleNoiseImageFilterIF3IF3_swigregister = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_swigregister
itkSpeckleNoiseImageFilterIF3IF3_swigregister(itkSpeckleNoiseImageFilterIF3IF3)

def itkSpeckleNoiseImageFilterIF3IF3___New_orig__() -> "itkSpeckleNoiseImageFilterIF3IF3_Pointer":
    """itkSpeckleNoiseImageFilterIF3IF3___New_orig__() -> itkSpeckleNoiseImageFilterIF3IF3_Pointer"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3___New_orig__()

def itkSpeckleNoiseImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIF3IF3 *":
    """itkSpeckleNoiseImageFilterIF3IF3_cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIF3IF3"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_cast(obj)

class itkSpeckleNoiseImageFilterISS2ISS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS2ISS2):
    """Proxy of C++ itkSpeckleNoiseImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpeckleNoiseImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkSpeckleNoiseImageFilterISS2ISS2_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpeckleNoiseImageFilterISS2ISS2_Pointer":
        """Clone(itkSpeckleNoiseImageFilterISS2ISS2 self) -> itkSpeckleNoiseImageFilterISS2ISS2_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_Clone(self)


    def GetStandardDeviation(self) -> "double":
        """GetStandardDeviation(itkSpeckleNoiseImageFilterISS2ISS2 self) -> double"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_GetStandardDeviation(self)


    def SetStandardDeviation(self, _arg: 'double const') -> "void":
        """SetStandardDeviation(itkSpeckleNoiseImageFilterISS2ISS2 self, double const _arg)"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_SetStandardDeviation(self, _arg)

    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterISS2ISS2"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpeckleNoiseImageFilterISS2ISS2 *":
        """GetPointer(itkSpeckleNoiseImageFilterISS2ISS2 self) -> itkSpeckleNoiseImageFilterISS2ISS2"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterISS2ISS2

        Create a new object of the class itkSpeckleNoiseImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpeckleNoiseImageFilterISS2ISS2.Clone = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_Clone, None, itkSpeckleNoiseImageFilterISS2ISS2)
itkSpeckleNoiseImageFilterISS2ISS2.GetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_GetStandardDeviation, None, itkSpeckleNoiseImageFilterISS2ISS2)
itkSpeckleNoiseImageFilterISS2ISS2.SetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_SetStandardDeviation, None, itkSpeckleNoiseImageFilterISS2ISS2)
itkSpeckleNoiseImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_GetPointer, None, itkSpeckleNoiseImageFilterISS2ISS2)
itkSpeckleNoiseImageFilterISS2ISS2_swigregister = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_swigregister
itkSpeckleNoiseImageFilterISS2ISS2_swigregister(itkSpeckleNoiseImageFilterISS2ISS2)

def itkSpeckleNoiseImageFilterISS2ISS2___New_orig__() -> "itkSpeckleNoiseImageFilterISS2ISS2_Pointer":
    """itkSpeckleNoiseImageFilterISS2ISS2___New_orig__() -> itkSpeckleNoiseImageFilterISS2ISS2_Pointer"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2___New_orig__()

def itkSpeckleNoiseImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterISS2ISS2 *":
    """itkSpeckleNoiseImageFilterISS2ISS2_cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterISS2ISS2"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_cast(obj)

class itkSpeckleNoiseImageFilterISS3ISS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS3ISS3):
    """Proxy of C++ itkSpeckleNoiseImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpeckleNoiseImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkSpeckleNoiseImageFilterISS3ISS3_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpeckleNoiseImageFilterISS3ISS3_Pointer":
        """Clone(itkSpeckleNoiseImageFilterISS3ISS3 self) -> itkSpeckleNoiseImageFilterISS3ISS3_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_Clone(self)


    def GetStandardDeviation(self) -> "double":
        """GetStandardDeviation(itkSpeckleNoiseImageFilterISS3ISS3 self) -> double"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_GetStandardDeviation(self)


    def SetStandardDeviation(self, _arg: 'double const') -> "void":
        """SetStandardDeviation(itkSpeckleNoiseImageFilterISS3ISS3 self, double const _arg)"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_SetStandardDeviation(self, _arg)

    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterISS3ISS3"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpeckleNoiseImageFilterISS3ISS3 *":
        """GetPointer(itkSpeckleNoiseImageFilterISS3ISS3 self) -> itkSpeckleNoiseImageFilterISS3ISS3"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterISS3ISS3

        Create a new object of the class itkSpeckleNoiseImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpeckleNoiseImageFilterISS3ISS3.Clone = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_Clone, None, itkSpeckleNoiseImageFilterISS3ISS3)
itkSpeckleNoiseImageFilterISS3ISS3.GetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_GetStandardDeviation, None, itkSpeckleNoiseImageFilterISS3ISS3)
itkSpeckleNoiseImageFilterISS3ISS3.SetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_SetStandardDeviation, None, itkSpeckleNoiseImageFilterISS3ISS3)
itkSpeckleNoiseImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_GetPointer, None, itkSpeckleNoiseImageFilterISS3ISS3)
itkSpeckleNoiseImageFilterISS3ISS3_swigregister = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_swigregister
itkSpeckleNoiseImageFilterISS3ISS3_swigregister(itkSpeckleNoiseImageFilterISS3ISS3)

def itkSpeckleNoiseImageFilterISS3ISS3___New_orig__() -> "itkSpeckleNoiseImageFilterISS3ISS3_Pointer":
    """itkSpeckleNoiseImageFilterISS3ISS3___New_orig__() -> itkSpeckleNoiseImageFilterISS3ISS3_Pointer"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3___New_orig__()

def itkSpeckleNoiseImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterISS3ISS3 *":
    """itkSpeckleNoiseImageFilterISS3ISS3_cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterISS3ISS3"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_cast(obj)

class itkSpeckleNoiseImageFilterIUC2IUC2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC2IUC2):
    """Proxy of C++ itkSpeckleNoiseImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpeckleNoiseImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkSpeckleNoiseImageFilterIUC2IUC2_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpeckleNoiseImageFilterIUC2IUC2_Pointer":
        """Clone(itkSpeckleNoiseImageFilterIUC2IUC2 self) -> itkSpeckleNoiseImageFilterIUC2IUC2_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_Clone(self)


    def GetStandardDeviation(self) -> "double":
        """GetStandardDeviation(itkSpeckleNoiseImageFilterIUC2IUC2 self) -> double"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_GetStandardDeviation(self)


    def SetStandardDeviation(self, _arg: 'double const') -> "void":
        """SetStandardDeviation(itkSpeckleNoiseImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_SetStandardDeviation(self, _arg)

    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIUC2IUC2"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpeckleNoiseImageFilterIUC2IUC2 *":
        """GetPointer(itkSpeckleNoiseImageFilterIUC2IUC2 self) -> itkSpeckleNoiseImageFilterIUC2IUC2"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIUC2IUC2

        Create a new object of the class itkSpeckleNoiseImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpeckleNoiseImageFilterIUC2IUC2.Clone = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_Clone, None, itkSpeckleNoiseImageFilterIUC2IUC2)
itkSpeckleNoiseImageFilterIUC2IUC2.GetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_GetStandardDeviation, None, itkSpeckleNoiseImageFilterIUC2IUC2)
itkSpeckleNoiseImageFilterIUC2IUC2.SetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_SetStandardDeviation, None, itkSpeckleNoiseImageFilterIUC2IUC2)
itkSpeckleNoiseImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_GetPointer, None, itkSpeckleNoiseImageFilterIUC2IUC2)
itkSpeckleNoiseImageFilterIUC2IUC2_swigregister = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_swigregister
itkSpeckleNoiseImageFilterIUC2IUC2_swigregister(itkSpeckleNoiseImageFilterIUC2IUC2)

def itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__() -> "itkSpeckleNoiseImageFilterIUC2IUC2_Pointer":
    """itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__() -> itkSpeckleNoiseImageFilterIUC2IUC2_Pointer"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__()

def itkSpeckleNoiseImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIUC2IUC2 *":
    """itkSpeckleNoiseImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIUC2IUC2"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_cast(obj)

class itkSpeckleNoiseImageFilterIUC3IUC3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC3IUC3):
    """Proxy of C++ itkSpeckleNoiseImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpeckleNoiseImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkSpeckleNoiseImageFilterIUC3IUC3_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpeckleNoiseImageFilterIUC3IUC3_Pointer":
        """Clone(itkSpeckleNoiseImageFilterIUC3IUC3 self) -> itkSpeckleNoiseImageFilterIUC3IUC3_Pointer"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_Clone(self)


    def GetStandardDeviation(self) -> "double":
        """GetStandardDeviation(itkSpeckleNoiseImageFilterIUC3IUC3 self) -> double"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_GetStandardDeviation(self)


    def SetStandardDeviation(self, _arg: 'double const') -> "void":
        """SetStandardDeviation(itkSpeckleNoiseImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_SetStandardDeviation(self, _arg)

    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIUC3IUC3"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpeckleNoiseImageFilterIUC3IUC3 *":
        """GetPointer(itkSpeckleNoiseImageFilterIUC3IUC3 self) -> itkSpeckleNoiseImageFilterIUC3IUC3"""
        return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIUC3IUC3

        Create a new object of the class itkSpeckleNoiseImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpeckleNoiseImageFilterIUC3IUC3.Clone = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_Clone, None, itkSpeckleNoiseImageFilterIUC3IUC3)
itkSpeckleNoiseImageFilterIUC3IUC3.GetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_GetStandardDeviation, None, itkSpeckleNoiseImageFilterIUC3IUC3)
itkSpeckleNoiseImageFilterIUC3IUC3.SetStandardDeviation = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_SetStandardDeviation, None, itkSpeckleNoiseImageFilterIUC3IUC3)
itkSpeckleNoiseImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_GetPointer, None, itkSpeckleNoiseImageFilterIUC3IUC3)
itkSpeckleNoiseImageFilterIUC3IUC3_swigregister = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_swigregister
itkSpeckleNoiseImageFilterIUC3IUC3_swigregister(itkSpeckleNoiseImageFilterIUC3IUC3)

def itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__() -> "itkSpeckleNoiseImageFilterIUC3IUC3_Pointer":
    """itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__() -> itkSpeckleNoiseImageFilterIUC3IUC3_Pointer"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__()

def itkSpeckleNoiseImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkSpeckleNoiseImageFilterIUC3IUC3 *":
    """itkSpeckleNoiseImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkSpeckleNoiseImageFilterIUC3IUC3"""
    return _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_cast(obj)



