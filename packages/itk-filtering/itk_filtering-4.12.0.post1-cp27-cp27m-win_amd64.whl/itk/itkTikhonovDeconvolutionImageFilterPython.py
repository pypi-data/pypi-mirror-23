# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTikhonovDeconvolutionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTikhonovDeconvolutionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTikhonovDeconvolutionImageFilterPython')
    _itkTikhonovDeconvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTikhonovDeconvolutionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkTikhonovDeconvolutionImageFilterPython
            return _itkTikhonovDeconvolutionImageFilterPython
        try:
            _mod = imp.load_module('_itkTikhonovDeconvolutionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTikhonovDeconvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTikhonovDeconvolutionImageFilterPython
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


import itkInverseDeconvolutionImageFilterPython
import itkFFTConvolutionImageFilterPython
import itkConvolutionImageFilterBasePython
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
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageBoundaryConditionPython

def itkTikhonovDeconvolutionImageFilterIF3IF3_New():
  return itkTikhonovDeconvolutionImageFilterIF3IF3.New()


def itkTikhonovDeconvolutionImageFilterIF2IF2_New():
  return itkTikhonovDeconvolutionImageFilterIF2IF2.New()


def itkTikhonovDeconvolutionImageFilterIUC3IUC3_New():
  return itkTikhonovDeconvolutionImageFilterIUC3IUC3.New()


def itkTikhonovDeconvolutionImageFilterIUC2IUC2_New():
  return itkTikhonovDeconvolutionImageFilterIUC2IUC2.New()


def itkTikhonovDeconvolutionImageFilterISS3ISS3_New():
  return itkTikhonovDeconvolutionImageFilterISS3ISS3.New()


def itkTikhonovDeconvolutionImageFilterISS2ISS2_New():
  return itkTikhonovDeconvolutionImageFilterISS2ISS2.New()

class itkTikhonovDeconvolutionImageFilterIF2IF2(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF2IF2):
    """Proxy of C++ itkTikhonovDeconvolutionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTikhonovDeconvolutionImageFilterIF2IF2_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTikhonovDeconvolutionImageFilterIF2IF2 self) -> itkTikhonovDeconvolutionImageFilterIF2IF2_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_Clone(self)


    def SetRegularizationConstant(self, _arg):
        """SetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIF2IF2 self, double const _arg)"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_SetRegularizationConstant(self, _arg)


    def GetRegularizationConstant(self):
        """GetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIF2IF2 self) -> double"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_GetRegularizationConstant(self)

    __swig_destroy__ = _itkTikhonovDeconvolutionImageFilterPython.delete_itkTikhonovDeconvolutionImageFilterIF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIF2IF2"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTikhonovDeconvolutionImageFilterIF2IF2 self) -> itkTikhonovDeconvolutionImageFilterIF2IF2"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTikhonovDeconvolutionImageFilterIF2IF2

        Create a new object of the class itkTikhonovDeconvolutionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTikhonovDeconvolutionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTikhonovDeconvolutionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTikhonovDeconvolutionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTikhonovDeconvolutionImageFilterIF2IF2.Clone = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_Clone, None, itkTikhonovDeconvolutionImageFilterIF2IF2)
itkTikhonovDeconvolutionImageFilterIF2IF2.SetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_SetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIF2IF2)
itkTikhonovDeconvolutionImageFilterIF2IF2.GetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_GetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIF2IF2)
itkTikhonovDeconvolutionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_GetPointer, None, itkTikhonovDeconvolutionImageFilterIF2IF2)
itkTikhonovDeconvolutionImageFilterIF2IF2_swigregister = _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_swigregister
itkTikhonovDeconvolutionImageFilterIF2IF2_swigregister(itkTikhonovDeconvolutionImageFilterIF2IF2)

def itkTikhonovDeconvolutionImageFilterIF2IF2___New_orig__():
    """itkTikhonovDeconvolutionImageFilterIF2IF2___New_orig__() -> itkTikhonovDeconvolutionImageFilterIF2IF2_Pointer"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2___New_orig__()

