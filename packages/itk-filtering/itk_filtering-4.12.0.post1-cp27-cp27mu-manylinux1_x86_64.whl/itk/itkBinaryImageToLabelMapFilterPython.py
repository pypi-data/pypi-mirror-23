# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryImageToLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinaryImageToLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinaryImageToLabelMapFilterPython')
    _itkBinaryImageToLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryImageToLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryImageToLabelMapFilterPython
            return _itkBinaryImageToLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkBinaryImageToLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinaryImageToLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryImageToLabelMapFilterPython
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


import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import ITKLabelMapBasePython
import itkImagePython
import stdcomplexPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
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
import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython

def itkBinaryImageToLabelMapFilterIUC3LM3_New():
  return itkBinaryImageToLabelMapFilterIUC3LM3.New()


def itkBinaryImageToLabelMapFilterIUC2LM2_New():
  return itkBinaryImageToLabelMapFilterIUC2LM2.New()

class itkBinaryImageToLabelMapFilterIUC2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    """Proxy of C++ itkBinaryImageToLabelMapFilterIUC2LM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinaryImageToLabelMapFilterIUC2LM2_Pointer"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinaryImageToLabelMapFilterIUC2LM2 self) -> itkBinaryImageToLabelMapFilterIUC2LM2_Pointer"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_Clone(self)


    def SetFullyConnected(self, _arg):
        """SetFullyConnected(itkBinaryImageToLabelMapFilterIUC2LM2 self, bool const _arg)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SetFullyConnected(self, _arg)


    def GetFullyConnected(self):
        """GetFullyConnected(itkBinaryImageToLabelMapFilterIUC2LM2 self) -> bool const &"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetFullyConnected(self)


    def FullyConnectedOn(self):
        """FullyConnectedOn(itkBinaryImageToLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_FullyConnectedOn(self)


    def FullyConnectedOff(self):
        """FullyConnectedOff(itkBinaryImageToLabelMapFilterIUC2LM2 self)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_FullyConnectedOff(self)


    def GetNumberOfObjects(self):
        """GetNumberOfObjects(itkBinaryImageToLabelMapFilterIUC2LM2 self) -> unsigned long const &"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetNumberOfObjects(self)


    def SetOutputBackgroundValue(self, _arg):
        """SetOutputBackgroundValue(itkBinaryImageToLabelMapFilterIUC2LM2 self, unsigned long const _arg)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SetOutputBackgroundValue(self, _arg)


    def GetOutputBackgroundValue(self):
        """GetOutputBackgroundValue(itkBinaryImageToLabelMapFilterIUC2LM2 self) -> unsigned long"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetOutputBackgroundValue(self)


    def SetInputForegroundValue(self, _arg):
        """SetInputForegroundValue(itkBinaryImageToLabelMapFilterIUC2LM2 self, unsigned char const _arg)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SetInputForegroundValue(self, _arg)


    def GetInputForegroundValue(self):
        """GetInputForegroundValue(itkBinaryImageToLabelMapFilterIUC2LM2 self) -> unsigned char"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetInputForegroundValue(self)

    SameDimension = _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SameDimension
    __swig_destroy__ = _itkBinaryImageToLabelMapFilterPython.delete_itkBinaryImageToLabelMapFilterIUC2LM2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinaryImageToLabelMapFilterIUC2LM2"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinaryImageToLabelMapFilterIUC2LM2 self) -> itkBinaryImageToLabelMapFilterIUC2LM2"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryImageToLabelMapFilterIUC2LM2

        Create a new object of the class itkBinaryImageToLabelMapFilterIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToLabelMapFilterIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToLabelMapFilterIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToLabelMapFilterIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryImageToLabelMapFilterIUC2LM2.Clone = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_Clone, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.SetFullyConnected = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SetFullyConnected, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.GetFullyConnected = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetFullyConnected, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.FullyConnectedOn = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_FullyConnectedOn, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.FullyConnectedOff = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_FullyConnectedOff, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.GetNumberOfObjects = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetNumberOfObjects, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.SetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SetOutputBackgroundValue, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.GetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetOutputBackgroundValue, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.SetInputForegroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_SetInputForegroundValue, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.GetInputForegroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetInputForegroundValue, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2.GetPointer = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_GetPointer, None, itkBinaryImageToLabelMapFilterIUC2LM2)
itkBinaryImageToLabelMapFilterIUC2LM2_swigregister = _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_swigregister
itkBinaryImageToLabelMapFilterIUC2LM2_swigregister(itkBinaryImageToLabelMapFilterIUC2LM2)

def itkBinaryImageToLabelMapFilterIUC2LM2___New_orig__():
    """itkBinaryImageToLabelMapFilterIUC2LM2___New_orig__() -> itkBinaryImageToLabelMapFilterIUC2LM2_Pointer"""
    return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2___New_orig__()

