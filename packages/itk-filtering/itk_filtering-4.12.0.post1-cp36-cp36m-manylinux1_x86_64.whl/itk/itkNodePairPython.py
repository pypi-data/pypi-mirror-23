# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNodePairPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNodePairPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNodePairPython')
    _itkNodePairPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNodePairPython', [dirname(__file__)])
        except ImportError:
            import _itkNodePairPython
            return _itkNodePairPython
        try:
            _mod = imp.load_module('_itkNodePairPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNodePairPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNodePairPython
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
class itkNodePairI2F(object):
    """Proxy of C++ itkNodePairI2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkNodePairI2F self) -> itkNodePairI2F
        __init__(itkNodePairI2F self, itkIndex2 iNode, float const & iValue) -> itkNodePairI2F
        __init__(itkNodePairI2F self, itkNodePairI2F iPair) -> itkNodePairI2F
        """
        _itkNodePairPython.itkNodePairI2F_swiginit(self, _itkNodePairPython.new_itkNodePairI2F(*args))

    def SetValue(self, iValue: 'float const &') -> "void":
        """SetValue(itkNodePairI2F self, float const & iValue)"""
        return _itkNodePairPython.itkNodePairI2F_SetValue(self, iValue)


    def GetValue(self, *args) -> "float &":
        """
        GetValue(itkNodePairI2F self) -> float const
        GetValue(itkNodePairI2F self) -> float &
        """
        return _itkNodePairPython.itkNodePairI2F_GetValue(self, *args)


    def SetNode(self, iNode: 'itkIndex2') -> "void":
        """SetNode(itkNodePairI2F self, itkIndex2 iNode)"""
        return _itkNodePairPython.itkNodePairI2F_SetNode(self, iNode)


    def GetNode(self, *args) -> "itkIndex2 &":
        """
        GetNode(itkNodePairI2F self) -> itkIndex2
        GetNode(itkNodePairI2F self) -> itkIndex2
        """
        return _itkNodePairPython.itkNodePairI2F_GetNode(self, *args)


    def __lt__(self, iRight: 'itkNodePairI2F') -> "bool":
        """__lt__(itkNodePairI2F self, itkNodePairI2F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2F___lt__(self, iRight)


    def __gt__(self, iRight: 'itkNodePairI2F') -> "bool":
        """__gt__(itkNodePairI2F self, itkNodePairI2F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2F___gt__(self, iRight)


    def __le__(self, iRight: 'itkNodePairI2F') -> "bool":
        """__le__(itkNodePairI2F self, itkNodePairI2F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2F___le__(self, iRight)


    def __ge__(self, iRight: 'itkNodePairI2F') -> "bool":
        """__ge__(itkNodePairI2F self, itkNodePairI2F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2F___ge__(self, iRight)

    __swig_destroy__ = _itkNodePairPython.delete_itkNodePairI2F
itkNodePairI2F.SetValue = new_instancemethod(_itkNodePairPython.itkNodePairI2F_SetValue, None, itkNodePairI2F)
itkNodePairI2F.GetValue = new_instancemethod(_itkNodePairPython.itkNodePairI2F_GetValue, None, itkNodePairI2F)
itkNodePairI2F.SetNode = new_instancemethod(_itkNodePairPython.itkNodePairI2F_SetNode, None, itkNodePairI2F)
itkNodePairI2F.GetNode = new_instancemethod(_itkNodePairPython.itkNodePairI2F_GetNode, None, itkNodePairI2F)
itkNodePairI2F.__lt__ = new_instancemethod(_itkNodePairPython.itkNodePairI2F___lt__, None, itkNodePairI2F)
itkNodePairI2F.__gt__ = new_instancemethod(_itkNodePairPython.itkNodePairI2F___gt__, None, itkNodePairI2F)
itkNodePairI2F.__le__ = new_instancemethod(_itkNodePairPython.itkNodePairI2F___le__, None, itkNodePairI2F)
itkNodePairI2F.__ge__ = new_instancemethod(_itkNodePairPython.itkNodePairI2F___ge__, None, itkNodePairI2F)
itkNodePairI2F_swigregister = _itkNodePairPython.itkNodePairI2F_swigregister
itkNodePairI2F_swigregister(itkNodePairI2F)

class itkNodePairI2SS(object):
    """Proxy of C++ itkNodePairI2SS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkNodePairI2SS self) -> itkNodePairI2SS
        __init__(itkNodePairI2SS self, itkIndex2 iNode, short const & iValue) -> itkNodePairI2SS
        __init__(itkNodePairI2SS self, itkNodePairI2SS iPair) -> itkNodePairI2SS
        """
        _itkNodePairPython.itkNodePairI2SS_swiginit(self, _itkNodePairPython.new_itkNodePairI2SS(*args))

    def SetValue(self, iValue: 'short const &') -> "void":
        """SetValue(itkNodePairI2SS self, short const & iValue)"""
        return _itkNodePairPython.itkNodePairI2SS_SetValue(self, iValue)


    def GetValue(self, *args) -> "short &":
        """
        GetValue(itkNodePairI2SS self) -> short const
        GetValue(itkNodePairI2SS self) -> short &
        """
        return _itkNodePairPython.itkNodePairI2SS_GetValue(self, *args)


    def SetNode(self, iNode: 'itkIndex2') -> "void":
        """SetNode(itkNodePairI2SS self, itkIndex2 iNode)"""
        return _itkNodePairPython.itkNodePairI2SS_SetNode(self, iNode)


    def GetNode(self, *args) -> "itkIndex2 &":
        """
        GetNode(itkNodePairI2SS self) -> itkIndex2
        GetNode(itkNodePairI2SS self) -> itkIndex2
        """
        return _itkNodePairPython.itkNodePairI2SS_GetNode(self, *args)


    def __lt__(self, iRight: 'itkNodePairI2SS') -> "bool":
        """__lt__(itkNodePairI2SS self, itkNodePairI2SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2SS___lt__(self, iRight)


    def __gt__(self, iRight: 'itkNodePairI2SS') -> "bool":
        """__gt__(itkNodePairI2SS self, itkNodePairI2SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2SS___gt__(self, iRight)


    def __le__(self, iRight: 'itkNodePairI2SS') -> "bool":
        """__le__(itkNodePairI2SS self, itkNodePairI2SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2SS___le__(self, iRight)


    def __ge__(self, iRight: 'itkNodePairI2SS') -> "bool":
        """__ge__(itkNodePairI2SS self, itkNodePairI2SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2SS___ge__(self, iRight)

    __swig_destroy__ = _itkNodePairPython.delete_itkNodePairI2SS
itkNodePairI2SS.SetValue = new_instancemethod(_itkNodePairPython.itkNodePairI2SS_SetValue, None, itkNodePairI2SS)
itkNodePairI2SS.GetValue = new_instancemethod(_itkNodePairPython.itkNodePairI2SS_GetValue, None, itkNodePairI2SS)
itkNodePairI2SS.SetNode = new_instancemethod(_itkNodePairPython.itkNodePairI2SS_SetNode, None, itkNodePairI2SS)
itkNodePairI2SS.GetNode = new_instancemethod(_itkNodePairPython.itkNodePairI2SS_GetNode, None, itkNodePairI2SS)
itkNodePairI2SS.__lt__ = new_instancemethod(_itkNodePairPython.itkNodePairI2SS___lt__, None, itkNodePairI2SS)
itkNodePairI2SS.__gt__ = new_instancemethod(_itkNodePairPython.itkNodePairI2SS___gt__, None, itkNodePairI2SS)
itkNodePairI2SS.__le__ = new_instancemethod(_itkNodePairPython.itkNodePairI2SS___le__, None, itkNodePairI2SS)
itkNodePairI2SS.__ge__ = new_instancemethod(_itkNodePairPython.itkNodePairI2SS___ge__, None, itkNodePairI2SS)
itkNodePairI2SS_swigregister = _itkNodePairPython.itkNodePairI2SS_swigregister
itkNodePairI2SS_swigregister(itkNodePairI2SS)

class itkNodePairI2UC(object):
    """Proxy of C++ itkNodePairI2UC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkNodePairI2UC self) -> itkNodePairI2UC
        __init__(itkNodePairI2UC self, itkIndex2 iNode, unsigned char const & iValue) -> itkNodePairI2UC
        __init__(itkNodePairI2UC self, itkNodePairI2UC iPair) -> itkNodePairI2UC
        """
        _itkNodePairPython.itkNodePairI2UC_swiginit(self, _itkNodePairPython.new_itkNodePairI2UC(*args))

    def SetValue(self, iValue: 'unsigned char const &') -> "void":
        """SetValue(itkNodePairI2UC self, unsigned char const & iValue)"""
        return _itkNodePairPython.itkNodePairI2UC_SetValue(self, iValue)


    def GetValue(self, *args) -> "unsigned char &":
        """
        GetValue(itkNodePairI2UC self) -> unsigned char const
        GetValue(itkNodePairI2UC self) -> unsigned char &
        """
        return _itkNodePairPython.itkNodePairI2UC_GetValue(self, *args)


    def SetNode(self, iNode: 'itkIndex2') -> "void":
        """SetNode(itkNodePairI2UC self, itkIndex2 iNode)"""
        return _itkNodePairPython.itkNodePairI2UC_SetNode(self, iNode)


    def GetNode(self, *args) -> "itkIndex2 &":
        """
        GetNode(itkNodePairI2UC self) -> itkIndex2
        GetNode(itkNodePairI2UC self) -> itkIndex2
        """
        return _itkNodePairPython.itkNodePairI2UC_GetNode(self, *args)


    def __lt__(self, iRight: 'itkNodePairI2UC') -> "bool":
        """__lt__(itkNodePairI2UC self, itkNodePairI2UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2UC___lt__(self, iRight)


    def __gt__(self, iRight: 'itkNodePairI2UC') -> "bool":
        """__gt__(itkNodePairI2UC self, itkNodePairI2UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2UC___gt__(self, iRight)


    def __le__(self, iRight: 'itkNodePairI2UC') -> "bool":
        """__le__(itkNodePairI2UC self, itkNodePairI2UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2UC___le__(self, iRight)


    def __ge__(self, iRight: 'itkNodePairI2UC') -> "bool":
        """__ge__(itkNodePairI2UC self, itkNodePairI2UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI2UC___ge__(self, iRight)

    __swig_destroy__ = _itkNodePairPython.delete_itkNodePairI2UC
itkNodePairI2UC.SetValue = new_instancemethod(_itkNodePairPython.itkNodePairI2UC_SetValue, None, itkNodePairI2UC)
itkNodePairI2UC.GetValue = new_instancemethod(_itkNodePairPython.itkNodePairI2UC_GetValue, None, itkNodePairI2UC)
itkNodePairI2UC.SetNode = new_instancemethod(_itkNodePairPython.itkNodePairI2UC_SetNode, None, itkNodePairI2UC)
itkNodePairI2UC.GetNode = new_instancemethod(_itkNodePairPython.itkNodePairI2UC_GetNode, None, itkNodePairI2UC)
itkNodePairI2UC.__lt__ = new_instancemethod(_itkNodePairPython.itkNodePairI2UC___lt__, None, itkNodePairI2UC)
itkNodePairI2UC.__gt__ = new_instancemethod(_itkNodePairPython.itkNodePairI2UC___gt__, None, itkNodePairI2UC)
itkNodePairI2UC.__le__ = new_instancemethod(_itkNodePairPython.itkNodePairI2UC___le__, None, itkNodePairI2UC)
itkNodePairI2UC.__ge__ = new_instancemethod(_itkNodePairPython.itkNodePairI2UC___ge__, None, itkNodePairI2UC)
itkNodePairI2UC_swigregister = _itkNodePairPython.itkNodePairI2UC_swigregister
itkNodePairI2UC_swigregister(itkNodePairI2UC)

class itkNodePairI3F(object):
    """Proxy of C++ itkNodePairI3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkNodePairI3F self) -> itkNodePairI3F
        __init__(itkNodePairI3F self, itkIndex3 iNode, float const & iValue) -> itkNodePairI3F
        __init__(itkNodePairI3F self, itkNodePairI3F iPair) -> itkNodePairI3F
        """
        _itkNodePairPython.itkNodePairI3F_swiginit(self, _itkNodePairPython.new_itkNodePairI3F(*args))

    def SetValue(self, iValue: 'float const &') -> "void":
        """SetValue(itkNodePairI3F self, float const & iValue)"""
        return _itkNodePairPython.itkNodePairI3F_SetValue(self, iValue)


    def GetValue(self, *args) -> "float &":
        """
        GetValue(itkNodePairI3F self) -> float const
        GetValue(itkNodePairI3F self) -> float &
        """
        return _itkNodePairPython.itkNodePairI3F_GetValue(self, *args)


    def SetNode(self, iNode: 'itkIndex3') -> "void":
        """SetNode(itkNodePairI3F self, itkIndex3 iNode)"""
        return _itkNodePairPython.itkNodePairI3F_SetNode(self, iNode)


    def GetNode(self, *args) -> "itkIndex3 &":
        """
        GetNode(itkNodePairI3F self) -> itkIndex3
        GetNode(itkNodePairI3F self) -> itkIndex3
        """
        return _itkNodePairPython.itkNodePairI3F_GetNode(self, *args)


    def __lt__(self, iRight: 'itkNodePairI3F') -> "bool":
        """__lt__(itkNodePairI3F self, itkNodePairI3F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3F___lt__(self, iRight)


    def __gt__(self, iRight: 'itkNodePairI3F') -> "bool":
        """__gt__(itkNodePairI3F self, itkNodePairI3F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3F___gt__(self, iRight)


    def __le__(self, iRight: 'itkNodePairI3F') -> "bool":
        """__le__(itkNodePairI3F self, itkNodePairI3F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3F___le__(self, iRight)


    def __ge__(self, iRight: 'itkNodePairI3F') -> "bool":
        """__ge__(itkNodePairI3F self, itkNodePairI3F iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3F___ge__(self, iRight)

    __swig_destroy__ = _itkNodePairPython.delete_itkNodePairI3F
itkNodePairI3F.SetValue = new_instancemethod(_itkNodePairPython.itkNodePairI3F_SetValue, None, itkNodePairI3F)
itkNodePairI3F.GetValue = new_instancemethod(_itkNodePairPython.itkNodePairI3F_GetValue, None, itkNodePairI3F)
itkNodePairI3F.SetNode = new_instancemethod(_itkNodePairPython.itkNodePairI3F_SetNode, None, itkNodePairI3F)
itkNodePairI3F.GetNode = new_instancemethod(_itkNodePairPython.itkNodePairI3F_GetNode, None, itkNodePairI3F)
itkNodePairI3F.__lt__ = new_instancemethod(_itkNodePairPython.itkNodePairI3F___lt__, None, itkNodePairI3F)
itkNodePairI3F.__gt__ = new_instancemethod(_itkNodePairPython.itkNodePairI3F___gt__, None, itkNodePairI3F)
itkNodePairI3F.__le__ = new_instancemethod(_itkNodePairPython.itkNodePairI3F___le__, None, itkNodePairI3F)
itkNodePairI3F.__ge__ = new_instancemethod(_itkNodePairPython.itkNodePairI3F___ge__, None, itkNodePairI3F)
itkNodePairI3F_swigregister = _itkNodePairPython.itkNodePairI3F_swigregister
itkNodePairI3F_swigregister(itkNodePairI3F)

class itkNodePairI3SS(object):
    """Proxy of C++ itkNodePairI3SS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkNodePairI3SS self) -> itkNodePairI3SS
        __init__(itkNodePairI3SS self, itkIndex3 iNode, short const & iValue) -> itkNodePairI3SS
        __init__(itkNodePairI3SS self, itkNodePairI3SS iPair) -> itkNodePairI3SS
        """
        _itkNodePairPython.itkNodePairI3SS_swiginit(self, _itkNodePairPython.new_itkNodePairI3SS(*args))

    def SetValue(self, iValue: 'short const &') -> "void":
        """SetValue(itkNodePairI3SS self, short const & iValue)"""
        return _itkNodePairPython.itkNodePairI3SS_SetValue(self, iValue)


    def GetValue(self, *args) -> "short &":
        """
        GetValue(itkNodePairI3SS self) -> short const
        GetValue(itkNodePairI3SS self) -> short &
        """
        return _itkNodePairPython.itkNodePairI3SS_GetValue(self, *args)


    def SetNode(self, iNode: 'itkIndex3') -> "void":
        """SetNode(itkNodePairI3SS self, itkIndex3 iNode)"""
        return _itkNodePairPython.itkNodePairI3SS_SetNode(self, iNode)


    def GetNode(self, *args) -> "itkIndex3 &":
        """
        GetNode(itkNodePairI3SS self) -> itkIndex3
        GetNode(itkNodePairI3SS self) -> itkIndex3
        """
        return _itkNodePairPython.itkNodePairI3SS_GetNode(self, *args)


    def __lt__(self, iRight: 'itkNodePairI3SS') -> "bool":
        """__lt__(itkNodePairI3SS self, itkNodePairI3SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3SS___lt__(self, iRight)


    def __gt__(self, iRight: 'itkNodePairI3SS') -> "bool":
        """__gt__(itkNodePairI3SS self, itkNodePairI3SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3SS___gt__(self, iRight)


    def __le__(self, iRight: 'itkNodePairI3SS') -> "bool":
        """__le__(itkNodePairI3SS self, itkNodePairI3SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3SS___le__(self, iRight)


    def __ge__(self, iRight: 'itkNodePairI3SS') -> "bool":
        """__ge__(itkNodePairI3SS self, itkNodePairI3SS iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3SS___ge__(self, iRight)

    __swig_destroy__ = _itkNodePairPython.delete_itkNodePairI3SS
itkNodePairI3SS.SetValue = new_instancemethod(_itkNodePairPython.itkNodePairI3SS_SetValue, None, itkNodePairI3SS)
itkNodePairI3SS.GetValue = new_instancemethod(_itkNodePairPython.itkNodePairI3SS_GetValue, None, itkNodePairI3SS)
itkNodePairI3SS.SetNode = new_instancemethod(_itkNodePairPython.itkNodePairI3SS_SetNode, None, itkNodePairI3SS)
itkNodePairI3SS.GetNode = new_instancemethod(_itkNodePairPython.itkNodePairI3SS_GetNode, None, itkNodePairI3SS)
itkNodePairI3SS.__lt__ = new_instancemethod(_itkNodePairPython.itkNodePairI3SS___lt__, None, itkNodePairI3SS)
itkNodePairI3SS.__gt__ = new_instancemethod(_itkNodePairPython.itkNodePairI3SS___gt__, None, itkNodePairI3SS)
itkNodePairI3SS.__le__ = new_instancemethod(_itkNodePairPython.itkNodePairI3SS___le__, None, itkNodePairI3SS)
itkNodePairI3SS.__ge__ = new_instancemethod(_itkNodePairPython.itkNodePairI3SS___ge__, None, itkNodePairI3SS)
itkNodePairI3SS_swigregister = _itkNodePairPython.itkNodePairI3SS_swigregister
itkNodePairI3SS_swigregister(itkNodePairI3SS)

class itkNodePairI3UC(object):
    """Proxy of C++ itkNodePairI3UC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkNodePairI3UC self) -> itkNodePairI3UC
        __init__(itkNodePairI3UC self, itkIndex3 iNode, unsigned char const & iValue) -> itkNodePairI3UC
        __init__(itkNodePairI3UC self, itkNodePairI3UC iPair) -> itkNodePairI3UC
        """
        _itkNodePairPython.itkNodePairI3UC_swiginit(self, _itkNodePairPython.new_itkNodePairI3UC(*args))

    def SetValue(self, iValue: 'unsigned char const &') -> "void":
        """SetValue(itkNodePairI3UC self, unsigned char const & iValue)"""
        return _itkNodePairPython.itkNodePairI3UC_SetValue(self, iValue)


    def GetValue(self, *args) -> "unsigned char &":
        """
        GetValue(itkNodePairI3UC self) -> unsigned char const
        GetValue(itkNodePairI3UC self) -> unsigned char &
        """
        return _itkNodePairPython.itkNodePairI3UC_GetValue(self, *args)


    def SetNode(self, iNode: 'itkIndex3') -> "void":
        """SetNode(itkNodePairI3UC self, itkIndex3 iNode)"""
        return _itkNodePairPython.itkNodePairI3UC_SetNode(self, iNode)


    def GetNode(self, *args) -> "itkIndex3 &":
        """
        GetNode(itkNodePairI3UC self) -> itkIndex3
        GetNode(itkNodePairI3UC self) -> itkIndex3
        """
        return _itkNodePairPython.itkNodePairI3UC_GetNode(self, *args)


    def __lt__(self, iRight: 'itkNodePairI3UC') -> "bool":
        """__lt__(itkNodePairI3UC self, itkNodePairI3UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3UC___lt__(self, iRight)


    def __gt__(self, iRight: 'itkNodePairI3UC') -> "bool":
        """__gt__(itkNodePairI3UC self, itkNodePairI3UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3UC___gt__(self, iRight)


    def __le__(self, iRight: 'itkNodePairI3UC') -> "bool":
        """__le__(itkNodePairI3UC self, itkNodePairI3UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3UC___le__(self, iRight)


    def __ge__(self, iRight: 'itkNodePairI3UC') -> "bool":
        """__ge__(itkNodePairI3UC self, itkNodePairI3UC iRight) -> bool"""
        return _itkNodePairPython.itkNodePairI3UC___ge__(self, iRight)

    __swig_destroy__ = _itkNodePairPython.delete_itkNodePairI3UC
itkNodePairI3UC.SetValue = new_instancemethod(_itkNodePairPython.itkNodePairI3UC_SetValue, None, itkNodePairI3UC)
itkNodePairI3UC.GetValue = new_instancemethod(_itkNodePairPython.itkNodePairI3UC_GetValue, None, itkNodePairI3UC)
itkNodePairI3UC.SetNode = new_instancemethod(_itkNodePairPython.itkNodePairI3UC_SetNode, None, itkNodePairI3UC)
itkNodePairI3UC.GetNode = new_instancemethod(_itkNodePairPython.itkNodePairI3UC_GetNode, None, itkNodePairI3UC)
itkNodePairI3UC.__lt__ = new_instancemethod(_itkNodePairPython.itkNodePairI3UC___lt__, None, itkNodePairI3UC)
itkNodePairI3UC.__gt__ = new_instancemethod(_itkNodePairPython.itkNodePairI3UC___gt__, None, itkNodePairI3UC)
itkNodePairI3UC.__le__ = new_instancemethod(_itkNodePairPython.itkNodePairI3UC___le__, None, itkNodePairI3UC)
itkNodePairI3UC.__ge__ = new_instancemethod(_itkNodePairPython.itkNodePairI3UC___ge__, None, itkNodePairI3UC)
itkNodePairI3UC_swigregister = _itkNodePairPython.itkNodePairI3UC_swigregister
itkNodePairI3UC_swigregister(itkNodePairI3UC)



