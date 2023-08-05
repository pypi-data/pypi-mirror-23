# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHoughTransform2DCirclesImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkHoughTransform2DCirclesImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkHoughTransform2DCirclesImageFilterPython')
    _itkHoughTransform2DCirclesImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHoughTransform2DCirclesImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHoughTransform2DCirclesImageFilterPython
            return _itkHoughTransform2DCirclesImageFilterPython
        try:
            _mod = imp.load_module('_itkHoughTransform2DCirclesImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkHoughTransform2DCirclesImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHoughTransform2DCirclesImageFilterPython
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
import itkEllipseSpatialObjectPython
import itkSpatialObjectBasePython
import itkScalableAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkAffineGeometryFramePython
import itkBoundingBoxPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkMapContainerPython
import itkSpatialObjectPropertyPython

def itkHoughTransform2DCirclesImageFilterFF_New():
  return itkHoughTransform2DCirclesImageFilterFF.New()

class itkHoughTransform2DCirclesImageFilterFF(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkHoughTransform2DCirclesImageFilterFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHoughTransform2DCirclesImageFilterFF_Pointer":
        """__New_orig__() -> itkHoughTransform2DCirclesImageFilterFF_Pointer"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHoughTransform2DCirclesImageFilterFF_Pointer":
        """Clone(itkHoughTransform2DCirclesImageFilterFF self) -> itkHoughTransform2DCirclesImageFilterFF_Pointer"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkHoughTransform2DCirclesImageFilterFF self)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GenerateData(self)


    def SetRadius(self, radius: 'double') -> "void":
        """SetRadius(itkHoughTransform2DCirclesImageFilterFF self, double radius)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetRadius(self, radius)


    def SetMinimumRadius(self, _arg: 'double const') -> "void":
        """SetMinimumRadius(itkHoughTransform2DCirclesImageFilterFF self, double const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetMinimumRadius(self, _arg)


    def GetMinimumRadius(self) -> "double":
        """GetMinimumRadius(itkHoughTransform2DCirclesImageFilterFF self) -> double"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetMinimumRadius(self)


    def SetMaximumRadius(self, _arg: 'double const') -> "void":
        """SetMaximumRadius(itkHoughTransform2DCirclesImageFilterFF self, double const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetMaximumRadius(self, _arg)


    def GetMaximumRadius(self) -> "double":
        """GetMaximumRadius(itkHoughTransform2DCirclesImageFilterFF self) -> double"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetMaximumRadius(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """SetThreshold(itkHoughTransform2DCirclesImageFilterFF self, double const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkHoughTransform2DCirclesImageFilterFF self) -> double"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetThreshold(self)


    def GetModifiableRadiusImage(self) -> "itkImageF2 *":
        """GetModifiableRadiusImage(itkHoughTransform2DCirclesImageFilterFF self) -> itkImageF2"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetModifiableRadiusImage(self)


    def GetRadiusImage(self, *args) -> "itkImageF2 *":
        """
        GetRadiusImage(itkHoughTransform2DCirclesImageFilterFF self) -> itkImageF2
        GetRadiusImage(itkHoughTransform2DCirclesImageFilterFF self) -> itkImageF2
        """
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetRadiusImage(self, *args)


    def SetSigmaGradient(self, _arg: 'double const') -> "void":
        """SetSigmaGradient(itkHoughTransform2DCirclesImageFilterFF self, double const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetSigmaGradient(self, _arg)


    def GetSigmaGradient(self) -> "double":
        """GetSigmaGradient(itkHoughTransform2DCirclesImageFilterFF self) -> double"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetSigmaGradient(self)


    def GetCircles(self, n: 'unsigned int'=0) -> "std::list< itkEllipseSpatialObject2_Pointer,std::allocator< itkEllipseSpatialObject2_Pointer > > &":
        """
        GetCircles(itkHoughTransform2DCirclesImageFilterFF self, unsigned int n=0) -> listitkEllipseSpatialObject2_Pointer
        GetCircles(itkHoughTransform2DCirclesImageFilterFF self) -> listitkEllipseSpatialObject2_Pointer
        """
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetCircles(self, n)


    def SetNumberOfCircles(self, _arg: 'unsigned long const') -> "void":
        """SetNumberOfCircles(itkHoughTransform2DCirclesImageFilterFF self, unsigned long const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetNumberOfCircles(self, _arg)


    def GetNumberOfCircles(self) -> "unsigned long":
        """GetNumberOfCircles(itkHoughTransform2DCirclesImageFilterFF self) -> unsigned long"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetNumberOfCircles(self)


    def SetDiscRadiusRatio(self, _arg: 'float const') -> "void":
        """SetDiscRadiusRatio(itkHoughTransform2DCirclesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetDiscRadiusRatio(self, _arg)


    def GetDiscRadiusRatio(self) -> "float":
        """GetDiscRadiusRatio(itkHoughTransform2DCirclesImageFilterFF self) -> float"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetDiscRadiusRatio(self)


    def SetVariance(self, _arg: 'float const') -> "void":
        """SetVariance(itkHoughTransform2DCirclesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetVariance(self, _arg)


    def GetVariance(self) -> "float":
        """GetVariance(itkHoughTransform2DCirclesImageFilterFF self) -> float"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetVariance(self)


    def SetSweepAngle(self, _arg: 'float const') -> "void":
        """SetSweepAngle(itkHoughTransform2DCirclesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetSweepAngle(self, _arg)


    def GetSweepAngle(self) -> "float":
        """GetSweepAngle(itkHoughTransform2DCirclesImageFilterFF self) -> float"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetSweepAngle(self)

    IntConvertibleToOutputCheck = _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_IntConvertibleToOutputCheck
    InputGreaterThanDoubleCheck = _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_InputGreaterThanDoubleCheck
    OutputPlusIntCheck = _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_OutputPlusIntCheck
    OutputDividedByIntCheck = _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_OutputDividedByIntCheck
    __swig_destroy__ = _itkHoughTransform2DCirclesImageFilterPython.delete_itkHoughTransform2DCirclesImageFilterFF

    def cast(obj: 'itkLightObject') -> "itkHoughTransform2DCirclesImageFilterFF *":
        """cast(itkLightObject obj) -> itkHoughTransform2DCirclesImageFilterFF"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHoughTransform2DCirclesImageFilterFF *":
        """GetPointer(itkHoughTransform2DCirclesImageFilterFF self) -> itkHoughTransform2DCirclesImageFilterFF"""
        return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHoughTransform2DCirclesImageFilterFF

        Create a new object of the class itkHoughTransform2DCirclesImageFilterFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHoughTransform2DCirclesImageFilterFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHoughTransform2DCirclesImageFilterFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHoughTransform2DCirclesImageFilterFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHoughTransform2DCirclesImageFilterFF.Clone = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_Clone, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GenerateData = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GenerateData, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetRadius = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetRadius, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetMinimumRadius = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetMinimumRadius, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetMinimumRadius = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetMinimumRadius, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetMaximumRadius = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetMaximumRadius, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetMaximumRadius = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetMaximumRadius, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetThreshold = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetThreshold, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetThreshold = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetThreshold, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetModifiableRadiusImage = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetModifiableRadiusImage, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetRadiusImage = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetRadiusImage, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetSigmaGradient = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetSigmaGradient, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetSigmaGradient = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetSigmaGradient, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetCircles = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetCircles, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetNumberOfCircles = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetNumberOfCircles, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetNumberOfCircles = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetNumberOfCircles, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetDiscRadiusRatio = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetDiscRadiusRatio, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetDiscRadiusRatio = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetDiscRadiusRatio, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetVariance = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetVariance, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetVariance = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetVariance, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.SetSweepAngle = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_SetSweepAngle, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetSweepAngle = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetSweepAngle, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF.GetPointer = new_instancemethod(_itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_GetPointer, None, itkHoughTransform2DCirclesImageFilterFF)
itkHoughTransform2DCirclesImageFilterFF_swigregister = _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_swigregister
itkHoughTransform2DCirclesImageFilterFF_swigregister(itkHoughTransform2DCirclesImageFilterFF)

def itkHoughTransform2DCirclesImageFilterFF___New_orig__() -> "itkHoughTransform2DCirclesImageFilterFF_Pointer":
    """itkHoughTransform2DCirclesImageFilterFF___New_orig__() -> itkHoughTransform2DCirclesImageFilterFF_Pointer"""
    return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF___New_orig__()

def itkHoughTransform2DCirclesImageFilterFF_cast(obj: 'itkLightObject') -> "itkHoughTransform2DCirclesImageFilterFF *":
    """itkHoughTransform2DCirclesImageFilterFF_cast(itkLightObject obj) -> itkHoughTransform2DCirclesImageFilterFF"""
    return _itkHoughTransform2DCirclesImageFilterPython.itkHoughTransform2DCirclesImageFilterFF_cast(obj)



