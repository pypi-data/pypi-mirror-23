# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapeRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkShapeRelabelLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkShapeRelabelLabelMapFilterPython')
    _itkShapeRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapeRelabelLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShapeRelabelLabelMapFilterPython
            return _itkShapeRelabelLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkShapeRelabelLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkShapeRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapeRelabelLabelMapFilterPython
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

def itkShapeRelabelLabelMapFilterLM3_New():
  return itkShapeRelabelLabelMapFilterLM3.New()


def itkShapeRelabelLabelMapFilterLM2_New():
  return itkShapeRelabelLabelMapFilterLM2.New()

class itkShapeRelabelLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkShapeRelabelLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeRelabelLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkShapeRelabelLabelMapFilterLM2_Pointer"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeRelabelLabelMapFilterLM2_Pointer":
        """Clone(itkShapeRelabelLabelMapFilterLM2 self) -> itkShapeRelabelLabelMapFilterLM2_Pointer"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeRelabelLabelMapFilterLM2 self, bool const _arg)"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkShapeRelabelLabelMapFilterLM2 self) -> bool const &"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeRelabelLabelMapFilterLM2 self)"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeRelabelLabelMapFilterLM2 self)"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeRelabelLabelMapFilterLM2 self) -> unsigned int"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeRelabelLabelMapFilterLM2 self, unsigned int const _arg)
        SetAttribute(itkShapeRelabelLabelMapFilterLM2 self, std::string const & s)
        """
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkShapeRelabelLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkShapeRelabelLabelMapFilterLM2"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeRelabelLabelMapFilterLM2 *":
        """GetPointer(itkShapeRelabelLabelMapFilterLM2 self) -> itkShapeRelabelLabelMapFilterLM2"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM2

        Create a new object of the class itkShapeRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeRelabelLabelMapFilterLM2.Clone = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_Clone, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.SetReverseOrdering = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetReverseOrdering, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.GetReverseOrdering = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetReverseOrdering, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.ReverseOrderingOn = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOn, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.ReverseOrderingOff = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOff, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.GetAttribute = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetAttribute, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.SetAttribute = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetAttribute, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2.GetPointer = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetPointer, None, itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2_swigregister = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_swigregister
itkShapeRelabelLabelMapFilterLM2_swigregister(itkShapeRelabelLabelMapFilterLM2)

def itkShapeRelabelLabelMapFilterLM2___New_orig__() -> "itkShapeRelabelLabelMapFilterLM2_Pointer":
    """itkShapeRelabelLabelMapFilterLM2___New_orig__() -> itkShapeRelabelLabelMapFilterLM2_Pointer"""
    return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2___New_orig__()

def itkShapeRelabelLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkShapeRelabelLabelMapFilterLM2 *":
    """itkShapeRelabelLabelMapFilterLM2_cast(itkLightObject obj) -> itkShapeRelabelLabelMapFilterLM2"""
    return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_cast(obj)

class itkShapeRelabelLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkShapeRelabelLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeRelabelLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkShapeRelabelLabelMapFilterLM3_Pointer"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeRelabelLabelMapFilterLM3_Pointer":
        """Clone(itkShapeRelabelLabelMapFilterLM3 self) -> itkShapeRelabelLabelMapFilterLM3_Pointer"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeRelabelLabelMapFilterLM3 self, bool const _arg)"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkShapeRelabelLabelMapFilterLM3 self) -> bool const &"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeRelabelLabelMapFilterLM3 self)"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeRelabelLabelMapFilterLM3 self)"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeRelabelLabelMapFilterLM3 self) -> unsigned int"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeRelabelLabelMapFilterLM3 self, unsigned int const _arg)
        SetAttribute(itkShapeRelabelLabelMapFilterLM3 self, std::string const & s)
        """
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkShapeRelabelLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkShapeRelabelLabelMapFilterLM3"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeRelabelLabelMapFilterLM3 *":
        """GetPointer(itkShapeRelabelLabelMapFilterLM3 self) -> itkShapeRelabelLabelMapFilterLM3"""
        return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM3

        Create a new object of the class itkShapeRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeRelabelLabelMapFilterLM3.Clone = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_Clone, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.SetReverseOrdering = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetReverseOrdering, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.GetReverseOrdering = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetReverseOrdering, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.ReverseOrderingOn = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOn, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.ReverseOrderingOff = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOff, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.GetAttribute = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetAttribute, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.SetAttribute = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetAttribute, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3.GetPointer = new_instancemethod(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetPointer, None, itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3_swigregister = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_swigregister
itkShapeRelabelLabelMapFilterLM3_swigregister(itkShapeRelabelLabelMapFilterLM3)

def itkShapeRelabelLabelMapFilterLM3___New_orig__() -> "itkShapeRelabelLabelMapFilterLM3_Pointer":
    """itkShapeRelabelLabelMapFilterLM3___New_orig__() -> itkShapeRelabelLabelMapFilterLM3_Pointer"""
    return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3___New_orig__()

def itkShapeRelabelLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkShapeRelabelLabelMapFilterLM3 *":
    """itkShapeRelabelLabelMapFilterLM3_cast(itkLightObject obj) -> itkShapeRelabelLabelMapFilterLM3"""
    return _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_cast(obj)



