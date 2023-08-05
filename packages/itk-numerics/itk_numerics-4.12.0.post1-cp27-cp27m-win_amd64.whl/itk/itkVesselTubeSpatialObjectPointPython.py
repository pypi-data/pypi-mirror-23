# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVesselTubeSpatialObjectPointPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVesselTubeSpatialObjectPointPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVesselTubeSpatialObjectPointPython')
    _itkVesselTubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVesselTubeSpatialObjectPointPython', [dirname(__file__)])
        except ImportError:
            import _itkVesselTubeSpatialObjectPointPython
            return _itkVesselTubeSpatialObjectPointPython
        try:
            _mod = imp.load_module('_itkVesselTubeSpatialObjectPointPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVesselTubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVesselTubeSpatialObjectPointPython
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


import itkTubeSpatialObjectPointPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkSpatialObjectPointPython
import itkRGBAPixelPython
import itkPointPython
import ITKCommonBasePython
class itkVesselTubeSpatialObjectPoint2(itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2):
    """Proxy of C++ itkVesselTubeSpatialObjectPoint2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkVesselTubeSpatialObjectPointPython.delete_itkVesselTubeSpatialObjectPoint2

    def GetMedialness(self):
        """GetMedialness(itkVesselTubeSpatialObjectPoint2 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetMedialness(self)


    def SetMedialness(self, newMedialness):
        """SetMedialness(itkVesselTubeSpatialObjectPoint2 self, float const newMedialness)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetMedialness(self, newMedialness)


    def GetRidgeness(self):
        """GetRidgeness(itkVesselTubeSpatialObjectPoint2 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetRidgeness(self)


    def SetRidgeness(self, newRidgeness):
        """SetRidgeness(itkVesselTubeSpatialObjectPoint2 self, float const newRidgeness)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetRidgeness(self, newRidgeness)


    def GetBranchness(self):
        """GetBranchness(itkVesselTubeSpatialObjectPoint2 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetBranchness(self)


    def SetBranchness(self, newBranchness):
        """SetBranchness(itkVesselTubeSpatialObjectPoint2 self, float const newBranchness)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetBranchness(self, newBranchness)


    def GetMark(self):
        """GetMark(itkVesselTubeSpatialObjectPoint2 self) -> bool"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetMark(self)


    def SetMark(self, newMark):
        """SetMark(itkVesselTubeSpatialObjectPoint2 self, bool const newMark)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetMark(self, newMark)


    def GetAlpha1(self):
        """GetAlpha1(itkVesselTubeSpatialObjectPoint2 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetAlpha1(self)


    def SetAlpha1(self, newAlpha):
        """SetAlpha1(itkVesselTubeSpatialObjectPoint2 self, float const newAlpha)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetAlpha1(self, newAlpha)


    def GetAlpha2(self):
        """GetAlpha2(itkVesselTubeSpatialObjectPoint2 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetAlpha2(self)


    def SetAlpha2(self, newAlpha):
        """SetAlpha2(itkVesselTubeSpatialObjectPoint2 self, float const newAlpha)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetAlpha2(self, newAlpha)


    def GetAlpha3(self):
        """GetAlpha3(itkVesselTubeSpatialObjectPoint2 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetAlpha3(self)


    def SetAlpha3(self, newAlpha):
        """SetAlpha3(itkVesselTubeSpatialObjectPoint2 self, float const newAlpha)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetAlpha3(self, newAlpha)


    def __init__(self, *args):
        """
        __init__(itkVesselTubeSpatialObjectPoint2 self) -> itkVesselTubeSpatialObjectPoint2
        __init__(itkVesselTubeSpatialObjectPoint2 self, itkVesselTubeSpatialObjectPoint2 arg0) -> itkVesselTubeSpatialObjectPoint2
        """
        _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_swiginit(self, _itkVesselTubeSpatialObjectPointPython.new_itkVesselTubeSpatialObjectPoint2(*args))
itkVesselTubeSpatialObjectPoint2.GetMedialness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetMedialness, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetMedialness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetMedialness, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.GetRidgeness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetRidgeness, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetRidgeness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetRidgeness, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.GetBranchness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetBranchness, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetBranchness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetBranchness, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.GetMark = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetMark, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetMark = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetMark, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.GetAlpha1 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetAlpha1, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetAlpha1 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetAlpha1, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.GetAlpha2 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetAlpha2, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetAlpha2 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetAlpha2, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.GetAlpha3 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_GetAlpha3, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2.SetAlpha3 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_SetAlpha3, None, itkVesselTubeSpatialObjectPoint2)
itkVesselTubeSpatialObjectPoint2_swigregister = _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint2_swigregister
itkVesselTubeSpatialObjectPoint2_swigregister(itkVesselTubeSpatialObjectPoint2)

class itkVesselTubeSpatialObjectPoint3(itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3):
    """Proxy of C++ itkVesselTubeSpatialObjectPoint3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkVesselTubeSpatialObjectPointPython.delete_itkVesselTubeSpatialObjectPoint3

    def GetMedialness(self):
        """GetMedialness(itkVesselTubeSpatialObjectPoint3 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetMedialness(self)


    def SetMedialness(self, newMedialness):
        """SetMedialness(itkVesselTubeSpatialObjectPoint3 self, float const newMedialness)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetMedialness(self, newMedialness)


    def GetRidgeness(self):
        """GetRidgeness(itkVesselTubeSpatialObjectPoint3 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetRidgeness(self)


    def SetRidgeness(self, newRidgeness):
        """SetRidgeness(itkVesselTubeSpatialObjectPoint3 self, float const newRidgeness)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetRidgeness(self, newRidgeness)


    def GetBranchness(self):
        """GetBranchness(itkVesselTubeSpatialObjectPoint3 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetBranchness(self)


    def SetBranchness(self, newBranchness):
        """SetBranchness(itkVesselTubeSpatialObjectPoint3 self, float const newBranchness)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetBranchness(self, newBranchness)


    def GetMark(self):
        """GetMark(itkVesselTubeSpatialObjectPoint3 self) -> bool"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetMark(self)


    def SetMark(self, newMark):
        """SetMark(itkVesselTubeSpatialObjectPoint3 self, bool const newMark)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetMark(self, newMark)


    def GetAlpha1(self):
        """GetAlpha1(itkVesselTubeSpatialObjectPoint3 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetAlpha1(self)


    def SetAlpha1(self, newAlpha):
        """SetAlpha1(itkVesselTubeSpatialObjectPoint3 self, float const newAlpha)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetAlpha1(self, newAlpha)


    def GetAlpha2(self):
        """GetAlpha2(itkVesselTubeSpatialObjectPoint3 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetAlpha2(self)


    def SetAlpha2(self, newAlpha):
        """SetAlpha2(itkVesselTubeSpatialObjectPoint3 self, float const newAlpha)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetAlpha2(self, newAlpha)


    def GetAlpha3(self):
        """GetAlpha3(itkVesselTubeSpatialObjectPoint3 self) -> float"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetAlpha3(self)


    def SetAlpha3(self, newAlpha):
        """SetAlpha3(itkVesselTubeSpatialObjectPoint3 self, float const newAlpha)"""
        return _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetAlpha3(self, newAlpha)


    def __init__(self, *args):
        """
        __init__(itkVesselTubeSpatialObjectPoint3 self) -> itkVesselTubeSpatialObjectPoint3
        __init__(itkVesselTubeSpatialObjectPoint3 self, itkVesselTubeSpatialObjectPoint3 arg0) -> itkVesselTubeSpatialObjectPoint3
        """
        _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_swiginit(self, _itkVesselTubeSpatialObjectPointPython.new_itkVesselTubeSpatialObjectPoint3(*args))
itkVesselTubeSpatialObjectPoint3.GetMedialness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetMedialness, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetMedialness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetMedialness, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.GetRidgeness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetRidgeness, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetRidgeness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetRidgeness, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.GetBranchness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetBranchness, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetBranchness = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetBranchness, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.GetMark = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetMark, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetMark = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetMark, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.GetAlpha1 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetAlpha1, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetAlpha1 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetAlpha1, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.GetAlpha2 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetAlpha2, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetAlpha2 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetAlpha2, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.GetAlpha3 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_GetAlpha3, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3.SetAlpha3 = new_instancemethod(_itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_SetAlpha3, None, itkVesselTubeSpatialObjectPoint3)
itkVesselTubeSpatialObjectPoint3_swigregister = _itkVesselTubeSpatialObjectPointPython.itkVesselTubeSpatialObjectPoint3_swigregister
itkVesselTubeSpatialObjectPoint3_swigregister(itkVesselTubeSpatialObjectPoint3)



