# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkOtsuThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkOtsuThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkOtsuThresholdCalculatorPython')
    _itkOtsuThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkOtsuThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkOtsuThresholdCalculatorPython
            return _itkOtsuThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkOtsuThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkOtsuThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkOtsuThresholdCalculatorPython
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
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkSamplePython
import ITKCommonBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython

def itkOtsuThresholdCalculatorHFF_New():
  return itkOtsuThresholdCalculatorHFF.New()


def itkOtsuThresholdCalculatorHDF_New():
  return itkOtsuThresholdCalculatorHDF.New()


def itkOtsuThresholdCalculatorHFUC_New():
  return itkOtsuThresholdCalculatorHFUC.New()


def itkOtsuThresholdCalculatorHDUC_New():
  return itkOtsuThresholdCalculatorHDUC.New()


def itkOtsuThresholdCalculatorHFSS_New():
  return itkOtsuThresholdCalculatorHFSS.New()


def itkOtsuThresholdCalculatorHDSS_New():
  return itkOtsuThresholdCalculatorHDSS.New()

class itkOtsuThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkOtsuThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOtsuThresholdCalculatorHDF_Pointer":
        """__New_orig__() -> itkOtsuThresholdCalculatorHDF_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOtsuThresholdCalculatorHDF_Pointer":
        """Clone(itkOtsuThresholdCalculatorHDF self) -> itkOtsuThresholdCalculatorHDF_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_Clone(self)


    def Compute(self) -> "void":
        """Compute(itkOtsuThresholdCalculatorHDF self)"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_Compute(self)

    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDF

    def cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHDF *":
        """cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHDF"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkOtsuThresholdCalculatorHDF *":
        """GetPointer(itkOtsuThresholdCalculatorHDF self) -> itkOtsuThresholdCalculatorHDF"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDF

        Create a new object of the class itkOtsuThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOtsuThresholdCalculatorHDF.Clone = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_Clone, None, itkOtsuThresholdCalculatorHDF)
itkOtsuThresholdCalculatorHDF.Compute = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_Compute, None, itkOtsuThresholdCalculatorHDF)
itkOtsuThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_GetPointer, None, itkOtsuThresholdCalculatorHDF)
itkOtsuThresholdCalculatorHDF_swigregister = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_swigregister
itkOtsuThresholdCalculatorHDF_swigregister(itkOtsuThresholdCalculatorHDF)

def itkOtsuThresholdCalculatorHDF___New_orig__() -> "itkOtsuThresholdCalculatorHDF_Pointer":
    """itkOtsuThresholdCalculatorHDF___New_orig__() -> itkOtsuThresholdCalculatorHDF_Pointer"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF___New_orig__()

def itkOtsuThresholdCalculatorHDF_cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHDF *":
    """itkOtsuThresholdCalculatorHDF_cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHDF"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_cast(obj)

class itkOtsuThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkOtsuThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOtsuThresholdCalculatorHDSS_Pointer":
        """__New_orig__() -> itkOtsuThresholdCalculatorHDSS_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOtsuThresholdCalculatorHDSS_Pointer":
        """Clone(itkOtsuThresholdCalculatorHDSS self) -> itkOtsuThresholdCalculatorHDSS_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_Clone(self)


    def Compute(self) -> "void":
        """Compute(itkOtsuThresholdCalculatorHDSS self)"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_Compute(self)

    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDSS

    def cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHDSS *":
        """cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHDSS"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkOtsuThresholdCalculatorHDSS *":
        """GetPointer(itkOtsuThresholdCalculatorHDSS self) -> itkOtsuThresholdCalculatorHDSS"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDSS

        Create a new object of the class itkOtsuThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOtsuThresholdCalculatorHDSS.Clone = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_Clone, None, itkOtsuThresholdCalculatorHDSS)