def itkTikhonovDeconvolutionImageFilterIF2IF2_cast(obj):
    """itkTikhonovDeconvolutionImageFilterIF2IF2_cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIF2IF2"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF2IF2_cast(obj)

class itkTikhonovDeconvolutionImageFilterIF3IF3(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIF3IF3):
    """Proxy of C++ itkTikhonovDeconvolutionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTikhonovDeconvolutionImageFilterIF3IF3_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTikhonovDeconvolutionImageFilterIF3IF3 self) -> itkTikhonovDeconvolutionImageFilterIF3IF3_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_Clone(self)


    def SetRegularizationConstant(self, _arg):
        """SetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIF3IF3 self, double const _arg)"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_SetRegularizationConstant(self, _arg)


    def GetRegularizationConstant(self):
        """GetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIF3IF3 self) -> double"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_GetRegularizationConstant(self)

    __swig_destroy__ = _itkTikhonovDeconvolutionImageFilterPython.delete_itkTikhonovDeconvolutionImageFilterIF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIF3IF3"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTikhonovDeconvolutionImageFilterIF3IF3 self) -> itkTikhonovDeconvolutionImageFilterIF3IF3"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTikhonovDeconvolutionImageFilterIF3IF3

        Create a new object of the class itkTikhonovDeconvolutionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTikhonovDeconvolutionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTikhonovDeconvolutionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTikhonovDeconvolutionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTikhonovDeconvolutionImageFilterIF3IF3.Clone = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_Clone, None, itkTikhonovDeconvolutionImageFilterIF3IF3)
itkTikhonovDeconvolutionImageFilterIF3IF3.SetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_SetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIF3IF3)
itkTikhonovDeconvolutionImageFilterIF3IF3.GetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_GetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIF3IF3)
itkTikhonovDeconvolutionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_GetPointer, None, itkTikhonovDeconvolutionImageFilterIF3IF3)
itkTikhonovDeconvolutionImageFilterIF3IF3_swigregister = _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_swigregister
itkTikhonovDeconvolutionImageFilterIF3IF3_swigregister(itkTikhonovDeconvolutionImageFilterIF3IF3)

def itkTikhonovDeconvolutionImageFilterIF3IF3___New_orig__():
    """itkTikhonovDeconvolutionImageFilterIF3IF3___New_orig__() -> itkTikhonovDeconvolutionImageFilterIF3IF3_Pointer"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3___New_orig__()

def itkTikhonovDeconvolutionImageFilterIF3IF3_cast(obj):
    """itkTikhonovDeconvolutionImageFilterIF3IF3_cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIF3IF3"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIF3IF3_cast(obj)

class itkTikhonovDeconvolutionImageFilterISS2ISS2(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS2ISS2):
    """Proxy of C++ itkTikhonovDeconvolutionImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTikhonovDeconvolutionImageFilterISS2ISS2_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTikhonovDeconvolutionImageFilterISS2ISS2 self) -> itkTikhonovDeconvolutionImageFilterISS2ISS2_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_Clone(self)


    def SetRegularizationConstant(self, _arg):
        """SetRegularizationConstant(itkTikhonovDeconvolutionImageFilterISS2ISS2 self, double const _arg)"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_SetRegularizationConstant(self, _arg)


    def GetRegularizationConstant(self):
        """GetRegularizationConstant(itkTikhonovDeconvolutionImageFilterISS2ISS2 self) -> double"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_GetRegularizationConstant(self)

    __swig_destroy__ = _itkTikhonovDeconvolutionImageFilterPython.delete_itkTikhonovDeconvolutionImageFilterISS2ISS2

    def cast(obj):
        """cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterISS2ISS2"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTikhonovDeconvolutionImageFilterISS2ISS2 self) -> itkTikhonovDeconvolutionImageFilterISS2ISS2"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTikhonovDeconvolutionImageFilterISS2ISS2

        Create a new object of the class itkTikhonovDeconvolutionImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTikhonovDeconvolutionImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTikhonovDeconvolutionImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTikhonovDeconvolutionImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTikhonovDeconvolutionImageFilterISS2ISS2.Clone = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_Clone, None, itkTikhonovDeconvolutionImageFilterISS2ISS2)
itkTikhonovDeconvolutionImageFilterISS2ISS2.SetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_SetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterISS2ISS2)
itkTikhonovDeconvolutionImageFilterISS2ISS2.GetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_GetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterISS2ISS2)
itkTikhonovDeconvolutionImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_GetPointer, None, itkTikhonovDeconvolutionImageFilterISS2ISS2)
itkTikhonovDeconvolutionImageFilterISS2ISS2_swigregister = _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_swigregister
itkTikhonovDeconvolutionImageFilterISS2ISS2_swigregister(itkTikhonovDeconvolutionImageFilterISS2ISS2)

