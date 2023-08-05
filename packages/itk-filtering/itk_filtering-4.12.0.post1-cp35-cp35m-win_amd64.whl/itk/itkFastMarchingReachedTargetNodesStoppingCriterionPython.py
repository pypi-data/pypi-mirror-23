# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingReachedTargetNodesStoppingCriterionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkFastMarchingReachedTargetNodesStoppingCriterionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkFastMarchingReachedTargetNodesStoppingCriterionPython')
    _itkFastMarchingReachedTargetNodesStoppingCriterionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingReachedTargetNodesStoppingCriterionPython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingReachedTargetNodesStoppingCriterionPython
            return _itkFastMarchingReachedTargetNodesStoppingCriterionPython
        try:
            _mod = imp.load_module('_itkFastMarchingReachedTargetNodesStoppingCriterionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkFastMarchingReachedTargetNodesStoppingCriterionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingReachedTargetNodesStoppingCriterionPython
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
import itkFastMarchingStoppingCriterionBasePython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import itkOffsetPython
import itkSizePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkIndexPython
import itkImageRegionPython
import itkNodePairPython

def itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_New():
  return itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.New()


def itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_New():
  return itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.New()

class itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2):
    """Proxy of C++ itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Pointer":
        """__New_orig__() -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Pointer"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Pointer":
        """Clone(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Pointer"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Clone(self)

    OneTarget = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_OneTarget
    SomeTargets = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SomeTargets
    AllTargets = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_AllTargets

    def SetTargetCondition(self, iCondition: 'itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2::TargetConditionType const &') -> "void":
        """SetTargetCondition(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2::TargetConditionType const & iCondition)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetTargetCondition(self, iCondition)


    def GetTargetCondition(self) -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2::TargetConditionType const &":
        """GetTargetCondition(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2::TargetConditionType const &"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_GetTargetCondition(self)


    def SetTargetOffset(self, _arg: 'float const') -> "void":
        """SetTargetOffset(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self, float const _arg)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetTargetOffset(self, _arg)


    def GetTargetOffset(self) -> "float":
        """GetTargetOffset(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self) -> float"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_GetTargetOffset(self)


    def SetNumberOfTargetsToBeReached(self, iN: 'unsigned long long const &') -> "void":
        """SetNumberOfTargetsToBeReached(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self, unsigned long long const & iN)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetNumberOfTargetsToBeReached(self, iN)


    def SetTargetNodes(self, iNodes: 'std::vector< itkIndex2,std::allocator< itkIndex2 > > const &') -> "void":
        """SetTargetNodes(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self, std::vector< itkIndex2,std::allocator< itkIndex2 > > const & iNodes)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetTargetNodes(self, iNodes)


    def SetCurrentNode(self, iNode: 'itkIndex2') -> "void":
        """SetCurrentNode(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self, itkIndex2 iNode)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetCurrentNode(self, iNode)

    __swig_destroy__ = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.delete_itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 *":
        """GetPointer(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 self) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2

        Create a new object of the class itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.Clone = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Clone, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.SetTargetCondition = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetTargetCondition, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.GetTargetCondition = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_GetTargetCondition, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.SetTargetOffset = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetTargetOffset, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.GetTargetOffset = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_GetTargetOffset, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.SetNumberOfTargetsToBeReached = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetNumberOfTargetsToBeReached, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.SetTargetNodes = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetTargetNodes, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.SetCurrentNode = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_SetCurrentNode, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2.GetPointer = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_GetPointer, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_swigregister = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_swigregister
itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_swigregister(itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2)

def itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2___New_orig__() -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Pointer":
    """itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2___New_orig__() -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_Pointer"""
    return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2___New_orig__()

def itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2 *":
    """itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_cast(itkLightObject obj) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2"""
    return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2_cast(obj)

class itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3):
    """Proxy of C++ itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Pointer":
        """__New_orig__() -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Pointer"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Pointer":
        """Clone(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Pointer"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Clone(self)

    OneTarget = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_OneTarget
    SomeTargets = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SomeTargets
    AllTargets = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_AllTargets

    def SetTargetCondition(self, iCondition: 'itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3::TargetConditionType const &') -> "void":
        """SetTargetCondition(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3::TargetConditionType const & iCondition)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetTargetCondition(self, iCondition)


    def GetTargetCondition(self) -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3::TargetConditionType const &":
        """GetTargetCondition(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3::TargetConditionType const &"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_GetTargetCondition(self)


    def SetTargetOffset(self, _arg: 'float const') -> "void":
        """SetTargetOffset(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self, float const _arg)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetTargetOffset(self, _arg)


    def GetTargetOffset(self) -> "float":
        """GetTargetOffset(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self) -> float"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_GetTargetOffset(self)


    def SetNumberOfTargetsToBeReached(self, iN: 'unsigned long long const &') -> "void":
        """SetNumberOfTargetsToBeReached(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self, unsigned long long const & iN)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetNumberOfTargetsToBeReached(self, iN)


    def SetTargetNodes(self, iNodes: 'std::vector< itkIndex3,std::allocator< itkIndex3 > > const &') -> "void":
        """SetTargetNodes(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self, std::vector< itkIndex3,std::allocator< itkIndex3 > > const & iNodes)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetTargetNodes(self, iNodes)


    def SetCurrentNode(self, iNode: 'itkIndex3') -> "void":
        """SetCurrentNode(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self, itkIndex3 iNode)"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetCurrentNode(self, iNode)

    __swig_destroy__ = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.delete_itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 *":
        """GetPointer(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 self) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3"""
        return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3

        Create a new object of the class itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.Clone = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Clone, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.SetTargetCondition = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetTargetCondition, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.GetTargetCondition = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_GetTargetCondition, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.SetTargetOffset = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetTargetOffset, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.GetTargetOffset = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_GetTargetOffset, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.SetNumberOfTargetsToBeReached = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetNumberOfTargetsToBeReached, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.SetTargetNodes = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetTargetNodes, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.SetCurrentNode = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_SetCurrentNode, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3.GetPointer = new_instancemethod(_itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_GetPointer, None, itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_swigregister = _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_swigregister
itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_swigregister(itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3)

def itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3___New_orig__() -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Pointer":
    """itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3___New_orig__() -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_Pointer"""
    return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3___New_orig__()

def itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3 *":
    """itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_cast(itkLightObject obj) -> itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3"""
    return _itkFastMarchingReachedTargetNodesStoppingCriterionPython.itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3_cast(obj)



