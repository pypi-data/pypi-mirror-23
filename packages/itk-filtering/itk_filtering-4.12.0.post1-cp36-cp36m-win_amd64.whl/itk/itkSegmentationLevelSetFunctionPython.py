# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSegmentationLevelSetFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSegmentationLevelSetFunctionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSegmentationLevelSetFunctionPython')
    _itkSegmentationLevelSetFunctionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSegmentationLevelSetFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkSegmentationLevelSetFunctionPython
            return _itkSegmentationLevelSetFunctionPython
        try:
            _mod = imp.load_module('_itkSegmentationLevelSetFunctionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSegmentationLevelSetFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSegmentationLevelSetFunctionPython
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


import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkImagePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython

def itkSegmentationLevelSetFunctionIF3IF3_New():
  return itkSegmentationLevelSetFunctionIF3IF3.New()


def itkSegmentationLevelSetFunctionIF2IF2_New():
  return itkSegmentationLevelSetFunctionIF2IF2.New()

class itkSegmentationLevelSetFunctionIF2IF2(itkLevelSetFunctionPython.itkLevelSetFunctionIF2):
    """Proxy of C++ itkSegmentationLevelSetFunctionIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def GetFeatureImage(self) -> "itkImageF2 const *":
        """GetFeatureImage(itkSegmentationLevelSetFunctionIF2IF2 self) -> itkImageF2"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetFeatureImage(self)


    def SetFeatureImage(self, f: 'itkImageF2') -> "void":
        """SetFeatureImage(itkSegmentationLevelSetFunctionIF2IF2 self, itkImageF2 f)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetFeatureImage(self, f)


    def GetSpeedImage(self) -> "itkImageF2 *":
        """GetSpeedImage(itkSegmentationLevelSetFunctionIF2IF2 self) -> itkImageF2"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetSpeedImage(self)


    def SetSpeedImage(self, s: 'itkImageF2') -> "void":
        """SetSpeedImage(itkSegmentationLevelSetFunctionIF2IF2 self, itkImageF2 s)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetSpeedImage(self, s)


    def GetAdvectionImage(self) -> "itkImageFAF22 *":
        """GetAdvectionImage(itkSegmentationLevelSetFunctionIF2IF2 self) -> itkImageFAF22"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetAdvectionImage(self)


    def SetAdvectionImage(self, s: 'itkImageFAF22') -> "void":
        """SetAdvectionImage(itkSegmentationLevelSetFunctionIF2IF2 self, itkImageFAF22 s)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetAdvectionImage(self, s)


    def CalculateSpeedImage(self) -> "void":
        """CalculateSpeedImage(itkSegmentationLevelSetFunctionIF2IF2 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_CalculateSpeedImage(self)


    def CalculateAdvectionImage(self) -> "void":
        """CalculateAdvectionImage(itkSegmentationLevelSetFunctionIF2IF2 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_CalculateAdvectionImage(self)


    def AllocateSpeedImage(self) -> "void":
        """AllocateSpeedImage(itkSegmentationLevelSetFunctionIF2IF2 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_AllocateSpeedImage(self)


    def AllocateAdvectionImage(self) -> "void":
        """AllocateAdvectionImage(itkSegmentationLevelSetFunctionIF2IF2 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_AllocateAdvectionImage(self)


    def ReverseExpansionDirection(self) -> "void":
        """ReverseExpansionDirection(itkSegmentationLevelSetFunctionIF2IF2 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_ReverseExpansionDirection(self)

    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSegmentationLevelSetFunctionIF2IF2 *":
        """cast(itkLightObject obj) -> itkSegmentationLevelSetFunctionIF2IF2"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSegmentationLevelSetFunctionIF2IF2 *":
        """GetPointer(itkSegmentationLevelSetFunctionIF2IF2 self) -> itkSegmentationLevelSetFunctionIF2IF2"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSegmentationLevelSetFunctionIF2IF2

        Create a new object of the class itkSegmentationLevelSetFunctionIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSegmentationLevelSetFunctionIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSegmentationLevelSetFunctionIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSegmentationLevelSetFunctionIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSegmentationLevelSetFunctionIF2IF2.GetFeatureImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetFeatureImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.SetFeatureImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetFeatureImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.GetSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetSpeedImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.SetSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetSpeedImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.GetAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetAdvectionImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.SetAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetAdvectionImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.CalculateSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_CalculateSpeedImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.CalculateAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_CalculateAdvectionImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.AllocateSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_AllocateSpeedImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.AllocateAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_AllocateAdvectionImage, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.ReverseExpansionDirection = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_ReverseExpansionDirection, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2.GetPointer = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetPointer, None, itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2_swigregister = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_swigregister
itkSegmentationLevelSetFunctionIF2IF2_swigregister(itkSegmentationLevelSetFunctionIF2IF2)

def itkSegmentationLevelSetFunctionIF2IF2_cast(obj: 'itkLightObject') -> "itkSegmentationLevelSetFunctionIF2IF2 *":
    """itkSegmentationLevelSetFunctionIF2IF2_cast(itkLightObject obj) -> itkSegmentationLevelSetFunctionIF2IF2"""
    return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_cast(obj)

class itkSegmentationLevelSetFunctionIF3IF3(itkLevelSetFunctionPython.itkLevelSetFunctionIF3):
    """Proxy of C++ itkSegmentationLevelSetFunctionIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def GetFeatureImage(self) -> "itkImageF3 const *":
        """GetFeatureImage(itkSegmentationLevelSetFunctionIF3IF3 self) -> itkImageF3"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetFeatureImage(self)


    def SetFeatureImage(self, f: 'itkImageF3') -> "void":
        """SetFeatureImage(itkSegmentationLevelSetFunctionIF3IF3 self, itkImageF3 f)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetFeatureImage(self, f)


    def GetSpeedImage(self) -> "itkImageF3 *":
        """GetSpeedImage(itkSegmentationLevelSetFunctionIF3IF3 self) -> itkImageF3"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetSpeedImage(self)


    def SetSpeedImage(self, s: 'itkImageF3') -> "void":
        """SetSpeedImage(itkSegmentationLevelSetFunctionIF3IF3 self, itkImageF3 s)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetSpeedImage(self, s)


    def GetAdvectionImage(self) -> "itkImageFAF33 *":
        """GetAdvectionImage(itkSegmentationLevelSetFunctionIF3IF3 self) -> itkImageFAF33"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetAdvectionImage(self)


    def SetAdvectionImage(self, s: 'itkImageFAF33') -> "void":
        """SetAdvectionImage(itkSegmentationLevelSetFunctionIF3IF3 self, itkImageFAF33 s)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetAdvectionImage(self, s)


    def CalculateSpeedImage(self) -> "void":
        """CalculateSpeedImage(itkSegmentationLevelSetFunctionIF3IF3 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_CalculateSpeedImage(self)


    def CalculateAdvectionImage(self) -> "void":
        """CalculateAdvectionImage(itkSegmentationLevelSetFunctionIF3IF3 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_CalculateAdvectionImage(self)


    def AllocateSpeedImage(self) -> "void":
        """AllocateSpeedImage(itkSegmentationLevelSetFunctionIF3IF3 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_AllocateSpeedImage(self)


    def AllocateAdvectionImage(self) -> "void":
        """AllocateAdvectionImage(itkSegmentationLevelSetFunctionIF3IF3 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_AllocateAdvectionImage(self)


    def ReverseExpansionDirection(self) -> "void":
        """ReverseExpansionDirection(itkSegmentationLevelSetFunctionIF3IF3 self)"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_ReverseExpansionDirection(self)

    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSegmentationLevelSetFunctionIF3IF3 *":
        """cast(itkLightObject obj) -> itkSegmentationLevelSetFunctionIF3IF3"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSegmentationLevelSetFunctionIF3IF3 *":
        """GetPointer(itkSegmentationLevelSetFunctionIF3IF3 self) -> itkSegmentationLevelSetFunctionIF3IF3"""
        return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSegmentationLevelSetFunctionIF3IF3

        Create a new object of the class itkSegmentationLevelSetFunctionIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSegmentationLevelSetFunctionIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSegmentationLevelSetFunctionIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSegmentationLevelSetFunctionIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSegmentationLevelSetFunctionIF3IF3.GetFeatureImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetFeatureImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.SetFeatureImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetFeatureImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.GetSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetSpeedImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.SetSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetSpeedImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.GetAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetAdvectionImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.SetAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetAdvectionImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.CalculateSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_CalculateSpeedImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.CalculateAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_CalculateAdvectionImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.AllocateSpeedImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_AllocateSpeedImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.AllocateAdvectionImage = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_AllocateAdvectionImage, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.ReverseExpansionDirection = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_ReverseExpansionDirection, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3.GetPointer = new_instancemethod(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetPointer, None, itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3_swigregister = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_swigregister
itkSegmentationLevelSetFunctionIF3IF3_swigregister(itkSegmentationLevelSetFunctionIF3IF3)

def itkSegmentationLevelSetFunctionIF3IF3_cast(obj: 'itkLightObject') -> "itkSegmentationLevelSetFunctionIF3IF3 *":
    """itkSegmentationLevelSetFunctionIF3IF3_cast(itkLightObject obj) -> itkSegmentationLevelSetFunctionIF3IF3"""
    return _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_cast(obj)



