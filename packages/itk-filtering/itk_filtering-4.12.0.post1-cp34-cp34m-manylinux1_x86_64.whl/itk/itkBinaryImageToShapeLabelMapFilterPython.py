# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryImageToShapeLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinaryImageToShapeLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinaryImageToShapeLabelMapFilterPython')
    _itkBinaryImageToShapeLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryImageToShapeLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryImageToShapeLabelMapFilterPython
            return _itkBinaryImageToShapeLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkBinaryImageToShapeLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinaryImageToShapeLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryImageToShapeLabelMapFilterPython
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
import ITKLabelMapBasePython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkOptimizerParametersPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkArrayPython
import itkCovariantVectorPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkPointPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkLabelObjectPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkLabelObjectLinePython
import itkImageRegionPython
import itkHistogramPython
import itkSamplePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkImageSourceCommonPython

def itkBinaryImageToShapeLabelMapFilterIUC3LM3_New():
  return itkBinaryImageToShapeLabelMapFilterIUC3LM3.New()


def itkBinaryImageToShapeLabelMapFilterIUC2LM2_New():
  return itkBinaryImageToShapeLabelMapFilterIUC2LM2.New()

class itkBinaryImageToShapeLabelMapFilterIUC2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    """Proxy of C++ itkBinaryImageToShapeLabelMapFilterIUC2LM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryImageToShapeLabelMapFilterIUC2LM2_Pointer":
        """__New_orig__() -> itkBinaryImageToShapeLabelMapFilterIUC2LM2_Pointer"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryImageToShapeLabelMapFilterIUC2LM2_Pointer":
        """Clone(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> itkBinaryImageToShapeLabelMapFilterIUC2LM2_Pointer"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_Clone(self)


    def SetFullyConnected(self, _arg: 'bool const') -> "void":
        """SetFullyConnected(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetFullyConnected(self, _arg)


    def GetFullyConnected(self) -> "bool const &":
        """GetFullyConnected(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetFullyConnected(self)


    def FullyConnectedOn(self) -> "void":
        """FullyConnectedOn(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_FullyConnectedOn(self)


    def FullyConnectedOff(self) -> "void":
        """FullyConnectedOff(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_FullyConnectedOff(self)

    InputEqualityComparableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_InputOStreamWritableCheck

    def SetOutputBackgroundValue(self, _arg: 'unsigned long const') -> "void":
        """SetOutputBackgroundValue(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self, unsigned long const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetOutputBackgroundValue(self, _arg)


    def GetOutputBackgroundValue(self) -> "unsigned long":
        """GetOutputBackgroundValue(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> unsigned long"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetOutputBackgroundValue(self)


    def SetInputForegroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetInputForegroundValue(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self, unsigned char const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetInputForegroundValue(self, _arg)


    def GetInputForegroundValue(self) -> "unsigned char":
        """GetInputForegroundValue(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> unsigned char"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetInputForegroundValue(self)


    def SetComputeFeretDiameter(self, _arg: 'bool const') -> "void":
        """SetComputeFeretDiameter(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputeFeretDiameter(self, _arg)


    def GetComputeFeretDiameter(self) -> "bool const &":
        """GetComputeFeretDiameter(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputeFeretDiameter(self)


    def ComputeFeretDiameterOn(self) -> "void":
        """ComputeFeretDiameterOn(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOn(self)


    def ComputeFeretDiameterOff(self) -> "void":
        """ComputeFeretDiameterOff(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOff(self)


    def SetComputePerimeter(self, _arg: 'bool const') -> "void":
        """SetComputePerimeter(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputePerimeter(self, _arg)


    def GetComputePerimeter(self) -> "bool const &":
        """GetComputePerimeter(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputePerimeter(self)


    def ComputePerimeterOn(self) -> "void":
        """ComputePerimeterOn(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOn(self)


    def ComputePerimeterOff(self) -> "void":
        """ComputePerimeterOff(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOff(self)

    __swig_destroy__ = _itkBinaryImageToShapeLabelMapFilterPython.delete_itkBinaryImageToShapeLabelMapFilterIUC2LM2

    def cast(obj: 'itkLightObject') -> "itkBinaryImageToShapeLabelMapFilterIUC2LM2 *":
        """cast(itkLightObject obj) -> itkBinaryImageToShapeLabelMapFilterIUC2LM2"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryImageToShapeLabelMapFilterIUC2LM2 *":
        """GetPointer(itkBinaryImageToShapeLabelMapFilterIUC2LM2 self) -> itkBinaryImageToShapeLabelMapFilterIUC2LM2"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryImageToShapeLabelMapFilterIUC2LM2

        Create a new object of the class itkBinaryImageToShapeLabelMapFilterIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToShapeLabelMapFilterIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToShapeLabelMapFilterIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToShapeLabelMapFilterIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryImageToShapeLabelMapFilterIUC2LM2.Clone = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_Clone, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.SetFullyConnected = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetFullyConnected, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.GetFullyConnected = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetFullyConnected, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.FullyConnectedOn = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_FullyConnectedOn, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.FullyConnectedOff = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_FullyConnectedOff, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.SetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetOutputBackgroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.GetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetOutputBackgroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.SetInputForegroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetInputForegroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.GetInputForegroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetInputForegroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.SetComputeFeretDiameter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputeFeretDiameter, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.GetComputeFeretDiameter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputeFeretDiameter, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.ComputeFeretDiameterOn = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOn, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.ComputeFeretDiameterOff = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOff, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.SetComputePerimeter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputePerimeter, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.GetComputePerimeter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputePerimeter, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.ComputePerimeterOn = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOn, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.ComputePerimeterOff = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOff, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2.GetPointer = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetPointer, None, itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2_swigregister = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_swigregister
itkBinaryImageToShapeLabelMapFilterIUC2LM2_swigregister(itkBinaryImageToShapeLabelMapFilterIUC2LM2)

def itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__() -> "itkBinaryImageToShapeLabelMapFilterIUC2LM2_Pointer":
    """itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__() -> itkBinaryImageToShapeLabelMapFilterIUC2LM2_Pointer"""
    return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__()

def itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast(obj: 'itkLightObject') -> "itkBinaryImageToShapeLabelMapFilterIUC2LM2 *":
    """itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast(itkLightObject obj) -> itkBinaryImageToShapeLabelMapFilterIUC2LM2"""
    return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast(obj)

class itkBinaryImageToShapeLabelMapFilterIUC3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    """Proxy of C++ itkBinaryImageToShapeLabelMapFilterIUC3LM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryImageToShapeLabelMapFilterIUC3LM3_Pointer":
        """__New_orig__() -> itkBinaryImageToShapeLabelMapFilterIUC3LM3_Pointer"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryImageToShapeLabelMapFilterIUC3LM3_Pointer":
        """Clone(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> itkBinaryImageToShapeLabelMapFilterIUC3LM3_Pointer"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_Clone(self)


    def SetFullyConnected(self, _arg: 'bool const') -> "void":
        """SetFullyConnected(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetFullyConnected(self, _arg)


    def GetFullyConnected(self) -> "bool const &":
        """GetFullyConnected(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetFullyConnected(self)


    def FullyConnectedOn(self) -> "void":
        """FullyConnectedOn(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_FullyConnectedOn(self)


    def FullyConnectedOff(self) -> "void":
        """FullyConnectedOff(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_FullyConnectedOff(self)

    InputEqualityComparableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_InputEqualityComparableCheck
    IntConvertibleToInputCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_IntConvertibleToInputCheck
    InputOStreamWritableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_InputOStreamWritableCheck

    def SetOutputBackgroundValue(self, _arg: 'unsigned long const') -> "void":
        """SetOutputBackgroundValue(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self, unsigned long const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetOutputBackgroundValue(self, _arg)


    def GetOutputBackgroundValue(self) -> "unsigned long":
        """GetOutputBackgroundValue(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> unsigned long"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetOutputBackgroundValue(self)


    def SetInputForegroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetInputForegroundValue(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self, unsigned char const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetInputForegroundValue(self, _arg)


    def GetInputForegroundValue(self) -> "unsigned char":
        """GetInputForegroundValue(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> unsigned char"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetInputForegroundValue(self)


    def SetComputeFeretDiameter(self, _arg: 'bool const') -> "void":
        """SetComputeFeretDiameter(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputeFeretDiameter(self, _arg)


    def GetComputeFeretDiameter(self) -> "bool const &":
        """GetComputeFeretDiameter(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputeFeretDiameter(self)


    def ComputeFeretDiameterOn(self) -> "void":
        """ComputeFeretDiameterOn(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOn(self)


    def ComputeFeretDiameterOff(self) -> "void":
        """ComputeFeretDiameterOff(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOff(self)


    def SetComputePerimeter(self, _arg: 'bool const') -> "void":
        """SetComputePerimeter(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputePerimeter(self, _arg)


    def GetComputePerimeter(self) -> "bool const &":
        """GetComputePerimeter(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputePerimeter(self)


    def ComputePerimeterOn(self) -> "void":
        """ComputePerimeterOn(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOn(self)


    def ComputePerimeterOff(self) -> "void":
        """ComputePerimeterOff(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOff(self)

    __swig_destroy__ = _itkBinaryImageToShapeLabelMapFilterPython.delete_itkBinaryImageToShapeLabelMapFilterIUC3LM3

    def cast(obj: 'itkLightObject') -> "itkBinaryImageToShapeLabelMapFilterIUC3LM3 *":
        """cast(itkLightObject obj) -> itkBinaryImageToShapeLabelMapFilterIUC3LM3"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryImageToShapeLabelMapFilterIUC3LM3 *":
        """GetPointer(itkBinaryImageToShapeLabelMapFilterIUC3LM3 self) -> itkBinaryImageToShapeLabelMapFilterIUC3LM3"""
        return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryImageToShapeLabelMapFilterIUC3LM3

        Create a new object of the class itkBinaryImageToShapeLabelMapFilterIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToShapeLabelMapFilterIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToShapeLabelMapFilterIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToShapeLabelMapFilterIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryImageToShapeLabelMapFilterIUC3LM3.Clone = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_Clone, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.SetFullyConnected = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetFullyConnected, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.GetFullyConnected = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetFullyConnected, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.FullyConnectedOn = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_FullyConnectedOn, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.FullyConnectedOff = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_FullyConnectedOff, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.SetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetOutputBackgroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.GetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetOutputBackgroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.SetInputForegroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetInputForegroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.GetInputForegroundValue = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetInputForegroundValue, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.SetComputeFeretDiameter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputeFeretDiameter, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.GetComputeFeretDiameter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputeFeretDiameter, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.ComputeFeretDiameterOn = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOn, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.ComputeFeretDiameterOff = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOff, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.SetComputePerimeter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputePerimeter, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.GetComputePerimeter = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputePerimeter, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.ComputePerimeterOn = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOn, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.ComputePerimeterOff = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOff, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3.GetPointer = new_instancemethod(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetPointer, None, itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3_swigregister = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_swigregister
itkBinaryImageToShapeLabelMapFilterIUC3LM3_swigregister(itkBinaryImageToShapeLabelMapFilterIUC3LM3)

def itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__() -> "itkBinaryImageToShapeLabelMapFilterIUC3LM3_Pointer":
    """itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__() -> itkBinaryImageToShapeLabelMapFilterIUC3LM3_Pointer"""
    return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__()

def itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast(obj: 'itkLightObject') -> "itkBinaryImageToShapeLabelMapFilterIUC3LM3 *":
    """itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast(itkLightObject obj) -> itkBinaryImageToShapeLabelMapFilterIUC3LM3"""
    return _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast(obj)



