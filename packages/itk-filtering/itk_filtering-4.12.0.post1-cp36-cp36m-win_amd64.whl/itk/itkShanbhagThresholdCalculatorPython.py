# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShanbhagThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkShanbhagThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkShanbhagThresholdCalculatorPython')
    _itkShanbhagThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShanbhagThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkShanbhagThresholdCalculatorPython
            return _itkShanbhagThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkShanbhagThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkShanbhagThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShanbhagThresholdCalculatorPython
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
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkSamplePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython

def itkShanbhagThresholdCalculatorHFF_New():
  return itkShanbhagThresholdCalculatorHFF.New()


def itkShanbhagThresholdCalculatorHDF_New():
  return itkShanbhagThresholdCalculatorHDF.New()


def itkShanbhagThresholdCalculatorHFUC_New():
  return itkShanbhagThresholdCalculatorHFUC.New()


def itkShanbhagThresholdCalculatorHDUC_New():
  return itkShanbhagThresholdCalculatorHDUC.New()


def itkShanbhagThresholdCalculatorHFSS_New():
  return itkShanbhagThresholdCalculatorHFSS.New()


def itkShanbhagThresholdCalculatorHDSS_New():
  return itkShanbhagThresholdCalculatorHDSS.New()

class itkShanbhagThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkShanbhagThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShanbhagThresholdCalculatorHDF_Pointer":
        """__New_orig__() -> itkShanbhagThresholdCalculatorHDF_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShanbhagThresholdCalculatorHDF_Pointer":
        """Clone(itkShanbhagThresholdCalculatorHDF self) -> itkShanbhagThresholdCalculatorHDF_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_Clone(self)

    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDF

    def cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHDF *":
        """cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHDF"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShanbhagThresholdCalculatorHDF *":
        """GetPointer(itkShanbhagThresholdCalculatorHDF self) -> itkShanbhagThresholdCalculatorHDF"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDF

        Create a new object of the class itkShanbhagThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShanbhagThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShanbhagThresholdCalculatorHDF.Clone = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_Clone, None, itkShanbhagThresholdCalculatorHDF)
itkShanbhagThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_GetPointer, None, itkShanbhagThresholdCalculatorHDF)
itkShanbhagThresholdCalculatorHDF_swigregister = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_swigregister
itkShanbhagThresholdCalculatorHDF_swigregister(itkShanbhagThresholdCalculatorHDF)

def itkShanbhagThresholdCalculatorHDF___New_orig__() -> "itkShanbhagThresholdCalculatorHDF_Pointer":
    """itkShanbhagThresholdCalculatorHDF___New_orig__() -> itkShanbhagThresholdCalculatorHDF_Pointer"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF___New_orig__()

def itkShanbhagThresholdCalculatorHDF_cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHDF *":
    """itkShanbhagThresholdCalculatorHDF_cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHDF"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_cast(obj)

class itkShanbhagThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkShanbhagThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShanbhagThresholdCalculatorHDSS_Pointer":
        """__New_orig__() -> itkShanbhagThresholdCalculatorHDSS_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShanbhagThresholdCalculatorHDSS_Pointer":
        """Clone(itkShanbhagThresholdCalculatorHDSS self) -> itkShanbhagThresholdCalculatorHDSS_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_Clone(self)

    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDSS

    def cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHDSS *":
        """cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHDSS"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShanbhagThresholdCalculatorHDSS *":
        """GetPointer(itkShanbhagThresholdCalculatorHDSS self) -> itkShanbhagThresholdCalculatorHDSS"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDSS

        Create a new object of the class itkShanbhagThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShanbhagThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShanbhagThresholdCalculatorHDSS.Clone = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_Clone, None, itkShanbhagThresholdCalculatorHDSS)
itkShanbhagThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_GetPointer, None, itkShanbhagThresholdCalculatorHDSS)
itkShanbhagThresholdCalculatorHDSS_swigregister = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_swigregister
itkShanbhagThresholdCalculatorHDSS_swigregister(itkShanbhagThresholdCalculatorHDSS)

def itkShanbhagThresholdCalculatorHDSS___New_orig__() -> "itkShanbhagThresholdCalculatorHDSS_Pointer":
    """itkShanbhagThresholdCalculatorHDSS___New_orig__() -> itkShanbhagThresholdCalculatorHDSS_Pointer"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS___New_orig__()

def itkShanbhagThresholdCalculatorHDSS_cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHDSS *":
    """itkShanbhagThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHDSS"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_cast(obj)

class itkShanbhagThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkShanbhagThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShanbhagThresholdCalculatorHDUC_Pointer":
        """__New_orig__() -> itkShanbhagThresholdCalculatorHDUC_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShanbhagThresholdCalculatorHDUC_Pointer":
        """Clone(itkShanbhagThresholdCalculatorHDUC self) -> itkShanbhagThresholdCalculatorHDUC_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_Clone(self)

    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDUC

    def cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHDUC *":
        """cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHDUC"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShanbhagThresholdCalculatorHDUC *":
        """GetPointer(itkShanbhagThresholdCalculatorHDUC self) -> itkShanbhagThresholdCalculatorHDUC"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDUC

        Create a new object of the class itkShanbhagThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShanbhagThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShanbhagThresholdCalculatorHDUC.Clone = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_Clone, None, itkShanbhagThresholdCalculatorHDUC)
itkShanbhagThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_GetPointer, None, itkShanbhagThresholdCalculatorHDUC)
itkShanbhagThresholdCalculatorHDUC_swigregister = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_swigregister
itkShanbhagThresholdCalculatorHDUC_swigregister(itkShanbhagThresholdCalculatorHDUC)

