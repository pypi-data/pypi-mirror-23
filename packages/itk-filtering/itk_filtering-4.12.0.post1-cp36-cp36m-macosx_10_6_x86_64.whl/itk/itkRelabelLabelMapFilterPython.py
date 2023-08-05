# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRelabelLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRelabelLabelMapFilterPython')
    _itkRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRelabelLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRelabelLabelMapFilterPython
            return _itkRelabelLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkRelabelLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRelabelLabelMapFilterPython
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


import itkInPlaceLabelMapFilterPython
import ITKCommonBasePython
import pyBasePython
import itkLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkHistogramPython
import itkSamplePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkArrayPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkAffineTransformPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkPointPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkImageRegionPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourceCommonPython

def itkRelabelLabelMapFilterLM3_New():
  return itkRelabelLabelMapFilterLM3.New()


def itkRelabelLabelMapFilterLM3_Superclass_New():
  return itkRelabelLabelMapFilterLM3_Superclass.New()


def itkRelabelLabelMapFilterLM2_New():
  return itkRelabelLabelMapFilterLM2.New()


def itkRelabelLabelMapFilterLM2_Superclass_New():
  return itkRelabelLabelMapFilterLM2_Superclass.New()

class itkRelabelLabelMapFilterLM2_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkRelabelLabelMapFilterLM2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM2_Superclass_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM2_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM2_Superclass_Pointer":
        """Clone(itkRelabelLabelMapFilterLM2_Superclass self) -> itkRelabelLabelMapFilterLM2_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkRelabelLabelMapFilterLM2_Superclass self, bool const _arg)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkRelabelLabelMapFilterLM2_Superclass self) -> bool const &"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkRelabelLabelMapFilterLM2_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkRelabelLabelMapFilterLM2_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOff(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM2_Superclass

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2_Superclass *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2_Superclass"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRelabelLabelMapFilterLM2_Superclass *":
        """GetPointer(itkRelabelLabelMapFilterLM2_Superclass self) -> itkRelabelLabelMapFilterLM2_Superclass"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM2_Superclass

        Create a new object of the class itkRelabelLabelMapFilterLM2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM2_Superclass.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_Clone, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.SetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_SetReverseOrdering, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.GetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetReverseOrdering, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.ReverseOrderingOn = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOn, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.ReverseOrderingOff = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOff, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.GetPointer = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetPointer, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_swigregister
itkRelabelLabelMapFilterLM2_Superclass_swigregister(itkRelabelLabelMapFilterLM2_Superclass)

def itkRelabelLabelMapFilterLM2_Superclass___New_orig__() -> "itkRelabelLabelMapFilterLM2_Superclass_Pointer":
    """itkRelabelLabelMapFilterLM2_Superclass___New_orig__() -> itkRelabelLabelMapFilterLM2_Superclass_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass___New_orig__()

def itkRelabelLabelMapFilterLM2_Superclass_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2_Superclass *":
    """itkRelabelLabelMapFilterLM2_Superclass_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2_Superclass"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_cast(obj)

class itkRelabelLabelMapFilterLM3_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkRelabelLabelMapFilterLM3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM3_Superclass_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM3_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM3_Superclass_Pointer":
        """Clone(itkRelabelLabelMapFilterLM3_Superclass self) -> itkRelabelLabelMapFilterLM3_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkRelabelLabelMapFilterLM3_Superclass self, bool const _arg)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkRelabelLabelMapFilterLM3_Superclass self) -> bool const &"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkRelabelLabelMapFilterLM3_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkRelabelLabelMapFilterLM3_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOff(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM3_Superclass

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3_Superclass *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3_Superclass"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRelabelLabelMapFilterLM3_Superclass *":
        """GetPointer(itkRelabelLabelMapFilterLM3_Superclass self) -> itkRelabelLabelMapFilterLM3_Superclass"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM3_Superclass

        Create a new object of the class itkRelabelLabelMapFilterLM3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM3_Superclass.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_Clone, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.SetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_SetReverseOrdering, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.GetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetReverseOrdering, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.ReverseOrderingOn = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOn, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.ReverseOrderingOff = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOff, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.GetPointer = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetPointer, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_swigregister
itkRelabelLabelMapFilterLM3_Superclass_swigregister(itkRelabelLabelMapFilterLM3_Superclass)

def itkRelabelLabelMapFilterLM3_Superclass___New_orig__() -> "itkRelabelLabelMapFilterLM3_Superclass_Pointer":
    """itkRelabelLabelMapFilterLM3_Superclass___New_orig__() -> itkRelabelLabelMapFilterLM3_Superclass_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass___New_orig__()

def itkRelabelLabelMapFilterLM3_Superclass_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3_Superclass *":
    """itkRelabelLabelMapFilterLM3_Superclass_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3_Superclass"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_cast(obj)

class itkRelabelLabelMapFilterLM2(itkRelabelLabelMapFilterLM2_Superclass):
    """Proxy of C++ itkRelabelLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM2_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM2_Pointer":
        """Clone(itkRelabelLabelMapFilterLM2 self) -> itkRelabelLabelMapFilterLM2_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Clone(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRelabelLabelMapFilterLM2 *":
        """GetPointer(itkRelabelLabelMapFilterLM2 self) -> itkRelabelLabelMapFilterLM2"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM2

        Create a new object of the class itkRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM2.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Clone, None, itkRelabelLabelMapFilterLM2)
itkRelabelLabelMapFilterLM2.GetPointer = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_GetPointer, None, itkRelabelLabelMapFilterLM2)
itkRelabelLabelMapFilterLM2_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_swigregister
itkRelabelLabelMapFilterLM2_swigregister(itkRelabelLabelMapFilterLM2)

def itkRelabelLabelMapFilterLM2___New_orig__() -> "itkRelabelLabelMapFilterLM2_Pointer":
    """itkRelabelLabelMapFilterLM2___New_orig__() -> itkRelabelLabelMapFilterLM2_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2___New_orig__()

def itkRelabelLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2 *":
    """itkRelabelLabelMapFilterLM2_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_cast(obj)

class itkRelabelLabelMapFilterLM3(itkRelabelLabelMapFilterLM3_Superclass):
    """Proxy of C++ itkRelabelLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM3_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM3_Pointer":
        """Clone(itkRelabelLabelMapFilterLM3 self) -> itkRelabelLabelMapFilterLM3_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Clone(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRelabelLabelMapFilterLM3 *":
        """GetPointer(itkRelabelLabelMapFilterLM3 self) -> itkRelabelLabelMapFilterLM3"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM3

        Create a new object of the class itkRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM3.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Clone, None, itkRelabelLabelMapFilterLM3)
itkRelabelLabelMapFilterLM3.GetPointer = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_GetPointer, None, itkRelabelLabelMapFilterLM3)
itkRelabelLabelMapFilterLM3_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_swigregister
itkRelabelLabelMapFilterLM3_swigregister(itkRelabelLabelMapFilterLM3)

def itkRelabelLabelMapFilterLM3___New_orig__() -> "itkRelabelLabelMapFilterLM3_Pointer":
    """itkRelabelLabelMapFilterLM3___New_orig__() -> itkRelabelLabelMapFilterLM3_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3___New_orig__()

def itkRelabelLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3 *":
    """itkRelabelLabelMapFilterLM3_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_cast(obj)



