# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBlobSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBlobSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBlobSpatialObjectPython')
    _itkBlobSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBlobSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkBlobSpatialObjectPython
            return _itkBlobSpatialObjectPython
        try:
            _mod = imp.load_module('_itkBlobSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBlobSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBlobSpatialObjectPython
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


import itkPointPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkFixedArrayPython
import vnl_vector_refPython
import ITKCommonBasePython
import itkSpatialObjectPointPython
import itkRGBAPixelPython
import itkPointBasedSpatialObjectPython
import itkSpatialObjectBasePython
import itkAffineGeometryFramePython
import itkScalableAffineTransformPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkSymmetricSecondRankTensorPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkSpatialObjectPropertyPython
import itkImageRegionPython

def itkBlobSpatialObject3_New():
  return itkBlobSpatialObject3.New()


def itkBlobSpatialObject2_New():
  return itkBlobSpatialObject2.New()

class itkBlobSpatialObject2(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2):
    """Proxy of C++ itkBlobSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBlobSpatialObject2_Pointer":
        """__New_orig__() -> itkBlobSpatialObject2_Pointer"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBlobSpatialObject2_Pointer":
        """Clone(itkBlobSpatialObject2 self) -> itkBlobSpatialObject2_Pointer"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkSpatialObjectPoint2,std::allocator< itkSpatialObjectPoint2 > > const &":
        """
        GetPoints(itkBlobSpatialObject2 self) -> vectoritkSpatialObjectPoint2
        GetPoints(itkBlobSpatialObject2 self) -> vectoritkSpatialObjectPoint2
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_GetPoints(self, *args)


    def SetPoints(self, newPoints: 'vectoritkSpatialObjectPoint2') -> "void":
        """SetPoints(itkBlobSpatialObject2 self, vectoritkSpatialObjectPoint2 newPoints)"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_SetPoints(self, newPoints)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint2 *":
        """
        GetPoint(itkBlobSpatialObject2 self, unsigned long long id) -> itkSpatialObjectPoint2
        GetPoint(itkBlobSpatialObject2 self, unsigned long long id) -> itkSpatialObjectPoint2
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_GetPoint(self, *args)


    def IsEvaluableAt(self, point: 'itkPointD2', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkBlobSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkBlobSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkBlobSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD2', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkBlobSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkBlobSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkBlobSpatialObject2 self, itkPointD2 point, double & value) -> bool
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkBlobSpatialObject2 self, itkPointD2 point, unsigned int depth, char * name) -> bool
        IsInside(itkBlobSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_IsInside(self, *args)

    __swig_destroy__ = _itkBlobSpatialObjectPython.delete_itkBlobSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkBlobSpatialObject2 *":
        """cast(itkLightObject obj) -> itkBlobSpatialObject2"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBlobSpatialObject2 *":
        """GetPointer(itkBlobSpatialObject2 self) -> itkBlobSpatialObject2"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBlobSpatialObject2

        Create a new object of the class itkBlobSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlobSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBlobSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBlobSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBlobSpatialObject2.Clone = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_Clone, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.GetPoints = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_GetPoints, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.SetPoints = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_SetPoints, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.GetPoint = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_GetPoint, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.IsEvaluableAt = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_IsEvaluableAt, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.ValueAt = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_ValueAt, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.IsInside = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_IsInside, None, itkBlobSpatialObject2)
itkBlobSpatialObject2.GetPointer = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject2_GetPointer, None, itkBlobSpatialObject2)
itkBlobSpatialObject2_swigregister = _itkBlobSpatialObjectPython.itkBlobSpatialObject2_swigregister
itkBlobSpatialObject2_swigregister(itkBlobSpatialObject2)

def itkBlobSpatialObject2___New_orig__() -> "itkBlobSpatialObject2_Pointer":
    """itkBlobSpatialObject2___New_orig__() -> itkBlobSpatialObject2_Pointer"""
    return _itkBlobSpatialObjectPython.itkBlobSpatialObject2___New_orig__()

def itkBlobSpatialObject2_cast(obj: 'itkLightObject') -> "itkBlobSpatialObject2 *":
    """itkBlobSpatialObject2_cast(itkLightObject obj) -> itkBlobSpatialObject2"""
    return _itkBlobSpatialObjectPython.itkBlobSpatialObject2_cast(obj)

class itkBlobSpatialObject3(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    """Proxy of C++ itkBlobSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBlobSpatialObject3_Pointer":
        """__New_orig__() -> itkBlobSpatialObject3_Pointer"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBlobSpatialObject3_Pointer":
        """Clone(itkBlobSpatialObject3 self) -> itkBlobSpatialObject3_Pointer"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkSpatialObjectPoint3,std::allocator< itkSpatialObjectPoint3 > > const &":
        """
        GetPoints(itkBlobSpatialObject3 self) -> vectoritkSpatialObjectPoint3
        GetPoints(itkBlobSpatialObject3 self) -> vectoritkSpatialObjectPoint3
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_GetPoints(self, *args)


    def SetPoints(self, newPoints: 'vectoritkSpatialObjectPoint3') -> "void":
        """SetPoints(itkBlobSpatialObject3 self, vectoritkSpatialObjectPoint3 newPoints)"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_SetPoints(self, newPoints)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint3 *":
        """
        GetPoint(itkBlobSpatialObject3 self, unsigned long long id) -> itkSpatialObjectPoint3
        GetPoint(itkBlobSpatialObject3 self, unsigned long long id) -> itkSpatialObjectPoint3
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_GetPoint(self, *args)


    def IsEvaluableAt(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkBlobSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkBlobSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkBlobSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD3', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkBlobSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkBlobSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkBlobSpatialObject3 self, itkPointD3 point, double & value) -> bool
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkBlobSpatialObject3 self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkBlobSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_IsInside(self, *args)

    __swig_destroy__ = _itkBlobSpatialObjectPython.delete_itkBlobSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkBlobSpatialObject3 *":
        """cast(itkLightObject obj) -> itkBlobSpatialObject3"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBlobSpatialObject3 *":
        """GetPointer(itkBlobSpatialObject3 self) -> itkBlobSpatialObject3"""
        return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBlobSpatialObject3

        Create a new object of the class itkBlobSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlobSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBlobSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBlobSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBlobSpatialObject3.Clone = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_Clone, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.GetPoints = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_GetPoints, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.SetPoints = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_SetPoints, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.GetPoint = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_GetPoint, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.IsEvaluableAt = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_IsEvaluableAt, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.ValueAt = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_ValueAt, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.IsInside = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_IsInside, None, itkBlobSpatialObject3)
itkBlobSpatialObject3.GetPointer = new_instancemethod(_itkBlobSpatialObjectPython.itkBlobSpatialObject3_GetPointer, None, itkBlobSpatialObject3)
itkBlobSpatialObject3_swigregister = _itkBlobSpatialObjectPython.itkBlobSpatialObject3_swigregister
itkBlobSpatialObject3_swigregister(itkBlobSpatialObject3)

def itkBlobSpatialObject3___New_orig__() -> "itkBlobSpatialObject3_Pointer":
    """itkBlobSpatialObject3___New_orig__() -> itkBlobSpatialObject3_Pointer"""
    return _itkBlobSpatialObjectPython.itkBlobSpatialObject3___New_orig__()

def itkBlobSpatialObject3_cast(obj: 'itkLightObject') -> "itkBlobSpatialObject3 *":
    """itkBlobSpatialObject3_cast(itkLightObject obj) -> itkBlobSpatialObject3"""
    return _itkBlobSpatialObjectPython.itkBlobSpatialObject3_cast(obj)



