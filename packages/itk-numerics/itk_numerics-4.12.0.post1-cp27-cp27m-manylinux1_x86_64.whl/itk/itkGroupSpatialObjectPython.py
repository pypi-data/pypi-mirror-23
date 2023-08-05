# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGroupSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGroupSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGroupSpatialObjectPython')
    _itkGroupSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGroupSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkGroupSpatialObjectPython
            return _itkGroupSpatialObjectPython
        try:
            _mod = imp.load_module('_itkGroupSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGroupSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGroupSpatialObjectPython
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

def itkGroupSpatialObject3_New():
  return itkGroupSpatialObject3.New()


def itkGroupSpatialObject2_New():
  return itkGroupSpatialObject2.New()

class itkGroupSpatialObject2(itkSpatialObjectBasePython.itkSpatialObject2):
    """Proxy of C++ itkGroupSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkGroupSpatialObject2_Pointer"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkGroupSpatialObject2 self) -> itkGroupSpatialObject2_Pointer"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject2_Clone(self)

    __swig_destroy__ = _itkGroupSpatialObjectPython.delete_itkGroupSpatialObject2

    def cast(obj):
        """cast(itkLightObject obj) -> itkGroupSpatialObject2"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkGroupSpatialObject2 self) -> itkGroupSpatialObject2"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGroupSpatialObject2

        Create a new object of the class itkGroupSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGroupSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGroupSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGroupSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGroupSpatialObject2.Clone = new_instancemethod(_itkGroupSpatialObjectPython.itkGroupSpatialObject2_Clone, None, itkGroupSpatialObject2)
itkGroupSpatialObject2.GetPointer = new_instancemethod(_itkGroupSpatialObjectPython.itkGroupSpatialObject2_GetPointer, None, itkGroupSpatialObject2)
itkGroupSpatialObject2_swigregister = _itkGroupSpatialObjectPython.itkGroupSpatialObject2_swigregister
itkGroupSpatialObject2_swigregister(itkGroupSpatialObject2)

def itkGroupSpatialObject2___New_orig__():
    """itkGroupSpatialObject2___New_orig__() -> itkGroupSpatialObject2_Pointer"""
    return _itkGroupSpatialObjectPython.itkGroupSpatialObject2___New_orig__()

def itkGroupSpatialObject2_cast(obj):
    """itkGroupSpatialObject2_cast(itkLightObject obj) -> itkGroupSpatialObject2"""
    return _itkGroupSpatialObjectPython.itkGroupSpatialObject2_cast(obj)

class itkGroupSpatialObject3(itkSpatialObjectBasePython.itkSpatialObject3):
    """Proxy of C++ itkGroupSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkGroupSpatialObject3_Pointer"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkGroupSpatialObject3 self) -> itkGroupSpatialObject3_Pointer"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject3_Clone(self)

    __swig_destroy__ = _itkGroupSpatialObjectPython.delete_itkGroupSpatialObject3

    def cast(obj):
        """cast(itkLightObject obj) -> itkGroupSpatialObject3"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkGroupSpatialObject3 self) -> itkGroupSpatialObject3"""
        return _itkGroupSpatialObjectPython.itkGroupSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGroupSpatialObject3

        Create a new object of the class itkGroupSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGroupSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGroupSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGroupSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGroupSpatialObject3.Clone = new_instancemethod(_itkGroupSpatialObjectPython.itkGroupSpatialObject3_Clone, None, itkGroupSpatialObject3)
itkGroupSpatialObject3.GetPointer = new_instancemethod(_itkGroupSpatialObjectPython.itkGroupSpatialObject3_GetPointer, None, itkGroupSpatialObject3)
itkGroupSpatialObject3_swigregister = _itkGroupSpatialObjectPython.itkGroupSpatialObject3_swigregister
itkGroupSpatialObject3_swigregister(itkGroupSpatialObject3)

def itkGroupSpatialObject3___New_orig__():
    """itkGroupSpatialObject3___New_orig__() -> itkGroupSpatialObject3_Pointer"""
    return _itkGroupSpatialObjectPython.itkGroupSpatialObject3___New_orig__()

def itkGroupSpatialObject3_cast(obj):
    """itkGroupSpatialObject3_cast(itkLightObject obj) -> itkGroupSpatialObject3"""
    return _itkGroupSpatialObjectPython.itkGroupSpatialObject3_cast(obj)



