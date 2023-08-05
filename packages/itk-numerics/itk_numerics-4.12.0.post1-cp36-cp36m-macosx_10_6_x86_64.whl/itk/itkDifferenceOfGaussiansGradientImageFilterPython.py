# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDifferenceOfGaussiansGradientImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDifferenceOfGaussiansGradientImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDifferenceOfGaussiansGradientImageFilterPython')
    _itkDifferenceOfGaussiansGradientImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDifferenceOfGaussiansGradientImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDifferenceOfGaussiansGradientImageFilterPython
            return _itkDifferenceOfGaussiansGradientImageFilterPython
        try:
            _mod = imp.load_module('_itkDifferenceOfGaussiansGradientImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDifferenceOfGaussiansGradientImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDifferenceOfGaussiansGradientImageFilterPython
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


import ITKCommonBasePython
import pyBasePython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
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

def itkDifferenceOfGaussiansGradientImageFilterIF3F_New():
  return itkDifferenceOfGaussiansGradientImageFilterIF3F.New()


def itkDifferenceOfGaussiansGradientImageFilterIUC3F_New():
  return itkDifferenceOfGaussiansGradientImageFilterIUC3F.New()


def itkDifferenceOfGaussiansGradientImageFilterISS3F_New():
  return itkDifferenceOfGaussiansGradientImageFilterISS3F.New()


def itkDifferenceOfGaussiansGradientImageFilterIF2F_New():
  return itkDifferenceOfGaussiansGradientImageFilterIF2F.New()


def itkDifferenceOfGaussiansGradientImageFilterIUC2F_New():
  return itkDifferenceOfGaussiansGradientImageFilterIUC2F.New()


def itkDifferenceOfGaussiansGradientImageFilterISS2F_New():
  return itkDifferenceOfGaussiansGradientImageFilterISS2F.New()

class itkDifferenceOfGaussiansGradientImageFilterIF2F(itkImageToImageFilterBPython.itkImageToImageFilterIF2ICVF22):
    """Proxy of C++ itkDifferenceOfGaussiansGradientImageFilterIF2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIF2F_Pointer":
        """__New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIF2F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDifferenceOfGaussiansGradientImageFilterIF2F_Pointer":
        """Clone(itkDifferenceOfGaussiansGradientImageFilterIF2F self) -> itkDifferenceOfGaussiansGradientImageFilterIF2F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_Clone(self)


    def GetWidth(self) -> "unsigned int":
        """GetWidth(itkDifferenceOfGaussiansGradientImageFilterIF2F self) -> unsigned int"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_GetWidth(self)


    def SetWidth(self, _arg: 'unsigned int const') -> "void":
        """SetWidth(itkDifferenceOfGaussiansGradientImageFilterIF2F self, unsigned int const _arg)"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_SetWidth(self, _arg)

    DataTypeHasNumericTraitsCheck = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_DataTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkDifferenceOfGaussiansGradientImageFilterPython.delete_itkDifferenceOfGaussiansGradientImageFilterIF2F

    def cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIF2F *":
        """cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIF2F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDifferenceOfGaussiansGradientImageFilterIF2F *":
        """GetPointer(itkDifferenceOfGaussiansGradientImageFilterIF2F self) -> itkDifferenceOfGaussiansGradientImageFilterIF2F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDifferenceOfGaussiansGradientImageFilterIF2F

        Create a new object of the class itkDifferenceOfGaussiansGradientImageFilterIF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDifferenceOfGaussiansGradientImageFilterIF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDifferenceOfGaussiansGradientImageFilterIF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDifferenceOfGaussiansGradientImageFilterIF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDifferenceOfGaussiansGradientImageFilterIF2F.Clone = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_Clone, None, itkDifferenceOfGaussiansGradientImageFilterIF2F)
itkDifferenceOfGaussiansGradientImageFilterIF2F.GetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_GetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIF2F)
itkDifferenceOfGaussiansGradientImageFilterIF2F.SetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_SetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIF2F)
itkDifferenceOfGaussiansGradientImageFilterIF2F.GetPointer = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_GetPointer, None, itkDifferenceOfGaussiansGradientImageFilterIF2F)
itkDifferenceOfGaussiansGradientImageFilterIF2F_swigregister = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_swigregister
itkDifferenceOfGaussiansGradientImageFilterIF2F_swigregister(itkDifferenceOfGaussiansGradientImageFilterIF2F)

def itkDifferenceOfGaussiansGradientImageFilterIF2F___New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIF2F_Pointer":
    """itkDifferenceOfGaussiansGradientImageFilterIF2F___New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIF2F_Pointer"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F___New_orig__()

def itkDifferenceOfGaussiansGradientImageFilterIF2F_cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIF2F *":
    """itkDifferenceOfGaussiansGradientImageFilterIF2F_cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIF2F"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF2F_cast(obj)

class itkDifferenceOfGaussiansGradientImageFilterIF3F(itkImageToImageFilterBPython.itkImageToImageFilterIF3ICVF33):
    """Proxy of C++ itkDifferenceOfGaussiansGradientImageFilterIF3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIF3F_Pointer":
        """__New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIF3F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDifferenceOfGaussiansGradientImageFilterIF3F_Pointer":
        """Clone(itkDifferenceOfGaussiansGradientImageFilterIF3F self) -> itkDifferenceOfGaussiansGradientImageFilterIF3F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_Clone(self)


    def GetWidth(self) -> "unsigned int":
        """GetWidth(itkDifferenceOfGaussiansGradientImageFilterIF3F self) -> unsigned int"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_GetWidth(self)


    def SetWidth(self, _arg: 'unsigned int const') -> "void":
        """SetWidth(itkDifferenceOfGaussiansGradientImageFilterIF3F self, unsigned int const _arg)"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_SetWidth(self, _arg)

    DataTypeHasNumericTraitsCheck = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_DataTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkDifferenceOfGaussiansGradientImageFilterPython.delete_itkDifferenceOfGaussiansGradientImageFilterIF3F

    def cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIF3F *":
        """cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIF3F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDifferenceOfGaussiansGradientImageFilterIF3F *":
        """GetPointer(itkDifferenceOfGaussiansGradientImageFilterIF3F self) -> itkDifferenceOfGaussiansGradientImageFilterIF3F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDifferenceOfGaussiansGradientImageFilterIF3F

        Create a new object of the class itkDifferenceOfGaussiansGradientImageFilterIF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDifferenceOfGaussiansGradientImageFilterIF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDifferenceOfGaussiansGradientImageFilterIF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDifferenceOfGaussiansGradientImageFilterIF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDifferenceOfGaussiansGradientImageFilterIF3F.Clone = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_Clone, None, itkDifferenceOfGaussiansGradientImageFilterIF3F)
