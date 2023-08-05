# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkObjectByObjectLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkObjectByObjectLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkObjectByObjectLabelMapFilterPython')
    _itkObjectByObjectLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkObjectByObjectLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkObjectByObjectLabelMapFilterPython
            return _itkObjectByObjectLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkObjectByObjectLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkObjectByObjectLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkObjectByObjectLabelMapFilterPython
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


import itkImageSourcePython
import itkVectorImagePython
import ITKCommonBasePython
import pyBasePython
import stdcomplexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import itkLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkHistogramPython
import itkArrayPython
import itkSamplePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import ITKLabelMapBasePython

def itkObjectByObjectLabelMapFilterLM3_New():
  return itkObjectByObjectLabelMapFilterLM3.New()


def itkObjectByObjectLabelMapFilterLM2_New():
  return itkObjectByObjectLabelMapFilterLM2.New()

class itkObjectByObjectLabelMapFilterLM2(itkLabelMapFilterPython.itkLabelMapFilterLM2LM2):
    """Proxy of C++ itkObjectByObjectLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkObjectByObjectLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkObjectByObjectLabelMapFilterLM2_Pointer"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkObjectByObjectLabelMapFilterLM2_Pointer":
        """Clone(itkObjectByObjectLabelMapFilterLM2 self) -> itkObjectByObjectLabelMapFilterLM2_Pointer"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_Clone(self)


    def SetFilter(self, filter: 'itkImageToImageFilterIUC2IUC2') -> "void":
        """SetFilter(itkObjectByObjectLabelMapFilterLM2 self, itkImageToImageFilterIUC2IUC2 filter)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetFilter(self, filter)


    def GetFilter(self, *args) -> "itkImageToImageFilterIUC2IUC2 const *":
        """
        GetFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageToImageFilterIUC2IUC2
        GetFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageToImageFilterIUC2IUC2
        """
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetFilter(self, *args)


    def SetInputFilter(self, filter: 'itkImageToImageFilterIUC2IUC2') -> "void":
        """SetInputFilter(itkObjectByObjectLabelMapFilterLM2 self, itkImageToImageFilterIUC2IUC2 filter)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInputFilter(self, filter)


    def GetModifiableInputFilter(self) -> "itkImageToImageFilterIUC2IUC2 *":
        """GetModifiableInputFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageToImageFilterIUC2IUC2"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableInputFilter(self)


    def GetInputFilter(self, *args) -> "itkImageToImageFilterIUC2IUC2 *":
        """
        GetInputFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageToImageFilterIUC2IUC2
        GetInputFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageToImageFilterIUC2IUC2
        """
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInputFilter(self, *args)


    def SetOutputFilter(self, filter: 'itkImageSourceIUC2') -> "void":
        """SetOutputFilter(itkObjectByObjectLabelMapFilterLM2 self, itkImageSourceIUC2 filter)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetOutputFilter(self, filter)


    def GetModifiableOutputFilter(self) -> "itkImageSourceIUC2 *":
        """GetModifiableOutputFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageSourceIUC2"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableOutputFilter(self)


    def GetOutputFilter(self, *args) -> "itkImageSourceIUC2 *":
        """
        GetOutputFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageSourceIUC2
        GetOutputFilter(itkObjectByObjectLabelMapFilterLM2 self) -> itkImageSourceIUC2
        """
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetOutputFilter(self, *args)


    def SetKeepLabels(self, _arg: 'bool const') -> "void":
        """SetKeepLabels(itkObjectByObjectLabelMapFilterLM2 self, bool const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetKeepLabels(self, _arg)


    def GetKeepLabels(self) -> "bool":
        """GetKeepLabels(itkObjectByObjectLabelMapFilterLM2 self) -> bool"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetKeepLabels(self)


    def KeepLabelsOn(self) -> "void":
        """KeepLabelsOn(itkObjectByObjectLabelMapFilterLM2 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOn(self)


    def KeepLabelsOff(self) -> "void":
        """KeepLabelsOff(itkObjectByObjectLabelMapFilterLM2 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOff(self)


    def SetPadSize(self, _arg: 'itkSize2') -> "void":
        """SetPadSize(itkObjectByObjectLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetPadSize(self, _arg)


    def GetPadSize(self) -> "itkSize2":
        """GetPadSize(itkObjectByObjectLabelMapFilterLM2 self) -> itkSize2"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetPadSize(self)


    def SetConstrainPaddingToImage(self, _arg: 'bool const') -> "void":
        """SetConstrainPaddingToImage(itkObjectByObjectLabelMapFilterLM2 self, bool const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetConstrainPaddingToImage(self, _arg)


    def GetConstrainPaddingToImage(self) -> "bool":
        """GetConstrainPaddingToImage(itkObjectByObjectLabelMapFilterLM2 self) -> bool"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetConstrainPaddingToImage(self)


    def ConstrainPaddingToImageOn(self) -> "void":
        """ConstrainPaddingToImageOn(itkObjectByObjectLabelMapFilterLM2 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOn(self)


    def ConstrainPaddingToImageOff(self) -> "void":
        """ConstrainPaddingToImageOff(itkObjectByObjectLabelMapFilterLM2 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOff(self)


    def SetBinaryInternalOutput(self, _arg: 'bool const') -> "void":
        """SetBinaryInternalOutput(itkObjectByObjectLabelMapFilterLM2 self, bool const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetBinaryInternalOutput(self, _arg)


    def GetBinaryInternalOutput(self) -> "bool":
        """GetBinaryInternalOutput(itkObjectByObjectLabelMapFilterLM2 self) -> bool"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetBinaryInternalOutput(self)


    def BinaryInternalOutputOn(self) -> "void":
        """BinaryInternalOutputOn(itkObjectByObjectLabelMapFilterLM2 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOn(self)


    def BinaryInternalOutputOff(self) -> "void":
        """BinaryInternalOutputOff(itkObjectByObjectLabelMapFilterLM2 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOff(self)


    def SetInternalForegroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetInternalForegroundValue(itkObjectByObjectLabelMapFilterLM2 self, unsigned char const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInternalForegroundValue(self, _arg)


    def GetInternalForegroundValue(self) -> "unsigned char":
        """GetInternalForegroundValue(itkObjectByObjectLabelMapFilterLM2 self) -> unsigned char"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInternalForegroundValue(self)


    def GetLabel(self) -> "unsigned long":
        """GetLabel(itkObjectByObjectLabelMapFilterLM2 self) -> unsigned long"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetLabel(self)

    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkObjectByObjectLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkObjectByObjectLabelMapFilterLM2"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkObjectByObjectLabelMapFilterLM2 *":
        """GetPointer(itkObjectByObjectLabelMapFilterLM2 self) -> itkObjectByObjectLabelMapFilterLM2"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM2

        Create a new object of the class itkObjectByObjectLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectByObjectLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkObjectByObjectLabelMapFilterLM2.Clone = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_Clone, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetInputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInputFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetModifiableInputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableInputFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetInputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInputFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetOutputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetOutputFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetModifiableOutputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableOutputFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetOutputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetOutputFilter, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetKeepLabels = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetKeepLabels, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetKeepLabels = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetKeepLabels, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.KeepLabelsOn = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOn, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.KeepLabelsOff = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOff, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetPadSize = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetPadSize, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetPadSize = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetPadSize, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetConstrainPaddingToImage = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetConstrainPaddingToImage, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetConstrainPaddingToImage = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetConstrainPaddingToImage, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.ConstrainPaddingToImageOn = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOn, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.ConstrainPaddingToImageOff = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOff, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetBinaryInternalOutput = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetBinaryInternalOutput, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetBinaryInternalOutput = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetBinaryInternalOutput, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.BinaryInternalOutputOn = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOn, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.BinaryInternalOutputOff = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOff, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.SetInternalForegroundValue = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInternalForegroundValue, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetInternalForegroundValue = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInternalForegroundValue, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetLabel = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetLabel, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2.GetPointer = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetPointer, None, itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2_swigregister = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_swigregister
itkObjectByObjectLabelMapFilterLM2_swigregister(itkObjectByObjectLabelMapFilterLM2)

def itkObjectByObjectLabelMapFilterLM2___New_orig__() -> "itkObjectByObjectLabelMapFilterLM2_Pointer":
    """itkObjectByObjectLabelMapFilterLM2___New_orig__() -> itkObjectByObjectLabelMapFilterLM2_Pointer"""
    return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2___New_orig__()

def itkObjectByObjectLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkObjectByObjectLabelMapFilterLM2 *":
    """itkObjectByObjectLabelMapFilterLM2_cast(itkLightObject obj) -> itkObjectByObjectLabelMapFilterLM2"""
    return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_cast(obj)

class itkObjectByObjectLabelMapFilterLM3(itkLabelMapFilterPython.itkLabelMapFilterLM3LM3):
    """Proxy of C++ itkObjectByObjectLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkObjectByObjectLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkObjectByObjectLabelMapFilterLM3_Pointer"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkObjectByObjectLabelMapFilterLM3_Pointer":
        """Clone(itkObjectByObjectLabelMapFilterLM3 self) -> itkObjectByObjectLabelMapFilterLM3_Pointer"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_Clone(self)


    def SetFilter(self, filter: 'itkImageToImageFilterIUC3IUC3') -> "void":
        """SetFilter(itkObjectByObjectLabelMapFilterLM3 self, itkImageToImageFilterIUC3IUC3 filter)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetFilter(self, filter)


    def GetFilter(self, *args) -> "itkImageToImageFilterIUC3IUC3 const *":
        """
        GetFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageToImageFilterIUC3IUC3
        GetFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageToImageFilterIUC3IUC3
        """
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetFilter(self, *args)


    def SetInputFilter(self, filter: 'itkImageToImageFilterIUC3IUC3') -> "void":
        """SetInputFilter(itkObjectByObjectLabelMapFilterLM3 self, itkImageToImageFilterIUC3IUC3 filter)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInputFilter(self, filter)


    def GetModifiableInputFilter(self) -> "itkImageToImageFilterIUC3IUC3 *":
        """GetModifiableInputFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageToImageFilterIUC3IUC3"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableInputFilter(self)


    def GetInputFilter(self, *args) -> "itkImageToImageFilterIUC3IUC3 *":
        """
        GetInputFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageToImageFilterIUC3IUC3
        GetInputFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageToImageFilterIUC3IUC3
        """
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInputFilter(self, *args)


    def SetOutputFilter(self, filter: 'itkImageSourceIUC3') -> "void":
        """SetOutputFilter(itkObjectByObjectLabelMapFilterLM3 self, itkImageSourceIUC3 filter)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetOutputFilter(self, filter)


    def GetModifiableOutputFilter(self) -> "itkImageSourceIUC3 *":
        """GetModifiableOutputFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageSourceIUC3"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableOutputFilter(self)


    def GetOutputFilter(self, *args) -> "itkImageSourceIUC3 *":
        """
        GetOutputFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageSourceIUC3
        GetOutputFilter(itkObjectByObjectLabelMapFilterLM3 self) -> itkImageSourceIUC3
        """
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetOutputFilter(self, *args)


    def SetKeepLabels(self, _arg: 'bool const') -> "void":
        """SetKeepLabels(itkObjectByObjectLabelMapFilterLM3 self, bool const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetKeepLabels(self, _arg)


    def GetKeepLabels(self) -> "bool":
        """GetKeepLabels(itkObjectByObjectLabelMapFilterLM3 self) -> bool"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetKeepLabels(self)


    def KeepLabelsOn(self) -> "void":
        """KeepLabelsOn(itkObjectByObjectLabelMapFilterLM3 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOn(self)


    def KeepLabelsOff(self) -> "void":
        """KeepLabelsOff(itkObjectByObjectLabelMapFilterLM3 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOff(self)


    def SetPadSize(self, _arg: 'itkSize3') -> "void":
        """SetPadSize(itkObjectByObjectLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetPadSize(self, _arg)


    def GetPadSize(self) -> "itkSize3":
        """GetPadSize(itkObjectByObjectLabelMapFilterLM3 self) -> itkSize3"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetPadSize(self)


    def SetConstrainPaddingToImage(self, _arg: 'bool const') -> "void":
        """SetConstrainPaddingToImage(itkObjectByObjectLabelMapFilterLM3 self, bool const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetConstrainPaddingToImage(self, _arg)


    def GetConstrainPaddingToImage(self) -> "bool":
        """GetConstrainPaddingToImage(itkObjectByObjectLabelMapFilterLM3 self) -> bool"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetConstrainPaddingToImage(self)


    def ConstrainPaddingToImageOn(self) -> "void":
        """ConstrainPaddingToImageOn(itkObjectByObjectLabelMapFilterLM3 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOn(self)


    def ConstrainPaddingToImageOff(self) -> "void":
        """ConstrainPaddingToImageOff(itkObjectByObjectLabelMapFilterLM3 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOff(self)


    def SetBinaryInternalOutput(self, _arg: 'bool const') -> "void":
        """SetBinaryInternalOutput(itkObjectByObjectLabelMapFilterLM3 self, bool const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetBinaryInternalOutput(self, _arg)


    def GetBinaryInternalOutput(self) -> "bool":
        """GetBinaryInternalOutput(itkObjectByObjectLabelMapFilterLM3 self) -> bool"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetBinaryInternalOutput(self)


    def BinaryInternalOutputOn(self) -> "void":
        """BinaryInternalOutputOn(itkObjectByObjectLabelMapFilterLM3 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOn(self)


    def BinaryInternalOutputOff(self) -> "void":
        """BinaryInternalOutputOff(itkObjectByObjectLabelMapFilterLM3 self)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOff(self)


    def SetInternalForegroundValue(self, _arg: 'unsigned char const') -> "void":
        """SetInternalForegroundValue(itkObjectByObjectLabelMapFilterLM3 self, unsigned char const _arg)"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInternalForegroundValue(self, _arg)


    def GetInternalForegroundValue(self) -> "unsigned char":
        """GetInternalForegroundValue(itkObjectByObjectLabelMapFilterLM3 self) -> unsigned char"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInternalForegroundValue(self)


    def GetLabel(self) -> "unsigned long":
        """GetLabel(itkObjectByObjectLabelMapFilterLM3 self) -> unsigned long"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetLabel(self)

    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkObjectByObjectLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkObjectByObjectLabelMapFilterLM3"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkObjectByObjectLabelMapFilterLM3 *":
        """GetPointer(itkObjectByObjectLabelMapFilterLM3 self) -> itkObjectByObjectLabelMapFilterLM3"""
        return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM3

        Create a new object of the class itkObjectByObjectLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectByObjectLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkObjectByObjectLabelMapFilterLM3.Clone = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_Clone, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetInputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInputFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetModifiableInputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableInputFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetInputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInputFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetOutputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetOutputFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetModifiableOutputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableOutputFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetOutputFilter = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetOutputFilter, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetKeepLabels = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetKeepLabels, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetKeepLabels = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetKeepLabels, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.KeepLabelsOn = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOn, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.KeepLabelsOff = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOff, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetPadSize = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetPadSize, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetPadSize = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetPadSize, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetConstrainPaddingToImage = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetConstrainPaddingToImage, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetConstrainPaddingToImage = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetConstrainPaddingToImage, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.ConstrainPaddingToImageOn = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOn, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.ConstrainPaddingToImageOff = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOff, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetBinaryInternalOutput = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetBinaryInternalOutput, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetBinaryInternalOutput = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetBinaryInternalOutput, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.BinaryInternalOutputOn = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOn, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.BinaryInternalOutputOff = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOff, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.SetInternalForegroundValue = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInternalForegroundValue, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetInternalForegroundValue = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInternalForegroundValue, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetLabel = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetLabel, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3.GetPointer = new_instancemethod(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetPointer, None, itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3_swigregister = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_swigregister
itkObjectByObjectLabelMapFilterLM3_swigregister(itkObjectByObjectLabelMapFilterLM3)

def itkObjectByObjectLabelMapFilterLM3___New_orig__() -> "itkObjectByObjectLabelMapFilterLM3_Pointer":
    """itkObjectByObjectLabelMapFilterLM3___New_orig__() -> itkObjectByObjectLabelMapFilterLM3_Pointer"""
    return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3___New_orig__()

def itkObjectByObjectLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkObjectByObjectLabelMapFilterLM3 *":
    """itkObjectByObjectLabelMapFilterLM3_cast(itkLightObject obj) -> itkObjectByObjectLabelMapFilterLM3"""
    return _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_cast(obj)



