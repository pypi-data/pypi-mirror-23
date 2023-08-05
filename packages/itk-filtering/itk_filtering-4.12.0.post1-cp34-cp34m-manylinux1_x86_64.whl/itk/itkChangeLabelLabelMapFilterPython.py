# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkChangeLabelLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkChangeLabelLabelMapFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkChangeLabelLabelMapFilterPython')
    _itkChangeLabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkChangeLabelLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkChangeLabelLabelMapFilterPython
            return _itkChangeLabelLabelMapFilterPython
        try:
            _mod = imp.load_module('_itkChangeLabelLabelMapFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkChangeLabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkChangeLabelLabelMapFilterPython
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
import itkLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkOptimizerParametersPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython
import itkArrayPython
import itkCovariantVectorPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkPointPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkLabelObjectPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkLabelObjectLinePython
import itkImageRegionPython
import itkHistogramPython
import itkSamplePython
import ITKLabelMapBasePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkImageSourceCommonPython

def itkChangeLabelLabelMapFilterLM3_New():
  return itkChangeLabelLabelMapFilterLM3.New()


def itkChangeLabelLabelMapFilterLM2_New():
  return itkChangeLabelLabelMapFilterLM2.New()

class itkChangeLabelLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkChangeLabelLabelMapFilterLM2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkChangeLabelLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkChangeLabelLabelMapFilterLM2_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkChangeLabelLabelMapFilterLM2_Pointer":
        """Clone(itkChangeLabelLabelMapFilterLM2 self) -> itkChangeLabelLabelMapFilterLM2_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_Clone(self)


    def SetChangeMap(self, changeMap: 'mapULUL') -> "void":
        """SetChangeMap(itkChangeLabelLabelMapFilterLM2 self, mapULUL changeMap)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChangeMap(self, changeMap)


    def GetChangeMap(self) -> "std::map< unsigned long,unsigned long,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,unsigned long > > > const &":
        """GetChangeMap(itkChangeLabelLabelMapFilterLM2 self) -> mapULUL"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetChangeMap(self)


    def SetChange(self, oldLabel: 'unsigned long const &', newLabel: 'unsigned long const &') -> "void":
        """SetChange(itkChangeLabelLabelMapFilterLM2 self, unsigned long const & oldLabel, unsigned long const & newLabel)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChange(self, oldLabel, newLabel)


    def ClearChangeMap(self) -> "void":
        """ClearChangeMap(itkChangeLabelLabelMapFilterLM2 self)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_ClearChangeMap(self)

    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM2"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkChangeLabelLabelMapFilterLM2 *":
        """GetPointer(itkChangeLabelLabelMapFilterLM2 self) -> itkChangeLabelLabelMapFilterLM2"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM2

        Create a new object of the class itkChangeLabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkChangeLabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkChangeLabelLabelMapFilterLM2.Clone = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_Clone, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.SetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChangeMap, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.GetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetChangeMap, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.SetChange = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChange, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.ClearChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_ClearChangeMap, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.GetPointer = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetPointer, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2_swigregister = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_swigregister
itkChangeLabelLabelMapFilterLM2_swigregister(itkChangeLabelLabelMapFilterLM2)

def itkChangeLabelLabelMapFilterLM2___New_orig__() -> "itkChangeLabelLabelMapFilterLM2_Pointer":
    """itkChangeLabelLabelMapFilterLM2___New_orig__() -> itkChangeLabelLabelMapFilterLM2_Pointer"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2___New_orig__()

def itkChangeLabelLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM2 *":
    """itkChangeLabelLabelMapFilterLM2_cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM2"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_cast(obj)

class itkChangeLabelLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkChangeLabelLabelMapFilterLM3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkChangeLabelLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkChangeLabelLabelMapFilterLM3_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkChangeLabelLabelMapFilterLM3_Pointer":
        """Clone(itkChangeLabelLabelMapFilterLM3 self) -> itkChangeLabelLabelMapFilterLM3_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_Clone(self)


    def SetChangeMap(self, changeMap: 'mapULUL') -> "void":
        """SetChangeMap(itkChangeLabelLabelMapFilterLM3 self, mapULUL changeMap)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChangeMap(self, changeMap)


    def GetChangeMap(self) -> "std::map< unsigned long,unsigned long,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,unsigned long > > > const &":
        """GetChangeMap(itkChangeLabelLabelMapFilterLM3 self) -> mapULUL"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetChangeMap(self)


    def SetChange(self, oldLabel: 'unsigned long const &', newLabel: 'unsigned long const &') -> "void":
        """SetChange(itkChangeLabelLabelMapFilterLM3 self, unsigned long const & oldLabel, unsigned long const & newLabel)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChange(self, oldLabel, newLabel)


    def ClearChangeMap(self) -> "void":
        """ClearChangeMap(itkChangeLabelLabelMapFilterLM3 self)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_ClearChangeMap(self)

    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM3"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkChangeLabelLabelMapFilterLM3 *":
        """GetPointer(itkChangeLabelLabelMapFilterLM3 self) -> itkChangeLabelLabelMapFilterLM3"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM3

        Create a new object of the class itkChangeLabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkChangeLabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkChangeLabelLabelMapFilterLM3.Clone = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_Clone, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.SetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChangeMap, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.GetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetChangeMap, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.SetChange = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChange, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.ClearChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_ClearChangeMap, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.GetPointer = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetPointer, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3_swigregister = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_swigregister
itkChangeLabelLabelMapFilterLM3_swigregister(itkChangeLabelLabelMapFilterLM3)

def itkChangeLabelLabelMapFilterLM3___New_orig__() -> "itkChangeLabelLabelMapFilterLM3_Pointer":
    """itkChangeLabelLabelMapFilterLM3___New_orig__() -> itkChangeLabelLabelMapFilterLM3_Pointer"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3___New_orig__()

def itkChangeLabelLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM3 *":
    """itkChangeLabelLabelMapFilterLM3_cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM3"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_cast(obj)



