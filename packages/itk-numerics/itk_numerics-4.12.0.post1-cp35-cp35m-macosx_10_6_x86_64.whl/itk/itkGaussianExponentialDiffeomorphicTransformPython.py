# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGaussianExponentialDiffeomorphicTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGaussianExponentialDiffeomorphicTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGaussianExponentialDiffeomorphicTransformPython')
    _itkGaussianExponentialDiffeomorphicTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGaussianExponentialDiffeomorphicTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkGaussianExponentialDiffeomorphicTransformPython
            return _itkGaussianExponentialDiffeomorphicTransformPython
        try:
            _mod = imp.load_module('_itkGaussianExponentialDiffeomorphicTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGaussianExponentialDiffeomorphicTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGaussianExponentialDiffeomorphicTransformPython
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


import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkSizePython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import ITKCommonBasePython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkConstantVelocityFieldTransformPython
import itkOptimizerParametersPython
import itkTransformBasePython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkDisplacementFieldTransformPython

def itkGaussianExponentialDiffeomorphicTransformD3_New():
  return itkGaussianExponentialDiffeomorphicTransformD3.New()


def itkGaussianExponentialDiffeomorphicTransformD2_New():
  return itkGaussianExponentialDiffeomorphicTransformD2.New()

class itkGaussianExponentialDiffeomorphicTransformD2(itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2):
    """Proxy of C++ itkGaussianExponentialDiffeomorphicTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD2_Pointer":
        """__New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD2_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianExponentialDiffeomorphicTransformD2_Pointer":
        """Clone(itkGaussianExponentialDiffeomorphicTransformD2 self) -> itkGaussianExponentialDiffeomorphicTransformD2_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD2 self, itkArrayD update)
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothConstantVelocityField(self, arg0: 'itkImageVD22', arg1: 'double') -> "itkImageVD22_Pointer":
        """GaussianSmoothConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD2 self, itkImageVD22 arg0, double arg1) -> itkImageVD22_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GaussianSmoothConstantVelocityField(self, arg0, arg1)


    def SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg: 'double const') -> "void":
        """SetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD2 self, double const _arg)"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg)


    def GetGaussianSmoothingVarianceForTheConstantVelocityField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD2 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheConstantVelocityField(self)


    def SetGaussianSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """SetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD2 self, double const _arg)"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSmoothingVarianceForTheUpdateField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD2 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheUpdateField(self)

    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD2

    def cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD2 *":
        """cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD2"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGaussianExponentialDiffeomorphicTransformD2 *":
        """GetPointer(itkGaussianExponentialDiffeomorphicTransformD2 self) -> itkGaussianExponentialDiffeomorphicTransformD2"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD2

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianExponentialDiffeomorphicTransformD2.Clone = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_Clone, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.UpdateTransformParameters = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_UpdateTransformParameters, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GaussianSmoothConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GaussianSmoothConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.SetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.SetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GetPointer = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetPointer, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2_swigregister = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_swigregister
itkGaussianExponentialDiffeomorphicTransformD2_swigregister(itkGaussianExponentialDiffeomorphicTransformD2)

def itkGaussianExponentialDiffeomorphicTransformD2___New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD2_Pointer":
    """itkGaussianExponentialDiffeomorphicTransformD2___New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD2_Pointer"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2___New_orig__()

def itkGaussianExponentialDiffeomorphicTransformD2_cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD2 *":
    """itkGaussianExponentialDiffeomorphicTransformD2_cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD2"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_cast(obj)

class itkGaussianExponentialDiffeomorphicTransformD3(itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3):
    """Proxy of C++ itkGaussianExponentialDiffeomorphicTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD3_Pointer":
        """__New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD3_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianExponentialDiffeomorphicTransformD3_Pointer":
        """Clone(itkGaussianExponentialDiffeomorphicTransformD3 self) -> itkGaussianExponentialDiffeomorphicTransformD3_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD3 self, itkArrayD update)
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothConstantVelocityField(self, arg0: 'itkImageVD33', arg1: 'double') -> "itkImageVD33_Pointer":
        """GaussianSmoothConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD3 self, itkImageVD33 arg0, double arg1) -> itkImageVD33_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GaussianSmoothConstantVelocityField(self, arg0, arg1)


    def SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg: 'double const') -> "void":
        """SetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD3 self, double const _arg)"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg)


    def GetGaussianSmoothingVarianceForTheConstantVelocityField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD3 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheConstantVelocityField(self)


    def SetGaussianSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """SetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD3 self, double const _arg)"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSmoothingVarianceForTheUpdateField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD3 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheUpdateField(self)

    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD3

    def cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD3 *":
        """cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD3"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkGaussianExponentialDiffeomorphicTransformD3 *":
        """GetPointer(itkGaussianExponentialDiffeomorphicTransformD3 self) -> itkGaussianExponentialDiffeomorphicTransformD3"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD3

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianExponentialDiffeomorphicTransformD3.Clone = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_Clone, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.UpdateTransformParameters = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_UpdateTransformParameters, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GaussianSmoothConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GaussianSmoothConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.SetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.SetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GetPointer = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetPointer, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3_swigregister = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_swigregister
itkGaussianExponentialDiffeomorphicTransformD3_swigregister(itkGaussianExponentialDiffeomorphicTransformD3)

def itkGaussianExponentialDiffeomorphicTransformD3___New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD3_Pointer":
    """itkGaussianExponentialDiffeomorphicTransformD3___New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD3_Pointer"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3___New_orig__()

def itkGaussianExponentialDiffeomorphicTransformD3_cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD3 *":
    """itkGaussianExponentialDiffeomorphicTransformD3_cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD3"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_cast(obj)



