# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkConvolutionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkConvolutionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkConvolutionImageFilterPython')
    _itkConvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkConvolutionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkConvolutionImageFilterPython
            return _itkConvolutionImageFilterPython
        try:
            _mod = imp.load_module('_itkConvolutionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkConvolutionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkConvolutionImageFilterPython
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


import itkSizePython
import pyBasePython
import itkConvolutionImageFilterBasePython
import itkImageToImageFilterAPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import itkOffsetPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageBoundaryConditionPython

def itkConvolutionImageFilterIF3IF3_New():
  return itkConvolutionImageFilterIF3IF3.New()


def itkConvolutionImageFilterIF2IF2_New():
  return itkConvolutionImageFilterIF2IF2.New()


def itkConvolutionImageFilterIUC3IUC3_New():
  return itkConvolutionImageFilterIUC3IUC3.New()


def itkConvolutionImageFilterIUC2IUC2_New():
  return itkConvolutionImageFilterIUC2IUC2.New()


def itkConvolutionImageFilterISS3ISS3_New():
  return itkConvolutionImageFilterISS3ISS3.New()


def itkConvolutionImageFilterISS2ISS2_New():
  return itkConvolutionImageFilterISS2ISS2.New()

class itkConvolutionImageFilterIF2IF2(itkConvolutionImageFilterBasePython.itkConvolutionImageFilterBaseIF2IF2):
    """Proxy of C++ itkConvolutionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConvolutionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkConvolutionImageFilterIF2IF2_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConvolutionImageFilterIF2IF2_Pointer":
        """Clone(itkConvolutionImageFilterIF2IF2 self) -> itkConvolutionImageFilterIF2IF2_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_Clone(self)

    __swig_destroy__ = _itkConvolutionImageFilterPython.delete_itkConvolutionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkConvolutionImageFilterIF2IF2"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkConvolutionImageFilterIF2IF2 *":
        """GetPointer(itkConvolutionImageFilterIF2IF2 self) -> itkConvolutionImageFilterIF2IF2"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkConvolutionImageFilterIF2IF2

        Create a new object of the class itkConvolutionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConvolutionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConvolutionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConvolutionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkConvolutionImageFilterIF2IF2.Clone = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_Clone, None, itkConvolutionImageFilterIF2IF2)
itkConvolutionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_GetPointer, None, itkConvolutionImageFilterIF2IF2)
itkConvolutionImageFilterIF2IF2_swigregister = _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_swigregister
itkConvolutionImageFilterIF2IF2_swigregister(itkConvolutionImageFilterIF2IF2)

def itkConvolutionImageFilterIF2IF2___New_orig__() -> "itkConvolutionImageFilterIF2IF2_Pointer":
    """itkConvolutionImageFilterIF2IF2___New_orig__() -> itkConvolutionImageFilterIF2IF2_Pointer"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2___New_orig__()

def itkConvolutionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIF2IF2 *":
    """itkConvolutionImageFilterIF2IF2_cast(itkLightObject obj) -> itkConvolutionImageFilterIF2IF2"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF2IF2_cast(obj)

class itkConvolutionImageFilterIF3IF3(itkConvolutionImageFilterBasePython.itkConvolutionImageFilterBaseIF3IF3):
    """Proxy of C++ itkConvolutionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConvolutionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkConvolutionImageFilterIF3IF3_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConvolutionImageFilterIF3IF3_Pointer":
        """Clone(itkConvolutionImageFilterIF3IF3 self) -> itkConvolutionImageFilterIF3IF3_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_Clone(self)

    __swig_destroy__ = _itkConvolutionImageFilterPython.delete_itkConvolutionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkConvolutionImageFilterIF3IF3"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkConvolutionImageFilterIF3IF3 *":
        """GetPointer(itkConvolutionImageFilterIF3IF3 self) -> itkConvolutionImageFilterIF3IF3"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkConvolutionImageFilterIF3IF3

        Create a new object of the class itkConvolutionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConvolutionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConvolutionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConvolutionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkConvolutionImageFilterIF3IF3.Clone = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_Clone, None, itkConvolutionImageFilterIF3IF3)
itkConvolutionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_GetPointer, None, itkConvolutionImageFilterIF3IF3)
itkConvolutionImageFilterIF3IF3_swigregister = _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_swigregister
itkConvolutionImageFilterIF3IF3_swigregister(itkConvolutionImageFilterIF3IF3)

