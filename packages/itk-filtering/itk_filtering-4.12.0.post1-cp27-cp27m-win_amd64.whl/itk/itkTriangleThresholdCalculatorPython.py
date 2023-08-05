# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTriangleThresholdCalculatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTriangleThresholdCalculatorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTriangleThresholdCalculatorPython')
    _itkTriangleThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTriangleThresholdCalculatorPython', [dirname(__file__)])
        except ImportError:
            import _itkTriangleThresholdCalculatorPython
            return _itkTriangleThresholdCalculatorPython
        try:
            _mod = imp.load_module('_itkTriangleThresholdCalculatorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTriangleThresholdCalculatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTriangleThresholdCalculatorPython
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
import itkSimpleDataObjectDecoratorPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkArrayPython
import ITKCommonBasePython
import itkHistogramPython
import itkSamplePython

def itkTriangleThresholdCalculatorHFF_New():
  return itkTriangleThresholdCalculatorHFF.New()


def itkTriangleThresholdCalculatorHDF_New():
  return itkTriangleThresholdCalculatorHDF.New()


def itkTriangleThresholdCalculatorHFUC_New():
  return itkTriangleThresholdCalculatorHFUC.New()


def itkTriangleThresholdCalculatorHDUC_New():
  return itkTriangleThresholdCalculatorHDUC.New()


def itkTriangleThresholdCalculatorHFSS_New():
  return itkTriangleThresholdCalculatorHFSS.New()


def itkTriangleThresholdCalculatorHDSS_New():
  return itkTriangleThresholdCalculatorHDSS.New()

class itkTriangleThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    """Proxy of C++ itkTriangleThresholdCalculatorHDF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTriangleThresholdCalculatorHDF_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTriangleThresholdCalculatorHDF self) -> itkTriangleThresholdCalculatorHDF_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_Clone(self)

    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDF

    def cast(obj):
        """cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHDF"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTriangleThresholdCalculatorHDF self) -> itkTriangleThresholdCalculatorHDF"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDF

        Create a new object of the class itkTriangleThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTriangleThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTriangleThresholdCalculatorHDF.Clone = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_Clone, None, itkTriangleThresholdCalculatorHDF)
itkTriangleThresholdCalculatorHDF.GetPointer = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_GetPointer, None, itkTriangleThresholdCalculatorHDF)
itkTriangleThresholdCalculatorHDF_swigregister = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_swigregister
itkTriangleThresholdCalculatorHDF_swigregister(itkTriangleThresholdCalculatorHDF)

def itkTriangleThresholdCalculatorHDF___New_orig__():
    """itkTriangleThresholdCalculatorHDF___New_orig__() -> itkTriangleThresholdCalculatorHDF_Pointer"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF___New_orig__()

def itkTriangleThresholdCalculatorHDF_cast(obj):
    """itkTriangleThresholdCalculatorHDF_cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHDF"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_cast(obj)

class itkTriangleThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    """Proxy of C++ itkTriangleThresholdCalculatorHDSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTriangleThresholdCalculatorHDSS_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTriangleThresholdCalculatorHDSS self) -> itkTriangleThresholdCalculatorHDSS_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_Clone(self)

    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDSS

    def cast(obj):
        """cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHDSS"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTriangleThresholdCalculatorHDSS self) -> itkTriangleThresholdCalculatorHDSS"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDSS

        Create a new object of the class itkTriangleThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTriangleThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTriangleThresholdCalculatorHDSS.Clone = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_Clone, None, itkTriangleThresholdCalculatorHDSS)
itkTriangleThresholdCalculatorHDSS.GetPointer = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_GetPointer, None, itkTriangleThresholdCalculatorHDSS)
itkTriangleThresholdCalculatorHDSS_swigregister = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_swigregister
itkTriangleThresholdCalculatorHDSS_swigregister(itkTriangleThresholdCalculatorHDSS)

def itkTriangleThresholdCalculatorHDSS___New_orig__():
    """itkTriangleThresholdCalculatorHDSS___New_orig__() -> itkTriangleThresholdCalculatorHDSS_Pointer"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS___New_orig__()

def itkTriangleThresholdCalculatorHDSS_cast(obj):
    """itkTriangleThresholdCalculatorHDSS_cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHDSS"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_cast(obj)

class itkTriangleThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    """Proxy of C++ itkTriangleThresholdCalculatorHDUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTriangleThresholdCalculatorHDUC_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTriangleThresholdCalculatorHDUC self) -> itkTriangleThresholdCalculatorHDUC_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_Clone(self)

    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDUC

    def cast(obj):
        """cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHDUC"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTriangleThresholdCalculatorHDUC self) -> itkTriangleThresholdCalculatorHDUC"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDUC

        Create a new object of the class itkTriangleThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTriangleThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTriangleThresholdCalculatorHDUC.Clone = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_Clone, None, itkTriangleThresholdCalculatorHDUC)
