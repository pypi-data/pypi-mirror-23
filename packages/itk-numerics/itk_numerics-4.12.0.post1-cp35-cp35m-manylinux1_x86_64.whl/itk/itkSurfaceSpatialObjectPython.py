# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSurfaceSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSurfaceSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSurfaceSpatialObjectPython')
    _itkSurfaceSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSurfaceSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkSurfaceSpatialObjectPython
            return _itkSurfaceSpatialObjectPython
        try:
            _mod = imp.load_module('_itkSurfaceSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSurfaceSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSurfaceSpatialObjectPython
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
import itkSurfaceSpatialObjectPointPython

def itkSurfaceSpatialObject3_New():
  return itkSurfaceSpatialObject3.New()


def itkSurfaceSpatialObject2_New():
  return itkSurfaceSpatialObject2.New()

class itkSurfaceSpatialObject2(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2):
    """Proxy of C++ itkSurfaceSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSurfaceSpatialObject2_Pointer":
        """__New_orig__() -> itkSurfaceSpatialObject2_Pointer"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSurfaceSpatialObject2_Pointer":
        """Clone(itkSurfaceSpatialObject2 self) -> itkSurfaceSpatialObject2_Pointer"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkSurfaceSpatialObjectPoint2,std::allocator< itkSurfaceSpatialObjectPoint2 > > const &":
        """
        GetPoints(itkSurfaceSpatialObject2 self) -> vectoritkSurfaceSpatialObjectPoint2
        GetPoints(itkSurfaceSpatialObject2 self) -> vectoritkSurfaceSpatialObjectPoint2
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_GetPoints(self, *args)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint2 *":
        """
        GetPoint(itkSurfaceSpatialObject2 self, unsigned long id) -> itkSpatialObjectPoint2
        GetPoint(itkSurfaceSpatialObject2 self, unsigned long id) -> itkSpatialObjectPoint2
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_GetPoint(self, *args)


    def SetPoints(self, newPoints: 'vectoritkSurfaceSpatialObjectPoint2') -> "void":
        """SetPoints(itkSurfaceSpatialObject2 self, vectoritkSurfaceSpatialObjectPoint2 newPoints)"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_SetPoints(self, newPoints)


    def IsEvaluableAt(self, point: 'itkPointD2', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkSurfaceSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkSurfaceSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkSurfaceSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD2', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkSurfaceSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkSurfaceSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkSurfaceSpatialObject2 self, itkPointD2 point, double & value) -> bool
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkSurfaceSpatialObject2 self, itkPointD2 point, unsigned int depth, char * name) -> bool
        IsInside(itkSurfaceSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_IsInside(self, *args)


    def Approximate3DNormals(self) -> "bool":
        """Approximate3DNormals(itkSurfaceSpatialObject2 self) -> bool"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_Approximate3DNormals(self)

    __swig_destroy__ = _itkSurfaceSpatialObjectPython.delete_itkSurfaceSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkSurfaceSpatialObject2 *":
        """cast(itkLightObject obj) -> itkSurfaceSpatialObject2"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSurfaceSpatialObject2 *":
        """GetPointer(itkSurfaceSpatialObject2 self) -> itkSurfaceSpatialObject2"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSurfaceSpatialObject2

        Create a new object of the class itkSurfaceSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSurfaceSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSurfaceSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSurfaceSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSurfaceSpatialObject2.Clone = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_Clone, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.GetPoints = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_GetPoints, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.GetPoint = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_GetPoint, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.SetPoints = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_SetPoints, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.IsEvaluableAt = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_IsEvaluableAt, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.ValueAt = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_ValueAt, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.IsInside = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_IsInside, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.Approximate3DNormals = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_Approximate3DNormals, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2.GetPointer = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_GetPointer, None, itkSurfaceSpatialObject2)
itkSurfaceSpatialObject2_swigregister = _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_swigregister
itkSurfaceSpatialObject2_swigregister(itkSurfaceSpatialObject2)

def itkSurfaceSpatialObject2___New_orig__() -> "itkSurfaceSpatialObject2_Pointer":
    """itkSurfaceSpatialObject2___New_orig__() -> itkSurfaceSpatialObject2_Pointer"""
    return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2___New_orig__()

def itkSurfaceSpatialObject2_cast(obj: 'itkLightObject') -> "itkSurfaceSpatialObject2 *":
    """itkSurfaceSpatialObject2_cast(itkLightObject obj) -> itkSurfaceSpatialObject2"""
    return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject2_cast(obj)

class itkSurfaceSpatialObject3(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    """Proxy of C++ itkSurfaceSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSurfaceSpatialObject3_Pointer":
        """__New_orig__() -> itkSurfaceSpatialObject3_Pointer"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSurfaceSpatialObject3_Pointer":
        """Clone(itkSurfaceSpatialObject3 self) -> itkSurfaceSpatialObject3_Pointer"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkSurfaceSpatialObjectPoint3,std::allocator< itkSurfaceSpatialObjectPoint3 > > const &":
        """
        GetPoints(itkSurfaceSpatialObject3 self) -> vectoritkSurfaceSpatialObjectPoint3
        GetPoints(itkSurfaceSpatialObject3 self) -> vectoritkSurfaceSpatialObjectPoint3
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_GetPoints(self, *args)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint3 *":
        """
        GetPoint(itkSurfaceSpatialObject3 self, unsigned long id) -> itkSpatialObjectPoint3
        GetPoint(itkSurfaceSpatialObject3 self, unsigned long id) -> itkSpatialObjectPoint3
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_GetPoint(self, *args)


    def SetPoints(self, newPoints: 'vectoritkSurfaceSpatialObjectPoint3') -> "void":
        """SetPoints(itkSurfaceSpatialObject3 self, vectoritkSurfaceSpatialObjectPoint3 newPoints)"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_SetPoints(self, newPoints)


    def IsEvaluableAt(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkSurfaceSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkSurfaceSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkSurfaceSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD3', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkSurfaceSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkSurfaceSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkSurfaceSpatialObject3 self, itkPointD3 point, double & value) -> bool
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkSurfaceSpatialObject3 self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkSurfaceSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_IsInside(self, *args)


    def Approximate3DNormals(self) -> "bool":
        """Approximate3DNormals(itkSurfaceSpatialObject3 self) -> bool"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_Approximate3DNormals(self)

    __swig_destroy__ = _itkSurfaceSpatialObjectPython.delete_itkSurfaceSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkSurfaceSpatialObject3 *":
        """cast(itkLightObject obj) -> itkSurfaceSpatialObject3"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSurfaceSpatialObject3 *":
        """GetPointer(itkSurfaceSpatialObject3 self) -> itkSurfaceSpatialObject3"""
        return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSurfaceSpatialObject3

        Create a new object of the class itkSurfaceSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSurfaceSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSurfaceSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSurfaceSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSurfaceSpatialObject3.Clone = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_Clone, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.GetPoints = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_GetPoints, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.GetPoint = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_GetPoint, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.SetPoints = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_SetPoints, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.IsEvaluableAt = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_IsEvaluableAt, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.ValueAt = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_ValueAt, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.IsInside = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_IsInside, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.Approximate3DNormals = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_Approximate3DNormals, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3.GetPointer = new_instancemethod(_itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_GetPointer, None, itkSurfaceSpatialObject3)
itkSurfaceSpatialObject3_swigregister = _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_swigregister
itkSurfaceSpatialObject3_swigregister(itkSurfaceSpatialObject3)

def itkSurfaceSpatialObject3___New_orig__() -> "itkSurfaceSpatialObject3_Pointer":
    """itkSurfaceSpatialObject3___New_orig__() -> itkSurfaceSpatialObject3_Pointer"""
    return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3___New_orig__()

def itkSurfaceSpatialObject3_cast(obj: 'itkLightObject') -> "itkSurfaceSpatialObject3 *":
    """itkSurfaceSpatialObject3_cast(itkLightObject obj) -> itkSurfaceSpatialObject3"""
    return _itkSurfaceSpatialObjectPython.itkSurfaceSpatialObject3_cast(obj)



