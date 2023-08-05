# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkThresholdSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkThresholdSegmentationLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkThresholdSegmentationLevelSetImageFilterPython')
    _itkThresholdSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkThresholdSegmentationLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkThresholdSegmentationLevelSetImageFilterPython
            return _itkThresholdSegmentationLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkThresholdSegmentationLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkThresholdSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkThresholdSegmentationLevelSetImageFilterPython
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


import itkSegmentationLevelSetImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
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
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython

def itkThresholdSegmentationLevelSetImageFilterIF3IF3F_New():
  return itkThresholdSegmentationLevelSetImageFilterIF3IF3F.New()


def itkThresholdSegmentationLevelSetImageFilterIF2IF2F_New():
  return itkThresholdSegmentationLevelSetImageFilterIF2IF2F.New()

class itkThresholdSegmentationLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    """Proxy of C++ itkThresholdSegmentationLevelSetImageFilterIF2IF2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """__New_orig__() -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """Clone(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Clone(self)


    def SetUpperThreshold(self, v: 'float') -> "void":
        """SetUpperThreshold(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetUpperThreshold(self, v)


    def SetLowerThreshold(self, v: 'float') -> "void":
        """SetLowerThreshold(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetLowerThreshold(self, v)


    def GetUpperThreshold(self) -> "float":
        """GetUpperThreshold(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetUpperThreshold(self)


    def GetLowerThreshold(self) -> "float":
        """GetLowerThreshold(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetLowerThreshold(self)


    def SetEdgeWeight(self, v: 'float') -> "void":
        """SetEdgeWeight(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetEdgeWeight(self, v)


    def GetEdgeWeight(self) -> "float":
        """GetEdgeWeight(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetEdgeWeight(self)


    def SetSmoothingIterations(self, v: 'int') -> "void":
        """SetSmoothingIterations(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self, int v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingIterations(self, v)


    def GetSmoothingIterations(self) -> "int":
        """GetSmoothingIterations(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> int"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingIterations(self)


    def SetSmoothingTimeStep(self, v: 'float') -> "void":
        """SetSmoothingTimeStep(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingTimeStep(self, v)


    def GetSmoothingTimeStep(self) -> "float":
        """GetSmoothingTimeStep(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingTimeStep(self)


    def SetSmoothingConductance(self, v: 'float') -> "void":
        """SetSmoothingConductance(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingConductance(self, v)


    def GetSmoothingConductance(self) -> "float":
        """GetSmoothingConductance(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingConductance(self)

    __swig_destroy__ = _itkThresholdSegmentationLevelSetImageFilterPython.delete_itkThresholdSegmentationLevelSetImageFilterIF2IF2F

    def cast(obj: 'itkLightObject') -> "itkThresholdSegmentationLevelSetImageFilterIF2IF2F *":
        """cast(itkLightObject obj) -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkThresholdSegmentationLevelSetImageFilterIF2IF2F *":
        """GetPointer(itkThresholdSegmentationLevelSetImageFilterIF2IF2F self) -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F

        Create a new object of the class itkThresholdSegmentationLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkThresholdSegmentationLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkThresholdSegmentationLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkThresholdSegmentationLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkThresholdSegmentationLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Clone, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.SetUpperThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetUpperThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.SetLowerThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetLowerThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetUpperThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetUpperThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetLowerThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetLowerThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.SetEdgeWeight = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetEdgeWeight, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetEdgeWeight = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetEdgeWeight, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.SetSmoothingIterations = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingIterations, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetSmoothingIterations = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingIterations, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.SetSmoothingTimeStep = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingTimeStep, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetSmoothingTimeStep = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingTimeStep, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.SetSmoothingConductance = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_SetSmoothingConductance, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetSmoothingConductance = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetSmoothingConductance, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F.GetPointer = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_GetPointer, None, itkThresholdSegmentationLevelSetImageFilterIF2IF2F)
itkThresholdSegmentationLevelSetImageFilterIF2IF2F_swigregister = _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_swigregister
itkThresholdSegmentationLevelSetImageFilterIF2IF2F_swigregister(itkThresholdSegmentationLevelSetImageFilterIF2IF2F)

def itkThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> "itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer":
    """itkThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

def itkThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(obj: 'itkLightObject') -> "itkThresholdSegmentationLevelSetImageFilterIF2IF2F *":
    """itkThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkThresholdSegmentationLevelSetImageFilterIF2IF2F"""
    return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

class itkThresholdSegmentationLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    """Proxy of C++ itkThresholdSegmentationLevelSetImageFilterIF3IF3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """__New_orig__() -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """Clone(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Clone(self)


    def SetUpperThreshold(self, v: 'float') -> "void":
        """SetUpperThreshold(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetUpperThreshold(self, v)


    def SetLowerThreshold(self, v: 'float') -> "void":
        """SetLowerThreshold(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetLowerThreshold(self, v)


    def GetUpperThreshold(self) -> "float":
        """GetUpperThreshold(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetUpperThreshold(self)


    def GetLowerThreshold(self) -> "float":
        """GetLowerThreshold(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetLowerThreshold(self)


    def SetEdgeWeight(self, v: 'float') -> "void":
        """SetEdgeWeight(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetEdgeWeight(self, v)


    def GetEdgeWeight(self) -> "float":
        """GetEdgeWeight(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetEdgeWeight(self)


    def SetSmoothingIterations(self, v: 'int') -> "void":
        """SetSmoothingIterations(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self, int v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingIterations(self, v)


    def GetSmoothingIterations(self) -> "int":
        """GetSmoothingIterations(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> int"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingIterations(self)


    def SetSmoothingTimeStep(self, v: 'float') -> "void":
        """SetSmoothingTimeStep(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingTimeStep(self, v)


    def GetSmoothingTimeStep(self) -> "float":
        """GetSmoothingTimeStep(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingTimeStep(self)


    def SetSmoothingConductance(self, v: 'float') -> "void":
        """SetSmoothingConductance(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self, float v)"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingConductance(self, v)


    def GetSmoothingConductance(self) -> "float":
        """GetSmoothingConductance(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingConductance(self)

    __swig_destroy__ = _itkThresholdSegmentationLevelSetImageFilterPython.delete_itkThresholdSegmentationLevelSetImageFilterIF3IF3F

    def cast(obj: 'itkLightObject') -> "itkThresholdSegmentationLevelSetImageFilterIF3IF3F *":
        """cast(itkLightObject obj) -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkThresholdSegmentationLevelSetImageFilterIF3IF3F *":
        """GetPointer(itkThresholdSegmentationLevelSetImageFilterIF3IF3F self) -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F

        Create a new object of the class itkThresholdSegmentationLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkThresholdSegmentationLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkThresholdSegmentationLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkThresholdSegmentationLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkThresholdSegmentationLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Clone, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.SetUpperThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetUpperThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.SetLowerThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetLowerThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetUpperThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetUpperThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetLowerThreshold = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetLowerThreshold, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.SetEdgeWeight = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetEdgeWeight, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetEdgeWeight = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetEdgeWeight, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.SetSmoothingIterations = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingIterations, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetSmoothingIterations = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingIterations, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.SetSmoothingTimeStep = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingTimeStep, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetSmoothingTimeStep = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingTimeStep, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.SetSmoothingConductance = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_SetSmoothingConductance, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetSmoothingConductance = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetSmoothingConductance, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F.GetPointer = new_instancemethod(_itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_GetPointer, None, itkThresholdSegmentationLevelSetImageFilterIF3IF3F)
itkThresholdSegmentationLevelSetImageFilterIF3IF3F_swigregister = _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_swigregister
itkThresholdSegmentationLevelSetImageFilterIF3IF3F_swigregister(itkThresholdSegmentationLevelSetImageFilterIF3IF3F)

def itkThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> "itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer":
    """itkThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

def itkThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(obj: 'itkLightObject') -> "itkThresholdSegmentationLevelSetImageFilterIF3IF3F *":
    """itkThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkThresholdSegmentationLevelSetImageFilterIF3IF3F"""
    return _itkThresholdSegmentationLevelSetImageFilterPython.itkThresholdSegmentationLevelSetImageFilterIF3IF3F_cast(obj)