def itkShanbhagThresholdCalculatorHDUC___New_orig__() -> "itkShanbhagThresholdCalculatorHDUC_Pointer":
    """itkShanbhagThresholdCalculatorHDUC___New_orig__() -> itkShanbhagThresholdCalculatorHDUC_Pointer"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC___New_orig__()

def itkShanbhagThresholdCalculatorHDUC_cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHDUC *":
    """itkShanbhagThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHDUC"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_cast(obj)

class itkShanbhagThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkShanbhagThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShanbhagThresholdCalculatorHFF_Pointer":
        """__New_orig__() -> itkShanbhagThresholdCalculatorHFF_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShanbhagThresholdCalculatorHFF_Pointer":
        """Clone(itkShanbhagThresholdCalculatorHFF self) -> itkShanbhagThresholdCalculatorHFF_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_Clone(self)

    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFF

    def cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHFF *":
        """cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHFF"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShanbhagThresholdCalculatorHFF *":
        """GetPointer(itkShanbhagThresholdCalculatorHFF self) -> itkShanbhagThresholdCalculatorHFF"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFF

        Create a new object of the class itkShanbhagThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShanbhagThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShanbhagThresholdCalculatorHFF.Clone = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_Clone, None, itkShanbhagThresholdCalculatorHFF)
itkShanbhagThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_GetPointer, None, itkShanbhagThresholdCalculatorHFF)
itkShanbhagThresholdCalculatorHFF_swigregister = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_swigregister
itkShanbhagThresholdCalculatorHFF_swigregister(itkShanbhagThresholdCalculatorHFF)

def itkShanbhagThresholdCalculatorHFF___New_orig__() -> "itkShanbhagThresholdCalculatorHFF_Pointer":
    """itkShanbhagThresholdCalculatorHFF___New_orig__() -> itkShanbhagThresholdCalculatorHFF_Pointer"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF___New_orig__()

def itkShanbhagThresholdCalculatorHFF_cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHFF *":
    """itkShanbhagThresholdCalculatorHFF_cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHFF"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_cast(obj)

class itkShanbhagThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkShanbhagThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShanbhagThresholdCalculatorHFSS_Pointer":
        """__New_orig__() -> itkShanbhagThresholdCalculatorHFSS_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShanbhagThresholdCalculatorHFSS_Pointer":
        """Clone(itkShanbhagThresholdCalculatorHFSS self) -> itkShanbhagThresholdCalculatorHFSS_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_Clone(self)

    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFSS

    def cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHFSS *":
        """cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHFSS"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShanbhagThresholdCalculatorHFSS *":
        """GetPointer(itkShanbhagThresholdCalculatorHFSS self) -> itkShanbhagThresholdCalculatorHFSS"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFSS

        Create a new object of the class itkShanbhagThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShanbhagThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShanbhagThresholdCalculatorHFSS.Clone = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_Clone, None, itkShanbhagThresholdCalculatorHFSS)
itkShanbhagThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_GetPointer, None, itkShanbhagThresholdCalculatorHFSS)
itkShanbhagThresholdCalculatorHFSS_swigregister = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_swigregister
itkShanbhagThresholdCalculatorHFSS_swigregister(itkShanbhagThresholdCalculatorHFSS)

def itkShanbhagThresholdCalculatorHFSS___New_orig__() -> "itkShanbhagThresholdCalculatorHFSS_Pointer":
    """itkShanbhagThresholdCalculatorHFSS___New_orig__() -> itkShanbhagThresholdCalculatorHFSS_Pointer"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS___New_orig__()

def itkShanbhagThresholdCalculatorHFSS_cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHFSS *":
    """itkShanbhagThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHFSS"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_cast(obj)

class itkShanbhagThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkShanbhagThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShanbhagThresholdCalculatorHFUC_Pointer":
        """__New_orig__() -> itkShanbhagThresholdCalculatorHFUC_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShanbhagThresholdCalculatorHFUC_Pointer":
        """Clone(itkShanbhagThresholdCalculatorHFUC self) -> itkShanbhagThresholdCalculatorHFUC_Pointer"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_Clone(self)

    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFUC

    def cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHFUC *":
        """cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHFUC"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkShanbhagThresholdCalculatorHFUC *":
        """GetPointer(itkShanbhagThresholdCalculatorHFUC self) -> itkShanbhagThresholdCalculatorHFUC"""
        return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFUC

        Create a new object of the class itkShanbhagThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShanbhagThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShanbhagThresholdCalculatorHFUC.Clone = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_Clone, None, itkShanbhagThresholdCalculatorHFUC)
itkShanbhagThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_GetPointer, None, itkShanbhagThresholdCalculatorHFUC)
itkShanbhagThresholdCalculatorHFUC_swigregister = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_swigregister
itkShanbhagThresholdCalculatorHFUC_swigregister(itkShanbhagThresholdCalculatorHFUC)

def itkShanbhagThresholdCalculatorHFUC___New_orig__() -> "itkShanbhagThresholdCalculatorHFUC_Pointer":
    """itkShanbhagThresholdCalculatorHFUC___New_orig__() -> itkShanbhagThresholdCalculatorHFUC_Pointer"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC___New_orig__()

def itkShanbhagThresholdCalculatorHFUC_cast(obj: 'itkLightObject') -> "itkShanbhagThresholdCalculatorHFUC *":
    """itkShanbhagThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkShanbhagThresholdCalculatorHFUC"""
    return _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_cast(obj)