def itkConvolutionImageFilterIF3IF3___New_orig__() -> "itkConvolutionImageFilterIF3IF3_Pointer":
    """itkConvolutionImageFilterIF3IF3___New_orig__() -> itkConvolutionImageFilterIF3IF3_Pointer"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3___New_orig__()

def itkConvolutionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIF3IF3 *":
    """itkConvolutionImageFilterIF3IF3_cast(itkLightObject obj) -> itkConvolutionImageFilterIF3IF3"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIF3IF3_cast(obj)

class itkConvolutionImageFilterISS2ISS2(itkConvolutionImageFilterBasePython.itkConvolutionImageFilterBaseISS2ISS2):
    """Proxy of C++ itkConvolutionImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConvolutionImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkConvolutionImageFilterISS2ISS2_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConvolutionImageFilterISS2ISS2_Pointer":
        """Clone(itkConvolutionImageFilterISS2ISS2 self) -> itkConvolutionImageFilterISS2ISS2_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_Clone(self)

    __swig_destroy__ = _itkConvolutionImageFilterPython.delete_itkConvolutionImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkConvolutionImageFilterISS2ISS2"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkConvolutionImageFilterISS2ISS2 *":
        """GetPointer(itkConvolutionImageFilterISS2ISS2 self) -> itkConvolutionImageFilterISS2ISS2"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkConvolutionImageFilterISS2ISS2

        Create a new object of the class itkConvolutionImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConvolutionImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConvolutionImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConvolutionImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkConvolutionImageFilterISS2ISS2.Clone = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_Clone, None, itkConvolutionImageFilterISS2ISS2)
itkConvolutionImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_GetPointer, None, itkConvolutionImageFilterISS2ISS2)
itkConvolutionImageFilterISS2ISS2_swigregister = _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_swigregister
itkConvolutionImageFilterISS2ISS2_swigregister(itkConvolutionImageFilterISS2ISS2)

def itkConvolutionImageFilterISS2ISS2___New_orig__() -> "itkConvolutionImageFilterISS2ISS2_Pointer":
    """itkConvolutionImageFilterISS2ISS2___New_orig__() -> itkConvolutionImageFilterISS2ISS2_Pointer"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2___New_orig__()

def itkConvolutionImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterISS2ISS2 *":
    """itkConvolutionImageFilterISS2ISS2_cast(itkLightObject obj) -> itkConvolutionImageFilterISS2ISS2"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS2ISS2_cast(obj)

class itkConvolutionImageFilterISS3ISS3(itkConvolutionImageFilterBasePython.itkConvolutionImageFilterBaseISS3ISS3):
    """Proxy of C++ itkConvolutionImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConvolutionImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkConvolutionImageFilterISS3ISS3_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConvolutionImageFilterISS3ISS3_Pointer":
        """Clone(itkConvolutionImageFilterISS3ISS3 self) -> itkConvolutionImageFilterISS3ISS3_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_Clone(self)

    __swig_destroy__ = _itkConvolutionImageFilterPython.delete_itkConvolutionImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkConvolutionImageFilterISS3ISS3"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkConvolutionImageFilterISS3ISS3 *":
        """GetPointer(itkConvolutionImageFilterISS3ISS3 self) -> itkConvolutionImageFilterISS3ISS3"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkConvolutionImageFilterISS3ISS3

        Create a new object of the class itkConvolutionImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConvolutionImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConvolutionImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConvolutionImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkConvolutionImageFilterISS3ISS3.Clone = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_Clone, None, itkConvolutionImageFilterISS3ISS3)
itkConvolutionImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_GetPointer, None, itkConvolutionImageFilterISS3ISS3)
itkConvolutionImageFilterISS3ISS3_swigregister = _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_swigregister
itkConvolutionImageFilterISS3ISS3_swigregister(itkConvolutionImageFilterISS3ISS3)