def itkBinaryImageToLabelMapFilterIUC2LM2_cast(obj):
    """itkBinaryImageToLabelMapFilterIUC2LM2_cast(itkLightObject obj) -> itkBinaryImageToLabelMapFilterIUC2LM2"""
    return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC2LM2_cast(obj)

class itkBinaryImageToLabelMapFilterIUC3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    """Proxy of C++ itkBinaryImageToLabelMapFilterIUC3LM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinaryImageToLabelMapFilterIUC3LM3_Pointer"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinaryImageToLabelMapFilterIUC3LM3 self) -> itkBinaryImageToLabelMapFilterIUC3LM3_Pointer"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_Clone(self)


    def SetFullyConnected(self, _arg):
        """SetFullyConnected(itkBinaryImageToLabelMapFilterIUC3LM3 self, bool const _arg)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SetFullyConnected(self, _arg)


    def GetFullyConnected(self):
        """GetFullyConnected(itkBinaryImageToLabelMapFilterIUC3LM3 self) -> bool const &"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetFullyConnected(self)


    def FullyConnectedOn(self):
        """FullyConnectedOn(itkBinaryImageToLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_FullyConnectedOn(self)


    def FullyConnectedOff(self):
        """FullyConnectedOff(itkBinaryImageToLabelMapFilterIUC3LM3 self)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_FullyConnectedOff(self)


    def GetNumberOfObjects(self):
        """GetNumberOfObjects(itkBinaryImageToLabelMapFilterIUC3LM3 self) -> unsigned long const &"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetNumberOfObjects(self)


    def SetOutputBackgroundValue(self, _arg):
        """SetOutputBackgroundValue(itkBinaryImageToLabelMapFilterIUC3LM3 self, unsigned long const _arg)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SetOutputBackgroundValue(self, _arg)


    def GetOutputBackgroundValue(self):
        """GetOutputBackgroundValue(itkBinaryImageToLabelMapFilterIUC3LM3 self) -> unsigned long"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetOutputBackgroundValue(self)


    def SetInputForegroundValue(self, _arg):
        """SetInputForegroundValue(itkBinaryImageToLabelMapFilterIUC3LM3 self, unsigned char const _arg)"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SetInputForegroundValue(self, _arg)


    def GetInputForegroundValue(self):
        """GetInputForegroundValue(itkBinaryImageToLabelMapFilterIUC3LM3 self) -> unsigned char"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetInputForegroundValue(self)

    SameDimension = _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SameDimension
    __swig_destroy__ = _itkBinaryImageToLabelMapFilterPython.delete_itkBinaryImageToLabelMapFilterIUC3LM3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinaryImageToLabelMapFilterIUC3LM3"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinaryImageToLabelMapFilterIUC3LM3 self) -> itkBinaryImageToLabelMapFilterIUC3LM3"""
        return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryImageToLabelMapFilterIUC3LM3

        Create a new object of the class itkBinaryImageToLabelMapFilterIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToLabelMapFilterIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToLabelMapFilterIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToLabelMapFilterIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryImageToLabelMapFilterIUC3LM3.Clone = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_Clone, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.SetFullyConnected = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SetFullyConnected, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.GetFullyConnected = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetFullyConnected, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.FullyConnectedOn = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_FullyConnectedOn, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.FullyConnectedOff = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_FullyConnectedOff, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.GetNumberOfObjects = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetNumberOfObjects, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.SetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SetOutputBackgroundValue, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.GetOutputBackgroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetOutputBackgroundValue, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.SetInputForegroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_SetInputForegroundValue, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.GetInputForegroundValue = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetInputForegroundValue, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3.GetPointer = new_instancemethod(_itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_GetPointer, None, itkBinaryImageToLabelMapFilterIUC3LM3)
itkBinaryImageToLabelMapFilterIUC3LM3_swigregister = _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_swigregister
itkBinaryImageToLabelMapFilterIUC3LM3_swigregister(itkBinaryImageToLabelMapFilterIUC3LM3)

def itkBinaryImageToLabelMapFilterIUC3LM3___New_orig__():
    """itkBinaryImageToLabelMapFilterIUC3LM3___New_orig__() -> itkBinaryImageToLabelMapFilterIUC3LM3_Pointer"""
    return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3___New_orig__()

def itkBinaryImageToLabelMapFilterIUC3LM3_cast(obj):
    """itkBinaryImageToLabelMapFilterIUC3LM3_cast(itkLightObject obj) -> itkBinaryImageToLabelMapFilterIUC3LM3"""
    return _itkBinaryImageToLabelMapFilterPython.itkBinaryImageToLabelMapFilterIUC3LM3_cast(obj)



