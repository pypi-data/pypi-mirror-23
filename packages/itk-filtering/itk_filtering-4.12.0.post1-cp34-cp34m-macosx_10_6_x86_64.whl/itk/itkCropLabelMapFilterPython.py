# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCropLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkCropLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkCropLabelMapFilterPython')
    _itkCropLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCropLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCropLabelMapFilterPython
            return _itkCropLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkCropLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkCropLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCropLabelMapFilterPython
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


import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkChangeRegionLabelMapFilterPython
import itkInPlaceLabelMapFilterPython
import itkLabelMapFilterPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkStatisticsLabelObjectPython
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import ITKLabelMapBasePython
import itkImageSourcePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkImageToImageFilterCommonPython

def itkCropLabelMapFilterLM3_New():
  return itkCropLabelMapFilterLM3.New()


def itkCropLabelMapFilterLM2_New():
  return itkCropLabelMapFilterLM2.New()

class itkCropLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """Proxy of C++ itkCropLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCropLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkCropLabelMapFilterLM2_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCropLabelMapFilterLM2_Pointer":
        """Clone(itkCropLabelMapFilterLM2 self) -> itkCropLabelMapFilterLM2_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_Clone(self)


    def SetUpperBoundaryCropSize(self, _arg: 'itkSize2') -> "void":
        """SetUpperBoundaryCropSize(itkCropLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetUpperBoundaryCropSize(self, _arg)


    def GetUpperBoundaryCropSize(self) -> "itkSize2":
        """GetUpperBoundaryCropSize(itkCropLabelMapFilterLM2 self) -> itkSize2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetUpperBoundaryCropSize(self)


    def SetLowerBoundaryCropSize(self, _arg: 'itkSize2') -> "void":
        """SetLowerBoundaryCropSize(itkCropLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetLowerBoundaryCropSize(self, _arg)


    def GetLowerBoundaryCropSize(self) -> "itkSize2":
        """GetLowerBoundaryCropSize(itkCropLabelMapFilterLM2 self) -> itkSize2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetLowerBoundaryCropSize(self)


    def SetCropSize(self, size: 'itkSize2') -> "void":
        """SetCropSize(itkCropLabelMapFilterLM2 self, itkSize2 size)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetCropSize(self, size)

    __swig_destroy__ = _itkCropLabelMapFilterPython.delete_itkCropLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkCropLabelMapFilterLM2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkCropLabelMapFilterLM2 *":
        """GetPointer(itkCropLabelMapFilterLM2 self) -> itkCropLabelMapFilterLM2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCropLabelMapFilterLM2

        Create a new object of the class itkCropLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCropLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCropLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCropLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCropLabelMapFilterLM2.Clone = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_Clone, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.SetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.GetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.SetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.GetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.SetCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.GetPointer = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetPointer, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2_swigregister = _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_swigregister
itkCropLabelMapFilterLM2_swigregister(itkCropLabelMapFilterLM2)

def itkCropLabelMapFilterLM2___New_orig__() -> "itkCropLabelMapFilterLM2_Pointer":
    """itkCropLabelMapFilterLM2___New_orig__() -> itkCropLabelMapFilterLM2_Pointer"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2___New_orig__()

def itkCropLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM2 *":
    """itkCropLabelMapFilterLM2_cast(itkLightObject obj) -> itkCropLabelMapFilterLM2"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_cast(obj)

class itkCropLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """Proxy of C++ itkCropLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCropLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkCropLabelMapFilterLM3_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCropLabelMapFilterLM3_Pointer":
        """Clone(itkCropLabelMapFilterLM3 self) -> itkCropLabelMapFilterLM3_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_Clone(self)


    def SetUpperBoundaryCropSize(self, _arg: 'itkSize3') -> "void":
        """SetUpperBoundaryCropSize(itkCropLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetUpperBoundaryCropSize(self, _arg)


    def GetUpperBoundaryCropSize(self) -> "itkSize3":
        """GetUpperBoundaryCropSize(itkCropLabelMapFilterLM3 self) -> itkSize3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetUpperBoundaryCropSize(self)


    def SetLowerBoundaryCropSize(self, _arg: 'itkSize3') -> "void":
        """SetLowerBoundaryCropSize(itkCropLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetLowerBoundaryCropSize(self, _arg)


    def GetLowerBoundaryCropSize(self) -> "itkSize3":
        """GetLowerBoundaryCropSize(itkCropLabelMapFilterLM3 self) -> itkSize3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetLowerBoundaryCropSize(self)


    def SetCropSize(self, size: 'itkSize3') -> "void":
        """SetCropSize(itkCropLabelMapFilterLM3 self, itkSize3 size)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetCropSize(self, size)

    __swig_destroy__ = _itkCropLabelMapFilterPython.delete_itkCropLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkCropLabelMapFilterLM3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkCropLabelMapFilterLM3 *":
        """GetPointer(itkCropLabelMapFilterLM3 self) -> itkCropLabelMapFilterLM3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCropLabelMapFilterLM3

        Create a new object of the class itkCropLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCropLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCropLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCropLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCropLabelMapFilterLM3.Clone = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_Clone, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.SetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.GetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.SetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.GetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.SetCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.GetPointer = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetPointer, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3_swigregister = _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_swigregister
itkCropLabelMapFilterLM3_swigregister(itkCropLabelMapFilterLM3)

def itkCropLabelMapFilterLM3___New_orig__() -> "itkCropLabelMapFilterLM3_Pointer":
    """itkCropLabelMapFilterLM3___New_orig__() -> itkCropLabelMapFilterLM3_Pointer"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3___New_orig__()

def itkCropLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM3 *":
    """itkCropLabelMapFilterLM3_cast(itkLightObject obj) -> itkCropLabelMapFilterLM3"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_cast(obj)



