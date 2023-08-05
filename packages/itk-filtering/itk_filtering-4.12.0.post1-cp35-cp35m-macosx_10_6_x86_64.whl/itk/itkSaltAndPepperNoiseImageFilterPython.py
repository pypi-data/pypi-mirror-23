# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSaltAndPepperNoiseImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSaltAndPepperNoiseImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSaltAndPepperNoiseImageFilterPython')
    _itkSaltAndPepperNoiseImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSaltAndPepperNoiseImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSaltAndPepperNoiseImageFilterPython
            return _itkSaltAndPepperNoiseImageFilterPython
        try:
            _mod = imp.load_module('_itkSaltAndPepperNoiseImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSaltAndPepperNoiseImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSaltAndPepperNoiseImageFilterPython
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
import itkNoiseBaseImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkSaltAndPepperNoiseImageFilterIF3IF3_New():
  return itkSaltAndPepperNoiseImageFilterIF3IF3.New()


def itkSaltAndPepperNoiseImageFilterIF2IF2_New():
  return itkSaltAndPepperNoiseImageFilterIF2IF2.New()


def itkSaltAndPepperNoiseImageFilterIUC3IUC3_New():
  return itkSaltAndPepperNoiseImageFilterIUC3IUC3.New()


def itkSaltAndPepperNoiseImageFilterIUC2IUC2_New():
  return itkSaltAndPepperNoiseImageFilterIUC2IUC2.New()


def itkSaltAndPepperNoiseImageFilterISS3ISS3_New():
  return itkSaltAndPepperNoiseImageFilterISS3ISS3.New()


def itkSaltAndPepperNoiseImageFilterISS2ISS2_New():
  return itkSaltAndPepperNoiseImageFilterISS2ISS2.New()

class itkSaltAndPepperNoiseImageFilterIF2IF2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF2IF2):
    """Proxy of C++ itkSaltAndPepperNoiseImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSaltAndPepperNoiseImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSaltAndPepperNoiseImageFilterIF2IF2_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSaltAndPepperNoiseImageFilterIF2IF2_Pointer":
        """Clone(itkSaltAndPepperNoiseImageFilterIF2IF2 self) -> itkSaltAndPepperNoiseImageFilterIF2IF2_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_Clone(self)


    def GetProbability(self) -> "double":
        """GetProbability(itkSaltAndPepperNoiseImageFilterIF2IF2 self) -> double"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_GetProbability(self)


    def SetProbability(self, _arg: 'double const') -> "void":
        """SetProbability(itkSaltAndPepperNoiseImageFilterIF2IF2 self, double const _arg)"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_SetProbability(self, _arg)

    InputConvertibleToOutputCheck = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSaltAndPepperNoiseImageFilterPython.delete_itkSaltAndPepperNoiseImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIF2IF2"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSaltAndPepperNoiseImageFilterIF2IF2 *":
        """GetPointer(itkSaltAndPepperNoiseImageFilterIF2IF2 self) -> itkSaltAndPepperNoiseImageFilterIF2IF2"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSaltAndPepperNoiseImageFilterIF2IF2

        Create a new object of the class itkSaltAndPepperNoiseImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSaltAndPepperNoiseImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSaltAndPepperNoiseImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSaltAndPepperNoiseImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSaltAndPepperNoiseImageFilterIF2IF2.Clone = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_Clone, None, itkSaltAndPepperNoiseImageFilterIF2IF2)
itkSaltAndPepperNoiseImageFilterIF2IF2.GetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_GetProbability, None, itkSaltAndPepperNoiseImageFilterIF2IF2)
itkSaltAndPepperNoiseImageFilterIF2IF2.SetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_SetProbability, None, itkSaltAndPepperNoiseImageFilterIF2IF2)
itkSaltAndPepperNoiseImageFilterIF2IF2.GetPointer = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_GetPointer, None, itkSaltAndPepperNoiseImageFilterIF2IF2)
itkSaltAndPepperNoiseImageFilterIF2IF2_swigregister = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_swigregister
itkSaltAndPepperNoiseImageFilterIF2IF2_swigregister(itkSaltAndPepperNoiseImageFilterIF2IF2)

def itkSaltAndPepperNoiseImageFilterIF2IF2___New_orig__() -> "itkSaltAndPepperNoiseImageFilterIF2IF2_Pointer":
    """itkSaltAndPepperNoiseImageFilterIF2IF2___New_orig__() -> itkSaltAndPepperNoiseImageFilterIF2IF2_Pointer"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2___New_orig__()

def itkSaltAndPepperNoiseImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIF2IF2 *":
    """itkSaltAndPepperNoiseImageFilterIF2IF2_cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIF2IF2"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF2IF2_cast(obj)

class itkSaltAndPepperNoiseImageFilterIF3IF3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF3IF3):
    """Proxy of C++ itkSaltAndPepperNoiseImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSaltAndPepperNoiseImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSaltAndPepperNoiseImageFilterIF3IF3_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSaltAndPepperNoiseImageFilterIF3IF3_Pointer":
        """Clone(itkSaltAndPepperNoiseImageFilterIF3IF3 self) -> itkSaltAndPepperNoiseImageFilterIF3IF3_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_Clone(self)


    def GetProbability(self) -> "double":
        """GetProbability(itkSaltAndPepperNoiseImageFilterIF3IF3 self) -> double"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_GetProbability(self)


    def SetProbability(self, _arg: 'double const') -> "void":
        """SetProbability(itkSaltAndPepperNoiseImageFilterIF3IF3 self, double const _arg)"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_SetProbability(self, _arg)

    InputConvertibleToOutputCheck = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSaltAndPepperNoiseImageFilterPython.delete_itkSaltAndPepperNoiseImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIF3IF3"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSaltAndPepperNoiseImageFilterIF3IF3 *":
        """GetPointer(itkSaltAndPepperNoiseImageFilterIF3IF3 self) -> itkSaltAndPepperNoiseImageFilterIF3IF3"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSaltAndPepperNoiseImageFilterIF3IF3

        Create a new object of the class itkSaltAndPepperNoiseImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSaltAndPepperNoiseImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSaltAndPepperNoiseImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSaltAndPepperNoiseImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSaltAndPepperNoiseImageFilterIF3IF3.Clone = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_Clone, None, itkSaltAndPepperNoiseImageFilterIF3IF3)
itkSaltAndPepperNoiseImageFilterIF3IF3.GetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_GetProbability, None, itkSaltAndPepperNoiseImageFilterIF3IF3)
itkSaltAndPepperNoiseImageFilterIF3IF3.SetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_SetProbability, None, itkSaltAndPepperNoiseImageFilterIF3IF3)
itkSaltAndPepperNoiseImageFilterIF3IF3.GetPointer = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_GetPointer, None, itkSaltAndPepperNoiseImageFilterIF3IF3)
itkSaltAndPepperNoiseImageFilterIF3IF3_swigregister = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_swigregister
itkSaltAndPepperNoiseImageFilterIF3IF3_swigregister(itkSaltAndPepperNoiseImageFilterIF3IF3)

def itkSaltAndPepperNoiseImageFilterIF3IF3___New_orig__() -> "itkSaltAndPepperNoiseImageFilterIF3IF3_Pointer":
    """itkSaltAndPepperNoiseImageFilterIF3IF3___New_orig__() -> itkSaltAndPepperNoiseImageFilterIF3IF3_Pointer"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3___New_orig__()

def itkSaltAndPepperNoiseImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIF3IF3 *":
    """itkSaltAndPepperNoiseImageFilterIF3IF3_cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIF3IF3"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIF3IF3_cast(obj)

