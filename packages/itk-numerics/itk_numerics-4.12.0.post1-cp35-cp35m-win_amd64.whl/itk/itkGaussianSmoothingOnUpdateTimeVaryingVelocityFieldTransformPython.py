# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython')
    _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython
            return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython
        try:
            _mod = imp.load_module('_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython
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
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import itkOffsetPython
import itkSizePython
import itkVectorPython
import vnl_vector_refPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkIndexPython
import itkImageRegionPython
import itkTimeVaryingVelocityFieldTransformPython
import itkVelocityFieldTransformPython
import itkTransformBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkDisplacementFieldTransformPython

def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_New():
  return itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.New()


def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_New():
  return itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.New()

class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2(itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2):
    """Proxy of C++ itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Pointer":
        """__New_orig__() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Pointer"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Pointer":
        """Clone(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Pointer"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Clone(self)


    def SetGaussianSpatialSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """SetGaussianSpatialSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianSpatialSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSpatialSmoothingVarianceForTheUpdateField(self) -> "double const &":
        """GetGaussianSpatialSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianSpatialSmoothingVarianceForTheUpdateField(self)


    def SetGaussianTemporalSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """SetGaussianTemporalSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianTemporalSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianTemporalSmoothingVarianceForTheUpdateField(self) -> "double const &":
        """GetGaussianTemporalSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianTemporalSmoothingVarianceForTheUpdateField(self)


    def SetGaussianSpatialSmoothingVarianceForTheTotalField(self, _arg: 'double const') -> "void":
        """SetGaussianSpatialSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianSpatialSmoothingVarianceForTheTotalField(self, _arg)


    def GetGaussianSpatialSmoothingVarianceForTheTotalField(self) -> "double const &":
        """GetGaussianSpatialSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianSpatialSmoothingVarianceForTheTotalField(self)


    def SetGaussianTemporalSmoothingVarianceForTheTotalField(self, _arg: 'double const') -> "void":
        """SetGaussianTemporalSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianTemporalSmoothingVarianceForTheTotalField(self, _arg)


    def GetGaussianTemporalSmoothingVarianceForTheTotalField(self) -> "double const &":
        """GetGaussianTemporalSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianTemporalSmoothingVarianceForTheTotalField(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, itkArrayD update)
        """
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothTimeVaryingVelocityField(self, arg0: 'itkImageVD23', arg1: 'double', arg2: 'double') -> "itkImageVD23_Pointer":
        """GaussianSmoothTimeVaryingVelocityField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self, itkImageVD23 arg0, double arg1, double arg2) -> itkImageVD23_Pointer"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GaussianSmoothTimeVaryingVelocityField(self, arg0, arg1, arg2)

    __swig_destroy__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.delete_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2

    def cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 *":
        """cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 *":
        """GetPointer(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 self) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2

        Create a new object of the class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.Clone = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Clone, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.SetGaussianSpatialSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianSpatialSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.GetGaussianSpatialSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianSpatialSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.SetGaussianTemporalSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianTemporalSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.GetGaussianTemporalSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianTemporalSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.SetGaussianSpatialSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianSpatialSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.GetGaussianSpatialSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianSpatialSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.SetGaussianTemporalSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianTemporalSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.GetGaussianTemporalSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianTemporalSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.UpdateTransformParameters = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_UpdateTransformParameters, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.GaussianSmoothTimeVaryingVelocityField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GaussianSmoothTimeVaryingVelocityField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.GetPointer = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetPointer, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_swigregister = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_swigregister
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_swigregister(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)

def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__() -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Pointer":
    """itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Pointer"""
    return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__()

def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 *":
    """itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2"""
    return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast(obj)

class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3(itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3):
    """Proxy of C++ itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Pointer":
        """__New_orig__() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Pointer"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Pointer":
        """Clone(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Pointer"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Clone(self)


    def SetGaussianSpatialSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """SetGaussianSpatialSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianSpatialSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSpatialSmoothingVarianceForTheUpdateField(self) -> "double const &":
        """GetGaussianSpatialSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianSpatialSmoothingVarianceForTheUpdateField(self)


    def SetGaussianTemporalSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """SetGaussianTemporalSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianTemporalSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianTemporalSmoothingVarianceForTheUpdateField(self) -> "double const &":
        """GetGaussianTemporalSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianTemporalSmoothingVarianceForTheUpdateField(self)


    def SetGaussianSpatialSmoothingVarianceForTheTotalField(self, _arg: 'double const') -> "void":
        """SetGaussianSpatialSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianSpatialSmoothingVarianceForTheTotalField(self, _arg)


    def GetGaussianSpatialSmoothingVarianceForTheTotalField(self) -> "double const &":
        """GetGaussianSpatialSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianSpatialSmoothingVarianceForTheTotalField(self)


    def SetGaussianTemporalSmoothingVarianceForTheTotalField(self, _arg: 'double const') -> "void":
        """SetGaussianTemporalSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, double const _arg)"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianTemporalSmoothingVarianceForTheTotalField(self, _arg)


    def GetGaussianTemporalSmoothingVarianceForTheTotalField(self) -> "double const &":
        """GetGaussianTemporalSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianTemporalSmoothingVarianceForTheTotalField(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, itkArrayD update)
        """
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothTimeVaryingVelocityField(self, arg0: 'itkImageVD34', arg1: 'double', arg2: 'double') -> "itkImageVD34_Pointer":
        """GaussianSmoothTimeVaryingVelocityField(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self, itkImageVD34 arg0, double arg1, double arg2) -> itkImageVD34_Pointer"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GaussianSmoothTimeVaryingVelocityField(self, arg0, arg1, arg2)

    __swig_destroy__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.delete_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3

    def cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 *":
        """cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 *":
        """GetPointer(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 self) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3"""
        return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3

        Create a new object of the class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.Clone = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Clone, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.SetGaussianSpatialSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianSpatialSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.GetGaussianSpatialSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianSpatialSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.SetGaussianTemporalSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianTemporalSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.GetGaussianTemporalSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianTemporalSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.SetGaussianSpatialSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianSpatialSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.GetGaussianSpatialSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianSpatialSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.SetGaussianTemporalSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianTemporalSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.GetGaussianTemporalSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianTemporalSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.UpdateTransformParameters = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_UpdateTransformParameters, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.GaussianSmoothTimeVaryingVelocityField = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GaussianSmoothTimeVaryingVelocityField, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.GetPointer = new_instancemethod(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetPointer, None, itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_swigregister = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_swigregister
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_swigregister(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)

def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__() -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Pointer":
    """itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Pointer"""
    return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__()

def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 *":
    """itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3"""
    return _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast(obj)