itkDifferenceOfGaussiansGradientImageFilterIF3F.GetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_GetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIF3F)
itkDifferenceOfGaussiansGradientImageFilterIF3F.SetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_SetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIF3F)
itkDifferenceOfGaussiansGradientImageFilterIF3F.GetPointer = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_GetPointer, None, itkDifferenceOfGaussiansGradientImageFilterIF3F)
itkDifferenceOfGaussiansGradientImageFilterIF3F_swigregister = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_swigregister
itkDifferenceOfGaussiansGradientImageFilterIF3F_swigregister(itkDifferenceOfGaussiansGradientImageFilterIF3F)

def itkDifferenceOfGaussiansGradientImageFilterIF3F___New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIF3F_Pointer":
    """itkDifferenceOfGaussiansGradientImageFilterIF3F___New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIF3F_Pointer"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F___New_orig__()

def itkDifferenceOfGaussiansGradientImageFilterIF3F_cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIF3F *":
    """itkDifferenceOfGaussiansGradientImageFilterIF3F_cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIF3F"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIF3F_cast(obj)

class itkDifferenceOfGaussiansGradientImageFilterISS2F(itkImageToImageFilterBPython.itkImageToImageFilterISS2ICVF22):
    """Proxy of C++ itkDifferenceOfGaussiansGradientImageFilterISS2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterISS2F_Pointer":
        """__New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterISS2F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDifferenceOfGaussiansGradientImageFilterISS2F_Pointer":
        """Clone(itkDifferenceOfGaussiansGradientImageFilterISS2F self) -> itkDifferenceOfGaussiansGradientImageFilterISS2F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_Clone(self)


    def GetWidth(self) -> "unsigned int":
        """GetWidth(itkDifferenceOfGaussiansGradientImageFilterISS2F self) -> unsigned int"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_GetWidth(self)


    def SetWidth(self, _arg: 'unsigned int const') -> "void":
        """SetWidth(itkDifferenceOfGaussiansGradientImageFilterISS2F self, unsigned int const _arg)"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_SetWidth(self, _arg)

    DataTypeHasNumericTraitsCheck = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_DataTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkDifferenceOfGaussiansGradientImageFilterPython.delete_itkDifferenceOfGaussiansGradientImageFilterISS2F

    def cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterISS2F *":
        """cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterISS2F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDifferenceOfGaussiansGradientImageFilterISS2F *":
        """GetPointer(itkDifferenceOfGaussiansGradientImageFilterISS2F self) -> itkDifferenceOfGaussiansGradientImageFilterISS2F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDifferenceOfGaussiansGradientImageFilterISS2F

        Create a new object of the class itkDifferenceOfGaussiansGradientImageFilterISS2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDifferenceOfGaussiansGradientImageFilterISS2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDifferenceOfGaussiansGradientImageFilterISS2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDifferenceOfGaussiansGradientImageFilterISS2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDifferenceOfGaussiansGradientImageFilterISS2F.Clone = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_Clone, None, itkDifferenceOfGaussiansGradientImageFilterISS2F)
itkDifferenceOfGaussiansGradientImageFilterISS2F.GetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_GetWidth, None, itkDifferenceOfGaussiansGradientImageFilterISS2F)
itkDifferenceOfGaussiansGradientImageFilterISS2F.SetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_SetWidth, None, itkDifferenceOfGaussiansGradientImageFilterISS2F)
itkDifferenceOfGaussiansGradientImageFilterISS2F.GetPointer = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_GetPointer, None, itkDifferenceOfGaussiansGradientImageFilterISS2F)
itkDifferenceOfGaussiansGradientImageFilterISS2F_swigregister = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_swigregister
itkDifferenceOfGaussiansGradientImageFilterISS2F_swigregister(itkDifferenceOfGaussiansGradientImageFilterISS2F)

def itkDifferenceOfGaussiansGradientImageFilterISS2F___New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterISS2F_Pointer":
    """itkDifferenceOfGaussiansGradientImageFilterISS2F___New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterISS2F_Pointer"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F___New_orig__()

