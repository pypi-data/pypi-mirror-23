# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkJoinSeriesImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkJoinSeriesImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkJoinSeriesImageFilterPython')
    _itkJoinSeriesImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkJoinSeriesImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkJoinSeriesImageFilterPython
            return _itkJoinSeriesImageFilterPython
        try:
            _mod = imp.load_module('_itkJoinSeriesImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkJoinSeriesImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkJoinSeriesImageFilterPython
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


import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkImageToImageFilterBPython
import itkImagePython
import stdcomplexPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
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

def itkJoinSeriesImageFilterIF2IF3_New():
  return itkJoinSeriesImageFilterIF2IF3.New()


def itkJoinSeriesImageFilterIUC2IUC3_New():
  return itkJoinSeriesImageFilterIUC2IUC3.New()


def itkJoinSeriesImageFilterISS2ISS3_New():
  return itkJoinSeriesImageFilterISS2ISS3.New()

class itkJoinSeriesImageFilterIF2IF3(itkImageToImageFilterBPython.itkImageToImageFilterIF2IF3):
    """Proxy of C++ itkJoinSeriesImageFilterIF2IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkJoinSeriesImageFilterIF2IF3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkJoinSeriesImageFilterIF2IF3 self) -> itkJoinSeriesImageFilterIF2IF3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_Clone(self)


    def SetSpacing(self, _arg):
        """SetSpacing(itkJoinSeriesImageFilterIF2IF3 self, double const _arg)"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetSpacing(self, _arg)


    def GetSpacing(self):
        """GetSpacing(itkJoinSeriesImageFilterIF2IF3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetSpacing(self)


    def SetOrigin(self, _arg):
        """SetOrigin(itkJoinSeriesImageFilterIF2IF3 self, double const _arg)"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetOrigin(self, _arg)


    def GetOrigin(self):
        """GetOrigin(itkJoinSeriesImageFilterIF2IF3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterIF2IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterIF2IF3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkJoinSeriesImageFilterIF2IF3 self) -> itkJoinSeriesImageFilterIF2IF3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterIF2IF3

        Create a new object of the class itkJoinSeriesImageFilterIF2IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterIF2IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterIF2IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterIF2IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterIF2IF3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_Clone, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetSpacing, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetSpacing, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetOrigin, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetOrigin, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.GetPointer = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetPointer, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_swigregister
itkJoinSeriesImageFilterIF2IF3_swigregister(itkJoinSeriesImageFilterIF2IF3)

def itkJoinSeriesImageFilterIF2IF3___New_orig__():
    """itkJoinSeriesImageFilterIF2IF3___New_orig__() -> itkJoinSeriesImageFilterIF2IF3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3___New_orig__()

def itkJoinSeriesImageFilterIF2IF3_cast(obj):
    """itkJoinSeriesImageFilterIF2IF3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterIF2IF3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_cast(obj)

class itkJoinSeriesImageFilterISS2ISS3(itkImageToImageFilterBPython.itkImageToImageFilterISS2ISS3):
    """Proxy of C++ itkJoinSeriesImageFilterISS2ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkJoinSeriesImageFilterISS2ISS3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkJoinSeriesImageFilterISS2ISS3 self) -> itkJoinSeriesImageFilterISS2ISS3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_Clone(self)


    def SetSpacing(self, _arg):
        """SetSpacing(itkJoinSeriesImageFilterISS2ISS3 self, double const _arg)"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetSpacing(self, _arg)


    def GetSpacing(self):
        """GetSpacing(itkJoinSeriesImageFilterISS2ISS3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetSpacing(self)


    def SetOrigin(self, _arg):
        """SetOrigin(itkJoinSeriesImageFilterISS2ISS3 self, double const _arg)"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetOrigin(self, _arg)


    def GetOrigin(self):
        """GetOrigin(itkJoinSeriesImageFilterISS2ISS3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterISS2ISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterISS2ISS3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkJoinSeriesImageFilterISS2ISS3 self) -> itkJoinSeriesImageFilterISS2ISS3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterISS2ISS3

        Create a new object of the class itkJoinSeriesImageFilterISS2ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterISS2ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterISS2ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterISS2ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterISS2ISS3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_Clone, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetSpacing, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetSpacing, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetOrigin, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetOrigin, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.GetPointer = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetPointer, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_swigregister
itkJoinSeriesImageFilterISS2ISS3_swigregister(itkJoinSeriesImageFilterISS2ISS3)

def itkJoinSeriesImageFilterISS2ISS3___New_orig__():
    """itkJoinSeriesImageFilterISS2ISS3___New_orig__() -> itkJoinSeriesImageFilterISS2ISS3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3___New_orig__()

def itkJoinSeriesImageFilterISS2ISS3_cast(obj):
    """itkJoinSeriesImageFilterISS2ISS3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterISS2ISS3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_cast(obj)

class itkJoinSeriesImageFilterIUC2IUC3(itkImageToImageFilterBPython.itkImageToImageFilterIUC2IUC3):
    """Proxy of C++ itkJoinSeriesImageFilterIUC2IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkJoinSeriesImageFilterIUC2IUC3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkJoinSeriesImageFilterIUC2IUC3 self) -> itkJoinSeriesImageFilterIUC2IUC3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_Clone(self)


    def SetSpacing(self, _arg):
        """SetSpacing(itkJoinSeriesImageFilterIUC2IUC3 self, double const _arg)"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetSpacing(self, _arg)


    def GetSpacing(self):
        """GetSpacing(itkJoinSeriesImageFilterIUC2IUC3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetSpacing(self)


    def SetOrigin(self, _arg):
        """SetOrigin(itkJoinSeriesImageFilterIUC2IUC3 self, double const _arg)"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetOrigin(self, _arg)


    def GetOrigin(self):
        """GetOrigin(itkJoinSeriesImageFilterIUC2IUC3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterIUC2IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterIUC2IUC3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkJoinSeriesImageFilterIUC2IUC3 self) -> itkJoinSeriesImageFilterIUC2IUC3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterIUC2IUC3

        Create a new object of the class itkJoinSeriesImageFilterIUC2IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterIUC2IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterIUC2IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterIUC2IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterIUC2IUC3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_Clone, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetSpacing, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetSpacing, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetOrigin, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetOrigin, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.GetPointer = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetPointer, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_swigregister
itkJoinSeriesImageFilterIUC2IUC3_swigregister(itkJoinSeriesImageFilterIUC2IUC3)

def itkJoinSeriesImageFilterIUC2IUC3___New_orig__():
    """itkJoinSeriesImageFilterIUC2IUC3___New_orig__() -> itkJoinSeriesImageFilterIUC2IUC3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3___New_orig__()

def itkJoinSeriesImageFilterIUC2IUC3_cast(obj):
    """itkJoinSeriesImageFilterIUC2IUC3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterIUC2IUC3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_cast(obj)



