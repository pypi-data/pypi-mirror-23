# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNarrowBandImageFilterBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNarrowBandImageFilterBasePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNarrowBandImageFilterBasePython')
    _itkNarrowBandImageFilterBasePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNarrowBandImageFilterBasePython', [dirname(__file__)])
        except ImportError:
            import _itkNarrowBandImageFilterBasePython
            return _itkNarrowBandImageFilterBasePython
        try:
            _mod = imp.load_module('_itkNarrowBandImageFilterBasePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNarrowBandImageFilterBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNarrowBandImageFilterBasePython
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


import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython
import ITKNarrowBandBasePython

def itkNarrowBandImageFilterBaseIF3IF3_New():
  return itkNarrowBandImageFilterBaseIF3IF3.New()


def itkNarrowBandImageFilterBaseIF2IF2_New():
  return itkNarrowBandImageFilterBaseIF2IF2.New()

class itkNarrowBandImageFilterBaseIF2IF2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF2IF2):
    """Proxy of C++ itkNarrowBandImageFilterBaseIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetIsoSurfaceValue(self, _arg: 'float const') -> "void":
        """SetIsoSurfaceValue(itkNarrowBandImageFilterBaseIF2IF2 self, float const _arg)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetIsoSurfaceValue(self, _arg)


    def GetIsoSurfaceValue(self) -> "float":
        """GetIsoSurfaceValue(itkNarrowBandImageFilterBaseIF2IF2 self) -> float"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetIsoSurfaceValue(self)


    def InsertNarrowBandNode(self, *args) -> "void":
        """
        InsertNarrowBandNode(itkNarrowBandImageFilterBaseIF2IF2 self, itkBandNodeI2F node)
        InsertNarrowBandNode(itkNarrowBandImageFilterBaseIF2IF2 self, itkIndex2 index)
        InsertNarrowBandNode(itkNarrowBandImageFilterBaseIF2IF2 self, itkIndex2 index, float const & value, signed char const & nodestate)
        """
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_InsertNarrowBandNode(self, *args)


    def SetNarrowBandTotalRadius(self, val: 'float const &') -> "void":
        """SetNarrowBandTotalRadius(itkNarrowBandImageFilterBaseIF2IF2 self, float const & val)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandTotalRadius(self, val)


    def GetNarrowBandTotalRadius(self) -> "float":
        """GetNarrowBandTotalRadius(itkNarrowBandImageFilterBaseIF2IF2 self) -> float"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandTotalRadius(self)


    def SetNarrowBandInnerRadius(self, val: 'float const &') -> "void":
        """SetNarrowBandInnerRadius(itkNarrowBandImageFilterBaseIF2IF2 self, float const & val)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandInnerRadius(self, val)


    def GetNarrowBandInnerRadius(self) -> "float":
        """GetNarrowBandInnerRadius(itkNarrowBandImageFilterBaseIF2IF2 self) -> float"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandInnerRadius(self)


    def CreateNarrowBand(self) -> "void":
        """CreateNarrowBand(itkNarrowBandImageFilterBaseIF2IF2 self)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CreateNarrowBand(self)


    def SetNarrowBand(self, ptr: 'itkNarrowBandBNI2F') -> "void":
        """SetNarrowBand(itkNarrowBandImageFilterBaseIF2IF2 self, itkNarrowBandBNI2F ptr)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBand(self, ptr)


    def CopyInputToOutput(self) -> "void":
        """CopyInputToOutput(itkNarrowBandImageFilterBaseIF2IF2 self)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CopyInputToOutput(self)

    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF2IF2

    def cast(obj: 'itkLightObject') -> "itkNarrowBandImageFilterBaseIF2IF2 *":
        """cast(itkLightObject obj) -> itkNarrowBandImageFilterBaseIF2IF2"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNarrowBandImageFilterBaseIF2IF2 *":
        """GetPointer(itkNarrowBandImageFilterBaseIF2IF2 self) -> itkNarrowBandImageFilterBaseIF2IF2"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNarrowBandImageFilterBaseIF2IF2

        Create a new object of the class itkNarrowBandImageFilterBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandImageFilterBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandImageFilterBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandImageFilterBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandImageFilterBaseIF2IF2.SetIsoSurfaceValue = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetIsoSurfaceValue, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.GetIsoSurfaceValue = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetIsoSurfaceValue, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.InsertNarrowBandNode = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_InsertNarrowBandNode, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.SetNarrowBandTotalRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandTotalRadius, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.GetNarrowBandTotalRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandTotalRadius, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.SetNarrowBandInnerRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandInnerRadius, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.GetNarrowBandInnerRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandInnerRadius, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.CreateNarrowBand = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CreateNarrowBand, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.SetNarrowBand = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBand, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.CopyInputToOutput = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CopyInputToOutput, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2.GetPointer = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetPointer, None, itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2_swigregister = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_swigregister
