# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSobelEdgeDetectionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSobelEdgeDetectionImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSobelEdgeDetectionImageFilterPython')
    _itkSobelEdgeDetectionImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSobelEdgeDetectionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSobelEdgeDetectionImageFilterPython
            return _itkSobelEdgeDetectionImageFilterPython
        try:
            _mod = imp.load_module('_itkSobelEdgeDetectionImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSobelEdgeDetectionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSobelEdgeDetectionImageFilterPython
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

def itkSobelEdgeDetectionImageFilterIF3IF3_New():
  return itkSobelEdgeDetectionImageFilterIF3IF3.New()


def itkSobelEdgeDetectionImageFilterIF2IF2_New():
  return itkSobelEdgeDetectionImageFilterIF2IF2.New()

class itkSobelEdgeDetectionImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkSobelEdgeDetectionImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSobelEdgeDetectionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSobelEdgeDetectionImageFilterIF2IF2_Pointer"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSobelEdgeDetectionImageFilterIF2IF2_Pointer":
        """Clone(itkSobelEdgeDetectionImageFilterIF2IF2 self) -> itkSobelEdgeDetectionImageFilterIF2IF2_Pointer"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkSobelEdgeDetectionImageFilterIF2IF2 self)"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_SameDimensionCheck
    OutputHasNumericTraitsCheck = _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkSobelEdgeDetectionImageFilterPython.delete_itkSobelEdgeDetectionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSobelEdgeDetectionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSobelEdgeDetectionImageFilterIF2IF2"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSobelEdgeDetectionImageFilterIF2IF2 *":
        """GetPointer(itkSobelEdgeDetectionImageFilterIF2IF2 self) -> itkSobelEdgeDetectionImageFilterIF2IF2"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSobelEdgeDetectionImageFilterIF2IF2

        Create a new object of the class itkSobelEdgeDetectionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSobelEdgeDetectionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSobelEdgeDetectionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSobelEdgeDetectionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSobelEdgeDetectionImageFilterIF2IF2.Clone = new_instancemethod(_itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_Clone, None, itkSobelEdgeDetectionImageFilterIF2IF2)
itkSobelEdgeDetectionImageFilterIF2IF2.GenerateInputRequestedRegion = new_instancemethod(_itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_GenerateInputRequestedRegion, None, itkSobelEdgeDetectionImageFilterIF2IF2)
itkSobelEdgeDetectionImageFilterIF2IF2.GetPointer = new_instancemethod(_itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_GetPointer, None, itkSobelEdgeDetectionImageFilterIF2IF2)
itkSobelEdgeDetectionImageFilterIF2IF2_swigregister = _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_swigregister
itkSobelEdgeDetectionImageFilterIF2IF2_swigregister(itkSobelEdgeDetectionImageFilterIF2IF2)

def itkSobelEdgeDetectionImageFilterIF2IF2___New_orig__() -> "itkSobelEdgeDetectionImageFilterIF2IF2_Pointer":
    """itkSobelEdgeDetectionImageFilterIF2IF2___New_orig__() -> itkSobelEdgeDetectionImageFilterIF2IF2_Pointer"""
    return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2___New_orig__()

def itkSobelEdgeDetectionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSobelEdgeDetectionImageFilterIF2IF2 *":
    """itkSobelEdgeDetectionImageFilterIF2IF2_cast(itkLightObject obj) -> itkSobelEdgeDetectionImageFilterIF2IF2"""
    return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF2IF2_cast(obj)

class itkSobelEdgeDetectionImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkSobelEdgeDetectionImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSobelEdgeDetectionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSobelEdgeDetectionImageFilterIF3IF3_Pointer"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSobelEdgeDetectionImageFilterIF3IF3_Pointer":
        """Clone(itkSobelEdgeDetectionImageFilterIF3IF3 self) -> itkSobelEdgeDetectionImageFilterIF3IF3_Pointer"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkSobelEdgeDetectionImageFilterIF3IF3 self)"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_GenerateInputRequestedRegion(self)

    SameDimensionCheck = _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_SameDimensionCheck
    OutputHasNumericTraitsCheck = _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkSobelEdgeDetectionImageFilterPython.delete_itkSobelEdgeDetectionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSobelEdgeDetectionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSobelEdgeDetectionImageFilterIF3IF3"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSobelEdgeDetectionImageFilterIF3IF3 *":
        """GetPointer(itkSobelEdgeDetectionImageFilterIF3IF3 self) -> itkSobelEdgeDetectionImageFilterIF3IF3"""
        return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSobelEdgeDetectionImageFilterIF3IF3

        Create a new object of the class itkSobelEdgeDetectionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSobelEdgeDetectionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSobelEdgeDetectionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSobelEdgeDetectionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSobelEdgeDetectionImageFilterIF3IF3.Clone = new_instancemethod(_itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_Clone, None, itkSobelEdgeDetectionImageFilterIF3IF3)
itkSobelEdgeDetectionImageFilterIF3IF3.GenerateInputRequestedRegion = new_instancemethod(_itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_GenerateInputRequestedRegion, None, itkSobelEdgeDetectionImageFilterIF3IF3)
itkSobelEdgeDetectionImageFilterIF3IF3.GetPointer = new_instancemethod(_itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_GetPointer, None, itkSobelEdgeDetectionImageFilterIF3IF3)
itkSobelEdgeDetectionImageFilterIF3IF3_swigregister = _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_swigregister
itkSobelEdgeDetectionImageFilterIF3IF3_swigregister(itkSobelEdgeDetectionImageFilterIF3IF3)

def itkSobelEdgeDetectionImageFilterIF3IF3___New_orig__() -> "itkSobelEdgeDetectionImageFilterIF3IF3_Pointer":
    """itkSobelEdgeDetectionImageFilterIF3IF3___New_orig__() -> itkSobelEdgeDetectionImageFilterIF3IF3_Pointer"""
    return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3___New_orig__()

def itkSobelEdgeDetectionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSobelEdgeDetectionImageFilterIF3IF3 *":
    """itkSobelEdgeDetectionImageFilterIF3IF3_cast(itkLightObject obj) -> itkSobelEdgeDetectionImageFilterIF3IF3"""
    return _itkSobelEdgeDetectionImageFilterPython.itkSobelEdgeDetectionImageFilterIF3IF3_cast(obj)



