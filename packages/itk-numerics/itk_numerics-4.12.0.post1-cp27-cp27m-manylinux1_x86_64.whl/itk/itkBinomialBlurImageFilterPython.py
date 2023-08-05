# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinomialBlurImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinomialBlurImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinomialBlurImageFilterPython')
    _itkBinomialBlurImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinomialBlurImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinomialBlurImageFilterPython
            return _itkBinomialBlurImageFilterPython
        try:
            _mod = imp.load_module('_itkBinomialBlurImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinomialBlurImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinomialBlurImageFilterPython
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
import itkImagePython
import stdcomplexPython
import pyBasePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkBinomialBlurImageFilterIF3IF3_New():
  return itkBinomialBlurImageFilterIF3IF3.New()


def itkBinomialBlurImageFilterIF2IF2_New():
  return itkBinomialBlurImageFilterIF2IF2.New()


def itkBinomialBlurImageFilterIUC3IUC3_New():
  return itkBinomialBlurImageFilterIUC3IUC3.New()


def itkBinomialBlurImageFilterIUC2IUC2_New():
  return itkBinomialBlurImageFilterIUC2IUC2.New()


def itkBinomialBlurImageFilterISS3ISS3_New():
  return itkBinomialBlurImageFilterISS3ISS3.New()


def itkBinomialBlurImageFilterISS2ISS2_New():
  return itkBinomialBlurImageFilterISS2ISS2.New()

class itkBinomialBlurImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkBinomialBlurImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinomialBlurImageFilterIF2IF2_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinomialBlurImageFilterIF2IF2 self) -> itkBinomialBlurImageFilterIF2IF2_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_Clone(self)


    def SetRepetitions(self, _arg):
        """SetRepetitions(itkBinomialBlurImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_SetRepetitions(self, _arg)


    def GetRepetitions(self):
        """GetRepetitions(itkBinomialBlurImageFilterIF2IF2 self) -> unsigned int"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_GetRepetitions(self)


    def GenerateInputRequestedRegion(self):
        """GenerateInputRequestedRegion(itkBinomialBlurImageFilterIF2IF2 self)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_SameDimensionCheck
    InputConvertibleToDoubleCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkBinomialBlurImageFilterPython.delete_itkBinomialBlurImageFilterIF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinomialBlurImageFilterIF2IF2"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinomialBlurImageFilterIF2IF2 self) -> itkBinomialBlurImageFilterIF2IF2"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinomialBlurImageFilterIF2IF2

        Create a new object of the class itkBinomialBlurImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinomialBlurImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinomialBlurImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinomialBlurImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinomialBlurImageFilterIF2IF2.Clone = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_Clone, None, itkBinomialBlurImageFilterIF2IF2)
itkBinomialBlurImageFilterIF2IF2.SetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_SetRepetitions, None, itkBinomialBlurImageFilterIF2IF2)
itkBinomialBlurImageFilterIF2IF2.GetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_GetRepetitions, None, itkBinomialBlurImageFilterIF2IF2)
itkBinomialBlurImageFilterIF2IF2.GenerateInputRequestedRegion = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_GenerateInputRequestedRegion, None, itkBinomialBlurImageFilterIF2IF2)
itkBinomialBlurImageFilterIF2IF2.GetPointer = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_GetPointer, None, itkBinomialBlurImageFilterIF2IF2)
itkBinomialBlurImageFilterIF2IF2_swigregister = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_swigregister
itkBinomialBlurImageFilterIF2IF2_swigregister(itkBinomialBlurImageFilterIF2IF2)

def itkBinomialBlurImageFilterIF2IF2___New_orig__():
    """itkBinomialBlurImageFilterIF2IF2___New_orig__() -> itkBinomialBlurImageFilterIF2IF2_Pointer"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2___New_orig__()

