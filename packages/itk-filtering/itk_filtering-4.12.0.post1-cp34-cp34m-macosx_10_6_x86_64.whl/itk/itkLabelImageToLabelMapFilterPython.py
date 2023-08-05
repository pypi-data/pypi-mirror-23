# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelImageToLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLabelImageToLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLabelImageToLabelMapFilterPython')
    _itkLabelImageToLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelImageToLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelImageToLabelMapFilterPython
            return _itkLabelImageToLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkLabelImageToLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLabelImageToLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelImageToLabelMapFilterPython
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
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKLabelMapBasePython
import itkImageSourcePython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkTransformBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython

def itkLabelImageToLabelMapFilterIUC3LM3_New():
  return itkLabelImageToLabelMapFilterIUC3LM3.New()


def itkLabelImageToLabelMapFilterIUC2LM2_New():
  return itkLabelImageToLabelMapFilterIUC2LM2.New()

class itkLabelImageToLabelMapFilterIUC2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    """Proxy of C++ itkLabelImageToLabelMapFilterIUC2LM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageToLabelMapFilterIUC2LM2_Pointer":
        """__New_orig__() -> itkLabelImageToLabelMapFilterIUC2LM2_Pointer"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageToLabelMapFilterIUC2LM2_Pointer":
        """Clone(itkLabelImageToLabelMapFilterIUC2LM2 self) -> itkLabelImageToLabelMapFilterIUC2LM2_Pointer"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_Clone(self)


    def SetBackgroundValue(self, _arg: 'unsigned long const') -> "void":
        """SetBackgroundValue(itkLabelImageToLabelMapFilterIUC2LM2 self, unsigned long const _arg)"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "unsigned long":
        """GetBackgroundValue(itkLabelImageToLabelMapFilterIUC2LM2 self) -> unsigned long"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_GetBackgroundValue(self)

    SameDimensionCheck = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_SameDimensionCheck
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkLabelImageToLabelMapFilterIUC2LM2

    def cast(obj: 'itkLightObject') -> "itkLabelImageToLabelMapFilterIUC2LM2 *":
        """cast(itkLightObject obj) -> itkLabelImageToLabelMapFilterIUC2LM2"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelImageToLabelMapFilterIUC2LM2 *":
        """GetPointer(itkLabelImageToLabelMapFilterIUC2LM2 self) -> itkLabelImageToLabelMapFilterIUC2LM2"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelImageToLabelMapFilterIUC2LM2

        Create a new object of the class itkLabelImageToLabelMapFilterIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToLabelMapFilterIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToLabelMapFilterIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToLabelMapFilterIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageToLabelMapFilterIUC2LM2.Clone = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_Clone, None, itkLabelImageToLabelMapFilterIUC2LM2)
itkLabelImageToLabelMapFilterIUC2LM2.SetBackgroundValue = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_SetBackgroundValue, None, itkLabelImageToLabelMapFilterIUC2LM2)
itkLabelImageToLabelMapFilterIUC2LM2.GetBackgroundValue = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_GetBackgroundValue, None, itkLabelImageToLabelMapFilterIUC2LM2)
itkLabelImageToLabelMapFilterIUC2LM2.GetPointer = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_GetPointer, None, itkLabelImageToLabelMapFilterIUC2LM2)
itkLabelImageToLabelMapFilterIUC2LM2_swigregister = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_swigregister
itkLabelImageToLabelMapFilterIUC2LM2_swigregister(itkLabelImageToLabelMapFilterIUC2LM2)

def itkLabelImageToLabelMapFilterIUC2LM2___New_orig__() -> "itkLabelImageToLabelMapFilterIUC2LM2_Pointer":
    """itkLabelImageToLabelMapFilterIUC2LM2___New_orig__() -> itkLabelImageToLabelMapFilterIUC2LM2_Pointer"""
    return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2___New_orig__()

def itkLabelImageToLabelMapFilterIUC2LM2_cast(obj: 'itkLightObject') -> "itkLabelImageToLabelMapFilterIUC2LM2 *":
    """itkLabelImageToLabelMapFilterIUC2LM2_cast(itkLightObject obj) -> itkLabelImageToLabelMapFilterIUC2LM2"""
    return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_cast(obj)

class itkLabelImageToLabelMapFilterIUC3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    """Proxy of C++ itkLabelImageToLabelMapFilterIUC3LM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageToLabelMapFilterIUC3LM3_Pointer":
        """__New_orig__() -> itkLabelImageToLabelMapFilterIUC3LM3_Pointer"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageToLabelMapFilterIUC3LM3_Pointer":
        """Clone(itkLabelImageToLabelMapFilterIUC3LM3 self) -> itkLabelImageToLabelMapFilterIUC3LM3_Pointer"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_Clone(self)


    def SetBackgroundValue(self, _arg: 'unsigned long const') -> "void":
        """SetBackgroundValue(itkLabelImageToLabelMapFilterIUC3LM3 self, unsigned long const _arg)"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self) -> "unsigned long":
        """GetBackgroundValue(itkLabelImageToLabelMapFilterIUC3LM3 self) -> unsigned long"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_GetBackgroundValue(self)

    SameDimensionCheck = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_SameDimensionCheck
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkLabelImageToLabelMapFilterIUC3LM3

    def cast(obj: 'itkLightObject') -> "itkLabelImageToLabelMapFilterIUC3LM3 *":
        """cast(itkLightObject obj) -> itkLabelImageToLabelMapFilterIUC3LM3"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelImageToLabelMapFilterIUC3LM3 *":
        """GetPointer(itkLabelImageToLabelMapFilterIUC3LM3 self) -> itkLabelImageToLabelMapFilterIUC3LM3"""
        return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelImageToLabelMapFilterIUC3LM3

        Create a new object of the class itkLabelImageToLabelMapFilterIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToLabelMapFilterIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToLabelMapFilterIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToLabelMapFilterIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageToLabelMapFilterIUC3LM3.Clone = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_Clone, None, itkLabelImageToLabelMapFilterIUC3LM3)
itkLabelImageToLabelMapFilterIUC3LM3.SetBackgroundValue = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_SetBackgroundValue, None, itkLabelImageToLabelMapFilterIUC3LM3)
itkLabelImageToLabelMapFilterIUC3LM3.GetBackgroundValue = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_GetBackgroundValue, None, itkLabelImageToLabelMapFilterIUC3LM3)
itkLabelImageToLabelMapFilterIUC3LM3.GetPointer = new_instancemethod(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_GetPointer, None, itkLabelImageToLabelMapFilterIUC3LM3)
itkLabelImageToLabelMapFilterIUC3LM3_swigregister = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_swigregister
itkLabelImageToLabelMapFilterIUC3LM3_swigregister(itkLabelImageToLabelMapFilterIUC3LM3)

def itkLabelImageToLabelMapFilterIUC3LM3___New_orig__() -> "itkLabelImageToLabelMapFilterIUC3LM3_Pointer":
    """itkLabelImageToLabelMapFilterIUC3LM3___New_orig__() -> itkLabelImageToLabelMapFilterIUC3LM3_Pointer"""
    return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3___New_orig__()

def itkLabelImageToLabelMapFilterIUC3LM3_cast(obj: 'itkLightObject') -> "itkLabelImageToLabelMapFilterIUC3LM3 *":
    """itkLabelImageToLabelMapFilterIUC3LM3_cast(itkLightObject obj) -> itkLabelImageToLabelMapFilterIUC3LM3"""
    return _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_cast(obj)



