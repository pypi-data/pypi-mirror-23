# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNormalizeToConstantImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNormalizeToConstantImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNormalizeToConstantImageFilterPython')
    _itkNormalizeToConstantImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNormalizeToConstantImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkNormalizeToConstantImageFilterPython
            return _itkNormalizeToConstantImageFilterPython
        try:
            _mod = imp.load_module('_itkNormalizeToConstantImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNormalizeToConstantImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNormalizeToConstantImageFilterPython
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
import ITKCommonBasePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkNormalizeToConstantImageFilterIF3IF3_New():
  return itkNormalizeToConstantImageFilterIF3IF3.New()


def itkNormalizeToConstantImageFilterIF2IF2_New():
  return itkNormalizeToConstantImageFilterIF2IF2.New()


def itkNormalizeToConstantImageFilterIUC3IUC3_New():
  return itkNormalizeToConstantImageFilterIUC3IUC3.New()


def itkNormalizeToConstantImageFilterIUC2IUC2_New():
  return itkNormalizeToConstantImageFilterIUC2IUC2.New()


def itkNormalizeToConstantImageFilterISS3ISS3_New():
  return itkNormalizeToConstantImageFilterISS3ISS3.New()


def itkNormalizeToConstantImageFilterISS2ISS2_New():
  return itkNormalizeToConstantImageFilterISS2ISS2.New()

class itkNormalizeToConstantImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkNormalizeToConstantImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeToConstantImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkNormalizeToConstantImageFilterIF2IF2_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeToConstantImageFilterIF2IF2_Pointer":
        """Clone(itkNormalizeToConstantImageFilterIF2IF2 self) -> itkNormalizeToConstantImageFilterIF2IF2_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_Clone(self)


    def SetConstant(self, _arg: 'double const') -> "void":
        """SetConstant(itkNormalizeToConstantImageFilterIF2IF2 self, double const _arg)"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_SetConstant(self, _arg)


    def GetConstant(self) -> "double":
        """GetConstant(itkNormalizeToConstantImageFilterIF2IF2 self) -> double"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_GetConstant(self)

    InputHasPixelTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_InputHasPixelTraitsCheck
    InputHasNumericTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkNormalizeToConstantImageFilterPython.delete_itkNormalizeToConstantImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIF2IF2"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeToConstantImageFilterIF2IF2 *":
        """GetPointer(itkNormalizeToConstantImageFilterIF2IF2 self) -> itkNormalizeToConstantImageFilterIF2IF2"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeToConstantImageFilterIF2IF2

        Create a new object of the class itkNormalizeToConstantImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeToConstantImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeToConstantImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeToConstantImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeToConstantImageFilterIF2IF2.Clone = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_Clone, None, itkNormalizeToConstantImageFilterIF2IF2)
itkNormalizeToConstantImageFilterIF2IF2.SetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_SetConstant, None, itkNormalizeToConstantImageFilterIF2IF2)
itkNormalizeToConstantImageFilterIF2IF2.GetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_GetConstant, None, itkNormalizeToConstantImageFilterIF2IF2)
itkNormalizeToConstantImageFilterIF2IF2.GetPointer = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_GetPointer, None, itkNormalizeToConstantImageFilterIF2IF2)
itkNormalizeToConstantImageFilterIF2IF2_swigregister = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_swigregister
itkNormalizeToConstantImageFilterIF2IF2_swigregister(itkNormalizeToConstantImageFilterIF2IF2)

def itkNormalizeToConstantImageFilterIF2IF2___New_orig__() -> "itkNormalizeToConstantImageFilterIF2IF2_Pointer":
    """itkNormalizeToConstantImageFilterIF2IF2___New_orig__() -> itkNormalizeToConstantImageFilterIF2IF2_Pointer"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2___New_orig__()

def itkNormalizeToConstantImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIF2IF2 *":
    """itkNormalizeToConstantImageFilterIF2IF2_cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIF2IF2"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF2IF2_cast(obj)

class itkNormalizeToConstantImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkNormalizeToConstantImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeToConstantImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkNormalizeToConstantImageFilterIF3IF3_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeToConstantImageFilterIF3IF3_Pointer":
        """Clone(itkNormalizeToConstantImageFilterIF3IF3 self) -> itkNormalizeToConstantImageFilterIF3IF3_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_Clone(self)


    def SetConstant(self, _arg: 'double const') -> "void":
        """SetConstant(itkNormalizeToConstantImageFilterIF3IF3 self, double const _arg)"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_SetConstant(self, _arg)


    def GetConstant(self) -> "double":
        """GetConstant(itkNormalizeToConstantImageFilterIF3IF3 self) -> double"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_GetConstant(self)

    InputHasPixelTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_InputHasPixelTraitsCheck
    InputHasNumericTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkNormalizeToConstantImageFilterPython.delete_itkNormalizeToConstantImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIF3IF3"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeToConstantImageFilterIF3IF3 *":
        """GetPointer(itkNormalizeToConstantImageFilterIF3IF3 self) -> itkNormalizeToConstantImageFilterIF3IF3"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeToConstantImageFilterIF3IF3

        Create a new object of the class itkNormalizeToConstantImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeToConstantImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeToConstantImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeToConstantImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeToConstantImageFilterIF3IF3.Clone = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_Clone, None, itkNormalizeToConstantImageFilterIF3IF3)
itkNormalizeToConstantImageFilterIF3IF3.SetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_SetConstant, None, itkNormalizeToConstantImageFilterIF3IF3)
itkNormalizeToConstantImageFilterIF3IF3.GetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_GetConstant, None, itkNormalizeToConstantImageFilterIF3IF3)
itkNormalizeToConstantImageFilterIF3IF3.GetPointer = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_GetPointer, None, itkNormalizeToConstantImageFilterIF3IF3)
itkNormalizeToConstantImageFilterIF3IF3_swigregister = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_swigregister
itkNormalizeToConstantImageFilterIF3IF3_swigregister(itkNormalizeToConstantImageFilterIF3IF3)

def itkNormalizeToConstantImageFilterIF3IF3___New_orig__() -> "itkNormalizeToConstantImageFilterIF3IF3_Pointer":
    """itkNormalizeToConstantImageFilterIF3IF3___New_orig__() -> itkNormalizeToConstantImageFilterIF3IF3_Pointer"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3___New_orig__()

def itkNormalizeToConstantImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIF3IF3 *":
    """itkNormalizeToConstantImageFilterIF3IF3_cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIF3IF3"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIF3IF3_cast(obj)

class itkNormalizeToConstantImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkNormalizeToConstantImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeToConstantImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkNormalizeToConstantImageFilterISS2ISS2_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeToConstantImageFilterISS2ISS2_Pointer":
        """Clone(itkNormalizeToConstantImageFilterISS2ISS2 self) -> itkNormalizeToConstantImageFilterISS2ISS2_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_Clone(self)


    def SetConstant(self, _arg: 'double const') -> "void":
        """SetConstant(itkNormalizeToConstantImageFilterISS2ISS2 self, double const _arg)"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_SetConstant(self, _arg)


    def GetConstant(self) -> "double":
        """GetConstant(itkNormalizeToConstantImageFilterISS2ISS2 self) -> double"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_GetConstant(self)

    InputHasPixelTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_InputHasPixelTraitsCheck
    InputHasNumericTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkNormalizeToConstantImageFilterPython.delete_itkNormalizeToConstantImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterISS2ISS2"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeToConstantImageFilterISS2ISS2 *":
        """GetPointer(itkNormalizeToConstantImageFilterISS2ISS2 self) -> itkNormalizeToConstantImageFilterISS2ISS2"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeToConstantImageFilterISS2ISS2

        Create a new object of the class itkNormalizeToConstantImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeToConstantImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeToConstantImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeToConstantImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeToConstantImageFilterISS2ISS2.Clone = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_Clone, None, itkNormalizeToConstantImageFilterISS2ISS2)
itkNormalizeToConstantImageFilterISS2ISS2.SetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_SetConstant, None, itkNormalizeToConstantImageFilterISS2ISS2)
itkNormalizeToConstantImageFilterISS2ISS2.GetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_GetConstant, None, itkNormalizeToConstantImageFilterISS2ISS2)
itkNormalizeToConstantImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_GetPointer, None, itkNormalizeToConstantImageFilterISS2ISS2)
itkNormalizeToConstantImageFilterISS2ISS2_swigregister = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_swigregister
itkNormalizeToConstantImageFilterISS2ISS2_swigregister(itkNormalizeToConstantImageFilterISS2ISS2)

