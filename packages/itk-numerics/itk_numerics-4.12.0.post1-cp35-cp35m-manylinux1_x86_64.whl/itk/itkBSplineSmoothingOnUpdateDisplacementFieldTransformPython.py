# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython')
    _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython
            return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython
        try:
            _mod = imp.load_module('_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython
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
import itkImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDisplacementFieldTransformPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkTransformBasePython

def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_New():
  return itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.New()


def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_New():
  return itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.New()

class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    """Proxy of C++ itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Pointer":
        """__New_orig__() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Pointer"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Pointer":
        """Clone(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Pointer"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, itkArrayD update)
        """
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_UpdateTransformParameters(self, update, factor)


    def SetSplineOrder(self, _arg: 'unsigned int const') -> "void":
        """SetSplineOrder(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, unsigned int const _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetSplineOrder(self, _arg)


    def GetSplineOrder(self) -> "unsigned int":
        """GetSplineOrder(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self) -> unsigned int"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetSplineOrder(self)


    def SetNumberOfControlPointsForTheUpdateField(self, _arg: 'itkFixedArrayUI2') -> "void":
        """SetNumberOfControlPointsForTheUpdateField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, itkFixedArrayUI2 _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetNumberOfControlPointsForTheUpdateField(self, _arg)


    def GetNumberOfControlPointsForTheUpdateField(self) -> "itkFixedArrayUI2":
        """GetNumberOfControlPointsForTheUpdateField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self) -> itkFixedArrayUI2"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetNumberOfControlPointsForTheUpdateField(self)


    def SetMeshSizeForTheUpdateField(self, arg0: 'itkFixedArrayUI2') -> "void":
        """SetMeshSizeForTheUpdateField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, itkFixedArrayUI2 arg0)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetMeshSizeForTheUpdateField(self, arg0)


    def SetNumberOfControlPointsForTheTotalField(self, _arg: 'itkFixedArrayUI2') -> "void":
        """SetNumberOfControlPointsForTheTotalField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, itkFixedArrayUI2 _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetNumberOfControlPointsForTheTotalField(self, _arg)


    def GetNumberOfControlPointsForTheTotalField(self) -> "itkFixedArrayUI2":
        """GetNumberOfControlPointsForTheTotalField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self) -> itkFixedArrayUI2"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetNumberOfControlPointsForTheTotalField(self)


    def SetMeshSizeForTheTotalField(self, arg0: 'itkFixedArrayUI2') -> "void":
        """SetMeshSizeForTheTotalField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, itkFixedArrayUI2 arg0)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetMeshSizeForTheTotalField(self, arg0)


    def EnforceStationaryBoundaryOn(self) -> "void":
        """EnforceStationaryBoundaryOn(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_EnforceStationaryBoundaryOn(self)


    def EnforceStationaryBoundaryOff(self) -> "void":
        """EnforceStationaryBoundaryOff(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_EnforceStationaryBoundaryOff(self)


    def SetEnforceStationaryBoundary(self, _arg: 'bool const') -> "void":
        """SetEnforceStationaryBoundary(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self, bool const _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetEnforceStationaryBoundary(self, _arg)


    def GetEnforceStationaryBoundary(self) -> "bool":
        """GetEnforceStationaryBoundary(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self) -> bool"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetEnforceStationaryBoundary(self)

    __swig_destroy__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2

    def cast(obj: 'itkLightObject') -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 *":
        """cast(itkLightObject obj) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 *":
        """GetPointer(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 self) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2

        Create a new object of the class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.Clone = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Clone, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.UpdateTransformParameters = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_UpdateTransformParameters, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.SetSplineOrder = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetSplineOrder, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.GetSplineOrder = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetSplineOrder, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.SetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetNumberOfControlPointsForTheUpdateField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.GetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetNumberOfControlPointsForTheUpdateField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.SetMeshSizeForTheUpdateField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetMeshSizeForTheUpdateField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.SetNumberOfControlPointsForTheTotalField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetNumberOfControlPointsForTheTotalField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.GetNumberOfControlPointsForTheTotalField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetNumberOfControlPointsForTheTotalField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.SetMeshSizeForTheTotalField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetMeshSizeForTheTotalField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.EnforceStationaryBoundaryOn = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_EnforceStationaryBoundaryOn, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.EnforceStationaryBoundaryOff = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_EnforceStationaryBoundaryOff, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.SetEnforceStationaryBoundary = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetEnforceStationaryBoundary, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.GetEnforceStationaryBoundary = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetEnforceStationaryBoundary, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.GetPointer = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetPointer, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_swigregister = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_swigregister
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_swigregister(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)

def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__() -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Pointer":
    """itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Pointer"""
    return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__()

def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast(obj: 'itkLightObject') -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 *":
    """itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast(itkLightObject obj) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2"""
    return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast(obj)

class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    """Proxy of C++ itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Pointer":
        """__New_orig__() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Pointer"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Pointer":
        """Clone(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Pointer"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, itkArrayD update)
        """
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_UpdateTransformParameters(self, update, factor)


    def SetSplineOrder(self, _arg: 'unsigned int const') -> "void":
        """SetSplineOrder(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, unsigned int const _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetSplineOrder(self, _arg)


    def GetSplineOrder(self) -> "unsigned int":
        """GetSplineOrder(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self) -> unsigned int"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetSplineOrder(self)


    def SetNumberOfControlPointsForTheUpdateField(self, _arg: 'itkFixedArrayUI3') -> "void":
        """SetNumberOfControlPointsForTheUpdateField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, itkFixedArrayUI3 _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetNumberOfControlPointsForTheUpdateField(self, _arg)


    def GetNumberOfControlPointsForTheUpdateField(self) -> "itkFixedArrayUI3":
        """GetNumberOfControlPointsForTheUpdateField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self) -> itkFixedArrayUI3"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetNumberOfControlPointsForTheUpdateField(self)


    def SetMeshSizeForTheUpdateField(self, arg0: 'itkFixedArrayUI3') -> "void":
        """SetMeshSizeForTheUpdateField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, itkFixedArrayUI3 arg0)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetMeshSizeForTheUpdateField(self, arg0)


    def SetNumberOfControlPointsForTheTotalField(self, _arg: 'itkFixedArrayUI3') -> "void":
        """SetNumberOfControlPointsForTheTotalField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, itkFixedArrayUI3 _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetNumberOfControlPointsForTheTotalField(self, _arg)


    def GetNumberOfControlPointsForTheTotalField(self) -> "itkFixedArrayUI3":
        """GetNumberOfControlPointsForTheTotalField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self) -> itkFixedArrayUI3"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetNumberOfControlPointsForTheTotalField(self)


    def SetMeshSizeForTheTotalField(self, arg0: 'itkFixedArrayUI3') -> "void":
        """SetMeshSizeForTheTotalField(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, itkFixedArrayUI3 arg0)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetMeshSizeForTheTotalField(self, arg0)


    def EnforceStationaryBoundaryOn(self) -> "void":
        """EnforceStationaryBoundaryOn(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_EnforceStationaryBoundaryOn(self)


    def EnforceStationaryBoundaryOff(self) -> "void":
        """EnforceStationaryBoundaryOff(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_EnforceStationaryBoundaryOff(self)


    def SetEnforceStationaryBoundary(self, _arg: 'bool const') -> "void":
        """SetEnforceStationaryBoundary(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self, bool const _arg)"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetEnforceStationaryBoundary(self, _arg)


    def GetEnforceStationaryBoundary(self) -> "bool":
        """GetEnforceStationaryBoundary(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self) -> bool"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetEnforceStationaryBoundary(self)

    __swig_destroy__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3

    def cast(obj: 'itkLightObject') -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 *":
        """cast(itkLightObject obj) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 *":
        """GetPointer(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 self) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3"""
        return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3

        Create a new object of the class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.Clone = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Clone, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.UpdateTransformParameters = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_UpdateTransformParameters, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.SetSplineOrder = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetSplineOrder, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.GetSplineOrder = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetSplineOrder, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.SetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetNumberOfControlPointsForTheUpdateField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.GetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetNumberOfControlPointsForTheUpdateField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.SetMeshSizeForTheUpdateField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetMeshSizeForTheUpdateField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.SetNumberOfControlPointsForTheTotalField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetNumberOfControlPointsForTheTotalField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.GetNumberOfControlPointsForTheTotalField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetNumberOfControlPointsForTheTotalField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.SetMeshSizeForTheTotalField = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetMeshSizeForTheTotalField, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.EnforceStationaryBoundaryOn = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_EnforceStationaryBoundaryOn, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.EnforceStationaryBoundaryOff = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_EnforceStationaryBoundaryOff, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.SetEnforceStationaryBoundary = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetEnforceStationaryBoundary, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.GetEnforceStationaryBoundary = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetEnforceStationaryBoundary, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.GetPointer = new_instancemethod(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetPointer, None, itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_swigregister = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_swigregister
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_swigregister(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)

def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__() -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Pointer":
    """itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Pointer"""
    return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__()

def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast(obj: 'itkLightObject') -> "itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 *":
    """itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast(itkLightObject obj) -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3"""
    return _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast(obj)