def itkDifferenceOfGaussiansGradientImageFilterISS2F_cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterISS2F *":
    """itkDifferenceOfGaussiansGradientImageFilterISS2F_cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterISS2F"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS2F_cast(obj)

class itkDifferenceOfGaussiansGradientImageFilterISS3F(itkImageToImageFilterBPython.itkImageToImageFilterISS3ICVF33):
    """Proxy of C++ itkDifferenceOfGaussiansGradientImageFilterISS3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterISS3F_Pointer":
        """__New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterISS3F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDifferenceOfGaussiansGradientImageFilterISS3F_Pointer":
        """Clone(itkDifferenceOfGaussiansGradientImageFilterISS3F self) -> itkDifferenceOfGaussiansGradientImageFilterISS3F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_Clone(self)


    def GetWidth(self) -> "unsigned int":
        """GetWidth(itkDifferenceOfGaussiansGradientImageFilterISS3F self) -> unsigned int"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_GetWidth(self)


    def SetWidth(self, _arg: 'unsigned int const') -> "void":
        """SetWidth(itkDifferenceOfGaussiansGradientImageFilterISS3F self, unsigned int const _arg)"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_SetWidth(self, _arg)

    DataTypeHasNumericTraitsCheck = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_DataTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkDifferenceOfGaussiansGradientImageFilterPython.delete_itkDifferenceOfGaussiansGradientImageFilterISS3F

    def cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterISS3F *":
        """cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterISS3F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDifferenceOfGaussiansGradientImageFilterISS3F *":
        """GetPointer(itkDifferenceOfGaussiansGradientImageFilterISS3F self) -> itkDifferenceOfGaussiansGradientImageFilterISS3F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDifferenceOfGaussiansGradientImageFilterISS3F

        Create a new object of the class itkDifferenceOfGaussiansGradientImageFilterISS3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDifferenceOfGaussiansGradientImageFilterISS3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDifferenceOfGaussiansGradientImageFilterISS3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDifferenceOfGaussiansGradientImageFilterISS3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDifferenceOfGaussiansGradientImageFilterISS3F.Clone = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_Clone, None, itkDifferenceOfGaussiansGradientImageFilterISS3F)