def itkNormalizeToConstantImageFilterISS2ISS2___New_orig__() -> "itkNormalizeToConstantImageFilterISS2ISS2_Pointer":
    """itkNormalizeToConstantImageFilterISS2ISS2___New_orig__() -> itkNormalizeToConstantImageFilterISS2ISS2_Pointer"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2___New_orig__()

def itkNormalizeToConstantImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterISS2ISS2 *":
    """itkNormalizeToConstantImageFilterISS2ISS2_cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterISS2ISS2"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS2ISS2_cast(obj)

class itkNormalizeToConstantImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkNormalizeToConstantImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeToConstantImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkNormalizeToConstantImageFilterISS3ISS3_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeToConstantImageFilterISS3ISS3_Pointer":
        """Clone(itkNormalizeToConstantImageFilterISS3ISS3 self) -> itkNormalizeToConstantImageFilterISS3ISS3_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_Clone(self)


    def SetConstant(self, _arg: 'double const') -> "void":
        """SetConstant(itkNormalizeToConstantImageFilterISS3ISS3 self, double const _arg)"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_SetConstant(self, _arg)


    def GetConstant(self) -> "double":
        """GetConstant(itkNormalizeToConstantImageFilterISS3ISS3 self) -> double"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_GetConstant(self)

    InputHasPixelTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_InputHasPixelTraitsCheck
    InputHasNumericTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkNormalizeToConstantImageFilterPython.delete_itkNormalizeToConstantImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterISS3ISS3"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeToConstantImageFilterISS3ISS3 *":
        """GetPointer(itkNormalizeToConstantImageFilterISS3ISS3 self) -> itkNormalizeToConstantImageFilterISS3ISS3"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeToConstantImageFilterISS3ISS3

        Create a new object of the class itkNormalizeToConstantImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeToConstantImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeToConstantImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeToConstantImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeToConstantImageFilterISS3ISS3.Clone = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_Clone, None, itkNormalizeToConstantImageFilterISS3ISS3)
itkNormalizeToConstantImageFilterISS3ISS3.SetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_SetConstant, None, itkNormalizeToConstantImageFilterISS3ISS3)
itkNormalizeToConstantImageFilterISS3ISS3.GetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_GetConstant, None, itkNormalizeToConstantImageFilterISS3ISS3)
itkNormalizeToConstantImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_GetPointer, None, itkNormalizeToConstantImageFilterISS3ISS3)
itkNormalizeToConstantImageFilterISS3ISS3_swigregister = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_swigregister
itkNormalizeToConstantImageFilterISS3ISS3_swigregister(itkNormalizeToConstantImageFilterISS3ISS3)

def itkNormalizeToConstantImageFilterISS3ISS3___New_orig__() -> "itkNormalizeToConstantImageFilterISS3ISS3_Pointer":
    """itkNormalizeToConstantImageFilterISS3ISS3___New_orig__() -> itkNormalizeToConstantImageFilterISS3ISS3_Pointer"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3___New_orig__()

def itkNormalizeToConstantImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterISS3ISS3 *":
    """itkNormalizeToConstantImageFilterISS3ISS3_cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterISS3ISS3"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterISS3ISS3_cast(obj)

class itkNormalizeToConstantImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkNormalizeToConstantImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeToConstantImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkNormalizeToConstantImageFilterIUC2IUC2_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeToConstantImageFilterIUC2IUC2_Pointer":
        """Clone(itkNormalizeToConstantImageFilterIUC2IUC2 self) -> itkNormalizeToConstantImageFilterIUC2IUC2_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_Clone(self)


    def SetConstant(self, _arg: 'double const') -> "void":
        """SetConstant(itkNormalizeToConstantImageFilterIUC2IUC2 self, double const _arg)"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_SetConstant(self, _arg)


    def GetConstant(self) -> "double":
        """GetConstant(itkNormalizeToConstantImageFilterIUC2IUC2 self) -> double"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_GetConstant(self)

    InputHasPixelTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_InputHasPixelTraitsCheck
    InputHasNumericTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkNormalizeToConstantImageFilterPython.delete_itkNormalizeToConstantImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIUC2IUC2"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeToConstantImageFilterIUC2IUC2 *":
        """GetPointer(itkNormalizeToConstantImageFilterIUC2IUC2 self) -> itkNormalizeToConstantImageFilterIUC2IUC2"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeToConstantImageFilterIUC2IUC2

        Create a new object of the class itkNormalizeToConstantImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeToConstantImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeToConstantImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeToConstantImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeToConstantImageFilterIUC2IUC2.Clone = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_Clone, None, itkNormalizeToConstantImageFilterIUC2IUC2)
