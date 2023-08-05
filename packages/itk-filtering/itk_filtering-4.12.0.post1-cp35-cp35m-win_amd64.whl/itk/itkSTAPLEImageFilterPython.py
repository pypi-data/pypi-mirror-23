# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSTAPLEImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSTAPLEImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSTAPLEImageFilterPython')
    _itkSTAPLEImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSTAPLEImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSTAPLEImageFilterPython
            return _itkSTAPLEImageFilterPython
        try:
            _mod = imp.load_module('_itkSTAPLEImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSTAPLEImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSTAPLEImageFilterPython
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


import ITKCommonBasePython
import pyBasePython
import itkImageToImageFilterAPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
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
import itkImageRegionPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkSTAPLEImageFilterIF3IF3_New():
  return itkSTAPLEImageFilterIF3IF3.New()


def itkSTAPLEImageFilterIF2IF2_New():
  return itkSTAPLEImageFilterIF2IF2.New()

class itkSTAPLEImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkSTAPLEImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSTAPLEImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSTAPLEImageFilterIF2IF2_Pointer"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSTAPLEImageFilterIF2IF2_Pointer":
        """Clone(itkSTAPLEImageFilterIF2IF2 self) -> itkSTAPLEImageFilterIF2IF2_Pointer"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_Clone(self)


    def SetForegroundValue(self, _arg: 'float const') -> "void":
        """SetForegroundValue(itkSTAPLEImageFilterIF2IF2 self, float const _arg)"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_SetForegroundValue(self, _arg)


    def GetForegroundValue(self) -> "float":
        """GetForegroundValue(itkSTAPLEImageFilterIF2IF2 self) -> float"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetForegroundValue(self)


    def GetSensitivity(self, *args) -> "double":
        """
        GetSensitivity(itkSTAPLEImageFilterIF2IF2 self) -> vectorD
        GetSensitivity(itkSTAPLEImageFilterIF2IF2 self, unsigned int i) -> double
        """
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetSensitivity(self, *args)


    def GetSpecificity(self, *args) -> "double":
        """
        GetSpecificity(itkSTAPLEImageFilterIF2IF2 self) -> vectorD
        GetSpecificity(itkSTAPLEImageFilterIF2IF2 self, unsigned int i) -> double
        """
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetSpecificity(self, *args)


    def SetMaximumIterations(self, _arg: 'unsigned int const') -> "void":
        """SetMaximumIterations(itkSTAPLEImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_SetMaximumIterations(self, _arg)


    def GetMaximumIterations(self) -> "unsigned int":
        """GetMaximumIterations(itkSTAPLEImageFilterIF2IF2 self) -> unsigned int"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetMaximumIterations(self)


    def SetConfidenceWeight(self, _arg: 'double const') -> "void":
        """SetConfidenceWeight(itkSTAPLEImageFilterIF2IF2 self, double const _arg)"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_SetConfidenceWeight(self, _arg)


    def GetConfidenceWeight(self) -> "double":
        """GetConfidenceWeight(itkSTAPLEImageFilterIF2IF2 self) -> double"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetConfidenceWeight(self)


    def GetElapsedIterations(self) -> "unsigned int":
        """GetElapsedIterations(itkSTAPLEImageFilterIF2IF2 self) -> unsigned int"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetElapsedIterations(self)

    InputHasNumericTraitsCheck = _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkSTAPLEImageFilterPython.delete_itkSTAPLEImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSTAPLEImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSTAPLEImageFilterIF2IF2"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSTAPLEImageFilterIF2IF2 *":
        """GetPointer(itkSTAPLEImageFilterIF2IF2 self) -> itkSTAPLEImageFilterIF2IF2"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSTAPLEImageFilterIF2IF2

        Create a new object of the class itkSTAPLEImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSTAPLEImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSTAPLEImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSTAPLEImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSTAPLEImageFilterIF2IF2.Clone = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_Clone, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.SetForegroundValue = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_SetForegroundValue, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetForegroundValue = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetForegroundValue, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetSensitivity = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetSensitivity, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetSpecificity = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetSpecificity, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.SetMaximumIterations = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_SetMaximumIterations, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetMaximumIterations = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetMaximumIterations, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.SetConfidenceWeight = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_SetConfidenceWeight, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetConfidenceWeight = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetConfidenceWeight, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetElapsedIterations = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetElapsedIterations, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2.GetPointer = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_GetPointer, None, itkSTAPLEImageFilterIF2IF2)
itkSTAPLEImageFilterIF2IF2_swigregister = _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_swigregister
itkSTAPLEImageFilterIF2IF2_swigregister(itkSTAPLEImageFilterIF2IF2)

def itkSTAPLEImageFilterIF2IF2___New_orig__() -> "itkSTAPLEImageFilterIF2IF2_Pointer":
    """itkSTAPLEImageFilterIF2IF2___New_orig__() -> itkSTAPLEImageFilterIF2IF2_Pointer"""
    return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2___New_orig__()

def itkSTAPLEImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSTAPLEImageFilterIF2IF2 *":
    """itkSTAPLEImageFilterIF2IF2_cast(itkLightObject obj) -> itkSTAPLEImageFilterIF2IF2"""
    return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF2IF2_cast(obj)

class itkSTAPLEImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkSTAPLEImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSTAPLEImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSTAPLEImageFilterIF3IF3_Pointer"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSTAPLEImageFilterIF3IF3_Pointer":
        """Clone(itkSTAPLEImageFilterIF3IF3 self) -> itkSTAPLEImageFilterIF3IF3_Pointer"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_Clone(self)


    def SetForegroundValue(self, _arg: 'float const') -> "void":
        """SetForegroundValue(itkSTAPLEImageFilterIF3IF3 self, float const _arg)"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_SetForegroundValue(self, _arg)


    def GetForegroundValue(self) -> "float":
        """GetForegroundValue(itkSTAPLEImageFilterIF3IF3 self) -> float"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetForegroundValue(self)


    def GetSensitivity(self, *args) -> "double":
        """
        GetSensitivity(itkSTAPLEImageFilterIF3IF3 self) -> vectorD
        GetSensitivity(itkSTAPLEImageFilterIF3IF3 self, unsigned int i) -> double
        """
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetSensitivity(self, *args)


    def GetSpecificity(self, *args) -> "double":
        """
        GetSpecificity(itkSTAPLEImageFilterIF3IF3 self) -> vectorD
        GetSpecificity(itkSTAPLEImageFilterIF3IF3 self, unsigned int i) -> double
        """
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetSpecificity(self, *args)


    def SetMaximumIterations(self, _arg: 'unsigned int const') -> "void":
        """SetMaximumIterations(itkSTAPLEImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_SetMaximumIterations(self, _arg)


    def GetMaximumIterations(self) -> "unsigned int":
        """GetMaximumIterations(itkSTAPLEImageFilterIF3IF3 self) -> unsigned int"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetMaximumIterations(self)


    def SetConfidenceWeight(self, _arg: 'double const') -> "void":
        """SetConfidenceWeight(itkSTAPLEImageFilterIF3IF3 self, double const _arg)"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_SetConfidenceWeight(self, _arg)


    def GetConfidenceWeight(self) -> "double":
        """GetConfidenceWeight(itkSTAPLEImageFilterIF3IF3 self) -> double"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetConfidenceWeight(self)


    def GetElapsedIterations(self) -> "unsigned int":
        """GetElapsedIterations(itkSTAPLEImageFilterIF3IF3 self) -> unsigned int"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetElapsedIterations(self)

    InputHasNumericTraitsCheck = _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkSTAPLEImageFilterPython.delete_itkSTAPLEImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSTAPLEImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSTAPLEImageFilterIF3IF3"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSTAPLEImageFilterIF3IF3 *":
        """GetPointer(itkSTAPLEImageFilterIF3IF3 self) -> itkSTAPLEImageFilterIF3IF3"""
        return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSTAPLEImageFilterIF3IF3

        Create a new object of the class itkSTAPLEImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSTAPLEImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSTAPLEImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSTAPLEImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSTAPLEImageFilterIF3IF3.Clone = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_Clone, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.SetForegroundValue = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_SetForegroundValue, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetForegroundValue = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetForegroundValue, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetSensitivity = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetSensitivity, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetSpecificity = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetSpecificity, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.SetMaximumIterations = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_SetMaximumIterations, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetMaximumIterations = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetMaximumIterations, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.SetConfidenceWeight = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_SetConfidenceWeight, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetConfidenceWeight = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetConfidenceWeight, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetElapsedIterations = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetElapsedIterations, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3.GetPointer = new_instancemethod(_itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_GetPointer, None, itkSTAPLEImageFilterIF3IF3)
itkSTAPLEImageFilterIF3IF3_swigregister = _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_swigregister
itkSTAPLEImageFilterIF3IF3_swigregister(itkSTAPLEImageFilterIF3IF3)

def itkSTAPLEImageFilterIF3IF3___New_orig__() -> "itkSTAPLEImageFilterIF3IF3_Pointer":
    """itkSTAPLEImageFilterIF3IF3___New_orig__() -> itkSTAPLEImageFilterIF3IF3_Pointer"""
    return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3___New_orig__()

def itkSTAPLEImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSTAPLEImageFilterIF3IF3 *":
    """itkSTAPLEImageFilterIF3IF3_cast(itkLightObject obj) -> itkSTAPLEImageFilterIF3IF3"""
    return _itkSTAPLEImageFilterPython.itkSTAPLEImageFilterIF3IF3_cast(obj)