itkDifferenceOfGaussiansGradientImageFilterISS3F.GetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_GetWidth, None, itkDifferenceOfGaussiansGradientImageFilterISS3F)
itkDifferenceOfGaussiansGradientImageFilterISS3F.SetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_SetWidth, None, itkDifferenceOfGaussiansGradientImageFilterISS3F)
itkDifferenceOfGaussiansGradientImageFilterISS3F.GetPointer = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_GetPointer, None, itkDifferenceOfGaussiansGradientImageFilterISS3F)
itkDifferenceOfGaussiansGradientImageFilterISS3F_swigregister = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_swigregister
itkDifferenceOfGaussiansGradientImageFilterISS3F_swigregister(itkDifferenceOfGaussiansGradientImageFilterISS3F)

def itkDifferenceOfGaussiansGradientImageFilterISS3F___New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterISS3F_Pointer":
    """itkDifferenceOfGaussiansGradientImageFilterISS3F___New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterISS3F_Pointer"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F___New_orig__()

def itkDifferenceOfGaussiansGradientImageFilterISS3F_cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterISS3F *":
    """itkDifferenceOfGaussiansGradientImageFilterISS3F_cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterISS3F"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterISS3F_cast(obj)

class itkDifferenceOfGaussiansGradientImageFilterIUC2F(itkImageToImageFilterBPython.itkImageToImageFilterIUC2ICVF22):
    """Proxy of C++ itkDifferenceOfGaussiansGradientImageFilterIUC2F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIUC2F_Pointer":
        """__New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIUC2F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDifferenceOfGaussiansGradientImageFilterIUC2F_Pointer":
        """Clone(itkDifferenceOfGaussiansGradientImageFilterIUC2F self) -> itkDifferenceOfGaussiansGradientImageFilterIUC2F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_Clone(self)


    def GetWidth(self) -> "unsigned int":
        """GetWidth(itkDifferenceOfGaussiansGradientImageFilterIUC2F self) -> unsigned int"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_GetWidth(self)


    def SetWidth(self, _arg: 'unsigned int const') -> "void":
        """SetWidth(itkDifferenceOfGaussiansGradientImageFilterIUC2F self, unsigned int const _arg)"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_SetWidth(self, _arg)

    DataTypeHasNumericTraitsCheck = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_DataTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkDifferenceOfGaussiansGradientImageFilterPython.delete_itkDifferenceOfGaussiansGradientImageFilterIUC2F

    def cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIUC2F *":
        """cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIUC2F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDifferenceOfGaussiansGradientImageFilterIUC2F *":
        """GetPointer(itkDifferenceOfGaussiansGradientImageFilterIUC2F self) -> itkDifferenceOfGaussiansGradientImageFilterIUC2F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDifferenceOfGaussiansGradientImageFilterIUC2F

        Create a new object of the class itkDifferenceOfGaussiansGradientImageFilterIUC2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDifferenceOfGaussiansGradientImageFilterIUC2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDifferenceOfGaussiansGradientImageFilterIUC2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDifferenceOfGaussiansGradientImageFilterIUC2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDifferenceOfGaussiansGradientImageFilterIUC2F.Clone = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_Clone, None, itkDifferenceOfGaussiansGradientImageFilterIUC2F)
itkDifferenceOfGaussiansGradientImageFilterIUC2F.GetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_GetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIUC2F)
itkDifferenceOfGaussiansGradientImageFilterIUC2F.SetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_SetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIUC2F)
itkDifferenceOfGaussiansGradientImageFilterIUC2F.GetPointer = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_GetPointer, None, itkDifferenceOfGaussiansGradientImageFilterIUC2F)
itkDifferenceOfGaussiansGradientImageFilterIUC2F_swigregister = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_swigregister
itkDifferenceOfGaussiansGradientImageFilterIUC2F_swigregister(itkDifferenceOfGaussiansGradientImageFilterIUC2F)

def itkDifferenceOfGaussiansGradientImageFilterIUC2F___New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIUC2F_Pointer":
    """itkDifferenceOfGaussiansGradientImageFilterIUC2F___New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIUC2F_Pointer"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F___New_orig__()

