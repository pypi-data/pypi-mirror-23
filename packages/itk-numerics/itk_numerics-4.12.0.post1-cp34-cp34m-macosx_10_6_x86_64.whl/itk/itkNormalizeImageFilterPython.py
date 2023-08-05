# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNormalizeImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNormalizeImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNormalizeImageFilterPython')
    _itkNormalizeImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNormalizeImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkNormalizeImageFilterPython
            return _itkNormalizeImageFilterPython
        try:
            _mod = imp.load_module('_itkNormalizeImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNormalizeImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNormalizeImageFilterPython
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
import ITKCommonBasePython
import pyBasePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import itkFixedArrayPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkNormalizeImageFilterIF3IF3_New():
  return itkNormalizeImageFilterIF3IF3.New()


def itkNormalizeImageFilterIF2IF2_New():
  return itkNormalizeImageFilterIF2IF2.New()


def itkNormalizeImageFilterIUC3IUC3_New():
  return itkNormalizeImageFilterIUC3IUC3.New()


def itkNormalizeImageFilterIUC2IUC2_New():
  return itkNormalizeImageFilterIUC2IUC2.New()


def itkNormalizeImageFilterISS3ISS3_New():
  return itkNormalizeImageFilterISS3ISS3.New()


def itkNormalizeImageFilterISS2ISS2_New():
  return itkNormalizeImageFilterISS2ISS2.New()

class itkNormalizeImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkNormalizeImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkNormalizeImageFilterIF2IF2_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeImageFilterIF2IF2_Pointer":
        """Clone(itkNormalizeImageFilterIF2IF2 self) -> itkNormalizeImageFilterIF2IF2_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_Clone(self)

    __swig_destroy__ = _itkNormalizeImageFilterPython.delete_itkNormalizeImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkNormalizeImageFilterIF2IF2"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeImageFilterIF2IF2 *":
        """GetPointer(itkNormalizeImageFilterIF2IF2 self) -> itkNormalizeImageFilterIF2IF2"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeImageFilterIF2IF2

        Create a new object of the class itkNormalizeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeImageFilterIF2IF2.Clone = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_Clone, None, itkNormalizeImageFilterIF2IF2)
itkNormalizeImageFilterIF2IF2.GetPointer = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_GetPointer, None, itkNormalizeImageFilterIF2IF2)
itkNormalizeImageFilterIF2IF2_swigregister = _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_swigregister
itkNormalizeImageFilterIF2IF2_swigregister(itkNormalizeImageFilterIF2IF2)

def itkNormalizeImageFilterIF2IF2___New_orig__() -> "itkNormalizeImageFilterIF2IF2_Pointer":
    """itkNormalizeImageFilterIF2IF2___New_orig__() -> itkNormalizeImageFilterIF2IF2_Pointer"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2___New_orig__()

def itkNormalizeImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIF2IF2 *":
    """itkNormalizeImageFilterIF2IF2_cast(itkLightObject obj) -> itkNormalizeImageFilterIF2IF2"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF2IF2_cast(obj)

class itkNormalizeImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkNormalizeImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkNormalizeImageFilterIF3IF3_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeImageFilterIF3IF3_Pointer":
        """Clone(itkNormalizeImageFilterIF3IF3 self) -> itkNormalizeImageFilterIF3IF3_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_Clone(self)

    __swig_destroy__ = _itkNormalizeImageFilterPython.delete_itkNormalizeImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkNormalizeImageFilterIF3IF3"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeImageFilterIF3IF3 *":
        """GetPointer(itkNormalizeImageFilterIF3IF3 self) -> itkNormalizeImageFilterIF3IF3"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeImageFilterIF3IF3

        Create a new object of the class itkNormalizeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeImageFilterIF3IF3.Clone = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_Clone, None, itkNormalizeImageFilterIF3IF3)
itkNormalizeImageFilterIF3IF3.GetPointer = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_GetPointer, None, itkNormalizeImageFilterIF3IF3)
itkNormalizeImageFilterIF3IF3_swigregister = _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_swigregister
itkNormalizeImageFilterIF3IF3_swigregister(itkNormalizeImageFilterIF3IF3)

def itkNormalizeImageFilterIF3IF3___New_orig__() -> "itkNormalizeImageFilterIF3IF3_Pointer":
    """itkNormalizeImageFilterIF3IF3___New_orig__() -> itkNormalizeImageFilterIF3IF3_Pointer"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3___New_orig__()

def itkNormalizeImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIF3IF3 *":
    """itkNormalizeImageFilterIF3IF3_cast(itkLightObject obj) -> itkNormalizeImageFilterIF3IF3"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIF3IF3_cast(obj)

class itkNormalizeImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkNormalizeImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkNormalizeImageFilterISS2ISS2_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeImageFilterISS2ISS2_Pointer":
        """Clone(itkNormalizeImageFilterISS2ISS2 self) -> itkNormalizeImageFilterISS2ISS2_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_Clone(self)

    __swig_destroy__ = _itkNormalizeImageFilterPython.delete_itkNormalizeImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkNormalizeImageFilterISS2ISS2"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeImageFilterISS2ISS2 *":
        """GetPointer(itkNormalizeImageFilterISS2ISS2 self) -> itkNormalizeImageFilterISS2ISS2"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeImageFilterISS2ISS2

        Create a new object of the class itkNormalizeImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeImageFilterISS2ISS2.Clone = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_Clone, None, itkNormalizeImageFilterISS2ISS2)
itkNormalizeImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_GetPointer, None, itkNormalizeImageFilterISS2ISS2)
itkNormalizeImageFilterISS2ISS2_swigregister = _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_swigregister
itkNormalizeImageFilterISS2ISS2_swigregister(itkNormalizeImageFilterISS2ISS2)

