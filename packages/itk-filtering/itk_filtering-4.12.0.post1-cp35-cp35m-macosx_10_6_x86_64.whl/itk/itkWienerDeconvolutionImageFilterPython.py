# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkWienerDeconvolutionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkWienerDeconvolutionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkWienerDeconvolutionImageFilterPython')
    _itkWienerDeconvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkWienerDeconvolutionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkWienerDeconvolutionImageFilterPython
            return _itkWienerDeconvolutionImageFilterPython
        try:
            _mod = imp.load_module('_itkWienerDeconvolutionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkWienerDeconvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkWienerDeconvolutionImageFilterPython
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
import itkInverseDeconvolutionImageFilterPython
import itkFFTConvolutionImageFilterPython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkSizePython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSymmetricSecondRankTensorPython
import itkConvolutionImageFilterBasePython
import itkImageBoundaryConditionPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkWienerDeconvolutionImageFilterIF3IF3_New():
  return itkWienerDeconvolutionImageFilterIF3IF3.New()


def itkWienerDeconvolutionImageFilterIF2IF2_New():
  return itkWienerDeconvolutionImageFilterIF2IF2.New()


def itkWienerDeconvolutionImageFilterIUC3IUC3_New():
  return itkWienerDeconvolutionImageFilterIUC3IUC3.New()


def itkWienerDeconvolutionImageFilterIUC2IUC2_New():
  return itkWienerDeconvolutionImageFilterIUC2IUC2.New()


def itkWienerDeconvolutionImageFilterISS3ISS3_New():
  return itkWienerDeconvolutionImageFilterISS3ISS3.New()


def itkWienerDeconvolutionImageFilterISS2ISS2_New():
  return itkWienerDeconvolutionImageFilterISS2ISS2.New()

class itkWienerDeconvolutionImageFilterIF2IF2(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2):
    """Proxy of C++ itkWienerDeconvolutionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkWienerDeconvolutionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkWienerDeconvolutionImageFilterIF2IF2_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkWienerDeconvolutionImageFilterIF2IF2_Pointer":
        """Clone(itkWienerDeconvolutionImageFilterIF2IF2 self) -> itkWienerDeconvolutionImageFilterIF2IF2_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_Clone(self)


    def SetNoiseVariance(self, _arg: 'double const') -> "void":
        """SetNoiseVariance(itkWienerDeconvolutionImageFilterIF2IF2 self, double const _arg)"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_SetNoiseVariance(self, _arg)


    def GetNoiseVariance(self) -> "double":
        """GetNoiseVariance(itkWienerDeconvolutionImageFilterIF2IF2 self) -> double"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_GetNoiseVariance(self)

    __swig_destroy__ = _itkWienerDeconvolutionImageFilterPython.delete_itkWienerDeconvolutionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIF2IF2"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkWienerDeconvolutionImageFilterIF2IF2 *":
        """GetPointer(itkWienerDeconvolutionImageFilterIF2IF2 self) -> itkWienerDeconvolutionImageFilterIF2IF2"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkWienerDeconvolutionImageFilterIF2IF2

        Create a new object of the class itkWienerDeconvolutionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWienerDeconvolutionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWienerDeconvolutionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWienerDeconvolutionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkWienerDeconvolutionImageFilterIF2IF2.Clone = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_Clone, None, itkWienerDeconvolutionImageFilterIF2IF2)
itkWienerDeconvolutionImageFilterIF2IF2.SetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_SetNoiseVariance, None, itkWienerDeconvolutionImageFilterIF2IF2)
itkWienerDeconvolutionImageFilterIF2IF2.GetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_GetNoiseVariance, None, itkWienerDeconvolutionImageFilterIF2IF2)
itkWienerDeconvolutionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_GetPointer, None, itkWienerDeconvolutionImageFilterIF2IF2)
itkWienerDeconvolutionImageFilterIF2IF2_swigregister = _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_swigregister
itkWienerDeconvolutionImageFilterIF2IF2_swigregister(itkWienerDeconvolutionImageFilterIF2IF2)

def itkWienerDeconvolutionImageFilterIF2IF2___New_orig__() -> "itkWienerDeconvolutionImageFilterIF2IF2_Pointer":
    """itkWienerDeconvolutionImageFilterIF2IF2___New_orig__() -> itkWienerDeconvolutionImageFilterIF2IF2_Pointer"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2___New_orig__()

def itkWienerDeconvolutionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIF2IF2 *":
    """itkWienerDeconvolutionImageFilterIF2IF2_cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIF2IF2"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF2IF2_cast(obj)

class itkWienerDeconvolutionImageFilterIF3IF3(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3):
    """Proxy of C++ itkWienerDeconvolutionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkWienerDeconvolutionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkWienerDeconvolutionImageFilterIF3IF3_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkWienerDeconvolutionImageFilterIF3IF3_Pointer":
        """Clone(itkWienerDeconvolutionImageFilterIF3IF3 self) -> itkWienerDeconvolutionImageFilterIF3IF3_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_Clone(self)


    def SetNoiseVariance(self, _arg: 'double const') -> "void":
        """SetNoiseVariance(itkWienerDeconvolutionImageFilterIF3IF3 self, double const _arg)"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_SetNoiseVariance(self, _arg)


    def GetNoiseVariance(self) -> "double":
        """GetNoiseVariance(itkWienerDeconvolutionImageFilterIF3IF3 self) -> double"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_GetNoiseVariance(self)

    __swig_destroy__ = _itkWienerDeconvolutionImageFilterPython.delete_itkWienerDeconvolutionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIF3IF3"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkWienerDeconvolutionImageFilterIF3IF3 *":
        """GetPointer(itkWienerDeconvolutionImageFilterIF3IF3 self) -> itkWienerDeconvolutionImageFilterIF3IF3"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkWienerDeconvolutionImageFilterIF3IF3

        Create a new object of the class itkWienerDeconvolutionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWienerDeconvolutionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWienerDeconvolutionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWienerDeconvolutionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkWienerDeconvolutionImageFilterIF3IF3.Clone = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_Clone, None, itkWienerDeconvolutionImageFilterIF3IF3)
