# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingThresholdStoppingCriterionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingThresholdStoppingCriterionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingThresholdStoppingCriterionPython')
    _itkFastMarchingThresholdStoppingCriterionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingThresholdStoppingCriterionPython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingThresholdStoppingCriterionPython
            return _itkFastMarchingThresholdStoppingCriterionPython
        try:
            _mod = imp.load_module('_itkFastMarchingThresholdStoppingCriterionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingThresholdStoppingCriterionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingThresholdStoppingCriterionPython
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


import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkFastMarchingStoppingCriterionBasePython
import itkNodePairPython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import ITKCommonBasePython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython

def itkFastMarchingThresholdStoppingCriterionIF3IF3_New():
  return itkFastMarchingThresholdStoppingCriterionIF3IF3.New()


def itkFastMarchingThresholdStoppingCriterionIF2IF2_New():
  return itkFastMarchingThresholdStoppingCriterionIF2IF2.New()

class itkFastMarchingThresholdStoppingCriterionIF2IF2(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2):
    """Proxy of C++ itkFastMarchingThresholdStoppingCriterionIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer":
        """__New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer":
        """Clone(itkFastMarchingThresholdStoppingCriterionIF2IF2 self) -> itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_Clone(self)


    def SetThreshold(self, _arg: 'float const') -> "void":
        """SetThreshold(itkFastMarchingThresholdStoppingCriterionIF2IF2 self, float const _arg)"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_SetThreshold(self, _arg)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkFastMarchingThresholdStoppingCriterionIF2IF2 self) -> float"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetThreshold(self)

    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF2IF2"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingThresholdStoppingCriterionIF2IF2 *":
        """GetPointer(itkFastMarchingThresholdStoppingCriterionIF2IF2 self) -> itkFastMarchingThresholdStoppingCriterionIF2IF2"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF2IF2

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingThresholdStoppingCriterionIF2IF2.Clone = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_Clone, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2.SetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_SetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2.GetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2.GetPointer = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetPointer, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister
itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister(itkFastMarchingThresholdStoppingCriterionIF2IF2)

def itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer":
    """itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__()

def itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF2IF2 *":
    """itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF2IF2"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(obj)

class itkFastMarchingThresholdStoppingCriterionIF3IF3(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3):
    """Proxy of C++ itkFastMarchingThresholdStoppingCriterionIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer":
        """__New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer":
        """Clone(itkFastMarchingThresholdStoppingCriterionIF3IF3 self) -> itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_Clone(self)


    def SetThreshold(self, _arg: 'float const') -> "void":
        """SetThreshold(itkFastMarchingThresholdStoppingCriterionIF3IF3 self, float const _arg)"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_SetThreshold(self, _arg)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkFastMarchingThresholdStoppingCriterionIF3IF3 self) -> float"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetThreshold(self)

    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF3IF3"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingThresholdStoppingCriterionIF3IF3 *":
        """GetPointer(itkFastMarchingThresholdStoppingCriterionIF3IF3 self) -> itkFastMarchingThresholdStoppingCriterionIF3IF3"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF3IF3

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingThresholdStoppingCriterionIF3IF3.Clone = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_Clone, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3.SetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_SetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3.GetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3.GetPointer = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetPointer, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister
itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister(itkFastMarchingThresholdStoppingCriterionIF3IF3)

def itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer":
    """itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__()

def itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF3IF3 *":
    """itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF3IF3"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(obj)



