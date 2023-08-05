# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelObjectLinePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLabelObjectLinePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLabelObjectLinePython')
    _itkLabelObjectLinePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelObjectLinePython', [dirname(__file__)])
        except ImportError:
            import _itkLabelObjectLinePython
            return _itkLabelObjectLinePython
        try:
            _mod = imp.load_module('_itkLabelObjectLinePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLabelObjectLinePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelObjectLinePython
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


import itkIndexPython
import itkSizePython
import pyBasePython
import itkOffsetPython
import ITKCommonBasePython
class itkLabelObjectLine2(object):
    """Proxy of C++ itkLabelObjectLine2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkLabelObjectLinePython.delete_itkLabelObjectLine2

    def SetIndex(self, idx: 'itkIndex2') -> "void":
        """SetIndex(itkLabelObjectLine2 self, itkIndex2 idx)"""
        return _itkLabelObjectLinePython.itkLabelObjectLine2_SetIndex(self, idx)


    def GetIndex(self) -> "itkIndex2 const &":
        """GetIndex(itkLabelObjectLine2 self) -> itkIndex2"""
        return _itkLabelObjectLinePython.itkLabelObjectLine2_GetIndex(self)


    def SetLength(self, length: 'unsigned long const') -> "void":
        """SetLength(itkLabelObjectLine2 self, unsigned long const length)"""
        return _itkLabelObjectLinePython.itkLabelObjectLine2_SetLength(self, length)


    def GetLength(self) -> "unsigned long const &":
        """GetLength(itkLabelObjectLine2 self) -> unsigned long const &"""
        return _itkLabelObjectLinePython.itkLabelObjectLine2_GetLength(self)


    def HasIndex(self, idx: 'itkIndex2') -> "bool":
        """HasIndex(itkLabelObjectLine2 self, itkIndex2 idx) -> bool"""
        return _itkLabelObjectLinePython.itkLabelObjectLine2_HasIndex(self, idx)


    def IsNextIndex(self, idx: 'itkIndex2') -> "bool":
        """IsNextIndex(itkLabelObjectLine2 self, itkIndex2 idx) -> bool"""
        return _itkLabelObjectLinePython.itkLabelObjectLine2_IsNextIndex(self, idx)


    def Print(self, os: 'ostream', indent: 'itkIndent'=0) -> "void":
        """
        Print(itkLabelObjectLine2 self, ostream os, itkIndent indent=0)
        Print(itkLabelObjectLine2 self, ostream os)
        """
        return _itkLabelObjectLinePython.itkLabelObjectLine2_Print(self, os, indent)


    def __init__(self, *args):
        """
        __init__(itkLabelObjectLine2 self) -> itkLabelObjectLine2
        __init__(itkLabelObjectLine2 self, itkIndex2 idx, unsigned long const & length) -> itkLabelObjectLine2
        __init__(itkLabelObjectLine2 self, itkLabelObjectLine2 arg0) -> itkLabelObjectLine2
        """
        _itkLabelObjectLinePython.itkLabelObjectLine2_swiginit(self, _itkLabelObjectLinePython.new_itkLabelObjectLine2(*args))
itkLabelObjectLine2.SetIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_SetIndex, None, itkLabelObjectLine2)
itkLabelObjectLine2.GetIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_GetIndex, None, itkLabelObjectLine2)
itkLabelObjectLine2.SetLength = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_SetLength, None, itkLabelObjectLine2)
itkLabelObjectLine2.GetLength = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_GetLength, None, itkLabelObjectLine2)
itkLabelObjectLine2.HasIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_HasIndex, None, itkLabelObjectLine2)
itkLabelObjectLine2.IsNextIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_IsNextIndex, None, itkLabelObjectLine2)
itkLabelObjectLine2.Print = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine2_Print, None, itkLabelObjectLine2)
itkLabelObjectLine2_swigregister = _itkLabelObjectLinePython.itkLabelObjectLine2_swigregister
itkLabelObjectLine2_swigregister(itkLabelObjectLine2)

class itkLabelObjectLine3(object):
    """Proxy of C++ itkLabelObjectLine3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkLabelObjectLinePython.delete_itkLabelObjectLine3

    def SetIndex(self, idx: 'itkIndex3') -> "void":
        """SetIndex(itkLabelObjectLine3 self, itkIndex3 idx)"""
        return _itkLabelObjectLinePython.itkLabelObjectLine3_SetIndex(self, idx)


    def GetIndex(self) -> "itkIndex3 const &":
        """GetIndex(itkLabelObjectLine3 self) -> itkIndex3"""
        return _itkLabelObjectLinePython.itkLabelObjectLine3_GetIndex(self)


    def SetLength(self, length: 'unsigned long const') -> "void":
        """SetLength(itkLabelObjectLine3 self, unsigned long const length)"""
        return _itkLabelObjectLinePython.itkLabelObjectLine3_SetLength(self, length)


    def GetLength(self) -> "unsigned long const &":
        """GetLength(itkLabelObjectLine3 self) -> unsigned long const &"""
        return _itkLabelObjectLinePython.itkLabelObjectLine3_GetLength(self)


    def HasIndex(self, idx: 'itkIndex3') -> "bool":
        """HasIndex(itkLabelObjectLine3 self, itkIndex3 idx) -> bool"""
        return _itkLabelObjectLinePython.itkLabelObjectLine3_HasIndex(self, idx)


    def IsNextIndex(self, idx: 'itkIndex3') -> "bool":
        """IsNextIndex(itkLabelObjectLine3 self, itkIndex3 idx) -> bool"""
        return _itkLabelObjectLinePython.itkLabelObjectLine3_IsNextIndex(self, idx)


    def Print(self, os: 'ostream', indent: 'itkIndent'=0) -> "void":
        """
        Print(itkLabelObjectLine3 self, ostream os, itkIndent indent=0)
        Print(itkLabelObjectLine3 self, ostream os)
        """
        return _itkLabelObjectLinePython.itkLabelObjectLine3_Print(self, os, indent)


    def __init__(self, *args):
        """
        __init__(itkLabelObjectLine3 self) -> itkLabelObjectLine3
        __init__(itkLabelObjectLine3 self, itkIndex3 idx, unsigned long const & length) -> itkLabelObjectLine3
        __init__(itkLabelObjectLine3 self, itkLabelObjectLine3 arg0) -> itkLabelObjectLine3
        """
        _itkLabelObjectLinePython.itkLabelObjectLine3_swiginit(self, _itkLabelObjectLinePython.new_itkLabelObjectLine3(*args))
itkLabelObjectLine3.SetIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_SetIndex, None, itkLabelObjectLine3)
itkLabelObjectLine3.GetIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_GetIndex, None, itkLabelObjectLine3)
itkLabelObjectLine3.SetLength = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_SetLength, None, itkLabelObjectLine3)
itkLabelObjectLine3.GetLength = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_GetLength, None, itkLabelObjectLine3)
itkLabelObjectLine3.HasIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_HasIndex, None, itkLabelObjectLine3)
itkLabelObjectLine3.IsNextIndex = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_IsNextIndex, None, itkLabelObjectLine3)
itkLabelObjectLine3.Print = new_instancemethod(_itkLabelObjectLinePython.itkLabelObjectLine3_Print, None, itkLabelObjectLine3)
itkLabelObjectLine3_swigregister = _itkLabelObjectLinePython.itkLabelObjectLine3_swigregister
itkLabelObjectLine3_swigregister(itkLabelObjectLine3)



