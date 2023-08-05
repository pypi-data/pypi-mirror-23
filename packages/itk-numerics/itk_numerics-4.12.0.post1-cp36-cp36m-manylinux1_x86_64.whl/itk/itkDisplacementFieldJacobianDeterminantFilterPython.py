# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDisplacementFieldJacobianDeterminantFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDisplacementFieldJacobianDeterminantFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDisplacementFieldJacobianDeterminantFilterPython')
    _itkDisplacementFieldJacobianDeterminantFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDisplacementFieldJacobianDeterminantFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDisplacementFieldJacobianDeterminantFilterPython
            return _itkDisplacementFieldJacobianDeterminantFilterPython
        try:
            _mod = imp.load_module('_itkDisplacementFieldJacobianDeterminantFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDisplacementFieldJacobianDeterminantFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDisplacementFieldJacobianDeterminantFilterPython
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


import itkSizePython
import pyBasePython
import itkFixedArrayPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBPixelPython
import itkOffsetPython
import ITKCommonBasePython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkDisplacementFieldJacobianDeterminantFilterIVF33F_New():
  return itkDisplacementFieldJacobianDeterminantFilterIVF33F.New()


def itkDisplacementFieldJacobianDeterminantFilterIVF22F_New():
  return itkDisplacementFieldJacobianDeterminantFilterIVF22F.New()

class itkDisplacementFieldJacobianDeterminantFilterIVF22F(itkImageToImageFilterBPython.itkImageToImageFilterIVF22IF2):
    """Proxy of C++ itkDisplacementFieldJacobianDeterminantFilterIVF22F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDisplacementFieldJacobianDeterminantFilterIVF22F_Pointer":
        """__New_orig__() -> itkDisplacementFieldJacobianDeterminantFilterIVF22F_Pointer"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDisplacementFieldJacobianDeterminantFilterIVF22F_Pointer":
        """Clone(itkDisplacementFieldJacobianDeterminantFilterIVF22F self) -> itkDisplacementFieldJacobianDeterminantFilterIVF22F_Pointer"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkDisplacementFieldJacobianDeterminantFilterIVF22F self)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GenerateInputRequestedRegion(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkDisplacementFieldJacobianDeterminantFilterIVF22F self)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkDisplacementFieldJacobianDeterminantFilterIVF22F self)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, arg0: 'bool') -> "void":
        """SetUseImageSpacing(itkDisplacementFieldJacobianDeterminantFilterIVF22F self, bool arg0)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetUseImageSpacing(self, arg0)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkDisplacementFieldJacobianDeterminantFilterIVF22F self) -> bool"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GetUseImageSpacing(self)


    def SetDerivativeWeights(self, arg0: 'itkFixedArrayF2') -> "void":
        """SetDerivativeWeights(itkDisplacementFieldJacobianDeterminantFilterIVF22F self, itkFixedArrayF2 arg0)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetDerivativeWeights(self, arg0)


    def GetDerivativeWeights(self) -> "itkFixedArrayF2 const &":
        """GetDerivativeWeights(itkDisplacementFieldJacobianDeterminantFilterIVF22F self) -> itkFixedArrayF2"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GetDerivativeWeights(self)

    __swig_destroy__ = _itkDisplacementFieldJacobianDeterminantFilterPython.delete_itkDisplacementFieldJacobianDeterminantFilterIVF22F

    def cast(obj: 'itkLightObject') -> "itkDisplacementFieldJacobianDeterminantFilterIVF22F *":
        """cast(itkLightObject obj) -> itkDisplacementFieldJacobianDeterminantFilterIVF22F"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDisplacementFieldJacobianDeterminantFilterIVF22F *":
        """GetPointer(itkDisplacementFieldJacobianDeterminantFilterIVF22F self) -> itkDisplacementFieldJacobianDeterminantFilterIVF22F"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDisplacementFieldJacobianDeterminantFilterIVF22F

        Create a new object of the class itkDisplacementFieldJacobianDeterminantFilterIVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDisplacementFieldJacobianDeterminantFilterIVF22F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDisplacementFieldJacobianDeterminantFilterIVF22F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDisplacementFieldJacobianDeterminantFilterIVF22F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDisplacementFieldJacobianDeterminantFilterIVF22F.Clone = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_Clone, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.GenerateInputRequestedRegion = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GenerateInputRequestedRegion, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.SetUseImageSpacingOn = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetUseImageSpacingOn, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.SetUseImageSpacingOff = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetUseImageSpacingOff, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.SetUseImageSpacing = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetUseImageSpacing, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.GetUseImageSpacing = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GetUseImageSpacing, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.SetDerivativeWeights = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_SetDerivativeWeights, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.GetDerivativeWeights = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GetDerivativeWeights, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F.GetPointer = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_GetPointer, None, itkDisplacementFieldJacobianDeterminantFilterIVF22F)
itkDisplacementFieldJacobianDeterminantFilterIVF22F_swigregister = _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_swigregister
itkDisplacementFieldJacobianDeterminantFilterIVF22F_swigregister(itkDisplacementFieldJacobianDeterminantFilterIVF22F)

def itkDisplacementFieldJacobianDeterminantFilterIVF22F___New_orig__() -> "itkDisplacementFieldJacobianDeterminantFilterIVF22F_Pointer":
    """itkDisplacementFieldJacobianDeterminantFilterIVF22F___New_orig__() -> itkDisplacementFieldJacobianDeterminantFilterIVF22F_Pointer"""
    return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F___New_orig__()

