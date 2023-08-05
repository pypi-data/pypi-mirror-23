# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShotNoiseImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkShotNoiseImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkShotNoiseImageFilterPython')
    _itkShotNoiseImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShotNoiseImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShotNoiseImageFilterPython
            return _itkShotNoiseImageFilterPython
        try:
            _mod = imp.load_module('_itkShotNoiseImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkShotNoiseImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShotNoiseImageFilterPython
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
import ITKCommonBasePython
import pyBasePython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkShotNoiseImageFilterIF3IF3_New():
  return itkShotNoiseImageFilterIF3IF3.New()


def itkShotNoiseImageFilterIF2IF2_New():
  return itkShotNoiseImageFilterIF2IF2.New()


def itkShotNoiseImageFilterIUC3IUC3_New():
  return itkShotNoiseImageFilterIUC3IUC3.New()


def itkShotNoiseImageFilterIUC2IUC2_New():
  return itkShotNoiseImageFilterIUC2IUC2.New()


def itkShotNoiseImageFilterISS3ISS3_New():
  return itkShotNoiseImageFilterISS3ISS3.New()


def itkShotNoiseImageFilterISS2ISS2_New():
  return itkShotNoiseImageFilterISS2ISS2.New()

class itkShotNoiseImageFilterIF2IF2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF2IF2):
    """Proxy of C++ itkShotNoiseImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShotNoiseImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkShotNoiseImageFilterIF2IF2_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShotNoiseImageFilterIF2IF2_Pointer":
        """Clone(itkShotNoiseImageFilterIF2IF2 self) -> itkShotNoiseImageFilterIF2IF2_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_Clone(self)


    def GetScale(self) -> "double":
        """GetScale(itkShotNoiseImageFilterIF2IF2 self) -> double"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_GetScale(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShotNoiseImageFilterIF2IF2 self, double const _arg)"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_SetScale(self, _arg)

    InputConvertibleToOutputCheck = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkShotNoiseImageFilterPython.delete_itkShotNoiseImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkShotNoiseImageFilterIF2IF2"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShotNoiseImageFilterIF2IF2 *":
        """GetPointer(itkShotNoiseImageFilterIF2IF2 self) -> itkShotNoiseImageFilterIF2IF2"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShotNoiseImageFilterIF2IF2

        Create a new object of the class itkShotNoiseImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShotNoiseImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShotNoiseImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShotNoiseImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShotNoiseImageFilterIF2IF2.Clone = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_Clone, None, itkShotNoiseImageFilterIF2IF2)
itkShotNoiseImageFilterIF2IF2.GetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_GetScale, None, itkShotNoiseImageFilterIF2IF2)
itkShotNoiseImageFilterIF2IF2.SetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_SetScale, None, itkShotNoiseImageFilterIF2IF2)
itkShotNoiseImageFilterIF2IF2.GetPointer = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_GetPointer, None, itkShotNoiseImageFilterIF2IF2)
itkShotNoiseImageFilterIF2IF2_swigregister = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_swigregister
itkShotNoiseImageFilterIF2IF2_swigregister(itkShotNoiseImageFilterIF2IF2)

def itkShotNoiseImageFilterIF2IF2___New_orig__() -> "itkShotNoiseImageFilterIF2IF2_Pointer":
    """itkShotNoiseImageFilterIF2IF2___New_orig__() -> itkShotNoiseImageFilterIF2IF2_Pointer"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2___New_orig__()

def itkShotNoiseImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIF2IF2 *":
    """itkShotNoiseImageFilterIF2IF2_cast(itkLightObject obj) -> itkShotNoiseImageFilterIF2IF2"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF2IF2_cast(obj)