class itkSaltAndPepperNoiseImageFilterISS2ISS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS2ISS2):
    """Proxy of C++ itkSaltAndPepperNoiseImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSaltAndPepperNoiseImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkSaltAndPepperNoiseImageFilterISS2ISS2_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSaltAndPepperNoiseImageFilterISS2ISS2_Pointer":
        """Clone(itkSaltAndPepperNoiseImageFilterISS2ISS2 self) -> itkSaltAndPepperNoiseImageFilterISS2ISS2_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_Clone(self)


    def GetProbability(self) -> "double":
        """GetProbability(itkSaltAndPepperNoiseImageFilterISS2ISS2 self) -> double"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_GetProbability(self)


    def SetProbability(self, _arg: 'double const') -> "void":
        """SetProbability(itkSaltAndPepperNoiseImageFilterISS2ISS2 self, double const _arg)"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_SetProbability(self, _arg)

    InputConvertibleToOutputCheck = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSaltAndPepperNoiseImageFilterPython.delete_itkSaltAndPepperNoiseImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterISS2ISS2"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSaltAndPepperNoiseImageFilterISS2ISS2 *":
        """GetPointer(itkSaltAndPepperNoiseImageFilterISS2ISS2 self) -> itkSaltAndPepperNoiseImageFilterISS2ISS2"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSaltAndPepperNoiseImageFilterISS2ISS2

        Create a new object of the class itkSaltAndPepperNoiseImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSaltAndPepperNoiseImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSaltAndPepperNoiseImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSaltAndPepperNoiseImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSaltAndPepperNoiseImageFilterISS2ISS2.Clone = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_Clone, None, itkSaltAndPepperNoiseImageFilterISS2ISS2)
itkSaltAndPepperNoiseImageFilterISS2ISS2.GetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_GetProbability, None, itkSaltAndPepperNoiseImageFilterISS2ISS2)
itkSaltAndPepperNoiseImageFilterISS2ISS2.SetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_SetProbability, None, itkSaltAndPepperNoiseImageFilterISS2ISS2)
itkSaltAndPepperNoiseImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_GetPointer, None, itkSaltAndPepperNoiseImageFilterISS2ISS2)
itkSaltAndPepperNoiseImageFilterISS2ISS2_swigregister = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_swigregister
itkSaltAndPepperNoiseImageFilterISS2ISS2_swigregister(itkSaltAndPepperNoiseImageFilterISS2ISS2)

def itkSaltAndPepperNoiseImageFilterISS2ISS2___New_orig__() -> "itkSaltAndPepperNoiseImageFilterISS2ISS2_Pointer":
    """itkSaltAndPepperNoiseImageFilterISS2ISS2___New_orig__() -> itkSaltAndPepperNoiseImageFilterISS2ISS2_Pointer"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2___New_orig__()

def itkSaltAndPepperNoiseImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterISS2ISS2 *":
    """itkSaltAndPepperNoiseImageFilterISS2ISS2_cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterISS2ISS2"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS2ISS2_cast(obj)

class itkSaltAndPepperNoiseImageFilterISS3ISS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS3ISS3):
    """Proxy of C++ itkSaltAndPepperNoiseImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSaltAndPepperNoiseImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkSaltAndPepperNoiseImageFilterISS3ISS3_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSaltAndPepperNoiseImageFilterISS3ISS3_Pointer":
        """Clone(itkSaltAndPepperNoiseImageFilterISS3ISS3 self) -> itkSaltAndPepperNoiseImageFilterISS3ISS3_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_Clone(self)


    def GetProbability(self) -> "double":
        """GetProbability(itkSaltAndPepperNoiseImageFilterISS3ISS3 self) -> double"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_GetProbability(self)


    def SetProbability(self, _arg: 'double const') -> "void":
        """SetProbability(itkSaltAndPepperNoiseImageFilterISS3ISS3 self, double const _arg)"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_SetProbability(self, _arg)

    InputConvertibleToOutputCheck = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSaltAndPepperNoiseImageFilterPython.delete_itkSaltAndPepperNoiseImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterISS3ISS3"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSaltAndPepperNoiseImageFilterISS3ISS3 *":
        """GetPointer(itkSaltAndPepperNoiseImageFilterISS3ISS3 self) -> itkSaltAndPepperNoiseImageFilterISS3ISS3"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSaltAndPepperNoiseImageFilterISS3ISS3

        Create a new object of the class itkSaltAndPepperNoiseImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSaltAndPepperNoiseImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSaltAndPepperNoiseImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSaltAndPepperNoiseImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSaltAndPepperNoiseImageFilterISS3ISS3.Clone = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_Clone, None, itkSaltAndPepperNoiseImageFilterISS3ISS3)
