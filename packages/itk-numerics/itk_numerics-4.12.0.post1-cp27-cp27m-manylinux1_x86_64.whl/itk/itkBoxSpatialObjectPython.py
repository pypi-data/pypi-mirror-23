# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBoxSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBoxSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBoxSpatialObjectPython')
    _itkBoxSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBoxSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkBoxSpatialObjectPython
            return _itkBoxSpatialObjectPython
        try:
            _mod = imp.load_module('_itkBoxSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBoxSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBoxSpatialObjectPython
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


import itkSpatialObjectBasePython
import itkAffineGeometryFramePython
import itkScalableAffineTransformPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkAffineTransformPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageRegionPython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython

def itkBoxSpatialObject3_New():
  return itkBoxSpatialObject3.New()


def itkBoxSpatialObject2_New():
  return itkBoxSpatialObject2.New()

class itkBoxSpatialObject2(itkSpatialObjectBasePython.itkSpatialObject2):
    """Proxy of C++ itkBoxSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxSpatialObject2_Pointer"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxSpatialObject2 self) -> itkBoxSpatialObject2_Pointer"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_Clone(self)


    def SetSize(self, _arg):
        """SetSize(itkBoxSpatialObject2 self, itkFixedArrayD2 _arg)"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_SetSize(self, _arg)


    def GetSize(self):
        """GetSize(itkBoxSpatialObject2 self) -> itkFixedArrayD2"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_GetSize(self)


    def ValueAt(self, point, value, depth=0, name=None):
        """
        ValueAt(itkBoxSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkBoxSpatialObject2 self, itkPointD2 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkBoxSpatialObject2 self, itkPointD2 point, double & value) -> bool
        """
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_ValueAt(self, point, value, depth, name)


    def IsEvaluableAt(self, point, depth=0, name=None):
        """
        IsEvaluableAt(itkBoxSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkBoxSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkBoxSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_IsEvaluableAt(self, point, depth, name)


    def IsInside(self, *args):
        """
        IsInside(itkBoxSpatialObject2 self, itkPointD2 point, unsigned int depth, char * arg2) -> bool
        IsInside(itkBoxSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_IsInside(self, *args)

    __swig_destroy__ = _itkBoxSpatialObjectPython.delete_itkBoxSpatialObject2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxSpatialObject2"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxSpatialObject2 self) -> itkBoxSpatialObject2"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxSpatialObject2

        Create a new object of the class itkBoxSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxSpatialObject2.Clone = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_Clone, None, itkBoxSpatialObject2)
itkBoxSpatialObject2.SetSize = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_SetSize, None, itkBoxSpatialObject2)
itkBoxSpatialObject2.GetSize = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_GetSize, None, itkBoxSpatialObject2)
itkBoxSpatialObject2.ValueAt = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_ValueAt, None, itkBoxSpatialObject2)
itkBoxSpatialObject2.IsEvaluableAt = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_IsEvaluableAt, None, itkBoxSpatialObject2)
itkBoxSpatialObject2.IsInside = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_IsInside, None, itkBoxSpatialObject2)
itkBoxSpatialObject2.GetPointer = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_GetPointer, None, itkBoxSpatialObject2)
itkBoxSpatialObject2_swigregister = _itkBoxSpatialObjectPython.itkBoxSpatialObject2_swigregister
itkBoxSpatialObject2_swigregister(itkBoxSpatialObject2)

def itkBoxSpatialObject2___New_orig__():
    """itkBoxSpatialObject2___New_orig__() -> itkBoxSpatialObject2_Pointer"""
    return _itkBoxSpatialObjectPython.itkBoxSpatialObject2___New_orig__()

def itkBoxSpatialObject2_cast(obj):
    """itkBoxSpatialObject2_cast(itkLightObject obj) -> itkBoxSpatialObject2"""
    return _itkBoxSpatialObjectPython.itkBoxSpatialObject2_cast(obj)

class itkBoxSpatialObject3(itkSpatialObjectBasePython.itkSpatialObject3):
    """Proxy of C++ itkBoxSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxSpatialObject3_Pointer"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxSpatialObject3 self) -> itkBoxSpatialObject3_Pointer"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_Clone(self)


    def SetSize(self, _arg):
        """SetSize(itkBoxSpatialObject3 self, itkFixedArrayD3 _arg)"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_SetSize(self, _arg)


    def GetSize(self):
        """GetSize(itkBoxSpatialObject3 self) -> itkFixedArrayD3"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_GetSize(self)


    def ValueAt(self, point, value, depth=0, name=None):
        """
        ValueAt(itkBoxSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0, char * name=None) -> bool
        ValueAt(itkBoxSpatialObject3 self, itkPointD3 point, double & value, unsigned int depth=0) -> bool
        ValueAt(itkBoxSpatialObject3 self, itkPointD3 point, double & value) -> bool
        """
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_ValueAt(self, point, value, depth, name)


    def IsEvaluableAt(self, point, depth=0, name=None):
        """
        IsEvaluableAt(itkBoxSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsEvaluableAt(itkBoxSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsEvaluableAt(itkBoxSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_IsEvaluableAt(self, point, depth, name)


    def IsInside(self, *args):
        """
        IsInside(itkBoxSpatialObject3 self, itkPointD3 point, unsigned int depth, char * arg2) -> bool
        IsInside(itkBoxSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_IsInside(self, *args)

    __swig_destroy__ = _itkBoxSpatialObjectPython.delete_itkBoxSpatialObject3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxSpatialObject3"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxSpatialObject3 self) -> itkBoxSpatialObject3"""
        return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxSpatialObject3

        Create a new object of the class itkBoxSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxSpatialObject3.Clone = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_Clone, None, itkBoxSpatialObject3)
itkBoxSpatialObject3.SetSize = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_SetSize, None, itkBoxSpatialObject3)
itkBoxSpatialObject3.GetSize = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_GetSize, None, itkBoxSpatialObject3)
itkBoxSpatialObject3.ValueAt = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_ValueAt, None, itkBoxSpatialObject3)
itkBoxSpatialObject3.IsEvaluableAt = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_IsEvaluableAt, None, itkBoxSpatialObject3)
itkBoxSpatialObject3.IsInside = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_IsInside, None, itkBoxSpatialObject3)
itkBoxSpatialObject3.GetPointer = new_instancemethod(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_GetPointer, None, itkBoxSpatialObject3)
itkBoxSpatialObject3_swigregister = _itkBoxSpatialObjectPython.itkBoxSpatialObject3_swigregister
itkBoxSpatialObject3_swigregister(itkBoxSpatialObject3)

def itkBoxSpatialObject3___New_orig__():
    """itkBoxSpatialObject3___New_orig__() -> itkBoxSpatialObject3_Pointer"""
    return _itkBoxSpatialObjectPython.itkBoxSpatialObject3___New_orig__()

def itkBoxSpatialObject3_cast(obj):
    """itkBoxSpatialObject3_cast(itkLightObject obj) -> itkBoxSpatialObject3"""
    return _itkBoxSpatialObjectPython.itkBoxSpatialObject3_cast(obj)