class itkShotNoiseImageFilterIF3IF3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF3IF3):
    """Proxy of C++ itkShotNoiseImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShotNoiseImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkShotNoiseImageFilterIF3IF3_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShotNoiseImageFilterIF3IF3_Pointer":
        """Clone(itkShotNoiseImageFilterIF3IF3 self) -> itkShotNoiseImageFilterIF3IF3_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_Clone(self)


    def GetScale(self) -> "double":
        """GetScale(itkShotNoiseImageFilterIF3IF3 self) -> double"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_GetScale(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShotNoiseImageFilterIF3IF3 self, double const _arg)"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_SetScale(self, _arg)

    InputConvertibleToOutputCheck = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkShotNoiseImageFilterPython.delete_itkShotNoiseImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkShotNoiseImageFilterIF3IF3"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShotNoiseImageFilterIF3IF3 *":
        """GetPointer(itkShotNoiseImageFilterIF3IF3 self) -> itkShotNoiseImageFilterIF3IF3"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShotNoiseImageFilterIF3IF3

        Create a new object of the class itkShotNoiseImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShotNoiseImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShotNoiseImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShotNoiseImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShotNoiseImageFilterIF3IF3.Clone = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_Clone, None, itkShotNoiseImageFilterIF3IF3)
itkShotNoiseImageFilterIF3IF3.GetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_GetScale, None, itkShotNoiseImageFilterIF3IF3)
itkShotNoiseImageFilterIF3IF3.SetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_SetScale, None, itkShotNoiseImageFilterIF3IF3)
itkShotNoiseImageFilterIF3IF3.GetPointer = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_GetPointer, None, itkShotNoiseImageFilterIF3IF3)
itkShotNoiseImageFilterIF3IF3_swigregister = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_swigregister
itkShotNoiseImageFilterIF3IF3_swigregister(itkShotNoiseImageFilterIF3IF3)

def itkShotNoiseImageFilterIF3IF3___New_orig__() -> "itkShotNoiseImageFilterIF3IF3_Pointer":
    """itkShotNoiseImageFilterIF3IF3___New_orig__() -> itkShotNoiseImageFilterIF3IF3_Pointer"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3___New_orig__()

def itkShotNoiseImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIF3IF3 *":
    """itkShotNoiseImageFilterIF3IF3_cast(itkLightObject obj) -> itkShotNoiseImageFilterIF3IF3"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIF3IF3_cast(obj)

class itkShotNoiseImageFilterISS2ISS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS2ISS2):
    """Proxy of C++ itkShotNoiseImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShotNoiseImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkShotNoiseImageFilterISS2ISS2_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShotNoiseImageFilterISS2ISS2_Pointer":
        """Clone(itkShotNoiseImageFilterISS2ISS2 self) -> itkShotNoiseImageFilterISS2ISS2_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_Clone(self)


    def GetScale(self) -> "double":
        """GetScale(itkShotNoiseImageFilterISS2ISS2 self) -> double"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_GetScale(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShotNoiseImageFilterISS2ISS2 self, double const _arg)"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_SetScale(self, _arg)

    InputConvertibleToOutputCheck = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkShotNoiseImageFilterPython.delete_itkShotNoiseImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkShotNoiseImageFilterISS2ISS2"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShotNoiseImageFilterISS2ISS2 *":
        """GetPointer(itkShotNoiseImageFilterISS2ISS2 self) -> itkShotNoiseImageFilterISS2ISS2"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShotNoiseImageFilterISS2ISS2

        Create a new object of the class itkShotNoiseImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShotNoiseImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShotNoiseImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShotNoiseImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShotNoiseImageFilterISS2ISS2.Clone = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_Clone, None, itkShotNoiseImageFilterISS2ISS2)
itkShotNoiseImageFilterISS2ISS2.GetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_GetScale, None, itkShotNoiseImageFilterISS2ISS2)
itkShotNoiseImageFilterISS2ISS2.SetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_SetScale, None, itkShotNoiseImageFilterISS2ISS2)
itkShotNoiseImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_GetPointer, None, itkShotNoiseImageFilterISS2ISS2)
itkShotNoiseImageFilterISS2ISS2_swigregister = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_swigregister
itkShotNoiseImageFilterISS2ISS2_swigregister(itkShotNoiseImageFilterISS2ISS2)

