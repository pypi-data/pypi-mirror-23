# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDerivativeImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDerivativeImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDerivativeImageFilterPython')
    _itkDerivativeImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDerivativeImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDerivativeImageFilterPython
            return _itkDerivativeImageFilterPython
        try:
            _mod = imp.load_module('_itkDerivativeImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDerivativeImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDerivativeImageFilterPython
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
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import pyBasePython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkSizePython
import itkRGBPixelPython
import itkOffsetPython
import ITKCommonBasePython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkDerivativeImageFilterIF3IF3_New():
  return itkDerivativeImageFilterIF3IF3.New()


def itkDerivativeImageFilterIF2IF2_New():
  return itkDerivativeImageFilterIF2IF2.New()


def itkDerivativeImageFilterISS3ISS3_New():
  return itkDerivativeImageFilterISS3ISS3.New()


def itkDerivativeImageFilterISS2ISS2_New():
  return itkDerivativeImageFilterISS2ISS2.New()

class itkDerivativeImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkDerivativeImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDerivativeImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkDerivativeImageFilterIF2IF2_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDerivativeImageFilterIF2IF2_Pointer":
        """Clone(itkDerivativeImageFilterIF2IF2 self) -> itkDerivativeImageFilterIF2IF2_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_Clone(self)

    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SignedOutputPixelType

    def SetOrder(self, _arg: 'unsigned int const') -> "void":
        """SetOrder(itkDerivativeImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetOrder(self, _arg)


    def GetOrder(self) -> "unsigned int":
        """GetOrder(itkDerivativeImageFilterIF2IF2 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetOrder(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkDerivativeImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetDirection(self, _arg)


    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkDerivativeImageFilterIF2IF2 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetDirection(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkDerivativeImageFilterIF2IF2 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkDerivativeImageFilterIF2IF2 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """SetUseImageSpacing(itkDerivativeImageFilterIF2IF2 self, bool const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkDerivativeImageFilterIF2IF2 self) -> bool"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetUseImageSpacing(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkDerivativeImageFilterIF2IF2 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GenerateInputRequestedRegion(self)

    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkDerivativeImageFilterIF2IF2"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDerivativeImageFilterIF2IF2 *":
        """GetPointer(itkDerivativeImageFilterIF2IF2 self) -> itkDerivativeImageFilterIF2IF2"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterIF2IF2

        Create a new object of the class itkDerivativeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDerivativeImageFilterIF2IF2.Clone = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_Clone, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.SetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetOrder, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.GetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetOrder, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.SetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetDirection, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.GetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetDirection, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.SetUseImageSpacingOn = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacingOn, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.SetUseImageSpacingOff = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacingOff, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.SetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacing, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.GetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetUseImageSpacing, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.GenerateInputRequestedRegion = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GenerateInputRequestedRegion, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2.GetPointer = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetPointer, None, itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2_swigregister = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_swigregister
itkDerivativeImageFilterIF2IF2_swigregister(itkDerivativeImageFilterIF2IF2)

def itkDerivativeImageFilterIF2IF2___New_orig__() -> "itkDerivativeImageFilterIF2IF2_Pointer":
    """itkDerivativeImageFilterIF2IF2___New_orig__() -> itkDerivativeImageFilterIF2IF2_Pointer"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2___New_orig__()

def itkDerivativeImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterIF2IF2 *":
    """itkDerivativeImageFilterIF2IF2_cast(itkLightObject obj) -> itkDerivativeImageFilterIF2IF2"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_cast(obj)

class itkDerivativeImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkDerivativeImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDerivativeImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkDerivativeImageFilterIF3IF3_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDerivativeImageFilterIF3IF3_Pointer":
        """Clone(itkDerivativeImageFilterIF3IF3 self) -> itkDerivativeImageFilterIF3IF3_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_Clone(self)

    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SignedOutputPixelType

    def SetOrder(self, _arg: 'unsigned int const') -> "void":
        """SetOrder(itkDerivativeImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetOrder(self, _arg)


    def GetOrder(self) -> "unsigned int":
        """GetOrder(itkDerivativeImageFilterIF3IF3 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetOrder(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkDerivativeImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetDirection(self, _arg)


    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkDerivativeImageFilterIF3IF3 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetDirection(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkDerivativeImageFilterIF3IF3 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkDerivativeImageFilterIF3IF3 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """SetUseImageSpacing(itkDerivativeImageFilterIF3IF3 self, bool const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkDerivativeImageFilterIF3IF3 self) -> bool"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetUseImageSpacing(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkDerivativeImageFilterIF3IF3 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GenerateInputRequestedRegion(self)

    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkDerivativeImageFilterIF3IF3"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDerivativeImageFilterIF3IF3 *":
        """GetPointer(itkDerivativeImageFilterIF3IF3 self) -> itkDerivativeImageFilterIF3IF3"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterIF3IF3

        Create a new object of the class itkDerivativeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDerivativeImageFilterIF3IF3.Clone = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_Clone, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.SetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetOrder, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.GetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetOrder, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.SetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetDirection, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.GetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetDirection, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.SetUseImageSpacingOn = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacingOn, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.SetUseImageSpacingOff = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacingOff, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.SetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacing, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.GetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetUseImageSpacing, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.GenerateInputRequestedRegion = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GenerateInputRequestedRegion, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3.GetPointer = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetPointer, None, itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3_swigregister = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_swigregister
itkDerivativeImageFilterIF3IF3_swigregister(itkDerivativeImageFilterIF3IF3)

def itkDerivativeImageFilterIF3IF3___New_orig__() -> "itkDerivativeImageFilterIF3IF3_Pointer":
    """itkDerivativeImageFilterIF3IF3___New_orig__() -> itkDerivativeImageFilterIF3IF3_Pointer"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3___New_orig__()

def itkDerivativeImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterIF3IF3 *":
    """itkDerivativeImageFilterIF3IF3_cast(itkLightObject obj) -> itkDerivativeImageFilterIF3IF3"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_cast(obj)

class itkDerivativeImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkDerivativeImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDerivativeImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkDerivativeImageFilterISS2ISS2_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDerivativeImageFilterISS2ISS2_Pointer":
        """Clone(itkDerivativeImageFilterISS2ISS2 self) -> itkDerivativeImageFilterISS2ISS2_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_Clone(self)

    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SignedOutputPixelType

    def SetOrder(self, _arg: 'unsigned int const') -> "void":
        """SetOrder(itkDerivativeImageFilterISS2ISS2 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetOrder(self, _arg)


    def GetOrder(self) -> "unsigned int":
        """GetOrder(itkDerivativeImageFilterISS2ISS2 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetOrder(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkDerivativeImageFilterISS2ISS2 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetDirection(self, _arg)


    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkDerivativeImageFilterISS2ISS2 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetDirection(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkDerivativeImageFilterISS2ISS2 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkDerivativeImageFilterISS2ISS2 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """SetUseImageSpacing(itkDerivativeImageFilterISS2ISS2 self, bool const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkDerivativeImageFilterISS2ISS2 self) -> bool"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetUseImageSpacing(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkDerivativeImageFilterISS2ISS2 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GenerateInputRequestedRegion(self)

    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkDerivativeImageFilterISS2ISS2"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDerivativeImageFilterISS2ISS2 *":
        """GetPointer(itkDerivativeImageFilterISS2ISS2 self) -> itkDerivativeImageFilterISS2ISS2"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterISS2ISS2

        Create a new object of the class itkDerivativeImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDerivativeImageFilterISS2ISS2.Clone = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_Clone, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.SetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetOrder, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.GetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetOrder, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.SetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetDirection, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.GetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetDirection, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.SetUseImageSpacingOn = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacingOn, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.SetUseImageSpacingOff = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacingOff, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.SetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacing, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.GetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetUseImageSpacing, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.GenerateInputRequestedRegion = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GenerateInputRequestedRegion, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetPointer, None, itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2_swigregister = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_swigregister
itkDerivativeImageFilterISS2ISS2_swigregister(itkDerivativeImageFilterISS2ISS2)

def itkDerivativeImageFilterISS2ISS2___New_orig__() -> "itkDerivativeImageFilterISS2ISS2_Pointer":
    """itkDerivativeImageFilterISS2ISS2___New_orig__() -> itkDerivativeImageFilterISS2ISS2_Pointer"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2___New_orig__()

def itkDerivativeImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterISS2ISS2 *":
    """itkDerivativeImageFilterISS2ISS2_cast(itkLightObject obj) -> itkDerivativeImageFilterISS2ISS2"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_cast(obj)

class itkDerivativeImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkDerivativeImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDerivativeImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkDerivativeImageFilterISS3ISS3_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDerivativeImageFilterISS3ISS3_Pointer":
        """Clone(itkDerivativeImageFilterISS3ISS3 self) -> itkDerivativeImageFilterISS3ISS3_Pointer"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_Clone(self)

    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SignedOutputPixelType

    def SetOrder(self, _arg: 'unsigned int const') -> "void":
        """SetOrder(itkDerivativeImageFilterISS3ISS3 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetOrder(self, _arg)


    def GetOrder(self) -> "unsigned int":
        """GetOrder(itkDerivativeImageFilterISS3ISS3 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetOrder(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkDerivativeImageFilterISS3ISS3 self, unsigned int const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetDirection(self, _arg)


    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkDerivativeImageFilterISS3ISS3 self) -> unsigned int"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetDirection(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkDerivativeImageFilterISS3ISS3 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkDerivativeImageFilterISS3ISS3 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """SetUseImageSpacing(itkDerivativeImageFilterISS3ISS3 self, bool const _arg)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkDerivativeImageFilterISS3ISS3 self) -> bool"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetUseImageSpacing(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkDerivativeImageFilterISS3ISS3 self)"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GenerateInputRequestedRegion(self)

    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkDerivativeImageFilterISS3ISS3"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDerivativeImageFilterISS3ISS3 *":
        """GetPointer(itkDerivativeImageFilterISS3ISS3 self) -> itkDerivativeImageFilterISS3ISS3"""
        return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterISS3ISS3

        Create a new object of the class itkDerivativeImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDerivativeImageFilterISS3ISS3.Clone = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_Clone, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.SetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetOrder, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.GetOrder = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetOrder, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.SetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetDirection, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.GetDirection = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetDirection, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.SetUseImageSpacingOn = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacingOn, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.SetUseImageSpacingOff = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacingOff, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.SetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacing, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.GetUseImageSpacing = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetUseImageSpacing, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.GenerateInputRequestedRegion = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GenerateInputRequestedRegion, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetPointer, None, itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3_swigregister = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_swigregister
itkDerivativeImageFilterISS3ISS3_swigregister(itkDerivativeImageFilterISS3ISS3)

def itkDerivativeImageFilterISS3ISS3___New_orig__() -> "itkDerivativeImageFilterISS3ISS3_Pointer":
    """itkDerivativeImageFilterISS3ISS3___New_orig__() -> itkDerivativeImageFilterISS3ISS3_Pointer"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3___New_orig__()

def itkDerivativeImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkDerivativeImageFilterISS3ISS3 *":
    """itkDerivativeImageFilterISS3ISS3_cast(itkLightObject obj) -> itkDerivativeImageFilterISS3ISS3"""
    return _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_cast(obj)



