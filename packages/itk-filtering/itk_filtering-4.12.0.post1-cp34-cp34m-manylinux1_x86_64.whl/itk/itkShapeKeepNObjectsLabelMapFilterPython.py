# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapeKeepNObjectsLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkShapeKeepNObjectsLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkShapeKeepNObjectsLabelMapFilterPython')
    _itkShapeKeepNObjectsLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapeKeepNObjectsLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShapeKeepNObjectsLabelMapFilterPython
            return _itkShapeKeepNObjectsLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkShapeKeepNObjectsLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkShapeKeepNObjectsLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapeKeepNObjectsLabelMapFilterPython
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
import itkLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkOptimizerParametersPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython
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
import ITKLabelMapBasePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkImageSourceCommonPython

def itkShapeKeepNObjectsLabelMapFilterLM3_New():
  return itkShapeKeepNObjectsLabelMapFilterLM3.New()


def itkShapeKeepNObjectsLabelMapFilterLM2_New():
  return itkShapeKeepNObjectsLabelMapFilterLM2.New()

class itkShapeKeepNObjectsLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkShapeKeepNObjectsLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeKeepNObjectsLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkShapeKeepNObjectsLabelMapFilterLM2_Pointer"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeKeepNObjectsLabelMapFilterLM2_Pointer":
        """Clone(itkShapeKeepNObjectsLabelMapFilterLM2 self) -> itkShapeKeepNObjectsLabelMapFilterLM2_Pointer"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeKeepNObjectsLabelMapFilterLM2 self, bool const _arg)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkShapeKeepNObjectsLabelMapFilterLM2 self) -> bool const &"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeKeepNObjectsLabelMapFilterLM2 self)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeKeepNObjectsLabelMapFilterLM2 self)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_ReverseOrderingOff(self)


    def SetNumberOfObjects(self, _arg: 'unsigned long const') -> "void":
        """SetNumberOfObjects(itkShapeKeepNObjectsLabelMapFilterLM2 self, unsigned long const _arg)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetNumberOfObjects(self, _arg)


    def GetNumberOfObjects(self) -> "unsigned long const &":
        """GetNumberOfObjects(itkShapeKeepNObjectsLabelMapFilterLM2 self) -> unsigned long const &"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetNumberOfObjects(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeKeepNObjectsLabelMapFilterLM2 self) -> unsigned int"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeKeepNObjectsLabelMapFilterLM2 self, unsigned int const _arg)
        SetAttribute(itkShapeKeepNObjectsLabelMapFilterLM2 self, std::string const & s)
        """
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeKeepNObjectsLabelMapFilterPython.delete_itkShapeKeepNObjectsLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkShapeKeepNObjectsLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkShapeKeepNObjectsLabelMapFilterLM2"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeKeepNObjectsLabelMapFilterLM2 *":
        """GetPointer(itkShapeKeepNObjectsLabelMapFilterLM2 self) -> itkShapeKeepNObjectsLabelMapFilterLM2"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeKeepNObjectsLabelMapFilterLM2

        Create a new object of the class itkShapeKeepNObjectsLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeKeepNObjectsLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeKeepNObjectsLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeKeepNObjectsLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeKeepNObjectsLabelMapFilterLM2.Clone = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_Clone, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.SetReverseOrdering = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetReverseOrdering, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.GetReverseOrdering = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetReverseOrdering, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.ReverseOrderingOn = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_ReverseOrderingOn, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.ReverseOrderingOff = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_ReverseOrderingOff, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.SetNumberOfObjects = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetNumberOfObjects, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.GetNumberOfObjects = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetNumberOfObjects, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.GetAttribute = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetAttribute, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.SetAttribute = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetAttribute, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2.GetPointer = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetPointer, None, itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2_swigregister = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_swigregister
itkShapeKeepNObjectsLabelMapFilterLM2_swigregister(itkShapeKeepNObjectsLabelMapFilterLM2)

def itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__() -> "itkShapeKeepNObjectsLabelMapFilterLM2_Pointer":
    """itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__() -> itkShapeKeepNObjectsLabelMapFilterLM2_Pointer"""
    return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__()

def itkShapeKeepNObjectsLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkShapeKeepNObjectsLabelMapFilterLM2 *":
    """itkShapeKeepNObjectsLabelMapFilterLM2_cast(itkLightObject obj) -> itkShapeKeepNObjectsLabelMapFilterLM2"""
    return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_cast(obj)

class itkShapeKeepNObjectsLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkShapeKeepNObjectsLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeKeepNObjectsLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkShapeKeepNObjectsLabelMapFilterLM3_Pointer"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeKeepNObjectsLabelMapFilterLM3_Pointer":
        """Clone(itkShapeKeepNObjectsLabelMapFilterLM3 self) -> itkShapeKeepNObjectsLabelMapFilterLM3_Pointer"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeKeepNObjectsLabelMapFilterLM3 self, bool const _arg)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkShapeKeepNObjectsLabelMapFilterLM3 self) -> bool const &"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeKeepNObjectsLabelMapFilterLM3 self)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeKeepNObjectsLabelMapFilterLM3 self)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_ReverseOrderingOff(self)


    def SetNumberOfObjects(self, _arg: 'unsigned long const') -> "void":
        """SetNumberOfObjects(itkShapeKeepNObjectsLabelMapFilterLM3 self, unsigned long const _arg)"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetNumberOfObjects(self, _arg)


    def GetNumberOfObjects(self) -> "unsigned long const &":
        """GetNumberOfObjects(itkShapeKeepNObjectsLabelMapFilterLM3 self) -> unsigned long const &"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetNumberOfObjects(self)


    def GetAttribute(self) -> "unsigned int":
        """GetAttribute(itkShapeKeepNObjectsLabelMapFilterLM3 self) -> unsigned int"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeKeepNObjectsLabelMapFilterLM3 self, unsigned int const _arg)
        SetAttribute(itkShapeKeepNObjectsLabelMapFilterLM3 self, std::string const & s)
        """
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeKeepNObjectsLabelMapFilterPython.delete_itkShapeKeepNObjectsLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkShapeKeepNObjectsLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkShapeKeepNObjectsLabelMapFilterLM3"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShapeKeepNObjectsLabelMapFilterLM3 *":
        """GetPointer(itkShapeKeepNObjectsLabelMapFilterLM3 self) -> itkShapeKeepNObjectsLabelMapFilterLM3"""
        return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShapeKeepNObjectsLabelMapFilterLM3

        Create a new object of the class itkShapeKeepNObjectsLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeKeepNObjectsLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeKeepNObjectsLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeKeepNObjectsLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeKeepNObjectsLabelMapFilterLM3.Clone = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_Clone, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.SetReverseOrdering = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetReverseOrdering, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.GetReverseOrdering = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetReverseOrdering, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.ReverseOrderingOn = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_ReverseOrderingOn, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.ReverseOrderingOff = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_ReverseOrderingOff, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.SetNumberOfObjects = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetNumberOfObjects, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.GetNumberOfObjects = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetNumberOfObjects, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.GetAttribute = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetAttribute, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.SetAttribute = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetAttribute, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3.GetPointer = new_instancemethod(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetPointer, None, itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3_swigregister = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_swigregister
itkShapeKeepNObjectsLabelMapFilterLM3_swigregister(itkShapeKeepNObjectsLabelMapFilterLM3)

def itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__() -> "itkShapeKeepNObjectsLabelMapFilterLM3_Pointer":
    """itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__() -> itkShapeKeepNObjectsLabelMapFilterLM3_Pointer"""
    return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__()

def itkShapeKeepNObjectsLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkShapeKeepNObjectsLabelMapFilterLM3 *":
    """itkShapeKeepNObjectsLabelMapFilterLM3_cast(itkLightObject obj) -> itkShapeKeepNObjectsLabelMapFilterLM3"""
    return _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_cast(obj)



