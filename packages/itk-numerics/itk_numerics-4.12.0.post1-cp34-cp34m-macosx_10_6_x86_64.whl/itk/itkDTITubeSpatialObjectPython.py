# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDTITubeSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDTITubeSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDTITubeSpatialObjectPython')
    _itkDTITubeSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDTITubeSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkDTITubeSpatialObjectPython
            return _itkDTITubeSpatialObjectPython
        try:
            _mod = imp.load_module('_itkDTITubeSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDTITubeSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDTITubeSpatialObjectPython
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


import itkSpatialObjectPointPython
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkRGBAPixelPython
import ITKCommonBasePython
import itkDTITubeSpatialObjectPointPython
import itkTubeSpatialObjectPointPython
import itkCovariantVectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointBasedSpatialObjectPython
import itkSpatialObjectBasePython
import itkSpatialObjectPropertyPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkScalableAffineTransformPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkAffineGeometryFramePython

def itkDTITubeSpatialObject3_New():
  return itkDTITubeSpatialObject3.New()


def itkDTITubeSpatialObject3_Superclass_New():
  return itkDTITubeSpatialObject3_Superclass.New()

class itkDTITubeSpatialObject3_Superclass(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    """Proxy of C++ itkDTITubeSpatialObject3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDTITubeSpatialObject3_Superclass_Pointer":
        """__New_orig__() -> itkDTITubeSpatialObject3_Superclass_Pointer"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDTITubeSpatialObject3_Superclass_Pointer":
        """Clone(itkDTITubeSpatialObject3_Superclass self) -> itkDTITubeSpatialObject3_Superclass_Pointer"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_Clone(self)


    def GetPoints(self, *args) -> "std::vector< itkDTITubeSpatialObjectPoint3,std::allocator< itkDTITubeSpatialObjectPoint3 > > const &":
        """
        GetPoints(itkDTITubeSpatialObject3_Superclass self) -> std::vector< itkDTITubeSpatialObjectPoint3,std::allocator< itkDTITubeSpatialObjectPoint3 > >
        GetPoints(itkDTITubeSpatialObject3_Superclass self) -> std::vector< itkDTITubeSpatialObjectPoint3,std::allocator< itkDTITubeSpatialObjectPoint3 > > const &
        """
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetPoints(self, *args)


    def SetPoints(self, newPoints: 'std::vector< itkDTITubeSpatialObjectPoint3,std::allocator< itkDTITubeSpatialObjectPoint3 > > &') -> "void":
        """SetPoints(itkDTITubeSpatialObject3_Superclass self, std::vector< itkDTITubeSpatialObjectPoint3,std::allocator< itkDTITubeSpatialObjectPoint3 > > & newPoints)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetPoints(self, newPoints)


    def GetPoint(self, *args) -> "itkSpatialObjectPoint3 *":
        """
        GetPoint(itkDTITubeSpatialObject3_Superclass self, unsigned long ind) -> itkSpatialObjectPoint3
        GetPoint(itkDTITubeSpatialObject3_Superclass self, unsigned long ind) -> itkSpatialObjectPoint3
        """
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetPoint(self, *args)


    def SetPoint(self, ind: 'unsigned long', pnt: 'itkDTITubeSpatialObjectPoint3') -> "void":
        """SetPoint(itkDTITubeSpatialObject3_Superclass self, unsigned long ind, itkDTITubeSpatialObjectPoint3 pnt)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetPoint(self, ind, pnt)


    def RemovePoint(self, ind: 'unsigned long') -> "void":
        """RemovePoint(itkDTITubeSpatialObject3_Superclass self, unsigned long ind)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RemovePoint(self, ind)


    def SetEndType(self, _arg: 'unsigned int const') -> "void":
        """SetEndType(itkDTITubeSpatialObject3_Superclass self, unsigned int const _arg)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetEndType(self, _arg)


    def GetEndType(self) -> "unsigned int":
        """GetEndType(itkDTITubeSpatialObject3_Superclass self) -> unsigned int"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetEndType(self)


    def ComputeTangentAndNormals(self) -> "bool":
        """ComputeTangentAndNormals(itkDTITubeSpatialObject3_Superclass self) -> bool"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_ComputeTangentAndNormals(self)


    def RemoveDuplicatePoints(self, step: 'unsigned int'=1) -> "unsigned int":
        """
        RemoveDuplicatePoints(itkDTITubeSpatialObject3_Superclass self, unsigned int step=1) -> unsigned int
        RemoveDuplicatePoints(itkDTITubeSpatialObject3_Superclass self) -> unsigned int
        """
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RemoveDuplicatePoints(self, step)


    def IsEvaluableAt(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsEvaluableAt(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point) -> bool
        """
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_IsEvaluableAt(self, point, depth, name)


    def ValueAt(self, point: 'itkPointD3', value: 'double &', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        ValueAt(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point, double & value) -> bool
        """
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_ValueAt(self, point, value, depth, name)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkDTITubeSpatialObject3_Superclass self, itkPointD3 point) -> bool
        """
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_IsInside(self, *args)


    def SetParentPoint(self, _arg: 'int const') -> "void":
        """SetParentPoint(itkDTITubeSpatialObject3_Superclass self, int const _arg)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetParentPoint(self, _arg)


    def GetParentPoint(self) -> "int":
        """GetParentPoint(itkDTITubeSpatialObject3_Superclass self) -> int"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetParentPoint(self)


    def SetRoot(self, _arg: 'bool const') -> "void":
        """SetRoot(itkDTITubeSpatialObject3_Superclass self, bool const _arg)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetRoot(self, _arg)


    def GetRoot(self) -> "bool":
        """GetRoot(itkDTITubeSpatialObject3_Superclass self) -> bool"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetRoot(self)


    def SetArtery(self, _arg: 'bool const') -> "void":
        """SetArtery(itkDTITubeSpatialObject3_Superclass self, bool const _arg)"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetArtery(self, _arg)


    def GetArtery(self) -> "bool":
        """GetArtery(itkDTITubeSpatialObject3_Superclass self) -> bool"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetArtery(self)

    __swig_destroy__ = _itkDTITubeSpatialObjectPython.delete_itkDTITubeSpatialObject3_Superclass

    def cast(obj: 'itkLightObject') -> "itkDTITubeSpatialObject3_Superclass *":
        """cast(itkLightObject obj) -> itkDTITubeSpatialObject3_Superclass"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDTITubeSpatialObject3_Superclass *":
        """GetPointer(itkDTITubeSpatialObject3_Superclass self) -> itkDTITubeSpatialObject3_Superclass"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDTITubeSpatialObject3_Superclass

        Create a new object of the class itkDTITubeSpatialObject3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDTITubeSpatialObject3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDTITubeSpatialObject3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDTITubeSpatialObject3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDTITubeSpatialObject3_Superclass.Clone = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_Clone, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetPoints = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetPoints, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.SetPoints = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetPoints, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetPoint = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetPoint, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.SetPoint = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetPoint, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.RemovePoint = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RemovePoint, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.SetEndType = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetEndType, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetEndType = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetEndType, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.ComputeTangentAndNormals = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_ComputeTangentAndNormals, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.RemoveDuplicatePoints = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RemoveDuplicatePoints, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.IsEvaluableAt = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_IsEvaluableAt, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.ValueAt = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_ValueAt, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.IsInside = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_IsInside, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.SetParentPoint = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetParentPoint, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetParentPoint = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetParentPoint, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.SetRoot = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetRoot, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetRoot = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetRoot, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.SetArtery = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetArtery, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetArtery = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetArtery, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass.GetPointer = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetPointer, None, itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass_swigregister = _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_swigregister
itkDTITubeSpatialObject3_Superclass_swigregister(itkDTITubeSpatialObject3_Superclass)

def itkDTITubeSpatialObject3_Superclass___New_orig__() -> "itkDTITubeSpatialObject3_Superclass_Pointer":
    """itkDTITubeSpatialObject3_Superclass___New_orig__() -> itkDTITubeSpatialObject3_Superclass_Pointer"""
    return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass___New_orig__()

def itkDTITubeSpatialObject3_Superclass_cast(obj: 'itkLightObject') -> "itkDTITubeSpatialObject3_Superclass *":
    """itkDTITubeSpatialObject3_Superclass_cast(itkLightObject obj) -> itkDTITubeSpatialObject3_Superclass"""
    return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_cast(obj)

class itkDTITubeSpatialObject3(itkDTITubeSpatialObject3_Superclass):
    """Proxy of C++ itkDTITubeSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDTITubeSpatialObject3_Pointer":
        """__New_orig__() -> itkDTITubeSpatialObject3_Pointer"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDTITubeSpatialObject3_Pointer":
        """Clone(itkDTITubeSpatialObject3 self) -> itkDTITubeSpatialObject3_Pointer"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Clone(self)

    __swig_destroy__ = _itkDTITubeSpatialObjectPython.delete_itkDTITubeSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkDTITubeSpatialObject3 *":
        """cast(itkLightObject obj) -> itkDTITubeSpatialObject3"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDTITubeSpatialObject3 *":
        """GetPointer(itkDTITubeSpatialObject3 self) -> itkDTITubeSpatialObject3"""
        return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDTITubeSpatialObject3

        Create a new object of the class itkDTITubeSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDTITubeSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDTITubeSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDTITubeSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDTITubeSpatialObject3.Clone = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Clone, None, itkDTITubeSpatialObject3)
itkDTITubeSpatialObject3.GetPointer = new_instancemethod(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_GetPointer, None, itkDTITubeSpatialObject3)
itkDTITubeSpatialObject3_swigregister = _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_swigregister
itkDTITubeSpatialObject3_swigregister(itkDTITubeSpatialObject3)

def itkDTITubeSpatialObject3___New_orig__() -> "itkDTITubeSpatialObject3_Pointer":
    """itkDTITubeSpatialObject3___New_orig__() -> itkDTITubeSpatialObject3_Pointer"""
    return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3___New_orig__()

def itkDTITubeSpatialObject3_cast(obj: 'itkLightObject') -> "itkDTITubeSpatialObject3 *":
    """itkDTITubeSpatialObject3_cast(itkLightObject obj) -> itkDTITubeSpatialObject3"""
    return _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_cast(obj)



