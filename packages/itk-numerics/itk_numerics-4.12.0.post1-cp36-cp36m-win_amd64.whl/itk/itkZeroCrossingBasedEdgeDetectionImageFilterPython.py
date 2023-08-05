# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkZeroCrossingBasedEdgeDetectionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkZeroCrossingBasedEdgeDetectionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkZeroCrossingBasedEdgeDetectionImageFilterPython')
    _itkZeroCrossingBasedEdgeDetectionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkZeroCrossingBasedEdgeDetectionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkZeroCrossingBasedEdgeDetectionImageFilterPython
            return _itkZeroCrossingBasedEdgeDetectionImageFilterPython
        try:
            _mod = imp.load_module('_itkZeroCrossingBasedEdgeDetectionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkZeroCrossingBasedEdgeDetectionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkZeroCrossingBasedEdgeDetectionImageFilterPython
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
import itkImageToImageFilterAPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
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

def itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_New():
  return itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.New()


def itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_New():
  return itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.New()

class itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Pointer"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Pointer":
        """Clone(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Pointer"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Clone(self)


    def GetVariance(self) -> "itkFixedArrayD2 const":
        """GetVariance(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self) -> itkFixedArrayD2"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetVariance(self)


    def GetMaximumError(self) -> "itkFixedArrayD2 const":
        """GetMaximumError(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self) -> itkFixedArrayD2"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetMaximumError(self)


    def GetBackgroundValue(self) -> "float":
        """GetBackgroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self) -> float"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetBackgroundValue(self)


    def SetBackgroundValue(self, _arg: 'float const') -> "void":
        """SetBackgroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self, float const _arg)"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetBackgroundValue(self, _arg)


    def GetForegroundValue(self) -> "float":
        """GetForegroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self) -> float"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetForegroundValue(self)


    def SetForegroundValue(self, _arg: 'float const') -> "void":
        """SetForegroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self, float const _arg)"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetForegroundValue(self, _arg)


    def SetVariance(self, *args) -> "void":
        """
        SetVariance(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self, itkFixedArrayD2 _arg)
        SetVariance(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self, double const v)
        """
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetVariance(self, *args)


    def SetMaximumError(self, *args) -> "void":
        """
        SetMaximumError(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self, itkFixedArrayD2 _arg)
        SetMaximumError(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self, double const v)
        """
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetMaximumError(self, *args)

    OutputEqualityComparableCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_OutputEqualityComparableCheck
    SameDimensionCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SameDimensionCheck
    SameTypeCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SameTypeCheck
    OutputOStreamWritableCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_OutputOStreamWritableCheck
    PixelTypeIsFloatingPointCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_PixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.delete_itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 *":
        """GetPointer(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 self) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2

        Create a new object of the class itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.Clone = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Clone, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.GetVariance = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetVariance, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.GetMaximumError = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetMaximumError, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.GetBackgroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetBackgroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.SetBackgroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetBackgroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.GetForegroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetForegroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.SetForegroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetForegroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.SetVariance = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetVariance, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.SetMaximumError = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_SetMaximumError, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_GetPointer, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_swigregister = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_swigregister
itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_swigregister(itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2)

def itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2___New_orig__() -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Pointer":
    """itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2___New_orig__() -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_Pointer"""
    return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2___New_orig__()

def itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2 *":
    """itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_cast(itkLightObject obj) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2"""
    return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2_cast(obj)

class itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Pointer"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Pointer":
        """Clone(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Pointer"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Clone(self)


    def GetVariance(self) -> "itkFixedArrayD3 const":
        """GetVariance(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self) -> itkFixedArrayD3"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetVariance(self)


    def GetMaximumError(self) -> "itkFixedArrayD3 const":
        """GetMaximumError(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self) -> itkFixedArrayD3"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetMaximumError(self)


    def GetBackgroundValue(self) -> "float":
        """GetBackgroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self) -> float"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetBackgroundValue(self)


    def SetBackgroundValue(self, _arg: 'float const') -> "void":
        """SetBackgroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self, float const _arg)"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetBackgroundValue(self, _arg)


    def GetForegroundValue(self) -> "float":
        """GetForegroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self) -> float"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetForegroundValue(self)


    def SetForegroundValue(self, _arg: 'float const') -> "void":
        """SetForegroundValue(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self, float const _arg)"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetForegroundValue(self, _arg)


    def SetVariance(self, *args) -> "void":
        """
        SetVariance(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self, itkFixedArrayD3 _arg)
        SetVariance(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self, double const v)
        """
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetVariance(self, *args)


    def SetMaximumError(self, *args) -> "void":
        """
        SetMaximumError(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self, itkFixedArrayD3 _arg)
        SetMaximumError(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self, double const v)
        """
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetMaximumError(self, *args)

    OutputEqualityComparableCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_OutputEqualityComparableCheck
    SameDimensionCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SameDimensionCheck
    SameTypeCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SameTypeCheck
    OutputOStreamWritableCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_OutputOStreamWritableCheck
    PixelTypeIsFloatingPointCheck = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_PixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.delete_itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 *":
        """GetPointer(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 self) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3"""
        return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3

        Create a new object of the class itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.Clone = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Clone, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.GetVariance = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetVariance, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.GetMaximumError = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetMaximumError, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.GetBackgroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetBackgroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.SetBackgroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetBackgroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.GetForegroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetForegroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.SetForegroundValue = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetForegroundValue, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.SetVariance = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetVariance, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.SetMaximumError = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_SetMaximumError, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_GetPointer, None, itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_swigregister = _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_swigregister
itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_swigregister(itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3)

def itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3___New_orig__() -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Pointer":
    """itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3___New_orig__() -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_Pointer"""
    return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3___New_orig__()

def itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3 *":
    """itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_cast(itkLightObject obj) -> itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3"""
    return _itkZeroCrossingBasedEdgeDetectionImageFilterPython.itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3_cast(obj)



