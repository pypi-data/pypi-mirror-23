# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython')
    _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython
            return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython
        try:
            _mod = imp.load_module('_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython
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
import itkDiscreteCurvatureQuadEdgeMeshFilterPython
import itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itkQuadEdgeMeshBasePython
import itkImagePython
import stdcomplexPython
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
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkMapContainerPython
import itkQuadEdgeCellTraitsInfoPython
import itkQuadEdgeMeshPointPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython

def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_New():
  return itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.New()


def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_New():
  return itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.New()

class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2(itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2):
    """Proxy of C++ itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2 self) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_Clone(self)

    OutputIsFloatingPointCheck = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2 self) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.Clone = new_instancemethod(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_Clone, None, itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.GetPointer = new_instancemethod(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_GetPointer, None, itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_swigregister = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_swigregister
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_swigregister(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2)

def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__():
    """itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_Pointer"""
    return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__()

def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast(obj):
    """itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2"""
    return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast(obj)

class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3(itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3):
    """Proxy of C++ itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3 self) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_Clone(self)

    OutputIsFloatingPointCheck = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3 self) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3"""
        return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.Clone = new_instancemethod(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_Clone, None, itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.GetPointer = new_instancemethod(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_GetPointer, None, itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_swigregister = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_swigregister
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_swigregister(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3)

def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__():
    """itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_Pointer"""
    return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__()

def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast(obj):
    """itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3"""
    return _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast(obj)



