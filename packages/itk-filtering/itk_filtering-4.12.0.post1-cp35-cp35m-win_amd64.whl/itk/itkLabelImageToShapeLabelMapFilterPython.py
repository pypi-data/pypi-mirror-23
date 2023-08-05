# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelImageToShapeLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLabelImageToShapeLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLabelImageToShapeLabelMapFilterPython')
    _itkLabelImageToShapeLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelImageToShapeLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelImageToShapeLabelMapFilterPython
            return _itkLabelImageToShapeLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkLabelImageToShapeLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLabelImageToShapeLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelImageToShapeLabelMapFilterPython
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


import ITKLabelMapBasePython
import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageSourcePython
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
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkStatisticsLabelObjectPython
import itkHistogramPython
import itkSamplePython
import itkArrayPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython

def itkLabelImageToShapeLabelMapFilterIUC3LM3_New():
  return itkLabelImageToShapeLabelMapFilterIUC3LM3.New()


def itkLabelImageToShapeLabelMapFilterIUC2LM2_New():
  return itkLabelImageToShapeLabelMapFilterIUC2LM2.New()

class itkLabelImageToShapeLabelMapFilterIUC2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    """Proxy of C++ itkLabelImageToShapeLabelMapFilterIUC2LM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageToShapeLabelMapFilterIUC2LM2_Pointer":
        """__New_orig__() -> itkLabelImageToShapeLabelMapFilterIUC2LM2_Pointer"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageToShapeLabelMapFilterIUC2LM2_Pointer":
        """Clone(itkLabelImageToShapeLabelMapFilterIUC2LM2 self) -> itkLabelImageToShapeLabelMapFilterIUC2LM2_Pointer"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_Clone(self)

    InputEqualityComparableCheck = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_InputOStreamWritableCheck

    def SetBackgroundValue(self, _arg: 'unsigned long const') -> "void":
        """SetBackgroundValue(itkLabelImageToShapeLabelMapFilterIUC2LM2 self, unsigned long const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "unsigned long":
        """GetBackgroundValue(itkLabelImageToShapeLabelMapFilterIUC2LM2 self) -> unsigned long"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetBackgroundValue(self)


    def SetComputeFeretDiameter(self, _arg: 'bool const') -> "void":
        """SetComputeFeretDiameter(itkLabelImageToShapeLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetComputeFeretDiameter(self, _arg)


    def GetComputeFeretDiameter(self) -> "bool const &":
        """GetComputeFeretDiameter(itkLabelImageToShapeLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetComputeFeretDiameter(self)


    def ComputeFeretDiameterOn(self) -> "void":
        """ComputeFeretDiameterOn(itkLabelImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOn(self)


    def ComputeFeretDiameterOff(self) -> "void":
        """ComputeFeretDiameterOff(itkLabelImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOff(self)


    def SetComputePerimeter(self, _arg: 'bool const') -> "void":
        """SetComputePerimeter(itkLabelImageToShapeLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetComputePerimeter(self, _arg)


    def GetComputePerimeter(self) -> "bool const &":
        """GetComputePerimeter(itkLabelImageToShapeLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetComputePerimeter(self)


    def ComputePerimeterOn(self) -> "void":
        """ComputePerimeterOn(itkLabelImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOn(self)


    def ComputePerimeterOff(self) -> "void":
        """ComputePerimeterOff(itkLabelImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOff(self)


    def SetComputeOrientedBoundingBox(self, _arg: 'bool const') -> "void":
        """SetComputeOrientedBoundingBox(itkLabelImageToShapeLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetComputeOrientedBoundingBox(self, _arg)


    def GetComputeOrientedBoundingBox(self) -> "bool const &":
        """GetComputeOrientedBoundingBox(itkLabelImageToShapeLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetComputeOrientedBoundingBox(self)


    def ComputeOrientedBoundingBoxOn(self) -> "void":
        """ComputeOrientedBoundingBoxOn(itkLabelImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeOrientedBoundingBoxOn(self)


    def ComputeOrientedBoundingBoxOff(self) -> "void":
        """ComputeOrientedBoundingBoxOff(itkLabelImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeOrientedBoundingBoxOff(self)

    __swig_destroy__ = _itkLabelImageToShapeLabelMapFilterPython.delete_itkLabelImageToShapeLabelMapFilterIUC2LM2

    def cast(obj: 'itkLightObject') -> "itkLabelImageToShapeLabelMapFilterIUC2LM2 *":
        """cast(itkLightObject obj) -> itkLabelImageToShapeLabelMapFilterIUC2LM2"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelImageToShapeLabelMapFilterIUC2LM2 *":
        """GetPointer(itkLabelImageToShapeLabelMapFilterIUC2LM2 self) -> itkLabelImageToShapeLabelMapFilterIUC2LM2"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelImageToShapeLabelMapFilterIUC2LM2

        Create a new object of the class itkLabelImageToShapeLabelMapFilterIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToShapeLabelMapFilterIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToShapeLabelMapFilterIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToShapeLabelMapFilterIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageToShapeLabelMapFilterIUC2LM2.Clone = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_Clone, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.SetBackgroundValue = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetBackgroundValue, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.GetBackgroundValue = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetBackgroundValue, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.SetComputeFeretDiameter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetComputeFeretDiameter, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.GetComputeFeretDiameter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetComputeFeretDiameter, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.ComputeFeretDiameterOn = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOn, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.ComputeFeretDiameterOff = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOff, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.SetComputePerimeter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetComputePerimeter, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.GetComputePerimeter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetComputePerimeter, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.ComputePerimeterOn = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOn, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.ComputePerimeterOff = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOff, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.SetComputeOrientedBoundingBox = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_SetComputeOrientedBoundingBox, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.GetComputeOrientedBoundingBox = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetComputeOrientedBoundingBox, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.ComputeOrientedBoundingBoxOn = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeOrientedBoundingBoxOn, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.ComputeOrientedBoundingBoxOff = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_ComputeOrientedBoundingBoxOff, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2.GetPointer = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_GetPointer, None, itkLabelImageToShapeLabelMapFilterIUC2LM2)
itkLabelImageToShapeLabelMapFilterIUC2LM2_swigregister = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_swigregister
itkLabelImageToShapeLabelMapFilterIUC2LM2_swigregister(itkLabelImageToShapeLabelMapFilterIUC2LM2)

def itkLabelImageToShapeLabelMapFilterIUC2LM2___New_orig__() -> "itkLabelImageToShapeLabelMapFilterIUC2LM2_Pointer":
    """itkLabelImageToShapeLabelMapFilterIUC2LM2___New_orig__() -> itkLabelImageToShapeLabelMapFilterIUC2LM2_Pointer"""
    return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2___New_orig__()

def itkLabelImageToShapeLabelMapFilterIUC2LM2_cast(obj: 'itkLightObject') -> "itkLabelImageToShapeLabelMapFilterIUC2LM2 *":
    """itkLabelImageToShapeLabelMapFilterIUC2LM2_cast(itkLightObject obj) -> itkLabelImageToShapeLabelMapFilterIUC2LM2"""
    return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC2LM2_cast(obj)

class itkLabelImageToShapeLabelMapFilterIUC3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    """Proxy of C++ itkLabelImageToShapeLabelMapFilterIUC3LM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageToShapeLabelMapFilterIUC3LM3_Pointer":
        """__New_orig__() -> itkLabelImageToShapeLabelMapFilterIUC3LM3_Pointer"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageToShapeLabelMapFilterIUC3LM3_Pointer":
        """Clone(itkLabelImageToShapeLabelMapFilterIUC3LM3 self) -> itkLabelImageToShapeLabelMapFilterIUC3LM3_Pointer"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_Clone(self)

    InputEqualityComparableCheck = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_InputOStreamWritableCheck

    def SetBackgroundValue(self, _arg: 'unsigned long const') -> "void":
        """SetBackgroundValue(itkLabelImageToShapeLabelMapFilterIUC3LM3 self, unsigned long const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "unsigned long":
        """GetBackgroundValue(itkLabelImageToShapeLabelMapFilterIUC3LM3 self) -> unsigned long"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetBackgroundValue(self)


    def SetComputeFeretDiameter(self, _arg: 'bool const') -> "void":
        """SetComputeFeretDiameter(itkLabelImageToShapeLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetComputeFeretDiameter(self, _arg)


    def GetComputeFeretDiameter(self) -> "bool const &":
        """GetComputeFeretDiameter(itkLabelImageToShapeLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetComputeFeretDiameter(self)


    def ComputeFeretDiameterOn(self) -> "void":
        """ComputeFeretDiameterOn(itkLabelImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOn(self)


    def ComputeFeretDiameterOff(self) -> "void":
        """ComputeFeretDiameterOff(itkLabelImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOff(self)


    def SetComputePerimeter(self, _arg: 'bool const') -> "void":
        """SetComputePerimeter(itkLabelImageToShapeLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetComputePerimeter(self, _arg)


    def GetComputePerimeter(self) -> "bool const &":
        """GetComputePerimeter(itkLabelImageToShapeLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetComputePerimeter(self)


    def ComputePerimeterOn(self) -> "void":
        """ComputePerimeterOn(itkLabelImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOn(self)


    def ComputePerimeterOff(self) -> "void":
        """ComputePerimeterOff(itkLabelImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOff(self)


    def SetComputeOrientedBoundingBox(self, _arg: 'bool const') -> "void":
        """SetComputeOrientedBoundingBox(itkLabelImageToShapeLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetComputeOrientedBoundingBox(self, _arg)


    def GetComputeOrientedBoundingBox(self) -> "bool const &":
        """GetComputeOrientedBoundingBox(itkLabelImageToShapeLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetComputeOrientedBoundingBox(self)


    def ComputeOrientedBoundingBoxOn(self) -> "void":
        """ComputeOrientedBoundingBoxOn(itkLabelImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeOrientedBoundingBoxOn(self)


    def ComputeOrientedBoundingBoxOff(self) -> "void":
        """ComputeOrientedBoundingBoxOff(itkLabelImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeOrientedBoundingBoxOff(self)

    __swig_destroy__ = _itkLabelImageToShapeLabelMapFilterPython.delete_itkLabelImageToShapeLabelMapFilterIUC3LM3

    def cast(obj: 'itkLightObject') -> "itkLabelImageToShapeLabelMapFilterIUC3LM3 *":
        """cast(itkLightObject obj) -> itkLabelImageToShapeLabelMapFilterIUC3LM3"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelImageToShapeLabelMapFilterIUC3LM3 *":
        """GetPointer(itkLabelImageToShapeLabelMapFilterIUC3LM3 self) -> itkLabelImageToShapeLabelMapFilterIUC3LM3"""
        return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelImageToShapeLabelMapFilterIUC3LM3

        Create a new object of the class itkLabelImageToShapeLabelMapFilterIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToShapeLabelMapFilterIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToShapeLabelMapFilterIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToShapeLabelMapFilterIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageToShapeLabelMapFilterIUC3LM3.Clone = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_Clone, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.SetBackgroundValue = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetBackgroundValue, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.GetBackgroundValue = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetBackgroundValue, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.SetComputeFeretDiameter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetComputeFeretDiameter, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.GetComputeFeretDiameter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetComputeFeretDiameter, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.ComputeFeretDiameterOn = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOn, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.ComputeFeretDiameterOff = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOff, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.SetComputePerimeter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetComputePerimeter, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.GetComputePerimeter = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetComputePerimeter, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.ComputePerimeterOn = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOn, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.ComputePerimeterOff = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOff, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.SetComputeOrientedBoundingBox = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_SetComputeOrientedBoundingBox, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.GetComputeOrientedBoundingBox = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetComputeOrientedBoundingBox, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.ComputeOrientedBoundingBoxOn = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeOrientedBoundingBoxOn, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.ComputeOrientedBoundingBoxOff = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_ComputeOrientedBoundingBoxOff, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3.GetPointer = new_instancemethod(_itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_GetPointer, None, itkLabelImageToShapeLabelMapFilterIUC3LM3)
itkLabelImageToShapeLabelMapFilterIUC3LM3_swigregister = _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_swigregister
itkLabelImageToShapeLabelMapFilterIUC3LM3_swigregister(itkLabelImageToShapeLabelMapFilterIUC3LM3)

def itkLabelImageToShapeLabelMapFilterIUC3LM3___New_orig__() -> "itkLabelImageToShapeLabelMapFilterIUC3LM3_Pointer":
    """itkLabelImageToShapeLabelMapFilterIUC3LM3___New_orig__() -> itkLabelImageToShapeLabelMapFilterIUC3LM3_Pointer"""
    return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3___New_orig__()

def itkLabelImageToShapeLabelMapFilterIUC3LM3_cast(obj: 'itkLightObject') -> "itkLabelImageToShapeLabelMapFilterIUC3LM3 *":
    """itkLabelImageToShapeLabelMapFilterIUC3LM3_cast(itkLightObject obj) -> itkLabelImageToShapeLabelMapFilterIUC3LM3"""
    return _itkLabelImageToShapeLabelMapFilterPython.itkLabelImageToShapeLabelMapFilterIUC3LM3_cast(obj)



