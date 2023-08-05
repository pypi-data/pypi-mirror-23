# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelMapToBinaryImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLabelMapToBinaryImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLabelMapToBinaryImageFilterPython')
    _itkLabelMapToBinaryImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelMapToBinaryImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelMapToBinaryImageFilterPython
            return _itkLabelMapToBinaryImageFilterPython
        try:
            _mod = imp.load_module('_itkLabelMapToBinaryImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLabelMapToBinaryImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelMapToBinaryImageFilterPython
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


import itkImagePython
import stdcomplexPython
import pyBasePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import ITKLabelMapBasePython
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
import itkLabelMapFilterPython

def itkLabelMapToBinaryImageFilterLM3IUC3_New():
  return itkLabelMapToBinaryImageFilterLM3IUC3.New()


def itkLabelMapToBinaryImageFilterLM2IUC2_New():
  return itkLabelMapToBinaryImageFilterLM2IUC2.New()

class itkLabelMapToBinaryImageFilterLM2IUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IUC2):
    """Proxy of C++ itkLabelMapToBinaryImageFilterLM2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkLabelMapToBinaryImageFilterLM2IUC2_Pointer"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkLabelMapToBinaryImageFilterLM2IUC2 self) -> itkLabelMapToBinaryImageFilterLM2IUC2_Pointer"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_Clone(self)


    def SetBackgroundValue(self, _arg):
        """SetBackgroundValue(itkLabelMapToBinaryImageFilterLM2IUC2 self, unsigned char const _arg)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self):
        """GetBackgroundValue(itkLabelMapToBinaryImageFilterLM2IUC2 self) -> unsigned char"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetBackgroundValue(self)


    def SetForegroundValue(self, _arg):
        """SetForegroundValue(itkLabelMapToBinaryImageFilterLM2IUC2 self, unsigned char const _arg)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetForegroundValue(self, _arg)


    def GetForegroundValue(self):
        """GetForegroundValue(itkLabelMapToBinaryImageFilterLM2IUC2 self) -> unsigned char"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetForegroundValue(self)


    def SetBackgroundImage(self, input):
        """SetBackgroundImage(itkLabelMapToBinaryImageFilterLM2IUC2 self, itkImageUC2 input)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetBackgroundImage(self, input)


    def GetBackgroundImage(self):
        """GetBackgroundImage(itkLabelMapToBinaryImageFilterLM2IUC2 self) -> itkImageUC2"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetBackgroundImage(self)


    def SetInput1(self, input):
        """SetInput1(itkLabelMapToBinaryImageFilterLM2IUC2 self, itkLabelMap2 input)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetInput1(self, input)


    def SetInput2(self, input):
        """SetInput2(itkLabelMapToBinaryImageFilterLM2IUC2 self, itkImageUC2 input)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetInput2(self, input)

    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM2IUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkLabelMapToBinaryImageFilterLM2IUC2"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkLabelMapToBinaryImageFilterLM2IUC2 self) -> itkLabelMapToBinaryImageFilterLM2IUC2"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM2IUC2

        Create a new object of the class itkLabelMapToBinaryImageFilterLM2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToBinaryImageFilterLM2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToBinaryImageFilterLM2IUC2.Clone = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_Clone, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.SetBackgroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetBackgroundValue, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.GetBackgroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetBackgroundValue, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.SetForegroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetForegroundValue, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.GetForegroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetForegroundValue, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.SetBackgroundImage = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetBackgroundImage, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.GetBackgroundImage = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetBackgroundImage, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.SetInput1 = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetInput1, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.SetInput2 = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetInput2, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2.GetPointer = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetPointer, None, itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2_swigregister = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_swigregister
itkLabelMapToBinaryImageFilterLM2IUC2_swigregister(itkLabelMapToBinaryImageFilterLM2IUC2)

def itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__():
    """itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__() -> itkLabelMapToBinaryImageFilterLM2IUC2_Pointer"""
    return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__()

def itkLabelMapToBinaryImageFilterLM2IUC2_cast(obj):
    """itkLabelMapToBinaryImageFilterLM2IUC2_cast(itkLightObject obj) -> itkLabelMapToBinaryImageFilterLM2IUC2"""
    return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_cast(obj)

class itkLabelMapToBinaryImageFilterLM3IUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IUC3):
    """Proxy of C++ itkLabelMapToBinaryImageFilterLM3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkLabelMapToBinaryImageFilterLM3IUC3_Pointer"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkLabelMapToBinaryImageFilterLM3IUC3 self) -> itkLabelMapToBinaryImageFilterLM3IUC3_Pointer"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_Clone(self)


    def SetBackgroundValue(self, _arg):
        """SetBackgroundValue(itkLabelMapToBinaryImageFilterLM3IUC3 self, unsigned char const _arg)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetBackgroundValue(self, _arg)


    def GetBackgroundValue(self):
        """GetBackgroundValue(itkLabelMapToBinaryImageFilterLM3IUC3 self) -> unsigned char"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetBackgroundValue(self)


    def SetForegroundValue(self, _arg):
        """SetForegroundValue(itkLabelMapToBinaryImageFilterLM3IUC3 self, unsigned char const _arg)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetForegroundValue(self, _arg)


    def GetForegroundValue(self):
        """GetForegroundValue(itkLabelMapToBinaryImageFilterLM3IUC3 self) -> unsigned char"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetForegroundValue(self)


    def SetBackgroundImage(self, input):
        """SetBackgroundImage(itkLabelMapToBinaryImageFilterLM3IUC3 self, itkImageUC3 input)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetBackgroundImage(self, input)


    def GetBackgroundImage(self):
        """GetBackgroundImage(itkLabelMapToBinaryImageFilterLM3IUC3 self) -> itkImageUC3"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetBackgroundImage(self)


    def SetInput1(self, input):
        """SetInput1(itkLabelMapToBinaryImageFilterLM3IUC3 self, itkLabelMap3 input)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetInput1(self, input)


    def SetInput2(self, input):
        """SetInput2(itkLabelMapToBinaryImageFilterLM3IUC3 self, itkImageUC3 input)"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetInput2(self, input)

    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM3IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkLabelMapToBinaryImageFilterLM3IUC3"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkLabelMapToBinaryImageFilterLM3IUC3 self) -> itkLabelMapToBinaryImageFilterLM3IUC3"""
        return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM3IUC3

        Create a new object of the class itkLabelMapToBinaryImageFilterLM3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToBinaryImageFilterLM3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToBinaryImageFilterLM3IUC3.Clone = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_Clone, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.SetBackgroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetBackgroundValue, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.GetBackgroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetBackgroundValue, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.SetForegroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetForegroundValue, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.GetForegroundValue = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetForegroundValue, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.SetBackgroundImage = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetBackgroundImage, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.GetBackgroundImage = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetBackgroundImage, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.SetInput1 = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetInput1, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.SetInput2 = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetInput2, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3.GetPointer = new_instancemethod(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetPointer, None, itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3_swigregister = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_swigregister
itkLabelMapToBinaryImageFilterLM3IUC3_swigregister(itkLabelMapToBinaryImageFilterLM3IUC3)

def itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__():
    """itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__() -> itkLabelMapToBinaryImageFilterLM3IUC3_Pointer"""
    return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__()

def itkLabelMapToBinaryImageFilterLM3IUC3_cast(obj):
    """itkLabelMapToBinaryImageFilterLM3IUC3_cast(itkLightObject obj) -> itkLabelMapToBinaryImageFilterLM3IUC3"""
    return _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_cast(obj)



