# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkStatisticsRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkStatisticsRelabelLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkStatisticsRelabelLabelMapFilterPython')
    _itkStatisticsRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkStatisticsRelabelLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkStatisticsRelabelLabelMapFilterPython
            return _itkStatisticsRelabelLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkStatisticsRelabelLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkStatisticsRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkStatisticsRelabelLabelMapFilterPython
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


import itkShapeRelabelLabelMapFilterPython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import pyBasePython
import itkImageSourceCommonPython
import ITKCommonBasePython
import itkImageSourcePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
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
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkArray2DPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkHistogramPython
import itkSamplePython
import itkLabelMapFilterPython

def itkStatisticsRelabelLabelMapFilterLM3_New():
  return itkStatisticsRelabelLabelMapFilterLM3.New()


def itkStatisticsRelabelLabelMapFilterLM2_New():
  return itkStatisticsRelabelLabelMapFilterLM2.New()

class itkStatisticsRelabelLabelMapFilterLM2(itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2):
    """Proxy of C++ itkStatisticsRelabelLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkStatisticsRelabelLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkStatisticsRelabelLabelMapFilterLM2_Pointer"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkStatisticsRelabelLabelMapFilterLM2_Pointer":
        """Clone(itkStatisticsRelabelLabelMapFilterLM2 self) -> itkStatisticsRelabelLabelMapFilterLM2_Pointer"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_Clone(self)

    __swig_destroy__ = _itkStatisticsRelabelLabelMapFilterPython.delete_itkStatisticsRelabelLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkStatisticsRelabelLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkStatisticsRelabelLabelMapFilterLM2"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkStatisticsRelabelLabelMapFilterLM2 *":
        """GetPointer(itkStatisticsRelabelLabelMapFilterLM2 self) -> itkStatisticsRelabelLabelMapFilterLM2"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkStatisticsRelabelLabelMapFilterLM2

        Create a new object of the class itkStatisticsRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsRelabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsRelabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsRelabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStatisticsRelabelLabelMapFilterLM2.Clone = new_instancemethod(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_Clone, None, itkStatisticsRelabelLabelMapFilterLM2)
itkStatisticsRelabelLabelMapFilterLM2.GetPointer = new_instancemethod(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_GetPointer, None, itkStatisticsRelabelLabelMapFilterLM2)
itkStatisticsRelabelLabelMapFilterLM2_swigregister = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_swigregister
itkStatisticsRelabelLabelMapFilterLM2_swigregister(itkStatisticsRelabelLabelMapFilterLM2)

def itkStatisticsRelabelLabelMapFilterLM2___New_orig__() -> "itkStatisticsRelabelLabelMapFilterLM2_Pointer":
    """itkStatisticsRelabelLabelMapFilterLM2___New_orig__() -> itkStatisticsRelabelLabelMapFilterLM2_Pointer"""
    return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2___New_orig__()

def itkStatisticsRelabelLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkStatisticsRelabelLabelMapFilterLM2 *":
    """itkStatisticsRelabelLabelMapFilterLM2_cast(itkLightObject obj) -> itkStatisticsRelabelLabelMapFilterLM2"""
    return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_cast(obj)

class itkStatisticsRelabelLabelMapFilterLM3(itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3):
    """Proxy of C++ itkStatisticsRelabelLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkStatisticsRelabelLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkStatisticsRelabelLabelMapFilterLM3_Pointer"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkStatisticsRelabelLabelMapFilterLM3_Pointer":
        """Clone(itkStatisticsRelabelLabelMapFilterLM3 self) -> itkStatisticsRelabelLabelMapFilterLM3_Pointer"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_Clone(self)

    __swig_destroy__ = _itkStatisticsRelabelLabelMapFilterPython.delete_itkStatisticsRelabelLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkStatisticsRelabelLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkStatisticsRelabelLabelMapFilterLM3"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkStatisticsRelabelLabelMapFilterLM3 *":
        """GetPointer(itkStatisticsRelabelLabelMapFilterLM3 self) -> itkStatisticsRelabelLabelMapFilterLM3"""
        return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkStatisticsRelabelLabelMapFilterLM3

        Create a new object of the class itkStatisticsRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsRelabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsRelabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsRelabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStatisticsRelabelLabelMapFilterLM3.Clone = new_instancemethod(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_Clone, None, itkStatisticsRelabelLabelMapFilterLM3)
itkStatisticsRelabelLabelMapFilterLM3.GetPointer = new_instancemethod(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_GetPointer, None, itkStatisticsRelabelLabelMapFilterLM3)
itkStatisticsRelabelLabelMapFilterLM3_swigregister = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_swigregister
itkStatisticsRelabelLabelMapFilterLM3_swigregister(itkStatisticsRelabelLabelMapFilterLM3)

def itkStatisticsRelabelLabelMapFilterLM3___New_orig__() -> "itkStatisticsRelabelLabelMapFilterLM3_Pointer":
    """itkStatisticsRelabelLabelMapFilterLM3___New_orig__() -> itkStatisticsRelabelLabelMapFilterLM3_Pointer"""
    return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3___New_orig__()

def itkStatisticsRelabelLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkStatisticsRelabelLabelMapFilterLM3 *":
    """itkStatisticsRelabelLabelMapFilterLM3_cast(itkLightObject obj) -> itkStatisticsRelabelLabelMapFilterLM3"""
    return _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_cast(obj)