itkSaltAndPepperNoiseImageFilterISS3ISS3.GetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_GetProbability, None, itkSaltAndPepperNoiseImageFilterISS3ISS3)
itkSaltAndPepperNoiseImageFilterISS3ISS3.SetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_SetProbability, None, itkSaltAndPepperNoiseImageFilterISS3ISS3)
itkSaltAndPepperNoiseImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_GetPointer, None, itkSaltAndPepperNoiseImageFilterISS3ISS3)
itkSaltAndPepperNoiseImageFilterISS3ISS3_swigregister = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_swigregister
itkSaltAndPepperNoiseImageFilterISS3ISS3_swigregister(itkSaltAndPepperNoiseImageFilterISS3ISS3)

def itkSaltAndPepperNoiseImageFilterISS3ISS3___New_orig__() -> "itkSaltAndPepperNoiseImageFilterISS3ISS3_Pointer":
    """itkSaltAndPepperNoiseImageFilterISS3ISS3___New_orig__() -> itkSaltAndPepperNoiseImageFilterISS3ISS3_Pointer"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3___New_orig__()

def itkSaltAndPepperNoiseImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterISS3ISS3 *":
    """itkSaltAndPepperNoiseImageFilterISS3ISS3_cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterISS3ISS3"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterISS3ISS3_cast(obj)

