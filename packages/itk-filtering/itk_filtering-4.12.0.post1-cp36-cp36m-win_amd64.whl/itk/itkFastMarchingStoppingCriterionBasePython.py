# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingStoppingCriterionBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingStoppingCriterionBasePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingStoppingCriterionBasePython')
    _itkFastMarchingStoppingCriterionBasePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingStoppingCriterionBasePython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingStoppingCriterionBasePython
            return _itkFastMarchingStoppingCriterionBasePython
        try:
            _mod = imp.load_module('_itkFastMarchingStoppingCriterionBasePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingStoppingCriterionBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingStoppingCriterionBasePython
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


import itkImagePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
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
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkNodePairPython

def itkFastMarchingStoppingCriterionBaseIF3IF3_New():
  return itkFastMarchingStoppingCriterionBaseIF3IF3.New()


def itkFastMarchingStoppingCriterionBaseIF2IF2_New():
  return itkFastMarchingStoppingCriterionBaseIF2IF2.New()

class itkFastMarchingStoppingCriterionBaseIF2IF2(ITKCommonBasePython.itkStoppingCriterionBase):
    """Proxy of C++ itkFastMarchingStoppingCriterionBaseIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reinitialize(self) -> "void":
        """Reinitialize(itkFastMarchingStoppingCriterionBaseIF2IF2 self)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_Reinitialize(self)


    def SetCurrentNodePair(self, iNodePair: 'itkNodePairI2F') -> "void":
        """SetCurrentNodePair(itkFastMarchingStoppingCriterionBaseIF2IF2 self, itkNodePairI2F iNodePair)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetCurrentNodePair(self, iNodePair)


    def SetDomain(self, _arg: 'itkImageF2') -> "void":
        """SetDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self, itkImageF2 _arg)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetDomain(self, _arg)


    def GetModifiableDomain(self) -> "itkImageF2 *":
        """GetModifiableDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkImageF2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetModifiableDomain(self)


    def GetDomain(self, *args) -> "itkImageF2 *":
        """
        GetDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkImageF2
        GetDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkImageF2
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetDomain(self, *args)

    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF2IF2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingStoppingCriterionBaseIF2IF2 *":
        """GetPointer(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkFastMarchingStoppingCriterionBaseIF2IF2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingStoppingCriterionBaseIF2IF2

        Create a new object of the class itkFastMarchingStoppingCriterionBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingStoppingCriterionBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingStoppingCriterionBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingStoppingCriterionBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingStoppingCriterionBaseIF2IF2.Reinitialize = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_Reinitialize, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.SetCurrentNodePair = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetCurrentNodePair, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.SetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetDomain, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.GetModifiableDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetModifiableDomain, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.GetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetDomain, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.GetPointer = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetPointer, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister
itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister(itkFastMarchingStoppingCriterionBaseIF2IF2)

def itkFastMarchingStoppingCriterionBaseIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF2IF2 *":
    """itkFastMarchingStoppingCriterionBaseIF2IF2_cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF2IF2"""
    return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_cast(obj)

class itkFastMarchingStoppingCriterionBaseIF3IF3(ITKCommonBasePython.itkStoppingCriterionBase):
    """Proxy of C++ itkFastMarchingStoppingCriterionBaseIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reinitialize(self) -> "void":
        """Reinitialize(itkFastMarchingStoppingCriterionBaseIF3IF3 self)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_Reinitialize(self)


    def SetCurrentNodePair(self, iNodePair: 'itkNodePairI3F') -> "void":
        """SetCurrentNodePair(itkFastMarchingStoppingCriterionBaseIF3IF3 self, itkNodePairI3F iNodePair)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetCurrentNodePair(self, iNodePair)


    def SetDomain(self, _arg: 'itkImageF3') -> "void":
        """SetDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self, itkImageF3 _arg)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetDomain(self, _arg)


    def GetModifiableDomain(self) -> "itkImageF3 *":
        """GetModifiableDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkImageF3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetModifiableDomain(self)


    def GetDomain(self, *args) -> "itkImageF3 *":
        """
        GetDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkImageF3
        GetDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkImageF3
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetDomain(self, *args)

    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF3IF3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingStoppingCriterionBaseIF3IF3 *":
        """GetPointer(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkFastMarchingStoppingCriterionBaseIF3IF3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingStoppingCriterionBaseIF3IF3

        Create a new object of the class itkFastMarchingStoppingCriterionBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingStoppingCriterionBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingStoppingCriterionBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingStoppingCriterionBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingStoppingCriterionBaseIF3IF3.Reinitialize = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_Reinitialize, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.SetCurrentNodePair = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetCurrentNodePair, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.SetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetDomain, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.GetModifiableDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetModifiableDomain, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.GetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetDomain, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.GetPointer = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetPointer, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister
itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister(itkFastMarchingStoppingCriterionBaseIF3IF3)

def itkFastMarchingStoppingCriterionBaseIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF3IF3 *":
    """itkFastMarchingStoppingCriterionBaseIF3IF3_cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF3IF3"""
    return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_cast(obj)



