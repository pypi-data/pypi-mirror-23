# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkImageShapeModelEstimatorBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkImageShapeModelEstimatorBasePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkImageShapeModelEstimatorBasePython')
    _itkImageShapeModelEstimatorBasePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkImageShapeModelEstimatorBasePython', [dirname(__file__)])
        except ImportError:
            import _itkImageShapeModelEstimatorBasePython
            return _itkImageShapeModelEstimatorBasePython
        try:
            _mod = imp.load_module('_itkImageShapeModelEstimatorBasePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkImageShapeModelEstimatorBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkImageShapeModelEstimatorBasePython
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

def itkImageShapeModelEstimatorBaseIF3IF3_New():
  return itkImageShapeModelEstimatorBaseIF3IF3.New()


def itkImageShapeModelEstimatorBaseIUC3IF3_New():
  return itkImageShapeModelEstimatorBaseIUC3IF3.New()


def itkImageShapeModelEstimatorBaseISS3IF3_New():
  return itkImageShapeModelEstimatorBaseISS3IF3.New()


def itkImageShapeModelEstimatorBaseIF2IF2_New():
  return itkImageShapeModelEstimatorBaseIF2IF2.New()


def itkImageShapeModelEstimatorBaseIUC2IF2_New():
  return itkImageShapeModelEstimatorBaseIUC2IF2.New()


def itkImageShapeModelEstimatorBaseISS2IF2_New():
  return itkImageShapeModelEstimatorBaseISS2IF2.New()

class itkImageShapeModelEstimatorBaseIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkImageShapeModelEstimatorBaseIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkImageShapeModelEstimatorBasePython.delete_itkImageShapeModelEstimatorBaseIF2IF2

    def cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIF2IF2 *":
        """cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIF2IF2"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageShapeModelEstimatorBaseIF2IF2 *":
        """GetPointer(itkImageShapeModelEstimatorBaseIF2IF2 self) -> itkImageShapeModelEstimatorBaseIF2IF2"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageShapeModelEstimatorBaseIF2IF2

        Create a new object of the class itkImageShapeModelEstimatorBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageShapeModelEstimatorBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageShapeModelEstimatorBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageShapeModelEstimatorBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageShapeModelEstimatorBaseIF2IF2.GetPointer = new_instancemethod(_itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF2IF2_GetPointer, None, itkImageShapeModelEstimatorBaseIF2IF2)
itkImageShapeModelEstimatorBaseIF2IF2_swigregister = _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF2IF2_swigregister
itkImageShapeModelEstimatorBaseIF2IF2_swigregister(itkImageShapeModelEstimatorBaseIF2IF2)

def itkImageShapeModelEstimatorBaseIF2IF2_cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIF2IF2 *":
    """itkImageShapeModelEstimatorBaseIF2IF2_cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIF2IF2"""
    return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF2IF2_cast(obj)

class itkImageShapeModelEstimatorBaseIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkImageShapeModelEstimatorBaseIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkImageShapeModelEstimatorBasePython.delete_itkImageShapeModelEstimatorBaseIF3IF3

    def cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIF3IF3 *":
        """cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIF3IF3"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageShapeModelEstimatorBaseIF3IF3 *":
        """GetPointer(itkImageShapeModelEstimatorBaseIF3IF3 self) -> itkImageShapeModelEstimatorBaseIF3IF3"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageShapeModelEstimatorBaseIF3IF3

        Create a new object of the class itkImageShapeModelEstimatorBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageShapeModelEstimatorBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageShapeModelEstimatorBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageShapeModelEstimatorBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageShapeModelEstimatorBaseIF3IF3.GetPointer = new_instancemethod(_itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF3IF3_GetPointer, None, itkImageShapeModelEstimatorBaseIF3IF3)
itkImageShapeModelEstimatorBaseIF3IF3_swigregister = _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF3IF3_swigregister
itkImageShapeModelEstimatorBaseIF3IF3_swigregister(itkImageShapeModelEstimatorBaseIF3IF3)

def itkImageShapeModelEstimatorBaseIF3IF3_cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIF3IF3 *":
    """itkImageShapeModelEstimatorBaseIF3IF3_cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIF3IF3"""
    return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIF3IF3_cast(obj)

class itkImageShapeModelEstimatorBaseISS2IF2(itkImageToImageFilterAPython.itkImageToImageFilterISS2IF2):
    """Proxy of C++ itkImageShapeModelEstimatorBaseISS2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkImageShapeModelEstimatorBasePython.delete_itkImageShapeModelEstimatorBaseISS2IF2

    def cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseISS2IF2 *":
        """cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseISS2IF2"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageShapeModelEstimatorBaseISS2IF2 *":
        """GetPointer(itkImageShapeModelEstimatorBaseISS2IF2 self) -> itkImageShapeModelEstimatorBaseISS2IF2"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageShapeModelEstimatorBaseISS2IF2

        Create a new object of the class itkImageShapeModelEstimatorBaseISS2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageShapeModelEstimatorBaseISS2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageShapeModelEstimatorBaseISS2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageShapeModelEstimatorBaseISS2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageShapeModelEstimatorBaseISS2IF2.GetPointer = new_instancemethod(_itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS2IF2_GetPointer, None, itkImageShapeModelEstimatorBaseISS2IF2)
itkImageShapeModelEstimatorBaseISS2IF2_swigregister = _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS2IF2_swigregister
itkImageShapeModelEstimatorBaseISS2IF2_swigregister(itkImageShapeModelEstimatorBaseISS2IF2)

def itkImageShapeModelEstimatorBaseISS2IF2_cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseISS2IF2 *":
    """itkImageShapeModelEstimatorBaseISS2IF2_cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseISS2IF2"""
    return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS2IF2_cast(obj)

class itkImageShapeModelEstimatorBaseISS3IF3(itkImageToImageFilterAPython.itkImageToImageFilterISS3IF3):
    """Proxy of C++ itkImageShapeModelEstimatorBaseISS3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkImageShapeModelEstimatorBasePython.delete_itkImageShapeModelEstimatorBaseISS3IF3

    def cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseISS3IF3 *":
        """cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseISS3IF3"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageShapeModelEstimatorBaseISS3IF3 *":
        """GetPointer(itkImageShapeModelEstimatorBaseISS3IF3 self) -> itkImageShapeModelEstimatorBaseISS3IF3"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageShapeModelEstimatorBaseISS3IF3

        Create a new object of the class itkImageShapeModelEstimatorBaseISS3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageShapeModelEstimatorBaseISS3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageShapeModelEstimatorBaseISS3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageShapeModelEstimatorBaseISS3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageShapeModelEstimatorBaseISS3IF3.GetPointer = new_instancemethod(_itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS3IF3_GetPointer, None, itkImageShapeModelEstimatorBaseISS3IF3)
itkImageShapeModelEstimatorBaseISS3IF3_swigregister = _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS3IF3_swigregister
itkImageShapeModelEstimatorBaseISS3IF3_swigregister(itkImageShapeModelEstimatorBaseISS3IF3)

def itkImageShapeModelEstimatorBaseISS3IF3_cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseISS3IF3 *":
    """itkImageShapeModelEstimatorBaseISS3IF3_cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseISS3IF3"""
    return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseISS3IF3_cast(obj)

class itkImageShapeModelEstimatorBaseIUC2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IF2):
    """Proxy of C++ itkImageShapeModelEstimatorBaseIUC2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkImageShapeModelEstimatorBasePython.delete_itkImageShapeModelEstimatorBaseIUC2IF2

    def cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIUC2IF2 *":
        """cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIUC2IF2"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageShapeModelEstimatorBaseIUC2IF2 *":
        """GetPointer(itkImageShapeModelEstimatorBaseIUC2IF2 self) -> itkImageShapeModelEstimatorBaseIUC2IF2"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageShapeModelEstimatorBaseIUC2IF2

        Create a new object of the class itkImageShapeModelEstimatorBaseIUC2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageShapeModelEstimatorBaseIUC2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageShapeModelEstimatorBaseIUC2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageShapeModelEstimatorBaseIUC2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageShapeModelEstimatorBaseIUC2IF2.GetPointer = new_instancemethod(_itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC2IF2_GetPointer, None, itkImageShapeModelEstimatorBaseIUC2IF2)
itkImageShapeModelEstimatorBaseIUC2IF2_swigregister = _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC2IF2_swigregister
itkImageShapeModelEstimatorBaseIUC2IF2_swigregister(itkImageShapeModelEstimatorBaseIUC2IF2)

def itkImageShapeModelEstimatorBaseIUC2IF2_cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIUC2IF2 *":
    """itkImageShapeModelEstimatorBaseIUC2IF2_cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIUC2IF2"""
    return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC2IF2_cast(obj)

class itkImageShapeModelEstimatorBaseIUC3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IF3):
    """Proxy of C++ itkImageShapeModelEstimatorBaseIUC3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkImageShapeModelEstimatorBasePython.delete_itkImageShapeModelEstimatorBaseIUC3IF3

    def cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIUC3IF3 *":
        """cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIUC3IF3"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageShapeModelEstimatorBaseIUC3IF3 *":
        """GetPointer(itkImageShapeModelEstimatorBaseIUC3IF3 self) -> itkImageShapeModelEstimatorBaseIUC3IF3"""
        return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageShapeModelEstimatorBaseIUC3IF3

        Create a new object of the class itkImageShapeModelEstimatorBaseIUC3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageShapeModelEstimatorBaseIUC3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageShapeModelEstimatorBaseIUC3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageShapeModelEstimatorBaseIUC3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageShapeModelEstimatorBaseIUC3IF3.GetPointer = new_instancemethod(_itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC3IF3_GetPointer, None, itkImageShapeModelEstimatorBaseIUC3IF3)
itkImageShapeModelEstimatorBaseIUC3IF3_swigregister = _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC3IF3_swigregister
itkImageShapeModelEstimatorBaseIUC3IF3_swigregister(itkImageShapeModelEstimatorBaseIUC3IF3)

def itkImageShapeModelEstimatorBaseIUC3IF3_cast(obj: 'itkLightObject') -> "itkImageShapeModelEstimatorBaseIUC3IF3 *":
    """itkImageShapeModelEstimatorBaseIUC3IF3_cast(itkLightObject obj) -> itkImageShapeModelEstimatorBaseIUC3IF3"""
    return _itkImageShapeModelEstimatorBasePython.itkImageShapeModelEstimatorBaseIUC3IF3_cast(obj)



