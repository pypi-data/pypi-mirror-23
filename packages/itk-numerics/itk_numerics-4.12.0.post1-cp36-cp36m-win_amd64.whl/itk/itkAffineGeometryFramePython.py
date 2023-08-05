# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAffineGeometryFramePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkAffineGeometryFramePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkAffineGeometryFramePython')
    _itkAffineGeometryFramePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAffineGeometryFramePython', [dirname(__file__)])
        except ImportError:
            import _itkAffineGeometryFramePython
            return _itkAffineGeometryFramePython
        try:
            _mod = imp.load_module('_itkAffineGeometryFramePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkAffineGeometryFramePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAffineGeometryFramePython
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


import itkScalableAffineTransformPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import ITKCommonBasePython
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

def itkAffineGeometryFrameD3_New():
  return itkAffineGeometryFrameD3.New()


def itkAffineGeometryFrameD2_New():
  return itkAffineGeometryFrameD2.New()

class itkAffineGeometryFrameD2(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkAffineGeometryFrameD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAffineGeometryFrameD2_Pointer":
        """__New_orig__() -> itkAffineGeometryFrameD2_Pointer"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAffineGeometryFrameD2_Pointer":
        """Clone(itkAffineGeometryFrameD2 self) -> itkAffineGeometryFrameD2_Pointer"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_Clone(self)


    def GetModifiableBoundingBox(self) -> "itkBoundingBoxULL2DVCULLPD2 *":
        """GetModifiableBoundingBox(itkAffineGeometryFrameD2 self) -> itkBoundingBoxULL2DVCULLPD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableBoundingBox(self)


    def GetBoundingBox(self, *args) -> "itkBoundingBoxULL2DVCULLPD2 *":
        """
        GetBoundingBox(itkAffineGeometryFrameD2 self) -> itkBoundingBoxULL2DVCULLPD2
        GetBoundingBox(itkAffineGeometryFrameD2 self) -> itkBoundingBoxULL2DVCULLPD2
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetBoundingBox(self, *args)


    def GetBounds(self) -> "itkFixedArrayD4 const":
        """GetBounds(itkAffineGeometryFrameD2 self) -> itkFixedArrayD4"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetBounds(self)


    def SetBounds(self, bounds: 'itkFixedArrayD4') -> "void":
        """SetBounds(itkAffineGeometryFrameD2 self, itkFixedArrayD4 bounds)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetBounds(self, bounds)


    def GetExtent(self, direction: 'unsigned int') -> "double":
        """GetExtent(itkAffineGeometryFrameD2 self, unsigned int direction) -> double"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetExtent(self, direction)


    def SetIndexToObjectTransform(self, _arg: 'itkScalableAffineTransformD2') -> "void":
        """SetIndexToObjectTransform(itkAffineGeometryFrameD2 self, itkScalableAffineTransformD2 _arg)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetIndexToObjectTransform(self, _arg)


    def GetModifiableIndexToObjectTransform(self) -> "itkScalableAffineTransformD2 *":
        """GetModifiableIndexToObjectTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableIndexToObjectTransform(self)


    def GetIndexToObjectTransform(self, *args) -> "itkScalableAffineTransformD2 *":
        """
        GetIndexToObjectTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        GetIndexToObjectTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetIndexToObjectTransform(self, *args)


    def SetObjectToNodeTransform(self, _arg: 'itkScalableAffineTransformD2') -> "void":
        """SetObjectToNodeTransform(itkAffineGeometryFrameD2 self, itkScalableAffineTransformD2 _arg)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetObjectToNodeTransform(self, _arg)


    def GetModifiableObjectToNodeTransform(self) -> "itkScalableAffineTransformD2 *":
        """GetModifiableObjectToNodeTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableObjectToNodeTransform(self)


    def GetObjectToNodeTransform(self, *args) -> "itkScalableAffineTransformD2 *":
        """
        GetObjectToNodeTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        GetObjectToNodeTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetObjectToNodeTransform(self, *args)


    def SetIndexToWorldTransform(self, _arg: 'itkScalableAffineTransformD2') -> "void":
        """SetIndexToWorldTransform(itkAffineGeometryFrameD2 self, itkScalableAffineTransformD2 _arg)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetIndexToWorldTransform(self, _arg)


    def GetModifiableIndexToWorldTransform(self) -> "itkScalableAffineTransformD2 *":
        """GetModifiableIndexToWorldTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableIndexToWorldTransform(self)


    def GetIndexToWorldTransform(self, *args) -> "itkScalableAffineTransformD2 *":
        """
        GetIndexToWorldTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        GetIndexToWorldTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetIndexToWorldTransform(self, *args)


    def GetModifiableIndexToNodeTransform(self) -> "itkScalableAffineTransformD2 *":
        """GetModifiableIndexToNodeTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableIndexToNodeTransform(self)


    def GetIndexToNodeTransform(self, *args) -> "itkScalableAffineTransformD2 *":
        """
        GetIndexToNodeTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        GetIndexToNodeTransform(itkAffineGeometryFrameD2 self) -> itkScalableAffineTransformD2
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetIndexToNodeTransform(self, *args)


    def Initialize(self) -> "void":
        """Initialize(itkAffineGeometryFrameD2 self)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_Initialize(self)


    def InternalClone(self) -> "itkLightObject_Pointer":
        """InternalClone(itkAffineGeometryFrameD2 self) -> itkLightObject_Pointer"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_InternalClone(self)

    __swig_destroy__ = _itkAffineGeometryFramePython.delete_itkAffineGeometryFrameD2

    def cast(obj: 'itkLightObject') -> "itkAffineGeometryFrameD2 *":
        """cast(itkLightObject obj) -> itkAffineGeometryFrameD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAffineGeometryFrameD2 *":
        """GetPointer(itkAffineGeometryFrameD2 self) -> itkAffineGeometryFrameD2"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAffineGeometryFrameD2

        Create a new object of the class itkAffineGeometryFrameD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAffineGeometryFrameD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAffineGeometryFrameD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAffineGeometryFrameD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAffineGeometryFrameD2.Clone = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_Clone, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetModifiableBoundingBox = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableBoundingBox, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetBoundingBox = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetBoundingBox, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetBounds = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetBounds, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.SetBounds = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetBounds, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetExtent = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetExtent, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.SetIndexToObjectTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetIndexToObjectTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetModifiableIndexToObjectTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableIndexToObjectTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetIndexToObjectTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetIndexToObjectTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.SetObjectToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetObjectToNodeTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetModifiableObjectToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableObjectToNodeTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetObjectToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetObjectToNodeTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.SetIndexToWorldTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_SetIndexToWorldTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetModifiableIndexToWorldTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableIndexToWorldTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetIndexToWorldTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetIndexToWorldTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetModifiableIndexToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetModifiableIndexToNodeTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetIndexToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetIndexToNodeTransform, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.Initialize = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_Initialize, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.InternalClone = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_InternalClone, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2.GetPointer = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD2_GetPointer, None, itkAffineGeometryFrameD2)
itkAffineGeometryFrameD2_swigregister = _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_swigregister
itkAffineGeometryFrameD2_swigregister(itkAffineGeometryFrameD2)

def itkAffineGeometryFrameD2___New_orig__() -> "itkAffineGeometryFrameD2_Pointer":
    """itkAffineGeometryFrameD2___New_orig__() -> itkAffineGeometryFrameD2_Pointer"""
    return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2___New_orig__()

def itkAffineGeometryFrameD2_cast(obj: 'itkLightObject') -> "itkAffineGeometryFrameD2 *":
    """itkAffineGeometryFrameD2_cast(itkLightObject obj) -> itkAffineGeometryFrameD2"""
    return _itkAffineGeometryFramePython.itkAffineGeometryFrameD2_cast(obj)

class itkAffineGeometryFrameD3(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkAffineGeometryFrameD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAffineGeometryFrameD3_Pointer":
        """__New_orig__() -> itkAffineGeometryFrameD3_Pointer"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAffineGeometryFrameD3_Pointer":
        """Clone(itkAffineGeometryFrameD3 self) -> itkAffineGeometryFrameD3_Pointer"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_Clone(self)


    def GetModifiableBoundingBox(self) -> "itkBoundingBoxULL3DVCULLPD3 *":
        """GetModifiableBoundingBox(itkAffineGeometryFrameD3 self) -> itkBoundingBoxULL3DVCULLPD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableBoundingBox(self)


    def GetBoundingBox(self, *args) -> "itkBoundingBoxULL3DVCULLPD3 *":
        """
        GetBoundingBox(itkAffineGeometryFrameD3 self) -> itkBoundingBoxULL3DVCULLPD3
        GetBoundingBox(itkAffineGeometryFrameD3 self) -> itkBoundingBoxULL3DVCULLPD3
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetBoundingBox(self, *args)


    def GetBounds(self) -> "itkFixedArrayD6 const":
        """GetBounds(itkAffineGeometryFrameD3 self) -> itkFixedArrayD6"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetBounds(self)


    def SetBounds(self, bounds: 'itkFixedArrayD6') -> "void":
        """SetBounds(itkAffineGeometryFrameD3 self, itkFixedArrayD6 bounds)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetBounds(self, bounds)


    def GetExtent(self, direction: 'unsigned int') -> "double":
        """GetExtent(itkAffineGeometryFrameD3 self, unsigned int direction) -> double"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetExtent(self, direction)


    def SetIndexToObjectTransform(self, _arg: 'itkScalableAffineTransformD3') -> "void":
        """SetIndexToObjectTransform(itkAffineGeometryFrameD3 self, itkScalableAffineTransformD3 _arg)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetIndexToObjectTransform(self, _arg)


    def GetModifiableIndexToObjectTransform(self) -> "itkScalableAffineTransformD3 *":
        """GetModifiableIndexToObjectTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableIndexToObjectTransform(self)


    def GetIndexToObjectTransform(self, *args) -> "itkScalableAffineTransformD3 *":
        """
        GetIndexToObjectTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        GetIndexToObjectTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetIndexToObjectTransform(self, *args)


    def SetObjectToNodeTransform(self, _arg: 'itkScalableAffineTransformD3') -> "void":
        """SetObjectToNodeTransform(itkAffineGeometryFrameD3 self, itkScalableAffineTransformD3 _arg)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetObjectToNodeTransform(self, _arg)


    def GetModifiableObjectToNodeTransform(self) -> "itkScalableAffineTransformD3 *":
        """GetModifiableObjectToNodeTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableObjectToNodeTransform(self)


    def GetObjectToNodeTransform(self, *args) -> "itkScalableAffineTransformD3 *":
        """
        GetObjectToNodeTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        GetObjectToNodeTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetObjectToNodeTransform(self, *args)


    def SetIndexToWorldTransform(self, _arg: 'itkScalableAffineTransformD3') -> "void":
        """SetIndexToWorldTransform(itkAffineGeometryFrameD3 self, itkScalableAffineTransformD3 _arg)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetIndexToWorldTransform(self, _arg)


    def GetModifiableIndexToWorldTransform(self) -> "itkScalableAffineTransformD3 *":
        """GetModifiableIndexToWorldTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableIndexToWorldTransform(self)


    def GetIndexToWorldTransform(self, *args) -> "itkScalableAffineTransformD3 *":
        """
        GetIndexToWorldTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        GetIndexToWorldTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetIndexToWorldTransform(self, *args)


    def GetModifiableIndexToNodeTransform(self) -> "itkScalableAffineTransformD3 *":
        """GetModifiableIndexToNodeTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableIndexToNodeTransform(self)


    def GetIndexToNodeTransform(self, *args) -> "itkScalableAffineTransformD3 *":
        """
        GetIndexToNodeTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        GetIndexToNodeTransform(itkAffineGeometryFrameD3 self) -> itkScalableAffineTransformD3
        """
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetIndexToNodeTransform(self, *args)


    def Initialize(self) -> "void":
        """Initialize(itkAffineGeometryFrameD3 self)"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_Initialize(self)


    def InternalClone(self) -> "itkLightObject_Pointer":
        """InternalClone(itkAffineGeometryFrameD3 self) -> itkLightObject_Pointer"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_InternalClone(self)

    __swig_destroy__ = _itkAffineGeometryFramePython.delete_itkAffineGeometryFrameD3

    def cast(obj: 'itkLightObject') -> "itkAffineGeometryFrameD3 *":
        """cast(itkLightObject obj) -> itkAffineGeometryFrameD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAffineGeometryFrameD3 *":
        """GetPointer(itkAffineGeometryFrameD3 self) -> itkAffineGeometryFrameD3"""
        return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAffineGeometryFrameD3

        Create a new object of the class itkAffineGeometryFrameD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAffineGeometryFrameD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAffineGeometryFrameD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAffineGeometryFrameD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAffineGeometryFrameD3.Clone = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_Clone, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetModifiableBoundingBox = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableBoundingBox, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetBoundingBox = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetBoundingBox, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetBounds = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetBounds, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.SetBounds = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetBounds, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetExtent = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetExtent, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.SetIndexToObjectTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetIndexToObjectTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetModifiableIndexToObjectTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableIndexToObjectTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetIndexToObjectTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetIndexToObjectTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.SetObjectToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetObjectToNodeTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetModifiableObjectToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableObjectToNodeTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetObjectToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetObjectToNodeTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.SetIndexToWorldTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_SetIndexToWorldTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetModifiableIndexToWorldTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableIndexToWorldTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetIndexToWorldTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetIndexToWorldTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetModifiableIndexToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetModifiableIndexToNodeTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetIndexToNodeTransform = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetIndexToNodeTransform, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.Initialize = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_Initialize, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.InternalClone = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_InternalClone, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3.GetPointer = new_instancemethod(_itkAffineGeometryFramePython.itkAffineGeometryFrameD3_GetPointer, None, itkAffineGeometryFrameD3)
itkAffineGeometryFrameD3_swigregister = _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_swigregister
itkAffineGeometryFrameD3_swigregister(itkAffineGeometryFrameD3)

def itkAffineGeometryFrameD3___New_orig__() -> "itkAffineGeometryFrameD3_Pointer":
    """itkAffineGeometryFrameD3___New_orig__() -> itkAffineGeometryFrameD3_Pointer"""
    return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3___New_orig__()

def itkAffineGeometryFrameD3_cast(obj: 'itkLightObject') -> "itkAffineGeometryFrameD3 *":
    """itkAffineGeometryFrameD3_cast(itkLightObject obj) -> itkAffineGeometryFrameD3"""
    return _itkAffineGeometryFramePython.itkAffineGeometryFrameD3_cast(obj)