def itkBinomialBlurImageFilterIF2IF2_cast(obj):
    """itkBinomialBlurImageFilterIF2IF2_cast(itkLightObject obj) -> itkBinomialBlurImageFilterIF2IF2"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF2IF2_cast(obj)

class itkBinomialBlurImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkBinomialBlurImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinomialBlurImageFilterIF3IF3_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinomialBlurImageFilterIF3IF3 self) -> itkBinomialBlurImageFilterIF3IF3_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_Clone(self)


    def SetRepetitions(self, _arg):
        """SetRepetitions(itkBinomialBlurImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_SetRepetitions(self, _arg)


    def GetRepetitions(self):
        """GetRepetitions(itkBinomialBlurImageFilterIF3IF3 self) -> unsigned int"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_GetRepetitions(self)


    def GenerateInputRequestedRegion(self):
        """GenerateInputRequestedRegion(itkBinomialBlurImageFilterIF3IF3 self)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_SameDimensionCheck
    InputConvertibleToDoubleCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkBinomialBlurImageFilterPython.delete_itkBinomialBlurImageFilterIF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinomialBlurImageFilterIF3IF3"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinomialBlurImageFilterIF3IF3 self) -> itkBinomialBlurImageFilterIF3IF3"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinomialBlurImageFilterIF3IF3

        Create a new object of the class itkBinomialBlurImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinomialBlurImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinomialBlurImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinomialBlurImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinomialBlurImageFilterIF3IF3.Clone = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_Clone, None, itkBinomialBlurImageFilterIF3IF3)
itkBinomialBlurImageFilterIF3IF3.SetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_SetRepetitions, None, itkBinomialBlurImageFilterIF3IF3)
itkBinomialBlurImageFilterIF3IF3.GetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_GetRepetitions, None, itkBinomialBlurImageFilterIF3IF3)
itkBinomialBlurImageFilterIF3IF3.GenerateInputRequestedRegion = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_GenerateInputRequestedRegion, None, itkBinomialBlurImageFilterIF3IF3)
itkBinomialBlurImageFilterIF3IF3.GetPointer = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_GetPointer, None, itkBinomialBlurImageFilterIF3IF3)
itkBinomialBlurImageFilterIF3IF3_swigregister = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_swigregister
itkBinomialBlurImageFilterIF3IF3_swigregister(itkBinomialBlurImageFilterIF3IF3)

def itkBinomialBlurImageFilterIF3IF3___New_orig__():
    """itkBinomialBlurImageFilterIF3IF3___New_orig__() -> itkBinomialBlurImageFilterIF3IF3_Pointer"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3___New_orig__()

def itkBinomialBlurImageFilterIF3IF3_cast(obj):
    """itkBinomialBlurImageFilterIF3IF3_cast(itkLightObject obj) -> itkBinomialBlurImageFilterIF3IF3"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIF3IF3_cast(obj)

class itkBinomialBlurImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkBinomialBlurImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinomialBlurImageFilterISS2ISS2_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinomialBlurImageFilterISS2ISS2 self) -> itkBinomialBlurImageFilterISS2ISS2_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_Clone(self)


    def SetRepetitions(self, _arg):
        """SetRepetitions(itkBinomialBlurImageFilterISS2ISS2 self, unsigned int const _arg)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_SetRepetitions(self, _arg)


    def GetRepetitions(self):
        """GetRepetitions(itkBinomialBlurImageFilterISS2ISS2 self) -> unsigned int"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_GetRepetitions(self)


    def GenerateInputRequestedRegion(self):
        """GenerateInputRequestedRegion(itkBinomialBlurImageFilterISS2ISS2 self)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_SameDimensionCheck
    InputConvertibleToDoubleCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkBinomialBlurImageFilterPython.delete_itkBinomialBlurImageFilterISS2ISS2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinomialBlurImageFilterISS2ISS2"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinomialBlurImageFilterISS2ISS2 self) -> itkBinomialBlurImageFilterISS2ISS2"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinomialBlurImageFilterISS2ISS2

        Create a new object of the class itkBinomialBlurImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinomialBlurImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinomialBlurImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinomialBlurImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinomialBlurImageFilterISS2ISS2.Clone = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_Clone, None, itkBinomialBlurImageFilterISS2ISS2)
itkBinomialBlurImageFilterISS2ISS2.SetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_SetRepetitions, None, itkBinomialBlurImageFilterISS2ISS2)
itkBinomialBlurImageFilterISS2ISS2.GetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_GetRepetitions, None, itkBinomialBlurImageFilterISS2ISS2)
itkBinomialBlurImageFilterISS2ISS2.GenerateInputRequestedRegion = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_GenerateInputRequestedRegion, None, itkBinomialBlurImageFilterISS2ISS2)
itkBinomialBlurImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_GetPointer, None, itkBinomialBlurImageFilterISS2ISS2)
itkBinomialBlurImageFilterISS2ISS2_swigregister = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_swigregister
itkBinomialBlurImageFilterISS2ISS2_swigregister(itkBinomialBlurImageFilterISS2ISS2)

def itkBinomialBlurImageFilterISS2ISS2___New_orig__():
    """itkBinomialBlurImageFilterISS2ISS2___New_orig__() -> itkBinomialBlurImageFilterISS2ISS2_Pointer"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2___New_orig__()

