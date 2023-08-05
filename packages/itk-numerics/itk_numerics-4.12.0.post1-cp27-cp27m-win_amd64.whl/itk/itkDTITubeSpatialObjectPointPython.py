# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDTITubeSpatialObjectPointPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDTITubeSpatialObjectPointPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDTITubeSpatialObjectPointPython')
    _itkDTITubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDTITubeSpatialObjectPointPython', [dirname(__file__)])
        except ImportError:
            import _itkDTITubeSpatialObjectPointPython
            return _itkDTITubeSpatialObjectPointPython
        try:
            _mod = imp.load_module('_itkDTITubeSpatialObjectPointPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDTITubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDTITubeSpatialObjectPointPython
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
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
class itkDTITubeSpatialObjectPoint3(itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3):
    """Proxy of C++ itkDTITubeSpatialObjectPoint3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    FA = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_FA
    ADC = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_ADC
    GA = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GA
    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_itkDTITubeSpatialObjectPoint3

    def SetTensorMatrix(self, *args):
        """
        SetTensorMatrix(itkDTITubeSpatialObjectPoint3 self, itkDiffusionTensor3DD matrix)
        SetTensorMatrix(itkDTITubeSpatialObjectPoint3 self, itkDiffusionTensor3DF matrix)
        SetTensorMatrix(itkDTITubeSpatialObjectPoint3 self, float const * matrix)
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetTensorMatrix(self, *args)


    def GetTensorMatrix(self):
        """GetTensorMatrix(itkDTITubeSpatialObjectPoint3 self) -> float const *"""
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetTensorMatrix(self)


    def AddField(self, *args):
        """
        AddField(itkDTITubeSpatialObjectPoint3 self, char const * name, float value)
        AddField(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3::FieldEnumType name, float value)
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_AddField(self, *args)


    def SetField(self, *args):
        """
        SetField(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3::FieldEnumType name, float value)
        SetField(itkDTITubeSpatialObjectPoint3 self, char const * name, float value)
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetField(self, *args)


    def GetFields(self):
        """GetFields(itkDTITubeSpatialObjectPoint3 self) -> std::vector< std::pair< std::string,float >,std::allocator< std::pair< std::string,float > > > const &"""
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetFields(self)


    def GetField(self, *args):
        """
        GetField(itkDTITubeSpatialObjectPoint3 self, char const * name) -> float
        GetField(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3::FieldEnumType name) -> float
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetField(self, *args)


    def __init__(self, *args):
        """
        __init__(itkDTITubeSpatialObjectPoint3 self) -> itkDTITubeSpatialObjectPoint3
        __init__(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3 arg0) -> itkDTITubeSpatialObjectPoint3
        """
        _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_itkDTITubeSpatialObjectPoint3(*args))
itkDTITubeSpatialObjectPoint3.SetTensorMatrix = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetTensorMatrix, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.GetTensorMatrix = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetTensorMatrix, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.AddField = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_AddField, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.SetField = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetField, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.GetFields = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetFields, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.GetField = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetField, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3_swigregister = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_swigregister
itkDTITubeSpatialObjectPoint3_swigregister(itkDTITubeSpatialObjectPoint3)



