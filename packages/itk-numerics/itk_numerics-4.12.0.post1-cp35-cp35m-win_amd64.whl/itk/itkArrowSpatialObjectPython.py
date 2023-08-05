# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkArrowSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkArrowSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkArrowSpatialObjectPython')
    _itkArrowSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkArrowSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkArrowSpatialObjectPython
            return _itkArrowSpatialObjectPython
        try:
            _mod = imp.load_module('_itkArrowSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkArrowSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkArrowSpatialObjectPython
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


import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import ITKCommonBasePython
import itkSpatialObjectBasePython
import itkPointPython
import itkScalableAffineTransformPython
import itkTransformBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkVariableLengthVectorPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkAffineGeometryFramePython
import itkBoundingBoxPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkMapContainerPython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkImageRegionPython

def itkArrowSpatialObject3_New():
  return itkArrowSpatialObject3.New()


def itkArrowSpatialObject2_New():
  return itkArrowSpatialObject2.New()

class itkArrowSpatialObject2(itkSpatialObjectBasePython.itkSpatialObject2):
    """Proxy of C++ itkArrowSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkArrowSpatialObject2_Pointer":
        """__New_orig__() -> itkArrowSpatialObject2_Pointer"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkArrowSpatialObject2_Pointer":
        """Clone(itkArrowSpatialObject2 self) -> itkArrowSpatialObject2_Pointer"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_Clone(self)


    def GetPosition(self) -> "itkPointD2":
        """GetPosition(itkArrowSpatialObject2 self) -> itkPointD2"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetPosition(self)


    def SetPosition(self, *args) -> "void":
        """
        SetPosition(itkArrowSpatialObject2 self, itkPointD2 p)
        SetPosition(itkArrowSpatialObject2 self, float x, float y)
        SetPosition(itkArrowSpatialObject2 self, float x, float y, float z)
        """
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetPosition(self, *args)


    def GetDirection(self) -> "itkVectorD2":
        """GetDirection(itkArrowSpatialObject2 self) -> itkVectorD2"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetDirection(self)


    def SetDirection(self, *args) -> "void":
        """
        SetDirection(itkArrowSpatialObject2 self, itkVectorD2 d)
        SetDirection(itkArrowSpatialObject2 self, float x, float y)
        SetDirection(itkArrowSpatialObject2 self, float x, float y, float z)
        """
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetDirection(self, *args)


    def SetLength(self, length: 'double') -> "void":
        """SetLength(itkArrowSpatialObject2 self, double length)"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetLength(self, length)


    def GetLength(self) -> "double const &":
        """GetLength(itkArrowSpatialObject2 self) -> double const &"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetLength(self)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkArrowSpatialObject2 self, itkPointD2 point, unsigned int depth, char * name) -> bool
        IsInside(itkArrowSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_IsInside(self, *args)

    __swig_destroy__ = _itkArrowSpatialObjectPython.delete_itkArrowSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkArrowSpatialObject2 *":
        """cast(itkLightObject obj) -> itkArrowSpatialObject2"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkArrowSpatialObject2 *":
        """GetPointer(itkArrowSpatialObject2 self) -> itkArrowSpatialObject2"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkArrowSpatialObject2

        Create a new object of the class itkArrowSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkArrowSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkArrowSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkArrowSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkArrowSpatialObject2.Clone = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_Clone, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.GetPosition = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetPosition, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.SetPosition = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetPosition, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.GetDirection = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetDirection, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.SetDirection = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetDirection, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.SetLength = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetLength, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.GetLength = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetLength, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.IsInside = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_IsInside, None, itkArrowSpatialObject2)
itkArrowSpatialObject2.GetPointer = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetPointer, None, itkArrowSpatialObject2)
itkArrowSpatialObject2_swigregister = _itkArrowSpatialObjectPython.itkArrowSpatialObject2_swigregister
itkArrowSpatialObject2_swigregister(itkArrowSpatialObject2)

def itkArrowSpatialObject2___New_orig__() -> "itkArrowSpatialObject2_Pointer":
    """itkArrowSpatialObject2___New_orig__() -> itkArrowSpatialObject2_Pointer"""
    return _itkArrowSpatialObjectPython.itkArrowSpatialObject2___New_orig__()

def itkArrowSpatialObject2_cast(obj: 'itkLightObject') -> "itkArrowSpatialObject2 *":
    """itkArrowSpatialObject2_cast(itkLightObject obj) -> itkArrowSpatialObject2"""
    return _itkArrowSpatialObjectPython.itkArrowSpatialObject2_cast(obj)

class itkArrowSpatialObject3(itkSpatialObjectBasePython.itkSpatialObject3):
    """Proxy of C++ itkArrowSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkArrowSpatialObject3_Pointer":
        """__New_orig__() -> itkArrowSpatialObject3_Pointer"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkArrowSpatialObject3_Pointer":
        """Clone(itkArrowSpatialObject3 self) -> itkArrowSpatialObject3_Pointer"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_Clone(self)


    def GetPosition(self) -> "itkPointD3":
        """GetPosition(itkArrowSpatialObject3 self) -> itkPointD3"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetPosition(self)


    def SetPosition(self, *args) -> "void":
        """
        SetPosition(itkArrowSpatialObject3 self, itkPointD3 p)
        SetPosition(itkArrowSpatialObject3 self, float x, float y)
        SetPosition(itkArrowSpatialObject3 self, float x, float y, float z)
        """
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetPosition(self, *args)


    def GetDirection(self) -> "itkVectorD3":
        """GetDirection(itkArrowSpatialObject3 self) -> itkVectorD3"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetDirection(self)


    def SetDirection(self, *args) -> "void":
        """
        SetDirection(itkArrowSpatialObject3 self, itkVectorD3 d)
        SetDirection(itkArrowSpatialObject3 self, float x, float y)
        SetDirection(itkArrowSpatialObject3 self, float x, float y, float z)
        """
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetDirection(self, *args)


    def SetLength(self, length: 'double') -> "void":
        """SetLength(itkArrowSpatialObject3 self, double length)"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetLength(self, length)


    def GetLength(self) -> "double const &":
        """GetLength(itkArrowSpatialObject3 self) -> double const &"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetLength(self)


    def IsInside(self, *args) -> "bool":
        """
        IsInside(itkArrowSpatialObject3 self, itkPointD3 point, unsigned int depth, char * name) -> bool
        IsInside(itkArrowSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_IsInside(self, *args)

    __swig_destroy__ = _itkArrowSpatialObjectPython.delete_itkArrowSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkArrowSpatialObject3 *":
        """cast(itkLightObject obj) -> itkArrowSpatialObject3"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkArrowSpatialObject3 *":
        """GetPointer(itkArrowSpatialObject3 self) -> itkArrowSpatialObject3"""
        return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkArrowSpatialObject3

        Create a new object of the class itkArrowSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkArrowSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkArrowSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkArrowSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkArrowSpatialObject3.Clone = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_Clone, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.GetPosition = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetPosition, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.SetPosition = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetPosition, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.GetDirection = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetDirection, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.SetDirection = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetDirection, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.SetLength = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetLength, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.GetLength = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetLength, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.IsInside = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_IsInside, None, itkArrowSpatialObject3)
itkArrowSpatialObject3.GetPointer = new_instancemethod(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetPointer, None, itkArrowSpatialObject3)
itkArrowSpatialObject3_swigregister = _itkArrowSpatialObjectPython.itkArrowSpatialObject3_swigregister
itkArrowSpatialObject3_swigregister(itkArrowSpatialObject3)

def itkArrowSpatialObject3___New_orig__() -> "itkArrowSpatialObject3_Pointer":
    """itkArrowSpatialObject3___New_orig__() -> itkArrowSpatialObject3_Pointer"""
    return _itkArrowSpatialObjectPython.itkArrowSpatialObject3___New_orig__()

def itkArrowSpatialObject3_cast(obj: 'itkLightObject') -> "itkArrowSpatialObject3 *":
    """itkArrowSpatialObject3_cast(itkLightObject obj) -> itkArrowSpatialObject3"""
    return _itkArrowSpatialObjectPython.itkArrowSpatialObject3_cast(obj)



