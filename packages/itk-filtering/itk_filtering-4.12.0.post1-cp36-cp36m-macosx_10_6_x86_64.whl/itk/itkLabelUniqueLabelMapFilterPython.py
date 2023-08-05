# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelUniqueLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLabelUniqueLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLabelUniqueLabelMapFilterPython')
    _itkLabelUniqueLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelUniqueLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelUniqueLabelMapFilterPython
            return _itkLabelUniqueLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkLabelUniqueLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLabelUniqueLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelUniqueLabelMapFilterPython
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

def itkLabelUniqueLabelMapFilterLM3_New():
  return itkLabelUniqueLabelMapFilterLM3.New()


def itkLabelUniqueLabelMapFilterLM3_Superclass_New():
  return itkLabelUniqueLabelMapFilterLM3_Superclass.New()


def itkLabelUniqueLabelMapFilterLM2_New():
  return itkLabelUniqueLabelMapFilterLM2.New()


def itkLabelUniqueLabelMapFilterLM2_Superclass_New():
  return itkLabelUniqueLabelMapFilterLM2_Superclass.New()

class itkLabelUniqueLabelMapFilterLM2_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkLabelUniqueLabelMapFilterLM2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelUniqueLabelMapFilterLM2_Superclass_Pointer":
        """__New_orig__() -> itkLabelUniqueLabelMapFilterLM2_Superclass_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelUniqueLabelMapFilterLM2_Superclass_Pointer":
        """Clone(itkLabelUniqueLabelMapFilterLM2_Superclass self) -> itkLabelUniqueLabelMapFilterLM2_Superclass_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkLabelUniqueLabelMapFilterLM2_Superclass self, bool const _arg)"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkLabelUniqueLabelMapFilterLM2_Superclass self) -> bool const &"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkLabelUniqueLabelMapFilterLM2_Superclass self)"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkLabelUniqueLabelMapFilterLM2_Superclass self)"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_ReverseOrderingOff(self)

    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM2_Superclass

    def cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM2_Superclass *":
        """cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM2_Superclass"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelUniqueLabelMapFilterLM2_Superclass *":
        """GetPointer(itkLabelUniqueLabelMapFilterLM2_Superclass self) -> itkLabelUniqueLabelMapFilterLM2_Superclass"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM2_Superclass

        Create a new object of the class itkLabelUniqueLabelMapFilterLM2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelUniqueLabelMapFilterLM2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelUniqueLabelMapFilterLM2_Superclass.Clone = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_Clone, None, itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass.SetReverseOrdering = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_SetReverseOrdering, None, itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass.GetReverseOrdering = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_GetReverseOrdering, None, itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass.ReverseOrderingOn = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_ReverseOrderingOn, None, itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass.ReverseOrderingOff = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_ReverseOrderingOff, None, itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass.GetPointer = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_GetPointer, None, itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass_swigregister = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_swigregister
itkLabelUniqueLabelMapFilterLM2_Superclass_swigregister(itkLabelUniqueLabelMapFilterLM2_Superclass)

def itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__() -> "itkLabelUniqueLabelMapFilterLM2_Superclass_Pointer":
    """itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__() -> itkLabelUniqueLabelMapFilterLM2_Superclass_Pointer"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__()

def itkLabelUniqueLabelMapFilterLM2_Superclass_cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM2_Superclass *":
    """itkLabelUniqueLabelMapFilterLM2_Superclass_cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM2_Superclass"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_cast(obj)

class itkLabelUniqueLabelMapFilterLM3_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkLabelUniqueLabelMapFilterLM3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelUniqueLabelMapFilterLM3_Superclass_Pointer":
        """__New_orig__() -> itkLabelUniqueLabelMapFilterLM3_Superclass_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelUniqueLabelMapFilterLM3_Superclass_Pointer":
        """Clone(itkLabelUniqueLabelMapFilterLM3_Superclass self) -> itkLabelUniqueLabelMapFilterLM3_Superclass_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkLabelUniqueLabelMapFilterLM3_Superclass self, bool const _arg)"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkLabelUniqueLabelMapFilterLM3_Superclass self) -> bool const &"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkLabelUniqueLabelMapFilterLM3_Superclass self)"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkLabelUniqueLabelMapFilterLM3_Superclass self)"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_ReverseOrderingOff(self)

    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM3_Superclass

    def cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM3_Superclass *":
        """cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM3_Superclass"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelUniqueLabelMapFilterLM3_Superclass *":
        """GetPointer(itkLabelUniqueLabelMapFilterLM3_Superclass self) -> itkLabelUniqueLabelMapFilterLM3_Superclass"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM3_Superclass

        Create a new object of the class itkLabelUniqueLabelMapFilterLM3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelUniqueLabelMapFilterLM3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelUniqueLabelMapFilterLM3_Superclass.Clone = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_Clone, None, itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass.SetReverseOrdering = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_SetReverseOrdering, None, itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass.GetReverseOrdering = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_GetReverseOrdering, None, itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass.ReverseOrderingOn = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_ReverseOrderingOn, None, itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass.ReverseOrderingOff = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_ReverseOrderingOff, None, itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass.GetPointer = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_GetPointer, None, itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass_swigregister = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_swigregister
