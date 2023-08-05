# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSparseFieldLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSparseFieldLevelSetImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSparseFieldLevelSetImageFilterPython')
    _itkSparseFieldLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSparseFieldLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSparseFieldLevelSetImageFilterPython
            return _itkSparseFieldLevelSetImageFilterPython
        try:
            _mod = imp.load_module('_itkSparseFieldLevelSetImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSparseFieldLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSparseFieldLevelSetImageFilterPython
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
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython

def itkSparseFieldLayerSFLSNI3_New():
  return itkSparseFieldLayerSFLSNI3.New()


def itkSparseFieldLayerSFLSNI2_New():
  return itkSparseFieldLayerSFLSNI2.New()


def itkSparseFieldLevelSetImageFilterIF3IF3_New():
  return itkSparseFieldLevelSetImageFilterIF3IF3.New()


def itkSparseFieldLevelSetImageFilterIF2IF2_New():
  return itkSparseFieldLevelSetImageFilterIF2IF2.New()

class itkSparseFieldLayerSFLSNI2(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkSparseFieldLayerSFLSNI2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSparseFieldLayerSFLSNI2_Pointer":
        """__New_orig__() -> itkSparseFieldLayerSFLSNI2_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSparseFieldLayerSFLSNI2_Pointer":
        """Clone(itkSparseFieldLayerSFLSNI2 self) -> itkSparseFieldLayerSFLSNI2_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Clone(self)


    def Front(self, *args) -> "itkSparseFieldLevelSetNodeI2 const *":
        """
        Front(itkSparseFieldLayerSFLSNI2 self) -> itkSparseFieldLevelSetNodeI2
        Front(itkSparseFieldLayerSFLSNI2 self) -> itkSparseFieldLevelSetNodeI2
        """
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Front(self, *args)


    def PopFront(self) -> "void":
        """PopFront(itkSparseFieldLayerSFLSNI2 self)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_PopFront(self)


    def PushFront(self, n: 'itkSparseFieldLevelSetNodeI2') -> "void":
        """PushFront(itkSparseFieldLayerSFLSNI2 self, itkSparseFieldLevelSetNodeI2 n)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_PushFront(self, n)


    def Unlink(self, n: 'itkSparseFieldLevelSetNodeI2') -> "void":
        """Unlink(itkSparseFieldLayerSFLSNI2 self, itkSparseFieldLevelSetNodeI2 n)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Unlink(self, n)


    def Empty(self) -> "bool":
        """Empty(itkSparseFieldLayerSFLSNI2 self) -> bool"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Empty(self)


    def Size(self) -> "unsigned int":
        """Size(itkSparseFieldLayerSFLSNI2 self) -> unsigned int"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Size(self)


    def SplitRegions(self, num: 'int') -> "std::vector< itkSparseFieldLayerSFLSNI2::RegionType,std::allocator< itkSparseFieldLayerSFLSNI2::RegionType > >":
        """SplitRegions(itkSparseFieldLayerSFLSNI2 self, int num) -> std::vector< itkSparseFieldLayerSFLSNI2::RegionType,std::allocator< itkSparseFieldLayerSFLSNI2::RegionType > >"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_SplitRegions(self, num)

    __swig_destroy__ = _itkSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLayerSFLSNI2

    def cast(obj: 'itkLightObject') -> "itkSparseFieldLayerSFLSNI2 *":
        """cast(itkLightObject obj) -> itkSparseFieldLayerSFLSNI2"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSparseFieldLayerSFLSNI2 *":
        """GetPointer(itkSparseFieldLayerSFLSNI2 self) -> itkSparseFieldLayerSFLSNI2"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSparseFieldLayerSFLSNI2

        Create a new object of the class itkSparseFieldLayerSFLSNI2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLayerSFLSNI2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLayerSFLSNI2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLayerSFLSNI2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSparseFieldLayerSFLSNI2.Clone = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Clone, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.Front = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Front, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.PopFront = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_PopFront, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.PushFront = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_PushFront, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.Unlink = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Unlink, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.Empty = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Empty, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.Size = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_Size, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.SplitRegions = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_SplitRegions, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2.GetPointer = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_GetPointer, None, itkSparseFieldLayerSFLSNI2)
itkSparseFieldLayerSFLSNI2_swigregister = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_swigregister
itkSparseFieldLayerSFLSNI2_swigregister(itkSparseFieldLayerSFLSNI2)

def itkSparseFieldLayerSFLSNI2___New_orig__() -> "itkSparseFieldLayerSFLSNI2_Pointer":
    """itkSparseFieldLayerSFLSNI2___New_orig__() -> itkSparseFieldLayerSFLSNI2_Pointer"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2___New_orig__()

def itkSparseFieldLayerSFLSNI2_cast(obj: 'itkLightObject') -> "itkSparseFieldLayerSFLSNI2 *":
    """itkSparseFieldLayerSFLSNI2_cast(itkLightObject obj) -> itkSparseFieldLayerSFLSNI2"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI2_cast(obj)

class itkSparseFieldLayerSFLSNI3(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkSparseFieldLayerSFLSNI3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSparseFieldLayerSFLSNI3_Pointer":
        """__New_orig__() -> itkSparseFieldLayerSFLSNI3_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSparseFieldLayerSFLSNI3_Pointer":
        """Clone(itkSparseFieldLayerSFLSNI3 self) -> itkSparseFieldLayerSFLSNI3_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Clone(self)


    def Front(self, *args) -> "itkSparseFieldLevelSetNodeI3 const *":
        """
        Front(itkSparseFieldLayerSFLSNI3 self) -> itkSparseFieldLevelSetNodeI3
        Front(itkSparseFieldLayerSFLSNI3 self) -> itkSparseFieldLevelSetNodeI3
        """
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Front(self, *args)


    def PopFront(self) -> "void":
        """PopFront(itkSparseFieldLayerSFLSNI3 self)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_PopFront(self)


    def PushFront(self, n: 'itkSparseFieldLevelSetNodeI3') -> "void":
        """PushFront(itkSparseFieldLayerSFLSNI3 self, itkSparseFieldLevelSetNodeI3 n)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_PushFront(self, n)


    def Unlink(self, n: 'itkSparseFieldLevelSetNodeI3') -> "void":
        """Unlink(itkSparseFieldLayerSFLSNI3 self, itkSparseFieldLevelSetNodeI3 n)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Unlink(self, n)


    def Empty(self) -> "bool":
        """Empty(itkSparseFieldLayerSFLSNI3 self) -> bool"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Empty(self)


    def Size(self) -> "unsigned int":
        """Size(itkSparseFieldLayerSFLSNI3 self) -> unsigned int"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Size(self)


    def SplitRegions(self, num: 'int') -> "std::vector< itkSparseFieldLayerSFLSNI3::RegionType,std::allocator< itkSparseFieldLayerSFLSNI3::RegionType > >":
        """SplitRegions(itkSparseFieldLayerSFLSNI3 self, int num) -> std::vector< itkSparseFieldLayerSFLSNI3::RegionType,std::allocator< itkSparseFieldLayerSFLSNI3::RegionType > >"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_SplitRegions(self, num)

    __swig_destroy__ = _itkSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLayerSFLSNI3

    def cast(obj: 'itkLightObject') -> "itkSparseFieldLayerSFLSNI3 *":
        """cast(itkLightObject obj) -> itkSparseFieldLayerSFLSNI3"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSparseFieldLayerSFLSNI3 *":
        """GetPointer(itkSparseFieldLayerSFLSNI3 self) -> itkSparseFieldLayerSFLSNI3"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSparseFieldLayerSFLSNI3

        Create a new object of the class itkSparseFieldLayerSFLSNI3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLayerSFLSNI3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLayerSFLSNI3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLayerSFLSNI3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSparseFieldLayerSFLSNI3.Clone = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Clone, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.Front = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Front, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.PopFront = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_PopFront, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.PushFront = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_PushFront, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.Unlink = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Unlink, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.Empty = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Empty, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.Size = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_Size, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.SplitRegions = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_SplitRegions, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3.GetPointer = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_GetPointer, None, itkSparseFieldLayerSFLSNI3)
itkSparseFieldLayerSFLSNI3_swigregister = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_swigregister
itkSparseFieldLayerSFLSNI3_swigregister(itkSparseFieldLayerSFLSNI3)

def itkSparseFieldLayerSFLSNI3___New_orig__() -> "itkSparseFieldLayerSFLSNI3_Pointer":
    """itkSparseFieldLayerSFLSNI3___New_orig__() -> itkSparseFieldLayerSFLSNI3_Pointer"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3___New_orig__()

def itkSparseFieldLayerSFLSNI3_cast(obj: 'itkLightObject') -> "itkSparseFieldLayerSFLSNI3 *":
    """itkSparseFieldLayerSFLSNI3_cast(itkLightObject obj) -> itkSparseFieldLayerSFLSNI3"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerSFLSNI3_cast(obj)

class itkSparseFieldLevelSetImageFilterIF2IF2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF2IF2):
    """Proxy of C++ itkSparseFieldLevelSetImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSparseFieldLevelSetImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSparseFieldLevelSetImageFilterIF2IF2_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSparseFieldLevelSetImageFilterIF2IF2_Pointer":
        """Clone(itkSparseFieldLevelSetImageFilterIF2IF2 self) -> itkSparseFieldLevelSetImageFilterIF2IF2_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_Clone(self)


    def SetNumberOfLayers(self, _arg: 'unsigned int const') -> "void":
        """SetNumberOfLayers(itkSparseFieldLevelSetImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_SetNumberOfLayers(self, _arg)


    def GetNumberOfLayers(self) -> "unsigned int":
        """GetNumberOfLayers(itkSparseFieldLevelSetImageFilterIF2IF2 self) -> unsigned int"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetNumberOfLayers(self)


    def SetIsoSurfaceValue(self, _arg: 'float const') -> "void":
        """SetIsoSurfaceValue(itkSparseFieldLevelSetImageFilterIF2IF2 self, float const _arg)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_SetIsoSurfaceValue(self, _arg)


    def GetIsoSurfaceValue(self) -> "float":
        """GetIsoSurfaceValue(itkSparseFieldLevelSetImageFilterIF2IF2 self) -> float"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetIsoSurfaceValue(self)


    def SetInterpolateSurfaceLocation(self, _arg: 'bool const') -> "void":
        """SetInterpolateSurfaceLocation(itkSparseFieldLevelSetImageFilterIF2IF2 self, bool const _arg)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_SetInterpolateSurfaceLocation(self, _arg)


    def GetInterpolateSurfaceLocation(self) -> "bool":
        """GetInterpolateSurfaceLocation(itkSparseFieldLevelSetImageFilterIF2IF2 self) -> bool"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetInterpolateSurfaceLocation(self)


    def InterpolateSurfaceLocationOn(self) -> "void":
        """InterpolateSurfaceLocationOn(itkSparseFieldLevelSetImageFilterIF2IF2 self)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_InterpolateSurfaceLocationOn(self)


    def InterpolateSurfaceLocationOff(self) -> "void":
        """InterpolateSurfaceLocationOff(itkSparseFieldLevelSetImageFilterIF2IF2 self)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_InterpolateSurfaceLocationOff(self)

    OutputEqualityComparableCheck = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_OutputEqualityComparableCheck
    DoubleConvertibleToOutputCheck = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    OutputOStreamWritableCheck = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_OutputOStreamWritableCheck
    __swig_destroy__ = _itkSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLevelSetImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSparseFieldLevelSetImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSparseFieldLevelSetImageFilterIF2IF2"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSparseFieldLevelSetImageFilterIF2IF2 *":
        """GetPointer(itkSparseFieldLevelSetImageFilterIF2IF2 self) -> itkSparseFieldLevelSetImageFilterIF2IF2"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSparseFieldLevelSetImageFilterIF2IF2

        Create a new object of the class itkSparseFieldLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSparseFieldLevelSetImageFilterIF2IF2.Clone = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_Clone, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.SetNumberOfLayers = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_SetNumberOfLayers, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.GetNumberOfLayers = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetNumberOfLayers, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.SetIsoSurfaceValue = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_SetIsoSurfaceValue, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.GetIsoSurfaceValue = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetIsoSurfaceValue, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.SetInterpolateSurfaceLocation = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_SetInterpolateSurfaceLocation, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.GetInterpolateSurfaceLocation = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetInterpolateSurfaceLocation, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.InterpolateSurfaceLocationOn = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_InterpolateSurfaceLocationOn, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.InterpolateSurfaceLocationOff = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_InterpolateSurfaceLocationOff, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2.GetPointer = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_GetPointer, None, itkSparseFieldLevelSetImageFilterIF2IF2)
itkSparseFieldLevelSetImageFilterIF2IF2_swigregister = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_swigregister
itkSparseFieldLevelSetImageFilterIF2IF2_swigregister(itkSparseFieldLevelSetImageFilterIF2IF2)

def itkSparseFieldLevelSetImageFilterIF2IF2___New_orig__() -> "itkSparseFieldLevelSetImageFilterIF2IF2_Pointer":
    """itkSparseFieldLevelSetImageFilterIF2IF2___New_orig__() -> itkSparseFieldLevelSetImageFilterIF2IF2_Pointer"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2___New_orig__()

def itkSparseFieldLevelSetImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSparseFieldLevelSetImageFilterIF2IF2 *":
    """itkSparseFieldLevelSetImageFilterIF2IF2_cast(itkLightObject obj) -> itkSparseFieldLevelSetImageFilterIF2IF2"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF2IF2_cast(obj)

class itkSparseFieldLevelSetImageFilterIF3IF3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF3IF3):
    """Proxy of C++ itkSparseFieldLevelSetImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSparseFieldLevelSetImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSparseFieldLevelSetImageFilterIF3IF3_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSparseFieldLevelSetImageFilterIF3IF3_Pointer":
        """Clone(itkSparseFieldLevelSetImageFilterIF3IF3 self) -> itkSparseFieldLevelSetImageFilterIF3IF3_Pointer"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_Clone(self)


    def SetNumberOfLayers(self, _arg: 'unsigned int const') -> "void":
        """SetNumberOfLayers(itkSparseFieldLevelSetImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_SetNumberOfLayers(self, _arg)


    def GetNumberOfLayers(self) -> "unsigned int":
        """GetNumberOfLayers(itkSparseFieldLevelSetImageFilterIF3IF3 self) -> unsigned int"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetNumberOfLayers(self)


    def SetIsoSurfaceValue(self, _arg: 'float const') -> "void":
        """SetIsoSurfaceValue(itkSparseFieldLevelSetImageFilterIF3IF3 self, float const _arg)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_SetIsoSurfaceValue(self, _arg)


    def GetIsoSurfaceValue(self) -> "float":
        """GetIsoSurfaceValue(itkSparseFieldLevelSetImageFilterIF3IF3 self) -> float"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetIsoSurfaceValue(self)


    def SetInterpolateSurfaceLocation(self, _arg: 'bool const') -> "void":
        """SetInterpolateSurfaceLocation(itkSparseFieldLevelSetImageFilterIF3IF3 self, bool const _arg)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_SetInterpolateSurfaceLocation(self, _arg)


    def GetInterpolateSurfaceLocation(self) -> "bool":
        """GetInterpolateSurfaceLocation(itkSparseFieldLevelSetImageFilterIF3IF3 self) -> bool"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetInterpolateSurfaceLocation(self)


    def InterpolateSurfaceLocationOn(self) -> "void":
        """InterpolateSurfaceLocationOn(itkSparseFieldLevelSetImageFilterIF3IF3 self)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_InterpolateSurfaceLocationOn(self)


    def InterpolateSurfaceLocationOff(self) -> "void":
        """InterpolateSurfaceLocationOff(itkSparseFieldLevelSetImageFilterIF3IF3 self)"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_InterpolateSurfaceLocationOff(self)

    OutputEqualityComparableCheck = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_OutputEqualityComparableCheck
    DoubleConvertibleToOutputCheck = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    OutputOStreamWritableCheck = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_OutputOStreamWritableCheck
    __swig_destroy__ = _itkSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLevelSetImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSparseFieldLevelSetImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSparseFieldLevelSetImageFilterIF3IF3"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSparseFieldLevelSetImageFilterIF3IF3 *":
        """GetPointer(itkSparseFieldLevelSetImageFilterIF3IF3 self) -> itkSparseFieldLevelSetImageFilterIF3IF3"""
        return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSparseFieldLevelSetImageFilterIF3IF3

        Create a new object of the class itkSparseFieldLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSparseFieldLevelSetImageFilterIF3IF3.Clone = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_Clone, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.SetNumberOfLayers = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_SetNumberOfLayers, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.GetNumberOfLayers = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetNumberOfLayers, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.SetIsoSurfaceValue = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_SetIsoSurfaceValue, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.GetIsoSurfaceValue = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetIsoSurfaceValue, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.SetInterpolateSurfaceLocation = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_SetInterpolateSurfaceLocation, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.GetInterpolateSurfaceLocation = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetInterpolateSurfaceLocation, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.InterpolateSurfaceLocationOn = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_InterpolateSurfaceLocationOn, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.InterpolateSurfaceLocationOff = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_InterpolateSurfaceLocationOff, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3.GetPointer = new_instancemethod(_itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_GetPointer, None, itkSparseFieldLevelSetImageFilterIF3IF3)
itkSparseFieldLevelSetImageFilterIF3IF3_swigregister = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_swigregister
itkSparseFieldLevelSetImageFilterIF3IF3_swigregister(itkSparseFieldLevelSetImageFilterIF3IF3)

def itkSparseFieldLevelSetImageFilterIF3IF3___New_orig__() -> "itkSparseFieldLevelSetImageFilterIF3IF3_Pointer":
    """itkSparseFieldLevelSetImageFilterIF3IF3___New_orig__() -> itkSparseFieldLevelSetImageFilterIF3IF3_Pointer"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3___New_orig__()

def itkSparseFieldLevelSetImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSparseFieldLevelSetImageFilterIF3IF3 *":
    """itkSparseFieldLevelSetImageFilterIF3IF3_cast(itkLightObject obj) -> itkSparseFieldLevelSetImageFilterIF3IF3"""
    return _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetImageFilterIF3IF3_cast(obj)

class itkSparseFieldLevelSetNodeI2(object):
    """Proxy of C++ itkSparseFieldLevelSetNodeI2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkSparseFieldLevelSetNodeI2 self) -> itkSparseFieldLevelSetNodeI2
        __init__(itkSparseFieldLevelSetNodeI2 self, itkSparseFieldLevelSetNodeI2 arg0) -> itkSparseFieldLevelSetNodeI2
        """
        _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetNodeI2_swiginit(self, _itkSparseFieldLevelSetImageFilterPython.new_itkSparseFieldLevelSetNodeI2(*args))
    __swig_destroy__ = _itkSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLevelSetNodeI2
itkSparseFieldLevelSetNodeI2_swigregister = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetNodeI2_swigregister
itkSparseFieldLevelSetNodeI2_swigregister(itkSparseFieldLevelSetNodeI2)

class itkSparseFieldLevelSetNodeI3(object):
    """Proxy of C++ itkSparseFieldLevelSetNodeI3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkSparseFieldLevelSetNodeI3 self) -> itkSparseFieldLevelSetNodeI3
        __init__(itkSparseFieldLevelSetNodeI3 self, itkSparseFieldLevelSetNodeI3 arg0) -> itkSparseFieldLevelSetNodeI3
        """
        _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetNodeI3_swiginit(self, _itkSparseFieldLevelSetImageFilterPython.new_itkSparseFieldLevelSetNodeI3(*args))
    __swig_destroy__ = _itkSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLevelSetNodeI3
itkSparseFieldLevelSetNodeI3_swigregister = _itkSparseFieldLevelSetImageFilterPython.itkSparseFieldLevelSetNodeI3_swigregister
itkSparseFieldLevelSetNodeI3_swigregister(itkSparseFieldLevelSetNodeI3)



