# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPlaneSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPlaneSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPlaneSpatialObjectPython')
    _itkPlaneSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPlaneSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkPlaneSpatialObjectPython
            return _itkPlaneSpatialObjectPython
        try:
            _mod = imp.load_module('_itkPlaneSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPlaneSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPlaneSpatialObjectPython
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
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import ITKCommonBasePython
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
import itkRGBAPixelPython

def itkPlaneSpatialObject3_New():
  return itkPlaneSpatialObject3.New()


def itkPlaneSpatialObject2_New():
  return itkPlaneSpatialObject2.New()

class itkPlaneSpatialObject2(itkSpatialObjectBasePython.itkSpatialObject2):
    """Proxy of C++ itkPlaneSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPlaneSpatialObject2_Pointer":
        """__New_orig__() -> itkPlaneSpatialObject2_Pointer"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPlaneSpatialObject2_Pointer":
        """Clone(itkPlaneSpatialObject2 self) -> itkPlaneSpatialObject2_Pointer"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_Clone(self)


    def ValueAt(self, point: 'itkPointD2', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkPlaneSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkPlaneSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkPlaneSpatialObject2 self, itkPointD2 point, double & value) -> bool
        """
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_ValueAt(self, point, value, depth, name)


    def IsEvaluableAt(self, point: 'itkPointD2', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkPlaneSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkPlaneSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkPlaneSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_IsEvaluableAt(self, point, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkPlaneSpatialObject2 self, itkPointD2 point, unsigned int depth, char * name) -> bool
        IsInside(itkPlaneSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_IsInside(self, *args)


    def SetLowerPoint(self, _arg: 'itkPointD2') -> "void":
        """SetLowerPoint(itkPlaneSpatialObject2 self, itkPointD2 _arg)"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_SetLowerPoint(self, _arg)


    def SetUpperPoint(self, _arg: 'itkPointD2') -> "void":
        """SetUpperPoint(itkPlaneSpatialObject2 self, itkPointD2 _arg)"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_SetUpperPoint(self, _arg)


    def GetLowerPoint(self) -> "itkPointD2":
        """GetLowerPoint(itkPlaneSpatialObject2 self) -> itkPointD2"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_GetLowerPoint(self)


    def GetUpperPoint(self) -> "itkPointD2":
        """GetUpperPoint(itkPlaneSpatialObject2 self) -> itkPointD2"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_GetUpperPoint(self)

    __swig_destroy__ = _itkPlaneSpatialObjectPython.delete_itkPlaneSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkPlaneSpatialObject2 *":
        """cast(itkLightObject obj) -> itkPlaneSpatialObject2"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPlaneSpatialObject2 *":
        """GetPointer(itkPlaneSpatialObject2 self) -> itkPlaneSpatialObject2"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPlaneSpatialObject2

        Create a new object of the class itkPlaneSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPlaneSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPlaneSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPlaneSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPlaneSpatialObject2.Clone = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_Clone, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.ValueAt = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_ValueAt, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.IsEvaluableAt = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_IsEvaluableAt, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.IsInside = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_IsInside, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.SetLowerPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_SetLowerPoint, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.SetUpperPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_SetUpperPoint, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.GetLowerPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_GetLowerPoint, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.GetUpperPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_GetUpperPoint, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2.GetPointer = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_GetPointer, None, itkPlaneSpatialObject2)
itkPlaneSpatialObject2_swigregister = _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_swigregister
itkPlaneSpatialObject2_swigregister(itkPlaneSpatialObject2)

def itkPlaneSpatialObject2___New_orig__() -> "itkPlaneSpatialObject2_Pointer":
    """itkPlaneSpatialObject2___New_orig__() -> itkPlaneSpatialObject2_Pointer"""
    return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2___New_orig__()

def itkPlaneSpatialObject2_cast(obj: 'itkLightObject') -> "itkPlaneSpatialObject2 *":
    """itkPlaneSpatialObject2_cast(itkLightObject obj) -> itkPlaneSpatialObject2"""
    return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject2_cast(obj)

class itkPlaneSpatialObject3(itkSpatialObjectBasePython.itkSpatialObject3):
    """Proxy of C++ itkPlaneSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPlaneSpatialObject3_Pointer":
        """__New_orig__() -> itkPlaneSpatialObject3_Pointer"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPlaneSpatialObject3_Pointer":
        """Clone(itkPlaneSpatialObject3 self) -> itkPlaneSpatialObject3_Pointer"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_Clone(self)


    def ValueAt(self, point: 'itkPointD3', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkPlaneSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkPlaneSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkPlaneSpatialObject3 self, itkPointD3 point, double & value) -> bool
        """
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_ValueAt(self, point, value, depth, name)


    def IsEvaluableAt(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkPlaneSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkPlaneSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkPlaneSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_IsEvaluableAt(self, point, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkPlaneSpatialObject3 self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkPlaneSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_IsInside(self, *args)


    def SetLowerPoint(self, _arg: 'itkPointD3') -> "void":
        """SetLowerPoint(itkPlaneSpatialObject3 self, itkPointD3 _arg)"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_SetLowerPoint(self, _arg)


    def SetUpperPoint(self, _arg: 'itkPointD3') -> "void":
        """SetUpperPoint(itkPlaneSpatialObject3 self, itkPointD3 _arg)"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_SetUpperPoint(self, _arg)


    def GetLowerPoint(self) -> "itkPointD3":
        """GetLowerPoint(itkPlaneSpatialObject3 self) -> itkPointD3"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_GetLowerPoint(self)


    def GetUpperPoint(self) -> "itkPointD3":
        """GetUpperPoint(itkPlaneSpatialObject3 self) -> itkPointD3"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_GetUpperPoint(self)

    __swig_destroy__ = _itkPlaneSpatialObjectPython.delete_itkPlaneSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkPlaneSpatialObject3 *":
        """cast(itkLightObject obj) -> itkPlaneSpatialObject3"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPlaneSpatialObject3 *":
        """GetPointer(itkPlaneSpatialObject3 self) -> itkPlaneSpatialObject3"""
        return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPlaneSpatialObject3

        Create a new object of the class itkPlaneSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPlaneSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPlaneSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPlaneSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPlaneSpatialObject3.Clone = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_Clone, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.ValueAt = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_ValueAt, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.IsEvaluableAt = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_IsEvaluableAt, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.IsInside = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_IsInside, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.SetLowerPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_SetLowerPoint, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.SetUpperPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_SetUpperPoint, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.GetLowerPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_GetLowerPoint, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.GetUpperPoint = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_GetUpperPoint, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3.GetPointer = new_instancemethod(_itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_GetPointer, None, itkPlaneSpatialObject3)
itkPlaneSpatialObject3_swigregister = _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_swigregister
itkPlaneSpatialObject3_swigregister(itkPlaneSpatialObject3)

def itkPlaneSpatialObject3___New_orig__() -> "itkPlaneSpatialObject3_Pointer":
    """itkPlaneSpatialObject3___New_orig__() -> itkPlaneSpatialObject3_Pointer"""
    return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3___New_orig__()

def itkPlaneSpatialObject3_cast(obj: 'itkLightObject') -> "itkPlaneSpatialObject3 *":
    """itkPlaneSpatialObject3_cast(itkLightObject obj) -> itkPlaneSpatialObject3"""
    return _itkPlaneSpatialObjectPython.itkPlaneSpatialObject3_cast(obj)



