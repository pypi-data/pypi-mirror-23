# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkKittlerIllingworthThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkKittlerIllingworthThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkKittlerIllingworthThresholdCalculatorPython')
    _itkKittlerIllingworthThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkKittlerIllingworthThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkKittlerIllingworthThresholdCalculatorPython
            return _itkKittlerIllingworthThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkKittlerIllingworthThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkKittlerIllingworthThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkKittlerIllingworthThresholdCalculatorPython
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


import itkHistogramThresholdCalculatorPython
import itkHistogramPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython
import itkSamplePython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkRGBAPixelPython

def itkKittlerIllingworthThresholdCalculatorHFF_New():
  return itkKittlerIllingworthThresholdCalculatorHFF.New()


def itkKittlerIllingworthThresholdCalculatorHDF_New():
  return itkKittlerIllingworthThresholdCalculatorHDF.New()


def itkKittlerIllingworthThresholdCalculatorHFUC_New():
  return itkKittlerIllingworthThresholdCalculatorHFUC.New()


def itkKittlerIllingworthThresholdCalculatorHDUC_New():
  return itkKittlerIllingworthThresholdCalculatorHDUC.New()


def itkKittlerIllingworthThresholdCalculatorHFSS_New():
  return itkKittlerIllingworthThresholdCalculatorHFSS.New()


def itkKittlerIllingworthThresholdCalculatorHDSS_New():
  return itkKittlerIllingworthThresholdCalculatorHDSS.New()

class itkKittlerIllingworthThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkKittlerIllingworthThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHDF_Pointer":
        """__New_orig__() -> itkKittlerIllingworthThresholdCalculatorHDF_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKittlerIllingworthThresholdCalculatorHDF_Pointer":
        """Clone(itkKittlerIllingworthThresholdCalculatorHDF self) -> itkKittlerIllingworthThresholdCalculatorHDF_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_Clone(self)

    __swig_destroy__ = _itkKittlerIllingworthThresholdCalculatorPython.delete_itkKittlerIllingworthThresholdCalculatorHDF

    def cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHDF *":
        """cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHDF"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKittlerIllingworthThresholdCalculatorHDF *":
        """GetPointer(itkKittlerIllingworthThresholdCalculatorHDF self) -> itkKittlerIllingworthThresholdCalculatorHDF"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKittlerIllingworthThresholdCalculatorHDF

        Create a new object of the class itkKittlerIllingworthThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKittlerIllingworthThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKittlerIllingworthThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKittlerIllingworthThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKittlerIllingworthThresholdCalculatorHDF.Clone = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_Clone, None, itkKittlerIllingworthThresholdCalculatorHDF)
itkKittlerIllingworthThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_GetPointer, None, itkKittlerIllingworthThresholdCalculatorHDF)
itkKittlerIllingworthThresholdCalculatorHDF_swigregister = _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_swigregister
itkKittlerIllingworthThresholdCalculatorHDF_swigregister(itkKittlerIllingworthThresholdCalculatorHDF)

def itkKittlerIllingworthThresholdCalculatorHDF___New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHDF_Pointer":
    """itkKittlerIllingworthThresholdCalculatorHDF___New_orig__() -> itkKittlerIllingworthThresholdCalculatorHDF_Pointer"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF___New_orig__()

def itkKittlerIllingworthThresholdCalculatorHDF_cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHDF *":
    """itkKittlerIllingworthThresholdCalculatorHDF_cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHDF"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDF_cast(obj)

class itkKittlerIllingworthThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkKittlerIllingworthThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHDSS_Pointer":
        """__New_orig__() -> itkKittlerIllingworthThresholdCalculatorHDSS_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKittlerIllingworthThresholdCalculatorHDSS_Pointer":
        """Clone(itkKittlerIllingworthThresholdCalculatorHDSS self) -> itkKittlerIllingworthThresholdCalculatorHDSS_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_Clone(self)

    __swig_destroy__ = _itkKittlerIllingworthThresholdCalculatorPython.delete_itkKittlerIllingworthThresholdCalculatorHDSS

    def cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHDSS *":
        """cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHDSS"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKittlerIllingworthThresholdCalculatorHDSS *":
        """GetPointer(itkKittlerIllingworthThresholdCalculatorHDSS self) -> itkKittlerIllingworthThresholdCalculatorHDSS"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKittlerIllingworthThresholdCalculatorHDSS

        Create a new object of the class itkKittlerIllingworthThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKittlerIllingworthThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKittlerIllingworthThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKittlerIllingworthThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKittlerIllingworthThresholdCalculatorHDSS.Clone = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_Clone, None, itkKittlerIllingworthThresholdCalculatorHDSS)
itkKittlerIllingworthThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_GetPointer, None, itkKittlerIllingworthThresholdCalculatorHDSS)
itkKittlerIllingworthThresholdCalculatorHDSS_swigregister = _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_swigregister
itkKittlerIllingworthThresholdCalculatorHDSS_swigregister(itkKittlerIllingworthThresholdCalculatorHDSS)

def itkKittlerIllingworthThresholdCalculatorHDSS___New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHDSS_Pointer":
    """itkKittlerIllingworthThresholdCalculatorHDSS___New_orig__() -> itkKittlerIllingworthThresholdCalculatorHDSS_Pointer"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS___New_orig__()

def itkKittlerIllingworthThresholdCalculatorHDSS_cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHDSS *":
    """itkKittlerIllingworthThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHDSS"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDSS_cast(obj)

class itkKittlerIllingworthThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkKittlerIllingworthThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHDUC_Pointer":
        """__New_orig__() -> itkKittlerIllingworthThresholdCalculatorHDUC_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKittlerIllingworthThresholdCalculatorHDUC_Pointer":
        """Clone(itkKittlerIllingworthThresholdCalculatorHDUC self) -> itkKittlerIllingworthThresholdCalculatorHDUC_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_Clone(self)

    __swig_destroy__ = _itkKittlerIllingworthThresholdCalculatorPython.delete_itkKittlerIllingworthThresholdCalculatorHDUC

    def cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHDUC *":
        """cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHDUC"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKittlerIllingworthThresholdCalculatorHDUC *":
        """GetPointer(itkKittlerIllingworthThresholdCalculatorHDUC self) -> itkKittlerIllingworthThresholdCalculatorHDUC"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKittlerIllingworthThresholdCalculatorHDUC

        Create a new object of the class itkKittlerIllingworthThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKittlerIllingworthThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKittlerIllingworthThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKittlerIllingworthThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKittlerIllingworthThresholdCalculatorHDUC.Clone = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_Clone, None, itkKittlerIllingworthThresholdCalculatorHDUC)
itkKittlerIllingworthThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_GetPointer, None, itkKittlerIllingworthThresholdCalculatorHDUC)
itkKittlerIllingworthThresholdCalculatorHDUC_swigregister = _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_swigregister
itkKittlerIllingworthThresholdCalculatorHDUC_swigregister(itkKittlerIllingworthThresholdCalculatorHDUC)

def itkKittlerIllingworthThresholdCalculatorHDUC___New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHDUC_Pointer":
    """itkKittlerIllingworthThresholdCalculatorHDUC___New_orig__() -> itkKittlerIllingworthThresholdCalculatorHDUC_Pointer"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC___New_orig__()

def itkKittlerIllingworthThresholdCalculatorHDUC_cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHDUC *":
    """itkKittlerIllingworthThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHDUC"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHDUC_cast(obj)

class itkKittlerIllingworthThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkKittlerIllingworthThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHFF_Pointer":
        """__New_orig__() -> itkKittlerIllingworthThresholdCalculatorHFF_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKittlerIllingworthThresholdCalculatorHFF_Pointer":
        """Clone(itkKittlerIllingworthThresholdCalculatorHFF self) -> itkKittlerIllingworthThresholdCalculatorHFF_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_Clone(self)

    __swig_destroy__ = _itkKittlerIllingworthThresholdCalculatorPython.delete_itkKittlerIllingworthThresholdCalculatorHFF

    def cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHFF *":
        """cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHFF"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKittlerIllingworthThresholdCalculatorHFF *":
        """GetPointer(itkKittlerIllingworthThresholdCalculatorHFF self) -> itkKittlerIllingworthThresholdCalculatorHFF"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKittlerIllingworthThresholdCalculatorHFF

        Create a new object of the class itkKittlerIllingworthThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKittlerIllingworthThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKittlerIllingworthThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKittlerIllingworthThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKittlerIllingworthThresholdCalculatorHFF.Clone = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_Clone, None, itkKittlerIllingworthThresholdCalculatorHFF)
itkKittlerIllingworthThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_GetPointer, None, itkKittlerIllingworthThresholdCalculatorHFF)
itkKittlerIllingworthThresholdCalculatorHFF_swigregister = _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_swigregister
itkKittlerIllingworthThresholdCalculatorHFF_swigregister(itkKittlerIllingworthThresholdCalculatorHFF)