def itkTikhonovDeconvolutionImageFilterISS2ISS2___New_orig__():
    """itkTikhonovDeconvolutionImageFilterISS2ISS2___New_orig__() -> itkTikhonovDeconvolutionImageFilterISS2ISS2_Pointer"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2___New_orig__()

def itkTikhonovDeconvolutionImageFilterISS2ISS2_cast(obj):
    """itkTikhonovDeconvolutionImageFilterISS2ISS2_cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterISS2ISS2"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS2ISS2_cast(obj)

class itkTikhonovDeconvolutionImageFilterISS3ISS3(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterISS3ISS3):
    """Proxy of C++ itkTikhonovDeconvolutionImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTikhonovDeconvolutionImageFilterISS3ISS3_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTikhonovDeconvolutionImageFilterISS3ISS3 self) -> itkTikhonovDeconvolutionImageFilterISS3ISS3_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_Clone(self)


    def SetRegularizationConstant(self, _arg):
        """SetRegularizationConstant(itkTikhonovDeconvolutionImageFilterISS3ISS3 self, double const _arg)"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_SetRegularizationConstant(self, _arg)


    def GetRegularizationConstant(self):
        """GetRegularizationConstant(itkTikhonovDeconvolutionImageFilterISS3ISS3 self) -> double"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_GetRegularizationConstant(self)

    __swig_destroy__ = _itkTikhonovDeconvolutionImageFilterPython.delete_itkTikhonovDeconvolutionImageFilterISS3ISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterISS3ISS3"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTikhonovDeconvolutionImageFilterISS3ISS3 self) -> itkTikhonovDeconvolutionImageFilterISS3ISS3"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTikhonovDeconvolutionImageFilterISS3ISS3

        Create a new object of the class itkTikhonovDeconvolutionImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTikhonovDeconvolutionImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTikhonovDeconvolutionImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTikhonovDeconvolutionImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTikhonovDeconvolutionImageFilterISS3ISS3.Clone = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_Clone, None, itkTikhonovDeconvolutionImageFilterISS3ISS3)
itkTikhonovDeconvolutionImageFilterISS3ISS3.SetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_SetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterISS3ISS3)
itkTikhonovDeconvolutionImageFilterISS3ISS3.GetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_GetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterISS3ISS3)
itkTikhonovDeconvolutionImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_GetPointer, None, itkTikhonovDeconvolutionImageFilterISS3ISS3)
itkTikhonovDeconvolutionImageFilterISS3ISS3_swigregister = _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_swigregister
itkTikhonovDeconvolutionImageFilterISS3ISS3_swigregister(itkTikhonovDeconvolutionImageFilterISS3ISS3)

def itkTikhonovDeconvolutionImageFilterISS3ISS3___New_orig__():
    """itkTikhonovDeconvolutionImageFilterISS3ISS3___New_orig__() -> itkTikhonovDeconvolutionImageFilterISS3ISS3_Pointer"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3___New_orig__()

def itkTikhonovDeconvolutionImageFilterISS3ISS3_cast(obj):
    """itkTikhonovDeconvolutionImageFilterISS3ISS3_cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterISS3ISS3"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterISS3ISS3_cast(obj)

class itkTikhonovDeconvolutionImageFilterIUC2IUC2(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC2IUC2):
    """Proxy of C++ itkTikhonovDeconvolutionImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTikhonovDeconvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTikhonovDeconvolutionImageFilterIUC2IUC2 self) -> itkTikhonovDeconvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_Clone(self)


    def SetRegularizationConstant(self, _arg):
        """SetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_SetRegularizationConstant(self, _arg)


    def GetRegularizationConstant(self):
        """GetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIUC2IUC2 self) -> double"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_GetRegularizationConstant(self)

    __swig_destroy__ = _itkTikhonovDeconvolutionImageFilterPython.delete_itkTikhonovDeconvolutionImageFilterIUC2IUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIUC2IUC2"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTikhonovDeconvolutionImageFilterIUC2IUC2 self) -> itkTikhonovDeconvolutionImageFilterIUC2IUC2"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTikhonovDeconvolutionImageFilterIUC2IUC2

        Create a new object of the class itkTikhonovDeconvolutionImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTikhonovDeconvolutionImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTikhonovDeconvolutionImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTikhonovDeconvolutionImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTikhonovDeconvolutionImageFilterIUC2IUC2.Clone = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_Clone, None, itkTikhonovDeconvolutionImageFilterIUC2IUC2)
