# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHoughTransform2DLinesImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkHoughTransform2DLinesImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkHoughTransform2DLinesImageFilterPython')
    _itkHoughTransform2DLinesImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHoughTransform2DLinesImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHoughTransform2DLinesImageFilterPython
            return _itkHoughTransform2DLinesImageFilterPython
        try:
            _mod = imp.load_module('_itkHoughTransform2DLinesImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkHoughTransform2DLinesImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHoughTransform2DLinesImageFilterPython
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


import itkLineSpatialObjectPython
import itkLineSpatialObjectPointPython
import itkCovariantVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkSpatialObjectPointPython
import ITKCommonBasePython
import itkPointPython
import itkRGBAPixelPython
import itkPointBasedSpatialObjectPython
import itkSpatialObjectBasePython
import itkAffineGeometryFramePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkScalableAffineTransformPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython
import itkArrayPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkImageRegionPython
import itkSpatialObjectPropertyPython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkImagePython
import itkRGBPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkHoughTransform2DLinesImageFilterFF_New():
  return itkHoughTransform2DLinesImageFilterFF.New()

class itkHoughTransform2DLinesImageFilterFF(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkHoughTransform2DLinesImageFilterFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHoughTransform2DLinesImageFilterFF_Pointer":
        """__New_orig__() -> itkHoughTransform2DLinesImageFilterFF_Pointer"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHoughTransform2DLinesImageFilterFF_Pointer":
        """Clone(itkHoughTransform2DLinesImageFilterFF self) -> itkHoughTransform2DLinesImageFilterFF_Pointer"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkHoughTransform2DLinesImageFilterFF self)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GenerateData(self)


    def SetThreshold(self, _arg: 'float const') -> "void":
        """SetThreshold(itkHoughTransform2DLinesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetThreshold(self, _arg)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkHoughTransform2DLinesImageFilterFF self) -> float"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetThreshold(self)


    def SetAngleResolution(self, _arg: 'float const') -> "void":
        """SetAngleResolution(itkHoughTransform2DLinesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetAngleResolution(self, _arg)


    def GetAngleResolution(self) -> "float":
        """GetAngleResolution(itkHoughTransform2DLinesImageFilterFF self) -> float"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetAngleResolution(self)


    def Simplify(self) -> "void":
        """Simplify(itkHoughTransform2DLinesImageFilterFF self)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Simplify(self)


    def GetModifiableSimplifyAccumulator(self) -> "itkImageF2 *":
        """GetModifiableSimplifyAccumulator(itkHoughTransform2DLinesImageFilterFF self) -> itkImageF2"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetModifiableSimplifyAccumulator(self)


    def GetSimplifyAccumulator(self, *args) -> "itkImageF2 *":
        """
        GetSimplifyAccumulator(itkHoughTransform2DLinesImageFilterFF self) -> itkImageF2
        GetSimplifyAccumulator(itkHoughTransform2DLinesImageFilterFF self) -> itkImageF2
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetSimplifyAccumulator(self, *args)


    def GetLines(self, n: 'unsigned int'=0) -> "std::list< itkLineSpatialObject2_Pointer,std::allocator< itkLineSpatialObject2_Pointer > > &":
        """
        GetLines(itkHoughTransform2DLinesImageFilterFF self, unsigned int n=0) -> std::list< itkLineSpatialObject2_Pointer,std::allocator< itkLineSpatialObject2_Pointer > >
        GetLines(itkHoughTransform2DLinesImageFilterFF self) -> std::list< itkLineSpatialObject2_Pointer,std::allocator< itkLineSpatialObject2_Pointer > > &
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetLines(self, n)


    def SetNumberOfLines(self, _arg: 'unsigned long const') -> "void":
        """SetNumberOfLines(itkHoughTransform2DLinesImageFilterFF self, unsigned long const _arg)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetNumberOfLines(self, _arg)


    def GetNumberOfLines(self) -> "unsigned long":
        """GetNumberOfLines(itkHoughTransform2DLinesImageFilterFF self) -> unsigned long"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetNumberOfLines(self)


    def SetDiscRadius(self, _arg: 'float const') -> "void":
        """SetDiscRadius(itkHoughTransform2DLinesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetDiscRadius(self, _arg)


    def GetDiscRadius(self) -> "float":
        """GetDiscRadius(itkHoughTransform2DLinesImageFilterFF self) -> float"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetDiscRadius(self)


    def SetVariance(self, _arg: 'float const') -> "void":
        """SetVariance(itkHoughTransform2DLinesImageFilterFF self, float const _arg)"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetVariance(self, _arg)


    def GetVariance(self) -> "float":
        """GetVariance(itkHoughTransform2DLinesImageFilterFF self) -> float"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetVariance(self)

    IntConvertibleToOutputCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_IntConvertibleToOutputCheck
    InputGreaterThanFloatCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_InputGreaterThanFloatCheck
    OutputPlusIntCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_OutputPlusIntCheck
    __swig_destroy__ = _itkHoughTransform2DLinesImageFilterPython.delete_itkHoughTransform2DLinesImageFilterFF

    def cast(obj: 'itkLightObject') -> "itkHoughTransform2DLinesImageFilterFF *":
        """cast(itkLightObject obj) -> itkHoughTransform2DLinesImageFilterFF"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHoughTransform2DLinesImageFilterFF *":
        """GetPointer(itkHoughTransform2DLinesImageFilterFF self) -> itkHoughTransform2DLinesImageFilterFF"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHoughTransform2DLinesImageFilterFF

        Create a new object of the class itkHoughTransform2DLinesImageFilterFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHoughTransform2DLinesImageFilterFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHoughTransform2DLinesImageFilterFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHoughTransform2DLinesImageFilterFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHoughTransform2DLinesImageFilterFF.Clone = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Clone, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GenerateData = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GenerateData, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetThreshold = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetThreshold, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetThreshold = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetThreshold, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetAngleResolution = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetAngleResolution, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetAngleResolution = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetAngleResolution, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.Simplify = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Simplify, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetModifiableSimplifyAccumulator = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetModifiableSimplifyAccumulator, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetSimplifyAccumulator = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetSimplifyAccumulator, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetLines, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetNumberOfLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetNumberOfLines, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetNumberOfLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetNumberOfLines, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetDiscRadius = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetDiscRadius, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetDiscRadius = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetDiscRadius, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetVariance = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetVariance, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetVariance = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetVariance, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetPointer = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetPointer, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF_swigregister = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_swigregister
itkHoughTransform2DLinesImageFilterFF_swigregister(itkHoughTransform2DLinesImageFilterFF)

def itkHoughTransform2DLinesImageFilterFF___New_orig__() -> "itkHoughTransform2DLinesImageFilterFF_Pointer":
    """itkHoughTransform2DLinesImageFilterFF___New_orig__() -> itkHoughTransform2DLinesImageFilterFF_Pointer"""
    return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF___New_orig__()

def itkHoughTransform2DLinesImageFilterFF_cast(obj: 'itkLightObject') -> "itkHoughTransform2DLinesImageFilterFF *":
    """itkHoughTransform2DLinesImageFilterFF_cast(itkLightObject obj) -> itkHoughTransform2DLinesImageFilterFF"""
    return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_cast(obj)