itkNormalizeToConstantImageFilterIUC2IUC2.SetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_SetConstant, None, itkNormalizeToConstantImageFilterIUC2IUC2)
itkNormalizeToConstantImageFilterIUC2IUC2.GetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_GetConstant, None, itkNormalizeToConstantImageFilterIUC2IUC2)
itkNormalizeToConstantImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_GetPointer, None, itkNormalizeToConstantImageFilterIUC2IUC2)
itkNormalizeToConstantImageFilterIUC2IUC2_swigregister = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_swigregister
itkNormalizeToConstantImageFilterIUC2IUC2_swigregister(itkNormalizeToConstantImageFilterIUC2IUC2)

def itkNormalizeToConstantImageFilterIUC2IUC2___New_orig__() -> "itkNormalizeToConstantImageFilterIUC2IUC2_Pointer":
    """itkNormalizeToConstantImageFilterIUC2IUC2___New_orig__() -> itkNormalizeToConstantImageFilterIUC2IUC2_Pointer"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2___New_orig__()

def itkNormalizeToConstantImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIUC2IUC2 *":
    """itkNormalizeToConstantImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIUC2IUC2"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC2IUC2_cast(obj)

class itkNormalizeToConstantImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkNormalizeToConstantImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNormalizeToConstantImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkNormalizeToConstantImageFilterIUC3IUC3_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNormalizeToConstantImageFilterIUC3IUC3_Pointer":
        """Clone(itkNormalizeToConstantImageFilterIUC3IUC3 self) -> itkNormalizeToConstantImageFilterIUC3IUC3_Pointer"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_Clone(self)


    def SetConstant(self, _arg: 'double const') -> "void":
        """SetConstant(itkNormalizeToConstantImageFilterIUC3IUC3 self, double const _arg)"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_SetConstant(self, _arg)


    def GetConstant(self) -> "double":
        """GetConstant(itkNormalizeToConstantImageFilterIUC3IUC3 self) -> double"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_GetConstant(self)

    InputHasPixelTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_InputHasPixelTraitsCheck
    InputHasNumericTraitsCheck = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkNormalizeToConstantImageFilterPython.delete_itkNormalizeToConstantImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIUC3IUC3"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNormalizeToConstantImageFilterIUC3IUC3 *":
        """GetPointer(itkNormalizeToConstantImageFilterIUC3IUC3 self) -> itkNormalizeToConstantImageFilterIUC3IUC3"""
        return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalizeToConstantImageFilterIUC3IUC3

        Create a new object of the class itkNormalizeToConstantImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalizeToConstantImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalizeToConstantImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalizeToConstantImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalizeToConstantImageFilterIUC3IUC3.Clone = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_Clone, None, itkNormalizeToConstantImageFilterIUC3IUC3)
itkNormalizeToConstantImageFilterIUC3IUC3.SetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_SetConstant, None, itkNormalizeToConstantImageFilterIUC3IUC3)
itkNormalizeToConstantImageFilterIUC3IUC3.GetConstant = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_GetConstant, None, itkNormalizeToConstantImageFilterIUC3IUC3)
itkNormalizeToConstantImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_GetPointer, None, itkNormalizeToConstantImageFilterIUC3IUC3)
itkNormalizeToConstantImageFilterIUC3IUC3_swigregister = _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_swigregister
itkNormalizeToConstantImageFilterIUC3IUC3_swigregister(itkNormalizeToConstantImageFilterIUC3IUC3)

def itkNormalizeToConstantImageFilterIUC3IUC3___New_orig__() -> "itkNormalizeToConstantImageFilterIUC3IUC3_Pointer":
    """itkNormalizeToConstantImageFilterIUC3IUC3___New_orig__() -> itkNormalizeToConstantImageFilterIUC3IUC3_Pointer"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3___New_orig__()

def itkNormalizeToConstantImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkNormalizeToConstantImageFilterIUC3IUC3 *":
    """itkNormalizeToConstantImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkNormalizeToConstantImageFilterIUC3IUC3"""
    return _itkNormalizeToConstantImageFilterPython.itkNormalizeToConstantImageFilterIUC3IUC3_cast(obj)