itkLabelUniqueLabelMapFilterLM3_Superclass_swigregister(itkLabelUniqueLabelMapFilterLM3_Superclass)

def itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__() -> "itkLabelUniqueLabelMapFilterLM3_Superclass_Pointer":
    """itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__() -> itkLabelUniqueLabelMapFilterLM3_Superclass_Pointer"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__()

def itkLabelUniqueLabelMapFilterLM3_Superclass_cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM3_Superclass *":
    """itkLabelUniqueLabelMapFilterLM3_Superclass_cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM3_Superclass"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_cast(obj)

class itkLabelUniqueLabelMapFilterLM2(itkLabelUniqueLabelMapFilterLM2_Superclass):
    """Proxy of C++ itkLabelUniqueLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelUniqueLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkLabelUniqueLabelMapFilterLM2_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelUniqueLabelMapFilterLM2_Pointer":
        """Clone(itkLabelUniqueLabelMapFilterLM2 self) -> itkLabelUniqueLabelMapFilterLM2_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Clone(self)

    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM2"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelUniqueLabelMapFilterLM2 *":
        """GetPointer(itkLabelUniqueLabelMapFilterLM2 self) -> itkLabelUniqueLabelMapFilterLM2"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM2

        Create a new object of the class itkLabelUniqueLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelUniqueLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelUniqueLabelMapFilterLM2.Clone = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Clone, None, itkLabelUniqueLabelMapFilterLM2)
itkLabelUniqueLabelMapFilterLM2.GetPointer = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_GetPointer, None, itkLabelUniqueLabelMapFilterLM2)
itkLabelUniqueLabelMapFilterLM2_swigregister = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_swigregister
itkLabelUniqueLabelMapFilterLM2_swigregister(itkLabelUniqueLabelMapFilterLM2)

def itkLabelUniqueLabelMapFilterLM2___New_orig__() -> "itkLabelUniqueLabelMapFilterLM2_Pointer":
    """itkLabelUniqueLabelMapFilterLM2___New_orig__() -> itkLabelUniqueLabelMapFilterLM2_Pointer"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2___New_orig__()

def itkLabelUniqueLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM2 *":
    """itkLabelUniqueLabelMapFilterLM2_cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM2"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_cast(obj)

class itkLabelUniqueLabelMapFilterLM3(itkLabelUniqueLabelMapFilterLM3_Superclass):
    """Proxy of C++ itkLabelUniqueLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelUniqueLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkLabelUniqueLabelMapFilterLM3_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelUniqueLabelMapFilterLM3_Pointer":
        """Clone(itkLabelUniqueLabelMapFilterLM3 self) -> itkLabelUniqueLabelMapFilterLM3_Pointer"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Clone(self)

    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM3"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelUniqueLabelMapFilterLM3 *":
        """GetPointer(itkLabelUniqueLabelMapFilterLM3 self) -> itkLabelUniqueLabelMapFilterLM3"""
        return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM3

        Create a new object of the class itkLabelUniqueLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelUniqueLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelUniqueLabelMapFilterLM3.Clone = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Clone, None, itkLabelUniqueLabelMapFilterLM3)
itkLabelUniqueLabelMapFilterLM3.GetPointer = new_instancemethod(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_GetPointer, None, itkLabelUniqueLabelMapFilterLM3)
itkLabelUniqueLabelMapFilterLM3_swigregister = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_swigregister
itkLabelUniqueLabelMapFilterLM3_swigregister(itkLabelUniqueLabelMapFilterLM3)

def itkLabelUniqueLabelMapFilterLM3___New_orig__() -> "itkLabelUniqueLabelMapFilterLM3_Pointer":
    """itkLabelUniqueLabelMapFilterLM3___New_orig__() -> itkLabelUniqueLabelMapFilterLM3_Pointer"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3___New_orig__()

def itkLabelUniqueLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkLabelUniqueLabelMapFilterLM3 *":
    """itkLabelUniqueLabelMapFilterLM3_cast(itkLightObject obj) -> itkLabelUniqueLabelMapFilterLM3"""
    return _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_cast(obj)



