# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkContourSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkContourSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkContourSpatialObjectPython')
    _itkContourSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkContourSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkContourSpatialObjectPython
            return _itkContourSpatialObjectPython
        try:
            _mod = imp.load_module('_itkContourSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkContourSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkContourSpatialObjectPython
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


import itkPointBasedSpatialObjectPython
import ITKCommonBasePython
import pyBasePython
import itkSpatialObjectPointPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkRGBAPixelPython
import itkSpatialObjectBasePython
import itkCovariantVectorPython
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
import itkContourSpatialObjectPointPython

def itkContourSpatialObject3_New():
  return itkContourSpatialObject3.New()


def itkContourSpatialObject2_New():
  return itkContourSpatialObject2.New()

class itkContourSpatialObject2(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2):
    """Proxy of C++ itkContourSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkContourSpatialObject2_Pointer":
        """__New_orig__() -> itkContourSpatialObject2_Pointer"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkContourSpatialObject2_Pointer":
        """Clone(itkContourSpatialObject2 self) -> itkContourSpatialObject2_Pointer"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_Clone(self)


    def GetControlPoints(self, *args) -> "std::vector< itkContourSpatialObjectPoint2,std::allocator< itkContourSpatialObjectPoint2 > > const &":
        """
        GetControlPoints(itkContourSpatialObject2 self) -> vectoritkContourSpatialObjectPoint2
        GetControlPoints(itkContourSpatialObject2 self) -> vectoritkContourSpatialObjectPoint2
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetControlPoints(self, *args)


    def SetControlPoints(self, newPoints: 'vectoritkContourSpatialObjectPoint2') -> "void":
        """SetControlPoints(itkContourSpatialObject2 self, vectoritkContourSpatialObjectPoint2 newPoints)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_SetControlPoints(self, newPoints)


    def GetControlPoint(self, *args) -> "itkContourSpatialObjectPoint2 *":
        """
        GetControlPoint(itkContourSpatialObject2 self, unsigned long id) -> itkContourSpatialObjectPoint2
        GetControlPoint(itkContourSpatialObject2 self, unsigned long id) -> itkContourSpatialObjectPoint2
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetControlPoint(self, *args)


    def GetNumberOfControlPoints(self) -> "unsigned long":
        """GetNumberOfControlPoints(itkContourSpatialObject2 self) -> unsigned long"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetNumberOfControlPoints(self)


    def GetInterpolatedPoints(self, *args) -> "std::vector< itkSpatialObjectPoint2,std::allocator< itkSpatialObjectPoint2 > > const &":
        """
        GetInterpolatedPoints(itkContourSpatialObject2 self) -> vectoritkSpatialObjectPoint2
        GetInterpolatedPoints(itkContourSpatialObject2 self) -> vectoritkSpatialObjectPoint2
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetInterpolatedPoints(self, *args)


    def SetInterpolatedPoints(self, newPoints: 'vectoritkSpatialObjectPoint2') -> "void":
        """SetInterpolatedPoints(itkContourSpatialObject2 self, vectoritkSpatialObjectPoint2 newPoints)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_SetInterpolatedPoints(self, newPoints)


    def GetInterpolatedPoint(self, *args) -> "itkSpatialObjectPoint2 *":
        """
        GetInterpolatedPoint(itkContourSpatialObject2 self, unsigned long id) -> itkSpatialObjectPoint2
        GetInterpolatedPoint(itkContourSpatialObject2 self, unsigned long id) -> itkSpatialObjectPoint2
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetInterpolatedPoint(self, *args)


    def GetNumberOfInterpolatedPoints(self) -> "unsigned long":
        """GetNumberOfInterpolatedPoints(itkContourSpatialObject2 self) -> unsigned long"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetNumberOfInterpolatedPoints(self)

    NO_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject2_NO_INTERPOLATION
    EXPLICIT_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject2_EXPLICIT_INTERPOLATION
    BEZIER_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject2_BEZIER_INTERPOLATION
    LINEAR_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject2_LINEAR_INTERPOLATION

    def GetInterpolationType(self) -> "itkContourSpatialObject2::InterpolationType":
        """GetInterpolationType(itkContourSpatialObject2 self) -> itkContourSpatialObject2::InterpolationType"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetInterpolationType(self)


    def SetInterpolationType(self, interpolation: 'itkContourSpatialObject2::InterpolationType') -> "void":
        """SetInterpolationType(itkContourSpatialObject2 self, itkContourSpatialObject2::InterpolationType interpolation)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_SetInterpolationType(self, interpolation)


    def SetClosed(self, _arg: 'bool const') -> "void":
        """SetClosed(itkContourSpatialObject2 self, bool const _arg)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_SetClosed(self, _arg)


    def GetClosed(self) -> "bool":
        """GetClosed(itkContourSpatialObject2 self) -> bool"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetClosed(self)


    def SetDisplayOrientation(self, _arg: 'int const') -> "void":
        """SetDisplayOrientation(itkContourSpatialObject2 self, int const _arg)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_SetDisplayOrientation(self, _arg)


    def GetDisplayOrientation(self) -> "int":
        """GetDisplayOrientation(itkContourSpatialObject2 self) -> int"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetDisplayOrientation(self)


    def SetAttachedToSlice(self, _arg: 'int const') -> "void":
        """SetAttachedToSlice(itkContourSpatialObject2 self, int const _arg)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_SetAttachedToSlice(self, _arg)


    def GetAttachedToSlice(self) -> "int":
        """GetAttachedToSlice(itkContourSpatialObject2 self) -> int"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetAttachedToSlice(self)


    def IsEvaluableAt(self, point: 'itkPointD2', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkContourSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkContourSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkContourSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD2', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkContourSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkContourSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkContourSpatialObject2 self, itkPointD2 point, double & value) -> bool
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkContourSpatialObject2 self, itkPointD2 point, unsigned int depth, char * name) -> bool
        IsInside(itkContourSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_IsInside(self, *args)

    __swig_destroy__ = _itkContourSpatialObjectPython.delete_itkContourSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkContourSpatialObject2 *":
        """cast(itkLightObject obj) -> itkContourSpatialObject2"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkContourSpatialObject2 *":
        """GetPointer(itkContourSpatialObject2 self) -> itkContourSpatialObject2"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkContourSpatialObject2

        Create a new object of the class itkContourSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkContourSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkContourSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkContourSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkContourSpatialObject2.Clone = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_Clone, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetControlPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetControlPoints, None, itkContourSpatialObject2)
itkContourSpatialObject2.SetControlPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_SetControlPoints, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetControlPoint = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetControlPoint, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetNumberOfControlPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetNumberOfControlPoints, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetInterpolatedPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetInterpolatedPoints, None, itkContourSpatialObject2)
itkContourSpatialObject2.SetInterpolatedPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_SetInterpolatedPoints, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetInterpolatedPoint = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetInterpolatedPoint, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetNumberOfInterpolatedPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetNumberOfInterpolatedPoints, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetInterpolationType = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetInterpolationType, None, itkContourSpatialObject2)
itkContourSpatialObject2.SetInterpolationType = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_SetInterpolationType, None, itkContourSpatialObject2)
itkContourSpatialObject2.SetClosed = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_SetClosed, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetClosed = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetClosed, None, itkContourSpatialObject2)
itkContourSpatialObject2.SetDisplayOrientation = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_SetDisplayOrientation, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetDisplayOrientation = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetDisplayOrientation, None, itkContourSpatialObject2)
itkContourSpatialObject2.SetAttachedToSlice = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_SetAttachedToSlice, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetAttachedToSlice = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetAttachedToSlice, None, itkContourSpatialObject2)
itkContourSpatialObject2.IsEvaluableAt = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_IsEvaluableAt, None, itkContourSpatialObject2)
itkContourSpatialObject2.ValueAt = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_ValueAt, None, itkContourSpatialObject2)
itkContourSpatialObject2.IsInside = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_IsInside, None, itkContourSpatialObject2)
itkContourSpatialObject2.GetPointer = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject2_GetPointer, None, itkContourSpatialObject2)
itkContourSpatialObject2_swigregister = _itkContourSpatialObjectPython.itkContourSpatialObject2_swigregister
itkContourSpatialObject2_swigregister(itkContourSpatialObject2)

def itkContourSpatialObject2___New_orig__() -> "itkContourSpatialObject2_Pointer":
    """itkContourSpatialObject2___New_orig__() -> itkContourSpatialObject2_Pointer"""
    return _itkContourSpatialObjectPython.itkContourSpatialObject2___New_orig__()

def itkContourSpatialObject2_cast(obj: 'itkLightObject') -> "itkContourSpatialObject2 *":
    """itkContourSpatialObject2_cast(itkLightObject obj) -> itkContourSpatialObject2"""
    return _itkContourSpatialObjectPython.itkContourSpatialObject2_cast(obj)

class itkContourSpatialObject3(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    """Proxy of C++ itkContourSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkContourSpatialObject3_Pointer":
        """__New_orig__() -> itkContourSpatialObject3_Pointer"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkContourSpatialObject3_Pointer":
        """Clone(itkContourSpatialObject3 self) -> itkContourSpatialObject3_Pointer"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_Clone(self)


    def GetControlPoints(self, *args) -> "std::vector< itkContourSpatialObjectPoint3,std::allocator< itkContourSpatialObjectPoint3 > > const &":
        """
        GetControlPoints(itkContourSpatialObject3 self) -> vectoritkContourSpatialObjectPoint3
        GetControlPoints(itkContourSpatialObject3 self) -> vectoritkContourSpatialObjectPoint3
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetControlPoints(self, *args)


    def SetControlPoints(self, newPoints: 'vectoritkContourSpatialObjectPoint3') -> "void":
        """SetControlPoints(itkContourSpatialObject3 self, vectoritkContourSpatialObjectPoint3 newPoints)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_SetControlPoints(self, newPoints)


    def GetControlPoint(self, *args) -> "itkContourSpatialObjectPoint3 *":
        """
        GetControlPoint(itkContourSpatialObject3 self, unsigned long id) -> itkContourSpatialObjectPoint3
        GetControlPoint(itkContourSpatialObject3 self, unsigned long id) -> itkContourSpatialObjectPoint3
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetControlPoint(self, *args)


    def GetNumberOfControlPoints(self) -> "unsigned long":
        """GetNumberOfControlPoints(itkContourSpatialObject3 self) -> unsigned long"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetNumberOfControlPoints(self)


    def GetInterpolatedPoints(self, *args) -> "std::vector< itkSpatialObjectPoint3,std::allocator< itkSpatialObjectPoint3 > > const &":
        """
        GetInterpolatedPoints(itkContourSpatialObject3 self) -> vectoritkSpatialObjectPoint3
        GetInterpolatedPoints(itkContourSpatialObject3 self) -> vectoritkSpatialObjectPoint3
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetInterpolatedPoints(self, *args)


    def SetInterpolatedPoints(self, newPoints: 'vectoritkSpatialObjectPoint3') -> "void":
        """SetInterpolatedPoints(itkContourSpatialObject3 self, vectoritkSpatialObjectPoint3 newPoints)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_SetInterpolatedPoints(self, newPoints)


    def GetInterpolatedPoint(self, *args) -> "itkSpatialObjectPoint3 *":
        """
        GetInterpolatedPoint(itkContourSpatialObject3 self, unsigned long id) -> itkSpatialObjectPoint3
        GetInterpolatedPoint(itkContourSpatialObject3 self, unsigned long id) -> itkSpatialObjectPoint3
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetInterpolatedPoint(self, *args)


    def GetNumberOfInterpolatedPoints(self) -> "unsigned long":
        """GetNumberOfInterpolatedPoints(itkContourSpatialObject3 self) -> unsigned long"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetNumberOfInterpolatedPoints(self)

    NO_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject3_NO_INTERPOLATION
    EXPLICIT_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject3_EXPLICIT_INTERPOLATION
    BEZIER_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject3_BEZIER_INTERPOLATION
    LINEAR_INTERPOLATION = _itkContourSpatialObjectPython.itkContourSpatialObject3_LINEAR_INTERPOLATION

    def GetInterpolationType(self) -> "itkContourSpatialObject3::InterpolationType":
        """GetInterpolationType(itkContourSpatialObject3 self) -> itkContourSpatialObject3::InterpolationType"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetInterpolationType(self)


    def SetInterpolationType(self, interpolation: 'itkContourSpatialObject3::InterpolationType') -> "void":
        """SetInterpolationType(itkContourSpatialObject3 self, itkContourSpatialObject3::InterpolationType interpolation)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_SetInterpolationType(self, interpolation)


    def SetClosed(self, _arg: 'bool const') -> "void":
        """SetClosed(itkContourSpatialObject3 self, bool const _arg)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_SetClosed(self, _arg)


    def GetClosed(self) -> "bool":
        """GetClosed(itkContourSpatialObject3 self) -> bool"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetClosed(self)


    def SetDisplayOrientation(self, _arg: 'int const') -> "void":
        """SetDisplayOrientation(itkContourSpatialObject3 self, int const _arg)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_SetDisplayOrientation(self, _arg)


    def GetDisplayOrientation(self) -> "int":
        """GetDisplayOrientation(itkContourSpatialObject3 self) -> int"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetDisplayOrientation(self)


    def SetAttachedToSlice(self, _arg: 'int const') -> "void":
        """SetAttachedToSlice(itkContourSpatialObject3 self, int const _arg)"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_SetAttachedToSlice(self, _arg)


    def GetAttachedToSlice(self) -> "int":
        """GetAttachedToSlice(itkContourSpatialObject3 self) -> int"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetAttachedToSlice(self)


    def IsEvaluableAt(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkContourSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkContourSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkContourSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD3', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkContourSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkContourSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkContourSpatialObject3 self, itkPointD3 point, double & value) -> bool
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkContourSpatialObject3 self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkContourSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_IsInside(self, *args)

    __swig_destroy__ = _itkContourSpatialObjectPython.delete_itkContourSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkContourSpatialObject3 *":
        """cast(itkLightObject obj) -> itkContourSpatialObject3"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkContourSpatialObject3 *":
        """GetPointer(itkContourSpatialObject3 self) -> itkContourSpatialObject3"""
        return _itkContourSpatialObjectPython.itkContourSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkContourSpatialObject3

        Create a new object of the class itkContourSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkContourSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkContourSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkContourSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkContourSpatialObject3.Clone = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_Clone, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetControlPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetControlPoints, None, itkContourSpatialObject3)
itkContourSpatialObject3.SetControlPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_SetControlPoints, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetControlPoint = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetControlPoint, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetNumberOfControlPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetNumberOfControlPoints, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetInterpolatedPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetInterpolatedPoints, None, itkContourSpatialObject3)
itkContourSpatialObject3.SetInterpolatedPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_SetInterpolatedPoints, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetInterpolatedPoint = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetInterpolatedPoint, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetNumberOfInterpolatedPoints = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetNumberOfInterpolatedPoints, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetInterpolationType = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetInterpolationType, None, itkContourSpatialObject3)
itkContourSpatialObject3.SetInterpolationType = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_SetInterpolationType, None, itkContourSpatialObject3)
itkContourSpatialObject3.SetClosed = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_SetClosed, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetClosed = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetClosed, None, itkContourSpatialObject3)
itkContourSpatialObject3.SetDisplayOrientation = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_SetDisplayOrientation, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetDisplayOrientation = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetDisplayOrientation, None, itkContourSpatialObject3)
itkContourSpatialObject3.SetAttachedToSlice = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_SetAttachedToSlice, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetAttachedToSlice = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetAttachedToSlice, None, itkContourSpatialObject3)
itkContourSpatialObject3.IsEvaluableAt = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_IsEvaluableAt, None, itkContourSpatialObject3)
itkContourSpatialObject3.ValueAt = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_ValueAt, None, itkContourSpatialObject3)
itkContourSpatialObject3.IsInside = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_IsInside, None, itkContourSpatialObject3)
itkContourSpatialObject3.GetPointer = new_instancemethod(_itkContourSpatialObjectPython.itkContourSpatialObject3_GetPointer, None, itkContourSpatialObject3)
itkContourSpatialObject3_swigregister = _itkContourSpatialObjectPython.itkContourSpatialObject3_swigregister
itkContourSpatialObject3_swigregister(itkContourSpatialObject3)

def itkContourSpatialObject3___New_orig__() -> "itkContourSpatialObject3_Pointer":
    """itkContourSpatialObject3___New_orig__() -> itkContourSpatialObject3_Pointer"""
    return _itkContourSpatialObjectPython.itkContourSpatialObject3___New_orig__()

def itkContourSpatialObject3_cast(obj: 'itkLightObject') -> "itkContourSpatialObject3 *":
    """itkContourSpatialObject3_cast(itkLightObject obj) -> itkContourSpatialObject3"""
    return _itkContourSpatialObjectPython.itkContourSpatialObject3_cast(obj)



