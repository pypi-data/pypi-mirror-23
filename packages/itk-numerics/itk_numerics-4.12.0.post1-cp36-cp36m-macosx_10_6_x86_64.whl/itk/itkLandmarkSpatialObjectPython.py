# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLandmarkSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLandmarkSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLandmarkSpatialObjectPython')
    _itkLandmarkSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLandmarkSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkLandmarkSpatialObjectPython
            return _itkLandmarkSpatialObjectPython
        try:
            _mod = imp.load_module('_itkLandmarkSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLandmarkSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLandmarkSpatialObjectPython
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
import itkPointBasedSpatialObjectPython
import itkSpatialObjectBasePython
import itkAffineGeometryFramePython
import itkScalableAffineTransformPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkPointPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkSpatialObjectPointPython

def itkLandmarkSpatialObject3_New():
  return itkLandmarkSpatialObject3.New()


def itkLandmarkSpatialObject2_New():
  return itkLandmarkSpatialObject2.New()

class itkLandmarkSpatialObject2(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2):
    """Proxy of C++ itkLandmarkSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLandmarkSpatialObject2_Pointer":
        """__New_orig__() -> itkLandmarkSpatialObject2_Pointer"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLandmarkSpatialObject2_Pointer":
        """Clone(itkLandmarkSpatialObject2 self) -> itkLandmarkSpatialObject2_Pointer"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkSpatialObjectPoint2,std::allocator< itkSpatialObjectPoint2 > > const &":
        """
        GetPoints(itkLandmarkSpatialObject2 self) -> vectoritkSpatialObjectPoint2
        GetPoints(itkLandmarkSpatialObject2 self) -> vectoritkSpatialObjectPoint2
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_GetPoints(self, *args)


    def SetPoints(self, newPoints: 'vectoritkSpatialObjectPoint2') -> "void":
        """SetPoints(itkLandmarkSpatialObject2 self, vectoritkSpatialObjectPoint2 newPoints)"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_SetPoints(self, newPoints)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint2 *":
        """
        GetPoint(itkLandmarkSpatialObject2 self, unsigned long id) -> itkSpatialObjectPoint2
        GetPoint(itkLandmarkSpatialObject2 self, unsigned long id) -> itkSpatialObjectPoint2
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_GetPoint(self, *args)


    def IsEvaluableAt(self, point: 'itkPointD2', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkLandmarkSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkLandmarkSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkLandmarkSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD2', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkLandmarkSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkLandmarkSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkLandmarkSpatialObject2 self, itkPointD2 point, double & value) -> bool
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkLandmarkSpatialObject2 self, itkPointD2 point, unsigned int depth, char * name) -> bool
        IsInside(itkLandmarkSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_IsInside(self, *args)

    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkLandmarkSpatialObject2 *":
        """cast(itkLightObject obj) -> itkLandmarkSpatialObject2"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLandmarkSpatialObject2 *":
        """GetPointer(itkLandmarkSpatialObject2 self) -> itkLandmarkSpatialObject2"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject2

        Create a new object of the class itkLandmarkSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLandmarkSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLandmarkSpatialObject2.Clone = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_Clone, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.GetPoints = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_GetPoints, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.SetPoints = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_SetPoints, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.GetPoint = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_GetPoint, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.IsEvaluableAt = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_IsEvaluableAt, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.ValueAt = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_ValueAt, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.IsInside = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_IsInside, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2.GetPointer = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_GetPointer, None, itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2_swigregister = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_swigregister
itkLandmarkSpatialObject2_swigregister(itkLandmarkSpatialObject2)

def itkLandmarkSpatialObject2___New_orig__() -> "itkLandmarkSpatialObject2_Pointer":
    """itkLandmarkSpatialObject2___New_orig__() -> itkLandmarkSpatialObject2_Pointer"""
    return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2___New_orig__()

def itkLandmarkSpatialObject2_cast(obj: 'itkLightObject') -> "itkLandmarkSpatialObject2 *":
    """itkLandmarkSpatialObject2_cast(itkLightObject obj) -> itkLandmarkSpatialObject2"""
    return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_cast(obj)

class itkLandmarkSpatialObject3(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    """Proxy of C++ itkLandmarkSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLandmarkSpatialObject3_Pointer":
        """__New_orig__() -> itkLandmarkSpatialObject3_Pointer"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLandmarkSpatialObject3_Pointer":
        """Clone(itkLandmarkSpatialObject3 self) -> itkLandmarkSpatialObject3_Pointer"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkSpatialObjectPoint3,std::allocator< itkSpatialObjectPoint3 > > const &":
        """
        GetPoints(itkLandmarkSpatialObject3 self) -> vectoritkSpatialObjectPoint3
        GetPoints(itkLandmarkSpatialObject3 self) -> vectoritkSpatialObjectPoint3
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_GetPoints(self, *args)


    def SetPoints(self, newPoints: 'vectoritkSpatialObjectPoint3') -> "void":
        """SetPoints(itkLandmarkSpatialObject3 self, vectoritkSpatialObjectPoint3 newPoints)"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_SetPoints(self, newPoints)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint3 *":
        """
        GetPoint(itkLandmarkSpatialObject3 self, unsigned long id) -> itkSpatialObjectPoint3
        GetPoint(itkLandmarkSpatialObject3 self, unsigned long id) -> itkSpatialObjectPoint3
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_GetPoint(self, *args)


    def IsEvaluableAt(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkLandmarkSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkLandmarkSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkLandmarkSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD3', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkLandmarkSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkLandmarkSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkLandmarkSpatialObject3 self, itkPointD3 point, double & value) -> bool
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkLandmarkSpatialObject3 self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkLandmarkSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_IsInside(self, *args)

    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkLandmarkSpatialObject3 *":
        """cast(itkLightObject obj) -> itkLandmarkSpatialObject3"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLandmarkSpatialObject3 *":
        """GetPointer(itkLandmarkSpatialObject3 self) -> itkLandmarkSpatialObject3"""
        return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject3

        Create a new object of the class itkLandmarkSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLandmarkSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLandmarkSpatialObject3.Clone = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_Clone, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.GetPoints = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_GetPoints, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.SetPoints = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_SetPoints, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.GetPoint = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_GetPoint, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.IsEvaluableAt = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_IsEvaluableAt, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.ValueAt = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_ValueAt, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.IsInside = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_IsInside, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3.GetPointer = new_instancemethod(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_GetPointer, None, itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3_swigregister = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_swigregister
itkLandmarkSpatialObject3_swigregister(itkLandmarkSpatialObject3)

def itkLandmarkSpatialObject3___New_orig__() -> "itkLandmarkSpatialObject3_Pointer":
    """itkLandmarkSpatialObject3___New_orig__() -> itkLandmarkSpatialObject3_Pointer"""
    return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3___New_orig__()

def itkLandmarkSpatialObject3_cast(obj: 'itkLightObject') -> "itkLandmarkSpatialObject3 *":
    """itkLandmarkSpatialObject3_cast(itkLightObject obj) -> itkLandmarkSpatialObject3"""
    return _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_cast(obj)



