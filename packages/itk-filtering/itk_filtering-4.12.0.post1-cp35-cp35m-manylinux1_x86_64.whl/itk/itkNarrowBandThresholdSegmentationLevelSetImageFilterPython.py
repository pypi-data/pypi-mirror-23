# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython')
    _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython
            return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython
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
import itkNarrowBandLevelSetImageFilterPython
import itkNarrowBandImageFilterBasePython
import ITKNarrowBandBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import stdcomplexPython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython

def itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_New():
  return itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.New()


def itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_New():
  return itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.New()

class itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterIF2IF2F):
    """Proxy of C++ itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """__New_orig__() -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """Clone(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Clone(self)


    def SetUpperThreshold(self, v: 'float') -> "void":
        """SetUpperThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetUpperThreshold(self, v)


    def SetLowerThreshold(self, v: 'float') -> "void":
        """SetLowerThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetLowerThreshold(self, v)


    def GetUpperThreshold(self) -> "float":
        """GetUpperThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetUpperThreshold(self)


    def GetLowerThreshold(self) -> "float":
        """GetLowerThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetLowerThreshold(self)


    def SetEdgeWeight(self, v: 'float') -> "void":
        """SetEdgeWeight(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetEdgeWeight(self, v)


    def GetEdgeWeight(self) -> "float":
        """GetEdgeWeight(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetEdgeWeight(self)


    def SetSmoothingIterations(self, v: 'int') -> "void":
        """SetSmoothingIterations(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self, int v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingIterations(self, v)


    def GetSmoothingIterations(self) -> "int":
        """GetSmoothingIterations(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> int"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingIterations(self)


    def SetSmoothingTimeStep(self, v: 'float') -> "void":
        """SetSmoothingTimeStep(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingTimeStep(self, v)


    def GetSmoothingTimeStep(self) -> "float":
        """GetSmoothingTimeStep(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingTimeStep(self)


    def SetSmoothingConductance(self, v: 'float') -> "void":
        """SetSmoothingConductance(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingConductance(self, v)


    def GetSmoothingConductance(self) -> "float":
        """GetSmoothingConductance(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingConductance(self)

    OutputHasNumericTraitsCheck = _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.delete_itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F

    def cast(obj: 'itkLightObject') -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F *":
        """cast(itkLightObject obj) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F *":
        """GetPointer(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F

        Create a new object of the class itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Clone, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.SetUpperThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetUpperThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.SetLowerThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetLowerThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetUpperThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetUpperThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetLowerThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetLowerThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.SetEdgeWeight = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetEdgeWeight, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetEdgeWeight = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetEdgeWeight, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.SetSmoothingIterations = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingIterations, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetSmoothingIterations = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingIterations, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.SetSmoothingTimeStep = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingTimeStep, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetSmoothingTimeStep = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingTimeStep, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.SetSmoothingConductance = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingConductance, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetSmoothingConductance = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingConductance, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F.GetPointer = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_GetPointer, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_swigregister = _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_swigregister
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_swigregister(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F)

def itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer":
    """itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

def itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(obj: 'itkLightObject') -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F *":
    """itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F"""
    return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

class itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterIF3IF3F):
    """Proxy of C++ itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """__New_orig__() -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """Clone(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Clone(self)


    def SetUpperThreshold(self, v: 'float') -> "void":
        """SetUpperThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetUpperThreshold(self, v)


    def SetLowerThreshold(self, v: 'float') -> "void":
        """SetLowerThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetLowerThreshold(self, v)


    def GetUpperThreshold(self) -> "float":
        """GetUpperThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetUpperThreshold(self)


    def GetLowerThreshold(self) -> "float":
        """GetLowerThreshold(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetLowerThreshold(self)


    def SetEdgeWeight(self, v: 'float') -> "void":
        """SetEdgeWeight(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetEdgeWeight(self, v)


    def GetEdgeWeight(self) -> "float":
        """GetEdgeWeight(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetEdgeWeight(self)


    def SetSmoothingIterations(self, v: 'int') -> "void":
        """SetSmoothingIterations(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self, int v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingIterations(self, v)


    def GetSmoothingIterations(self) -> "int":
        """GetSmoothingIterations(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> int"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingIterations(self)


    def SetSmoothingTimeStep(self, v: 'float') -> "void":
        """SetSmoothingTimeStep(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingTimeStep(self, v)


    def GetSmoothingTimeStep(self) -> "float":
        """GetSmoothingTimeStep(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingTimeStep(self)


    def SetSmoothingConductance(self, v: 'float') -> "void":
        """SetSmoothingConductance(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingConductance(self, v)


    def GetSmoothingConductance(self) -> "float":
        """GetSmoothingConductance(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingConductance(self)

    OutputHasNumericTraitsCheck = _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.delete_itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F

    def cast(obj: 'itkLightObject') -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F *":
        """cast(itkLightObject obj) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F *":
        """GetPointer(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F

        Create a new object of the class itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Clone, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.SetUpperThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetUpperThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.SetLowerThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetLowerThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetUpperThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetUpperThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetLowerThreshold = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetLowerThreshold, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.SetEdgeWeight = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetEdgeWeight, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetEdgeWeight = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetEdgeWeight, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.SetSmoothingIterations = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingIterations, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetSmoothingIterations = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingIterations, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.SetSmoothingTimeStep = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingTimeStep, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetSmoothingTimeStep = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingTimeStep, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.SetSmoothingConductance = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingConductance, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetSmoothingConductance = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingConductance, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F.GetPointer = new_instancemethod(_itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_GetPointer, None, itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_swigregister = _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_swigregister
itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_swigregister(itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F)

def itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer":
    """itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

def itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(obj: 'itkLightObject') -> "itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F *":
    """itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F"""
    return _itkNarrowBandThresholdSegmentationLevelSetImageFilterPython.itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(obj)