itkTikhonovDeconvolutionImageFilterIUC2IUC2.SetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_SetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIUC2IUC2)
itkTikhonovDeconvolutionImageFilterIUC2IUC2.GetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_GetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIUC2IUC2)
itkTikhonovDeconvolutionImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_GetPointer, None, itkTikhonovDeconvolutionImageFilterIUC2IUC2)
itkTikhonovDeconvolutionImageFilterIUC2IUC2_swigregister = _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_swigregister
itkTikhonovDeconvolutionImageFilterIUC2IUC2_swigregister(itkTikhonovDeconvolutionImageFilterIUC2IUC2)

def itkTikhonovDeconvolutionImageFilterIUC2IUC2___New_orig__():
    """itkTikhonovDeconvolutionImageFilterIUC2IUC2___New_orig__() -> itkTikhonovDeconvolutionImageFilterIUC2IUC2_Pointer"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2___New_orig__()

def itkTikhonovDeconvolutionImageFilterIUC2IUC2_cast(obj):
    """itkTikhonovDeconvolutionImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIUC2IUC2"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC2IUC2_cast(obj)

class itkTikhonovDeconvolutionImageFilterIUC3IUC3(itkInverseDeconvolutionImageFilterPython.itkInverseDeconvolutionImageFilterIUC3IUC3):
    """Proxy of C++ itkTikhonovDeconvolutionImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTikhonovDeconvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTikhonovDeconvolutionImageFilterIUC3IUC3 self) -> itkTikhonovDeconvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_Clone(self)


    def SetRegularizationConstant(self, _arg):
        """SetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_SetRegularizationConstant(self, _arg)


    def GetRegularizationConstant(self):
        """GetRegularizationConstant(itkTikhonovDeconvolutionImageFilterIUC3IUC3 self) -> double"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_GetRegularizationConstant(self)

    __swig_destroy__ = _itkTikhonovDeconvolutionImageFilterPython.delete_itkTikhonovDeconvolutionImageFilterIUC3IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIUC3IUC3"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTikhonovDeconvolutionImageFilterIUC3IUC3 self) -> itkTikhonovDeconvolutionImageFilterIUC3IUC3"""
        return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTikhonovDeconvolutionImageFilterIUC3IUC3

        Create a new object of the class itkTikhonovDeconvolutionImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTikhonovDeconvolutionImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTikhonovDeconvolutionImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTikhonovDeconvolutionImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTikhonovDeconvolutionImageFilterIUC3IUC3.Clone = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_Clone, None, itkTikhonovDeconvolutionImageFilterIUC3IUC3)
itkTikhonovDeconvolutionImageFilterIUC3IUC3.SetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_SetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIUC3IUC3)
itkTikhonovDeconvolutionImageFilterIUC3IUC3.GetRegularizationConstant = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_GetRegularizationConstant, None, itkTikhonovDeconvolutionImageFilterIUC3IUC3)
itkTikhonovDeconvolutionImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_GetPointer, None, itkTikhonovDeconvolutionImageFilterIUC3IUC3)
itkTikhonovDeconvolutionImageFilterIUC3IUC3_swigregister = _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_swigregister
itkTikhonovDeconvolutionImageFilterIUC3IUC3_swigregister(itkTikhonovDeconvolutionImageFilterIUC3IUC3)

def itkTikhonovDeconvolutionImageFilterIUC3IUC3___New_orig__():
    """itkTikhonovDeconvolutionImageFilterIUC3IUC3___New_orig__() -> itkTikhonovDeconvolutionImageFilterIUC3IUC3_Pointer"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3___New_orig__()

def itkTikhonovDeconvolutionImageFilterIUC3IUC3_cast(obj):
    """itkTikhonovDeconvolutionImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkTikhonovDeconvolutionImageFilterIUC3IUC3"""
    return _itkTikhonovDeconvolutionImageFilterPython.itkTikhonovDeconvolutionImageFilterIUC3IUC3_cast(obj)



