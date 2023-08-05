# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIsotropicFourthOrderLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkIsotropicFourthOrderLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkIsotropicFourthOrderLevelSetImageFilterPython')
    _itkIsotropicFourthOrderLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIsotropicFourthOrderLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkIsotropicFourthOrderLevelSetImageFilterPython
            return _itkIsotropicFourthOrderLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkIsotropicFourthOrderLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkIsotropicFourthOrderLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIsotropicFourthOrderLevelSetImageFilterPython
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


import itkSparseFieldFourthOrderLevelSetImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkLevelSetFunctionPython
import itkFixedArrayPython
import itkFiniteDifferenceFunctionPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkCovariantVectorPython
import itkImagePython
import itkPointPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_New():
  return itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.New()


def itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_New():
  return itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.New()

class itkIsotropicFourthOrderLevelSetImageFilterIF2IF2(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2):
    """Proxy of C++ itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer":
        """Clone(itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 self) -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 self) -> unsigned int"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkIsotropicFourthOrderLevelSetImageFilterPython.delete_itkIsotropicFourthOrderLevelSetImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 *":
        """GetPointer(itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 self) -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2

        Create a new object of the class itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.Clone = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Clone, None, itkIsotropicFourthOrderLevelSetImageFilterIF2IF2)
itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.GetMaxFilterIteration = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_GetMaxFilterIteration, None, itkIsotropicFourthOrderLevelSetImageFilterIF2IF2)
itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.SetMaxFilterIteration = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_SetMaxFilterIteration, None, itkIsotropicFourthOrderLevelSetImageFilterIF2IF2)
itkIsotropicFourthOrderLevelSetImageFilterIF2IF2.GetPointer = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_GetPointer, None, itkIsotropicFourthOrderLevelSetImageFilterIF2IF2)
itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister = _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister
itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister(itkIsotropicFourthOrderLevelSetImageFilterIF2IF2)

def itkIsotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__() -> "itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer":
    """itkIsotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__() -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer"""
    return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__()

def itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkIsotropicFourthOrderLevelSetImageFilterIF2IF2 *":
    """itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_cast(itkLightObject obj) -> itkIsotropicFourthOrderLevelSetImageFilterIF2IF2"""
    return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF2IF2_cast(obj)

class itkIsotropicFourthOrderLevelSetImageFilterIF3IF3(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3):
    """Proxy of C++ itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer":
        """Clone(itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 self) -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 self) -> unsigned int"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkIsotropicFourthOrderLevelSetImageFilterPython.delete_itkIsotropicFourthOrderLevelSetImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 *":
        """GetPointer(itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 self) -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3"""
        return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3

        Create a new object of the class itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.Clone = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Clone, None, itkIsotropicFourthOrderLevelSetImageFilterIF3IF3)
itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.GetMaxFilterIteration = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_GetMaxFilterIteration, None, itkIsotropicFourthOrderLevelSetImageFilterIF3IF3)
itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.SetMaxFilterIteration = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_SetMaxFilterIteration, None, itkIsotropicFourthOrderLevelSetImageFilterIF3IF3)
itkIsotropicFourthOrderLevelSetImageFilterIF3IF3.GetPointer = new_instancemethod(_itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_GetPointer, None, itkIsotropicFourthOrderLevelSetImageFilterIF3IF3)
itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister = _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister
itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister(itkIsotropicFourthOrderLevelSetImageFilterIF3IF3)

def itkIsotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__() -> "itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer":
    """itkIsotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__() -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer"""
    return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__()

def itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkIsotropicFourthOrderLevelSetImageFilterIF3IF3 *":
    """itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_cast(itkLightObject obj) -> itkIsotropicFourthOrderLevelSetImageFilterIF3IF3"""
    return _itkIsotropicFourthOrderLevelSetImageFilterPython.itkIsotropicFourthOrderLevelSetImageFilterIF3IF3_cast(obj)



