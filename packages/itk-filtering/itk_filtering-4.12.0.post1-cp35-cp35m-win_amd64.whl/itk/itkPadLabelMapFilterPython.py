# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPadLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPadLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPadLabelMapFilterPython')
    _itkPadLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPadLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkPadLabelMapFilterPython
            return _itkPadLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkPadLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPadLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPadLabelMapFilterPython
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


import itkChangeRegionLabelMapFilterPython
import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkStatisticsLabelObjectPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkHistogramPython
import itkSamplePython
import itkArrayPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageSourcePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkImageToImageFilterCommonPython
import itkLabelMapFilterPython

def itkPadLabelMapFilterLM3_New():
  return itkPadLabelMapFilterLM3.New()


def itkPadLabelMapFilterLM2_New():
  return itkPadLabelMapFilterLM2.New()

class itkPadLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """Proxy of C++ itkPadLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPadLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkPadLabelMapFilterLM2_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPadLabelMapFilterLM2_Pointer":
        """Clone(itkPadLabelMapFilterLM2 self) -> itkPadLabelMapFilterLM2_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_Clone(self)


    def SetUpperBoundaryPadSize(self, _arg: 'itkSize2') -> "void":
        """SetUpperBoundaryPadSize(itkPadLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetUpperBoundaryPadSize(self, _arg)


    def GetUpperBoundaryPadSize(self) -> "itkSize2":
        """GetUpperBoundaryPadSize(itkPadLabelMapFilterLM2 self) -> itkSize2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetUpperBoundaryPadSize(self)


    def SetLowerBoundaryPadSize(self, _arg: 'itkSize2') -> "void":
        """SetLowerBoundaryPadSize(itkPadLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetLowerBoundaryPadSize(self, _arg)


    def GetLowerBoundaryPadSize(self) -> "itkSize2":
        """GetLowerBoundaryPadSize(itkPadLabelMapFilterLM2 self) -> itkSize2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetLowerBoundaryPadSize(self)


    def SetPadSize(self, size: 'itkSize2') -> "void":
        """SetPadSize(itkPadLabelMapFilterLM2 self, itkSize2 size)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetPadSize(self, size)

    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkPadLabelMapFilterLM2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPadLabelMapFilterLM2 *":
        """GetPointer(itkPadLabelMapFilterLM2 self) -> itkPadLabelMapFilterLM2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM2

        Create a new object of the class itkPadLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPadLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPadLabelMapFilterLM2.Clone = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_Clone, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.SetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.GetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.SetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.GetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.SetPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.GetPointer = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetPointer, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2_swigregister = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_swigregister
itkPadLabelMapFilterLM2_swigregister(itkPadLabelMapFilterLM2)

def itkPadLabelMapFilterLM2___New_orig__() -> "itkPadLabelMapFilterLM2_Pointer":
    """itkPadLabelMapFilterLM2___New_orig__() -> itkPadLabelMapFilterLM2_Pointer"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2___New_orig__()

def itkPadLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM2 *":
    """itkPadLabelMapFilterLM2_cast(itkLightObject obj) -> itkPadLabelMapFilterLM2"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_cast(obj)

class itkPadLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """Proxy of C++ itkPadLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPadLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkPadLabelMapFilterLM3_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPadLabelMapFilterLM3_Pointer":
        """Clone(itkPadLabelMapFilterLM3 self) -> itkPadLabelMapFilterLM3_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_Clone(self)


    def SetUpperBoundaryPadSize(self, _arg: 'itkSize3') -> "void":
        """SetUpperBoundaryPadSize(itkPadLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetUpperBoundaryPadSize(self, _arg)


    def GetUpperBoundaryPadSize(self) -> "itkSize3":
        """GetUpperBoundaryPadSize(itkPadLabelMapFilterLM3 self) -> itkSize3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetUpperBoundaryPadSize(self)


    def SetLowerBoundaryPadSize(self, _arg: 'itkSize3') -> "void":
        """SetLowerBoundaryPadSize(itkPadLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetLowerBoundaryPadSize(self, _arg)


    def GetLowerBoundaryPadSize(self) -> "itkSize3":
        """GetLowerBoundaryPadSize(itkPadLabelMapFilterLM3 self) -> itkSize3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetLowerBoundaryPadSize(self)


    def SetPadSize(self, size: 'itkSize3') -> "void":
        """SetPadSize(itkPadLabelMapFilterLM3 self, itkSize3 size)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetPadSize(self, size)

    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkPadLabelMapFilterLM3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPadLabelMapFilterLM3 *":
        """GetPointer(itkPadLabelMapFilterLM3 self) -> itkPadLabelMapFilterLM3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM3

        Create a new object of the class itkPadLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPadLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPadLabelMapFilterLM3.Clone = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_Clone, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.SetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.GetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.SetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.GetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.SetPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.GetPointer = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetPointer, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3_swigregister = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_swigregister
itkPadLabelMapFilterLM3_swigregister(itkPadLabelMapFilterLM3)

def itkPadLabelMapFilterLM3___New_orig__() -> "itkPadLabelMapFilterLM3_Pointer":
    """itkPadLabelMapFilterLM3___New_orig__() -> itkPadLabelMapFilterLM3_Pointer"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3___New_orig__()

def itkPadLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM3 *":
    """itkPadLabelMapFilterLM3_cast(itkLightObject obj) -> itkPadLabelMapFilterLM3"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_cast(obj)



