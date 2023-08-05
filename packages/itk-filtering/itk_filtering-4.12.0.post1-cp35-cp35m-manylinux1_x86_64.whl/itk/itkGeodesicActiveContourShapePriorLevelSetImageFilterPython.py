# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython')
    _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython
            return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython
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


import itkShapePriorSegmentationLevelSetImageFilterPython
import itkShapePriorMAPCostFunctionBasePython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython
import ITKFastMarchingBasePython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkMatrixPython
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
import itkFastMarchingStoppingCriterionBasePython
import itkNodePairPython
import itkLevelSetNodePython
import ITKCostFunctionsPython
import itkOptimizerParametersPython
import vnl_least_squares_functionPython
import itkArray2DPython
import vnl_cost_functionPython
import vnl_unary_functionPython
import itkCostFunctionPython
import ITKOptimizersBasePython
import itkSegmentationLevelSetImageFilterPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkFiniteDifferenceFunctionPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython

def itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_New():
  return itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.New()


def itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_New():
  return itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.New()

class itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F(itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F):
    """Proxy of C++ itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Pointer":
        """__New_orig__() -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Pointer":
        """Clone(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F self) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Clone(self)


    def SetDerivativeSigma(self, value: 'float') -> "void":
        """SetDerivativeSigma(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F self, float value)"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_SetDerivativeSigma(self, value)


    def GetDerivativeSigma(self) -> "float":
        """GetDerivativeSigma(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_GetDerivativeSigma(self)

    __swig_destroy__ = _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.delete_itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F

    def cast(obj: 'itkLightObject') -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F *":
        """cast(itkLightObject obj) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F *":
        """GetPointer(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F self) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F

        Create a new object of the class itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Clone, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.SetDerivativeSigma = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_SetDerivativeSigma, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.GetDerivativeSigma = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_GetDerivativeSigma, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F.GetPointer = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_GetPointer, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_swigregister = _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_swigregister
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_swigregister(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F)

def itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F___New_orig__() -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Pointer":
    """itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F___New_orig__() -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F___New_orig__()

def itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_cast(obj: 'itkLightObject') -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F *":
    """itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F"""
    return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F_cast(obj)

class itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F(itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F):
    """Proxy of C++ itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Pointer":
        """__New_orig__() -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Pointer":
        """Clone(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F self) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Clone(self)


    def SetDerivativeSigma(self, value: 'float') -> "void":
        """SetDerivativeSigma(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F self, float value)"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_SetDerivativeSigma(self, value)


    def GetDerivativeSigma(self) -> "float":
        """GetDerivativeSigma(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_GetDerivativeSigma(self)

    __swig_destroy__ = _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.delete_itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F

    def cast(obj: 'itkLightObject') -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F *":
        """cast(itkLightObject obj) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F *":
        """GetPointer(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F self) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F"""
        return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F

        Create a new object of the class itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Clone, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.SetDerivativeSigma = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_SetDerivativeSigma, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.GetDerivativeSigma = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_GetDerivativeSigma, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F.GetPointer = new_instancemethod(_itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_GetPointer, None, itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F)
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_swigregister = _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_swigregister
itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_swigregister(itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F)

def itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F___New_orig__() -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Pointer":
    """itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F___New_orig__() -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F___New_orig__()

def itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_cast(obj: 'itkLightObject') -> "itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F *":
    """itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F"""
    return _itkGeodesicActiveContourShapePriorLevelSetImageFilterPython.itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F_cast(obj)



