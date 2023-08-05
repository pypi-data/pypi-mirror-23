# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkReinitializeLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkReinitializeLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkReinitializeLevelSetImageFilterPython')
    _itkReinitializeLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkReinitializeLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkReinitializeLevelSetImageFilterPython
            return _itkReinitializeLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkReinitializeLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkReinitializeLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkReinitializeLevelSetImageFilterPython
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
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkOffsetPython
import itkSizePython
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
import itkIndexPython
import ITKCommonBasePython
import itkImageRegionPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import ITKFastMarchingBasePython
import itkLevelSetNodePython
import itkNodePairPython
import itkFastMarchingStoppingCriterionBasePython

def itkReinitializeLevelSetImageFilterIF3_New():
  return itkReinitializeLevelSetImageFilterIF3.New()


def itkReinitializeLevelSetImageFilterIF2_New():
  return itkReinitializeLevelSetImageFilterIF2.New()

class itkReinitializeLevelSetImageFilterIF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkReinitializeLevelSetImageFilterIF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkReinitializeLevelSetImageFilterIF2_Pointer":
        """__New_orig__() -> itkReinitializeLevelSetImageFilterIF2_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkReinitializeLevelSetImageFilterIF2_Pointer":
        """Clone(itkReinitializeLevelSetImageFilterIF2 self) -> itkReinitializeLevelSetImageFilterIF2_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_Clone(self)


    def SetLevelSetValue(self, _arg: 'double const') -> "void":
        """SetLevelSetValue(itkReinitializeLevelSetImageFilterIF2 self, double const _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetLevelSetValue(self, _arg)


    def GetLevelSetValue(self) -> "double":
        """GetLevelSetValue(itkReinitializeLevelSetImageFilterIF2 self) -> double"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetLevelSetValue(self)


    def SetNarrowBanding(self, _arg: 'bool const') -> "void":
        """SetNarrowBanding(itkReinitializeLevelSetImageFilterIF2 self, bool const _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetNarrowBanding(self, _arg)


    def GetNarrowBanding(self) -> "bool":
        """GetNarrowBanding(itkReinitializeLevelSetImageFilterIF2 self) -> bool"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetNarrowBanding(self)


    def NarrowBandingOn(self) -> "void":
        """NarrowBandingOn(itkReinitializeLevelSetImageFilterIF2 self)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_NarrowBandingOn(self)


    def NarrowBandingOff(self) -> "void":
        """NarrowBandingOff(itkReinitializeLevelSetImageFilterIF2 self)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_NarrowBandingOff(self)


    def SetInputNarrowBandwidth(self, _arg: 'double') -> "void":
        """SetInputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF2 self, double _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetInputNarrowBandwidth(self, _arg)


    def GetInputNarrowBandwidth(self) -> "double":
        """GetInputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF2 self) -> double"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetInputNarrowBandwidth(self)


    def SetOutputNarrowBandwidth(self, _arg: 'double') -> "void":
        """SetOutputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF2 self, double _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetOutputNarrowBandwidth(self, _arg)


    def GetOutputNarrowBandwidth(self) -> "double":
        """GetOutputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF2 self) -> double"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetOutputNarrowBandwidth(self)


    def SetNarrowBandwidth(self, value: 'double') -> "void":
        """SetNarrowBandwidth(itkReinitializeLevelSetImageFilterIF2 self, double value)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetNarrowBandwidth(self, value)


    def SetInputNarrowBand(self, ptr: 'itkVectorContainerUILSNF2') -> "void":
        """SetInputNarrowBand(itkReinitializeLevelSetImageFilterIF2 self, itkVectorContainerUILSNF2 ptr)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetInputNarrowBand(self, ptr)


    def GetInputNarrowBand(self) -> "itkVectorContainerUILSNF2_Pointer":
        """GetInputNarrowBand(itkReinitializeLevelSetImageFilterIF2 self) -> itkVectorContainerUILSNF2_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetInputNarrowBand(self)


    def GetOutputNarrowBand(self) -> "itkVectorContainerUILSNF2_Pointer":
        """GetOutputNarrowBand(itkReinitializeLevelSetImageFilterIF2 self) -> itkVectorContainerUILSNF2_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetOutputNarrowBand(self)

    LevelSetDoubleAdditiveOperatorsCheck = _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_LevelSetDoubleAdditiveOperatorsCheck
    LevelSetOStreamWritableCheck = _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_LevelSetOStreamWritableCheck
    __swig_destroy__ = _itkReinitializeLevelSetImageFilterPython.delete_itkReinitializeLevelSetImageFilterIF2

    def cast(obj: 'itkLightObject') -> "itkReinitializeLevelSetImageFilterIF2 *":
        """cast(itkLightObject obj) -> itkReinitializeLevelSetImageFilterIF2"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkReinitializeLevelSetImageFilterIF2 *":
        """GetPointer(itkReinitializeLevelSetImageFilterIF2 self) -> itkReinitializeLevelSetImageFilterIF2"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkReinitializeLevelSetImageFilterIF2

        Create a new object of the class itkReinitializeLevelSetImageFilterIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkReinitializeLevelSetImageFilterIF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkReinitializeLevelSetImageFilterIF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkReinitializeLevelSetImageFilterIF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkReinitializeLevelSetImageFilterIF2.Clone = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_Clone, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.SetLevelSetValue = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetLevelSetValue, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetLevelSetValue = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetLevelSetValue, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.SetNarrowBanding = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetNarrowBanding, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetNarrowBanding = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetNarrowBanding, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.NarrowBandingOn = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_NarrowBandingOn, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.NarrowBandingOff = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_NarrowBandingOff, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.SetInputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetInputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetInputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetInputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.SetOutputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetOutputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetOutputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetOutputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.SetNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.SetInputNarrowBand = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_SetInputNarrowBand, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetInputNarrowBand = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetInputNarrowBand, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetOutputNarrowBand = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetOutputNarrowBand, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2.GetPointer = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_GetPointer, None, itkReinitializeLevelSetImageFilterIF2)
