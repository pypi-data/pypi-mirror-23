# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryMinMaxCurvatureFlowImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBinaryMinMaxCurvatureFlowImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBinaryMinMaxCurvatureFlowImageFilterPython')
    _itkBinaryMinMaxCurvatureFlowImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryMinMaxCurvatureFlowImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryMinMaxCurvatureFlowImageFilterPython
            return _itkBinaryMinMaxCurvatureFlowImageFilterPython
        try:
            _mod = imp.load_module('_itkBinaryMinMaxCurvatureFlowImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBinaryMinMaxCurvatureFlowImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryMinMaxCurvatureFlowImageFilterPython
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


import itkMinMaxCurvatureFlowImageFilterPython
import itkCurvatureFlowImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkDenseFiniteDifferenceImageFilterPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
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
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython

def itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_New():
  return itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.New()


def itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_New():
  return itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.New()

class itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2(itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2):
    """Proxy of C++ itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """Clone(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """SetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self, double const _arg)"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self) -> double"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_GetThreshold(self)

    InputConvertibleToOutputCheck = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkBinaryMinMaxCurvatureFlowImageFilterPython.delete_itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 *":
        """GetPointer(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2

        Create a new object of the class itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.Clone = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Clone, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.SetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_SetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.GetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_GetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.GetPointer = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_GetPointer, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_swigregister = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_swigregister
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_swigregister(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)

def itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

def itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 *":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

class itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3(itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3):
    """Proxy of C++ itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """Clone(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """SetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self, double const _arg)"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self) -> double"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_GetThreshold(self)

    InputConvertibleToOutputCheck = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkBinaryMinMaxCurvatureFlowImageFilterPython.delete_itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 *":
        """GetPointer(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3

        Create a new object of the class itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.Clone = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Clone, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.SetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_SetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.GetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_GetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.GetPointer = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_GetPointer, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_swigregister = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_swigregister
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_swigregister(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)

def itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

def itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 *":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)