itkOtsuThresholdCalculatorHDSS.Compute = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_Compute, None, itkOtsuThresholdCalculatorHDSS)
itkOtsuThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_GetPointer, None, itkOtsuThresholdCalculatorHDSS)
itkOtsuThresholdCalculatorHDSS_swigregister = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_swigregister
itkOtsuThresholdCalculatorHDSS_swigregister(itkOtsuThresholdCalculatorHDSS)

def itkOtsuThresholdCalculatorHDSS___New_orig__() -> "itkOtsuThresholdCalculatorHDSS_Pointer":
    """itkOtsuThresholdCalculatorHDSS___New_orig__() -> itkOtsuThresholdCalculatorHDSS_Pointer"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS___New_orig__()

def itkOtsuThresholdCalculatorHDSS_cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHDSS *":
    """itkOtsuThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHDSS"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_cast(obj)

class itkOtsuThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkOtsuThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOtsuThresholdCalculatorHDUC_Pointer":
        """__New_orig__() -> itkOtsuThresholdCalculatorHDUC_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOtsuThresholdCalculatorHDUC_Pointer":
        """Clone(itkOtsuThresholdCalculatorHDUC self) -> itkOtsuThresholdCalculatorHDUC_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_Clone(self)


    def Compute(self) -> "void":
        """Compute(itkOtsuThresholdCalculatorHDUC self)"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_Compute(self)

    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDUC

    def cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHDUC *":
        """cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHDUC"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkOtsuThresholdCalculatorHDUC *":
        """GetPointer(itkOtsuThresholdCalculatorHDUC self) -> itkOtsuThresholdCalculatorHDUC"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDUC

        Create a new object of the class itkOtsuThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOtsuThresholdCalculatorHDUC.Clone = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_Clone, None, itkOtsuThresholdCalculatorHDUC)
itkOtsuThresholdCalculatorHDUC.Compute = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_Compute, None, itkOtsuThresholdCalculatorHDUC)
itkOtsuThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_GetPointer, None, itkOtsuThresholdCalculatorHDUC)
itkOtsuThresholdCalculatorHDUC_swigregister = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_swigregister
itkOtsuThresholdCalculatorHDUC_swigregister(itkOtsuThresholdCalculatorHDUC)

def itkOtsuThresholdCalculatorHDUC___New_orig__() -> "itkOtsuThresholdCalculatorHDUC_Pointer":
    """itkOtsuThresholdCalculatorHDUC___New_orig__() -> itkOtsuThresholdCalculatorHDUC_Pointer"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC___New_orig__()

def itkOtsuThresholdCalculatorHDUC_cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHDUC *":
    """itkOtsuThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHDUC"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_cast(obj)

class itkOtsuThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkOtsuThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOtsuThresholdCalculatorHFF_Pointer":
        """__New_orig__() -> itkOtsuThresholdCalculatorHFF_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOtsuThresholdCalculatorHFF_Pointer":
        """Clone(itkOtsuThresholdCalculatorHFF self) -> itkOtsuThresholdCalculatorHFF_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_Clone(self)


    def Compute(self) -> "void":
        """Compute(itkOtsuThresholdCalculatorHFF self)"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_Compute(self)

    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFF

    def cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHFF *":
        """cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHFF"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkOtsuThresholdCalculatorHFF *":
        """GetPointer(itkOtsuThresholdCalculatorHFF self) -> itkOtsuThresholdCalculatorHFF"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFF

        Create a new object of the class itkOtsuThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOtsuThresholdCalculatorHFF.Clone = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_Clone, None, itkOtsuThresholdCalculatorHFF)
itkOtsuThresholdCalculatorHFF.Compute = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_Compute, None, itkOtsuThresholdCalculatorHFF)
itkOtsuThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_GetPointer, None, itkOtsuThresholdCalculatorHFF)
itkOtsuThresholdCalculatorHFF_swigregister = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_swigregister
itkOtsuThresholdCalculatorHFF_swigregister(itkOtsuThresholdCalculatorHFF)

