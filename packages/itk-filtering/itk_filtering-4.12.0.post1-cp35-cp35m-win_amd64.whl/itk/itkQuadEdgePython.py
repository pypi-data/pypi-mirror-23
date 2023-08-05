# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkQuadEdgePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkQuadEdgePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkQuadEdgePython')
    _itkQuadEdgePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkQuadEdgePython', [dirname(__file__)])
        except ImportError:
            import _itkQuadEdgePython
            return _itkQuadEdgePython
        try:
            _mod = imp.load_module('_itkQuadEdgePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkQuadEdgePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkQuadEdgePython
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


import pyBasePython
class itkQuadEdge(object):
    """Proxy of C++ itkQuadEdge class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def BeginOnext(self, *args) -> "itk::QuadEdgeMeshConstIterator< itk::QuadEdge >":
        """
        BeginOnext(itkQuadEdge self) -> itk::QuadEdgeMeshIterator< itk::QuadEdge >
        BeginOnext(itkQuadEdge self) -> itk::QuadEdgeMeshConstIterator< itk::QuadEdge >
        """
        return _itkQuadEdgePython.itkQuadEdge_BeginOnext(self, *args)


    def EndOnext(self, *args) -> "itk::QuadEdgeMeshConstIterator< itk::QuadEdge >":
        """
        EndOnext(itkQuadEdge self) -> itk::QuadEdgeMeshIterator< itk::QuadEdge >
        EndOnext(itkQuadEdge self) -> itk::QuadEdgeMeshConstIterator< itk::QuadEdge >
        """
        return _itkQuadEdgePython.itkQuadEdge_EndOnext(self, *args)

    __swig_destroy__ = _itkQuadEdgePython.delete_itkQuadEdge

    def SetOnext(self, onext: 'itkQuadEdge') -> "void":
        """SetOnext(itkQuadEdge self, itkQuadEdge onext)"""
        return _itkQuadEdgePython.itkQuadEdge_SetOnext(self, onext)


    def SetRot(self, rot: 'itkQuadEdge') -> "void":
        """SetRot(itkQuadEdge self, itkQuadEdge rot)"""
        return _itkQuadEdgePython.itkQuadEdge_SetRot(self, rot)


    def GetOnext(self, *args) -> "itkQuadEdge const *":
        """
        GetOnext(itkQuadEdge self) -> itkQuadEdge
        GetOnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetOnext(self, *args)


    def GetRot(self, *args) -> "itkQuadEdge const *":
        """
        GetRot(itkQuadEdge self) -> itkQuadEdge
        GetRot(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetRot(self, *args)


    def Splice(self, b: 'itkQuadEdge') -> "void":
        """Splice(itkQuadEdge self, itkQuadEdge b)"""
        return _itkQuadEdgePython.itkQuadEdge_Splice(self, b)


    def GetSym(self, *args) -> "itkQuadEdge const *":
        """
        GetSym(itkQuadEdge self) -> itkQuadEdge
        GetSym(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetSym(self, *args)


    def GetLnext(self, *args) -> "itkQuadEdge const *":
        """
        GetLnext(itkQuadEdge self) -> itkQuadEdge
        GetLnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetLnext(self, *args)


    def GetRnext(self, *args) -> "itkQuadEdge const *":
        """
        GetRnext(itkQuadEdge self) -> itkQuadEdge
        GetRnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetRnext(self, *args)


    def GetDnext(self, *args) -> "itkQuadEdge const *":
        """
        GetDnext(itkQuadEdge self) -> itkQuadEdge
        GetDnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetDnext(self, *args)


    def GetOprev(self, *args) -> "itkQuadEdge const *":
        """
        GetOprev(itkQuadEdge self) -> itkQuadEdge
        GetOprev(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetOprev(self, *args)


    def GetLprev(self, *args) -> "itkQuadEdge const *":
        """
        GetLprev(itkQuadEdge self) -> itkQuadEdge
        GetLprev(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetLprev(self, *args)


    def GetRprev(self, *args) -> "itkQuadEdge const *":
        """
        GetRprev(itkQuadEdge self) -> itkQuadEdge
        GetRprev(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetRprev(self, *args)


    def GetDprev(self, *args) -> "itkQuadEdge const *":
        """
        GetDprev(itkQuadEdge self) -> itkQuadEdge
        GetDprev(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetDprev(self, *args)


    def GetInvRot(self, *args) -> "itkQuadEdge const *":
        """
        GetInvRot(itkQuadEdge self) -> itkQuadEdge
        GetInvRot(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetInvRot(self, *args)


    def GetInvOnext(self, *args) -> "itkQuadEdge const *":
        """
        GetInvOnext(itkQuadEdge self) -> itkQuadEdge
        GetInvOnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetInvOnext(self, *args)


    def GetInvLnext(self, *args) -> "itkQuadEdge const *":
        """
        GetInvLnext(itkQuadEdge self) -> itkQuadEdge
        GetInvLnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetInvLnext(self, *args)


    def GetInvRnext(self, *args) -> "itkQuadEdge const *":
        """
        GetInvRnext(itkQuadEdge self) -> itkQuadEdge
        GetInvRnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetInvRnext(self, *args)


    def GetInvDnext(self, *args) -> "itkQuadEdge const *":
        """
        GetInvDnext(itkQuadEdge self) -> itkQuadEdge
        GetInvDnext(itkQuadEdge self) -> itkQuadEdge
        """
        return _itkQuadEdgePython.itkQuadEdge_GetInvDnext(self, *args)


    def IsHalfEdge(self) -> "bool":
        """IsHalfEdge(itkQuadEdge self) -> bool"""
        return _itkQuadEdgePython.itkQuadEdge_IsHalfEdge(self)


    def IsIsolated(self) -> "bool":
        """IsIsolated(itkQuadEdge self) -> bool"""
        return _itkQuadEdgePython.itkQuadEdge_IsIsolated(self)


    def IsEdgeInOnextRing(self, testEdge: 'itkQuadEdge') -> "bool":
        """IsEdgeInOnextRing(itkQuadEdge self, itkQuadEdge testEdge) -> bool"""
        return _itkQuadEdgePython.itkQuadEdge_IsEdgeInOnextRing(self, testEdge)


    def IsLnextGivenSizeCyclic(self, size: 'int const') -> "bool":
        """IsLnextGivenSizeCyclic(itkQuadEdge self, int const size) -> bool"""
        return _itkQuadEdgePython.itkQuadEdge_IsLnextGivenSizeCyclic(self, size)


    def GetOrder(self) -> "unsigned int":
        """GetOrder(itkQuadEdge self) -> unsigned int"""
        return _itkQuadEdgePython.itkQuadEdge_GetOrder(self)


    def __init__(self, *args):
        """
        __init__(itkQuadEdge self) -> itkQuadEdge
        __init__(itkQuadEdge self, itkQuadEdge arg0) -> itkQuadEdge
        """
        _itkQuadEdgePython.itkQuadEdge_swiginit(self, _itkQuadEdgePython.new_itkQuadEdge(*args))
itkQuadEdge.BeginOnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_BeginOnext, None, itkQuadEdge)
itkQuadEdge.EndOnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_EndOnext, None, itkQuadEdge)
itkQuadEdge.SetOnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_SetOnext, None, itkQuadEdge)
itkQuadEdge.SetRot = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_SetRot, None, itkQuadEdge)
itkQuadEdge.GetOnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetOnext, None, itkQuadEdge)
itkQuadEdge.GetRot = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetRot, None, itkQuadEdge)
itkQuadEdge.Splice = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_Splice, None, itkQuadEdge)
itkQuadEdge.GetSym = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetSym, None, itkQuadEdge)
itkQuadEdge.GetLnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetLnext, None, itkQuadEdge)
itkQuadEdge.GetRnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetRnext, None, itkQuadEdge)
itkQuadEdge.GetDnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetDnext, None, itkQuadEdge)
itkQuadEdge.GetOprev = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetOprev, None, itkQuadEdge)
itkQuadEdge.GetLprev = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetLprev, None, itkQuadEdge)
itkQuadEdge.GetRprev = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetRprev, None, itkQuadEdge)
itkQuadEdge.GetDprev = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetDprev, None, itkQuadEdge)
itkQuadEdge.GetInvRot = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetInvRot, None, itkQuadEdge)
itkQuadEdge.GetInvOnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetInvOnext, None, itkQuadEdge)
itkQuadEdge.GetInvLnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetInvLnext, None, itkQuadEdge)
itkQuadEdge.GetInvRnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetInvRnext, None, itkQuadEdge)
itkQuadEdge.GetInvDnext = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetInvDnext, None, itkQuadEdge)
itkQuadEdge.IsHalfEdge = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_IsHalfEdge, None, itkQuadEdge)
itkQuadEdge.IsIsolated = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_IsIsolated, None, itkQuadEdge)
itkQuadEdge.IsEdgeInOnextRing = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_IsEdgeInOnextRing, None, itkQuadEdge)
itkQuadEdge.IsLnextGivenSizeCyclic = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_IsLnextGivenSizeCyclic, None, itkQuadEdge)
itkQuadEdge.GetOrder = new_instancemethod(_itkQuadEdgePython.itkQuadEdge_GetOrder, None, itkQuadEdge)
itkQuadEdge_swigregister = _itkQuadEdgePython.itkQuadEdge_swigregister
itkQuadEdge_swigregister(itkQuadEdge)



