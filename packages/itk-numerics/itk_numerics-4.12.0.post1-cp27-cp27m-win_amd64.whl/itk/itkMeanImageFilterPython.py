# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMeanImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMeanImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMeanImageFilterPython')
    _itkMeanImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMeanImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMeanImageFilterPython
            return _itkMeanImageFilterPython
        try:
            _mod = imp.load_module('_itkMeanImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMeanImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMeanImageFilterPython
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
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
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

def itkMeanImageFilterIF3IF3_New():
  return itkMeanImageFilterIF3IF3.New()


def itkMeanImageFilterIF2IF2_New():
  return itkMeanImageFilterIF2IF2.New()


def itkMeanImageFilterIUC3IUC3_New():
  return itkMeanImageFilterIUC3IUC3.New()


def itkMeanImageFilterIUC2IUC2_New():
  return itkMeanImageFilterIUC2IUC2.New()


def itkMeanImageFilterISS3ISS3_New():
  return itkMeanImageFilterISS3ISS3.New()


def itkMeanImageFilterISS2ISS2_New():
  return itkMeanImageFilterISS2ISS2.New()

class itkMeanImageFilterIF2IF2(itkBoxImageFilterPython.itkBoxImageFilterIF2IF2):
    """Proxy of C++ itkMeanImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMeanImageFilterIF2IF2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMeanImageFilterIF2IF2 self) -> itkMeanImageFilterIF2IF2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkMeanImageFilterIF2IF2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMeanImageFilterIF2IF2 self) -> itkMeanImageFilterIF2IF2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIF2IF2

        Create a new object of the class itkMeanImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIF2IF2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_Clone, None, itkMeanImageFilterIF2IF2)
itkMeanImageFilterIF2IF2.GetPointer = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_GetPointer, None, itkMeanImageFilterIF2IF2)
itkMeanImageFilterIF2IF2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_swigregister
itkMeanImageFilterIF2IF2_swigregister(itkMeanImageFilterIF2IF2)

def itkMeanImageFilterIF2IF2___New_orig__():
    """itkMeanImageFilterIF2IF2___New_orig__() -> itkMeanImageFilterIF2IF2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2___New_orig__()

def itkMeanImageFilterIF2IF2_cast(obj):
    """itkMeanImageFilterIF2IF2_cast(itkLightObject obj) -> itkMeanImageFilterIF2IF2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_cast(obj)

class itkMeanImageFilterIF3IF3(itkBoxImageFilterPython.itkBoxImageFilterIF3IF3):
    """Proxy of C++ itkMeanImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMeanImageFilterIF3IF3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMeanImageFilterIF3IF3 self) -> itkMeanImageFilterIF3IF3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkMeanImageFilterIF3IF3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMeanImageFilterIF3IF3 self) -> itkMeanImageFilterIF3IF3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIF3IF3

        Create a new object of the class itkMeanImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIF3IF3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_Clone, None, itkMeanImageFilterIF3IF3)
itkMeanImageFilterIF3IF3.GetPointer = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_GetPointer, None, itkMeanImageFilterIF3IF3)
itkMeanImageFilterIF3IF3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_swigregister
itkMeanImageFilterIF3IF3_swigregister(itkMeanImageFilterIF3IF3)

def itkMeanImageFilterIF3IF3___New_orig__():
    """itkMeanImageFilterIF3IF3___New_orig__() -> itkMeanImageFilterIF3IF3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3___New_orig__()

def itkMeanImageFilterIF3IF3_cast(obj):
    """itkMeanImageFilterIF3IF3_cast(itkLightObject obj) -> itkMeanImageFilterIF3IF3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_cast(obj)

class itkMeanImageFilterISS2ISS2(itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2):
    """Proxy of C++ itkMeanImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMeanImageFilterISS2ISS2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMeanImageFilterISS2ISS2 self) -> itkMeanImageFilterISS2ISS2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterISS2ISS2

    def cast(obj):
        """cast(itkLightObject obj) -> itkMeanImageFilterISS2ISS2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMeanImageFilterISS2ISS2 self) -> itkMeanImageFilterISS2ISS2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeanImageFilterISS2ISS2

        Create a new object of the class itkMeanImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterISS2ISS2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_Clone, None, itkMeanImageFilterISS2ISS2)
itkMeanImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_GetPointer, None, itkMeanImageFilterISS2ISS2)
itkMeanImageFilterISS2ISS2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_swigregister
itkMeanImageFilterISS2ISS2_swigregister(itkMeanImageFilterISS2ISS2)

def itkMeanImageFilterISS2ISS2___New_orig__():
    """itkMeanImageFilterISS2ISS2___New_orig__() -> itkMeanImageFilterISS2ISS2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2___New_orig__()

def itkMeanImageFilterISS2ISS2_cast(obj):
    """itkMeanImageFilterISS2ISS2_cast(itkLightObject obj) -> itkMeanImageFilterISS2ISS2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_cast(obj)

class itkMeanImageFilterISS3ISS3(itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3):
    """Proxy of C++ itkMeanImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMeanImageFilterISS3ISS3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMeanImageFilterISS3ISS3 self) -> itkMeanImageFilterISS3ISS3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterISS3ISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkMeanImageFilterISS3ISS3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMeanImageFilterISS3ISS3 self) -> itkMeanImageFilterISS3ISS3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeanImageFilterISS3ISS3

        Create a new object of the class itkMeanImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterISS3ISS3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_Clone, None, itkMeanImageFilterISS3ISS3)
itkMeanImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_GetPointer, None, itkMeanImageFilterISS3ISS3)
itkMeanImageFilterISS3ISS3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_swigregister
itkMeanImageFilterISS3ISS3_swigregister(itkMeanImageFilterISS3ISS3)

def itkMeanImageFilterISS3ISS3___New_orig__():
    """itkMeanImageFilterISS3ISS3___New_orig__() -> itkMeanImageFilterISS3ISS3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3___New_orig__()

def itkMeanImageFilterISS3ISS3_cast(obj):
    """itkMeanImageFilterISS3ISS3_cast(itkLightObject obj) -> itkMeanImageFilterISS3ISS3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_cast(obj)

class itkMeanImageFilterIUC2IUC2(itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2):
    """Proxy of C++ itkMeanImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMeanImageFilterIUC2IUC2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMeanImageFilterIUC2IUC2 self) -> itkMeanImageFilterIUC2IUC2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUC2IUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkMeanImageFilterIUC2IUC2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMeanImageFilterIUC2IUC2 self) -> itkMeanImageFilterIUC2IUC2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUC2IUC2

        Create a new object of the class itkMeanImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIUC2IUC2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_Clone, None, itkMeanImageFilterIUC2IUC2)
itkMeanImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_GetPointer, None, itkMeanImageFilterIUC2IUC2)
itkMeanImageFilterIUC2IUC2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_swigregister
itkMeanImageFilterIUC2IUC2_swigregister(itkMeanImageFilterIUC2IUC2)

def itkMeanImageFilterIUC2IUC2___New_orig__():
    """itkMeanImageFilterIUC2IUC2___New_orig__() -> itkMeanImageFilterIUC2IUC2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2___New_orig__()

def itkMeanImageFilterIUC2IUC2_cast(obj):
    """itkMeanImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkMeanImageFilterIUC2IUC2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_cast(obj)

class itkMeanImageFilterIUC3IUC3(itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3):
    """Proxy of C++ itkMeanImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkMeanImageFilterIUC3IUC3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkMeanImageFilterIUC3IUC3 self) -> itkMeanImageFilterIUC3IUC3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUC3IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkMeanImageFilterIUC3IUC3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkMeanImageFilterIUC3IUC3 self) -> itkMeanImageFilterIUC3IUC3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUC3IUC3

        Create a new object of the class itkMeanImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIUC3IUC3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_Clone, None, itkMeanImageFilterIUC3IUC3)
itkMeanImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_GetPointer, None, itkMeanImageFilterIUC3IUC3)
itkMeanImageFilterIUC3IUC3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_swigregister
itkMeanImageFilterIUC3IUC3_swigregister(itkMeanImageFilterIUC3IUC3)

def itkMeanImageFilterIUC3IUC3___New_orig__():
    """itkMeanImageFilterIUC3IUC3___New_orig__() -> itkMeanImageFilterIUC3IUC3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3___New_orig__()

def itkMeanImageFilterIUC3IUC3_cast(obj):
    """itkMeanImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkMeanImageFilterIUC3IUC3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_cast(obj)



