# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAnisotropicFourthOrderLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkAnisotropicFourthOrderLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkAnisotropicFourthOrderLevelSetImageFilterPython')
    _itkAnisotropicFourthOrderLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAnisotropicFourthOrderLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAnisotropicFourthOrderLevelSetImageFilterPython
            return _itkAnisotropicFourthOrderLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkAnisotropicFourthOrderLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkAnisotropicFourthOrderLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAnisotropicFourthOrderLevelSetImageFilterPython
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
import itkSparseFieldFourthOrderLevelSetImageFilterPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkSizePython
import itkRGBPixelPython
import itkOffsetPython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython
import itkLevelSetFunctionPython

def itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_New():
  return itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.New()


def itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_New():
  return itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.New()

class itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2):
    """Proxy of C++ itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer":
        """Clone(itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 self) -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 self) -> unsigned int"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.delete_itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 *":
        """GetPointer(itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 self) -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2

        Create a new object of the class itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.Clone = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Clone, None, itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2)
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.GetMaxFilterIteration = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_GetMaxFilterIteration, None, itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2)
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.SetMaxFilterIteration = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_SetMaxFilterIteration, None, itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2)
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.GetPointer = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_GetPointer, None, itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2)
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister(itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2)

def itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__() -> "itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer":
    """itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__() -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Pointer"""
    return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__()

def itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 *":
    """itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast(itkLightObject obj) -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2"""
    return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast(obj)

class itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3):
    """Proxy of C++ itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer":
        """Clone(itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 self) -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 self) -> unsigned int"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.delete_itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 *":
        """GetPointer(itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 self) -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3"""
        return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3

        Create a new object of the class itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.Clone = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Clone, None, itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3)
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.GetMaxFilterIteration = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_GetMaxFilterIteration, None, itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3)
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.SetMaxFilterIteration = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_SetMaxFilterIteration, None, itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3)
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.GetPointer = new_instancemethod(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_GetPointer, None, itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3)
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister(itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3)

def itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__() -> "itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer":
    """itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__() -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Pointer"""
    return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__()

def itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 *":
    """itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast(itkLightObject obj) -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3"""
    return _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast(obj)



