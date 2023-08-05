# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTimeVaryingVelocityFieldTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTimeVaryingVelocityFieldTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTimeVaryingVelocityFieldTransformPython')
    _itkTimeVaryingVelocityFieldTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTimeVaryingVelocityFieldTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkTimeVaryingVelocityFieldTransformPython
            return _itkTimeVaryingVelocityFieldTransformPython
        try:
            _mod = imp.load_module('_itkTimeVaryingVelocityFieldTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTimeVaryingVelocityFieldTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTimeVaryingVelocityFieldTransformPython
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
import itkVelocityFieldTransformPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkDisplacementFieldTransformPython

def itkTimeVaryingVelocityFieldTransformD3_New():
  return itkTimeVaryingVelocityFieldTransformD3.New()


def itkTimeVaryingVelocityFieldTransformD2_New():
  return itkTimeVaryingVelocityFieldTransformD2.New()

class itkTimeVaryingVelocityFieldTransformD2(itkVelocityFieldTransformPython.itkVelocityFieldTransformD2):
    """Proxy of C++ itkTimeVaryingVelocityFieldTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTimeVaryingVelocityFieldTransformD2_Pointer":
        """__New_orig__() -> itkTimeVaryingVelocityFieldTransformD2_Pointer"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTimeVaryingVelocityFieldTransformD2_Pointer":
        """Clone(itkTimeVaryingVelocityFieldTransformD2 self) -> itkTimeVaryingVelocityFieldTransformD2_Pointer"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_Clone(self)


    def GetModifiableTimeVaryingVelocityField(self) -> "itkImageVD23 *":
        """GetModifiableTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD2 self) -> itkImageVD23"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetModifiableTimeVaryingVelocityField(self)


    def GetTimeVaryingVelocityField(self, *args) -> "itkImageVD23 const *":
        """
        GetTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD2 self) -> itkImageVD23
        GetTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD2 self) -> itkImageVD23
        """
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetTimeVaryingVelocityField(self, *args)


    def SetTimeVaryingVelocityField(self, field: 'itkImageVD23') -> "void":
        """SetTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD2 self, itkImageVD23 field)"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_SetTimeVaryingVelocityField(self, field)

    __swig_destroy__ = _itkTimeVaryingVelocityFieldTransformPython.delete_itkTimeVaryingVelocityFieldTransformD2

    def cast(obj: 'itkLightObject') -> "itkTimeVaryingVelocityFieldTransformD2 *":
        """cast(itkLightObject obj) -> itkTimeVaryingVelocityFieldTransformD2"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTimeVaryingVelocityFieldTransformD2 *":
        """GetPointer(itkTimeVaryingVelocityFieldTransformD2 self) -> itkTimeVaryingVelocityFieldTransformD2"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTimeVaryingVelocityFieldTransformD2

        Create a new object of the class itkTimeVaryingVelocityFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTimeVaryingVelocityFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTimeVaryingVelocityFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTimeVaryingVelocityFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTimeVaryingVelocityFieldTransformD2.Clone = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_Clone, None, itkTimeVaryingVelocityFieldTransformD2)
itkTimeVaryingVelocityFieldTransformD2.GetModifiableTimeVaryingVelocityField = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetModifiableTimeVaryingVelocityField, None, itkTimeVaryingVelocityFieldTransformD2)
itkTimeVaryingVelocityFieldTransformD2.GetTimeVaryingVelocityField = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetTimeVaryingVelocityField, None, itkTimeVaryingVelocityFieldTransformD2)
itkTimeVaryingVelocityFieldTransformD2.SetTimeVaryingVelocityField = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_SetTimeVaryingVelocityField, None, itkTimeVaryingVelocityFieldTransformD2)
itkTimeVaryingVelocityFieldTransformD2.GetPointer = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetPointer, None, itkTimeVaryingVelocityFieldTransformD2)
itkTimeVaryingVelocityFieldTransformD2_swigregister = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_swigregister
itkTimeVaryingVelocityFieldTransformD2_swigregister(itkTimeVaryingVelocityFieldTransformD2)

def itkTimeVaryingVelocityFieldTransformD2___New_orig__() -> "itkTimeVaryingVelocityFieldTransformD2_Pointer":
    """itkTimeVaryingVelocityFieldTransformD2___New_orig__() -> itkTimeVaryingVelocityFieldTransformD2_Pointer"""
    return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2___New_orig__()

def itkTimeVaryingVelocityFieldTransformD2_cast(obj: 'itkLightObject') -> "itkTimeVaryingVelocityFieldTransformD2 *":
    """itkTimeVaryingVelocityFieldTransformD2_cast(itkLightObject obj) -> itkTimeVaryingVelocityFieldTransformD2"""
    return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_cast(obj)

class itkTimeVaryingVelocityFieldTransformD3(itkVelocityFieldTransformPython.itkVelocityFieldTransformD3):
    """Proxy of C++ itkTimeVaryingVelocityFieldTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTimeVaryingVelocityFieldTransformD3_Pointer":
        """__New_orig__() -> itkTimeVaryingVelocityFieldTransformD3_Pointer"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTimeVaryingVelocityFieldTransformD3_Pointer":
        """Clone(itkTimeVaryingVelocityFieldTransformD3 self) -> itkTimeVaryingVelocityFieldTransformD3_Pointer"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_Clone(self)


    def GetModifiableTimeVaryingVelocityField(self) -> "itkImageVD34 *":
        """GetModifiableTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD3 self) -> itkImageVD34"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetModifiableTimeVaryingVelocityField(self)


    def GetTimeVaryingVelocityField(self, *args) -> "itkImageVD34 const *":
        """
        GetTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD3 self) -> itkImageVD34
        GetTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD3 self) -> itkImageVD34
        """
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetTimeVaryingVelocityField(self, *args)


    def SetTimeVaryingVelocityField(self, field: 'itkImageVD34') -> "void":
        """SetTimeVaryingVelocityField(itkTimeVaryingVelocityFieldTransformD3 self, itkImageVD34 field)"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_SetTimeVaryingVelocityField(self, field)

    __swig_destroy__ = _itkTimeVaryingVelocityFieldTransformPython.delete_itkTimeVaryingVelocityFieldTransformD3

    def cast(obj: 'itkLightObject') -> "itkTimeVaryingVelocityFieldTransformD3 *":
        """cast(itkLightObject obj) -> itkTimeVaryingVelocityFieldTransformD3"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTimeVaryingVelocityFieldTransformD3 *":
        """GetPointer(itkTimeVaryingVelocityFieldTransformD3 self) -> itkTimeVaryingVelocityFieldTransformD3"""
        return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTimeVaryingVelocityFieldTransformD3

        Create a new object of the class itkTimeVaryingVelocityFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTimeVaryingVelocityFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTimeVaryingVelocityFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTimeVaryingVelocityFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTimeVaryingVelocityFieldTransformD3.Clone = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_Clone, None, itkTimeVaryingVelocityFieldTransformD3)
itkTimeVaryingVelocityFieldTransformD3.GetModifiableTimeVaryingVelocityField = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetModifiableTimeVaryingVelocityField, None, itkTimeVaryingVelocityFieldTransformD3)
itkTimeVaryingVelocityFieldTransformD3.GetTimeVaryingVelocityField = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetTimeVaryingVelocityField, None, itkTimeVaryingVelocityFieldTransformD3)
itkTimeVaryingVelocityFieldTransformD3.SetTimeVaryingVelocityField = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_SetTimeVaryingVelocityField, None, itkTimeVaryingVelocityFieldTransformD3)
itkTimeVaryingVelocityFieldTransformD3.GetPointer = new_instancemethod(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetPointer, None, itkTimeVaryingVelocityFieldTransformD3)
itkTimeVaryingVelocityFieldTransformD3_swigregister = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_swigregister
itkTimeVaryingVelocityFieldTransformD3_swigregister(itkTimeVaryingVelocityFieldTransformD3)

def itkTimeVaryingVelocityFieldTransformD3___New_orig__() -> "itkTimeVaryingVelocityFieldTransformD3_Pointer":
    """itkTimeVaryingVelocityFieldTransformD3___New_orig__() -> itkTimeVaryingVelocityFieldTransformD3_Pointer"""
    return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3___New_orig__()

def itkTimeVaryingVelocityFieldTransformD3_cast(obj: 'itkLightObject') -> "itkTimeVaryingVelocityFieldTransformD3 *":
    """itkTimeVaryingVelocityFieldTransformD3_cast(itkLightObject obj) -> itkTimeVaryingVelocityFieldTransformD3"""
    return _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_cast(obj)



