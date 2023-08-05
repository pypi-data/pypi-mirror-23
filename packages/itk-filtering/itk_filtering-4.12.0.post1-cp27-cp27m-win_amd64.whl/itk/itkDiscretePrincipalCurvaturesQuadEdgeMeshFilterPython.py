# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython')
    _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython
            return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython
        try:
            _mod = imp.load_module('_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython
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


import itkDiscreteCurvatureQuadEdgeMeshFilterPython
import itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itkQuadEdgeMeshBasePython
import itkImagePython
import stdcomplexPython
import pyBasePython
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
import ITKCommonBasePython
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

def itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_New():
  return itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3.New()


def itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_New():
  return itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2.New()

class itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2(itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2):
    """Proxy of C++ itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.delete_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2"""
        return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2 self) -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2"""
        return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2.GetPointer = new_instancemethod(_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_GetPointer, None, itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2)
itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_swigregister = _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_swigregister
itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_swigregister(itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2)

def itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_cast(obj):
    """itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2"""
    return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2_cast(obj)

class itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3(itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3):
    """Proxy of C++ itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.delete_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3"""
        return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3 self) -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3"""
        return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3.GetPointer = new_instancemethod(_itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_GetPointer, None, itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3)
itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_swigregister = _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_swigregister
itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_swigregister(itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3)

def itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_cast(obj):
    """itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3"""
    return _itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3_cast(obj)



