# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHessian3DToVesselnessMeasureImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkHessian3DToVesselnessMeasureImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkHessian3DToVesselnessMeasureImageFilterPython')
    _itkHessian3DToVesselnessMeasureImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHessian3DToVesselnessMeasureImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHessian3DToVesselnessMeasureImageFilterPython
            return _itkHessian3DToVesselnessMeasureImageFilterPython
        try:
            _mod = imp.load_module('_itkHessian3DToVesselnessMeasureImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkHessian3DToVesselnessMeasureImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHessian3DToVesselnessMeasureImageFilterPython
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


import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import pyBasePython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkSizePython
import itkRGBPixelPython
import itkOffsetPython
import ITKCommonBasePython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkHessian3DToVesselnessMeasureImageFilterF_New():
  return itkHessian3DToVesselnessMeasureImageFilterF.New()


def itkHessian3DToVesselnessMeasureImageFilterUC_New():
  return itkHessian3DToVesselnessMeasureImageFilterUC.New()


def itkHessian3DToVesselnessMeasureImageFilterSS_New():
  return itkHessian3DToVesselnessMeasureImageFilterSS.New()

class itkHessian3DToVesselnessMeasureImageFilterF(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IF3):
    """Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHessian3DToVesselnessMeasureImageFilterF_Pointer":
        """__New_orig__() -> itkHessian3DToVesselnessMeasureImageFilterF_Pointer"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHessian3DToVesselnessMeasureImageFilterF_Pointer":
        """Clone(itkHessian3DToVesselnessMeasureImageFilterF self) -> itkHessian3DToVesselnessMeasureImageFilterF_Pointer"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_Clone(self)


    def SetAlpha1(self, _arg: 'double const') -> "void":
        """SetAlpha1(itkHessian3DToVesselnessMeasureImageFilterF self, double const _arg)"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha1(self, _arg)


    def GetAlpha1(self) -> "double":
        """GetAlpha1(itkHessian3DToVesselnessMeasureImageFilterF self) -> double"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha1(self)


    def SetAlpha2(self, _arg: 'double const') -> "void":
        """SetAlpha2(itkHessian3DToVesselnessMeasureImageFilterF self, double const _arg)"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha2(self, _arg)


    def GetAlpha2(self) -> "double":
        """GetAlpha2(itkHessian3DToVesselnessMeasureImageFilterF self) -> double"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha2(self)

    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterF

    def cast(obj: 'itkLightObject') -> "itkHessian3DToVesselnessMeasureImageFilterF *":
        """cast(itkLightObject obj) -> itkHessian3DToVesselnessMeasureImageFilterF"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHessian3DToVesselnessMeasureImageFilterF *":
        """GetPointer(itkHessian3DToVesselnessMeasureImageFilterF self) -> itkHessian3DToVesselnessMeasureImageFilterF"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterF

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHessian3DToVesselnessMeasureImageFilterF.Clone = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_Clone, None, itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF.SetAlpha1 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha1, None, itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF.GetAlpha1 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha1, None, itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF.SetAlpha2 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha2, None, itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF.GetAlpha2 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha2, None, itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF.GetPointer = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetPointer, None, itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF_swigregister = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_swigregister
itkHessian3DToVesselnessMeasureImageFilterF_swigregister(itkHessian3DToVesselnessMeasureImageFilterF)

def itkHessian3DToVesselnessMeasureImageFilterF___New_orig__() -> "itkHessian3DToVesselnessMeasureImageFilterF_Pointer":
    """itkHessian3DToVesselnessMeasureImageFilterF___New_orig__() -> itkHessian3DToVesselnessMeasureImageFilterF_Pointer"""
    return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF___New_orig__()

def itkHessian3DToVesselnessMeasureImageFilterF_cast(obj: 'itkLightObject') -> "itkHessian3DToVesselnessMeasureImageFilterF *":
    """itkHessian3DToVesselnessMeasureImageFilterF_cast(itkLightObject obj) -> itkHessian3DToVesselnessMeasureImageFilterF"""
    return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_cast(obj)

class itkHessian3DToVesselnessMeasureImageFilterSS(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ISS3):
    """Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterSS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHessian3DToVesselnessMeasureImageFilterSS_Pointer":
        """__New_orig__() -> itkHessian3DToVesselnessMeasureImageFilterSS_Pointer"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHessian3DToVesselnessMeasureImageFilterSS_Pointer":
        """Clone(itkHessian3DToVesselnessMeasureImageFilterSS self) -> itkHessian3DToVesselnessMeasureImageFilterSS_Pointer"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_Clone(self)


    def SetAlpha1(self, _arg: 'double const') -> "void":
        """SetAlpha1(itkHessian3DToVesselnessMeasureImageFilterSS self, double const _arg)"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha1(self, _arg)


    def GetAlpha1(self) -> "double":
        """GetAlpha1(itkHessian3DToVesselnessMeasureImageFilterSS self) -> double"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha1(self)


    def SetAlpha2(self, _arg: 'double const') -> "void":
        """SetAlpha2(itkHessian3DToVesselnessMeasureImageFilterSS self, double const _arg)"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha2(self, _arg)


    def GetAlpha2(self) -> "double":
        """GetAlpha2(itkHessian3DToVesselnessMeasureImageFilterSS self) -> double"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha2(self)

    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterSS

    def cast(obj: 'itkLightObject') -> "itkHessian3DToVesselnessMeasureImageFilterSS *":
        """cast(itkLightObject obj) -> itkHessian3DToVesselnessMeasureImageFilterSS"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHessian3DToVesselnessMeasureImageFilterSS *":
        """GetPointer(itkHessian3DToVesselnessMeasureImageFilterSS self) -> itkHessian3DToVesselnessMeasureImageFilterSS"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterSS

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHessian3DToVesselnessMeasureImageFilterSS.Clone = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_Clone, None, itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS.SetAlpha1 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha1, None, itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS.GetAlpha1 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha1, None, itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS.SetAlpha2 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha2, None, itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS.GetAlpha2 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha2, None, itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS.GetPointer = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetPointer, None, itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS_swigregister = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_swigregister
itkHessian3DToVesselnessMeasureImageFilterSS_swigregister(itkHessian3DToVesselnessMeasureImageFilterSS)

def itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__() -> "itkHessian3DToVesselnessMeasureImageFilterSS_Pointer":
    """itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__() -> itkHessian3DToVesselnessMeasureImageFilterSS_Pointer"""
    return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__()

def itkHessian3DToVesselnessMeasureImageFilterSS_cast(obj: 'itkLightObject') -> "itkHessian3DToVesselnessMeasureImageFilterSS *":
    """itkHessian3DToVesselnessMeasureImageFilterSS_cast(itkLightObject obj) -> itkHessian3DToVesselnessMeasureImageFilterSS"""
    return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_cast(obj)

class itkHessian3DToVesselnessMeasureImageFilterUC(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IUC3):
    """Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterUC class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHessian3DToVesselnessMeasureImageFilterUC_Pointer":
        """__New_orig__() -> itkHessian3DToVesselnessMeasureImageFilterUC_Pointer"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHessian3DToVesselnessMeasureImageFilterUC_Pointer":
        """Clone(itkHessian3DToVesselnessMeasureImageFilterUC self) -> itkHessian3DToVesselnessMeasureImageFilterUC_Pointer"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_Clone(self)


    def SetAlpha1(self, _arg: 'double const') -> "void":
        """SetAlpha1(itkHessian3DToVesselnessMeasureImageFilterUC self, double const _arg)"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha1(self, _arg)


    def GetAlpha1(self) -> "double":
        """GetAlpha1(itkHessian3DToVesselnessMeasureImageFilterUC self) -> double"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha1(self)


    def SetAlpha2(self, _arg: 'double const') -> "void":
        """SetAlpha2(itkHessian3DToVesselnessMeasureImageFilterUC self, double const _arg)"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha2(self, _arg)


    def GetAlpha2(self) -> "double":
        """GetAlpha2(itkHessian3DToVesselnessMeasureImageFilterUC self) -> double"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha2(self)

    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterUC

    def cast(obj: 'itkLightObject') -> "itkHessian3DToVesselnessMeasureImageFilterUC *":
        """cast(itkLightObject obj) -> itkHessian3DToVesselnessMeasureImageFilterUC"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHessian3DToVesselnessMeasureImageFilterUC *":
        """GetPointer(itkHessian3DToVesselnessMeasureImageFilterUC self) -> itkHessian3DToVesselnessMeasureImageFilterUC"""
        return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterUC

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHessian3DToVesselnessMeasureImageFilterUC.Clone = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_Clone, None, itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC.SetAlpha1 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha1, None, itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC.GetAlpha1 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha1, None, itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC.SetAlpha2 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha2, None, itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC.GetAlpha2 = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha2, None, itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC.GetPointer = new_instancemethod(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetPointer, None, itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC_swigregister = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_swigregister
itkHessian3DToVesselnessMeasureImageFilterUC_swigregister(itkHessian3DToVesselnessMeasureImageFilterUC)

def itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__() -> "itkHessian3DToVesselnessMeasureImageFilterUC_Pointer":
    """itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__() -> itkHessian3DToVesselnessMeasureImageFilterUC_Pointer"""
    return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__()

def itkHessian3DToVesselnessMeasureImageFilterUC_cast(obj: 'itkLightObject') -> "itkHessian3DToVesselnessMeasureImageFilterUC *":
    """itkHessian3DToVesselnessMeasureImageFilterUC_cast(itkLightObject obj) -> itkHessian3DToVesselnessMeasureImageFilterUC"""
    return _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_cast(obj)



