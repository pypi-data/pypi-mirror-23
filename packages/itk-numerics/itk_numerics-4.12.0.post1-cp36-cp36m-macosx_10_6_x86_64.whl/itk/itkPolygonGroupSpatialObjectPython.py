# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPolygonGroupSpatialObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPolygonGroupSpatialObjectPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPolygonGroupSpatialObjectPython')
    _itkPolygonGroupSpatialObjectPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPolygonGroupSpatialObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkPolygonGroupSpatialObjectPython
            return _itkPolygonGroupSpatialObjectPython
        try:
            _mod = imp.load_module('_itkPolygonGroupSpatialObjectPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPolygonGroupSpatialObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPolygonGroupSpatialObjectPython
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
import itkGroupSpatialObjectPython
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
import itkPolygonSpatialObjectPython
import itkBlobSpatialObjectPython
import itkPointBasedSpatialObjectPython
import itkSpatialObjectPointPython

def itkPolygonGroupSpatialObject3_New():
  return itkPolygonGroupSpatialObject3.New()


def itkPolygonGroupSpatialObject2_New():
  return itkPolygonGroupSpatialObject2.New()

class itkPolygonGroupSpatialObject2(itkGroupSpatialObjectPython.itkGroupSpatialObject2):
    """Proxy of C++ itkPolygonGroupSpatialObject2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPolygonGroupSpatialObject2_Pointer":
        """__New_orig__() -> itkPolygonGroupSpatialObject2_Pointer"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPolygonGroupSpatialObject2_Pointer":
        """Clone(itkPolygonGroupSpatialObject2 self) -> itkPolygonGroupSpatialObject2_Pointer"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_Clone(self)


    def AddStrand(self, toAdd: 'itkPolygonSpatialObject2') -> "bool":
        """AddStrand(itkPolygonGroupSpatialObject2 self, itkPolygonSpatialObject2 toAdd) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_AddStrand(self, toAdd)


    def DeleteStrand(self, toDelete: 'itkPolygonSpatialObject2') -> "bool":
        """DeleteStrand(itkPolygonGroupSpatialObject2 self, itkPolygonSpatialObject2 toDelete) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_DeleteStrand(self, toDelete)


    def ReplaceStrand(self, toReplace: 'itkPolygonSpatialObject2', replacement: 'itkPolygonSpatialObject2') -> "bool":
        """ReplaceStrand(itkPolygonGroupSpatialObject2 self, itkPolygonSpatialObject2 toReplace, itkPolygonSpatialObject2 replacement) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_ReplaceStrand(self, toReplace, replacement)


    def IsClosed(self) -> "bool":
        """IsClosed(itkPolygonGroupSpatialObject2 self) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_IsClosed(self)


    def NumberOfStrands(self) -> "unsigned int":
        """NumberOfStrands(itkPolygonGroupSpatialObject2 self) -> unsigned int"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_NumberOfStrands(self)


    def Volume(self) -> "double":
        """Volume(itkPolygonGroupSpatialObject2 self) -> double"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_Volume(self)


    def MeasureVolume(self) -> "double":
        """MeasureVolume(itkPolygonGroupSpatialObject2 self) -> double"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_MeasureVolume(self)


    def IsInside(self, point: 'itkPointD2', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsInside(itkPolygonGroupSpatialObject2 self, itkPointD2 point, unsigned int depth=0, char * name=None) -> bool
        IsInside(itkPolygonGroupSpatialObject2 self, itkPointD2 point, unsigned int depth=0) -> bool
        IsInside(itkPolygonGroupSpatialObject2 self, itkPointD2 point) -> bool
        """
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_IsInside(self, point, depth, name)

    __swig_destroy__ = _itkPolygonGroupSpatialObjectPython.delete_itkPolygonGroupSpatialObject2

    def cast(obj: 'itkLightObject') -> "itkPolygonGroupSpatialObject2 *":
        """cast(itkLightObject obj) -> itkPolygonGroupSpatialObject2"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPolygonGroupSpatialObject2 *":
        """GetPointer(itkPolygonGroupSpatialObject2 self) -> itkPolygonGroupSpatialObject2"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPolygonGroupSpatialObject2

        Create a new object of the class itkPolygonGroupSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolygonGroupSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPolygonGroupSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPolygonGroupSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPolygonGroupSpatialObject2.Clone = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_Clone, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.AddStrand = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_AddStrand, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.DeleteStrand = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_DeleteStrand, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.ReplaceStrand = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_ReplaceStrand, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.IsClosed = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_IsClosed, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.NumberOfStrands = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_NumberOfStrands, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.Volume = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_Volume, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.MeasureVolume = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_MeasureVolume, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.IsInside = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_IsInside, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2.GetPointer = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_GetPointer, None, itkPolygonGroupSpatialObject2)
itkPolygonGroupSpatialObject2_swigregister = _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_swigregister
itkPolygonGroupSpatialObject2_swigregister(itkPolygonGroupSpatialObject2)

def itkPolygonGroupSpatialObject2___New_orig__() -> "itkPolygonGroupSpatialObject2_Pointer":
    """itkPolygonGroupSpatialObject2___New_orig__() -> itkPolygonGroupSpatialObject2_Pointer"""
    return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2___New_orig__()

def itkPolygonGroupSpatialObject2_cast(obj: 'itkLightObject') -> "itkPolygonGroupSpatialObject2 *":
    """itkPolygonGroupSpatialObject2_cast(itkLightObject obj) -> itkPolygonGroupSpatialObject2"""
    return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject2_cast(obj)

class itkPolygonGroupSpatialObject3(itkGroupSpatialObjectPython.itkGroupSpatialObject3):
    """Proxy of C++ itkPolygonGroupSpatialObject3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPolygonGroupSpatialObject3_Pointer":
        """__New_orig__() -> itkPolygonGroupSpatialObject3_Pointer"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPolygonGroupSpatialObject3_Pointer":
        """Clone(itkPolygonGroupSpatialObject3 self) -> itkPolygonGroupSpatialObject3_Pointer"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_Clone(self)


    def AddStrand(self, toAdd: 'itkPolygonSpatialObject3') -> "bool":
        """AddStrand(itkPolygonGroupSpatialObject3 self, itkPolygonSpatialObject3 toAdd) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_AddStrand(self, toAdd)


    def DeleteStrand(self, toDelete: 'itkPolygonSpatialObject3') -> "bool":
        """DeleteStrand(itkPolygonGroupSpatialObject3 self, itkPolygonSpatialObject3 toDelete) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_DeleteStrand(self, toDelete)


    def ReplaceStrand(self, toReplace: 'itkPolygonSpatialObject3', replacement: 'itkPolygonSpatialObject3') -> "bool":
        """ReplaceStrand(itkPolygonGroupSpatialObject3 self, itkPolygonSpatialObject3 toReplace, itkPolygonSpatialObject3 replacement) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_ReplaceStrand(self, toReplace, replacement)


    def IsClosed(self) -> "bool":
        """IsClosed(itkPolygonGroupSpatialObject3 self) -> bool"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_IsClosed(self)


    def NumberOfStrands(self) -> "unsigned int":
        """NumberOfStrands(itkPolygonGroupSpatialObject3 self) -> unsigned int"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_NumberOfStrands(self)


    def Volume(self) -> "double":
        """Volume(itkPolygonGroupSpatialObject3 self) -> double"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_Volume(self)


    def MeasureVolume(self) -> "double":
        """MeasureVolume(itkPolygonGroupSpatialObject3 self) -> double"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_MeasureVolume(self)


    def IsInside(self, point: 'itkPointD3', depth: 'unsigned int'=0, name: 'char *'=None) -> "bool":
        """
        IsInside(itkPolygonGroupSpatialObject3 self, itkPointD3 point, unsigned int depth=0, char * name=None) -> bool
        IsInside(itkPolygonGroupSpatialObject3 self, itkPointD3 point, unsigned int depth=0) -> bool
        IsInside(itkPolygonGroupSpatialObject3 self, itkPointD3 point) -> bool
        """
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_IsInside(self, point, depth, name)

    __swig_destroy__ = _itkPolygonGroupSpatialObjectPython.delete_itkPolygonGroupSpatialObject3

    def cast(obj: 'itkLightObject') -> "itkPolygonGroupSpatialObject3 *":
        """cast(itkLightObject obj) -> itkPolygonGroupSpatialObject3"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPolygonGroupSpatialObject3 *":
        """GetPointer(itkPolygonGroupSpatialObject3 self) -> itkPolygonGroupSpatialObject3"""
        return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPolygonGroupSpatialObject3

        Create a new object of the class itkPolygonGroupSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolygonGroupSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPolygonGroupSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPolygonGroupSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPolygonGroupSpatialObject3.Clone = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_Clone, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.AddStrand = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_AddStrand, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.DeleteStrand = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_DeleteStrand, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.ReplaceStrand = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_ReplaceStrand, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.IsClosed = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_IsClosed, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.NumberOfStrands = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_NumberOfStrands, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.Volume = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_Volume, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.MeasureVolume = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_MeasureVolume, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.IsInside = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_IsInside, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3.GetPointer = new_instancemethod(_itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_GetPointer, None, itkPolygonGroupSpatialObject3)
itkPolygonGroupSpatialObject3_swigregister = _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_swigregister
itkPolygonGroupSpatialObject3_swigregister(itkPolygonGroupSpatialObject3)

def itkPolygonGroupSpatialObject3___New_orig__() -> "itkPolygonGroupSpatialObject3_Pointer":
    """itkPolygonGroupSpatialObject3___New_orig__() -> itkPolygonGroupSpatialObject3_Pointer"""
    return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3___New_orig__()

def itkPolygonGroupSpatialObject3_cast(obj: 'itkLightObject') -> "itkPolygonGroupSpatialObject3 *":
    """itkPolygonGroupSpatialObject3_cast(itkLightObject obj) -> itkPolygonGroupSpatialObject3"""
    return _itkPolygonGroupSpatialObjectPython.itkPolygonGroupSpatialObject3_cast(obj)



