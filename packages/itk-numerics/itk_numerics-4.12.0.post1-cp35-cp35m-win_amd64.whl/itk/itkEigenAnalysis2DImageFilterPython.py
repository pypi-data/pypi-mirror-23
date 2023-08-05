# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkEigenAnalysis2DImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkEigenAnalysis2DImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkEigenAnalysis2DImageFilterPython')
    _itkEigenAnalysis2DImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkEigenAnalysis2DImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkEigenAnalysis2DImageFilterPython
            return _itkEigenAnalysis2DImageFilterPython
        try:
            _mod = imp.load_module('_itkEigenAnalysis2DImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkEigenAnalysis2DImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkEigenAnalysis2DImageFilterPython
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
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
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
import ITKCommonBasePython
import itkImageRegionPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkEigenAnalysis2DImageFilterIF2IF2IVF42_New():
  return itkEigenAnalysis2DImageFilterIF2IF2IVF42.New()


def itkEigenAnalysis2DImageFilterIF2IF2IVF32_New():
  return itkEigenAnalysis2DImageFilterIF2IF2IVF32.New()


def itkEigenAnalysis2DImageFilterIF2IF2IVF22_New():
  return itkEigenAnalysis2DImageFilterIF2IF2IVF22.New()

class itkEigenAnalysis2DImageFilterIF2IF2IVF22(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkEigenAnalysis2DImageFilterIF2IF2IVF22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEigenAnalysis2DImageFilterIF2IF2IVF22_Pointer":
        """__New_orig__() -> itkEigenAnalysis2DImageFilterIF2IF2IVF22_Pointer"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEigenAnalysis2DImageFilterIF2IF2IVF22_Pointer":
        """Clone(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self) -> itkEigenAnalysis2DImageFilterIF2IF2IVF22_Pointer"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_Clone(self)


    def SetInput1(self, image1: 'itkImageF2') -> "void":
        """SetInput1(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self, itkImageF2 image1)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput1(self, image1)


    def SetInput2(self, image2: 'itkImageF2') -> "void":
        """SetInput2(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self, itkImageF2 image2)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput2(self, image2)


    def SetInput3(self, image3: 'itkImageF2') -> "void":
        """SetInput3(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self, itkImageF2 image3)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput3(self, image3)


    def GetMaxEigenValue(self) -> "itkImageF2 *":
        """GetMaxEigenValue(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self) -> itkImageF2"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMaxEigenValue(self)


    def GetMinEigenValue(self) -> "itkImageF2 *":
        """GetMinEigenValue(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self) -> itkImageF2"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMinEigenValue(self)


    def GetMaxEigenVector(self) -> "itkImageVF22 *":
        """GetMaxEigenVector(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self) -> itkImageVF22"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMaxEigenVector(self)

    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_VectorComponentHasNumericTraitsCheck
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterIF2IF2IVF22

    def cast(obj: 'itkLightObject') -> "itkEigenAnalysis2DImageFilterIF2IF2IVF22 *":
        """cast(itkLightObject obj) -> itkEigenAnalysis2DImageFilterIF2IF2IVF22"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkEigenAnalysis2DImageFilterIF2IF2IVF22 *":
        """GetPointer(itkEigenAnalysis2DImageFilterIF2IF2IVF22 self) -> itkEigenAnalysis2DImageFilterIF2IF2IVF22"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterIF2IF2IVF22

        Create a new object of the class itkEigenAnalysis2DImageFilterIF2IF2IVF22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterIF2IF2IVF22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterIF2IF2IVF22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterIF2IF2IVF22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEigenAnalysis2DImageFilterIF2IF2IVF22.Clone = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_Clone, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.SetInput1 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput1, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.SetInput2 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput2, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.SetInput3 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput3, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.GetMaxEigenValue = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMaxEigenValue, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.GetMinEigenValue = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMinEigenValue, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.GetMaxEigenVector = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMaxEigenVector, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22.GetPointer = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetPointer, None, itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22_swigregister = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_swigregister
itkEigenAnalysis2DImageFilterIF2IF2IVF22_swigregister(itkEigenAnalysis2DImageFilterIF2IF2IVF22)

def itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__() -> "itkEigenAnalysis2DImageFilterIF2IF2IVF22_Pointer":
    """itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__() -> itkEigenAnalysis2DImageFilterIF2IF2IVF22_Pointer"""
    return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__()

def itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast(obj: 'itkLightObject') -> "itkEigenAnalysis2DImageFilterIF2IF2IVF22 *":
    """itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast(itkLightObject obj) -> itkEigenAnalysis2DImageFilterIF2IF2IVF22"""
    return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast(obj)

class itkEigenAnalysis2DImageFilterIF2IF2IVF32(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkEigenAnalysis2DImageFilterIF2IF2IVF32 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEigenAnalysis2DImageFilterIF2IF2IVF32_Pointer":
        """__New_orig__() -> itkEigenAnalysis2DImageFilterIF2IF2IVF32_Pointer"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEigenAnalysis2DImageFilterIF2IF2IVF32_Pointer":
        """Clone(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self) -> itkEigenAnalysis2DImageFilterIF2IF2IVF32_Pointer"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_Clone(self)


    def SetInput1(self, image1: 'itkImageF2') -> "void":
        """SetInput1(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self, itkImageF2 image1)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput1(self, image1)


    def SetInput2(self, image2: 'itkImageF2') -> "void":
        """SetInput2(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self, itkImageF2 image2)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput2(self, image2)


    def SetInput3(self, image3: 'itkImageF2') -> "void":
        """SetInput3(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self, itkImageF2 image3)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput3(self, image3)


    def GetMaxEigenValue(self) -> "itkImageF2 *":
        """GetMaxEigenValue(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self) -> itkImageF2"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMaxEigenValue(self)


    def GetMinEigenValue(self) -> "itkImageF2 *":
        """GetMinEigenValue(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self) -> itkImageF2"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMinEigenValue(self)


    def GetMaxEigenVector(self) -> "itkImageVF32 *":
        """GetMaxEigenVector(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self) -> itkImageVF32"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMaxEigenVector(self)

    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_VectorComponentHasNumericTraitsCheck
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterIF2IF2IVF32

    def cast(obj: 'itkLightObject') -> "itkEigenAnalysis2DImageFilterIF2IF2IVF32 *":
        """cast(itkLightObject obj) -> itkEigenAnalysis2DImageFilterIF2IF2IVF32"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkEigenAnalysis2DImageFilterIF2IF2IVF32 *":
        """GetPointer(itkEigenAnalysis2DImageFilterIF2IF2IVF32 self) -> itkEigenAnalysis2DImageFilterIF2IF2IVF32"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterIF2IF2IVF32

        Create a new object of the class itkEigenAnalysis2DImageFilterIF2IF2IVF32 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterIF2IF2IVF32.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterIF2IF2IVF32.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterIF2IF2IVF32.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEigenAnalysis2DImageFilterIF2IF2IVF32.Clone = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_Clone, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.SetInput1 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput1, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.SetInput2 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput2, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.SetInput3 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput3, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.GetMaxEigenValue = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMaxEigenValue, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.GetMinEigenValue = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMinEigenValue, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.GetMaxEigenVector = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMaxEigenVector, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32.GetPointer = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetPointer, None, itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32_swigregister = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_swigregister
itkEigenAnalysis2DImageFilterIF2IF2IVF32_swigregister(itkEigenAnalysis2DImageFilterIF2IF2IVF32)

def itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__() -> "itkEigenAnalysis2DImageFilterIF2IF2IVF32_Pointer":
    """itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__() -> itkEigenAnalysis2DImageFilterIF2IF2IVF32_Pointer"""
    return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__()

def itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast(obj: 'itkLightObject') -> "itkEigenAnalysis2DImageFilterIF2IF2IVF32 *":
    """itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast(itkLightObject obj) -> itkEigenAnalysis2DImageFilterIF2IF2IVF32"""
    return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast(obj)

class itkEigenAnalysis2DImageFilterIF2IF2IVF42(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkEigenAnalysis2DImageFilterIF2IF2IVF42 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEigenAnalysis2DImageFilterIF2IF2IVF42_Pointer":
        """__New_orig__() -> itkEigenAnalysis2DImageFilterIF2IF2IVF42_Pointer"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEigenAnalysis2DImageFilterIF2IF2IVF42_Pointer":
        """Clone(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self) -> itkEigenAnalysis2DImageFilterIF2IF2IVF42_Pointer"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_Clone(self)


    def SetInput1(self, image1: 'itkImageF2') -> "void":
        """SetInput1(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self, itkImageF2 image1)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput1(self, image1)


    def SetInput2(self, image2: 'itkImageF2') -> "void":
        """SetInput2(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self, itkImageF2 image2)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput2(self, image2)


    def SetInput3(self, image3: 'itkImageF2') -> "void":
        """SetInput3(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self, itkImageF2 image3)"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput3(self, image3)


    def GetMaxEigenValue(self) -> "itkImageF2 *":
        """GetMaxEigenValue(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self) -> itkImageF2"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMaxEigenValue(self)


    def GetMinEigenValue(self) -> "itkImageF2 *":
        """GetMinEigenValue(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self) -> itkImageF2"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMinEigenValue(self)


    def GetMaxEigenVector(self) -> "itkImageVF42 *":
        """GetMaxEigenVector(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self) -> itkImageVF42"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMaxEigenVector(self)

    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_VectorComponentHasNumericTraitsCheck
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterIF2IF2IVF42

    def cast(obj: 'itkLightObject') -> "itkEigenAnalysis2DImageFilterIF2IF2IVF42 *":
        """cast(itkLightObject obj) -> itkEigenAnalysis2DImageFilterIF2IF2IVF42"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkEigenAnalysis2DImageFilterIF2IF2IVF42 *":
        """GetPointer(itkEigenAnalysis2DImageFilterIF2IF2IVF42 self) -> itkEigenAnalysis2DImageFilterIF2IF2IVF42"""
        return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterIF2IF2IVF42

        Create a new object of the class itkEigenAnalysis2DImageFilterIF2IF2IVF42 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterIF2IF2IVF42.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterIF2IF2IVF42.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterIF2IF2IVF42.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEigenAnalysis2DImageFilterIF2IF2IVF42.Clone = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_Clone, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.SetInput1 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput1, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.SetInput2 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput2, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.SetInput3 = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput3, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.GetMaxEigenValue = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMaxEigenValue, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.GetMinEigenValue = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMinEigenValue, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.GetMaxEigenVector = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMaxEigenVector, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42.GetPointer = new_instancemethod(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetPointer, None, itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42_swigregister = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_swigregister
itkEigenAnalysis2DImageFilterIF2IF2IVF42_swigregister(itkEigenAnalysis2DImageFilterIF2IF2IVF42)

def itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__() -> "itkEigenAnalysis2DImageFilterIF2IF2IVF42_Pointer":
    """itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__() -> itkEigenAnalysis2DImageFilterIF2IF2IVF42_Pointer"""
    return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__()

def itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast(obj: 'itkLightObject') -> "itkEigenAnalysis2DImageFilterIF2IF2IVF42 *":
    """itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast(itkLightObject obj) -> itkEigenAnalysis2DImageFilterIF2IF2IVF42"""
    return _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast(obj)