itkWienerDeconvolutionImageFilterIF3IF3.SetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_SetNoiseVariance, None, itkWienerDeconvolutionImageFilterIF3IF3)
itkWienerDeconvolutionImageFilterIF3IF3.GetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_GetNoiseVariance, None, itkWienerDeconvolutionImageFilterIF3IF3)
itkWienerDeconvolutionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_GetPointer, None, itkWienerDeconvolutionImageFilterIF3IF3)
itkWienerDeconvolutionImageFilterIF3IF3_swigregister = _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_swigregister
itkWienerDeconvolutionImageFilterIF3IF3_swigregister(itkWienerDeconvolutionImageFilterIF3IF3)

def itkWienerDeconvolutionImageFilterIF3IF3___New_orig__() -> "itkWienerDeconvolutionImageFilterIF3IF3_Pointer":
    """itkWienerDeconvolutionImageFilterIF3IF3___New_orig__() -> itkWienerDeconvolutionImageFilterIF3IF3_Pointer"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3___New_orig__()

def itkWienerDeconvolutionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIF3IF3 *":
    """itkWienerDeconvolutionImageFilterIF3IF3_cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIF3IF3"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIF3IF3_cast(obj)

class itkWienerDeconvolutionImageFilterISS2ISS2(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2):
    """Proxy of C++ itkWienerDeconvolutionImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkWienerDeconvolutionImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkWienerDeconvolutionImageFilterISS2ISS2_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkWienerDeconvolutionImageFilterISS2ISS2_Pointer":
        """Clone(itkWienerDeconvolutionImageFilterISS2ISS2 self) -> itkWienerDeconvolutionImageFilterISS2ISS2_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_Clone(self)


    def SetNoiseVariance(self, _arg: 'double const') -> "void":
        """SetNoiseVariance(itkWienerDeconvolutionImageFilterISS2ISS2 self, double const _arg)"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_SetNoiseVariance(self, _arg)


    def GetNoiseVariance(self) -> "double":
        """GetNoiseVariance(itkWienerDeconvolutionImageFilterISS2ISS2 self) -> double"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_GetNoiseVariance(self)

    __swig_destroy__ = _itkWienerDeconvolutionImageFilterPython.delete_itkWienerDeconvolutionImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterISS2ISS2"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkWienerDeconvolutionImageFilterISS2ISS2 *":
        """GetPointer(itkWienerDeconvolutionImageFilterISS2ISS2 self) -> itkWienerDeconvolutionImageFilterISS2ISS2"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkWienerDeconvolutionImageFilterISS2ISS2

        Create a new object of the class itkWienerDeconvolutionImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWienerDeconvolutionImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWienerDeconvolutionImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWienerDeconvolutionImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkWienerDeconvolutionImageFilterISS2ISS2.Clone = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_Clone, None, itkWienerDeconvolutionImageFilterISS2ISS2)
itkWienerDeconvolutionImageFilterISS2ISS2.SetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_SetNoiseVariance, None, itkWienerDeconvolutionImageFilterISS2ISS2)
itkWienerDeconvolutionImageFilterISS2ISS2.GetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_GetNoiseVariance, None, itkWienerDeconvolutionImageFilterISS2ISS2)
itkWienerDeconvolutionImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_GetPointer, None, itkWienerDeconvolutionImageFilterISS2ISS2)
itkWienerDeconvolutionImageFilterISS2ISS2_swigregister = _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_swigregister
itkWienerDeconvolutionImageFilterISS2ISS2_swigregister(itkWienerDeconvolutionImageFilterISS2ISS2)

def itkWienerDeconvolutionImageFilterISS2ISS2___New_orig__() -> "itkWienerDeconvolutionImageFilterISS2ISS2_Pointer":
    """itkWienerDeconvolutionImageFilterISS2ISS2___New_orig__() -> itkWienerDeconvolutionImageFilterISS2ISS2_Pointer"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2___New_orig__()

def itkWienerDeconvolutionImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterISS2ISS2 *":
    """itkWienerDeconvolutionImageFilterISS2ISS2_cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterISS2ISS2"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS2ISS2_cast(obj)

class itkWienerDeconvolutionImageFilterISS3ISS3(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3):
    """Proxy of C++ itkWienerDeconvolutionImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkWienerDeconvolutionImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkWienerDeconvolutionImageFilterISS3ISS3_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkWienerDeconvolutionImageFilterISS3ISS3_Pointer":
        """Clone(itkWienerDeconvolutionImageFilterISS3ISS3 self) -> itkWienerDeconvolutionImageFilterISS3ISS3_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_Clone(self)


    def SetNoiseVariance(self, _arg: 'double const') -> "void":
        """SetNoiseVariance(itkWienerDeconvolutionImageFilterISS3ISS3 self, double const _arg)"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_SetNoiseVariance(self, _arg)


    def GetNoiseVariance(self) -> "double":
        """GetNoiseVariance(itkWienerDeconvolutionImageFilterISS3ISS3 self) -> double"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_GetNoiseVariance(self)

    __swig_destroy__ = _itkWienerDeconvolutionImageFilterPython.delete_itkWienerDeconvolutionImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterISS3ISS3"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkWienerDeconvolutionImageFilterISS3ISS3 *":
        """GetPointer(itkWienerDeconvolutionImageFilterISS3ISS3 self) -> itkWienerDeconvolutionImageFilterISS3ISS3"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkWienerDeconvolutionImageFilterISS3ISS3

        Create a new object of the class itkWienerDeconvolutionImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWienerDeconvolutionImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWienerDeconvolutionImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWienerDeconvolutionImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkWienerDeconvolutionImageFilterISS3ISS3.Clone = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_Clone, None, itkWienerDeconvolutionImageFilterISS3ISS3)
itkWienerDeconvolutionImageFilterISS3ISS3.SetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_SetNoiseVariance, None, itkWienerDeconvolutionImageFilterISS3ISS3)
itkWienerDeconvolutionImageFilterISS3ISS3.GetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_GetNoiseVariance, None, itkWienerDeconvolutionImageFilterISS3ISS3)
itkWienerDeconvolutionImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_GetPointer, None, itkWienerDeconvolutionImageFilterISS3ISS3)
itkWienerDeconvolutionImageFilterISS3ISS3_swigregister = _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_swigregister
itkWienerDeconvolutionImageFilterISS3ISS3_swigregister(itkWienerDeconvolutionImageFilterISS3ISS3)

def itkWienerDeconvolutionImageFilterISS3ISS3___New_orig__() -> "itkWienerDeconvolutionImageFilterISS3ISS3_Pointer":
    """itkWienerDeconvolutionImageFilterISS3ISS3___New_orig__() -> itkWienerDeconvolutionImageFilterISS3ISS3_Pointer"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3___New_orig__()

def itkWienerDeconvolutionImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterISS3ISS3 *":
    """itkWienerDeconvolutionImageFilterISS3ISS3_cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterISS3ISS3"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterISS3ISS3_cast(obj)

