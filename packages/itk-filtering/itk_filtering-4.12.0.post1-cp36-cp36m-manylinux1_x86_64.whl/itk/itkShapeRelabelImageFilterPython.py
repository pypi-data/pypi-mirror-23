# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapeRelabelImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkShapeRelabelImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkShapeRelabelImageFilterPython')
    _itkShapeRelabelImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapeRelabelImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShapeRelabelImageFilterPython
            return _itkShapeRelabelImageFilterPython
        try:
            _mod = imp.load_module('_itkShapeRelabelImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkShapeRelabelImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapeRelabelImageFilterPython
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


import itkImageToImageFilterAPython
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

def itkShapeRelabelImageFilterIUC3_New():
  return itkShapeRelabelImageFilterIUC3.New()


def itkShapeRelabelImageFilterIUC2_New():
  return itkShapeRelabelImageFilterIUC2.New()


def itkShapeRelabelImageFilterISS3_New():
  return itkShapeRelabelImageFilterISS3.New()


def itkShapeRelabelImageFilterISS2_New():
  return itkShapeRelabelImageFilterISS2.New()

class itkShapeRelabelImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkShapeRelabelImageFilterISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeRelabelImageFilterISS2_Pointer":
        """__New_orig__() -> itkShapeRelabelImageFilterISS2_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeRelabelImageFilterISS2_Pointer":
        """Clone(itkShapeRelabelImageFilterISS2 self) -> itkShapeRelabelImageFilterISS2_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_Clone(self)

    InputEqualityComparableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_InputOStreamWritableCheck

    def SetBackgroundValue(self, _arg: 'short const') -> "void":
        """SetBackgroundValue(itkShapeRelabelImageFilterISS2 self, short const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "short":
        """GetBackgroundValue(itkShapeRelabelImageFilterISS2 self) -> short"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetBackgroundValue(self)


    def GetReverseOrdering(self) -> "bool":
        """GetReverseOrdering(itkShapeRelabelImageFilterISS2 self) -> bool"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetReverseOrdering(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeRelabelImageFilterISS2 self, bool const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_SetReverseOrdering(self, _arg)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeRelabelImageFilterISS2 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeRelabelImageFilterISS2 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeRelabelImageFilterISS2 self) -> unsigned int"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeRelabelImageFilterISS2 self, unsigned int const _arg)
        SetAttribute(itkShapeRelabelImageFilterISS2 self, std::string const & s)
        """
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeRelabelImageFilterPython.delete_itkShapeRelabelImageFilterISS2

    def cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterISS2 *":
        """cast(itkLightObject obj) -> itkShapeRelabelImageFilterISS2"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeRelabelImageFilterISS2 *":
        """GetPointer(itkShapeRelabelImageFilterISS2 self) -> itkShapeRelabelImageFilterISS2"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeRelabelImageFilterISS2

        Create a new object of the class itkShapeRelabelImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeRelabelImageFilterISS2.Clone = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_Clone, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.SetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_SetBackgroundValue, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.GetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetBackgroundValue, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.GetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetReverseOrdering, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.SetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_SetReverseOrdering, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.ReverseOrderingOn = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_ReverseOrderingOn, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.ReverseOrderingOff = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_ReverseOrderingOff, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.GetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetAttribute, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.SetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_SetAttribute, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2.GetPointer = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_GetPointer, None, itkShapeRelabelImageFilterISS2)
itkShapeRelabelImageFilterISS2_swigregister = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_swigregister
itkShapeRelabelImageFilterISS2_swigregister(itkShapeRelabelImageFilterISS2)

def itkShapeRelabelImageFilterISS2___New_orig__() -> "itkShapeRelabelImageFilterISS2_Pointer":
    """itkShapeRelabelImageFilterISS2___New_orig__() -> itkShapeRelabelImageFilterISS2_Pointer"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2___New_orig__()

def itkShapeRelabelImageFilterISS2_cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterISS2 *":
    """itkShapeRelabelImageFilterISS2_cast(itkLightObject obj) -> itkShapeRelabelImageFilterISS2"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS2_cast(obj)

class itkShapeRelabelImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkShapeRelabelImageFilterISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeRelabelImageFilterISS3_Pointer":
        """__New_orig__() -> itkShapeRelabelImageFilterISS3_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeRelabelImageFilterISS3_Pointer":
        """Clone(itkShapeRelabelImageFilterISS3 self) -> itkShapeRelabelImageFilterISS3_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_Clone(self)

    InputEqualityComparableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_InputOStreamWritableCheck

    def SetBackgroundValue(self, _arg: 'short const') -> "void":
        """SetBackgroundValue(itkShapeRelabelImageFilterISS3 self, short const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "short":
        """GetBackgroundValue(itkShapeRelabelImageFilterISS3 self) -> short"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetBackgroundValue(self)


    def GetReverseOrdering(self) -> "bool":
        """GetReverseOrdering(itkShapeRelabelImageFilterISS3 self) -> bool"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetReverseOrdering(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeRelabelImageFilterISS3 self, bool const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_SetReverseOrdering(self, _arg)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeRelabelImageFilterISS3 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeRelabelImageFilterISS3 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeRelabelImageFilterISS3 self) -> unsigned int"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeRelabelImageFilterISS3 self, unsigned int const _arg)
        SetAttribute(itkShapeRelabelImageFilterISS3 self, std::string const & s)
        """
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeRelabelImageFilterPython.delete_itkShapeRelabelImageFilterISS3

    def cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterISS3 *":
        """cast(itkLightObject obj) -> itkShapeRelabelImageFilterISS3"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeRelabelImageFilterISS3 *":
        """GetPointer(itkShapeRelabelImageFilterISS3 self) -> itkShapeRelabelImageFilterISS3"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeRelabelImageFilterISS3

        Create a new object of the class itkShapeRelabelImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeRelabelImageFilterISS3.Clone = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_Clone, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.SetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_SetBackgroundValue, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.GetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetBackgroundValue, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.GetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetReverseOrdering, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.SetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_SetReverseOrdering, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.ReverseOrderingOn = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_ReverseOrderingOn, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.ReverseOrderingOff = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_ReverseOrderingOff, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.GetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetAttribute, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.SetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_SetAttribute, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3.GetPointer = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_GetPointer, None, itkShapeRelabelImageFilterISS3)
itkShapeRelabelImageFilterISS3_swigregister = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_swigregister
itkShapeRelabelImageFilterISS3_swigregister(itkShapeRelabelImageFilterISS3)

def itkShapeRelabelImageFilterISS3___New_orig__() -> "itkShapeRelabelImageFilterISS3_Pointer":
    """itkShapeRelabelImageFilterISS3___New_orig__() -> itkShapeRelabelImageFilterISS3_Pointer"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3___New_orig__()

def itkShapeRelabelImageFilterISS3_cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterISS3 *":
    """itkShapeRelabelImageFilterISS3_cast(itkLightObject obj) -> itkShapeRelabelImageFilterISS3"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterISS3_cast(obj)

class itkShapeRelabelImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkShapeRelabelImageFilterIUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeRelabelImageFilterIUC2_Pointer":
        """__New_orig__() -> itkShapeRelabelImageFilterIUC2_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeRelabelImageFilterIUC2_Pointer":
        """Clone(itkShapeRelabelImageFilterIUC2 self) -> itkShapeRelabelImageFilterIUC2_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_Clone(self)

    InputEqualityComparableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_InputOStreamWritableCheck

    def SetBackgroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetBackgroundValue(itkShapeRelabelImageFilterIUC2 self, unsigned char const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "unsigned char":
        """GetBackgroundValue(itkShapeRelabelImageFilterIUC2 self) -> unsigned char"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetBackgroundValue(self)


    def GetReverseOrdering(self) -> "bool":
        """GetReverseOrdering(itkShapeRelabelImageFilterIUC2 self) -> bool"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetReverseOrdering(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeRelabelImageFilterIUC2 self, bool const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_SetReverseOrdering(self, _arg)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeRelabelImageFilterIUC2 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeRelabelImageFilterIUC2 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeRelabelImageFilterIUC2 self) -> unsigned int"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeRelabelImageFilterIUC2 self, unsigned int const _arg)
        SetAttribute(itkShapeRelabelImageFilterIUC2 self, std::string const & s)
        """
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeRelabelImageFilterPython.delete_itkShapeRelabelImageFilterIUC2

    def cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterIUC2 *":
        """cast(itkLightObject obj) -> itkShapeRelabelImageFilterIUC2"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeRelabelImageFilterIUC2 *":
        """GetPointer(itkShapeRelabelImageFilterIUC2 self) -> itkShapeRelabelImageFilterIUC2"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeRelabelImageFilterIUC2

        Create a new object of the class itkShapeRelabelImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeRelabelImageFilterIUC2.Clone = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_Clone, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.SetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_SetBackgroundValue, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.GetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetBackgroundValue, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.GetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetReverseOrdering, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.SetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_SetReverseOrdering, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.ReverseOrderingOn = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_ReverseOrderingOn, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.ReverseOrderingOff = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_ReverseOrderingOff, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.GetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetAttribute, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.SetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_SetAttribute, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2.GetPointer = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_GetPointer, None, itkShapeRelabelImageFilterIUC2)
itkShapeRelabelImageFilterIUC2_swigregister = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_swigregister
itkShapeRelabelImageFilterIUC2_swigregister(itkShapeRelabelImageFilterIUC2)

def itkShapeRelabelImageFilterIUC2___New_orig__() -> "itkShapeRelabelImageFilterIUC2_Pointer":
    """itkShapeRelabelImageFilterIUC2___New_orig__() -> itkShapeRelabelImageFilterIUC2_Pointer"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2___New_orig__()

