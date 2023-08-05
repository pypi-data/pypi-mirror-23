# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkChangeRegionLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkChangeRegionLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkChangeRegionLabelMapFilterPython')
    _itkChangeRegionLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkChangeRegionLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkChangeRegionLabelMapFilterPython
            return _itkChangeRegionLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkChangeRegionLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkChangeRegionLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkChangeRegionLabelMapFilterPython
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


import itkInPlaceLabelMapFilterPython
import ITKCommonBasePython
import pyBasePython
import itkLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkPointPython
import itkHistogramPython
import itkArrayPython
import itkSamplePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkSymmetricSecondRankTensorPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkImageRegionPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourceCommonPython

def itkChangeRegionLabelMapFilterLM3_New():
  return itkChangeRegionLabelMapFilterLM3.New()


def itkChangeRegionLabelMapFilterLM2_New():
  return itkChangeRegionLabelMapFilterLM2.New()

class itkChangeRegionLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkChangeRegionLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkChangeRegionLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkChangeRegionLabelMapFilterLM2_Pointer"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkChangeRegionLabelMapFilterLM2_Pointer":
        """Clone(itkChangeRegionLabelMapFilterLM2 self) -> itkChangeRegionLabelMapFilterLM2_Pointer"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_Clone(self)


    def SetRegion(self, _arg: 'itkImageRegion2') -> "void":
        """SetRegion(itkChangeRegionLabelMapFilterLM2 self, itkImageRegion2 _arg)"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_SetRegion(self, _arg)


    def GetRegion(self) -> "itkImageRegion2 const &":
        """GetRegion(itkChangeRegionLabelMapFilterLM2 self) -> itkImageRegion2"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_GetRegion(self)

    __swig_destroy__ = _itkChangeRegionLabelMapFilterPython.delete_itkChangeRegionLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkChangeRegionLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkChangeRegionLabelMapFilterLM2"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkChangeRegionLabelMapFilterLM2 *":
        """GetPointer(itkChangeRegionLabelMapFilterLM2 self) -> itkChangeRegionLabelMapFilterLM2"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkChangeRegionLabelMapFilterLM2

        Create a new object of the class itkChangeRegionLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeRegionLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkChangeRegionLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkChangeRegionLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkChangeRegionLabelMapFilterLM2.Clone = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_Clone, None, itkChangeRegionLabelMapFilterLM2)
itkChangeRegionLabelMapFilterLM2.SetRegion = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_SetRegion, None, itkChangeRegionLabelMapFilterLM2)
itkChangeRegionLabelMapFilterLM2.GetRegion = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_GetRegion, None, itkChangeRegionLabelMapFilterLM2)
itkChangeRegionLabelMapFilterLM2.GetPointer = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_GetPointer, None, itkChangeRegionLabelMapFilterLM2)
itkChangeRegionLabelMapFilterLM2_swigregister = _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_swigregister
itkChangeRegionLabelMapFilterLM2_swigregister(itkChangeRegionLabelMapFilterLM2)

def itkChangeRegionLabelMapFilterLM2___New_orig__() -> "itkChangeRegionLabelMapFilterLM2_Pointer":
    """itkChangeRegionLabelMapFilterLM2___New_orig__() -> itkChangeRegionLabelMapFilterLM2_Pointer"""
    return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2___New_orig__()

def itkChangeRegionLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkChangeRegionLabelMapFilterLM2 *":
    """itkChangeRegionLabelMapFilterLM2_cast(itkLightObject obj) -> itkChangeRegionLabelMapFilterLM2"""
    return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2_cast(obj)

class itkChangeRegionLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkChangeRegionLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkChangeRegionLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkChangeRegionLabelMapFilterLM3_Pointer"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkChangeRegionLabelMapFilterLM3_Pointer":
        """Clone(itkChangeRegionLabelMapFilterLM3 self) -> itkChangeRegionLabelMapFilterLM3_Pointer"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_Clone(self)


    def SetRegion(self, _arg: 'itkImageRegion3') -> "void":
        """SetRegion(itkChangeRegionLabelMapFilterLM3 self, itkImageRegion3 _arg)"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_SetRegion(self, _arg)


    def GetRegion(self) -> "itkImageRegion3 const &":
        """GetRegion(itkChangeRegionLabelMapFilterLM3 self) -> itkImageRegion3"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_GetRegion(self)

    __swig_destroy__ = _itkChangeRegionLabelMapFilterPython.delete_itkChangeRegionLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkChangeRegionLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkChangeRegionLabelMapFilterLM3"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkChangeRegionLabelMapFilterLM3 *":
        """GetPointer(itkChangeRegionLabelMapFilterLM3 self) -> itkChangeRegionLabelMapFilterLM3"""
        return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkChangeRegionLabelMapFilterLM3

        Create a new object of the class itkChangeRegionLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeRegionLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkChangeRegionLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkChangeRegionLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkChangeRegionLabelMapFilterLM3.Clone = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_Clone, None, itkChangeRegionLabelMapFilterLM3)
itkChangeRegionLabelMapFilterLM3.SetRegion = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_SetRegion, None, itkChangeRegionLabelMapFilterLM3)
itkChangeRegionLabelMapFilterLM3.GetRegion = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_GetRegion, None, itkChangeRegionLabelMapFilterLM3)
itkChangeRegionLabelMapFilterLM3.GetPointer = new_instancemethod(_itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_GetPointer, None, itkChangeRegionLabelMapFilterLM3)
itkChangeRegionLabelMapFilterLM3_swigregister = _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_swigregister
itkChangeRegionLabelMapFilterLM3_swigregister(itkChangeRegionLabelMapFilterLM3)

def itkChangeRegionLabelMapFilterLM3___New_orig__() -> "itkChangeRegionLabelMapFilterLM3_Pointer":
    """itkChangeRegionLabelMapFilterLM3___New_orig__() -> itkChangeRegionLabelMapFilterLM3_Pointer"""
    return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3___New_orig__()

def itkChangeRegionLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkChangeRegionLabelMapFilterLM3 *":
    """itkChangeRegionLabelMapFilterLM3_cast(itkLightObject obj) -> itkChangeRegionLabelMapFilterLM3"""
    return _itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3_cast(obj)



