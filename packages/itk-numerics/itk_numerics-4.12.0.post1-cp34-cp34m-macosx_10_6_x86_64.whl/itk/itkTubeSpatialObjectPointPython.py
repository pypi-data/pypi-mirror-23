# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTubeSpatialObjectPointPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTubeSpatialObjectPointPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTubeSpatialObjectPointPython')
    _itkTubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTubeSpatialObjectPointPython', [dirname(__file__)])
        except ImportError:
            import _itkTubeSpatialObjectPointPython
            return _itkTubeSpatialObjectPointPython
        try:
            _mod = imp.load_module('_itkTubeSpatialObjectPointPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTubeSpatialObjectPointPython
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


import itkSpatialObjectPointPython
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkRGBAPixelPython
import ITKCommonBasePython
import itkCovariantVectorPython
class itkTubeSpatialObjectPoint2(itkSpatialObjectPointPython.itkSpatialObjectPoint2):
    """Proxy of C++ itkTubeSpatialObjectPoint2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_itkTubeSpatialObjectPoint2

    def GetTangent(self) -> "itkVectorD2 const &":
        """GetTangent(itkTubeSpatialObjectPoint2 self) -> itkVectorD2"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetTangent(self)


    def SetTangent(self, *args) -> "void":
        """
        SetTangent(itkTubeSpatialObjectPoint2 self, itkVectorD2 newT)
        SetTangent(itkTubeSpatialObjectPoint2 self, double const t0, double const t1)
        SetTangent(itkTubeSpatialObjectPoint2 self, double const t0, double const t1, double const t2)
        """
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetTangent(self, *args)


    def GetNormal1(self) -> "itkCovariantVectorD2 const &":
        """GetNormal1(itkTubeSpatialObjectPoint2 self) -> itkCovariantVectorD2"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal1(self)


    def SetNormal1(self, *args) -> "void":
        """
        SetNormal1(itkTubeSpatialObjectPoint2 self, itkCovariantVectorD2 newV1)
        SetNormal1(itkTubeSpatialObjectPoint2 self, double const v10, double const v11)
        SetNormal1(itkTubeSpatialObjectPoint2 self, double const v10, double const v11, double const v12)
        """
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal1(self, *args)


    def GetNormal2(self) -> "itkCovariantVectorD2 const &":
        """GetNormal2(itkTubeSpatialObjectPoint2 self) -> itkCovariantVectorD2"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal2(self)


    def SetNormal2(self, *args) -> "void":
        """
        SetNormal2(itkTubeSpatialObjectPoint2 self, itkCovariantVectorD2 newV2)
        SetNormal2(itkTubeSpatialObjectPoint2 self, double const v20, double const v21)
        SetNormal2(itkTubeSpatialObjectPoint2 self, double const v20, double const v21, double const v22)
        """
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal2(self, *args)


    def GetRadius(self) -> "float":
        """GetRadius(itkTubeSpatialObjectPoint2 self) -> float"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetRadius(self)


    def SetRadius(self, newR: 'float const') -> "void":
        """SetRadius(itkTubeSpatialObjectPoint2 self, float const newR)"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetRadius(self, newR)


    def GetNumDimensions(self) -> "unsigned short":
        """GetNumDimensions(itkTubeSpatialObjectPoint2 self) -> unsigned short"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNumDimensions(self)


    def __init__(self, *args):
        """
        __init__(itkTubeSpatialObjectPoint2 self) -> itkTubeSpatialObjectPoint2
        __init__(itkTubeSpatialObjectPoint2 self, itkTubeSpatialObjectPoint2 arg0) -> itkTubeSpatialObjectPoint2
        """
        _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_swiginit(self, _itkTubeSpatialObjectPointPython.new_itkTubeSpatialObjectPoint2(*args))
itkTubeSpatialObjectPoint2.GetTangent = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetTangent, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.SetTangent = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetTangent, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.GetNormal1 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal1, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.SetNormal1 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal1, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.GetNormal2 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal2, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.SetNormal2 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal2, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.GetRadius = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetRadius, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.SetRadius = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetRadius, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2.GetNumDimensions = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNumDimensions, None, itkTubeSpatialObjectPoint2)
itkTubeSpatialObjectPoint2_swigregister = _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_swigregister
itkTubeSpatialObjectPoint2_swigregister(itkTubeSpatialObjectPoint2)

class itkTubeSpatialObjectPoint3(itkSpatialObjectPointPython.itkSpatialObjectPoint3):
    """Proxy of C++ itkTubeSpatialObjectPoint3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_itkTubeSpatialObjectPoint3

    def GetTangent(self) -> "itkVectorD3 const &":
        """GetTangent(itkTubeSpatialObjectPoint3 self) -> itkVectorD3"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetTangent(self)


    def SetTangent(self, *args) -> "void":
        """
        SetTangent(itkTubeSpatialObjectPoint3 self, itkVectorD3 newT)
        SetTangent(itkTubeSpatialObjectPoint3 self, double const t0, double const t1)
        SetTangent(itkTubeSpatialObjectPoint3 self, double const t0, double const t1, double const t2)
        """
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetTangent(self, *args)


    def GetNormal1(self) -> "itkCovariantVectorD3 const &":
        """GetNormal1(itkTubeSpatialObjectPoint3 self) -> itkCovariantVectorD3"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal1(self)


    def SetNormal1(self, *args) -> "void":
        """
        SetNormal1(itkTubeSpatialObjectPoint3 self, itkCovariantVectorD3 newV1)
        SetNormal1(itkTubeSpatialObjectPoint3 self, double const v10, double const v11)
        SetNormal1(itkTubeSpatialObjectPoint3 self, double const v10, double const v11, double const v12)
        """
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal1(self, *args)


    def GetNormal2(self) -> "itkCovariantVectorD3 const &":
        """GetNormal2(itkTubeSpatialObjectPoint3 self) -> itkCovariantVectorD3"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal2(self)


    def SetNormal2(self, *args) -> "void":
        """
        SetNormal2(itkTubeSpatialObjectPoint3 self, itkCovariantVectorD3 newV2)
        SetNormal2(itkTubeSpatialObjectPoint3 self, double const v20, double const v21)
        SetNormal2(itkTubeSpatialObjectPoint3 self, double const v20, double const v21, double const v22)
        """
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal2(self, *args)


    def GetRadius(self) -> "float":
        """GetRadius(itkTubeSpatialObjectPoint3 self) -> float"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetRadius(self)


    def SetRadius(self, newR: 'float const') -> "void":
        """SetRadius(itkTubeSpatialObjectPoint3 self, float const newR)"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetRadius(self, newR)


    def GetNumDimensions(self) -> "unsigned short":
        """GetNumDimensions(itkTubeSpatialObjectPoint3 self) -> unsigned short"""
        return _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNumDimensions(self)


    def __init__(self, *args):
        """
        __init__(itkTubeSpatialObjectPoint3 self) -> itkTubeSpatialObjectPoint3
        __init__(itkTubeSpatialObjectPoint3 self, itkTubeSpatialObjectPoint3 arg0) -> itkTubeSpatialObjectPoint3
        """
        _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_swiginit(self, _itkTubeSpatialObjectPointPython.new_itkTubeSpatialObjectPoint3(*args))
itkTubeSpatialObjectPoint3.GetTangent = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetTangent, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.SetTangent = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetTangent, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.GetNormal1 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal1, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.SetNormal1 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal1, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.GetNormal2 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal2, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.SetNormal2 = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal2, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.GetRadius = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetRadius, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.SetRadius = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetRadius, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3.GetNumDimensions = new_instancemethod(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNumDimensions, None, itkTubeSpatialObjectPoint3)
itkTubeSpatialObjectPoint3_swigregister = _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_swigregister
itkTubeSpatialObjectPoint3_swigregister(itkTubeSpatialObjectPoint3)



