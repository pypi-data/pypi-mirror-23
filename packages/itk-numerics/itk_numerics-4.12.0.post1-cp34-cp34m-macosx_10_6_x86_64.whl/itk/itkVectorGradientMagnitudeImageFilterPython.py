# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVectorGradientMagnitudeImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVectorGradientMagnitudeImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVectorGradientMagnitudeImageFilterPython')
    _itkVectorGradientMagnitudeImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVectorGradientMagnitudeImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkVectorGradientMagnitudeImageFilterPython
            return _itkVectorGradientMagnitudeImageFilterPython
        try:
            _mod = imp.load_module('_itkVectorGradientMagnitudeImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVectorGradientMagnitudeImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVectorGradientMagnitudeImageFilterPython
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
import itkFixedArrayPython
import itkImagePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkVectorGradientMagnitudeImageFilterIVF33F_New():
  return itkVectorGradientMagnitudeImageFilterIVF33F.New()


def itkVectorGradientMagnitudeImageFilterIVF22F_New():
  return itkVectorGradientMagnitudeImageFilterIVF22F.New()

class itkVectorGradientMagnitudeImageFilterIVF22F(itkImageToImageFilterBPython.itkImageToImageFilterIVF22IF2):
    """Proxy of C++ itkVectorGradientMagnitudeImageFilterIVF22F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVectorGradientMagnitudeImageFilterIVF22F_Pointer":
        """__New_orig__() -> itkVectorGradientMagnitudeImageFilterIVF22F_Pointer"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVectorGradientMagnitudeImageFilterIVF22F_Pointer":
        """Clone(itkVectorGradientMagnitudeImageFilterIVF22F self) -> itkVectorGradientMagnitudeImageFilterIVF22F_Pointer"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkVectorGradientMagnitudeImageFilterIVF22F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GenerateInputRequestedRegion(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkVectorGradientMagnitudeImageFilterIVF22F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkVectorGradientMagnitudeImageFilterIVF22F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, arg0: 'bool') -> "void":
        """SetUseImageSpacing(itkVectorGradientMagnitudeImageFilterIVF22F self, bool arg0)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUseImageSpacing(self, arg0)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkVectorGradientMagnitudeImageFilterIVF22F self) -> bool"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetUseImageSpacing(self)


    def SetDerivativeWeights(self, _arg: 'itkFixedArrayF2') -> "void":
        """SetDerivativeWeights(itkVectorGradientMagnitudeImageFilterIVF22F self, itkFixedArrayF2 _arg)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetDerivativeWeights(self, _arg)


    def GetDerivativeWeights(self) -> "itkFixedArrayF2 const &":
        """GetDerivativeWeights(itkVectorGradientMagnitudeImageFilterIVF22F self) -> itkFixedArrayF2"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetDerivativeWeights(self)


    def SetComponentWeights(self, _arg: 'itkFixedArrayF2') -> "void":
        """SetComponentWeights(itkVectorGradientMagnitudeImageFilterIVF22F self, itkFixedArrayF2 _arg)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetComponentWeights(self, _arg)


    def GetComponentWeights(self) -> "itkFixedArrayF2 const &":
        """GetComponentWeights(itkVectorGradientMagnitudeImageFilterIVF22F self) -> itkFixedArrayF2"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetComponentWeights(self)


    def GetNeighborhoodRadius(self) -> "itkSize2 const":
        """GetNeighborhoodRadius(itkVectorGradientMagnitudeImageFilterIVF22F self) -> itkSize2"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetNeighborhoodRadius(self)


    def SetNeighborhoodRadius(self, arg0: 'itkSize2') -> "void":
        """SetNeighborhoodRadius(itkVectorGradientMagnitudeImageFilterIVF22F self, itkSize2 arg0)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetNeighborhoodRadius(self, arg0)


    def SetUsePrincipleComponents(self, _arg: 'bool const') -> "void":
        """SetUsePrincipleComponents(itkVectorGradientMagnitudeImageFilterIVF22F self, bool const _arg)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUsePrincipleComponents(self, _arg)


    def GetUsePrincipleComponents(self) -> "bool":
        """GetUsePrincipleComponents(itkVectorGradientMagnitudeImageFilterIVF22F self) -> bool"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetUsePrincipleComponents(self)


    def SetUsePrincipleComponentsOn(self) -> "void":
        """SetUsePrincipleComponentsOn(itkVectorGradientMagnitudeImageFilterIVF22F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUsePrincipleComponentsOn(self)


    def SetUsePrincipleComponentsOff(self) -> "void":
        """SetUsePrincipleComponentsOff(itkVectorGradientMagnitudeImageFilterIVF22F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUsePrincipleComponentsOff(self)


    def CubicSolver(arg0: 'double *', arg1: 'double *') -> "int":
        """CubicSolver(double * arg0, double * arg1) -> int"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_CubicSolver(arg0, arg1)

    CubicSolver = staticmethod(CubicSolver)
    InputHasNumericTraitsCheck = _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_InputHasNumericTraitsCheck
    RealTypeHasNumericTraitsCheck = _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_RealTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkVectorGradientMagnitudeImageFilterPython.delete_itkVectorGradientMagnitudeImageFilterIVF22F

    def cast(obj: 'itkLightObject') -> "itkVectorGradientMagnitudeImageFilterIVF22F *":
        """cast(itkLightObject obj) -> itkVectorGradientMagnitudeImageFilterIVF22F"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVectorGradientMagnitudeImageFilterIVF22F *":
        """GetPointer(itkVectorGradientMagnitudeImageFilterIVF22F self) -> itkVectorGradientMagnitudeImageFilterIVF22F"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVectorGradientMagnitudeImageFilterIVF22F

        Create a new object of the class itkVectorGradientMagnitudeImageFilterIVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVectorGradientMagnitudeImageFilterIVF22F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVectorGradientMagnitudeImageFilterIVF22F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVectorGradientMagnitudeImageFilterIVF22F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVectorGradientMagnitudeImageFilterIVF22F.Clone = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_Clone, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GenerateInputRequestedRegion = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GenerateInputRequestedRegion, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetUseImageSpacingOn = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUseImageSpacingOn, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetUseImageSpacingOff = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUseImageSpacingOff, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetUseImageSpacing = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUseImageSpacing, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GetUseImageSpacing = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetUseImageSpacing, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetDerivativeWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetDerivativeWeights, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GetDerivativeWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetDerivativeWeights, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetComponentWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetComponentWeights, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GetComponentWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetComponentWeights, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GetNeighborhoodRadius = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetNeighborhoodRadius, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetNeighborhoodRadius = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetNeighborhoodRadius, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetUsePrincipleComponents = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUsePrincipleComponents, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GetUsePrincipleComponents = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetUsePrincipleComponents, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetUsePrincipleComponentsOn = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUsePrincipleComponentsOn, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.SetUsePrincipleComponentsOff = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_SetUsePrincipleComponentsOff, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F.GetPointer = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_GetPointer, None, itkVectorGradientMagnitudeImageFilterIVF22F)
itkVectorGradientMagnitudeImageFilterIVF22F_swigregister = _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_swigregister
itkVectorGradientMagnitudeImageFilterIVF22F_swigregister(itkVectorGradientMagnitudeImageFilterIVF22F)

def itkVectorGradientMagnitudeImageFilterIVF22F___New_orig__() -> "itkVectorGradientMagnitudeImageFilterIVF22F_Pointer":
    """itkVectorGradientMagnitudeImageFilterIVF22F___New_orig__() -> itkVectorGradientMagnitudeImageFilterIVF22F_Pointer"""
    return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F___New_orig__()

def itkVectorGradientMagnitudeImageFilterIVF22F_CubicSolver(arg0: 'double *', arg1: 'double *') -> "int":
    """itkVectorGradientMagnitudeImageFilterIVF22F_CubicSolver(double * arg0, double * arg1) -> int"""
    return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_CubicSolver(arg0, arg1)

def itkVectorGradientMagnitudeImageFilterIVF22F_cast(obj: 'itkLightObject') -> "itkVectorGradientMagnitudeImageFilterIVF22F *":
    """itkVectorGradientMagnitudeImageFilterIVF22F_cast(itkLightObject obj) -> itkVectorGradientMagnitudeImageFilterIVF22F"""
    return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF22F_cast(obj)

class itkVectorGradientMagnitudeImageFilterIVF33F(itkImageToImageFilterBPython.itkImageToImageFilterIVF33IF3):
    """Proxy of C++ itkVectorGradientMagnitudeImageFilterIVF33F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVectorGradientMagnitudeImageFilterIVF33F_Pointer":
        """__New_orig__() -> itkVectorGradientMagnitudeImageFilterIVF33F_Pointer"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVectorGradientMagnitudeImageFilterIVF33F_Pointer":
        """Clone(itkVectorGradientMagnitudeImageFilterIVF33F self) -> itkVectorGradientMagnitudeImageFilterIVF33F_Pointer"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkVectorGradientMagnitudeImageFilterIVF33F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GenerateInputRequestedRegion(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkVectorGradientMagnitudeImageFilterIVF33F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkVectorGradientMagnitudeImageFilterIVF33F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, arg0: 'bool') -> "void":
        """SetUseImageSpacing(itkVectorGradientMagnitudeImageFilterIVF33F self, bool arg0)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUseImageSpacing(self, arg0)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkVectorGradientMagnitudeImageFilterIVF33F self) -> bool"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetUseImageSpacing(self)


    def SetDerivativeWeights(self, _arg: 'itkFixedArrayF3') -> "void":
        """SetDerivativeWeights(itkVectorGradientMagnitudeImageFilterIVF33F self, itkFixedArrayF3 _arg)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetDerivativeWeights(self, _arg)


    def GetDerivativeWeights(self) -> "itkFixedArrayF3 const &":
        """GetDerivativeWeights(itkVectorGradientMagnitudeImageFilterIVF33F self) -> itkFixedArrayF3"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetDerivativeWeights(self)


    def SetComponentWeights(self, _arg: 'itkFixedArrayF3') -> "void":
        """SetComponentWeights(itkVectorGradientMagnitudeImageFilterIVF33F self, itkFixedArrayF3 _arg)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetComponentWeights(self, _arg)


    def GetComponentWeights(self) -> "itkFixedArrayF3 const &":
        """GetComponentWeights(itkVectorGradientMagnitudeImageFilterIVF33F self) -> itkFixedArrayF3"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetComponentWeights(self)


    def GetNeighborhoodRadius(self) -> "itkSize3 const":
        """GetNeighborhoodRadius(itkVectorGradientMagnitudeImageFilterIVF33F self) -> itkSize3"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetNeighborhoodRadius(self)


    def SetNeighborhoodRadius(self, arg0: 'itkSize3') -> "void":
        """SetNeighborhoodRadius(itkVectorGradientMagnitudeImageFilterIVF33F self, itkSize3 arg0)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetNeighborhoodRadius(self, arg0)


    def SetUsePrincipleComponents(self, _arg: 'bool const') -> "void":
        """SetUsePrincipleComponents(itkVectorGradientMagnitudeImageFilterIVF33F self, bool const _arg)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUsePrincipleComponents(self, _arg)


    def GetUsePrincipleComponents(self) -> "bool":
        """GetUsePrincipleComponents(itkVectorGradientMagnitudeImageFilterIVF33F self) -> bool"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetUsePrincipleComponents(self)


    def SetUsePrincipleComponentsOn(self) -> "void":
        """SetUsePrincipleComponentsOn(itkVectorGradientMagnitudeImageFilterIVF33F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUsePrincipleComponentsOn(self)


    def SetUsePrincipleComponentsOff(self) -> "void":
        """SetUsePrincipleComponentsOff(itkVectorGradientMagnitudeImageFilterIVF33F self)"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUsePrincipleComponentsOff(self)


    def CubicSolver(arg0: 'double *', arg1: 'double *') -> "int":
        """CubicSolver(double * arg0, double * arg1) -> int"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_CubicSolver(arg0, arg1)

    CubicSolver = staticmethod(CubicSolver)
    InputHasNumericTraitsCheck = _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_InputHasNumericTraitsCheck
    RealTypeHasNumericTraitsCheck = _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_RealTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkVectorGradientMagnitudeImageFilterPython.delete_itkVectorGradientMagnitudeImageFilterIVF33F

    def cast(obj: 'itkLightObject') -> "itkVectorGradientMagnitudeImageFilterIVF33F *":
        """cast(itkLightObject obj) -> itkVectorGradientMagnitudeImageFilterIVF33F"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVectorGradientMagnitudeImageFilterIVF33F *":
        """GetPointer(itkVectorGradientMagnitudeImageFilterIVF33F self) -> itkVectorGradientMagnitudeImageFilterIVF33F"""
        return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVectorGradientMagnitudeImageFilterIVF33F

        Create a new object of the class itkVectorGradientMagnitudeImageFilterIVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVectorGradientMagnitudeImageFilterIVF33F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVectorGradientMagnitudeImageFilterIVF33F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVectorGradientMagnitudeImageFilterIVF33F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVectorGradientMagnitudeImageFilterIVF33F.Clone = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_Clone, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GenerateInputRequestedRegion = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GenerateInputRequestedRegion, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetUseImageSpacingOn = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUseImageSpacingOn, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetUseImageSpacingOff = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUseImageSpacingOff, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetUseImageSpacing = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUseImageSpacing, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GetUseImageSpacing = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetUseImageSpacing, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetDerivativeWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetDerivativeWeights, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GetDerivativeWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetDerivativeWeights, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetComponentWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetComponentWeights, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GetComponentWeights = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetComponentWeights, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GetNeighborhoodRadius = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetNeighborhoodRadius, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetNeighborhoodRadius = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetNeighborhoodRadius, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetUsePrincipleComponents = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUsePrincipleComponents, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GetUsePrincipleComponents = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetUsePrincipleComponents, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetUsePrincipleComponentsOn = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUsePrincipleComponentsOn, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.SetUsePrincipleComponentsOff = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_SetUsePrincipleComponentsOff, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F.GetPointer = new_instancemethod(_itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_GetPointer, None, itkVectorGradientMagnitudeImageFilterIVF33F)
itkVectorGradientMagnitudeImageFilterIVF33F_swigregister = _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_swigregister
itkVectorGradientMagnitudeImageFilterIVF33F_swigregister(itkVectorGradientMagnitudeImageFilterIVF33F)

def itkVectorGradientMagnitudeImageFilterIVF33F___New_orig__() -> "itkVectorGradientMagnitudeImageFilterIVF33F_Pointer":
    """itkVectorGradientMagnitudeImageFilterIVF33F___New_orig__() -> itkVectorGradientMagnitudeImageFilterIVF33F_Pointer"""
    return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F___New_orig__()

def itkVectorGradientMagnitudeImageFilterIVF33F_CubicSolver(arg0: 'double *', arg1: 'double *') -> "int":
    """itkVectorGradientMagnitudeImageFilterIVF33F_CubicSolver(double * arg0, double * arg1) -> int"""
    return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_CubicSolver(arg0, arg1)

def itkVectorGradientMagnitudeImageFilterIVF33F_cast(obj: 'itkLightObject') -> "itkVectorGradientMagnitudeImageFilterIVF33F *":
    """itkVectorGradientMagnitudeImageFilterIVF33F_cast(itkLightObject obj) -> itkVectorGradientMagnitudeImageFilterIVF33F"""
    return _itkVectorGradientMagnitudeImageFilterPython.itkVectorGradientMagnitudeImageFilterIVF33F_cast(obj)