def itkShapeRelabelImageFilterIUC2_cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterIUC2 *":
    """itkShapeRelabelImageFilterIUC2_cast(itkLightObject obj) -> itkShapeRelabelImageFilterIUC2"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC2_cast(obj)

class itkShapeRelabelImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkShapeRelabelImageFilterIUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeRelabelImageFilterIUC3_Pointer":
        """__New_orig__() -> itkShapeRelabelImageFilterIUC3_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeRelabelImageFilterIUC3_Pointer":
        """Clone(itkShapeRelabelImageFilterIUC3 self) -> itkShapeRelabelImageFilterIUC3_Pointer"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_Clone(self)

    InputEqualityComparableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_InputOStreamWritableCheck

    def SetBackgroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetBackgroundValue(itkShapeRelabelImageFilterIUC3 self, unsigned char const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "unsigned char":
        """GetBackgroundValue(itkShapeRelabelImageFilterIUC3 self) -> unsigned char"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetBackgroundValue(self)


    def GetReverseOrdering(self) -> "bool":
        """GetReverseOrdering(itkShapeRelabelImageFilterIUC3 self) -> bool"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetReverseOrdering(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeRelabelImageFilterIUC3 self, bool const _arg)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_SetReverseOrdering(self, _arg)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeRelabelImageFilterIUC3 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeRelabelImageFilterIUC3 self)"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeRelabelImageFilterIUC3 self) -> unsigned int"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeRelabelImageFilterIUC3 self, unsigned int const _arg)
        SetAttribute(itkShapeRelabelImageFilterIUC3 self, std::string const & s)
        """
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeRelabelImageFilterPython.delete_itkShapeRelabelImageFilterIUC3

    def cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterIUC3 *":
        """cast(itkLightObject obj) -> itkShapeRelabelImageFilterIUC3"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeRelabelImageFilterIUC3 *":
        """GetPointer(itkShapeRelabelImageFilterIUC3 self) -> itkShapeRelabelImageFilterIUC3"""
        return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeRelabelImageFilterIUC3

        Create a new object of the class itkShapeRelabelImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeRelabelImageFilterIUC3.Clone = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_Clone, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.SetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_SetBackgroundValue, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.GetBackgroundValue = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetBackgroundValue, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.GetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetReverseOrdering, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.SetReverseOrdering = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_SetReverseOrdering, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.ReverseOrderingOn = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_ReverseOrderingOn, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.ReverseOrderingOff = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_ReverseOrderingOff, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.GetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetAttribute, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.SetAttribute = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_SetAttribute, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3.GetPointer = new_instancemethod(_itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_GetPointer, None, itkShapeRelabelImageFilterIUC3)
itkShapeRelabelImageFilterIUC3_swigregister = _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_swigregister
itkShapeRelabelImageFilterIUC3_swigregister(itkShapeRelabelImageFilterIUC3)

def itkShapeRelabelImageFilterIUC3___New_orig__() -> "itkShapeRelabelImageFilterIUC3_Pointer":
    """itkShapeRelabelImageFilterIUC3___New_orig__() -> itkShapeRelabelImageFilterIUC3_Pointer"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3___New_orig__()

def itkShapeRelabelImageFilterIUC3_cast(obj: 'itkLightObject') -> "itkShapeRelabelImageFilterIUC3 *":
    """itkShapeRelabelImageFilterIUC3_cast(itkLightObject obj) -> itkShapeRelabelImageFilterIUC3"""
    return _itkShapeRelabelImageFilterPython.itkShapeRelabelImageFilterIUC3_cast(obj)