class itkWienerDeconvolutionImageFilterIUC2IUC2(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2):
    """Proxy of C++ itkWienerDeconvolutionImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkWienerDeconvolutionImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkWienerDeconvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkWienerDeconvolutionImageFilterIUC2IUC2_Pointer":
        """Clone(itkWienerDeconvolutionImageFilterIUC2IUC2 self) -> itkWienerDeconvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_Clone(self)


    def SetNoiseVariance(self, _arg: 'double const') -> "void":
        """SetNoiseVariance(itkWienerDeconvolutionImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_SetNoiseVariance(self, _arg)


    def GetNoiseVariance(self) -> "double":
        """GetNoiseVariance(itkWienerDeconvolutionImageFilterIUC2IUC2 self) -> double"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_GetNoiseVariance(self)

    __swig_destroy__ = _itkWienerDeconvolutionImageFilterPython.delete_itkWienerDeconvolutionImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIUC2IUC2"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkWienerDeconvolutionImageFilterIUC2IUC2 *":
        """GetPointer(itkWienerDeconvolutionImageFilterIUC2IUC2 self) -> itkWienerDeconvolutionImageFilterIUC2IUC2"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkWienerDeconvolutionImageFilterIUC2IUC2

        Create a new object of the class itkWienerDeconvolutionImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWienerDeconvolutionImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWienerDeconvolutionImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWienerDeconvolutionImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkWienerDeconvolutionImageFilterIUC2IUC2.Clone = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_Clone, None, itkWienerDeconvolutionImageFilterIUC2IUC2)
itkWienerDeconvolutionImageFilterIUC2IUC2.SetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_SetNoiseVariance, None, itkWienerDeconvolutionImageFilterIUC2IUC2)
itkWienerDeconvolutionImageFilterIUC2IUC2.GetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_GetNoiseVariance, None, itkWienerDeconvolutionImageFilterIUC2IUC2)
itkWienerDeconvolutionImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_GetPointer, None, itkWienerDeconvolutionImageFilterIUC2IUC2)
itkWienerDeconvolutionImageFilterIUC2IUC2_swigregister = _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_swigregister
itkWienerDeconvolutionImageFilterIUC2IUC2_swigregister(itkWienerDeconvolutionImageFilterIUC2IUC2)

def itkWienerDeconvolutionImageFilterIUC2IUC2___New_orig__() -> "itkWienerDeconvolutionImageFilterIUC2IUC2_Pointer":
    """itkWienerDeconvolutionImageFilterIUC2IUC2___New_orig__() -> itkWienerDeconvolutionImageFilterIUC2IUC2_Pointer"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2___New_orig__()

def itkWienerDeconvolutionImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIUC2IUC2 *":
    """itkWienerDeconvolutionImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIUC2IUC2"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC2IUC2_cast(obj)

class itkWienerDeconvolutionImageFilterIUC3IUC3(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3):
    """Proxy of C++ itkWienerDeconvolutionImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkWienerDeconvolutionImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkWienerDeconvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkWienerDeconvolutionImageFilterIUC3IUC3_Pointer":
        """Clone(itkWienerDeconvolutionImageFilterIUC3IUC3 self) -> itkWienerDeconvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_Clone(self)


    def SetNoiseVariance(self, _arg: 'double const') -> "void":
        """SetNoiseVariance(itkWienerDeconvolutionImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_SetNoiseVariance(self, _arg)


    def GetNoiseVariance(self) -> "double":
        """GetNoiseVariance(itkWienerDeconvolutionImageFilterIUC3IUC3 self) -> double"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_GetNoiseVariance(self)

    __swig_destroy__ = _itkWienerDeconvolutionImageFilterPython.delete_itkWienerDeconvolutionImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIUC3IUC3"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkWienerDeconvolutionImageFilterIUC3IUC3 *":
        """GetPointer(itkWienerDeconvolutionImageFilterIUC3IUC3 self) -> itkWienerDeconvolutionImageFilterIUC3IUC3"""
        return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkWienerDeconvolutionImageFilterIUC3IUC3

        Create a new object of the class itkWienerDeconvolutionImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWienerDeconvolutionImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWienerDeconvolutionImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWienerDeconvolutionImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkWienerDeconvolutionImageFilterIUC3IUC3.Clone = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_Clone, None, itkWienerDeconvolutionImageFilterIUC3IUC3)
itkWienerDeconvolutionImageFilterIUC3IUC3.SetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_SetNoiseVariance, None, itkWienerDeconvolutionImageFilterIUC3IUC3)
itkWienerDeconvolutionImageFilterIUC3IUC3.GetNoiseVariance = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_GetNoiseVariance, None, itkWienerDeconvolutionImageFilterIUC3IUC3)
itkWienerDeconvolutionImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_GetPointer, None, itkWienerDeconvolutionImageFilterIUC3IUC3)
itkWienerDeconvolutionImageFilterIUC3IUC3_swigregister = _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_swigregister
itkWienerDeconvolutionImageFilterIUC3IUC3_swigregister(itkWienerDeconvolutionImageFilterIUC3IUC3)

def itkWienerDeconvolutionImageFilterIUC3IUC3___New_orig__() -> "itkWienerDeconvolutionImageFilterIUC3IUC3_Pointer":
    """itkWienerDeconvolutionImageFilterIUC3IUC3___New_orig__() -> itkWienerDeconvolutionImageFilterIUC3IUC3_Pointer"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3___New_orig__()

def itkWienerDeconvolutionImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkWienerDeconvolutionImageFilterIUC3IUC3 *":
    """itkWienerDeconvolutionImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkWienerDeconvolutionImageFilterIUC3IUC3"""
    return _itkWienerDeconvolutionImageFilterPython.itkWienerDeconvolutionImageFilterIUC3IUC3_cast(obj)



