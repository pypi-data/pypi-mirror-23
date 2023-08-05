# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMedianImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMedianImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMedianImageFilterPython')
    _itkMedianImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMedianImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMedianImageFilterPython
            return _itkMedianImageFilterPython
        try:
            _mod = imp.load_module('_itkMedianImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMedianImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMedianImageFilterPython
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
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkMedianImageFilterIF3IF3_New():
  return itkMedianImageFilterIF3IF3.New()


def itkMedianImageFilterIF2IF2_New():
  return itkMedianImageFilterIF2IF2.New()


def itkMedianImageFilterIUC3IUC3_New():
  return itkMedianImageFilterIUC3IUC3.New()


def itkMedianImageFilterIUC2IUC2_New():
  return itkMedianImageFilterIUC2IUC2.New()


def itkMedianImageFilterISS3ISS3_New():
  return itkMedianImageFilterISS3ISS3.New()


def itkMedianImageFilterISS2ISS2_New():
  return itkMedianImageFilterISS2ISS2.New()

class itkMedianImageFilterIF2IF2(itkBoxImageFilterPython.itkBoxImageFilterIF2IF2):
    """Proxy of C++ itkMedianImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMedianImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkMedianImageFilterIF2IF2_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMedianImageFilterIF2IF2_Pointer":
        """Clone(itkMedianImageFilterIF2IF2 self) -> itkMedianImageFilterIF2IF2_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_Clone(self)

    SameDimensionCheck = _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_SameDimensionCheck
    InputConvertibleToOutputCheck = _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_InputConvertibleToOutputCheck
    InputLessThanComparableCheck = _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_InputLessThanComparableCheck
    __swig_destroy__ = _itkMedianImageFilterPython.delete_itkMedianImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkMedianImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkMedianImageFilterIF2IF2"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMedianImageFilterIF2IF2 *":
        """GetPointer(itkMedianImageFilterIF2IF2 self) -> itkMedianImageFilterIF2IF2"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMedianImageFilterIF2IF2

        Create a new object of the class itkMedianImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMedianImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMedianImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMedianImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMedianImageFilterIF2IF2.Clone = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_Clone, None, itkMedianImageFilterIF2IF2)
itkMedianImageFilterIF2IF2.GetPointer = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_GetPointer, None, itkMedianImageFilterIF2IF2)
itkMedianImageFilterIF2IF2_swigregister = _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_swigregister
itkMedianImageFilterIF2IF2_swigregister(itkMedianImageFilterIF2IF2)

def itkMedianImageFilterIF2IF2___New_orig__() -> "itkMedianImageFilterIF2IF2_Pointer":
    """itkMedianImageFilterIF2IF2___New_orig__() -> itkMedianImageFilterIF2IF2_Pointer"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2___New_orig__()

def itkMedianImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkMedianImageFilterIF2IF2 *":
    """itkMedianImageFilterIF2IF2_cast(itkLightObject obj) -> itkMedianImageFilterIF2IF2"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIF2IF2_cast(obj)

class itkMedianImageFilterIF3IF3(itkBoxImageFilterPython.itkBoxImageFilterIF3IF3):
    """Proxy of C++ itkMedianImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMedianImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkMedianImageFilterIF3IF3_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMedianImageFilterIF3IF3_Pointer":
        """Clone(itkMedianImageFilterIF3IF3 self) -> itkMedianImageFilterIF3IF3_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_Clone(self)

    SameDimensionCheck = _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_SameDimensionCheck
    InputConvertibleToOutputCheck = _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_InputConvertibleToOutputCheck
    InputLessThanComparableCheck = _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_InputLessThanComparableCheck
    __swig_destroy__ = _itkMedianImageFilterPython.delete_itkMedianImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkMedianImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkMedianImageFilterIF3IF3"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMedianImageFilterIF3IF3 *":
        """GetPointer(itkMedianImageFilterIF3IF3 self) -> itkMedianImageFilterIF3IF3"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMedianImageFilterIF3IF3

        Create a new object of the class itkMedianImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMedianImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMedianImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMedianImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMedianImageFilterIF3IF3.Clone = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_Clone, None, itkMedianImageFilterIF3IF3)