def itkKittlerIllingworthThresholdCalculatorHFF___New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHFF_Pointer":
    """itkKittlerIllingworthThresholdCalculatorHFF___New_orig__() -> itkKittlerIllingworthThresholdCalculatorHFF_Pointer"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF___New_orig__()

def itkKittlerIllingworthThresholdCalculatorHFF_cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHFF *":
    """itkKittlerIllingworthThresholdCalculatorHFF_cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHFF"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFF_cast(obj)

class itkKittlerIllingworthThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkKittlerIllingworthThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHFSS_Pointer":
        """__New_orig__() -> itkKittlerIllingworthThresholdCalculatorHFSS_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKittlerIllingworthThresholdCalculatorHFSS_Pointer":
        """Clone(itkKittlerIllingworthThresholdCalculatorHFSS self) -> itkKittlerIllingworthThresholdCalculatorHFSS_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_Clone(self)

    __swig_destroy__ = _itkKittlerIllingworthThresholdCalculatorPython.delete_itkKittlerIllingworthThresholdCalculatorHFSS

    def cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHFSS *":
        """cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHFSS"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKittlerIllingworthThresholdCalculatorHFSS *":
        """GetPointer(itkKittlerIllingworthThresholdCalculatorHFSS self) -> itkKittlerIllingworthThresholdCalculatorHFSS"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKittlerIllingworthThresholdCalculatorHFSS

        Create a new object of the class itkKittlerIllingworthThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKittlerIllingworthThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKittlerIllingworthThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKittlerIllingworthThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKittlerIllingworthThresholdCalculatorHFSS.Clone = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_Clone, None, itkKittlerIllingworthThresholdCalculatorHFSS)
itkKittlerIllingworthThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_GetPointer, None, itkKittlerIllingworthThresholdCalculatorHFSS)
itkKittlerIllingworthThresholdCalculatorHFSS_swigregister = _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_swigregister
itkKittlerIllingworthThresholdCalculatorHFSS_swigregister(itkKittlerIllingworthThresholdCalculatorHFSS)

def itkKittlerIllingworthThresholdCalculatorHFSS___New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHFSS_Pointer":
    """itkKittlerIllingworthThresholdCalculatorHFSS___New_orig__() -> itkKittlerIllingworthThresholdCalculatorHFSS_Pointer"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS___New_orig__()

def itkKittlerIllingworthThresholdCalculatorHFSS_cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHFSS *":
    """itkKittlerIllingworthThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHFSS"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFSS_cast(obj)

class itkKittlerIllingworthThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkKittlerIllingworthThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHFUC_Pointer":
        """__New_orig__() -> itkKittlerIllingworthThresholdCalculatorHFUC_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKittlerIllingworthThresholdCalculatorHFUC_Pointer":
        """Clone(itkKittlerIllingworthThresholdCalculatorHFUC self) -> itkKittlerIllingworthThresholdCalculatorHFUC_Pointer"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_Clone(self)

    __swig_destroy__ = _itkKittlerIllingworthThresholdCalculatorPython.delete_itkKittlerIllingworthThresholdCalculatorHFUC

    def cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHFUC *":
        """cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHFUC"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKittlerIllingworthThresholdCalculatorHFUC *":
        """GetPointer(itkKittlerIllingworthThresholdCalculatorHFUC self) -> itkKittlerIllingworthThresholdCalculatorHFUC"""
        return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKittlerIllingworthThresholdCalculatorHFUC

        Create a new object of the class itkKittlerIllingworthThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKittlerIllingworthThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKittlerIllingworthThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKittlerIllingworthThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKittlerIllingworthThresholdCalculatorHFUC.Clone = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_Clone, None, itkKittlerIllingworthThresholdCalculatorHFUC)
itkKittlerIllingworthThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_GetPointer, None, itkKittlerIllingworthThresholdCalculatorHFUC)
itkKittlerIllingworthThresholdCalculatorHFUC_swigregister = _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_swigregister
itkKittlerIllingworthThresholdCalculatorHFUC_swigregister(itkKittlerIllingworthThresholdCalculatorHFUC)

def itkKittlerIllingworthThresholdCalculatorHFUC___New_orig__() -> "itkKittlerIllingworthThresholdCalculatorHFUC_Pointer":
    """itkKittlerIllingworthThresholdCalculatorHFUC___New_orig__() -> itkKittlerIllingworthThresholdCalculatorHFUC_Pointer"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC___New_orig__()

def itkKittlerIllingworthThresholdCalculatorHFUC_cast(obj: 'itkLightObject') -> "itkKittlerIllingworthThresholdCalculatorHFUC *":
    """itkKittlerIllingworthThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkKittlerIllingworthThresholdCalculatorHFUC"""
    return _itkKittlerIllingworthThresholdCalculatorPython.itkKittlerIllingworthThresholdCalculatorHFUC_cast(obj)



