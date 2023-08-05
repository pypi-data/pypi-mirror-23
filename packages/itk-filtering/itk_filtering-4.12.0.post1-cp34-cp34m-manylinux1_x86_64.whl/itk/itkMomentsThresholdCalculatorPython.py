# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMomentsThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMomentsThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMomentsThresholdCalculatorPython')
    _itkMomentsThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMomentsThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkMomentsThresholdCalculatorPython
            return _itkMomentsThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkMomentsThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMomentsThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMomentsThresholdCalculatorPython
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
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkRGBAPixelPython

def itkMomentsThresholdCalculatorHFF_New():
  return itkMomentsThresholdCalculatorHFF.New()


def itkMomentsThresholdCalculatorHDF_New():
  return itkMomentsThresholdCalculatorHDF.New()


def itkMomentsThresholdCalculatorHFUC_New():
  return itkMomentsThresholdCalculatorHFUC.New()


def itkMomentsThresholdCalculatorHDUC_New():
  return itkMomentsThresholdCalculatorHDUC.New()


def itkMomentsThresholdCalculatorHFSS_New():
  return itkMomentsThresholdCalculatorHFSS.New()


def itkMomentsThresholdCalculatorHDSS_New():
  return itkMomentsThresholdCalculatorHDSS.New()

class itkMomentsThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkMomentsThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMomentsThresholdCalculatorHDF_Pointer":
        """__New_orig__() -> itkMomentsThresholdCalculatorHDF_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMomentsThresholdCalculatorHDF_Pointer":
        """Clone(itkMomentsThresholdCalculatorHDF self) -> itkMomentsThresholdCalculatorHDF_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_Clone(self)

    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDF

    def cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHDF *":
        """cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHDF"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMomentsThresholdCalculatorHDF *":
        """GetPointer(itkMomentsThresholdCalculatorHDF self) -> itkMomentsThresholdCalculatorHDF"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDF

        Create a new object of the class itkMomentsThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMomentsThresholdCalculatorHDF.Clone = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_Clone, None, itkMomentsThresholdCalculatorHDF)
itkMomentsThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_GetPointer, None, itkMomentsThresholdCalculatorHDF)
itkMomentsThresholdCalculatorHDF_swigregister = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_swigregister
itkMomentsThresholdCalculatorHDF_swigregister(itkMomentsThresholdCalculatorHDF)

def itkMomentsThresholdCalculatorHDF___New_orig__() -> "itkMomentsThresholdCalculatorHDF_Pointer":
    """itkMomentsThresholdCalculatorHDF___New_orig__() -> itkMomentsThresholdCalculatorHDF_Pointer"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF___New_orig__()

def itkMomentsThresholdCalculatorHDF_cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHDF *":
    """itkMomentsThresholdCalculatorHDF_cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHDF"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_cast(obj)

class itkMomentsThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkMomentsThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMomentsThresholdCalculatorHDSS_Pointer":
        """__New_orig__() -> itkMomentsThresholdCalculatorHDSS_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMomentsThresholdCalculatorHDSS_Pointer":
        """Clone(itkMomentsThresholdCalculatorHDSS self) -> itkMomentsThresholdCalculatorHDSS_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_Clone(self)

    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDSS

    def cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHDSS *":
        """cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHDSS"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMomentsThresholdCalculatorHDSS *":
        """GetPointer(itkMomentsThresholdCalculatorHDSS self) -> itkMomentsThresholdCalculatorHDSS"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDSS

        Create a new object of the class itkMomentsThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMomentsThresholdCalculatorHDSS.Clone = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_Clone, None, itkMomentsThresholdCalculatorHDSS)
itkMomentsThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_GetPointer, None, itkMomentsThresholdCalculatorHDSS)
itkMomentsThresholdCalculatorHDSS_swigregister = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_swigregister
itkMomentsThresholdCalculatorHDSS_swigregister(itkMomentsThresholdCalculatorHDSS)

def itkMomentsThresholdCalculatorHDSS___New_orig__() -> "itkMomentsThresholdCalculatorHDSS_Pointer":
    """itkMomentsThresholdCalculatorHDSS___New_orig__() -> itkMomentsThresholdCalculatorHDSS_Pointer"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS___New_orig__()

def itkMomentsThresholdCalculatorHDSS_cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHDSS *":
    """itkMomentsThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHDSS"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_cast(obj)

class itkMomentsThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkMomentsThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMomentsThresholdCalculatorHDUC_Pointer":
        """__New_orig__() -> itkMomentsThresholdCalculatorHDUC_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMomentsThresholdCalculatorHDUC_Pointer":
        """Clone(itkMomentsThresholdCalculatorHDUC self) -> itkMomentsThresholdCalculatorHDUC_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_Clone(self)

    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDUC

    def cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHDUC *":
        """cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHDUC"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMomentsThresholdCalculatorHDUC *":
        """GetPointer(itkMomentsThresholdCalculatorHDUC self) -> itkMomentsThresholdCalculatorHDUC"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDUC

        Create a new object of the class itkMomentsThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMomentsThresholdCalculatorHDUC.Clone = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_Clone, None, itkMomentsThresholdCalculatorHDUC)
itkMomentsThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_GetPointer, None, itkMomentsThresholdCalculatorHDUC)
itkMomentsThresholdCalculatorHDUC_swigregister = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_swigregister
itkMomentsThresholdCalculatorHDUC_swigregister(itkMomentsThresholdCalculatorHDUC)

