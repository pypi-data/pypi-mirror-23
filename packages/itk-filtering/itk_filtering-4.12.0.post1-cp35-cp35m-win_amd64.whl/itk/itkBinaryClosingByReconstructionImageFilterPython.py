# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryClosingByReconstructionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinaryClosingByReconstructionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinaryClosingByReconstructionImageFilterPython')
    _itkBinaryClosingByReconstructionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryClosingByReconstructionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryClosingByReconstructionImageFilterPython
            return _itkBinaryClosingByReconstructionImageFilterPython
        try:
            _mod = imp.load_module('_itkBinaryClosingByReconstructionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinaryClosingByReconstructionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryClosingByReconstructionImageFilterPython
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
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import ITKCommonBasePython
import itkImageRegionPython
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkNeighborhoodPython

def itkBinaryClosingByReconstructionImageFilterIUC3SE3_New():
  return itkBinaryClosingByReconstructionImageFilterIUC3SE3.New()


def itkBinaryClosingByReconstructionImageFilterIUC2SE2_New():
  return itkBinaryClosingByReconstructionImageFilterIUC2SE2.New()

class itkBinaryClosingByReconstructionImageFilterIUC2SE2(itkFlatStructuringElementPython.itkKernelImageFilterIUC2IUC2SE2):
    """Proxy of C++ itkBinaryClosingByReconstructionImageFilterIUC2SE2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryClosingByReconstructionImageFilterIUC2SE2_Pointer":
        """__New_orig__() -> itkBinaryClosingByReconstructionImageFilterIUC2SE2_Pointer"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryClosingByReconstructionImageFilterIUC2SE2_Pointer":
        """Clone(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self) -> itkBinaryClosingByReconstructionImageFilterIUC2SE2_Pointer"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_Clone(self)


    def SetForegroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetForegroundValue(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self, unsigned char const _arg)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_SetForegroundValue(self, _arg)


    def GetForegroundValue(self) -> "unsigned char":
        """GetForegroundValue(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self) -> unsigned char"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_GetForegroundValue(self)


    def SetFullyConnected(self, _arg: 'bool const') -> "void":
        """SetFullyConnected(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self, bool const _arg)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_SetFullyConnected(self, _arg)


    def GetFullyConnected(self) -> "bool const &":
        """GetFullyConnected(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self) -> bool const &"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_GetFullyConnected(self)


    def FullyConnectedOn(self) -> "void":
        """FullyConnectedOn(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_FullyConnectedOn(self)


    def FullyConnectedOff(self) -> "void":
        """FullyConnectedOff(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_FullyConnectedOff(self)

    __swig_destroy__ = _itkBinaryClosingByReconstructionImageFilterPython.delete_itkBinaryClosingByReconstructionImageFilterIUC2SE2

    def cast(obj: 'itkLightObject') -> "itkBinaryClosingByReconstructionImageFilterIUC2SE2 *":
        """cast(itkLightObject obj) -> itkBinaryClosingByReconstructionImageFilterIUC2SE2"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryClosingByReconstructionImageFilterIUC2SE2 *":
        """GetPointer(itkBinaryClosingByReconstructionImageFilterIUC2SE2 self) -> itkBinaryClosingByReconstructionImageFilterIUC2SE2"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryClosingByReconstructionImageFilterIUC2SE2

        Create a new object of the class itkBinaryClosingByReconstructionImageFilterIUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryClosingByReconstructionImageFilterIUC2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryClosingByReconstructionImageFilterIUC2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryClosingByReconstructionImageFilterIUC2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryClosingByReconstructionImageFilterIUC2SE2.Clone = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_Clone, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.SetForegroundValue = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_SetForegroundValue, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.GetForegroundValue = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_GetForegroundValue, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.SetFullyConnected = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_SetFullyConnected, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.GetFullyConnected = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_GetFullyConnected, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.FullyConnectedOn = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_FullyConnectedOn, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.FullyConnectedOff = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_FullyConnectedOff, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2.GetPointer = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_GetPointer, None, itkBinaryClosingByReconstructionImageFilterIUC2SE2)
itkBinaryClosingByReconstructionImageFilterIUC2SE2_swigregister = _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_swigregister
itkBinaryClosingByReconstructionImageFilterIUC2SE2_swigregister(itkBinaryClosingByReconstructionImageFilterIUC2SE2)

def itkBinaryClosingByReconstructionImageFilterIUC2SE2___New_orig__() -> "itkBinaryClosingByReconstructionImageFilterIUC2SE2_Pointer":
    """itkBinaryClosingByReconstructionImageFilterIUC2SE2___New_orig__() -> itkBinaryClosingByReconstructionImageFilterIUC2SE2_Pointer"""
    return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2___New_orig__()

def itkBinaryClosingByReconstructionImageFilterIUC2SE2_cast(obj: 'itkLightObject') -> "itkBinaryClosingByReconstructionImageFilterIUC2SE2 *":
    """itkBinaryClosingByReconstructionImageFilterIUC2SE2_cast(itkLightObject obj) -> itkBinaryClosingByReconstructionImageFilterIUC2SE2"""
    return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC2SE2_cast(obj)

class itkBinaryClosingByReconstructionImageFilterIUC3SE3(itkFlatStructuringElementPython.itkKernelImageFilterIUC3IUC3SE3):
    """Proxy of C++ itkBinaryClosingByReconstructionImageFilterIUC3SE3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryClosingByReconstructionImageFilterIUC3SE3_Pointer":
        """__New_orig__() -> itkBinaryClosingByReconstructionImageFilterIUC3SE3_Pointer"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryClosingByReconstructionImageFilterIUC3SE3_Pointer":
        """Clone(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self) -> itkBinaryClosingByReconstructionImageFilterIUC3SE3_Pointer"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_Clone(self)


    def SetForegroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetForegroundValue(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self, unsigned char const _arg)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_SetForegroundValue(self, _arg)


    def GetForegroundValue(self) -> "unsigned char":
        """GetForegroundValue(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self) -> unsigned char"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_GetForegroundValue(self)


    def SetFullyConnected(self, _arg: 'bool const') -> "void":
        """SetFullyConnected(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self, bool const _arg)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_SetFullyConnected(self, _arg)


    def GetFullyConnected(self) -> "bool const &":
        """GetFullyConnected(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self) -> bool const &"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_GetFullyConnected(self)


    def FullyConnectedOn(self) -> "void":
        """FullyConnectedOn(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_FullyConnectedOn(self)


    def FullyConnectedOff(self) -> "void":
        """FullyConnectedOff(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self)"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_FullyConnectedOff(self)

    __swig_destroy__ = _itkBinaryClosingByReconstructionImageFilterPython.delete_itkBinaryClosingByReconstructionImageFilterIUC3SE3

    def cast(obj: 'itkLightObject') -> "itkBinaryClosingByReconstructionImageFilterIUC3SE3 *":
        """cast(itkLightObject obj) -> itkBinaryClosingByReconstructionImageFilterIUC3SE3"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryClosingByReconstructionImageFilterIUC3SE3 *":
        """GetPointer(itkBinaryClosingByReconstructionImageFilterIUC3SE3 self) -> itkBinaryClosingByReconstructionImageFilterIUC3SE3"""
        return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryClosingByReconstructionImageFilterIUC3SE3

        Create a new object of the class itkBinaryClosingByReconstructionImageFilterIUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryClosingByReconstructionImageFilterIUC3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryClosingByReconstructionImageFilterIUC3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryClosingByReconstructionImageFilterIUC3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryClosingByReconstructionImageFilterIUC3SE3.Clone = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_Clone, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.SetForegroundValue = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_SetForegroundValue, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.GetForegroundValue = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_GetForegroundValue, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.SetFullyConnected = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_SetFullyConnected, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.GetFullyConnected = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_GetFullyConnected, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.FullyConnectedOn = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_FullyConnectedOn, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.FullyConnectedOff = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_FullyConnectedOff, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3.GetPointer = new_instancemethod(_itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_GetPointer, None, itkBinaryClosingByReconstructionImageFilterIUC3SE3)
itkBinaryClosingByReconstructionImageFilterIUC3SE3_swigregister = _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_swigregister
itkBinaryClosingByReconstructionImageFilterIUC3SE3_swigregister(itkBinaryClosingByReconstructionImageFilterIUC3SE3)

def itkBinaryClosingByReconstructionImageFilterIUC3SE3___New_orig__() -> "itkBinaryClosingByReconstructionImageFilterIUC3SE3_Pointer":
    """itkBinaryClosingByReconstructionImageFilterIUC3SE3___New_orig__() -> itkBinaryClosingByReconstructionImageFilterIUC3SE3_Pointer"""
    return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3___New_orig__()

def itkBinaryClosingByReconstructionImageFilterIUC3SE3_cast(obj: 'itkLightObject') -> "itkBinaryClosingByReconstructionImageFilterIUC3SE3 *":
    """itkBinaryClosingByReconstructionImageFilterIUC3SE3_cast(itkLightObject obj) -> itkBinaryClosingByReconstructionImageFilterIUC3SE3"""
    return _itkBinaryClosingByReconstructionImageFilterPython.itkBinaryClosingByReconstructionImageFilterIUC3SE3_cast(obj)



