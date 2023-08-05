# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIsoDataThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkIsoDataThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkIsoDataThresholdCalculatorPython')
    _itkIsoDataThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIsoDataThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkIsoDataThresholdCalculatorPython
            return _itkIsoDataThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkIsoDataThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkIsoDataThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIsoDataThresholdCalculatorPython
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
import ITKCommonBasePython
import pyBasePython
import itkSimpleDataObjectDecoratorPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkArrayPython
import itkRGBAPixelPython
import itkHistogramPython
import itkSamplePython

def itkIsoDataThresholdCalculatorHFF_New():
  return itkIsoDataThresholdCalculatorHFF.New()


def itkIsoDataThresholdCalculatorHDF_New():
  return itkIsoDataThresholdCalculatorHDF.New()


def itkIsoDataThresholdCalculatorHFUC_New():
  return itkIsoDataThresholdCalculatorHFUC.New()


def itkIsoDataThresholdCalculatorHDUC_New():
  return itkIsoDataThresholdCalculatorHDUC.New()


def itkIsoDataThresholdCalculatorHFSS_New():
  return itkIsoDataThresholdCalculatorHFSS.New()


def itkIsoDataThresholdCalculatorHDSS_New():
  return itkIsoDataThresholdCalculatorHDSS.New()

class itkIsoDataThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkIsoDataThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoDataThresholdCalculatorHDF_Pointer":
        """__New_orig__() -> itkIsoDataThresholdCalculatorHDF_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoDataThresholdCalculatorHDF_Pointer":
        """Clone(itkIsoDataThresholdCalculatorHDF self) -> itkIsoDataThresholdCalculatorHDF_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_Clone(self)

    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDF

    def cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHDF *":
        """cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHDF"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoDataThresholdCalculatorHDF *":
        """GetPointer(itkIsoDataThresholdCalculatorHDF self) -> itkIsoDataThresholdCalculatorHDF"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDF

        Create a new object of the class itkIsoDataThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoDataThresholdCalculatorHDF.Clone = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_Clone, None, itkIsoDataThresholdCalculatorHDF)
itkIsoDataThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_GetPointer, None, itkIsoDataThresholdCalculatorHDF)
itkIsoDataThresholdCalculatorHDF_swigregister = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_swigregister
itkIsoDataThresholdCalculatorHDF_swigregister(itkIsoDataThresholdCalculatorHDF)

def itkIsoDataThresholdCalculatorHDF___New_orig__() -> "itkIsoDataThresholdCalculatorHDF_Pointer":
    """itkIsoDataThresholdCalculatorHDF___New_orig__() -> itkIsoDataThresholdCalculatorHDF_Pointer"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF___New_orig__()

def itkIsoDataThresholdCalculatorHDF_cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHDF *":
    """itkIsoDataThresholdCalculatorHDF_cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHDF"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_cast(obj)

class itkIsoDataThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkIsoDataThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoDataThresholdCalculatorHDSS_Pointer":
        """__New_orig__() -> itkIsoDataThresholdCalculatorHDSS_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoDataThresholdCalculatorHDSS_Pointer":
        """Clone(itkIsoDataThresholdCalculatorHDSS self) -> itkIsoDataThresholdCalculatorHDSS_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_Clone(self)

    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDSS

    def cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHDSS *":
        """cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHDSS"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoDataThresholdCalculatorHDSS *":
        """GetPointer(itkIsoDataThresholdCalculatorHDSS self) -> itkIsoDataThresholdCalculatorHDSS"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDSS

        Create a new object of the class itkIsoDataThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoDataThresholdCalculatorHDSS.Clone = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_Clone, None, itkIsoDataThresholdCalculatorHDSS)
itkIsoDataThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_GetPointer, None, itkIsoDataThresholdCalculatorHDSS)
itkIsoDataThresholdCalculatorHDSS_swigregister = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_swigregister
itkIsoDataThresholdCalculatorHDSS_swigregister(itkIsoDataThresholdCalculatorHDSS)

def itkIsoDataThresholdCalculatorHDSS___New_orig__() -> "itkIsoDataThresholdCalculatorHDSS_Pointer":
    """itkIsoDataThresholdCalculatorHDSS___New_orig__() -> itkIsoDataThresholdCalculatorHDSS_Pointer"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS___New_orig__()

def itkIsoDataThresholdCalculatorHDSS_cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHDSS *":
    """itkIsoDataThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHDSS"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_cast(obj)

class itkIsoDataThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkIsoDataThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoDataThresholdCalculatorHDUC_Pointer":
        """__New_orig__() -> itkIsoDataThresholdCalculatorHDUC_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoDataThresholdCalculatorHDUC_Pointer":
        """Clone(itkIsoDataThresholdCalculatorHDUC self) -> itkIsoDataThresholdCalculatorHDUC_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_Clone(self)

    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDUC

    def cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHDUC *":
        """cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHDUC"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoDataThresholdCalculatorHDUC *":
        """GetPointer(itkIsoDataThresholdCalculatorHDUC self) -> itkIsoDataThresholdCalculatorHDUC"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDUC

        Create a new object of the class itkIsoDataThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoDataThresholdCalculatorHDUC.Clone = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_Clone, None, itkIsoDataThresholdCalculatorHDUC)
itkIsoDataThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_GetPointer, None, itkIsoDataThresholdCalculatorHDUC)
itkIsoDataThresholdCalculatorHDUC_swigregister = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_swigregister
itkIsoDataThresholdCalculatorHDUC_swigregister(itkIsoDataThresholdCalculatorHDUC)