def itkMomentsThresholdCalculatorHDUC___New_orig__() -> "itkMomentsThresholdCalculatorHDUC_Pointer":
    """itkMomentsThresholdCalculatorHDUC___New_orig__() -> itkMomentsThresholdCalculatorHDUC_Pointer"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC___New_orig__()

def itkMomentsThresholdCalculatorHDUC_cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHDUC *":
    """itkMomentsThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHDUC"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_cast(obj)

class itkMomentsThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkMomentsThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMomentsThresholdCalculatorHFF_Pointer":
        """__New_orig__() -> itkMomentsThresholdCalculatorHFF_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMomentsThresholdCalculatorHFF_Pointer":
        """Clone(itkMomentsThresholdCalculatorHFF self) -> itkMomentsThresholdCalculatorHFF_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_Clone(self)

    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFF

    def cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHFF *":
        """cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHFF"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMomentsThresholdCalculatorHFF *":
        """GetPointer(itkMomentsThresholdCalculatorHFF self) -> itkMomentsThresholdCalculatorHFF"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFF

        Create a new object of the class itkMomentsThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMomentsThresholdCalculatorHFF.Clone = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_Clone, None, itkMomentsThresholdCalculatorHFF)
itkMomentsThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_GetPointer, None, itkMomentsThresholdCalculatorHFF)
itkMomentsThresholdCalculatorHFF_swigregister = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_swigregister
itkMomentsThresholdCalculatorHFF_swigregister(itkMomentsThresholdCalculatorHFF)

def itkMomentsThresholdCalculatorHFF___New_orig__() -> "itkMomentsThresholdCalculatorHFF_Pointer":
    """itkMomentsThresholdCalculatorHFF___New_orig__() -> itkMomentsThresholdCalculatorHFF_Pointer"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF___New_orig__()

def itkMomentsThresholdCalculatorHFF_cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHFF *":
    """itkMomentsThresholdCalculatorHFF_cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHFF"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_cast(obj)

class itkMomentsThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkMomentsThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMomentsThresholdCalculatorHFSS_Pointer":
        """__New_orig__() -> itkMomentsThresholdCalculatorHFSS_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMomentsThresholdCalculatorHFSS_Pointer":
        """Clone(itkMomentsThresholdCalculatorHFSS self) -> itkMomentsThresholdCalculatorHFSS_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_Clone(self)

    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFSS

    def cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHFSS *":
        """cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHFSS"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMomentsThresholdCalculatorHFSS *":
        """GetPointer(itkMomentsThresholdCalculatorHFSS self) -> itkMomentsThresholdCalculatorHFSS"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFSS

        Create a new object of the class itkMomentsThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMomentsThresholdCalculatorHFSS.Clone = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_Clone, None, itkMomentsThresholdCalculatorHFSS)
itkMomentsThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_GetPointer, None, itkMomentsThresholdCalculatorHFSS)
itkMomentsThresholdCalculatorHFSS_swigregister = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_swigregister
itkMomentsThresholdCalculatorHFSS_swigregister(itkMomentsThresholdCalculatorHFSS)

def itkMomentsThresholdCalculatorHFSS___New_orig__() -> "itkMomentsThresholdCalculatorHFSS_Pointer":
    """itkMomentsThresholdCalculatorHFSS___New_orig__() -> itkMomentsThresholdCalculatorHFSS_Pointer"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS___New_orig__()

def itkMomentsThresholdCalculatorHFSS_cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHFSS *":
    """itkMomentsThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHFSS"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_cast(obj)

class itkMomentsThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkMomentsThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMomentsThresholdCalculatorHFUC_Pointer":
        """__New_orig__() -> itkMomentsThresholdCalculatorHFUC_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMomentsThresholdCalculatorHFUC_Pointer":
        """Clone(itkMomentsThresholdCalculatorHFUC self) -> itkMomentsThresholdCalculatorHFUC_Pointer"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_Clone(self)

    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFUC

    def cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHFUC *":
        """cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHFUC"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMomentsThresholdCalculatorHFUC *":
        """GetPointer(itkMomentsThresholdCalculatorHFUC self) -> itkMomentsThresholdCalculatorHFUC"""
        return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFUC

        Create a new object of the class itkMomentsThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMomentsThresholdCalculatorHFUC.Clone = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_Clone, None, itkMomentsThresholdCalculatorHFUC)
itkMomentsThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_GetPointer, None, itkMomentsThresholdCalculatorHFUC)
itkMomentsThresholdCalculatorHFUC_swigregister = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_swigregister
itkMomentsThresholdCalculatorHFUC_swigregister(itkMomentsThresholdCalculatorHFUC)

def itkMomentsThresholdCalculatorHFUC___New_orig__() -> "itkMomentsThresholdCalculatorHFUC_Pointer":
    """itkMomentsThresholdCalculatorHFUC___New_orig__() -> itkMomentsThresholdCalculatorHFUC_Pointer"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC___New_orig__()

def itkMomentsThresholdCalculatorHFUC_cast(obj: 'itkLightObject') -> "itkMomentsThresholdCalculatorHFUC *":
    """itkMomentsThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkMomentsThresholdCalculatorHFUC"""
    return _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_cast(obj)



