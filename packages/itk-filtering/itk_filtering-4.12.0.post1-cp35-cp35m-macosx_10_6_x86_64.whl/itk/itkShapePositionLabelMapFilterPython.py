# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapePositionLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkShapePositionLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkShapePositionLabelMapFilterPython')
    _itkShapePositionLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapePositionLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShapePositionLabelMapFilterPython
            return _itkShapePositionLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkShapePositionLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkShapePositionLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapePositionLabelMapFilterPython
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


import itkStatisticsLabelObjectPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkHistogramPython
import ITKCommonBasePython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSamplePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkAffineTransformPython
import itkCovariantVectorPython
import itkMatrixOffsetTransformBasePython
import itkPointPython
import itkOptimizerParametersPython
import itkVariableLengthVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkTransformBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkShapeLabelObjectPython
import itkImageRegionPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageSourceCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkImageToImageFilterCommonPython
import itkLabelMapFilterPython

def itkShapePositionLabelMapFilterLM3_New():
  return itkShapePositionLabelMapFilterLM3.New()


def itkShapePositionLabelMapFilterLM2_New():
  return itkShapePositionLabelMapFilterLM2.New()

class itkShapePositionLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkShapePositionLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapePositionLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkShapePositionLabelMapFilterLM2_Pointer"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapePositionLabelMapFilterLM2_Pointer":
        """Clone(itkShapePositionLabelMapFilterLM2 self) -> itkShapePositionLabelMapFilterLM2_Pointer"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_Clone(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapePositionLabelMapFilterLM2 self) -> unsigned int"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapePositionLabelMapFilterLM2 self, unsigned int const _arg)
        SetAttribute(itkShapePositionLabelMapFilterLM2 self, std::string const & s)
        """
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapePositionLabelMapFilterPython.delete_itkShapePositionLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkShapePositionLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkShapePositionLabelMapFilterLM2"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapePositionLabelMapFilterLM2 *":
        """GetPointer(itkShapePositionLabelMapFilterLM2 self) -> itkShapePositionLabelMapFilterLM2"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapePositionLabelMapFilterLM2

        Create a new object of the class itkShapePositionLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePositionLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePositionLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePositionLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapePositionLabelMapFilterLM2.Clone = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_Clone, None, itkShapePositionLabelMapFilterLM2)
itkShapePositionLabelMapFilterLM2.GetAttribute = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_GetAttribute, None, itkShapePositionLabelMapFilterLM2)
itkShapePositionLabelMapFilterLM2.SetAttribute = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_SetAttribute, None, itkShapePositionLabelMapFilterLM2)
itkShapePositionLabelMapFilterLM2.GetPointer = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_GetPointer, None, itkShapePositionLabelMapFilterLM2)
itkShapePositionLabelMapFilterLM2_swigregister = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_swigregister
itkShapePositionLabelMapFilterLM2_swigregister(itkShapePositionLabelMapFilterLM2)

def itkShapePositionLabelMapFilterLM2___New_orig__() -> "itkShapePositionLabelMapFilterLM2_Pointer":
    """itkShapePositionLabelMapFilterLM2___New_orig__() -> itkShapePositionLabelMapFilterLM2_Pointer"""
    return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2___New_orig__()

def itkShapePositionLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkShapePositionLabelMapFilterLM2 *":
    """itkShapePositionLabelMapFilterLM2_cast(itkLightObject obj) -> itkShapePositionLabelMapFilterLM2"""
    return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_cast(obj)

class itkShapePositionLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkShapePositionLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapePositionLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkShapePositionLabelMapFilterLM3_Pointer"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapePositionLabelMapFilterLM3_Pointer":
        """Clone(itkShapePositionLabelMapFilterLM3 self) -> itkShapePositionLabelMapFilterLM3_Pointer"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_Clone(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapePositionLabelMapFilterLM3 self) -> unsigned int"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapePositionLabelMapFilterLM3 self, unsigned int const _arg)
        SetAttribute(itkShapePositionLabelMapFilterLM3 self, std::string const & s)
        """
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapePositionLabelMapFilterPython.delete_itkShapePositionLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkShapePositionLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkShapePositionLabelMapFilterLM3"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapePositionLabelMapFilterLM3 *":
        """GetPointer(itkShapePositionLabelMapFilterLM3 self) -> itkShapePositionLabelMapFilterLM3"""
        return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapePositionLabelMapFilterLM3

        Create a new object of the class itkShapePositionLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePositionLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePositionLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePositionLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapePositionLabelMapFilterLM3.Clone = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_Clone, None, itkShapePositionLabelMapFilterLM3)
itkShapePositionLabelMapFilterLM3.GetAttribute = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_GetAttribute, None, itkShapePositionLabelMapFilterLM3)
itkShapePositionLabelMapFilterLM3.SetAttribute = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_SetAttribute, None, itkShapePositionLabelMapFilterLM3)
itkShapePositionLabelMapFilterLM3.GetPointer = new_instancemethod(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_GetPointer, None, itkShapePositionLabelMapFilterLM3)
itkShapePositionLabelMapFilterLM3_swigregister = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_swigregister
itkShapePositionLabelMapFilterLM3_swigregister(itkShapePositionLabelMapFilterLM3)

def itkShapePositionLabelMapFilterLM3___New_orig__() -> "itkShapePositionLabelMapFilterLM3_Pointer":
    """itkShapePositionLabelMapFilterLM3___New_orig__() -> itkShapePositionLabelMapFilterLM3_Pointer"""
    return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3___New_orig__()

def itkShapePositionLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkShapePositionLabelMapFilterLM3 *":
    """itkShapePositionLabelMapFilterLM3_cast(itkLightObject obj) -> itkShapePositionLabelMapFilterLM3"""
    return _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_cast(obj)