def itkDisplacementFieldJacobianDeterminantFilterIVF22F_cast(obj: 'itkLightObject') -> "itkDisplacementFieldJacobianDeterminantFilterIVF22F *":
    """itkDisplacementFieldJacobianDeterminantFilterIVF22F_cast(itkLightObject obj) -> itkDisplacementFieldJacobianDeterminantFilterIVF22F"""
    return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF22F_cast(obj)

class itkDisplacementFieldJacobianDeterminantFilterIVF33F(itkImageToImageFilterBPython.itkImageToImageFilterIVF33IF3):
    """Proxy of C++ itkDisplacementFieldJacobianDeterminantFilterIVF33F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDisplacementFieldJacobianDeterminantFilterIVF33F_Pointer":
        """__New_orig__() -> itkDisplacementFieldJacobianDeterminantFilterIVF33F_Pointer"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDisplacementFieldJacobianDeterminantFilterIVF33F_Pointer":
        """Clone(itkDisplacementFieldJacobianDeterminantFilterIVF33F self) -> itkDisplacementFieldJacobianDeterminantFilterIVF33F_Pointer"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkDisplacementFieldJacobianDeterminantFilterIVF33F self)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GenerateInputRequestedRegion(self)


    def SetUseImageSpacingOn(self) -> "void":
        """SetUseImageSpacingOn(itkDisplacementFieldJacobianDeterminantFilterIVF33F self)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetUseImageSpacingOn(self)


    def SetUseImageSpacingOff(self) -> "void":
        """SetUseImageSpacingOff(itkDisplacementFieldJacobianDeterminantFilterIVF33F self)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetUseImageSpacingOff(self)


    def SetUseImageSpacing(self, arg0: 'bool') -> "void":
        """SetUseImageSpacing(itkDisplacementFieldJacobianDeterminantFilterIVF33F self, bool arg0)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetUseImageSpacing(self, arg0)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkDisplacementFieldJacobianDeterminantFilterIVF33F self) -> bool"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GetUseImageSpacing(self)


    def SetDerivativeWeights(self, arg0: 'itkFixedArrayF3') -> "void":
        """SetDerivativeWeights(itkDisplacementFieldJacobianDeterminantFilterIVF33F self, itkFixedArrayF3 arg0)"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetDerivativeWeights(self, arg0)


    def GetDerivativeWeights(self) -> "itkFixedArrayF3 const &":
        """GetDerivativeWeights(itkDisplacementFieldJacobianDeterminantFilterIVF33F self) -> itkFixedArrayF3"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GetDerivativeWeights(self)

    __swig_destroy__ = _itkDisplacementFieldJacobianDeterminantFilterPython.delete_itkDisplacementFieldJacobianDeterminantFilterIVF33F

    def cast(obj: 'itkLightObject') -> "itkDisplacementFieldJacobianDeterminantFilterIVF33F *":
        """cast(itkLightObject obj) -> itkDisplacementFieldJacobianDeterminantFilterIVF33F"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDisplacementFieldJacobianDeterminantFilterIVF33F *":
        """GetPointer(itkDisplacementFieldJacobianDeterminantFilterIVF33F self) -> itkDisplacementFieldJacobianDeterminantFilterIVF33F"""
        return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDisplacementFieldJacobianDeterminantFilterIVF33F

        Create a new object of the class itkDisplacementFieldJacobianDeterminantFilterIVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDisplacementFieldJacobianDeterminantFilterIVF33F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDisplacementFieldJacobianDeterminantFilterIVF33F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDisplacementFieldJacobianDeterminantFilterIVF33F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDisplacementFieldJacobianDeterminantFilterIVF33F.Clone = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_Clone, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.GenerateInputRequestedRegion = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GenerateInputRequestedRegion, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.SetUseImageSpacingOn = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetUseImageSpacingOn, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.SetUseImageSpacingOff = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetUseImageSpacingOff, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.SetUseImageSpacing = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetUseImageSpacing, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.GetUseImageSpacing = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GetUseImageSpacing, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.SetDerivativeWeights = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_SetDerivativeWeights, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.GetDerivativeWeights = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GetDerivativeWeights, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F.GetPointer = new_instancemethod(_itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_GetPointer, None, itkDisplacementFieldJacobianDeterminantFilterIVF33F)
itkDisplacementFieldJacobianDeterminantFilterIVF33F_swigregister = _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_swigregister
itkDisplacementFieldJacobianDeterminantFilterIVF33F_swigregister(itkDisplacementFieldJacobianDeterminantFilterIVF33F)

def itkDisplacementFieldJacobianDeterminantFilterIVF33F___New_orig__() -> "itkDisplacementFieldJacobianDeterminantFilterIVF33F_Pointer":
    """itkDisplacementFieldJacobianDeterminantFilterIVF33F___New_orig__() -> itkDisplacementFieldJacobianDeterminantFilterIVF33F_Pointer"""
    return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F___New_orig__()

def itkDisplacementFieldJacobianDeterminantFilterIVF33F_cast(obj: 'itkLightObject') -> "itkDisplacementFieldJacobianDeterminantFilterIVF33F *":
    """itkDisplacementFieldJacobianDeterminantFilterIVF33F_cast(itkLightObject obj) -> itkDisplacementFieldJacobianDeterminantFilterIVF33F"""
    return _itkDisplacementFieldJacobianDeterminantFilterPython.itkDisplacementFieldJacobianDeterminantFilterIVF33F_cast(obj)