itkReinitializeLevelSetImageFilterIF2_swigregister = _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_swigregister
itkReinitializeLevelSetImageFilterIF2_swigregister(itkReinitializeLevelSetImageFilterIF2)

def itkReinitializeLevelSetImageFilterIF2___New_orig__() -> "itkReinitializeLevelSetImageFilterIF2_Pointer":
    """itkReinitializeLevelSetImageFilterIF2___New_orig__() -> itkReinitializeLevelSetImageFilterIF2_Pointer"""
    return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2___New_orig__()

def itkReinitializeLevelSetImageFilterIF2_cast(obj: 'itkLightObject') -> "itkReinitializeLevelSetImageFilterIF2 *":
    """itkReinitializeLevelSetImageFilterIF2_cast(itkLightObject obj) -> itkReinitializeLevelSetImageFilterIF2"""
    return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF2_cast(obj)

class itkReinitializeLevelSetImageFilterIF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkReinitializeLevelSetImageFilterIF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkReinitializeLevelSetImageFilterIF3_Pointer":
        """__New_orig__() -> itkReinitializeLevelSetImageFilterIF3_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkReinitializeLevelSetImageFilterIF3_Pointer":
        """Clone(itkReinitializeLevelSetImageFilterIF3 self) -> itkReinitializeLevelSetImageFilterIF3_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_Clone(self)


    def SetLevelSetValue(self, _arg: 'double const') -> "void":
        """SetLevelSetValue(itkReinitializeLevelSetImageFilterIF3 self, double const _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetLevelSetValue(self, _arg)


    def GetLevelSetValue(self) -> "double":
        """GetLevelSetValue(itkReinitializeLevelSetImageFilterIF3 self) -> double"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetLevelSetValue(self)


    def SetNarrowBanding(self, _arg: 'bool const') -> "void":
        """SetNarrowBanding(itkReinitializeLevelSetImageFilterIF3 self, bool const _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetNarrowBanding(self, _arg)


    def GetNarrowBanding(self) -> "bool":
        """GetNarrowBanding(itkReinitializeLevelSetImageFilterIF3 self) -> bool"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetNarrowBanding(self)


    def NarrowBandingOn(self) -> "void":
        """NarrowBandingOn(itkReinitializeLevelSetImageFilterIF3 self)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_NarrowBandingOn(self)


    def NarrowBandingOff(self) -> "void":
        """NarrowBandingOff(itkReinitializeLevelSetImageFilterIF3 self)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_NarrowBandingOff(self)


    def SetInputNarrowBandwidth(self, _arg: 'double') -> "void":
        """SetInputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF3 self, double _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetInputNarrowBandwidth(self, _arg)


    def GetInputNarrowBandwidth(self) -> "double":
        """GetInputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF3 self) -> double"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetInputNarrowBandwidth(self)


    def SetOutputNarrowBandwidth(self, _arg: 'double') -> "void":
        """SetOutputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF3 self, double _arg)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetOutputNarrowBandwidth(self, _arg)


    def GetOutputNarrowBandwidth(self) -> "double":
        """GetOutputNarrowBandwidth(itkReinitializeLevelSetImageFilterIF3 self) -> double"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetOutputNarrowBandwidth(self)


    def SetNarrowBandwidth(self, value: 'double') -> "void":
        """SetNarrowBandwidth(itkReinitializeLevelSetImageFilterIF3 self, double value)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetNarrowBandwidth(self, value)


    def SetInputNarrowBand(self, ptr: 'itkVectorContainerUILSNF3') -> "void":
        """SetInputNarrowBand(itkReinitializeLevelSetImageFilterIF3 self, itkVectorContainerUILSNF3 ptr)"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetInputNarrowBand(self, ptr)


    def GetInputNarrowBand(self) -> "itkVectorContainerUILSNF3_Pointer":
        """GetInputNarrowBand(itkReinitializeLevelSetImageFilterIF3 self) -> itkVectorContainerUILSNF3_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetInputNarrowBand(self)


    def GetOutputNarrowBand(self) -> "itkVectorContainerUILSNF3_Pointer":
        """GetOutputNarrowBand(itkReinitializeLevelSetImageFilterIF3 self) -> itkVectorContainerUILSNF3_Pointer"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetOutputNarrowBand(self)

    LevelSetDoubleAdditiveOperatorsCheck = _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_LevelSetDoubleAdditiveOperatorsCheck
    LevelSetOStreamWritableCheck = _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_LevelSetOStreamWritableCheck
    __swig_destroy__ = _itkReinitializeLevelSetImageFilterPython.delete_itkReinitializeLevelSetImageFilterIF3

    def cast(obj: 'itkLightObject') -> "itkReinitializeLevelSetImageFilterIF3 *":
        """cast(itkLightObject obj) -> itkReinitializeLevelSetImageFilterIF3"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkReinitializeLevelSetImageFilterIF3 *":
        """GetPointer(itkReinitializeLevelSetImageFilterIF3 self) -> itkReinitializeLevelSetImageFilterIF3"""
        return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkReinitializeLevelSetImageFilterIF3

        Create a new object of the class itkReinitializeLevelSetImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkReinitializeLevelSetImageFilterIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkReinitializeLevelSetImageFilterIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkReinitializeLevelSetImageFilterIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkReinitializeLevelSetImageFilterIF3.Clone = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_Clone, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.SetLevelSetValue = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetLevelSetValue, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetLevelSetValue = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetLevelSetValue, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.SetNarrowBanding = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetNarrowBanding, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetNarrowBanding = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetNarrowBanding, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.NarrowBandingOn = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_NarrowBandingOn, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.NarrowBandingOff = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_NarrowBandingOff, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.SetInputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetInputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetInputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetInputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.SetOutputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetOutputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetOutputNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetOutputNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.SetNarrowBandwidth = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetNarrowBandwidth, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.SetInputNarrowBand = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_SetInputNarrowBand, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetInputNarrowBand = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetInputNarrowBand, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetOutputNarrowBand = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetOutputNarrowBand, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3.GetPointer = new_instancemethod(_itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_GetPointer, None, itkReinitializeLevelSetImageFilterIF3)
itkReinitializeLevelSetImageFilterIF3_swigregister = _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_swigregister
itkReinitializeLevelSetImageFilterIF3_swigregister(itkReinitializeLevelSetImageFilterIF3)

def itkReinitializeLevelSetImageFilterIF3___New_orig__() -> "itkReinitializeLevelSetImageFilterIF3_Pointer":
    """itkReinitializeLevelSetImageFilterIF3___New_orig__() -> itkReinitializeLevelSetImageFilterIF3_Pointer"""
    return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3___New_orig__()

def itkReinitializeLevelSetImageFilterIF3_cast(obj: 'itkLightObject') -> "itkReinitializeLevelSetImageFilterIF3 *":
    """itkReinitializeLevelSetImageFilterIF3_cast(itkLightObject obj) -> itkReinitializeLevelSetImageFilterIF3"""
    return _itkReinitializeLevelSetImageFilterPython.itkReinitializeLevelSetImageFilterIF3_cast(obj)