itkMedianImageFilterIF3IF3.GetPointer = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_GetPointer, None, itkMedianImageFilterIF3IF3)
itkMedianImageFilterIF3IF3_swigregister = _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_swigregister
itkMedianImageFilterIF3IF3_swigregister(itkMedianImageFilterIF3IF3)

def itkMedianImageFilterIF3IF3___New_orig__() -> "itkMedianImageFilterIF3IF3_Pointer":
    """itkMedianImageFilterIF3IF3___New_orig__() -> itkMedianImageFilterIF3IF3_Pointer"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3___New_orig__()

def itkMedianImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkMedianImageFilterIF3IF3 *":
    """itkMedianImageFilterIF3IF3_cast(itkLightObject obj) -> itkMedianImageFilterIF3IF3"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIF3IF3_cast(obj)

class itkMedianImageFilterISS2ISS2(itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2):
    """Proxy of C++ itkMedianImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMedianImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkMedianImageFilterISS2ISS2_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMedianImageFilterISS2ISS2_Pointer":
        """Clone(itkMedianImageFilterISS2ISS2 self) -> itkMedianImageFilterISS2ISS2_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_Clone(self)

    SameDimensionCheck = _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_SameDimensionCheck
    InputConvertibleToOutputCheck = _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_InputConvertibleToOutputCheck
    InputLessThanComparableCheck = _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_InputLessThanComparableCheck
    __swig_destroy__ = _itkMedianImageFilterPython.delete_itkMedianImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkMedianImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkMedianImageFilterISS2ISS2"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMedianImageFilterISS2ISS2 *":
        """GetPointer(itkMedianImageFilterISS2ISS2 self) -> itkMedianImageFilterISS2ISS2"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMedianImageFilterISS2ISS2

        Create a new object of the class itkMedianImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMedianImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMedianImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMedianImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMedianImageFilterISS2ISS2.Clone = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_Clone, None, itkMedianImageFilterISS2ISS2)
itkMedianImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_GetPointer, None, itkMedianImageFilterISS2ISS2)
itkMedianImageFilterISS2ISS2_swigregister = _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_swigregister
itkMedianImageFilterISS2ISS2_swigregister(itkMedianImageFilterISS2ISS2)

def itkMedianImageFilterISS2ISS2___New_orig__() -> "itkMedianImageFilterISS2ISS2_Pointer":
    """itkMedianImageFilterISS2ISS2___New_orig__() -> itkMedianImageFilterISS2ISS2_Pointer"""
    return _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2___New_orig__()

def itkMedianImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkMedianImageFilterISS2ISS2 *":
    """itkMedianImageFilterISS2ISS2_cast(itkLightObject obj) -> itkMedianImageFilterISS2ISS2"""
    return _itkMedianImageFilterPython.itkMedianImageFilterISS2ISS2_cast(obj)

class itkMedianImageFilterISS3ISS3(itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3):
    """Proxy of C++ itkMedianImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMedianImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkMedianImageFilterISS3ISS3_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMedianImageFilterISS3ISS3_Pointer":
        """Clone(itkMedianImageFilterISS3ISS3 self) -> itkMedianImageFilterISS3ISS3_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_Clone(self)

    SameDimensionCheck = _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_SameDimensionCheck
    InputConvertibleToOutputCheck = _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_InputConvertibleToOutputCheck
    InputLessThanComparableCheck = _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_InputLessThanComparableCheck
    __swig_destroy__ = _itkMedianImageFilterPython.delete_itkMedianImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkMedianImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkMedianImageFilterISS3ISS3"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMedianImageFilterISS3ISS3 *":
        """GetPointer(itkMedianImageFilterISS3ISS3 self) -> itkMedianImageFilterISS3ISS3"""
        return _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMedianImageFilterISS3ISS3

        Create a new object of the class itkMedianImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMedianImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMedianImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMedianImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMedianImageFilterISS3ISS3.Clone = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_Clone, None, itkMedianImageFilterISS3ISS3)
itkMedianImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_GetPointer, None, itkMedianImageFilterISS3ISS3)
itkMedianImageFilterISS3ISS3_swigregister = _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_swigregister
itkMedianImageFilterISS3ISS3_swigregister(itkMedianImageFilterISS3ISS3)

def itkMedianImageFilterISS3ISS3___New_orig__() -> "itkMedianImageFilterISS3ISS3_Pointer":
    """itkMedianImageFilterISS3ISS3___New_orig__() -> itkMedianImageFilterISS3ISS3_Pointer"""
    return _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3___New_orig__()

def itkMedianImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkMedianImageFilterISS3ISS3 *":
    """itkMedianImageFilterISS3ISS3_cast(itkLightObject obj) -> itkMedianImageFilterISS3ISS3"""
    return _itkMedianImageFilterPython.itkMedianImageFilterISS3ISS3_cast(obj)

class itkMedianImageFilterIUC2IUC2(itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2):
    """Proxy of C++ itkMedianImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMedianImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkMedianImageFilterIUC2IUC2_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMedianImageFilterIUC2IUC2_Pointer":
        """Clone(itkMedianImageFilterIUC2IUC2 self) -> itkMedianImageFilterIUC2IUC2_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_Clone(self)

    SameDimensionCheck = _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_SameDimensionCheck
    InputConvertibleToOutputCheck = _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    InputLessThanComparableCheck = _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_InputLessThanComparableCheck
    __swig_destroy__ = _itkMedianImageFilterPython.delete_itkMedianImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkMedianImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkMedianImageFilterIUC2IUC2"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMedianImageFilterIUC2IUC2 *":
        """GetPointer(itkMedianImageFilterIUC2IUC2 self) -> itkMedianImageFilterIUC2IUC2"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMedianImageFilterIUC2IUC2

        Create a new object of the class itkMedianImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMedianImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMedianImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMedianImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMedianImageFilterIUC2IUC2.Clone = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_Clone, None, itkMedianImageFilterIUC2IUC2)
itkMedianImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_GetPointer, None, itkMedianImageFilterIUC2IUC2)
itkMedianImageFilterIUC2IUC2_swigregister = _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_swigregister
itkMedianImageFilterIUC2IUC2_swigregister(itkMedianImageFilterIUC2IUC2)

def itkMedianImageFilterIUC2IUC2___New_orig__() -> "itkMedianImageFilterIUC2IUC2_Pointer":
    """itkMedianImageFilterIUC2IUC2___New_orig__() -> itkMedianImageFilterIUC2IUC2_Pointer"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2___New_orig__()

def itkMedianImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkMedianImageFilterIUC2IUC2 *":
    """itkMedianImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkMedianImageFilterIUC2IUC2"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIUC2IUC2_cast(obj)

class itkMedianImageFilterIUC3IUC3(itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3):
    """Proxy of C++ itkMedianImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMedianImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkMedianImageFilterIUC3IUC3_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMedianImageFilterIUC3IUC3_Pointer":
        """Clone(itkMedianImageFilterIUC3IUC3 self) -> itkMedianImageFilterIUC3IUC3_Pointer"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_Clone(self)

    SameDimensionCheck = _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_SameDimensionCheck
    InputConvertibleToOutputCheck = _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    InputLessThanComparableCheck = _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_InputLessThanComparableCheck
    __swig_destroy__ = _itkMedianImageFilterPython.delete_itkMedianImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkMedianImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkMedianImageFilterIUC3IUC3"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMedianImageFilterIUC3IUC3 *":
        """GetPointer(itkMedianImageFilterIUC3IUC3 self) -> itkMedianImageFilterIUC3IUC3"""
        return _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMedianImageFilterIUC3IUC3

        Create a new object of the class itkMedianImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMedianImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMedianImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMedianImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMedianImageFilterIUC3IUC3.Clone = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_Clone, None, itkMedianImageFilterIUC3IUC3)
itkMedianImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_GetPointer, None, itkMedianImageFilterIUC3IUC3)
itkMedianImageFilterIUC3IUC3_swigregister = _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_swigregister
itkMedianImageFilterIUC3IUC3_swigregister(itkMedianImageFilterIUC3IUC3)

def itkMedianImageFilterIUC3IUC3___New_orig__() -> "itkMedianImageFilterIUC3IUC3_Pointer":
    """itkMedianImageFilterIUC3IUC3___New_orig__() -> itkMedianImageFilterIUC3IUC3_Pointer"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3___New_orig__()

def itkMedianImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkMedianImageFilterIUC3IUC3 *":
    """itkMedianImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkMedianImageFilterIUC3IUC3"""
    return _itkMedianImageFilterPython.itkMedianImageFilterIUC3IUC3_cast(obj)