def itkNormalizeImageFilterISS2ISS2___New_orig__() -> "itkNormalizeImageFilterISS2ISS2_Pointer":
    """itkNormalizeImageFilterISS2ISS2___New_orig__() -> itkNormalizeImageFilterISS2ISS2_Pointer"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2___New_orig__()

def itkNormalizeImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterISS2ISS2 *":
    """itkNormalizeImageFilterISS2ISS2_cast(itkLightObject obj) -> itkNormalizeImageFilterISS2ISS2"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS2ISS2_cast(obj)

class itkNormalizeImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkNormalizeImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkNormalizeImageFilterISS3ISS3_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeImageFilterISS3ISS3_Pointer":
        """Clone(itkNormalizeImageFilterISS3ISS3 self) -> itkNormalizeImageFilterISS3ISS3_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_Clone(self)

    __swig_destroy__ = _itkNormalizeImageFilterPython.delete_itkNormalizeImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkNormalizeImageFilterISS3ISS3"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeImageFilterISS3ISS3 *":
        """GetPointer(itkNormalizeImageFilterISS3ISS3 self) -> itkNormalizeImageFilterISS3ISS3"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeImageFilterISS3ISS3

        Create a new object of the class itkNormalizeImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeImageFilterISS3ISS3.Clone = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_Clone, None, itkNormalizeImageFilterISS3ISS3)
itkNormalizeImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_GetPointer, None, itkNormalizeImageFilterISS3ISS3)
itkNormalizeImageFilterISS3ISS3_swigregister = _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_swigregister
itkNormalizeImageFilterISS3ISS3_swigregister(itkNormalizeImageFilterISS3ISS3)

def itkNormalizeImageFilterISS3ISS3___New_orig__() -> "itkNormalizeImageFilterISS3ISS3_Pointer":
    """itkNormalizeImageFilterISS3ISS3___New_orig__() -> itkNormalizeImageFilterISS3ISS3_Pointer"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3___New_orig__()

def itkNormalizeImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterISS3ISS3 *":
    """itkNormalizeImageFilterISS3ISS3_cast(itkLightObject obj) -> itkNormalizeImageFilterISS3ISS3"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterISS3ISS3_cast(obj)

class itkNormalizeImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkNormalizeImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkNormalizeImageFilterIUC2IUC2_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeImageFilterIUC2IUC2_Pointer":
        """Clone(itkNormalizeImageFilterIUC2IUC2 self) -> itkNormalizeImageFilterIUC2IUC2_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_Clone(self)

    __swig_destroy__ = _itkNormalizeImageFilterPython.delete_itkNormalizeImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkNormalizeImageFilterIUC2IUC2"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeImageFilterIUC2IUC2 *":
        """GetPointer(itkNormalizeImageFilterIUC2IUC2 self) -> itkNormalizeImageFilterIUC2IUC2"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeImageFilterIUC2IUC2

        Create a new object of the class itkNormalizeImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeImageFilterIUC2IUC2.Clone = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_Clone, None, itkNormalizeImageFilterIUC2IUC2)
itkNormalizeImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_GetPointer, None, itkNormalizeImageFilterIUC2IUC2)
itkNormalizeImageFilterIUC2IUC2_swigregister = _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_swigregister
itkNormalizeImageFilterIUC2IUC2_swigregister(itkNormalizeImageFilterIUC2IUC2)

def itkNormalizeImageFilterIUC2IUC2___New_orig__() -> "itkNormalizeImageFilterIUC2IUC2_Pointer":
    """itkNormalizeImageFilterIUC2IUC2___New_orig__() -> itkNormalizeImageFilterIUC2IUC2_Pointer"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2___New_orig__()

def itkNormalizeImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIUC2IUC2 *":
    """itkNormalizeImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkNormalizeImageFilterIUC2IUC2"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC2IUC2_cast(obj)

class itkNormalizeImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkNormalizeImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkNormalizeImageFilterIUC3IUC3_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeImageFilterIUC3IUC3_Pointer":
        """Clone(itkNormalizeImageFilterIUC3IUC3 self) -> itkNormalizeImageFilterIUC3IUC3_Pointer"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_Clone(self)

    __swig_destroy__ = _itkNormalizeImageFilterPython.delete_itkNormalizeImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkNormalizeImageFilterIUC3IUC3"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeImageFilterIUC3IUC3 *":
        """GetPointer(itkNormalizeImageFilterIUC3IUC3 self) -> itkNormalizeImageFilterIUC3IUC3"""
        return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeImageFilterIUC3IUC3

        Create a new object of the class itkNormalizeImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeImageFilterIUC3IUC3.Clone = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_Clone, None, itkNormalizeImageFilterIUC3IUC3)
itkNormalizeImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_GetPointer, None, itkNormalizeImageFilterIUC3IUC3)
itkNormalizeImageFilterIUC3IUC3_swigregister = _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_swigregister
itkNormalizeImageFilterIUC3IUC3_swigregister(itkNormalizeImageFilterIUC3IUC3)

def itkNormalizeImageFilterIUC3IUC3___New_orig__() -> "itkNormalizeImageFilterIUC3IUC3_Pointer":
    """itkNormalizeImageFilterIUC3IUC3___New_orig__() -> itkNormalizeImageFilterIUC3IUC3_Pointer"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3___New_orig__()

def itkNormalizeImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkNormalizeImageFilterIUC3IUC3 *":
    """itkNormalizeImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkNormalizeImageFilterIUC3IUC3"""
    return _itkNormalizeImageFilterPython.itkNormalizeImageFilterIUC3IUC3_cast(obj)



