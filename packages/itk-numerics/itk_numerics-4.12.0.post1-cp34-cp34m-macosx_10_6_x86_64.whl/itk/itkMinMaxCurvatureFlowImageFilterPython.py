# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMinMaxCurvatureFlowImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMinMaxCurvatureFlowImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMinMaxCurvatureFlowImageFilterPython')
    _itkMinMaxCurvatureFlowImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMinMaxCurvatureFlowImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMinMaxCurvatureFlowImageFilterPython
            return _itkMinMaxCurvatureFlowImageFilterPython
        try:
            _mod = imp.load_module('_itkMinMaxCurvatureFlowImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMinMaxCurvatureFlowImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMinMaxCurvatureFlowImageFilterPython
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


import itkCurvatureFlowImageFilterPython
import itkDenseFiniteDifferenceImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkSizePython
import pyBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkMatrixPython
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
import itkImageToImageFilterBPython

def itkMinMaxCurvatureFlowImageFilterIF3IF3_New():
  return itkMinMaxCurvatureFlowImageFilterIF3IF3.New()


def itkMinMaxCurvatureFlowImageFilterIF2IF2_New():
  return itkMinMaxCurvatureFlowImageFilterIF2IF2.New()

class itkMinMaxCurvatureFlowImageFilterIF2IF2(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2):
    """Proxy of C++ itkMinMaxCurvatureFlowImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """Clone(itkMinMaxCurvatureFlowImageFilterIF2IF2 self) -> itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_Clone(self)


    def SetStencilRadius(self, _arg: 'unsigned long const') -> "void":
        """SetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF2IF2 self, unsigned long const _arg)"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_SetStencilRadius(self, _arg)


    def GetStencilRadius(self) -> "unsigned long":
        """GetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF2IF2 self) -> unsigned long"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetStencilRadius(self)

    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_UnsignedLongConvertibleToOutputCheck
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputLessThanComparableCheck
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_LongConvertibleToOutputCheck
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputDoubleComparableCheck
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputDoubleMultiplyAndAssignOperatorCheck
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputGreaterThanUnsignedLongCheck
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_UnsignedLongOutputAditiveOperatorsCheck
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF2IF2"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMinMaxCurvatureFlowImageFilterIF2IF2 *":
        """GetPointer(itkMinMaxCurvatureFlowImageFilterIF2IF2 self) -> itkMinMaxCurvatureFlowImageFilterIF2IF2"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterIF2IF2

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMinMaxCurvatureFlowImageFilterIF2IF2.Clone = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_Clone, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2.SetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_SetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2.GetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2.GetPointer = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetPointer, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister
itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister(itkMinMaxCurvatureFlowImageFilterIF2IF2)

def itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
    """itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

def itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF2IF2 *":
    """itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF2IF2"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

class itkMinMaxCurvatureFlowImageFilterIF3IF3(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3):
    """Proxy of C++ itkMinMaxCurvatureFlowImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """Clone(itkMinMaxCurvatureFlowImageFilterIF3IF3 self) -> itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_Clone(self)


    def SetStencilRadius(self, _arg: 'unsigned long const') -> "void":
        """SetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF3IF3 self, unsigned long const _arg)"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_SetStencilRadius(self, _arg)


    def GetStencilRadius(self) -> "unsigned long":
        """GetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF3IF3 self) -> unsigned long"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetStencilRadius(self)

    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_UnsignedLongConvertibleToOutputCheck
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputLessThanComparableCheck
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_LongConvertibleToOutputCheck
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputDoubleComparableCheck
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputDoubleMultiplyAndAssignOperatorCheck
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputGreaterThanUnsignedLongCheck
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_UnsignedLongOutputAditiveOperatorsCheck
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF3IF3"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMinMaxCurvatureFlowImageFilterIF3IF3 *":
        """GetPointer(itkMinMaxCurvatureFlowImageFilterIF3IF3 self) -> itkMinMaxCurvatureFlowImageFilterIF3IF3"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterIF3IF3

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMinMaxCurvatureFlowImageFilterIF3IF3.Clone = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_Clone, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3.SetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_SetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3.GetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3.GetPointer = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetPointer, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister
itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister(itkMinMaxCurvatureFlowImageFilterIF3IF3)

def itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
    """itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

def itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF3IF3 *":
    """itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF3IF3"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)