class itkSaltAndPepperNoiseImageFilterIUC2IUC2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC2IUC2):
    """Proxy of C++ itkSaltAndPepperNoiseImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSaltAndPepperNoiseImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkSaltAndPepperNoiseImageFilterIUC2IUC2_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSaltAndPepperNoiseImageFilterIUC2IUC2_Pointer":
        """Clone(itkSaltAndPepperNoiseImageFilterIUC2IUC2 self) -> itkSaltAndPepperNoiseImageFilterIUC2IUC2_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_Clone(self)


    def GetProbability(self) -> "double":
        """GetProbability(itkSaltAndPepperNoiseImageFilterIUC2IUC2 self) -> double"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_GetProbability(self)


    def SetProbability(self, _arg: 'double const') -> "void":
        """SetProbability(itkSaltAndPepperNoiseImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_SetProbability(self, _arg)

    InputConvertibleToOutputCheck = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSaltAndPepperNoiseImageFilterPython.delete_itkSaltAndPepperNoiseImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIUC2IUC2"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSaltAndPepperNoiseImageFilterIUC2IUC2 *":
        """GetPointer(itkSaltAndPepperNoiseImageFilterIUC2IUC2 self) -> itkSaltAndPepperNoiseImageFilterIUC2IUC2"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSaltAndPepperNoiseImageFilterIUC2IUC2

        Create a new object of the class itkSaltAndPepperNoiseImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSaltAndPepperNoiseImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSaltAndPepperNoiseImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSaltAndPepperNoiseImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSaltAndPepperNoiseImageFilterIUC2IUC2.Clone = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_Clone, None, itkSaltAndPepperNoiseImageFilterIUC2IUC2)
itkSaltAndPepperNoiseImageFilterIUC2IUC2.GetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_GetProbability, None, itkSaltAndPepperNoiseImageFilterIUC2IUC2)
itkSaltAndPepperNoiseImageFilterIUC2IUC2.SetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_SetProbability, None, itkSaltAndPepperNoiseImageFilterIUC2IUC2)
itkSaltAndPepperNoiseImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_GetPointer, None, itkSaltAndPepperNoiseImageFilterIUC2IUC2)
itkSaltAndPepperNoiseImageFilterIUC2IUC2_swigregister = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_swigregister
itkSaltAndPepperNoiseImageFilterIUC2IUC2_swigregister(itkSaltAndPepperNoiseImageFilterIUC2IUC2)

def itkSaltAndPepperNoiseImageFilterIUC2IUC2___New_orig__() -> "itkSaltAndPepperNoiseImageFilterIUC2IUC2_Pointer":
    """itkSaltAndPepperNoiseImageFilterIUC2IUC2___New_orig__() -> itkSaltAndPepperNoiseImageFilterIUC2IUC2_Pointer"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2___New_orig__()

def itkSaltAndPepperNoiseImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIUC2IUC2 *":
    """itkSaltAndPepperNoiseImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIUC2IUC2"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC2IUC2_cast(obj)

class itkSaltAndPepperNoiseImageFilterIUC3IUC3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC3IUC3):
    """Proxy of C++ itkSaltAndPepperNoiseImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSaltAndPepperNoiseImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkSaltAndPepperNoiseImageFilterIUC3IUC3_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSaltAndPepperNoiseImageFilterIUC3IUC3_Pointer":
        """Clone(itkSaltAndPepperNoiseImageFilterIUC3IUC3 self) -> itkSaltAndPepperNoiseImageFilterIUC3IUC3_Pointer"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_Clone(self)


    def GetProbability(self) -> "double":
        """GetProbability(itkSaltAndPepperNoiseImageFilterIUC3IUC3 self) -> double"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_GetProbability(self)


    def SetProbability(self, _arg: 'double const') -> "void":
        """SetProbability(itkSaltAndPepperNoiseImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_SetProbability(self, _arg)

    InputConvertibleToOutputCheck = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkSaltAndPepperNoiseImageFilterPython.delete_itkSaltAndPepperNoiseImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIUC3IUC3"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSaltAndPepperNoiseImageFilterIUC3IUC3 *":
        """GetPointer(itkSaltAndPepperNoiseImageFilterIUC3IUC3 self) -> itkSaltAndPepperNoiseImageFilterIUC3IUC3"""
        return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSaltAndPepperNoiseImageFilterIUC3IUC3

        Create a new object of the class itkSaltAndPepperNoiseImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSaltAndPepperNoiseImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSaltAndPepperNoiseImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSaltAndPepperNoiseImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSaltAndPepperNoiseImageFilterIUC3IUC3.Clone = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_Clone, None, itkSaltAndPepperNoiseImageFilterIUC3IUC3)
itkSaltAndPepperNoiseImageFilterIUC3IUC3.GetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_GetProbability, None, itkSaltAndPepperNoiseImageFilterIUC3IUC3)
itkSaltAndPepperNoiseImageFilterIUC3IUC3.SetProbability = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_SetProbability, None, itkSaltAndPepperNoiseImageFilterIUC3IUC3)
itkSaltAndPepperNoiseImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_GetPointer, None, itkSaltAndPepperNoiseImageFilterIUC3IUC3)
itkSaltAndPepperNoiseImageFilterIUC3IUC3_swigregister = _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_swigregister
itkSaltAndPepperNoiseImageFilterIUC3IUC3_swigregister(itkSaltAndPepperNoiseImageFilterIUC3IUC3)

def itkSaltAndPepperNoiseImageFilterIUC3IUC3___New_orig__() -> "itkSaltAndPepperNoiseImageFilterIUC3IUC3_Pointer":
    """itkSaltAndPepperNoiseImageFilterIUC3IUC3___New_orig__() -> itkSaltAndPepperNoiseImageFilterIUC3IUC3_Pointer"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3___New_orig__()

def itkSaltAndPepperNoiseImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkSaltAndPepperNoiseImageFilterIUC3IUC3 *":
    """itkSaltAndPepperNoiseImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkSaltAndPepperNoiseImageFilterIUC3IUC3"""
    return _itkSaltAndPepperNoiseImageFilterPython.itkSaltAndPepperNoiseImageFilterIUC3IUC3_cast(obj)



