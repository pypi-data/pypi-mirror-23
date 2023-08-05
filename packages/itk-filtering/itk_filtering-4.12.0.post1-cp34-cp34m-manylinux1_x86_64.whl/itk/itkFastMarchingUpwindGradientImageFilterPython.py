# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingUpwindGradientImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingUpwindGradientImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingUpwindGradientImageFilterPython')
    _itkFastMarchingUpwindGradientImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingUpwindGradientImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingUpwindGradientImageFilterPython
            return _itkFastMarchingUpwindGradientImageFilterPython
        try:
            _mod = imp.load_module('_itkFastMarchingUpwindGradientImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingUpwindGradientImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingUpwindGradientImageFilterPython
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


import itkFastMarchingImageFilterPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import ITKFastMarchingBasePython
import itkLevelSetNodePython
import itkFastMarchingStoppingCriterionBasePython
import itkNodePairPython

def itkFastMarchingUpwindGradientImageFilterIF3IF3_New():
  return itkFastMarchingUpwindGradientImageFilterIF3IF3.New()


def itkFastMarchingUpwindGradientImageFilterIF2IF2_New():
  return itkFastMarchingUpwindGradientImageFilterIF2IF2.New()

class itkFastMarchingUpwindGradientImageFilterIF2IF2(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2):
    """Proxy of C++ itkFastMarchingUpwindGradientImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingUpwindGradientImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkFastMarchingUpwindGradientImageFilterIF2IF2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingUpwindGradientImageFilterIF2IF2_Pointer":
        """Clone(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> itkFastMarchingUpwindGradientImageFilterIF2IF2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_Clone(self)


    def SetTargetPoints(self, points: 'itkVectorContainerUILSNF2') -> "void":
        """SetTargetPoints(itkFastMarchingUpwindGradientImageFilterIF2IF2 self, itkVectorContainerUILSNF2 points)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetPoints(self, points)


    def GetTargetPoints(self) -> "itkVectorContainerUILSNF2_Pointer":
        """GetTargetPoints(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> itkVectorContainerUILSNF2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetPoints(self)


    def GetReachedTargetPoints(self) -> "itkVectorContainerUILSNF2_Pointer":
        """GetReachedTargetPoints(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> itkVectorContainerUILSNF2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetReachedTargetPoints(self)


    def GetGradientImage(self) -> "itkImageCVF22_Pointer":
        """GetGradientImage(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> itkImageCVF22_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetGradientImage(self)


    def SetGenerateGradientImage(self, _arg: 'bool const') -> "void":
        """SetGenerateGradientImage(itkFastMarchingUpwindGradientImageFilterIF2IF2 self, bool const _arg)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetGenerateGradientImage(self, _arg)


    def GetGenerateGradientImage(self) -> "bool const &":
        """GetGenerateGradientImage(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> bool const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetGenerateGradientImage(self)


    def GenerateGradientImageOn(self) -> "void":
        """GenerateGradientImageOn(itkFastMarchingUpwindGradientImageFilterIF2IF2 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GenerateGradientImageOn(self)


    def GenerateGradientImageOff(self) -> "void":
        """GenerateGradientImageOff(itkFastMarchingUpwindGradientImageFilterIF2IF2 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GenerateGradientImageOff(self)


    def SetTargetOffset(self, _arg: 'double const') -> "void":
        """SetTargetOffset(itkFastMarchingUpwindGradientImageFilterIF2IF2 self, double const _arg)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetOffset(self, _arg)


    def GetTargetOffset(self) -> "double const &":
        """GetTargetOffset(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> double const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetOffset(self)


    def SetTargetReachedMode(self, _arg: 'int const') -> "void":
        """SetTargetReachedMode(itkFastMarchingUpwindGradientImageFilterIF2IF2 self, int const _arg)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedMode(self, _arg)


    def GetTargetReachedMode(self) -> "int const &":
        """GetTargetReachedMode(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> int const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetReachedMode(self)


    def SetTargetReachedModeToNoTargets(self) -> "void":
        """SetTargetReachedModeToNoTargets(itkFastMarchingUpwindGradientImageFilterIF2IF2 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToNoTargets(self)


    def SetTargetReachedModeToOneTarget(self) -> "void":
        """SetTargetReachedModeToOneTarget(itkFastMarchingUpwindGradientImageFilterIF2IF2 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToOneTarget(self)


    def SetTargetReachedModeToSomeTargets(self, numberOfTargets: 'unsigned long') -> "void":
        """SetTargetReachedModeToSomeTargets(itkFastMarchingUpwindGradientImageFilterIF2IF2 self, unsigned long numberOfTargets)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToSomeTargets(self, numberOfTargets)


    def SetTargetReachedModeToAllTargets(self) -> "void":
        """SetTargetReachedModeToAllTargets(itkFastMarchingUpwindGradientImageFilterIF2IF2 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToAllTargets(self)


    def GetNumberOfTargets(self) -> "unsigned long const &":
        """GetNumberOfTargets(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> unsigned long const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetNumberOfTargets(self)


    def GetTargetValue(self) -> "double const &":
        """GetTargetValue(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> double const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetValue(self)

    NoTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_NoTargets
    OneTarget = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_OneTarget
    SomeTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SomeTargets
    AllTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_AllTargets
    LevelSetDoubleDivisionOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_LevelSetDoubleDivisionOperatorsCheck
    LevelSetDoubleDivisionAndAssignOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_LevelSetDoubleDivisionAndAssignOperatorsCheck
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterPython.delete_itkFastMarchingUpwindGradientImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterIF2IF2"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingUpwindGradientImageFilterIF2IF2 *":
        """GetPointer(itkFastMarchingUpwindGradientImageFilterIF2IF2 self) -> itkFastMarchingUpwindGradientImageFilterIF2IF2"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterIF2IF2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingUpwindGradientImageFilterIF2IF2.Clone = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_Clone, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetPoints = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetPoints, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetTargetPoints = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetPoints, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetReachedTargetPoints = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetReachedTargetPoints, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetGradientImage, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetGenerateGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetGenerateGradientImage, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetGenerateGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetGenerateGradientImage, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GenerateGradientImageOn = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GenerateGradientImageOn, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GenerateGradientImageOff = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GenerateGradientImageOff, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetOffset = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetOffset, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetTargetOffset = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetOffset, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetReachedMode = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedMode, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetTargetReachedMode = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetReachedMode, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetReachedModeToNoTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToNoTargets, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetReachedModeToOneTarget = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToOneTarget, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetReachedModeToSomeTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToSomeTargets, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.SetTargetReachedModeToAllTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToAllTargets, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetNumberOfTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetNumberOfTargets, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetTargetValue = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetValue, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2.GetPointer = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetPointer, None, itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2_swigregister = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_swigregister
itkFastMarchingUpwindGradientImageFilterIF2IF2_swigregister(itkFastMarchingUpwindGradientImageFilterIF2IF2)

def itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__() -> "itkFastMarchingUpwindGradientImageFilterIF2IF2_Pointer":
    """itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__() -> itkFastMarchingUpwindGradientImageFilterIF2IF2_Pointer"""
    return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__()

def itkFastMarchingUpwindGradientImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterIF2IF2 *":
    """itkFastMarchingUpwindGradientImageFilterIF2IF2_cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterIF2IF2"""
    return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_cast(obj)

class itkFastMarchingUpwindGradientImageFilterIF3IF3(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3):
    """Proxy of C++ itkFastMarchingUpwindGradientImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingUpwindGradientImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkFastMarchingUpwindGradientImageFilterIF3IF3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingUpwindGradientImageFilterIF3IF3_Pointer":
        """Clone(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> itkFastMarchingUpwindGradientImageFilterIF3IF3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_Clone(self)


    def SetTargetPoints(self, points: 'itkVectorContainerUILSNF3') -> "void":
        """SetTargetPoints(itkFastMarchingUpwindGradientImageFilterIF3IF3 self, itkVectorContainerUILSNF3 points)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetPoints(self, points)


    def GetTargetPoints(self) -> "itkVectorContainerUILSNF3_Pointer":
        """GetTargetPoints(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> itkVectorContainerUILSNF3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetPoints(self)


    def GetReachedTargetPoints(self) -> "itkVectorContainerUILSNF3_Pointer":
        """GetReachedTargetPoints(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> itkVectorContainerUILSNF3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetReachedTargetPoints(self)


    def GetGradientImage(self) -> "itkImageCVF33_Pointer":
        """GetGradientImage(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> itkImageCVF33_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetGradientImage(self)


    def SetGenerateGradientImage(self, _arg: 'bool const') -> "void":
        """SetGenerateGradientImage(itkFastMarchingUpwindGradientImageFilterIF3IF3 self, bool const _arg)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetGenerateGradientImage(self, _arg)


    def GetGenerateGradientImage(self) -> "bool const &":
        """GetGenerateGradientImage(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> bool const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetGenerateGradientImage(self)


    def GenerateGradientImageOn(self) -> "void":
        """GenerateGradientImageOn(itkFastMarchingUpwindGradientImageFilterIF3IF3 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GenerateGradientImageOn(self)


    def GenerateGradientImageOff(self) -> "void":
        """GenerateGradientImageOff(itkFastMarchingUpwindGradientImageFilterIF3IF3 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GenerateGradientImageOff(self)


    def SetTargetOffset(self, _arg: 'double const') -> "void":
        """SetTargetOffset(itkFastMarchingUpwindGradientImageFilterIF3IF3 self, double const _arg)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetOffset(self, _arg)


    def GetTargetOffset(self) -> "double const &":
        """GetTargetOffset(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> double const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetOffset(self)


    def SetTargetReachedMode(self, _arg: 'int const') -> "void":
        """SetTargetReachedMode(itkFastMarchingUpwindGradientImageFilterIF3IF3 self, int const _arg)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedMode(self, _arg)


    def GetTargetReachedMode(self) -> "int const &":
        """GetTargetReachedMode(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> int const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetReachedMode(self)


    def SetTargetReachedModeToNoTargets(self) -> "void":
        """SetTargetReachedModeToNoTargets(itkFastMarchingUpwindGradientImageFilterIF3IF3 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToNoTargets(self)


    def SetTargetReachedModeToOneTarget(self) -> "void":
        """SetTargetReachedModeToOneTarget(itkFastMarchingUpwindGradientImageFilterIF3IF3 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToOneTarget(self)


    def SetTargetReachedModeToSomeTargets(self, numberOfTargets: 'unsigned long') -> "void":
        """SetTargetReachedModeToSomeTargets(itkFastMarchingUpwindGradientImageFilterIF3IF3 self, unsigned long numberOfTargets)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToSomeTargets(self, numberOfTargets)


    def SetTargetReachedModeToAllTargets(self) -> "void":
        """SetTargetReachedModeToAllTargets(itkFastMarchingUpwindGradientImageFilterIF3IF3 self)"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToAllTargets(self)


    def GetNumberOfTargets(self) -> "unsigned long const &":
        """GetNumberOfTargets(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> unsigned long const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetNumberOfTargets(self)


    def GetTargetValue(self) -> "double const &":
        """GetTargetValue(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> double const &"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetValue(self)

    NoTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_NoTargets
    OneTarget = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_OneTarget
    SomeTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SomeTargets
    AllTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_AllTargets
    LevelSetDoubleDivisionOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_LevelSetDoubleDivisionOperatorsCheck
    LevelSetDoubleDivisionAndAssignOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_LevelSetDoubleDivisionAndAssignOperatorsCheck
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterPython.delete_itkFastMarchingUpwindGradientImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterIF3IF3"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingUpwindGradientImageFilterIF3IF3 *":
        """GetPointer(itkFastMarchingUpwindGradientImageFilterIF3IF3 self) -> itkFastMarchingUpwindGradientImageFilterIF3IF3"""
        return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterIF3IF3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingUpwindGradientImageFilterIF3IF3.Clone = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_Clone, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetPoints = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetPoints, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetTargetPoints = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetPoints, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetReachedTargetPoints = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetReachedTargetPoints, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetGradientImage, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetGenerateGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetGenerateGradientImage, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetGenerateGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetGenerateGradientImage, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GenerateGradientImageOn = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GenerateGradientImageOn, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GenerateGradientImageOff = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GenerateGradientImageOff, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetOffset = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetOffset, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetTargetOffset = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetOffset, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetReachedMode = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedMode, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetTargetReachedMode = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetReachedMode, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetReachedModeToNoTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToNoTargets, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetReachedModeToOneTarget = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToOneTarget, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetReachedModeToSomeTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToSomeTargets, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.SetTargetReachedModeToAllTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToAllTargets, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetNumberOfTargets = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetNumberOfTargets, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetTargetValue = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetValue, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3.GetPointer = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetPointer, None, itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3_swigregister = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_swigregister
itkFastMarchingUpwindGradientImageFilterIF3IF3_swigregister(itkFastMarchingUpwindGradientImageFilterIF3IF3)

def itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__() -> "itkFastMarchingUpwindGradientImageFilterIF3IF3_Pointer":
    """itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__() -> itkFastMarchingUpwindGradientImageFilterIF3IF3_Pointer"""
    return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__()

def itkFastMarchingUpwindGradientImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterIF3IF3 *":
    """itkFastMarchingUpwindGradientImageFilterIF3IF3_cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterIF3IF3"""
    return _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_cast(obj)