def itkShotNoiseImageFilterISS2ISS2___New_orig__() -> "itkShotNoiseImageFilterISS2ISS2_Pointer":
    """itkShotNoiseImageFilterISS2ISS2___New_orig__() -> itkShotNoiseImageFilterISS2ISS2_Pointer"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2___New_orig__()

def itkShotNoiseImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterISS2ISS2 *":
    """itkShotNoiseImageFilterISS2ISS2_cast(itkLightObject obj) -> itkShotNoiseImageFilterISS2ISS2"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS2ISS2_cast(obj)

class itkShotNoiseImageFilterISS3ISS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS3ISS3):
    """Proxy of C++ itkShotNoiseImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShotNoiseImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkShotNoiseImageFilterISS3ISS3_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShotNoiseImageFilterISS3ISS3_Pointer":
        """Clone(itkShotNoiseImageFilterISS3ISS3 self) -> itkShotNoiseImageFilterISS3ISS3_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_Clone(self)


    def GetScale(self) -> "double":
        """GetScale(itkShotNoiseImageFilterISS3ISS3 self) -> double"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_GetScale(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShotNoiseImageFilterISS3ISS3 self, double const _arg)"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_SetScale(self, _arg)

    InputConvertibleToOutputCheck = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkShotNoiseImageFilterPython.delete_itkShotNoiseImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkShotNoiseImageFilterISS3ISS3"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShotNoiseImageFilterISS3ISS3 *":
        """GetPointer(itkShotNoiseImageFilterISS3ISS3 self) -> itkShotNoiseImageFilterISS3ISS3"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShotNoiseImageFilterISS3ISS3

        Create a new object of the class itkShotNoiseImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShotNoiseImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShotNoiseImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShotNoiseImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShotNoiseImageFilterISS3ISS3.Clone = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_Clone, None, itkShotNoiseImageFilterISS3ISS3)
itkShotNoiseImageFilterISS3ISS3.GetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_GetScale, None, itkShotNoiseImageFilterISS3ISS3)
itkShotNoiseImageFilterISS3ISS3.SetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_SetScale, None, itkShotNoiseImageFilterISS3ISS3)
itkShotNoiseImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_GetPointer, None, itkShotNoiseImageFilterISS3ISS3)
itkShotNoiseImageFilterISS3ISS3_swigregister = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_swigregister
itkShotNoiseImageFilterISS3ISS3_swigregister(itkShotNoiseImageFilterISS3ISS3)

def itkShotNoiseImageFilterISS3ISS3___New_orig__() -> "itkShotNoiseImageFilterISS3ISS3_Pointer":
    """itkShotNoiseImageFilterISS3ISS3___New_orig__() -> itkShotNoiseImageFilterISS3ISS3_Pointer"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3___New_orig__()

def itkShotNoiseImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterISS3ISS3 *":
    """itkShotNoiseImageFilterISS3ISS3_cast(itkLightObject obj) -> itkShotNoiseImageFilterISS3ISS3"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterISS3ISS3_cast(obj)

class itkShotNoiseImageFilterIUC2IUC2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC2IUC2):
    """Proxy of C++ itkShotNoiseImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShotNoiseImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkShotNoiseImageFilterIUC2IUC2_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShotNoiseImageFilterIUC2IUC2_Pointer":
        """Clone(itkShotNoiseImageFilterIUC2IUC2 self) -> itkShotNoiseImageFilterIUC2IUC2_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_Clone(self)


    def GetScale(self) -> "double":
        """GetScale(itkShotNoiseImageFilterIUC2IUC2 self) -> double"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_GetScale(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShotNoiseImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_SetScale(self, _arg)

    InputConvertibleToOutputCheck = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkShotNoiseImageFilterPython.delete_itkShotNoiseImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkShotNoiseImageFilterIUC2IUC2"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShotNoiseImageFilterIUC2IUC2 *":
        """GetPointer(itkShotNoiseImageFilterIUC2IUC2 self) -> itkShotNoiseImageFilterIUC2IUC2"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShotNoiseImageFilterIUC2IUC2

        Create a new object of the class itkShotNoiseImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShotNoiseImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShotNoiseImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShotNoiseImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShotNoiseImageFilterIUC2IUC2.Clone = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_Clone, None, itkShotNoiseImageFilterIUC2IUC2)
