# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkYenThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkYenThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkYenThresholdCalculatorPython')
    _itkYenThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkYenThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkYenThresholdCalculatorPython
            return _itkYenThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkYenThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkYenThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkYenThresholdCalculatorPython
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
import itkHistogramThresholdCalculatorPython
import itkHistogramPython
import itkSamplePython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkArrayPython
import itkSimpleDataObjectDecoratorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkCovariantVectorPython

def itkYenThresholdCalculatorHFF_New():
  return itkYenThresholdCalculatorHFF.New()


def itkYenThresholdCalculatorHDF_New():
  return itkYenThresholdCalculatorHDF.New()


def itkYenThresholdCalculatorHFUC_New():
  return itkYenThresholdCalculatorHFUC.New()


def itkYenThresholdCalculatorHDUC_New():
  return itkYenThresholdCalculatorHDUC.New()


def itkYenThresholdCalculatorHFSS_New():
  return itkYenThresholdCalculatorHFSS.New()


def itkYenThresholdCalculatorHDSS_New():
  return itkYenThresholdCalculatorHDSS.New()

class itkYenThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkYenThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkYenThresholdCalculatorHDF_Pointer":
        """__New_orig__() -> itkYenThresholdCalculatorHDF_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkYenThresholdCalculatorHDF_Pointer":
        """Clone(itkYenThresholdCalculatorHDF self) -> itkYenThresholdCalculatorHDF_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_Clone(self)

    __swig_destroy__ = _itkYenThresholdCalculatorPython.delete_itkYenThresholdCalculatorHDF

    def cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHDF *":
        """cast(itkLightObject obj) -> itkYenThresholdCalculatorHDF"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkYenThresholdCalculatorHDF *":
        """GetPointer(itkYenThresholdCalculatorHDF self) -> itkYenThresholdCalculatorHDF"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkYenThresholdCalculatorHDF

        Create a new object of the class itkYenThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkYenThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkYenThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkYenThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkYenThresholdCalculatorHDF.Clone = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_Clone, None, itkYenThresholdCalculatorHDF)
itkYenThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_GetPointer, None, itkYenThresholdCalculatorHDF)
itkYenThresholdCalculatorHDF_swigregister = _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_swigregister
itkYenThresholdCalculatorHDF_swigregister(itkYenThresholdCalculatorHDF)

def itkYenThresholdCalculatorHDF___New_orig__() -> "itkYenThresholdCalculatorHDF_Pointer":
    """itkYenThresholdCalculatorHDF___New_orig__() -> itkYenThresholdCalculatorHDF_Pointer"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF___New_orig__()

def itkYenThresholdCalculatorHDF_cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHDF *":
    """itkYenThresholdCalculatorHDF_cast(itkLightObject obj) -> itkYenThresholdCalculatorHDF"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDF_cast(obj)

class itkYenThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkYenThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkYenThresholdCalculatorHDSS_Pointer":
        """__New_orig__() -> itkYenThresholdCalculatorHDSS_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkYenThresholdCalculatorHDSS_Pointer":
        """Clone(itkYenThresholdCalculatorHDSS self) -> itkYenThresholdCalculatorHDSS_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_Clone(self)

    __swig_destroy__ = _itkYenThresholdCalculatorPython.delete_itkYenThresholdCalculatorHDSS

    def cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHDSS *":
        """cast(itkLightObject obj) -> itkYenThresholdCalculatorHDSS"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkYenThresholdCalculatorHDSS *":
        """GetPointer(itkYenThresholdCalculatorHDSS self) -> itkYenThresholdCalculatorHDSS"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkYenThresholdCalculatorHDSS

        Create a new object of the class itkYenThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkYenThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkYenThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkYenThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkYenThresholdCalculatorHDSS.Clone = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_Clone, None, itkYenThresholdCalculatorHDSS)
itkYenThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_GetPointer, None, itkYenThresholdCalculatorHDSS)
itkYenThresholdCalculatorHDSS_swigregister = _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_swigregister
itkYenThresholdCalculatorHDSS_swigregister(itkYenThresholdCalculatorHDSS)

def itkYenThresholdCalculatorHDSS___New_orig__() -> "itkYenThresholdCalculatorHDSS_Pointer":
    """itkYenThresholdCalculatorHDSS___New_orig__() -> itkYenThresholdCalculatorHDSS_Pointer"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS___New_orig__()

def itkYenThresholdCalculatorHDSS_cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHDSS *":
    """itkYenThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkYenThresholdCalculatorHDSS"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDSS_cast(obj)

class itkYenThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkYenThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkYenThresholdCalculatorHDUC_Pointer":
        """__New_orig__() -> itkYenThresholdCalculatorHDUC_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkYenThresholdCalculatorHDUC_Pointer":
        """Clone(itkYenThresholdCalculatorHDUC self) -> itkYenThresholdCalculatorHDUC_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_Clone(self)

    __swig_destroy__ = _itkYenThresholdCalculatorPython.delete_itkYenThresholdCalculatorHDUC

    def cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHDUC *":
        """cast(itkLightObject obj) -> itkYenThresholdCalculatorHDUC"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkYenThresholdCalculatorHDUC *":
        """GetPointer(itkYenThresholdCalculatorHDUC self) -> itkYenThresholdCalculatorHDUC"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkYenThresholdCalculatorHDUC

        Create a new object of the class itkYenThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkYenThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkYenThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkYenThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkYenThresholdCalculatorHDUC.Clone = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_Clone, None, itkYenThresholdCalculatorHDUC)
itkYenThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_GetPointer, None, itkYenThresholdCalculatorHDUC)
itkYenThresholdCalculatorHDUC_swigregister = _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_swigregister
itkYenThresholdCalculatorHDUC_swigregister(itkYenThresholdCalculatorHDUC)

def itkYenThresholdCalculatorHDUC___New_orig__() -> "itkYenThresholdCalculatorHDUC_Pointer":
    """itkYenThresholdCalculatorHDUC___New_orig__() -> itkYenThresholdCalculatorHDUC_Pointer"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC___New_orig__()

def itkYenThresholdCalculatorHDUC_cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHDUC *":
    """itkYenThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkYenThresholdCalculatorHDUC"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHDUC_cast(obj)

class itkYenThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkYenThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkYenThresholdCalculatorHFF_Pointer":
        """__New_orig__() -> itkYenThresholdCalculatorHFF_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkYenThresholdCalculatorHFF_Pointer":
        """Clone(itkYenThresholdCalculatorHFF self) -> itkYenThresholdCalculatorHFF_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_Clone(self)

    __swig_destroy__ = _itkYenThresholdCalculatorPython.delete_itkYenThresholdCalculatorHFF

    def cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHFF *":
        """cast(itkLightObject obj) -> itkYenThresholdCalculatorHFF"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkYenThresholdCalculatorHFF *":
        """GetPointer(itkYenThresholdCalculatorHFF self) -> itkYenThresholdCalculatorHFF"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkYenThresholdCalculatorHFF

        Create a new object of the class itkYenThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkYenThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkYenThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkYenThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkYenThresholdCalculatorHFF.Clone = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_Clone, None, itkYenThresholdCalculatorHFF)
itkYenThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_GetPointer, None, itkYenThresholdCalculatorHFF)
itkYenThresholdCalculatorHFF_swigregister = _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_swigregister
itkYenThresholdCalculatorHFF_swigregister(itkYenThresholdCalculatorHFF)

def itkYenThresholdCalculatorHFF___New_orig__() -> "itkYenThresholdCalculatorHFF_Pointer":
    """itkYenThresholdCalculatorHFF___New_orig__() -> itkYenThresholdCalculatorHFF_Pointer"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF___New_orig__()

def itkYenThresholdCalculatorHFF_cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHFF *":
    """itkYenThresholdCalculatorHFF_cast(itkLightObject obj) -> itkYenThresholdCalculatorHFF"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFF_cast(obj)

class itkYenThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkYenThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkYenThresholdCalculatorHFSS_Pointer":
        """__New_orig__() -> itkYenThresholdCalculatorHFSS_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkYenThresholdCalculatorHFSS_Pointer":
        """Clone(itkYenThresholdCalculatorHFSS self) -> itkYenThresholdCalculatorHFSS_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_Clone(self)

    __swig_destroy__ = _itkYenThresholdCalculatorPython.delete_itkYenThresholdCalculatorHFSS

    def cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHFSS *":
        """cast(itkLightObject obj) -> itkYenThresholdCalculatorHFSS"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkYenThresholdCalculatorHFSS *":
        """GetPointer(itkYenThresholdCalculatorHFSS self) -> itkYenThresholdCalculatorHFSS"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkYenThresholdCalculatorHFSS

        Create a new object of the class itkYenThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkYenThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkYenThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkYenThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkYenThresholdCalculatorHFSS.Clone = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_Clone, None, itkYenThresholdCalculatorHFSS)
itkYenThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_GetPointer, None, itkYenThresholdCalculatorHFSS)
itkYenThresholdCalculatorHFSS_swigregister = _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_swigregister
itkYenThresholdCalculatorHFSS_swigregister(itkYenThresholdCalculatorHFSS)

def itkYenThresholdCalculatorHFSS___New_orig__() -> "itkYenThresholdCalculatorHFSS_Pointer":
    """itkYenThresholdCalculatorHFSS___New_orig__() -> itkYenThresholdCalculatorHFSS_Pointer"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS___New_orig__()

def itkYenThresholdCalculatorHFSS_cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHFSS *":
    """itkYenThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkYenThresholdCalculatorHFSS"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFSS_cast(obj)

class itkYenThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkYenThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkYenThresholdCalculatorHFUC_Pointer":
        """__New_orig__() -> itkYenThresholdCalculatorHFUC_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkYenThresholdCalculatorHFUC_Pointer":
        """Clone(itkYenThresholdCalculatorHFUC self) -> itkYenThresholdCalculatorHFUC_Pointer"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_Clone(self)

    __swig_destroy__ = _itkYenThresholdCalculatorPython.delete_itkYenThresholdCalculatorHFUC

    def cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHFUC *":
        """cast(itkLightObject obj) -> itkYenThresholdCalculatorHFUC"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkYenThresholdCalculatorHFUC *":
        """GetPointer(itkYenThresholdCalculatorHFUC self) -> itkYenThresholdCalculatorHFUC"""
        return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkYenThresholdCalculatorHFUC

        Create a new object of the class itkYenThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkYenThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkYenThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkYenThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkYenThresholdCalculatorHFUC.Clone = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_Clone, None, itkYenThresholdCalculatorHFUC)
itkYenThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_GetPointer, None, itkYenThresholdCalculatorHFUC)
itkYenThresholdCalculatorHFUC_swigregister = _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_swigregister
itkYenThresholdCalculatorHFUC_swigregister(itkYenThresholdCalculatorHFUC)

def itkYenThresholdCalculatorHFUC___New_orig__() -> "itkYenThresholdCalculatorHFUC_Pointer":
    """itkYenThresholdCalculatorHFUC___New_orig__() -> itkYenThresholdCalculatorHFUC_Pointer"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC___New_orig__()

def itkYenThresholdCalculatorHFUC_cast(obj: 'itkLightObject') -> "itkYenThresholdCalculatorHFUC *":
    """itkYenThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkYenThresholdCalculatorHFUC"""
    return _itkYenThresholdCalculatorPython.itkYenThresholdCalculatorHFUC_cast(obj)



