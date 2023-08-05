# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRegionFromReferenceLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRegionFromReferenceLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRegionFromReferenceLabelMapFilterPython')
    _itkRegionFromReferenceLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRegionFromReferenceLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRegionFromReferenceLabelMapFilterPython
            return _itkRegionFromReferenceLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkRegionFromReferenceLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRegionFromReferenceLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRegionFromReferenceLabelMapFilterPython
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
import itkChangeRegionLabelMapFilterPython
import itkInPlaceLabelMapFilterPython
import itkLabelMapFilterPython

def itkRegionFromReferenceLabelMapFilterLM3_New():
  return itkRegionFromReferenceLabelMapFilterLM3.New()


def itkRegionFromReferenceLabelMapFilterLM2_New():
  return itkRegionFromReferenceLabelMapFilterLM2.New()

class itkRegionFromReferenceLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """Proxy of C++ itkRegionFromReferenceLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkRegionFromReferenceLabelMapFilterLM2_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRegionFromReferenceLabelMapFilterLM2_Pointer":
        """Clone(itkRegionFromReferenceLabelMapFilterLM2 self) -> itkRegionFromReferenceLabelMapFilterLM2_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_Clone(self)


    def SetReferenceImage(self, image: 'itkImageBase2') -> "void":
        """SetReferenceImage(itkRegionFromReferenceLabelMapFilterLM2 self, itkImageBase2 image)"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetReferenceImage(self, image)


    def GetReferenceImage(self) -> "itkImageBase2 const *":
        """GetReferenceImage(itkRegionFromReferenceLabelMapFilterLM2 self) -> itkImageBase2"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetReferenceImage(self)


    def SetInput1(self, input: 'itkLabelMap2') -> "void":
        """SetInput1(itkRegionFromReferenceLabelMapFilterLM2 self, itkLabelMap2 input)"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageBase2') -> "void":
        """SetInput2(itkRegionFromReferenceLabelMapFilterLM2 self, itkImageBase2 input)"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput2(self, input)

    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM2"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRegionFromReferenceLabelMapFilterLM2 *":
        """GetPointer(itkRegionFromReferenceLabelMapFilterLM2 self) -> itkRegionFromReferenceLabelMapFilterLM2"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM2

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRegionFromReferenceLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRegionFromReferenceLabelMapFilterLM2.Clone = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_Clone, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.SetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.GetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.SetInput1 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput1, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.SetInput2 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput2, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.GetPointer = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetPointer, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2_swigregister = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_swigregister
itkRegionFromReferenceLabelMapFilterLM2_swigregister(itkRegionFromReferenceLabelMapFilterLM2)

def itkRegionFromReferenceLabelMapFilterLM2___New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM2_Pointer":
    """itkRegionFromReferenceLabelMapFilterLM2___New_orig__() -> itkRegionFromReferenceLabelMapFilterLM2_Pointer"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2___New_orig__()

def itkRegionFromReferenceLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM2 *":
    """itkRegionFromReferenceLabelMapFilterLM2_cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM2"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_cast(obj)

class itkRegionFromReferenceLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """Proxy of C++ itkRegionFromReferenceLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkRegionFromReferenceLabelMapFilterLM3_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRegionFromReferenceLabelMapFilterLM3_Pointer":
        """Clone(itkRegionFromReferenceLabelMapFilterLM3 self) -> itkRegionFromReferenceLabelMapFilterLM3_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_Clone(self)


    def SetReferenceImage(self, image: 'itkImageBase3') -> "void":
        """SetReferenceImage(itkRegionFromReferenceLabelMapFilterLM3 self, itkImageBase3 image)"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetReferenceImage(self, image)


    def GetReferenceImage(self) -> "itkImageBase3 const *":
        """GetReferenceImage(itkRegionFromReferenceLabelMapFilterLM3 self) -> itkImageBase3"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetReferenceImage(self)


    def SetInput1(self, input: 'itkLabelMap3') -> "void":
        """SetInput1(itkRegionFromReferenceLabelMapFilterLM3 self, itkLabelMap3 input)"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageBase3') -> "void":
        """SetInput2(itkRegionFromReferenceLabelMapFilterLM3 self, itkImageBase3 input)"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput2(self, input)

    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM3"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRegionFromReferenceLabelMapFilterLM3 *":
        """GetPointer(itkRegionFromReferenceLabelMapFilterLM3 self) -> itkRegionFromReferenceLabelMapFilterLM3"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM3

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRegionFromReferenceLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRegionFromReferenceLabelMapFilterLM3.Clone = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_Clone, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.SetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.GetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.SetInput1 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput1, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.SetInput2 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput2, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.GetPointer = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetPointer, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3_swigregister = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_swigregister
itkRegionFromReferenceLabelMapFilterLM3_swigregister(itkRegionFromReferenceLabelMapFilterLM3)

def itkRegionFromReferenceLabelMapFilterLM3___New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM3_Pointer":
    """itkRegionFromReferenceLabelMapFilterLM3___New_orig__() -> itkRegionFromReferenceLabelMapFilterLM3_Pointer"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3___New_orig__()

def itkRegionFromReferenceLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM3 *":
    """itkRegionFromReferenceLabelMapFilterLM3_cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM3"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_cast(obj)