def itkBinomialBlurImageFilterISS2ISS2_cast(obj):
    """itkBinomialBlurImageFilterISS2ISS2_cast(itkLightObject obj) -> itkBinomialBlurImageFilterISS2ISS2"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS2ISS2_cast(obj)

class itkBinomialBlurImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkBinomialBlurImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinomialBlurImageFilterISS3ISS3_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinomialBlurImageFilterISS3ISS3 self) -> itkBinomialBlurImageFilterISS3ISS3_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_Clone(self)


    def SetRepetitions(self, _arg):
        """SetRepetitions(itkBinomialBlurImageFilterISS3ISS3 self, unsigned int const _arg)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_SetRepetitions(self, _arg)


    def GetRepetitions(self):
        """GetRepetitions(itkBinomialBlurImageFilterISS3ISS3 self) -> unsigned int"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_GetRepetitions(self)


    def GenerateInputRequestedRegion(self):
        """GenerateInputRequestedRegion(itkBinomialBlurImageFilterISS3ISS3 self)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_SameDimensionCheck
    InputConvertibleToDoubleCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkBinomialBlurImageFilterPython.delete_itkBinomialBlurImageFilterISS3ISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinomialBlurImageFilterISS3ISS3"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinomialBlurImageFilterISS3ISS3 self) -> itkBinomialBlurImageFilterISS3ISS3"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinomialBlurImageFilterISS3ISS3

        Create a new object of the class itkBinomialBlurImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinomialBlurImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinomialBlurImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinomialBlurImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinomialBlurImageFilterISS3ISS3.Clone = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_Clone, None, itkBinomialBlurImageFilterISS3ISS3)
itkBinomialBlurImageFilterISS3ISS3.SetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_SetRepetitions, None, itkBinomialBlurImageFilterISS3ISS3)
itkBinomialBlurImageFilterISS3ISS3.GetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_GetRepetitions, None, itkBinomialBlurImageFilterISS3ISS3)
itkBinomialBlurImageFilterISS3ISS3.GenerateInputRequestedRegion = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_GenerateInputRequestedRegion, None, itkBinomialBlurImageFilterISS3ISS3)
itkBinomialBlurImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_GetPointer, None, itkBinomialBlurImageFilterISS3ISS3)
itkBinomialBlurImageFilterISS3ISS3_swigregister = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_swigregister
itkBinomialBlurImageFilterISS3ISS3_swigregister(itkBinomialBlurImageFilterISS3ISS3)

def itkBinomialBlurImageFilterISS3ISS3___New_orig__():
    """itkBinomialBlurImageFilterISS3ISS3___New_orig__() -> itkBinomialBlurImageFilterISS3ISS3_Pointer"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3___New_orig__()

def itkBinomialBlurImageFilterISS3ISS3_cast(obj):
    """itkBinomialBlurImageFilterISS3ISS3_cast(itkLightObject obj) -> itkBinomialBlurImageFilterISS3ISS3"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterISS3ISS3_cast(obj)

class itkBinomialBlurImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkBinomialBlurImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinomialBlurImageFilterIUC2IUC2_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinomialBlurImageFilterIUC2IUC2 self) -> itkBinomialBlurImageFilterIUC2IUC2_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_Clone(self)


    def SetRepetitions(self, _arg):
        """SetRepetitions(itkBinomialBlurImageFilterIUC2IUC2 self, unsigned int const _arg)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_SetRepetitions(self, _arg)


    def GetRepetitions(self):
        """GetRepetitions(itkBinomialBlurImageFilterIUC2IUC2 self) -> unsigned int"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_GetRepetitions(self)


    def GenerateInputRequestedRegion(self):
        """GenerateInputRequestedRegion(itkBinomialBlurImageFilterIUC2IUC2 self)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_SameDimensionCheck
    InputConvertibleToDoubleCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkBinomialBlurImageFilterPython.delete_itkBinomialBlurImageFilterIUC2IUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinomialBlurImageFilterIUC2IUC2"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinomialBlurImageFilterIUC2IUC2 self) -> itkBinomialBlurImageFilterIUC2IUC2"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinomialBlurImageFilterIUC2IUC2

        Create a new object of the class itkBinomialBlurImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinomialBlurImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinomialBlurImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinomialBlurImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinomialBlurImageFilterIUC2IUC2.Clone = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_Clone, None, itkBinomialBlurImageFilterIUC2IUC2)
itkBinomialBlurImageFilterIUC2IUC2.SetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_SetRepetitions, None, itkBinomialBlurImageFilterIUC2IUC2)
itkBinomialBlurImageFilterIUC2IUC2.GetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_GetRepetitions, None, itkBinomialBlurImageFilterIUC2IUC2)
itkBinomialBlurImageFilterIUC2IUC2.GenerateInputRequestedRegion = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_GenerateInputRequestedRegion, None, itkBinomialBlurImageFilterIUC2IUC2)
itkBinomialBlurImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_GetPointer, None, itkBinomialBlurImageFilterIUC2IUC2)
itkBinomialBlurImageFilterIUC2IUC2_swigregister = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_swigregister
itkBinomialBlurImageFilterIUC2IUC2_swigregister(itkBinomialBlurImageFilterIUC2IUC2)

def itkBinomialBlurImageFilterIUC2IUC2___New_orig__():
    """itkBinomialBlurImageFilterIUC2IUC2___New_orig__() -> itkBinomialBlurImageFilterIUC2IUC2_Pointer"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2___New_orig__()

def itkBinomialBlurImageFilterIUC2IUC2_cast(obj):
    """itkBinomialBlurImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkBinomialBlurImageFilterIUC2IUC2"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC2IUC2_cast(obj)

class itkBinomialBlurImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkBinomialBlurImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBinomialBlurImageFilterIUC3IUC3_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBinomialBlurImageFilterIUC3IUC3 self) -> itkBinomialBlurImageFilterIUC3IUC3_Pointer"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_Clone(self)


    def SetRepetitions(self, _arg):
        """SetRepetitions(itkBinomialBlurImageFilterIUC3IUC3 self, unsigned int const _arg)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_SetRepetitions(self, _arg)


    def GetRepetitions(self):
        """GetRepetitions(itkBinomialBlurImageFilterIUC3IUC3 self) -> unsigned int"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_GetRepetitions(self)


    def GenerateInputRequestedRegion(self):
        """GenerateInputRequestedRegion(itkBinomialBlurImageFilterIUC3IUC3 self)"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_SameDimensionCheck
    InputConvertibleToDoubleCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkBinomialBlurImageFilterPython.delete_itkBinomialBlurImageFilterIUC3IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBinomialBlurImageFilterIUC3IUC3"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBinomialBlurImageFilterIUC3IUC3 self) -> itkBinomialBlurImageFilterIUC3IUC3"""
        return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinomialBlurImageFilterIUC3IUC3

        Create a new object of the class itkBinomialBlurImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinomialBlurImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinomialBlurImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinomialBlurImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinomialBlurImageFilterIUC3IUC3.Clone = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_Clone, None, itkBinomialBlurImageFilterIUC3IUC3)
itkBinomialBlurImageFilterIUC3IUC3.SetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_SetRepetitions, None, itkBinomialBlurImageFilterIUC3IUC3)
itkBinomialBlurImageFilterIUC3IUC3.GetRepetitions = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_GetRepetitions, None, itkBinomialBlurImageFilterIUC3IUC3)
itkBinomialBlurImageFilterIUC3IUC3.GenerateInputRequestedRegion = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_GenerateInputRequestedRegion, None, itkBinomialBlurImageFilterIUC3IUC3)
itkBinomialBlurImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_GetPointer, None, itkBinomialBlurImageFilterIUC3IUC3)
itkBinomialBlurImageFilterIUC3IUC3_swigregister = _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_swigregister
itkBinomialBlurImageFilterIUC3IUC3_swigregister(itkBinomialBlurImageFilterIUC3IUC3)

def itkBinomialBlurImageFilterIUC3IUC3___New_orig__():
    """itkBinomialBlurImageFilterIUC3IUC3___New_orig__() -> itkBinomialBlurImageFilterIUC3IUC3_Pointer"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3___New_orig__()

def itkBinomialBlurImageFilterIUC3IUC3_cast(obj):
    """itkBinomialBlurImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkBinomialBlurImageFilterIUC3IUC3"""
    return _itkBinomialBlurImageFilterPython.itkBinomialBlurImageFilterIUC3IUC3_cast(obj)



