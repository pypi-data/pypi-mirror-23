# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryFillholeImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinaryFillholeImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinaryFillholeImageFilterPython')
    _itkBinaryFillholeImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryFillholeImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryFillholeImageFilterPython
            return _itkBinaryFillholeImageFilterPython
        try:
            _mod = imp.load_module('_itkBinaryFillholeImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinaryFillholeImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryFillholeImageFilterPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkBinaryFillholeImageFilterIUC3_New():
  return itkBinaryFillholeImageFilterIUC3.New()


def itkBinaryFillholeImageFilterIUC2_New():
  return itkBinaryFillholeImageFilterIUC2.New()


def itkBinaryFillholeImageFilterISS3_New():
  return itkBinaryFillholeImageFilterISS3.New()


def itkBinaryFillholeImageFilterISS2_New():
  return itkBinaryFillholeImageFilterISS2.New()

class itkBinaryFillholeImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkBinaryFillholeImageFilterISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinaryFillholeImageFilterISS2_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinaryFillholeImageFilterISS2 self) -> itkBinaryFillholeImageFilterISS2_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_Clone(self)


    def SetFullyConnected(self, _arg):
        """SetFullyConnected(itkBinaryFillholeImageFilterISS2 self, bool const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_SetFullyConnected(self, _arg)


    def GetFullyConnected(self):
        """GetFullyConnected(itkBinaryFillholeImageFilterISS2 self) -> bool const &"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetFullyConnected(self)


    def FullyConnectedOn(self):
        """FullyConnectedOn(itkBinaryFillholeImageFilterISS2 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_FullyConnectedOn(self)


    def FullyConnectedOff(self):
        """FullyConnectedOff(itkBinaryFillholeImageFilterISS2 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_FullyConnectedOff(self)

    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_InputOStreamWritableCheck

    def SetForegroundValue(self, _arg):
        """SetForegroundValue(itkBinaryFillholeImageFilterISS2 self, short const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_SetForegroundValue(self, _arg)


    def GetForegroundValue(self):
        """GetForegroundValue(itkBinaryFillholeImageFilterISS2 self) -> short"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetForegroundValue(self)

    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterISS2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinaryFillholeImageFilterISS2"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinaryFillholeImageFilterISS2 self) -> itkBinaryFillholeImageFilterISS2"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterISS2

        Create a new object of the class itkBinaryFillholeImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryFillholeImageFilterISS2.Clone = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_Clone, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.SetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_SetFullyConnected, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.GetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetFullyConnected, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.FullyConnectedOn = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_FullyConnectedOn, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.FullyConnectedOff = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_FullyConnectedOff, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.SetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_SetForegroundValue, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.GetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetForegroundValue, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2.GetPointer = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetPointer, None, itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2_swigregister = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_swigregister
itkBinaryFillholeImageFilterISS2_swigregister(itkBinaryFillholeImageFilterISS2)

def itkBinaryFillholeImageFilterISS2___New_orig__():
    """itkBinaryFillholeImageFilterISS2___New_orig__() -> itkBinaryFillholeImageFilterISS2_Pointer"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2___New_orig__()

def itkBinaryFillholeImageFilterISS2_cast(obj):
    """itkBinaryFillholeImageFilterISS2_cast(itkLightObject obj) -> itkBinaryFillholeImageFilterISS2"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_cast(obj)

class itkBinaryFillholeImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkBinaryFillholeImageFilterISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinaryFillholeImageFilterISS3_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinaryFillholeImageFilterISS3 self) -> itkBinaryFillholeImageFilterISS3_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_Clone(self)


    def SetFullyConnected(self, _arg):
        """SetFullyConnected(itkBinaryFillholeImageFilterISS3 self, bool const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_SetFullyConnected(self, _arg)


    def GetFullyConnected(self):
        """GetFullyConnected(itkBinaryFillholeImageFilterISS3 self) -> bool const &"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetFullyConnected(self)


    def FullyConnectedOn(self):
        """FullyConnectedOn(itkBinaryFillholeImageFilterISS3 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_FullyConnectedOn(self)


    def FullyConnectedOff(self):
        """FullyConnectedOff(itkBinaryFillholeImageFilterISS3 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_FullyConnectedOff(self)

    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_InputOStreamWritableCheck

    def SetForegroundValue(self, _arg):
        """SetForegroundValue(itkBinaryFillholeImageFilterISS3 self, short const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_SetForegroundValue(self, _arg)


    def GetForegroundValue(self):
        """GetForegroundValue(itkBinaryFillholeImageFilterISS3 self) -> short"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetForegroundValue(self)

    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinaryFillholeImageFilterISS3"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinaryFillholeImageFilterISS3 self) -> itkBinaryFillholeImageFilterISS3"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterISS3

        Create a new object of the class itkBinaryFillholeImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryFillholeImageFilterISS3.Clone = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_Clone, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.SetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_SetFullyConnected, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.GetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetFullyConnected, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.FullyConnectedOn = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_FullyConnectedOn, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.FullyConnectedOff = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_FullyConnectedOff, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.SetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_SetForegroundValue, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.GetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetForegroundValue, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3.GetPointer = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetPointer, None, itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3_swigregister = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_swigregister
itkBinaryFillholeImageFilterISS3_swigregister(itkBinaryFillholeImageFilterISS3)

def itkBinaryFillholeImageFilterISS3___New_orig__():
    """itkBinaryFillholeImageFilterISS3___New_orig__() -> itkBinaryFillholeImageFilterISS3_Pointer"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3___New_orig__()

def itkBinaryFillholeImageFilterISS3_cast(obj):
    """itkBinaryFillholeImageFilterISS3_cast(itkLightObject obj) -> itkBinaryFillholeImageFilterISS3"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_cast(obj)

class itkBinaryFillholeImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkBinaryFillholeImageFilterIUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinaryFillholeImageFilterIUC2_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinaryFillholeImageFilterIUC2 self) -> itkBinaryFillholeImageFilterIUC2_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_Clone(self)


    def SetFullyConnected(self, _arg):
        """SetFullyConnected(itkBinaryFillholeImageFilterIUC2 self, bool const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_SetFullyConnected(self, _arg)


    def GetFullyConnected(self):
        """GetFullyConnected(itkBinaryFillholeImageFilterIUC2 self) -> bool const &"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetFullyConnected(self)


    def FullyConnectedOn(self):
        """FullyConnectedOn(itkBinaryFillholeImageFilterIUC2 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_FullyConnectedOn(self)


    def FullyConnectedOff(self):
        """FullyConnectedOff(itkBinaryFillholeImageFilterIUC2 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_FullyConnectedOff(self)

    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_InputOStreamWritableCheck

    def SetForegroundValue(self, _arg):
        """SetForegroundValue(itkBinaryFillholeImageFilterIUC2 self, unsigned char const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_SetForegroundValue(self, _arg)


    def GetForegroundValue(self):
        """GetForegroundValue(itkBinaryFillholeImageFilterIUC2 self) -> unsigned char"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetForegroundValue(self)

    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterIUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinaryFillholeImageFilterIUC2"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinaryFillholeImageFilterIUC2 self) -> itkBinaryFillholeImageFilterIUC2"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterIUC2

        Create a new object of the class itkBinaryFillholeImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryFillholeImageFilterIUC2.Clone = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_Clone, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.SetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_SetFullyConnected, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.GetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetFullyConnected, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.FullyConnectedOn = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_FullyConnectedOn, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.FullyConnectedOff = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_FullyConnectedOff, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.SetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_SetForegroundValue, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.GetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetForegroundValue, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2.GetPointer = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetPointer, None, itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2_swigregister = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_swigregister
itkBinaryFillholeImageFilterIUC2_swigregister(itkBinaryFillholeImageFilterIUC2)

def itkBinaryFillholeImageFilterIUC2___New_orig__():
    """itkBinaryFillholeImageFilterIUC2___New_orig__() -> itkBinaryFillholeImageFilterIUC2_Pointer"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2___New_orig__()

def itkBinaryFillholeImageFilterIUC2_cast(obj):
    """itkBinaryFillholeImageFilterIUC2_cast(itkLightObject obj) -> itkBinaryFillholeImageFilterIUC2"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_cast(obj)

class itkBinaryFillholeImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkBinaryFillholeImageFilterIUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinaryFillholeImageFilterIUC3_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinaryFillholeImageFilterIUC3 self) -> itkBinaryFillholeImageFilterIUC3_Pointer"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_Clone(self)


    def SetFullyConnected(self, _arg):
        """SetFullyConnected(itkBinaryFillholeImageFilterIUC3 self, bool const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_SetFullyConnected(self, _arg)


    def GetFullyConnected(self):
        """GetFullyConnected(itkBinaryFillholeImageFilterIUC3 self) -> bool const &"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetFullyConnected(self)


    def FullyConnectedOn(self):
        """FullyConnectedOn(itkBinaryFillholeImageFilterIUC3 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_FullyConnectedOn(self)


    def FullyConnectedOff(self):
        """FullyConnectedOff(itkBinaryFillholeImageFilterIUC3 self)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_FullyConnectedOff(self)

    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_InputOStreamWritableCheck

    def SetForegroundValue(self, _arg):
        """SetForegroundValue(itkBinaryFillholeImageFilterIUC3 self, unsigned char const _arg)"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_SetForegroundValue(self, _arg)


    def GetForegroundValue(self):
        """GetForegroundValue(itkBinaryFillholeImageFilterIUC3 self) -> unsigned char"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetForegroundValue(self)

    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterIUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinaryFillholeImageFilterIUC3"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinaryFillholeImageFilterIUC3 self) -> itkBinaryFillholeImageFilterIUC3"""
        return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterIUC3

        Create a new object of the class itkBinaryFillholeImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryFillholeImageFilterIUC3.Clone = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_Clone, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.SetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_SetFullyConnected, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.GetFullyConnected = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetFullyConnected, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.FullyConnectedOn = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_FullyConnectedOn, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.FullyConnectedOff = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_FullyConnectedOff, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.SetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_SetForegroundValue, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.GetForegroundValue = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetForegroundValue, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3.GetPointer = new_instancemethod(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetPointer, None, itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3_swigregister = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_swigregister
itkBinaryFillholeImageFilterIUC3_swigregister(itkBinaryFillholeImageFilterIUC3)

def itkBinaryFillholeImageFilterIUC3___New_orig__():
    """itkBinaryFillholeImageFilterIUC3___New_orig__() -> itkBinaryFillholeImageFilterIUC3_Pointer"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3___New_orig__()

def itkBinaryFillholeImageFilterIUC3_cast(obj):
    """itkBinaryFillholeImageFilterIUC3_cast(itkLightObject obj) -> itkBinaryFillholeImageFilterIUC3"""
    return _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_cast(obj)



