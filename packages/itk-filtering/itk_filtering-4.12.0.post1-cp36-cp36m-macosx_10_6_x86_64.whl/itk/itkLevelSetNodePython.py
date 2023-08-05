# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLevelSetNodePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLevelSetNodePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLevelSetNodePython')
    _itkLevelSetNodePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLevelSetNodePython', [dirname(__file__)])
        except ImportError:
            import _itkLevelSetNodePython
            return _itkLevelSetNodePython
        try:
            _mod = imp.load_module('_itkLevelSetNodePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLevelSetNodePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLevelSetNodePython
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
class itkLevelSetNodeF2(object):
    """Proxy of C++ itkLevelSetNodeF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __gt__(self, node: 'itkLevelSetNodeF2') -> "bool":
        """__gt__(itkLevelSetNodeF2 self, itkLevelSetNodeF2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF2___gt__(self, node)


    def __lt__(self, node: 'itkLevelSetNodeF2') -> "bool":
        """__lt__(itkLevelSetNodeF2 self, itkLevelSetNodeF2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF2___lt__(self, node)


    def __le__(self, node: 'itkLevelSetNodeF2') -> "bool":
        """__le__(itkLevelSetNodeF2 self, itkLevelSetNodeF2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF2___le__(self, node)


    def __ge__(self, node: 'itkLevelSetNodeF2') -> "bool":
        """__ge__(itkLevelSetNodeF2 self, itkLevelSetNodeF2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF2___ge__(self, node)


    def GetValue(self, *args) -> "float const &":
        """
        GetValue(itkLevelSetNodeF2 self) -> float
        GetValue(itkLevelSetNodeF2 self) -> float const &
        """
        return _itkLevelSetNodePython.itkLevelSetNodeF2_GetValue(self, *args)


    def SetValue(self, input: 'float const &') -> "void":
        """SetValue(itkLevelSetNodeF2 self, float const & input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeF2_SetValue(self, input)


    def GetIndex(self, *args) -> "itkIndex2 const &":
        """
        GetIndex(itkLevelSetNodeF2 self) -> itkIndex2
        GetIndex(itkLevelSetNodeF2 self) -> itkIndex2
        """
        return _itkLevelSetNodePython.itkLevelSetNodeF2_GetIndex(self, *args)


    def SetIndex(self, input: 'itkIndex2') -> "void":
        """SetIndex(itkLevelSetNodeF2 self, itkIndex2 input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeF2_SetIndex(self, input)


    def __init__(self, *args):
        """
        __init__(itkLevelSetNodeF2 self) -> itkLevelSetNodeF2
        __init__(itkLevelSetNodeF2 self, itkLevelSetNodeF2 node) -> itkLevelSetNodeF2
        """
        _itkLevelSetNodePython.itkLevelSetNodeF2_swiginit(self, _itkLevelSetNodePython.new_itkLevelSetNodeF2(*args))
    __swig_destroy__ = _itkLevelSetNodePython.delete_itkLevelSetNodeF2
itkLevelSetNodeF2.__gt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2___gt__, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.__lt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2___lt__, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.__le__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2___le__, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.__ge__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2___ge__, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.GetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2_GetValue, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.SetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2_SetValue, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.GetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2_GetIndex, None, itkLevelSetNodeF2)
itkLevelSetNodeF2.SetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF2_SetIndex, None, itkLevelSetNodeF2)
itkLevelSetNodeF2_swigregister = _itkLevelSetNodePython.itkLevelSetNodeF2_swigregister
itkLevelSetNodeF2_swigregister(itkLevelSetNodeF2)

class itkLevelSetNodeF3(object):
    """Proxy of C++ itkLevelSetNodeF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __gt__(self, node: 'itkLevelSetNodeF3') -> "bool":
        """__gt__(itkLevelSetNodeF3 self, itkLevelSetNodeF3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF3___gt__(self, node)


    def __lt__(self, node: 'itkLevelSetNodeF3') -> "bool":
        """__lt__(itkLevelSetNodeF3 self, itkLevelSetNodeF3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF3___lt__(self, node)


    def __le__(self, node: 'itkLevelSetNodeF3') -> "bool":
        """__le__(itkLevelSetNodeF3 self, itkLevelSetNodeF3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF3___le__(self, node)


    def __ge__(self, node: 'itkLevelSetNodeF3') -> "bool":
        """__ge__(itkLevelSetNodeF3 self, itkLevelSetNodeF3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeF3___ge__(self, node)


    def GetValue(self, *args) -> "float const &":
        """
        GetValue(itkLevelSetNodeF3 self) -> float
        GetValue(itkLevelSetNodeF3 self) -> float const &
        """
        return _itkLevelSetNodePython.itkLevelSetNodeF3_GetValue(self, *args)


    def SetValue(self, input: 'float const &') -> "void":
        """SetValue(itkLevelSetNodeF3 self, float const & input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeF3_SetValue(self, input)


    def GetIndex(self, *args) -> "itkIndex3 const &":
        """
        GetIndex(itkLevelSetNodeF3 self) -> itkIndex3
        GetIndex(itkLevelSetNodeF3 self) -> itkIndex3
        """
        return _itkLevelSetNodePython.itkLevelSetNodeF3_GetIndex(self, *args)


    def SetIndex(self, input: 'itkIndex3') -> "void":
        """SetIndex(itkLevelSetNodeF3 self, itkIndex3 input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeF3_SetIndex(self, input)


    def __init__(self, *args):
        """
        __init__(itkLevelSetNodeF3 self) -> itkLevelSetNodeF3
        __init__(itkLevelSetNodeF3 self, itkLevelSetNodeF3 node) -> itkLevelSetNodeF3
        """
        _itkLevelSetNodePython.itkLevelSetNodeF3_swiginit(self, _itkLevelSetNodePython.new_itkLevelSetNodeF3(*args))
    __swig_destroy__ = _itkLevelSetNodePython.delete_itkLevelSetNodeF3
itkLevelSetNodeF3.__gt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3___gt__, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.__lt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3___lt__, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.__le__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3___le__, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.__ge__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3___ge__, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.GetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3_GetValue, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.SetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3_SetValue, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.GetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3_GetIndex, None, itkLevelSetNodeF3)
itkLevelSetNodeF3.SetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeF3_SetIndex, None, itkLevelSetNodeF3)
itkLevelSetNodeF3_swigregister = _itkLevelSetNodePython.itkLevelSetNodeF3_swigregister
itkLevelSetNodeF3_swigregister(itkLevelSetNodeF3)

class itkLevelSetNodeSS2(object):
    """Proxy of C++ itkLevelSetNodeSS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __gt__(self, node: 'itkLevelSetNodeSS2') -> "bool":
        """__gt__(itkLevelSetNodeSS2 self, itkLevelSetNodeSS2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS2___gt__(self, node)


    def __lt__(self, node: 'itkLevelSetNodeSS2') -> "bool":
        """__lt__(itkLevelSetNodeSS2 self, itkLevelSetNodeSS2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS2___lt__(self, node)


    def __le__(self, node: 'itkLevelSetNodeSS2') -> "bool":
        """__le__(itkLevelSetNodeSS2 self, itkLevelSetNodeSS2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS2___le__(self, node)


    def __ge__(self, node: 'itkLevelSetNodeSS2') -> "bool":
        """__ge__(itkLevelSetNodeSS2 self, itkLevelSetNodeSS2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS2___ge__(self, node)


    def GetValue(self, *args) -> "short const &":
        """
        GetValue(itkLevelSetNodeSS2 self) -> short
        GetValue(itkLevelSetNodeSS2 self) -> short const &
        """
        return _itkLevelSetNodePython.itkLevelSetNodeSS2_GetValue(self, *args)


    def SetValue(self, input: 'short const &') -> "void":
        """SetValue(itkLevelSetNodeSS2 self, short const & input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS2_SetValue(self, input)


    def GetIndex(self, *args) -> "itkIndex2 const &":
        """
        GetIndex(itkLevelSetNodeSS2 self) -> itkIndex2
        GetIndex(itkLevelSetNodeSS2 self) -> itkIndex2
        """
        return _itkLevelSetNodePython.itkLevelSetNodeSS2_GetIndex(self, *args)


    def SetIndex(self, input: 'itkIndex2') -> "void":
        """SetIndex(itkLevelSetNodeSS2 self, itkIndex2 input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS2_SetIndex(self, input)


    def __init__(self, *args):
        """
        __init__(itkLevelSetNodeSS2 self) -> itkLevelSetNodeSS2
        __init__(itkLevelSetNodeSS2 self, itkLevelSetNodeSS2 node) -> itkLevelSetNodeSS2
        """
        _itkLevelSetNodePython.itkLevelSetNodeSS2_swiginit(self, _itkLevelSetNodePython.new_itkLevelSetNodeSS2(*args))
    __swig_destroy__ = _itkLevelSetNodePython.delete_itkLevelSetNodeSS2
itkLevelSetNodeSS2.__gt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2___gt__, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.__lt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2___lt__, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.__le__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2___le__, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.__ge__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2___ge__, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.GetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2_GetValue, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.SetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2_SetValue, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.GetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2_GetIndex, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2.SetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS2_SetIndex, None, itkLevelSetNodeSS2)
itkLevelSetNodeSS2_swigregister = _itkLevelSetNodePython.itkLevelSetNodeSS2_swigregister
itkLevelSetNodeSS2_swigregister(itkLevelSetNodeSS2)

class itkLevelSetNodeSS3(object):
    """Proxy of C++ itkLevelSetNodeSS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __gt__(self, node: 'itkLevelSetNodeSS3') -> "bool":
        """__gt__(itkLevelSetNodeSS3 self, itkLevelSetNodeSS3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS3___gt__(self, node)


    def __lt__(self, node: 'itkLevelSetNodeSS3') -> "bool":
        """__lt__(itkLevelSetNodeSS3 self, itkLevelSetNodeSS3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS3___lt__(self, node)


    def __le__(self, node: 'itkLevelSetNodeSS3') -> "bool":
        """__le__(itkLevelSetNodeSS3 self, itkLevelSetNodeSS3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS3___le__(self, node)


    def __ge__(self, node: 'itkLevelSetNodeSS3') -> "bool":
        """__ge__(itkLevelSetNodeSS3 self, itkLevelSetNodeSS3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS3___ge__(self, node)


    def GetValue(self, *args) -> "short const &":
        """
        GetValue(itkLevelSetNodeSS3 self) -> short
        GetValue(itkLevelSetNodeSS3 self) -> short const &
        """
        return _itkLevelSetNodePython.itkLevelSetNodeSS3_GetValue(self, *args)


    def SetValue(self, input: 'short const &') -> "void":
        """SetValue(itkLevelSetNodeSS3 self, short const & input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS3_SetValue(self, input)


    def GetIndex(self, *args) -> "itkIndex3 const &":
        """
        GetIndex(itkLevelSetNodeSS3 self) -> itkIndex3
        GetIndex(itkLevelSetNodeSS3 self) -> itkIndex3
        """
        return _itkLevelSetNodePython.itkLevelSetNodeSS3_GetIndex(self, *args)


    def SetIndex(self, input: 'itkIndex3') -> "void":
        """SetIndex(itkLevelSetNodeSS3 self, itkIndex3 input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeSS3_SetIndex(self, input)


    def __init__(self, *args):
        """
        __init__(itkLevelSetNodeSS3 self) -> itkLevelSetNodeSS3
        __init__(itkLevelSetNodeSS3 self, itkLevelSetNodeSS3 node) -> itkLevelSetNodeSS3
        """
        _itkLevelSetNodePython.itkLevelSetNodeSS3_swiginit(self, _itkLevelSetNodePython.new_itkLevelSetNodeSS3(*args))
    __swig_destroy__ = _itkLevelSetNodePython.delete_itkLevelSetNodeSS3
itkLevelSetNodeSS3.__gt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3___gt__, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.__lt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3___lt__, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.__le__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3___le__, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.__ge__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3___ge__, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.GetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3_GetValue, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.SetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3_SetValue, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.GetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3_GetIndex, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3.SetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeSS3_SetIndex, None, itkLevelSetNodeSS3)
itkLevelSetNodeSS3_swigregister = _itkLevelSetNodePython.itkLevelSetNodeSS3_swigregister
itkLevelSetNodeSS3_swigregister(itkLevelSetNodeSS3)

class itkLevelSetNodeUC2(object):
    """Proxy of C++ itkLevelSetNodeUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __gt__(self, node: 'itkLevelSetNodeUC2') -> "bool":
        """__gt__(itkLevelSetNodeUC2 self, itkLevelSetNodeUC2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC2___gt__(self, node)


    def __lt__(self, node: 'itkLevelSetNodeUC2') -> "bool":
        """__lt__(itkLevelSetNodeUC2 self, itkLevelSetNodeUC2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC2___lt__(self, node)


    def __le__(self, node: 'itkLevelSetNodeUC2') -> "bool":
        """__le__(itkLevelSetNodeUC2 self, itkLevelSetNodeUC2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC2___le__(self, node)


    def __ge__(self, node: 'itkLevelSetNodeUC2') -> "bool":
        """__ge__(itkLevelSetNodeUC2 self, itkLevelSetNodeUC2 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC2___ge__(self, node)


    def GetValue(self, *args) -> "unsigned char const &":
        """
        GetValue(itkLevelSetNodeUC2 self) -> unsigned char
        GetValue(itkLevelSetNodeUC2 self) -> unsigned char const &
        """
        return _itkLevelSetNodePython.itkLevelSetNodeUC2_GetValue(self, *args)


    def SetValue(self, input: 'unsigned char const &') -> "void":
        """SetValue(itkLevelSetNodeUC2 self, unsigned char const & input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC2_SetValue(self, input)


    def GetIndex(self, *args) -> "itkIndex2 const &":
        """
        GetIndex(itkLevelSetNodeUC2 self) -> itkIndex2
        GetIndex(itkLevelSetNodeUC2 self) -> itkIndex2
        """
        return _itkLevelSetNodePython.itkLevelSetNodeUC2_GetIndex(self, *args)


    def SetIndex(self, input: 'itkIndex2') -> "void":
        """SetIndex(itkLevelSetNodeUC2 self, itkIndex2 input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC2_SetIndex(self, input)


    def __init__(self, *args):
        """
        __init__(itkLevelSetNodeUC2 self) -> itkLevelSetNodeUC2
        __init__(itkLevelSetNodeUC2 self, itkLevelSetNodeUC2 node) -> itkLevelSetNodeUC2
        """
        _itkLevelSetNodePython.itkLevelSetNodeUC2_swiginit(self, _itkLevelSetNodePython.new_itkLevelSetNodeUC2(*args))
    __swig_destroy__ = _itkLevelSetNodePython.delete_itkLevelSetNodeUC2
itkLevelSetNodeUC2.__gt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2___gt__, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.__lt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2___lt__, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.__le__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2___le__, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.__ge__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2___ge__, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.GetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2_GetValue, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.SetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2_SetValue, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.GetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2_GetIndex, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2.SetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC2_SetIndex, None, itkLevelSetNodeUC2)
itkLevelSetNodeUC2_swigregister = _itkLevelSetNodePython.itkLevelSetNodeUC2_swigregister
itkLevelSetNodeUC2_swigregister(itkLevelSetNodeUC2)

class itkLevelSetNodeUC3(object):
    """Proxy of C++ itkLevelSetNodeUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __gt__(self, node: 'itkLevelSetNodeUC3') -> "bool":
        """__gt__(itkLevelSetNodeUC3 self, itkLevelSetNodeUC3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC3___gt__(self, node)


    def __lt__(self, node: 'itkLevelSetNodeUC3') -> "bool":
        """__lt__(itkLevelSetNodeUC3 self, itkLevelSetNodeUC3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC3___lt__(self, node)


    def __le__(self, node: 'itkLevelSetNodeUC3') -> "bool":
        """__le__(itkLevelSetNodeUC3 self, itkLevelSetNodeUC3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC3___le__(self, node)


    def __ge__(self, node: 'itkLevelSetNodeUC3') -> "bool":
        """__ge__(itkLevelSetNodeUC3 self, itkLevelSetNodeUC3 node) -> bool"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC3___ge__(self, node)


    def GetValue(self, *args) -> "unsigned char const &":
        """
        GetValue(itkLevelSetNodeUC3 self) -> unsigned char
        GetValue(itkLevelSetNodeUC3 self) -> unsigned char const &
        """
        return _itkLevelSetNodePython.itkLevelSetNodeUC3_GetValue(self, *args)


    def SetValue(self, input: 'unsigned char const &') -> "void":
        """SetValue(itkLevelSetNodeUC3 self, unsigned char const & input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC3_SetValue(self, input)


    def GetIndex(self, *args) -> "itkIndex3 const &":
        """
        GetIndex(itkLevelSetNodeUC3 self) -> itkIndex3
        GetIndex(itkLevelSetNodeUC3 self) -> itkIndex3
        """
        return _itkLevelSetNodePython.itkLevelSetNodeUC3_GetIndex(self, *args)


    def SetIndex(self, input: 'itkIndex3') -> "void":
        """SetIndex(itkLevelSetNodeUC3 self, itkIndex3 input)"""
        return _itkLevelSetNodePython.itkLevelSetNodeUC3_SetIndex(self, input)


    def __init__(self, *args):
        """
        __init__(itkLevelSetNodeUC3 self) -> itkLevelSetNodeUC3
        __init__(itkLevelSetNodeUC3 self, itkLevelSetNodeUC3 node) -> itkLevelSetNodeUC3
        """
        _itkLevelSetNodePython.itkLevelSetNodeUC3_swiginit(self, _itkLevelSetNodePython.new_itkLevelSetNodeUC3(*args))
    __swig_destroy__ = _itkLevelSetNodePython.delete_itkLevelSetNodeUC3
itkLevelSetNodeUC3.__gt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3___gt__, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.__lt__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3___lt__, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.__le__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3___le__, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.__ge__ = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3___ge__, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.GetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3_GetValue, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.SetValue = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3_SetValue, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.GetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3_GetIndex, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3.SetIndex = new_instancemethod(_itkLevelSetNodePython.itkLevelSetNodeUC3_SetIndex, None, itkLevelSetNodeUC3)
itkLevelSetNodeUC3_swigregister = _itkLevelSetNodePython.itkLevelSetNodeUC3_swigregister
itkLevelSetNodeUC3_swigregister(itkLevelSetNodeUC3)



