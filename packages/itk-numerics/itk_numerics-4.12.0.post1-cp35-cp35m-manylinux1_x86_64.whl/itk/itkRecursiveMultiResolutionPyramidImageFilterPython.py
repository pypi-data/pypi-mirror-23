# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRecursiveMultiResolutionPyramidImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRecursiveMultiResolutionPyramidImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRecursiveMultiResolutionPyramidImageFilterPython')
    _itkRecursiveMultiResolutionPyramidImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRecursiveMultiResolutionPyramidImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRecursiveMultiResolutionPyramidImageFilterPython
            return _itkRecursiveMultiResolutionPyramidImageFilterPython
        try:
            _mod = imp.load_module('_itkRecursiveMultiResolutionPyramidImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRecursiveMultiResolutionPyramidImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRecursiveMultiResolutionPyramidImageFilterPython
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


import itkMultiResolutionPyramidImageFilterPython
import itkImageToImageFilterAPython
import itkVectorImagePython
import ITKCommonBasePython
import pyBasePython
import stdcomplexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkArray2DPython

def itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_New():
  return itkRecursiveMultiResolutionPyramidImageFilterIF3IF3.New()


def itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_New():
  return itkRecursiveMultiResolutionPyramidImageFilterIF2IF2.New()


def itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_New():
  return itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3.New()


def itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_New():
  return itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2.New()


def itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_New():
  return itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3.New()


def itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_New():
  return itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2.New()

class itkRecursiveMultiResolutionPyramidImageFilterIF2IF2(itkMultiResolutionPyramidImageFilterPython.itkMultiResolutionPyramidImageFilterIF2IF2):
    """Proxy of C++ itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Pointer":
        """Clone(itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 self) -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Clone(self)

    __swig_destroy__ = _itkRecursiveMultiResolutionPyramidImageFilterPython.delete_itkRecursiveMultiResolutionPyramidImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 *":
        """GetPointer(itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 self) -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2

        Create a new object of the class itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveMultiResolutionPyramidImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveMultiResolutionPyramidImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveMultiResolutionPyramidImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveMultiResolutionPyramidImageFilterIF2IF2.Clone = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Clone, None, itkRecursiveMultiResolutionPyramidImageFilterIF2IF2)
itkRecursiveMultiResolutionPyramidImageFilterIF2IF2.GetPointer = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_GetPointer, None, itkRecursiveMultiResolutionPyramidImageFilterIF2IF2)
itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_swigregister = _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_swigregister
itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_swigregister(itkRecursiveMultiResolutionPyramidImageFilterIF2IF2)

def itkRecursiveMultiResolutionPyramidImageFilterIF2IF2___New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Pointer":
    """itkRecursiveMultiResolutionPyramidImageFilterIF2IF2___New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_Pointer"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2___New_orig__()

def itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIF2IF2 *":
    """itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIF2IF2"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF2IF2_cast(obj)

class itkRecursiveMultiResolutionPyramidImageFilterIF3IF3(itkMultiResolutionPyramidImageFilterPython.itkMultiResolutionPyramidImageFilterIF3IF3):
    """Proxy of C++ itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Pointer":
        """Clone(itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 self) -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Clone(self)

    __swig_destroy__ = _itkRecursiveMultiResolutionPyramidImageFilterPython.delete_itkRecursiveMultiResolutionPyramidImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 *":
        """GetPointer(itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 self) -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3

        Create a new object of the class itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveMultiResolutionPyramidImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveMultiResolutionPyramidImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveMultiResolutionPyramidImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveMultiResolutionPyramidImageFilterIF3IF3.Clone = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Clone, None, itkRecursiveMultiResolutionPyramidImageFilterIF3IF3)
itkRecursiveMultiResolutionPyramidImageFilterIF3IF3.GetPointer = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_GetPointer, None, itkRecursiveMultiResolutionPyramidImageFilterIF3IF3)
itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_swigregister = _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_swigregister
itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_swigregister(itkRecursiveMultiResolutionPyramidImageFilterIF3IF3)

def itkRecursiveMultiResolutionPyramidImageFilterIF3IF3___New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Pointer":
    """itkRecursiveMultiResolutionPyramidImageFilterIF3IF3___New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_Pointer"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3___New_orig__()

def itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIF3IF3 *":
    """itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIF3IF3"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIF3IF3_cast(obj)

class itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2(itkMultiResolutionPyramidImageFilterPython.itkMultiResolutionPyramidImageFilterISS2ISS2):
    """Proxy of C++ itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Pointer":
        """Clone(itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 self) -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Clone(self)

    __swig_destroy__ = _itkRecursiveMultiResolutionPyramidImageFilterPython.delete_itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 *":
        """GetPointer(itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 self) -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2

        Create a new object of the class itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2.Clone = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Clone, None, itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2)
itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_GetPointer, None, itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2)
itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_swigregister = _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_swigregister
itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_swigregister(itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2)

def itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2___New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Pointer":
    """itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2___New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_Pointer"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2___New_orig__()

def itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2 *":
    """itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2_cast(obj)

class itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3(itkMultiResolutionPyramidImageFilterPython.itkMultiResolutionPyramidImageFilterISS3ISS3):
    """Proxy of C++ itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Pointer":
        """Clone(itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 self) -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Clone(self)

    __swig_destroy__ = _itkRecursiveMultiResolutionPyramidImageFilterPython.delete_itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 *":
        """GetPointer(itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 self) -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3

        Create a new object of the class itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3.Clone = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Clone, None, itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3)
itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_GetPointer, None, itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3)
itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_swigregister = _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_swigregister
itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_swigregister(itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3)

def itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3___New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Pointer":
    """itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3___New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_Pointer"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3___New_orig__()

def itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3 *":
    """itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3_cast(obj)

class itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2(itkMultiResolutionPyramidImageFilterPython.itkMultiResolutionPyramidImageFilterIUC2IUC2):
    """Proxy of C++ itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Pointer":
        """Clone(itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 self) -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Clone(self)

    __swig_destroy__ = _itkRecursiveMultiResolutionPyramidImageFilterPython.delete_itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 *":
        """GetPointer(itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 self) -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2

        Create a new object of the class itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2.Clone = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Clone, None, itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2)
itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_GetPointer, None, itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2)
itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_swigregister = _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_swigregister
itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_swigregister(itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2)

def itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2___New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Pointer":
    """itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2___New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_Pointer"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2___New_orig__()

def itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2 *":
    """itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2_cast(obj)

class itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3(itkMultiResolutionPyramidImageFilterPython.itkMultiResolutionPyramidImageFilterIUC3IUC3):
    """Proxy of C++ itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Pointer":
        """Clone(itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 self) -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Pointer"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Clone(self)

    __swig_destroy__ = _itkRecursiveMultiResolutionPyramidImageFilterPython.delete_itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 *":
        """GetPointer(itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 self) -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3"""
        return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3

        Create a new object of the class itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3.Clone = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Clone, None, itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3)
itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_GetPointer, None, itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3)
itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_swigregister = _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_swigregister
itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_swigregister(itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3)

def itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3___New_orig__() -> "itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Pointer":
    """itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3___New_orig__() -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_Pointer"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3___New_orig__()

def itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3 *":
    """itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3"""
    return _itkRecursiveMultiResolutionPyramidImageFilterPython.itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3_cast(obj)