def itkIsoDataThresholdCalculatorHDUC___New_orig__() -> "itkIsoDataThresholdCalculatorHDUC_Pointer":
    """itkIsoDataThresholdCalculatorHDUC___New_orig__() -> itkIsoDataThresholdCalculatorHDUC_Pointer"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC___New_orig__()

def itkIsoDataThresholdCalculatorHDUC_cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHDUC *":
    """itkIsoDataThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHDUC"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_cast(obj)

class itkIsoDataThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkIsoDataThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoDataThresholdCalculatorHFF_Pointer":
        """__New_orig__() -> itkIsoDataThresholdCalculatorHFF_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoDataThresholdCalculatorHFF_Pointer":
        """Clone(itkIsoDataThresholdCalculatorHFF self) -> itkIsoDataThresholdCalculatorHFF_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_Clone(self)

    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFF

    def cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHFF *":
        """cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHFF"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoDataThresholdCalculatorHFF *":
        """GetPointer(itkIsoDataThresholdCalculatorHFF self) -> itkIsoDataThresholdCalculatorHFF"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFF

        Create a new object of the class itkIsoDataThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoDataThresholdCalculatorHFF.Clone = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_Clone, None, itkIsoDataThresholdCalculatorHFF)
itkIsoDataThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_GetPointer, None, itkIsoDataThresholdCalculatorHFF)
itkIsoDataThresholdCalculatorHFF_swigregister = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_swigregister
itkIsoDataThresholdCalculatorHFF_swigregister(itkIsoDataThresholdCalculatorHFF)

def itkIsoDataThresholdCalculatorHFF___New_orig__() -> "itkIsoDataThresholdCalculatorHFF_Pointer":
    """itkIsoDataThresholdCalculatorHFF___New_orig__() -> itkIsoDataThresholdCalculatorHFF_Pointer"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF___New_orig__()

def itkIsoDataThresholdCalculatorHFF_cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHFF *":
    """itkIsoDataThresholdCalculatorHFF_cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHFF"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_cast(obj)

class itkIsoDataThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkIsoDataThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoDataThresholdCalculatorHFSS_Pointer":
        """__New_orig__() -> itkIsoDataThresholdCalculatorHFSS_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoDataThresholdCalculatorHFSS_Pointer":
        """Clone(itkIsoDataThresholdCalculatorHFSS self) -> itkIsoDataThresholdCalculatorHFSS_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_Clone(self)

    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFSS

    def cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHFSS *":
        """cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHFSS"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoDataThresholdCalculatorHFSS *":
        """GetPointer(itkIsoDataThresholdCalculatorHFSS self) -> itkIsoDataThresholdCalculatorHFSS"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFSS

        Create a new object of the class itkIsoDataThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoDataThresholdCalculatorHFSS.Clone = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_Clone, None, itkIsoDataThresholdCalculatorHFSS)
itkIsoDataThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_GetPointer, None, itkIsoDataThresholdCalculatorHFSS)
itkIsoDataThresholdCalculatorHFSS_swigregister = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_swigregister
itkIsoDataThresholdCalculatorHFSS_swigregister(itkIsoDataThresholdCalculatorHFSS)

def itkIsoDataThresholdCalculatorHFSS___New_orig__() -> "itkIsoDataThresholdCalculatorHFSS_Pointer":
    """itkIsoDataThresholdCalculatorHFSS___New_orig__() -> itkIsoDataThresholdCalculatorHFSS_Pointer"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS___New_orig__()

def itkIsoDataThresholdCalculatorHFSS_cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHFSS *":
    """itkIsoDataThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHFSS"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_cast(obj)

class itkIsoDataThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkIsoDataThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIsoDataThresholdCalculatorHFUC_Pointer":
        """__New_orig__() -> itkIsoDataThresholdCalculatorHFUC_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIsoDataThresholdCalculatorHFUC_Pointer":
        """Clone(itkIsoDataThresholdCalculatorHFUC self) -> itkIsoDataThresholdCalculatorHFUC_Pointer"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_Clone(self)

    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFUC

    def cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHFUC *":
        """cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHFUC"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIsoDataThresholdCalculatorHFUC *":
        """GetPointer(itkIsoDataThresholdCalculatorHFUC self) -> itkIsoDataThresholdCalculatorHFUC"""
        return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFUC

        Create a new object of the class itkIsoDataThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsoDataThresholdCalculatorHFUC.Clone = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_Clone, None, itkIsoDataThresholdCalculatorHFUC)
itkIsoDataThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_GetPointer, None, itkIsoDataThresholdCalculatorHFUC)
itkIsoDataThresholdCalculatorHFUC_swigregister = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_swigregister
itkIsoDataThresholdCalculatorHFUC_swigregister(itkIsoDataThresholdCalculatorHFUC)

def itkIsoDataThresholdCalculatorHFUC___New_orig__() -> "itkIsoDataThresholdCalculatorHFUC_Pointer":
    """itkIsoDataThresholdCalculatorHFUC___New_orig__() -> itkIsoDataThresholdCalculatorHFUC_Pointer"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC___New_orig__()

def itkIsoDataThresholdCalculatorHFUC_cast(obj: 'itkLightObject') -> "itkIsoDataThresholdCalculatorHFUC *":
    """itkIsoDataThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkIsoDataThresholdCalculatorHFUC"""
    return _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_cast(obj)



