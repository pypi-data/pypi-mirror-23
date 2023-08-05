# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingExtensionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingExtensionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingExtensionImageFilterPython')
    _itkFastMarchingExtensionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingExtensionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingExtensionImageFilterPython
            return _itkFastMarchingExtensionImageFilterPython
        try:
            _mod = imp.load_module('_itkFastMarchingExtensionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingExtensionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingExtensionImageFilterPython
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
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkOffsetPython
import itkSizePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkIndexPython
import ITKCommonBasePython
import itkImageRegionPython
import itkFastMarchingImageFilterPython
import ITKFastMarchingBasePython
import itkLevelSetNodePython
import itkNodePairPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkFastMarchingStoppingCriterionBasePython
import itkVectorContainerPython
import itkContinuousIndexPython

def itkFastMarchingExtensionImageFilterIF3UC1IF3_New():
  return itkFastMarchingExtensionImageFilterIF3UC1IF3.New()


def itkFastMarchingExtensionImageFilterIF2UC1IF2_New():
  return itkFastMarchingExtensionImageFilterIF2UC1IF2.New()

class itkFastMarchingExtensionImageFilterIF2UC1IF2(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2):
    """Proxy of C++ itkFastMarchingExtensionImageFilterIF2UC1IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingExtensionImageFilterIF2UC1IF2_Pointer":
        """__New_orig__() -> itkFastMarchingExtensionImageFilterIF2UC1IF2_Pointer"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingExtensionImageFilterIF2UC1IF2_Pointer":
        """Clone(itkFastMarchingExtensionImageFilterIF2UC1IF2 self) -> itkFastMarchingExtensionImageFilterIF2UC1IF2_Pointer"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_Clone(self)


    def GetAuxiliaryImage(self, idx: 'unsigned int') -> "itkImageUC2 *":
        """GetAuxiliaryImage(itkFastMarchingExtensionImageFilterIF2UC1IF2 self, unsigned int idx) -> itkImageUC2"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetAuxiliaryImage(self, idx)


    def SetAuxiliaryAliveValues(self, values: 'itkVectorContainerUIVUC1') -> "void":
        """SetAuxiliaryAliveValues(itkFastMarchingExtensionImageFilterIF2UC1IF2 self, itkVectorContainerUIVUC1 values)"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_SetAuxiliaryAliveValues(self, values)


    def GetAuxiliaryAliveValues(self) -> "itkVectorContainerUIVUC1 *":
        """GetAuxiliaryAliveValues(itkFastMarchingExtensionImageFilterIF2UC1IF2 self) -> itkVectorContainerUIVUC1"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetAuxiliaryAliveValues(self)


    def SetAuxiliaryTrialValues(self, values: 'itkVectorContainerUIVUC1') -> "void":
        """SetAuxiliaryTrialValues(itkFastMarchingExtensionImageFilterIF2UC1IF2 self, itkVectorContainerUIVUC1 values)"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_SetAuxiliaryTrialValues(self, values)


    def GetAuxiliaryTrialValues(self) -> "itkVectorContainerUIVUC1_Pointer":
        """GetAuxiliaryTrialValues(itkFastMarchingExtensionImageFilterIF2UC1IF2 self) -> itkVectorContainerUIVUC1_Pointer"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetAuxiliaryTrialValues(self)

    AuxValueHasNumericTraitsCheck = _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_AuxValueHasNumericTraitsCheck
    __swig_destroy__ = _itkFastMarchingExtensionImageFilterPython.delete_itkFastMarchingExtensionImageFilterIF2UC1IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingExtensionImageFilterIF2UC1IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingExtensionImageFilterIF2UC1IF2"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingExtensionImageFilterIF2UC1IF2 *":
        """GetPointer(itkFastMarchingExtensionImageFilterIF2UC1IF2 self) -> itkFastMarchingExtensionImageFilterIF2UC1IF2"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingExtensionImageFilterIF2UC1IF2

        Create a new object of the class itkFastMarchingExtensionImageFilterIF2UC1IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingExtensionImageFilterIF2UC1IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingExtensionImageFilterIF2UC1IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingExtensionImageFilterIF2UC1IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingExtensionImageFilterIF2UC1IF2.Clone = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_Clone, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2.GetAuxiliaryImage = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetAuxiliaryImage, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2.SetAuxiliaryAliveValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_SetAuxiliaryAliveValues, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2.GetAuxiliaryAliveValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetAuxiliaryAliveValues, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2.SetAuxiliaryTrialValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_SetAuxiliaryTrialValues, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2.GetAuxiliaryTrialValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetAuxiliaryTrialValues, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2.GetPointer = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_GetPointer, None, itkFastMarchingExtensionImageFilterIF2UC1IF2)
itkFastMarchingExtensionImageFilterIF2UC1IF2_swigregister = _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_swigregister
itkFastMarchingExtensionImageFilterIF2UC1IF2_swigregister(itkFastMarchingExtensionImageFilterIF2UC1IF2)

def itkFastMarchingExtensionImageFilterIF2UC1IF2___New_orig__() -> "itkFastMarchingExtensionImageFilterIF2UC1IF2_Pointer":
    """itkFastMarchingExtensionImageFilterIF2UC1IF2___New_orig__() -> itkFastMarchingExtensionImageFilterIF2UC1IF2_Pointer"""
    return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2___New_orig__()

def itkFastMarchingExtensionImageFilterIF2UC1IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingExtensionImageFilterIF2UC1IF2 *":
    """itkFastMarchingExtensionImageFilterIF2UC1IF2_cast(itkLightObject obj) -> itkFastMarchingExtensionImageFilterIF2UC1IF2"""
    return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF2UC1IF2_cast(obj)

class itkFastMarchingExtensionImageFilterIF3UC1IF3(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3):
    """Proxy of C++ itkFastMarchingExtensionImageFilterIF3UC1IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingExtensionImageFilterIF3UC1IF3_Pointer":
        """__New_orig__() -> itkFastMarchingExtensionImageFilterIF3UC1IF3_Pointer"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingExtensionImageFilterIF3UC1IF3_Pointer":
        """Clone(itkFastMarchingExtensionImageFilterIF3UC1IF3 self) -> itkFastMarchingExtensionImageFilterIF3UC1IF3_Pointer"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_Clone(self)


    def GetAuxiliaryImage(self, idx: 'unsigned int') -> "itkImageUC3 *":
        """GetAuxiliaryImage(itkFastMarchingExtensionImageFilterIF3UC1IF3 self, unsigned int idx) -> itkImageUC3"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetAuxiliaryImage(self, idx)


    def SetAuxiliaryAliveValues(self, values: 'itkVectorContainerUIVUC1') -> "void":
        """SetAuxiliaryAliveValues(itkFastMarchingExtensionImageFilterIF3UC1IF3 self, itkVectorContainerUIVUC1 values)"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_SetAuxiliaryAliveValues(self, values)


    def GetAuxiliaryAliveValues(self) -> "itkVectorContainerUIVUC1 *":
        """GetAuxiliaryAliveValues(itkFastMarchingExtensionImageFilterIF3UC1IF3 self) -> itkVectorContainerUIVUC1"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetAuxiliaryAliveValues(self)


    def SetAuxiliaryTrialValues(self, values: 'itkVectorContainerUIVUC1') -> "void":
        """SetAuxiliaryTrialValues(itkFastMarchingExtensionImageFilterIF3UC1IF3 self, itkVectorContainerUIVUC1 values)"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_SetAuxiliaryTrialValues(self, values)


    def GetAuxiliaryTrialValues(self) -> "itkVectorContainerUIVUC1_Pointer":
        """GetAuxiliaryTrialValues(itkFastMarchingExtensionImageFilterIF3UC1IF3 self) -> itkVectorContainerUIVUC1_Pointer"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetAuxiliaryTrialValues(self)

    AuxValueHasNumericTraitsCheck = _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_AuxValueHasNumericTraitsCheck
    __swig_destroy__ = _itkFastMarchingExtensionImageFilterPython.delete_itkFastMarchingExtensionImageFilterIF3UC1IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingExtensionImageFilterIF3UC1IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingExtensionImageFilterIF3UC1IF3"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingExtensionImageFilterIF3UC1IF3 *":
        """GetPointer(itkFastMarchingExtensionImageFilterIF3UC1IF3 self) -> itkFastMarchingExtensionImageFilterIF3UC1IF3"""
        return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingExtensionImageFilterIF3UC1IF3

        Create a new object of the class itkFastMarchingExtensionImageFilterIF3UC1IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingExtensionImageFilterIF3UC1IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingExtensionImageFilterIF3UC1IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingExtensionImageFilterIF3UC1IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingExtensionImageFilterIF3UC1IF3.Clone = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_Clone, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3.GetAuxiliaryImage = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetAuxiliaryImage, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3.SetAuxiliaryAliveValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_SetAuxiliaryAliveValues, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3.GetAuxiliaryAliveValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetAuxiliaryAliveValues, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3.SetAuxiliaryTrialValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_SetAuxiliaryTrialValues, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3.GetAuxiliaryTrialValues = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetAuxiliaryTrialValues, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3.GetPointer = new_instancemethod(_itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_GetPointer, None, itkFastMarchingExtensionImageFilterIF3UC1IF3)
itkFastMarchingExtensionImageFilterIF3UC1IF3_swigregister = _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_swigregister
itkFastMarchingExtensionImageFilterIF3UC1IF3_swigregister(itkFastMarchingExtensionImageFilterIF3UC1IF3)

def itkFastMarchingExtensionImageFilterIF3UC1IF3___New_orig__() -> "itkFastMarchingExtensionImageFilterIF3UC1IF3_Pointer":
    """itkFastMarchingExtensionImageFilterIF3UC1IF3___New_orig__() -> itkFastMarchingExtensionImageFilterIF3UC1IF3_Pointer"""
    return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3___New_orig__()

def itkFastMarchingExtensionImageFilterIF3UC1IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingExtensionImageFilterIF3UC1IF3 *":
    """itkFastMarchingExtensionImageFilterIF3UC1IF3_cast(itkLightObject obj) -> itkFastMarchingExtensionImageFilterIF3UC1IF3"""
    return _itkFastMarchingExtensionImageFilterPython.itkFastMarchingExtensionImageFilterIF3UC1IF3_cast(obj)



