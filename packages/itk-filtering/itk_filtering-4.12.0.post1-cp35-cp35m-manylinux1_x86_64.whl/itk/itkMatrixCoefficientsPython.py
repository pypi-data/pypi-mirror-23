# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMatrixCoefficientsPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMatrixCoefficientsPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMatrixCoefficientsPython')
    _itkMatrixCoefficientsPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMatrixCoefficientsPython', [dirname(__file__)])
        except ImportError:
            import _itkMatrixCoefficientsPython
            return _itkMatrixCoefficientsPython
        try:
            _mod = imp.load_module('_itkMatrixCoefficientsPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMatrixCoefficientsPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMatrixCoefficientsPython
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


import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import pyBasePython
import itkQuadEdgeMeshBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import ITKCommonBasePython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython
import itkQuadEdgeCellTraitsInfoPython
import itkQuadEdgeMeshPointPython
import itkPointPython
import itkMapContainerPython
import itkImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
class itkMatrixCoefficientsQEMD2(object):
    """Proxy of C++ itkMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD2

    def __call__(self, iMesh: 'itkQuadEdgeMeshD2', iEdge: 'itkGeometricalQuadEdgeULULBBF') -> "float":
        """__call__(itkMatrixCoefficientsQEMD2 self, itkQuadEdgeMeshD2 iMesh, itkGeometricalQuadEdgeULULBBF iEdge) -> float"""
        return _itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2___call__(self, iMesh, iEdge)

itkMatrixCoefficientsQEMD2.__call__ = new_instancemethod(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2___call__, None, itkMatrixCoefficientsQEMD2)
itkMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2_swigregister
itkMatrixCoefficientsQEMD2_swigregister(itkMatrixCoefficientsQEMD2)

class itkMatrixCoefficientsQEMD3(object):
    """Proxy of C++ itkMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD3

    def __call__(self, iMesh: 'itkQuadEdgeMeshD3', iEdge: 'itkGeometricalQuadEdgeULULBBF') -> "float":
        """__call__(itkMatrixCoefficientsQEMD3 self, itkQuadEdgeMeshD3 iMesh, itkGeometricalQuadEdgeULULBBF iEdge) -> float"""
        return _itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3___call__(self, iMesh, iEdge)

itkMatrixCoefficientsQEMD3.__call__ = new_instancemethod(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3___call__, None, itkMatrixCoefficientsQEMD3)
itkMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3_swigregister
itkMatrixCoefficientsQEMD3_swigregister(itkMatrixCoefficientsQEMD3)

class itkOnesMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    """Proxy of C++ itkOnesMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD2

    def __init__(self, *args):
        """
        __init__(itkOnesMatrixCoefficientsQEMD2 self) -> itkOnesMatrixCoefficientsQEMD2
        __init__(itkOnesMatrixCoefficientsQEMD2 self, itkOnesMatrixCoefficientsQEMD2 arg0) -> itkOnesMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD2(*args))
itkOnesMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD2_swigregister
itkOnesMatrixCoefficientsQEMD2_swigregister(itkOnesMatrixCoefficientsQEMD2)

class itkOnesMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    """Proxy of C++ itkOnesMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD3

    def __init__(self, *args):
        """
        __init__(itkOnesMatrixCoefficientsQEMD3 self) -> itkOnesMatrixCoefficientsQEMD3
        __init__(itkOnesMatrixCoefficientsQEMD3 self, itkOnesMatrixCoefficientsQEMD3 arg0) -> itkOnesMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD3(*args))
itkOnesMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD3_swigregister
itkOnesMatrixCoefficientsQEMD3_swigregister(itkOnesMatrixCoefficientsQEMD3)

class itkAuthalicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    """Proxy of C++ itkAuthalicMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD2

    def __init__(self, *args):
        """
        __init__(itkAuthalicMatrixCoefficientsQEMD2 self) -> itkAuthalicMatrixCoefficientsQEMD2
        __init__(itkAuthalicMatrixCoefficientsQEMD2 self, itkAuthalicMatrixCoefficientsQEMD2 arg0) -> itkAuthalicMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD2(*args))
itkAuthalicMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD2_swigregister
itkAuthalicMatrixCoefficientsQEMD2_swigregister(itkAuthalicMatrixCoefficientsQEMD2)

class itkAuthalicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    """Proxy of C++ itkAuthalicMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD3

    def __init__(self, *args):
        """
        __init__(itkAuthalicMatrixCoefficientsQEMD3 self) -> itkAuthalicMatrixCoefficientsQEMD3
        __init__(itkAuthalicMatrixCoefficientsQEMD3 self, itkAuthalicMatrixCoefficientsQEMD3 arg0) -> itkAuthalicMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD3(*args))
itkAuthalicMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD3_swigregister
itkAuthalicMatrixCoefficientsQEMD3_swigregister(itkAuthalicMatrixCoefficientsQEMD3)

class itkConformalMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    """Proxy of C++ itkConformalMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD2

    def __init__(self, *args):
        """
        __init__(itkConformalMatrixCoefficientsQEMD2 self) -> itkConformalMatrixCoefficientsQEMD2
        __init__(itkConformalMatrixCoefficientsQEMD2 self, itkConformalMatrixCoefficientsQEMD2 arg0) -> itkConformalMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD2(*args))
itkConformalMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD2_swigregister
itkConformalMatrixCoefficientsQEMD2_swigregister(itkConformalMatrixCoefficientsQEMD2)

class itkConformalMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    """Proxy of C++ itkConformalMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD3

    def __init__(self, *args):
        """
        __init__(itkConformalMatrixCoefficientsQEMD3 self) -> itkConformalMatrixCoefficientsQEMD3
        __init__(itkConformalMatrixCoefficientsQEMD3 self, itkConformalMatrixCoefficientsQEMD3 arg0) -> itkConformalMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD3(*args))
itkConformalMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD3_swigregister
itkConformalMatrixCoefficientsQEMD3_swigregister(itkConformalMatrixCoefficientsQEMD3)

class itkHarmonicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    """Proxy of C++ itkHarmonicMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD2

    def __init__(self, *args):
        """
        __init__(itkHarmonicMatrixCoefficientsQEMD2 self) -> itkHarmonicMatrixCoefficientsQEMD2
        __init__(itkHarmonicMatrixCoefficientsQEMD2 self, itkHarmonicMatrixCoefficientsQEMD2 arg0) -> itkHarmonicMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD2(*args))
itkHarmonicMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD2_swigregister
itkHarmonicMatrixCoefficientsQEMD2_swigregister(itkHarmonicMatrixCoefficientsQEMD2)

class itkHarmonicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    """Proxy of C++ itkHarmonicMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD3

    def __init__(self, *args):
        """
        __init__(itkHarmonicMatrixCoefficientsQEMD3 self) -> itkHarmonicMatrixCoefficientsQEMD3
        __init__(itkHarmonicMatrixCoefficientsQEMD3 self, itkHarmonicMatrixCoefficientsQEMD3 arg0) -> itkHarmonicMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD3(*args))
itkHarmonicMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD3_swigregister
itkHarmonicMatrixCoefficientsQEMD3_swigregister(itkHarmonicMatrixCoefficientsQEMD3)

class itkIntrinsicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    """Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD2

    def __init__(self, *args):
        """
        __init__(itkIntrinsicMatrixCoefficientsQEMD2 self, float const & iLambda) -> itkIntrinsicMatrixCoefficientsQEMD2
        __init__(itkIntrinsicMatrixCoefficientsQEMD2 self, itkIntrinsicMatrixCoefficientsQEMD2 arg0) -> itkIntrinsicMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD2(*args))
itkIntrinsicMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD2_swigregister
itkIntrinsicMatrixCoefficientsQEMD2_swigregister(itkIntrinsicMatrixCoefficientsQEMD2)

class itkIntrinsicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    """Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD3

    def __init__(self, *args):
        """
        __init__(itkIntrinsicMatrixCoefficientsQEMD3 self, float const & iLambda) -> itkIntrinsicMatrixCoefficientsQEMD3
        __init__(itkIntrinsicMatrixCoefficientsQEMD3 self, itkIntrinsicMatrixCoefficientsQEMD3 arg0) -> itkIntrinsicMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD3(*args))
itkIntrinsicMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD3_swigregister
itkIntrinsicMatrixCoefficientsQEMD3_swigregister(itkIntrinsicMatrixCoefficientsQEMD3)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    """Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD2

    def __init__(self, *args):
        """
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD2
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 self, itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD2(*args))
itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swigregister = _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swigregister
itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    """Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD3

    def __init__(self, *args):
        """
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD3
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 self, itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD3(*args))
itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swigregister = _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swigregister
itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3)



