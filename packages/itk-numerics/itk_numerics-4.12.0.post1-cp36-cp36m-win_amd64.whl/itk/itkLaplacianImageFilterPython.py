# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLaplacianImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLaplacianImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLaplacianImageFilterPython')
    _itkLaplacianImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLaplacianImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLaplacianImageFilterPython
            return _itkLaplacianImageFilterPython
        try:
            _mod = imp.load_module('_itkLaplacianImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLaplacianImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLaplacianImageFilterPython
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


import itkImageToImageFilterAPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
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

def itkLaplacianImageFilterIF3IF3_New():
  return itkLaplacianImageFilterIF3IF3.New()


def itkLaplacianImageFilterIF2IF2_New():
  return itkLaplacianImageFilterIF2IF2.New()

class itkLaplacianImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkLaplacianImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkLaplacianImageFilterIF2IF2_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianImageFilterIF2IF2_Pointer":
        """Clone(itkLaplacianImageFilterIF2IF2 self) -> itkLaplacianImageFilterIF2IF2_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkLaplacianImageFilterIF2IF2 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GenerateInputRequestedRegion(self)


    def UseImageSpacingOn(self) -> "void":
        """UseImageSpacingOn(itkLaplacianImageFilterIF2IF2 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOn(self)


    def UseImageSpacingOff(self) -> "void":
        """UseImageSpacingOff(itkLaplacianImageFilterIF2IF2 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """SetUseImageSpacing(itkLaplacianImageFilterIF2IF2 self, bool const _arg)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkLaplacianImageFilterIF2IF2 self) -> bool"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetUseImageSpacing(self)

    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SameDimensionCheck
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_InputPixelTypeIsFloatingPointCheck
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_OutputPixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkLaplacianImageFilterIF2IF2"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLaplacianImageFilterIF2IF2 *":
        """GetPointer(itkLaplacianImageFilterIF2IF2 self) -> itkLaplacianImageFilterIF2IF2"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF2IF2

        Create a new object of the class itkLaplacianImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianImageFilterIF2IF2.Clone = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_Clone, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.GenerateInputRequestedRegion = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GenerateInputRequestedRegion, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.UseImageSpacingOn = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOn, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.UseImageSpacingOff = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOff, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.SetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SetUseImageSpacing, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.GetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetUseImageSpacing, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.GetPointer = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetPointer, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2_swigregister = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_swigregister
itkLaplacianImageFilterIF2IF2_swigregister(itkLaplacianImageFilterIF2IF2)

def itkLaplacianImageFilterIF2IF2___New_orig__() -> "itkLaplacianImageFilterIF2IF2_Pointer":
    """itkLaplacianImageFilterIF2IF2___New_orig__() -> itkLaplacianImageFilterIF2IF2_Pointer"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2___New_orig__()

def itkLaplacianImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF2IF2 *":
    """itkLaplacianImageFilterIF2IF2_cast(itkLightObject obj) -> itkLaplacianImageFilterIF2IF2"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_cast(obj)

class itkLaplacianImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkLaplacianImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkLaplacianImageFilterIF3IF3_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianImageFilterIF3IF3_Pointer":
        """Clone(itkLaplacianImageFilterIF3IF3 self) -> itkLaplacianImageFilterIF3IF3_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkLaplacianImageFilterIF3IF3 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GenerateInputRequestedRegion(self)


    def UseImageSpacingOn(self) -> "void":
        """UseImageSpacingOn(itkLaplacianImageFilterIF3IF3 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOn(self)


    def UseImageSpacingOff(self) -> "void":
        """UseImageSpacingOff(itkLaplacianImageFilterIF3IF3 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """SetUseImageSpacing(itkLaplacianImageFilterIF3IF3 self, bool const _arg)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkLaplacianImageFilterIF3IF3 self) -> bool"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetUseImageSpacing(self)

    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SameDimensionCheck
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_InputPixelTypeIsFloatingPointCheck
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_OutputPixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkLaplacianImageFilterIF3IF3"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLaplacianImageFilterIF3IF3 *":
        """GetPointer(itkLaplacianImageFilterIF3IF3 self) -> itkLaplacianImageFilterIF3IF3"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF3IF3

        Create a new object of the class itkLaplacianImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianImageFilterIF3IF3.Clone = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_Clone, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.GenerateInputRequestedRegion = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GenerateInputRequestedRegion, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.UseImageSpacingOn = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOn, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.UseImageSpacingOff = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOff, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.SetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SetUseImageSpacing, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.GetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetUseImageSpacing, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.GetPointer = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetPointer, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3_swigregister = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_swigregister
itkLaplacianImageFilterIF3IF3_swigregister(itkLaplacianImageFilterIF3IF3)

def itkLaplacianImageFilterIF3IF3___New_orig__() -> "itkLaplacianImageFilterIF3IF3_Pointer":
    """itkLaplacianImageFilterIF3IF3___New_orig__() -> itkLaplacianImageFilterIF3IF3_Pointer"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3___New_orig__()

def itkLaplacianImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF3IF3 *":
    """itkLaplacianImageFilterIF3IF3_cast(itkLightObject obj) -> itkLaplacianImageFilterIF3IF3"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_cast(obj)