itkShotNoiseImageFilterIUC2IUC2.GetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_GetScale, None, itkShotNoiseImageFilterIUC2IUC2)
itkShotNoiseImageFilterIUC2IUC2.SetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_SetScale, None, itkShotNoiseImageFilterIUC2IUC2)
itkShotNoiseImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_GetPointer, None, itkShotNoiseImageFilterIUC2IUC2)
itkShotNoiseImageFilterIUC2IUC2_swigregister = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_swigregister
itkShotNoiseImageFilterIUC2IUC2_swigregister(itkShotNoiseImageFilterIUC2IUC2)

def itkShotNoiseImageFilterIUC2IUC2___New_orig__() -> "itkShotNoiseImageFilterIUC2IUC2_Pointer":
    """itkShotNoiseImageFilterIUC2IUC2___New_orig__() -> itkShotNoiseImageFilterIUC2IUC2_Pointer"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2___New_orig__()

def itkShotNoiseImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIUC2IUC2 *":
    """itkShotNoiseImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkShotNoiseImageFilterIUC2IUC2"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC2IUC2_cast(obj)

class itkShotNoiseImageFilterIUC3IUC3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC3IUC3):
    """Proxy of C++ itkShotNoiseImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShotNoiseImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkShotNoiseImageFilterIUC3IUC3_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShotNoiseImageFilterIUC3IUC3_Pointer":
        """Clone(itkShotNoiseImageFilterIUC3IUC3 self) -> itkShotNoiseImageFilterIUC3IUC3_Pointer"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_Clone(self)


    def GetScale(self) -> "double":
        """GetScale(itkShotNoiseImageFilterIUC3IUC3 self) -> double"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_GetScale(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShotNoiseImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_SetScale(self, _arg)

    InputConvertibleToOutputCheck = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkShotNoiseImageFilterPython.delete_itkShotNoiseImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkShotNoiseImageFilterIUC3IUC3"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShotNoiseImageFilterIUC3IUC3 *":
        """GetPointer(itkShotNoiseImageFilterIUC3IUC3 self) -> itkShotNoiseImageFilterIUC3IUC3"""
        return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShotNoiseImageFilterIUC3IUC3

        Create a new object of the class itkShotNoiseImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShotNoiseImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShotNoiseImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShotNoiseImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShotNoiseImageFilterIUC3IUC3.Clone = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_Clone, None, itkShotNoiseImageFilterIUC3IUC3)
itkShotNoiseImageFilterIUC3IUC3.GetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_GetScale, None, itkShotNoiseImageFilterIUC3IUC3)
itkShotNoiseImageFilterIUC3IUC3.SetScale = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_SetScale, None, itkShotNoiseImageFilterIUC3IUC3)
itkShotNoiseImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_GetPointer, None, itkShotNoiseImageFilterIUC3IUC3)
itkShotNoiseImageFilterIUC3IUC3_swigregister = _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_swigregister
itkShotNoiseImageFilterIUC3IUC3_swigregister(itkShotNoiseImageFilterIUC3IUC3)

def itkShotNoiseImageFilterIUC3IUC3___New_orig__() -> "itkShotNoiseImageFilterIUC3IUC3_Pointer":
    """itkShotNoiseImageFilterIUC3IUC3___New_orig__() -> itkShotNoiseImageFilterIUC3IUC3_Pointer"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3___New_orig__()

def itkShotNoiseImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkShotNoiseImageFilterIUC3IUC3 *":
    """itkShotNoiseImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkShotNoiseImageFilterIUC3IUC3"""
    return _itkShotNoiseImageFilterPython.itkShotNoiseImageFilterIUC3IUC3_cast(obj)



