# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCannyEdgeDetectionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkCannyEdgeDetectionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkCannyEdgeDetectionImageFilterPython')
    _itkCannyEdgeDetectionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCannyEdgeDetectionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCannyEdgeDetectionImageFilterPython
            return _itkCannyEdgeDetectionImageFilterPython
        try:
            _mod = imp.load_module('_itkCannyEdgeDetectionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkCannyEdgeDetectionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCannyEdgeDetectionImageFilterPython
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


import itkFixedArrayPython
import pyBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageToImageFilterAPython
import itkImageRegionPython
import ITKCommonBasePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkCannyEdgeDetectionImageFilterIF3IF3_New():
  return itkCannyEdgeDetectionImageFilterIF3IF3.New()


def itkCannyEdgeDetectionImageFilterIF2IF2_New():
  return itkCannyEdgeDetectionImageFilterIF2IF2.New()

class itkCannyEdgeDetectionImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkCannyEdgeDetectionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCannyEdgeDetectionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkCannyEdgeDetectionImageFilterIF2IF2_Pointer"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCannyEdgeDetectionImageFilterIF2IF2_Pointer":
        """Clone(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> itkCannyEdgeDetectionImageFilterIF2IF2_Pointer"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_Clone(self)


    def GetVariance(self) -> "itkFixedArrayD2 const":
        """GetVariance(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> itkFixedArrayD2"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetVariance(self)


    def GetMaximumError(self) -> "itkFixedArrayD2 const":
        """GetMaximumError(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> itkFixedArrayD2"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetMaximumError(self)


    def SetVariance(self, *args) -> "void":
        """
        SetVariance(itkCannyEdgeDetectionImageFilterIF2IF2 self, itkFixedArrayD2 _arg)
        SetVariance(itkCannyEdgeDetectionImageFilterIF2IF2 self, double const v)
        """
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetVariance(self, *args)


    def SetMaximumError(self, *args) -> "void":
        """
        SetMaximumError(itkCannyEdgeDetectionImageFilterIF2IF2 self, itkFixedArrayD2 _arg)
        SetMaximumError(itkCannyEdgeDetectionImageFilterIF2IF2 self, double const v)
        """
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetMaximumError(self, *args)


    def SetUpperThreshold(self, _arg: 'float const') -> "void":
        """SetUpperThreshold(itkCannyEdgeDetectionImageFilterIF2IF2 self, float const _arg)"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetUpperThreshold(self, _arg)


    def GetUpperThreshold(self) -> "float":
        """GetUpperThreshold(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> float"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetUpperThreshold(self)


    def SetLowerThreshold(self, _arg: 'float const') -> "void":
        """SetLowerThreshold(itkCannyEdgeDetectionImageFilterIF2IF2 self, float const _arg)"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetLowerThreshold(self, _arg)


    def GetLowerThreshold(self) -> "float":
        """GetLowerThreshold(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> float"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetLowerThreshold(self)


    def GetNonMaximumSuppressionImage(self) -> "itkImageF2 *":
        """GetNonMaximumSuppressionImage(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> itkImageF2"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetNonMaximumSuppressionImage(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkCannyEdgeDetectionImageFilterIF2IF2 self)"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GenerateInputRequestedRegion(self)

    InputHasNumericTraitsCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_InputHasNumericTraitsCheck
    OutputHasNumericTraitsCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_OutputHasNumericTraitsCheck
    SameDimensionCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SameDimensionCheck
    InputIsFloatingPointCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_InputIsFloatingPointCheck
    OutputIsFloatingPointCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkCannyEdgeDetectionImageFilterPython.delete_itkCannyEdgeDetectionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkCannyEdgeDetectionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkCannyEdgeDetectionImageFilterIF2IF2"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkCannyEdgeDetectionImageFilterIF2IF2 *":
        """GetPointer(itkCannyEdgeDetectionImageFilterIF2IF2 self) -> itkCannyEdgeDetectionImageFilterIF2IF2"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCannyEdgeDetectionImageFilterIF2IF2

        Create a new object of the class itkCannyEdgeDetectionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCannyEdgeDetectionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCannyEdgeDetectionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCannyEdgeDetectionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCannyEdgeDetectionImageFilterIF2IF2.Clone = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_Clone, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GetVariance = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetVariance, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GetMaximumError = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetMaximumError, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.SetVariance = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetVariance, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.SetMaximumError = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetMaximumError, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.SetUpperThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetUpperThreshold, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GetUpperThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetUpperThreshold, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.SetLowerThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_SetLowerThreshold, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GetLowerThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetLowerThreshold, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GetNonMaximumSuppressionImage = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetNonMaximumSuppressionImage, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GenerateInputRequestedRegion = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GenerateInputRequestedRegion, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_GetPointer, None, itkCannyEdgeDetectionImageFilterIF2IF2)
itkCannyEdgeDetectionImageFilterIF2IF2_swigregister = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_swigregister
itkCannyEdgeDetectionImageFilterIF2IF2_swigregister(itkCannyEdgeDetectionImageFilterIF2IF2)

def itkCannyEdgeDetectionImageFilterIF2IF2___New_orig__() -> "itkCannyEdgeDetectionImageFilterIF2IF2_Pointer":
    """itkCannyEdgeDetectionImageFilterIF2IF2___New_orig__() -> itkCannyEdgeDetectionImageFilterIF2IF2_Pointer"""
    return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2___New_orig__()

def itkCannyEdgeDetectionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkCannyEdgeDetectionImageFilterIF2IF2 *":
    """itkCannyEdgeDetectionImageFilterIF2IF2_cast(itkLightObject obj) -> itkCannyEdgeDetectionImageFilterIF2IF2"""
    return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF2IF2_cast(obj)

class itkCannyEdgeDetectionImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkCannyEdgeDetectionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCannyEdgeDetectionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkCannyEdgeDetectionImageFilterIF3IF3_Pointer"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCannyEdgeDetectionImageFilterIF3IF3_Pointer":
        """Clone(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> itkCannyEdgeDetectionImageFilterIF3IF3_Pointer"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_Clone(self)


    def GetVariance(self) -> "itkFixedArrayD3 const":
        """GetVariance(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> itkFixedArrayD3"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetVariance(self)


    def GetMaximumError(self) -> "itkFixedArrayD3 const":
        """GetMaximumError(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> itkFixedArrayD3"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetMaximumError(self)


    def SetVariance(self, *args) -> "void":
        """
        SetVariance(itkCannyEdgeDetectionImageFilterIF3IF3 self, itkFixedArrayD3 _arg)
        SetVariance(itkCannyEdgeDetectionImageFilterIF3IF3 self, double const v)
        """
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetVariance(self, *args)


    def SetMaximumError(self, *args) -> "void":
        """
        SetMaximumError(itkCannyEdgeDetectionImageFilterIF3IF3 self, itkFixedArrayD3 _arg)
        SetMaximumError(itkCannyEdgeDetectionImageFilterIF3IF3 self, double const v)
        """
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetMaximumError(self, *args)


    def SetUpperThreshold(self, _arg: 'float const') -> "void":
        """SetUpperThreshold(itkCannyEdgeDetectionImageFilterIF3IF3 self, float const _arg)"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetUpperThreshold(self, _arg)


    def GetUpperThreshold(self) -> "float":
        """GetUpperThreshold(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> float"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetUpperThreshold(self)


    def SetLowerThreshold(self, _arg: 'float const') -> "void":
        """SetLowerThreshold(itkCannyEdgeDetectionImageFilterIF3IF3 self, float const _arg)"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetLowerThreshold(self, _arg)


    def GetLowerThreshold(self) -> "float":
        """GetLowerThreshold(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> float"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetLowerThreshold(self)


    def GetNonMaximumSuppressionImage(self) -> "itkImageF3 *":
        """GetNonMaximumSuppressionImage(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> itkImageF3"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetNonMaximumSuppressionImage(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkCannyEdgeDetectionImageFilterIF3IF3 self)"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GenerateInputRequestedRegion(self)

    InputHasNumericTraitsCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_InputHasNumericTraitsCheck
    OutputHasNumericTraitsCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_OutputHasNumericTraitsCheck
    SameDimensionCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SameDimensionCheck
    InputIsFloatingPointCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_InputIsFloatingPointCheck
    OutputIsFloatingPointCheck = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkCannyEdgeDetectionImageFilterPython.delete_itkCannyEdgeDetectionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkCannyEdgeDetectionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkCannyEdgeDetectionImageFilterIF3IF3"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkCannyEdgeDetectionImageFilterIF3IF3 *":
        """GetPointer(itkCannyEdgeDetectionImageFilterIF3IF3 self) -> itkCannyEdgeDetectionImageFilterIF3IF3"""
        return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCannyEdgeDetectionImageFilterIF3IF3

        Create a new object of the class itkCannyEdgeDetectionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCannyEdgeDetectionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCannyEdgeDetectionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCannyEdgeDetectionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCannyEdgeDetectionImageFilterIF3IF3.Clone = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_Clone, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GetVariance = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetVariance, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GetMaximumError = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetMaximumError, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.SetVariance = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetVariance, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.SetMaximumError = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetMaximumError, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.SetUpperThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetUpperThreshold, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GetUpperThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetUpperThreshold, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.SetLowerThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_SetLowerThreshold, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GetLowerThreshold = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetLowerThreshold, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GetNonMaximumSuppressionImage = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetNonMaximumSuppressionImage, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GenerateInputRequestedRegion = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GenerateInputRequestedRegion, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_GetPointer, None, itkCannyEdgeDetectionImageFilterIF3IF3)
itkCannyEdgeDetectionImageFilterIF3IF3_swigregister = _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_swigregister
itkCannyEdgeDetectionImageFilterIF3IF3_swigregister(itkCannyEdgeDetectionImageFilterIF3IF3)

def itkCannyEdgeDetectionImageFilterIF3IF3___New_orig__() -> "itkCannyEdgeDetectionImageFilterIF3IF3_Pointer":
    """itkCannyEdgeDetectionImageFilterIF3IF3___New_orig__() -> itkCannyEdgeDetectionImageFilterIF3IF3_Pointer"""
    return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3___New_orig__()

def itkCannyEdgeDetectionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkCannyEdgeDetectionImageFilterIF3IF3 *":
    """itkCannyEdgeDetectionImageFilterIF3IF3_cast(itkLightObject obj) -> itkCannyEdgeDetectionImageFilterIF3IF3"""
    return _itkCannyEdgeDetectionImageFilterPython.itkCannyEdgeDetectionImageFilterIF3IF3_cast(obj)



