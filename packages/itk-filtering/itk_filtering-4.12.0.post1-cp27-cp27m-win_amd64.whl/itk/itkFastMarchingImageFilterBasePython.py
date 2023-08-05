# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingImageFilterBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingImageFilterBasePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingImageFilterBasePython')
    _itkFastMarchingImageFilterBasePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingImageFilterBasePython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingImageFilterBasePython
            return _itkFastMarchingImageFilterBasePython
        try:
            _mod = imp.load_module('_itkFastMarchingImageFilterBasePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingImageFilterBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingImageFilterBasePython
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
import stdcomplexPython
import pyBasePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
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

def itkFastMarchingImageFilterBaseIF3IF3_New():
  return itkFastMarchingImageFilterBaseIF3IF3.New()


def itkFastMarchingImageFilterBaseIF2IF2_New():
  return itkFastMarchingImageFilterBaseIF2IF2.New()

class itkFastMarchingImageFilterBaseIF2IF2(ITKFastMarchingBasePython.itkFastMarchingBaseIF2IF2):
    """Proxy of C++ itkFastMarchingImageFilterBaseIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkFastMarchingImageFilterBaseIF2IF2_Pointer"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkFastMarchingImageFilterBaseIF2IF2_Pointer"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_Clone(self)


    def GetModifiableLabelImage(self):
        """GetModifiableLabelImage(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkImageUC2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetModifiableLabelImage(self)


    def GetLabelImage(self, *args):
        """
        GetLabelImage(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkImageUC2
        GetLabelImage(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkImageUC2
        """
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetLabelImage(self, *args)


    def SetOutputSize(self, size):
        """SetOutputSize(itkFastMarchingImageFilterBaseIF2IF2 self, itkSize2 size)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputSize(self, size)


    def GetOutputSize(self):
        """GetOutputSize(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkSize2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputSize(self)


    def SetOutputRegion(self, _arg):
        """SetOutputRegion(itkFastMarchingImageFilterBaseIF2IF2 self, itkImageRegion2 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputRegion(self, _arg)


    def GetOutputRegion(self):
        """GetOutputRegion(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkImageRegion2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputRegion(self)


    def SetOutputSpacing(self, _arg):
        """SetOutputSpacing(itkFastMarchingImageFilterBaseIF2IF2 self, itkVectorD2 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputSpacing(self, _arg)


    def GetOutputSpacing(self):
        """GetOutputSpacing(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkVectorD2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputSpacing(self)


    def SetOutputDirection(self, _arg):
        """SetOutputDirection(itkFastMarchingImageFilterBaseIF2IF2 self, itkMatrixD22 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputDirection(self, _arg)


    def GetOutputDirection(self):
        """GetOutputDirection(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkMatrixD22"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputDirection(self)


    def SetOutputOrigin(self, _arg):
        """SetOutputOrigin(itkFastMarchingImageFilterBaseIF2IF2 self, itkPointD2 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputOrigin(self, _arg)


    def GetOutputOrigin(self):
        """GetOutputOrigin(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkPointD2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputOrigin(self)


    def SetOverrideOutputInformation(self, _arg):
        """SetOverrideOutputInformation(itkFastMarchingImageFilterBaseIF2IF2 self, bool const _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOverrideOutputInformation(self, _arg)


    def GetOverrideOutputInformation(self):
        """GetOverrideOutputInformation(itkFastMarchingImageFilterBaseIF2IF2 self) -> bool const &"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOverrideOutputInformation(self)


    def OverrideOutputInformationOn(self):
        """OverrideOutputInformationOn(itkFastMarchingImageFilterBaseIF2IF2 self)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_OverrideOutputInformationOn(self)


    def OverrideOutputInformationOff(self):
        """OverrideOutputInformationOff(itkFastMarchingImageFilterBaseIF2IF2 self)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_OverrideOutputInformationOff(self)

    __swig_destroy__ = _itkFastMarchingImageFilterBasePython.delete_itkFastMarchingImageFilterBaseIF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkFastMarchingImageFilterBaseIF2IF2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkFastMarchingImageFilterBaseIF2IF2 self) -> itkFastMarchingImageFilterBaseIF2IF2"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterBaseIF2IF2

        Create a new object of the class itkFastMarchingImageFilterBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingImageFilterBaseIF2IF2.Clone = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_Clone, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetModifiableLabelImage = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetModifiableLabelImage, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetLabelImage = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetLabelImage, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.SetOutputSize = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputSize, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetOutputSize = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputSize, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.SetOutputRegion = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputRegion, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetOutputRegion = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputRegion, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.SetOutputSpacing = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputSpacing, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetOutputSpacing = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputSpacing, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.SetOutputDirection = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputDirection, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetOutputDirection = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputDirection, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.SetOutputOrigin = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputOrigin, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetOutputOrigin = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputOrigin, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.SetOverrideOutputInformation = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOverrideOutputInformation, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetOverrideOutputInformation = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOverrideOutputInformation, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.OverrideOutputInformationOn = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_OverrideOutputInformationOn, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.OverrideOutputInformationOff = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_OverrideOutputInformationOff, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2.GetPointer = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetPointer, None, itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2_swigregister = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_swigregister
itkFastMarchingImageFilterBaseIF2IF2_swigregister(itkFastMarchingImageFilterBaseIF2IF2)

def itkFastMarchingImageFilterBaseIF2IF2___New_orig__():
    """itkFastMarchingImageFilterBaseIF2IF2___New_orig__() -> itkFastMarchingImageFilterBaseIF2IF2_Pointer"""
    return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2___New_orig__()

def itkFastMarchingImageFilterBaseIF2IF2_cast(obj):
    """itkFastMarchingImageFilterBaseIF2IF2_cast(itkLightObject obj) -> itkFastMarchingImageFilterBaseIF2IF2"""
    return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_cast(obj)

class itkFastMarchingImageFilterBaseIF3IF3(ITKFastMarchingBasePython.itkFastMarchingBaseIF3IF3):
    """Proxy of C++ itkFastMarchingImageFilterBaseIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkFastMarchingImageFilterBaseIF3IF3_Pointer"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkFastMarchingImageFilterBaseIF3IF3_Pointer"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_Clone(self)


    def GetModifiableLabelImage(self):
        """GetModifiableLabelImage(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkImageUC3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetModifiableLabelImage(self)


    def GetLabelImage(self, *args):
        """
        GetLabelImage(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkImageUC3
        GetLabelImage(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkImageUC3
        """
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetLabelImage(self, *args)


    def SetOutputSize(self, size):
        """SetOutputSize(itkFastMarchingImageFilterBaseIF3IF3 self, itkSize3 size)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputSize(self, size)


    def GetOutputSize(self):
        """GetOutputSize(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkSize3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputSize(self)


    def SetOutputRegion(self, _arg):
        """SetOutputRegion(itkFastMarchingImageFilterBaseIF3IF3 self, itkImageRegion3 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputRegion(self, _arg)


    def GetOutputRegion(self):
        """GetOutputRegion(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkImageRegion3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputRegion(self)


    def SetOutputSpacing(self, _arg):
        """SetOutputSpacing(itkFastMarchingImageFilterBaseIF3IF3 self, itkVectorD3 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputSpacing(self, _arg)


    def GetOutputSpacing(self):
        """GetOutputSpacing(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkVectorD3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputSpacing(self)


    def SetOutputDirection(self, _arg):
        """SetOutputDirection(itkFastMarchingImageFilterBaseIF3IF3 self, itkMatrixD33 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputDirection(self, _arg)


    def GetOutputDirection(self):
        """GetOutputDirection(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkMatrixD33"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputDirection(self)


    def SetOutputOrigin(self, _arg):
        """SetOutputOrigin(itkFastMarchingImageFilterBaseIF3IF3 self, itkPointD3 _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputOrigin(self, _arg)


    def GetOutputOrigin(self):
        """GetOutputOrigin(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkPointD3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputOrigin(self)


    def SetOverrideOutputInformation(self, _arg):
        """SetOverrideOutputInformation(itkFastMarchingImageFilterBaseIF3IF3 self, bool const _arg)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOverrideOutputInformation(self, _arg)


    def GetOverrideOutputInformation(self):
        """GetOverrideOutputInformation(itkFastMarchingImageFilterBaseIF3IF3 self) -> bool const &"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOverrideOutputInformation(self)


    def OverrideOutputInformationOn(self):
        """OverrideOutputInformationOn(itkFastMarchingImageFilterBaseIF3IF3 self)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_OverrideOutputInformationOn(self)


    def OverrideOutputInformationOff(self):
        """OverrideOutputInformationOff(itkFastMarchingImageFilterBaseIF3IF3 self)"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_OverrideOutputInformationOff(self)

    __swig_destroy__ = _itkFastMarchingImageFilterBasePython.delete_itkFastMarchingImageFilterBaseIF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkFastMarchingImageFilterBaseIF3IF3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkFastMarchingImageFilterBaseIF3IF3 self) -> itkFastMarchingImageFilterBaseIF3IF3"""
        return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterBaseIF3IF3

        Create a new object of the class itkFastMarchingImageFilterBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingImageFilterBaseIF3IF3.Clone = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_Clone, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetModifiableLabelImage = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetModifiableLabelImage, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetLabelImage = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetLabelImage, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.SetOutputSize = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputSize, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetOutputSize = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputSize, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.SetOutputRegion = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputRegion, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetOutputRegion = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputRegion, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.SetOutputSpacing = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputSpacing, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetOutputSpacing = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputSpacing, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.SetOutputDirection = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputDirection, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetOutputDirection = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputDirection, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.SetOutputOrigin = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputOrigin, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetOutputOrigin = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputOrigin, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.SetOverrideOutputInformation = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOverrideOutputInformation, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetOverrideOutputInformation = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOverrideOutputInformation, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.OverrideOutputInformationOn = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_OverrideOutputInformationOn, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.OverrideOutputInformationOff = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_OverrideOutputInformationOff, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3.GetPointer = new_instancemethod(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetPointer, None, itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3_swigregister = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_swigregister
itkFastMarchingImageFilterBaseIF3IF3_swigregister(itkFastMarchingImageFilterBaseIF3IF3)

def itkFastMarchingImageFilterBaseIF3IF3___New_orig__():
    """itkFastMarchingImageFilterBaseIF3IF3___New_orig__() -> itkFastMarchingImageFilterBaseIF3IF3_Pointer"""
    return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3___New_orig__()

def itkFastMarchingImageFilterBaseIF3IF3_cast(obj):
    """itkFastMarchingImageFilterBaseIF3IF3_cast(itkLightObject obj) -> itkFastMarchingImageFilterBaseIF3IF3"""
    return _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_cast(obj)