def itkConvolutionImageFilterISS3ISS3___New_orig__() -> "itkConvolutionImageFilterISS3ISS3_Pointer":
    """itkConvolutionImageFilterISS3ISS3___New_orig__() -> itkConvolutionImageFilterISS3ISS3_Pointer"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3___New_orig__()

def itkConvolutionImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterISS3ISS3 *":
    """itkConvolutionImageFilterISS3ISS3_cast(itkLightObject obj) -> itkConvolutionImageFilterISS3ISS3"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterISS3ISS3_cast(obj)

class itkConvolutionImageFilterIUC2IUC2(itkConvolutionImageFilterBasePython.itkConvolutionImageFilterBaseIUC2IUC2):
    """Proxy of C++ itkConvolutionImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConvolutionImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkConvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConvolutionImageFilterIUC2IUC2_Pointer":
        """Clone(itkConvolutionImageFilterIUC2IUC2 self) -> itkConvolutionImageFilterIUC2IUC2_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_Clone(self)

    __swig_destroy__ = _itkConvolutionImageFilterPython.delete_itkConvolutionImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkConvolutionImageFilterIUC2IUC2"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkConvolutionImageFilterIUC2IUC2 *":
        """GetPointer(itkConvolutionImageFilterIUC2IUC2 self) -> itkConvolutionImageFilterIUC2IUC2"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkConvolutionImageFilterIUC2IUC2

        Create a new object of the class itkConvolutionImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConvolutionImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConvolutionImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConvolutionImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkConvolutionImageFilterIUC2IUC2.Clone = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_Clone, None, itkConvolutionImageFilterIUC2IUC2)
itkConvolutionImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_GetPointer, None, itkConvolutionImageFilterIUC2IUC2)
itkConvolutionImageFilterIUC2IUC2_swigregister = _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_swigregister
itkConvolutionImageFilterIUC2IUC2_swigregister(itkConvolutionImageFilterIUC2IUC2)

def itkConvolutionImageFilterIUC2IUC2___New_orig__() -> "itkConvolutionImageFilterIUC2IUC2_Pointer":
    """itkConvolutionImageFilterIUC2IUC2___New_orig__() -> itkConvolutionImageFilterIUC2IUC2_Pointer"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2___New_orig__()

def itkConvolutionImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIUC2IUC2 *":
    """itkConvolutionImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkConvolutionImageFilterIUC2IUC2"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC2IUC2_cast(obj)

class itkConvolutionImageFilterIUC3IUC3(itkConvolutionImageFilterBasePython.itkConvolutionImageFilterBaseIUC3IUC3):
    """Proxy of C++ itkConvolutionImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConvolutionImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkConvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConvolutionImageFilterIUC3IUC3_Pointer":
        """Clone(itkConvolutionImageFilterIUC3IUC3 self) -> itkConvolutionImageFilterIUC3IUC3_Pointer"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_Clone(self)

    __swig_destroy__ = _itkConvolutionImageFilterPython.delete_itkConvolutionImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkConvolutionImageFilterIUC3IUC3"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkConvolutionImageFilterIUC3IUC3 *":
        """GetPointer(itkConvolutionImageFilterIUC3IUC3 self) -> itkConvolutionImageFilterIUC3IUC3"""
        return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkConvolutionImageFilterIUC3IUC3

        Create a new object of the class itkConvolutionImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConvolutionImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConvolutionImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConvolutionImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkConvolutionImageFilterIUC3IUC3.Clone = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_Clone, None, itkConvolutionImageFilterIUC3IUC3)
itkConvolutionImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_GetPointer, None, itkConvolutionImageFilterIUC3IUC3)
itkConvolutionImageFilterIUC3IUC3_swigregister = _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_swigregister
itkConvolutionImageFilterIUC3IUC3_swigregister(itkConvolutionImageFilterIUC3IUC3)

def itkConvolutionImageFilterIUC3IUC3___New_orig__() -> "itkConvolutionImageFilterIUC3IUC3_Pointer":
    """itkConvolutionImageFilterIUC3IUC3___New_orig__() -> itkConvolutionImageFilterIUC3IUC3_Pointer"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3___New_orig__()

def itkConvolutionImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkConvolutionImageFilterIUC3IUC3 *":
    """itkConvolutionImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkConvolutionImageFilterIUC3IUC3"""
    return _itkConvolutionImageFilterPython.itkConvolutionImageFilterIUC3IUC3_cast(obj)