def itkDifferenceOfGaussiansGradientImageFilterIUC2F_cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIUC2F *":
    """itkDifferenceOfGaussiansGradientImageFilterIUC2F_cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIUC2F"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC2F_cast(obj)

class itkDifferenceOfGaussiansGradientImageFilterIUC3F(itkImageToImageFilterBPython.itkImageToImageFilterIUC3ICVF33):
    """Proxy of C++ itkDifferenceOfGaussiansGradientImageFilterIUC3F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIUC3F_Pointer":
        """__New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIUC3F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDifferenceOfGaussiansGradientImageFilterIUC3F_Pointer":
        """Clone(itkDifferenceOfGaussiansGradientImageFilterIUC3F self) -> itkDifferenceOfGaussiansGradientImageFilterIUC3F_Pointer"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_Clone(self)


    def GetWidth(self) -> "unsigned int":
        """GetWidth(itkDifferenceOfGaussiansGradientImageFilterIUC3F self) -> unsigned int"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_GetWidth(self)


    def SetWidth(self, _arg: 'unsigned int const') -> "void":
        """SetWidth(itkDifferenceOfGaussiansGradientImageFilterIUC3F self, unsigned int const _arg)"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_SetWidth(self, _arg)

    DataTypeHasNumericTraitsCheck = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_DataTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkDifferenceOfGaussiansGradientImageFilterPython.delete_itkDifferenceOfGaussiansGradientImageFilterIUC3F

    def cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIUC3F *":
        """cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIUC3F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDifferenceOfGaussiansGradientImageFilterIUC3F *":
        """GetPointer(itkDifferenceOfGaussiansGradientImageFilterIUC3F self) -> itkDifferenceOfGaussiansGradientImageFilterIUC3F"""
        return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDifferenceOfGaussiansGradientImageFilterIUC3F

        Create a new object of the class itkDifferenceOfGaussiansGradientImageFilterIUC3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDifferenceOfGaussiansGradientImageFilterIUC3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDifferenceOfGaussiansGradientImageFilterIUC3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDifferenceOfGaussiansGradientImageFilterIUC3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDifferenceOfGaussiansGradientImageFilterIUC3F.Clone = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_Clone, None, itkDifferenceOfGaussiansGradientImageFilterIUC3F)
itkDifferenceOfGaussiansGradientImageFilterIUC3F.GetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_GetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIUC3F)
itkDifferenceOfGaussiansGradientImageFilterIUC3F.SetWidth = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_SetWidth, None, itkDifferenceOfGaussiansGradientImageFilterIUC3F)
itkDifferenceOfGaussiansGradientImageFilterIUC3F.GetPointer = new_instancemethod(_itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_GetPointer, None, itkDifferenceOfGaussiansGradientImageFilterIUC3F)
itkDifferenceOfGaussiansGradientImageFilterIUC3F_swigregister = _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_swigregister
itkDifferenceOfGaussiansGradientImageFilterIUC3F_swigregister(itkDifferenceOfGaussiansGradientImageFilterIUC3F)

def itkDifferenceOfGaussiansGradientImageFilterIUC3F___New_orig__() -> "itkDifferenceOfGaussiansGradientImageFilterIUC3F_Pointer":
    """itkDifferenceOfGaussiansGradientImageFilterIUC3F___New_orig__() -> itkDifferenceOfGaussiansGradientImageFilterIUC3F_Pointer"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F___New_orig__()

def itkDifferenceOfGaussiansGradientImageFilterIUC3F_cast(obj: 'itkLightObject') -> "itkDifferenceOfGaussiansGradientImageFilterIUC3F *":
    """itkDifferenceOfGaussiansGradientImageFilterIUC3F_cast(itkLightObject obj) -> itkDifferenceOfGaussiansGradientImageFilterIUC3F"""
    return _itkDifferenceOfGaussiansGradientImageFilterPython.itkDifferenceOfGaussiansGradientImageFilterIUC3F_cast(obj)