def itkOtsuThresholdCalculatorHFF___New_orig__() -> "itkOtsuThresholdCalculatorHFF_Pointer":
    """itkOtsuThresholdCalculatorHFF___New_orig__() -> itkOtsuThresholdCalculatorHFF_Pointer"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF___New_orig__()

def itkOtsuThresholdCalculatorHFF_cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHFF *":
    """itkOtsuThresholdCalculatorHFF_cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHFF"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_cast(obj)

class itkOtsuThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkOtsuThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOtsuThresholdCalculatorHFSS_Pointer":
        """__New_orig__() -> itkOtsuThresholdCalculatorHFSS_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOtsuThresholdCalculatorHFSS_Pointer":
        """Clone(itkOtsuThresholdCalculatorHFSS self) -> itkOtsuThresholdCalculatorHFSS_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_Clone(self)


    def Compute(self) -> "void":
        """Compute(itkOtsuThresholdCalculatorHFSS self)"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_Compute(self)

    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFSS

    def cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHFSS *":
        """cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHFSS"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkOtsuThresholdCalculatorHFSS *":
        """GetPointer(itkOtsuThresholdCalculatorHFSS self) -> itkOtsuThresholdCalculatorHFSS"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFSS

        Create a new object of the class itkOtsuThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOtsuThresholdCalculatorHFSS.Clone = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_Clone, None, itkOtsuThresholdCalculatorHFSS)
itkOtsuThresholdCalculatorHFSS.Compute = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_Compute, None, itkOtsuThresholdCalculatorHFSS)
itkOtsuThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_GetPointer, None, itkOtsuThresholdCalculatorHFSS)
itkOtsuThresholdCalculatorHFSS_swigregister = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_swigregister
itkOtsuThresholdCalculatorHFSS_swigregister(itkOtsuThresholdCalculatorHFSS)

def itkOtsuThresholdCalculatorHFSS___New_orig__() -> "itkOtsuThresholdCalculatorHFSS_Pointer":
    """itkOtsuThresholdCalculatorHFSS___New_orig__() -> itkOtsuThresholdCalculatorHFSS_Pointer"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS___New_orig__()

def itkOtsuThresholdCalculatorHFSS_cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHFSS *":
    """itkOtsuThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHFSS"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_cast(obj)

class itkOtsuThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkOtsuThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOtsuThresholdCalculatorHFUC_Pointer":
        """__New_orig__() -> itkOtsuThresholdCalculatorHFUC_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOtsuThresholdCalculatorHFUC_Pointer":
        """Clone(itkOtsuThresholdCalculatorHFUC self) -> itkOtsuThresholdCalculatorHFUC_Pointer"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_Clone(self)


    def Compute(self) -> "void":
        """Compute(itkOtsuThresholdCalculatorHFUC self)"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_Compute(self)

    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFUC

    def cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHFUC *":
        """cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHFUC"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkOtsuThresholdCalculatorHFUC *":
        """GetPointer(itkOtsuThresholdCalculatorHFUC self) -> itkOtsuThresholdCalculatorHFUC"""
        return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFUC

        Create a new object of the class itkOtsuThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOtsuThresholdCalculatorHFUC.Clone = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_Clone, None, itkOtsuThresholdCalculatorHFUC)
itkOtsuThresholdCalculatorHFUC.Compute = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_Compute, None, itkOtsuThresholdCalculatorHFUC)
itkOtsuThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_GetPointer, None, itkOtsuThresholdCalculatorHFUC)
itkOtsuThresholdCalculatorHFUC_swigregister = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_swigregister
itkOtsuThresholdCalculatorHFUC_swigregister(itkOtsuThresholdCalculatorHFUC)

def itkOtsuThresholdCalculatorHFUC___New_orig__() -> "itkOtsuThresholdCalculatorHFUC_Pointer":
    """itkOtsuThresholdCalculatorHFUC___New_orig__() -> itkOtsuThresholdCalculatorHFUC_Pointer"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC___New_orig__()

def itkOtsuThresholdCalculatorHFUC_cast(obj: 'itkLightObject') -> "itkOtsuThresholdCalculatorHFUC *":
    """itkOtsuThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkOtsuThresholdCalculatorHFUC"""
    return _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_cast(obj)