itkNarrowBandImageFilterBaseIF2IF2_swigregister(itkNarrowBandImageFilterBaseIF2IF2)

def itkNarrowBandImageFilterBaseIF2IF2_cast(obj: 'itkLightObject') -> "itkNarrowBandImageFilterBaseIF2IF2 *":
    """itkNarrowBandImageFilterBaseIF2IF2_cast(itkLightObject obj) -> itkNarrowBandImageFilterBaseIF2IF2"""
    return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_cast(obj)

class itkNarrowBandImageFilterBaseIF3IF3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF3IF3):
    """Proxy of C++ itkNarrowBandImageFilterBaseIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetIsoSurfaceValue(self, _arg: 'float const') -> "void":
        """SetIsoSurfaceValue(itkNarrowBandImageFilterBaseIF3IF3 self, float const _arg)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetIsoSurfaceValue(self, _arg)


    def GetIsoSurfaceValue(self) -> "float":
        """GetIsoSurfaceValue(itkNarrowBandImageFilterBaseIF3IF3 self) -> float"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetIsoSurfaceValue(self)


    def InsertNarrowBandNode(self, *args) -> "void":
        """
        InsertNarrowBandNode(itkNarrowBandImageFilterBaseIF3IF3 self, itkBandNodeI3F node)
        InsertNarrowBandNode(itkNarrowBandImageFilterBaseIF3IF3 self, itkIndex3 index)
        InsertNarrowBandNode(itkNarrowBandImageFilterBaseIF3IF3 self, itkIndex3 index, float const & value, signed char const & nodestate)
        """
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_InsertNarrowBandNode(self, *args)


    def SetNarrowBandTotalRadius(self, val: 'float const &') -> "void":
        """SetNarrowBandTotalRadius(itkNarrowBandImageFilterBaseIF3IF3 self, float const & val)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandTotalRadius(self, val)


    def GetNarrowBandTotalRadius(self) -> "float":
        """GetNarrowBandTotalRadius(itkNarrowBandImageFilterBaseIF3IF3 self) -> float"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandTotalRadius(self)


    def SetNarrowBandInnerRadius(self, val: 'float const &') -> "void":
        """SetNarrowBandInnerRadius(itkNarrowBandImageFilterBaseIF3IF3 self, float const & val)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandInnerRadius(self, val)


    def GetNarrowBandInnerRadius(self) -> "float":
        """GetNarrowBandInnerRadius(itkNarrowBandImageFilterBaseIF3IF3 self) -> float"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandInnerRadius(self)


    def CreateNarrowBand(self) -> "void":
        """CreateNarrowBand(itkNarrowBandImageFilterBaseIF3IF3 self)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CreateNarrowBand(self)


    def SetNarrowBand(self, ptr: 'itkNarrowBandBNI3F') -> "void":
        """SetNarrowBand(itkNarrowBandImageFilterBaseIF3IF3 self, itkNarrowBandBNI3F ptr)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBand(self, ptr)


    def CopyInputToOutput(self) -> "void":
        """CopyInputToOutput(itkNarrowBandImageFilterBaseIF3IF3 self)"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CopyInputToOutput(self)

    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF3IF3

    def cast(obj: 'itkLightObject') -> "itkNarrowBandImageFilterBaseIF3IF3 *":
        """cast(itkLightObject obj) -> itkNarrowBandImageFilterBaseIF3IF3"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNarrowBandImageFilterBaseIF3IF3 *":
        """GetPointer(itkNarrowBandImageFilterBaseIF3IF3 self) -> itkNarrowBandImageFilterBaseIF3IF3"""
        return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNarrowBandImageFilterBaseIF3IF3

        Create a new object of the class itkNarrowBandImageFilterBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandImageFilterBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandImageFilterBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandImageFilterBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandImageFilterBaseIF3IF3.SetIsoSurfaceValue = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetIsoSurfaceValue, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.GetIsoSurfaceValue = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetIsoSurfaceValue, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.InsertNarrowBandNode = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_InsertNarrowBandNode, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.SetNarrowBandTotalRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandTotalRadius, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.GetNarrowBandTotalRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandTotalRadius, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.SetNarrowBandInnerRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandInnerRadius, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.GetNarrowBandInnerRadius = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandInnerRadius, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.CreateNarrowBand = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CreateNarrowBand, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.SetNarrowBand = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBand, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.CopyInputToOutput = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CopyInputToOutput, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3.GetPointer = new_instancemethod(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetPointer, None, itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3_swigregister = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_swigregister
itkNarrowBandImageFilterBaseIF3IF3_swigregister(itkNarrowBandImageFilterBaseIF3IF3)

def itkNarrowBandImageFilterBaseIF3IF3_cast(obj: 'itkLightObject') -> "itkNarrowBandImageFilterBaseIF3IF3 *":
    """itkNarrowBandImageFilterBaseIF3IF3_cast(itkLightObject obj) -> itkNarrowBandImageFilterBaseIF3IF3"""
    return _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_cast(obj)