itkTriangleThresholdCalculatorHDUC.GetPointer = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_GetPointer, None, itkTriangleThresholdCalculatorHDUC)
itkTriangleThresholdCalculatorHDUC_swigregister = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_swigregister
itkTriangleThresholdCalculatorHDUC_swigregister(itkTriangleThresholdCalculatorHDUC)

def itkTriangleThresholdCalculatorHDUC___New_orig__():
    """itkTriangleThresholdCalculatorHDUC___New_orig__() -> itkTriangleThresholdCalculatorHDUC_Pointer"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC___New_orig__()

def itkTriangleThresholdCalculatorHDUC_cast(obj):
    """itkTriangleThresholdCalculatorHDUC_cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHDUC"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_cast(obj)

class itkTriangleThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    """Proxy of C++ itkTriangleThresholdCalculatorHFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTriangleThresholdCalculatorHFF_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTriangleThresholdCalculatorHFF self) -> itkTriangleThresholdCalculatorHFF_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_Clone(self)

    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFF

    def cast(obj):
        """cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHFF"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTriangleThresholdCalculatorHFF self) -> itkTriangleThresholdCalculatorHFF"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFF

        Create a new object of the class itkTriangleThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTriangleThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTriangleThresholdCalculatorHFF.Clone = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_Clone, None, itkTriangleThresholdCalculatorHFF)
itkTriangleThresholdCalculatorHFF.GetPointer = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_GetPointer, None, itkTriangleThresholdCalculatorHFF)
itkTriangleThresholdCalculatorHFF_swigregister = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_swigregister
itkTriangleThresholdCalculatorHFF_swigregister(itkTriangleThresholdCalculatorHFF)

def itkTriangleThresholdCalculatorHFF___New_orig__():
    """itkTriangleThresholdCalculatorHFF___New_orig__() -> itkTriangleThresholdCalculatorHFF_Pointer"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF___New_orig__()

def itkTriangleThresholdCalculatorHFF_cast(obj):
    """itkTriangleThresholdCalculatorHFF_cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHFF"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_cast(obj)

class itkTriangleThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    """Proxy of C++ itkTriangleThresholdCalculatorHFSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTriangleThresholdCalculatorHFSS_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTriangleThresholdCalculatorHFSS self) -> itkTriangleThresholdCalculatorHFSS_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_Clone(self)

    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFSS

    def cast(obj):
        """cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHFSS"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTriangleThresholdCalculatorHFSS self) -> itkTriangleThresholdCalculatorHFSS"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFSS

        Create a new object of the class itkTriangleThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTriangleThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTriangleThresholdCalculatorHFSS.Clone = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_Clone, None, itkTriangleThresholdCalculatorHFSS)
itkTriangleThresholdCalculatorHFSS.GetPointer = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_GetPointer, None, itkTriangleThresholdCalculatorHFSS)
itkTriangleThresholdCalculatorHFSS_swigregister = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_swigregister
itkTriangleThresholdCalculatorHFSS_swigregister(itkTriangleThresholdCalculatorHFSS)

def itkTriangleThresholdCalculatorHFSS___New_orig__():
    """itkTriangleThresholdCalculatorHFSS___New_orig__() -> itkTriangleThresholdCalculatorHFSS_Pointer"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS___New_orig__()

def itkTriangleThresholdCalculatorHFSS_cast(obj):
    """itkTriangleThresholdCalculatorHFSS_cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHFSS"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_cast(obj)

class itkTriangleThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    """Proxy of C++ itkTriangleThresholdCalculatorHFUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTriangleThresholdCalculatorHFUC_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTriangleThresholdCalculatorHFUC self) -> itkTriangleThresholdCalculatorHFUC_Pointer"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_Clone(self)

    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFUC

    def cast(obj):
        """cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHFUC"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTriangleThresholdCalculatorHFUC self) -> itkTriangleThresholdCalculatorHFUC"""
        return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFUC

        Create a new object of the class itkTriangleThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTriangleThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTriangleThresholdCalculatorHFUC.Clone = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_Clone, None, itkTriangleThresholdCalculatorHFUC)
itkTriangleThresholdCalculatorHFUC.GetPointer = new_instancemethod(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_GetPointer, None, itkTriangleThresholdCalculatorHFUC)
itkTriangleThresholdCalculatorHFUC_swigregister = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_swigregister
itkTriangleThresholdCalculatorHFUC_swigregister(itkTriangleThresholdCalculatorHFUC)

def itkTriangleThresholdCalculatorHFUC___New_orig__():
    """itkTriangleThresholdCalculatorHFUC___New_orig__() -> itkTriangleThresholdCalculatorHFUC_Pointer"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC___New_orig__()

def itkTriangleThresholdCalculatorHFUC_cast(obj):
    """itkTriangleThresholdCalculatorHFUC_cast(itkLightObject obj) -> itkTriangleThresholdCalculatorHFUC"""
    return _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_cast(obj)



