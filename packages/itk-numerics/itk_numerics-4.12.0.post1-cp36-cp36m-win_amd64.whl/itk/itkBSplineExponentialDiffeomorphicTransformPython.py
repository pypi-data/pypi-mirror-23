# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineExponentialDiffeomorphicTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBSplineExponentialDiffeomorphicTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBSplineExponentialDiffeomorphicTransformPython')
    _itkBSplineExponentialDiffeomorphicTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineExponentialDiffeomorphicTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineExponentialDiffeomorphicTransformPython
            return _itkBSplineExponentialDiffeomorphicTransformPython
        try:
            _mod = imp.load_module('_itkBSplineExponentialDiffeomorphicTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBSplineExponentialDiffeomorphicTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineExponentialDiffeomorphicTransformPython
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


import itkFixedArrayPython
import pyBasePython
import itkImagePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkConstantVelocityFieldTransformPython
import itkTransformBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkArrayPython
import itkOptimizerParametersPython
import itkVariableLengthVectorPython
import itkDisplacementFieldTransformPython

def itkBSplineExponentialDiffeomorphicTransformD3_New():
  return itkBSplineExponentialDiffeomorphicTransformD3.New()


def itkBSplineExponentialDiffeomorphicTransformD2_New():
  return itkBSplineExponentialDiffeomorphicTransformD2.New()

class itkBSplineExponentialDiffeomorphicTransformD2(itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2):
    """Proxy of C++ itkBSplineExponentialDiffeomorphicTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineExponentialDiffeomorphicTransformD2_Pointer":
        """__New_orig__() -> itkBSplineExponentialDiffeomorphicTransformD2_Pointer"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineExponentialDiffeomorphicTransformD2_Pointer":
        """Clone(itkBSplineExponentialDiffeomorphicTransformD2 self) -> itkBSplineExponentialDiffeomorphicTransformD2_Pointer"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineExponentialDiffeomorphicTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineExponentialDiffeomorphicTransformD2 self, itkArrayD update)
        """
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_UpdateTransformParameters(self, update, factor)


    def BSplineSmoothConstantVelocityField(self, arg0: 'itkImageVD22', arg1: 'itkFixedArrayUI2') -> "itkImageVD22_Pointer":
        """BSplineSmoothConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD2 self, itkImageVD22 arg0, itkFixedArrayUI2 arg1) -> itkImageVD22_Pointer"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_BSplineSmoothConstantVelocityField(self, arg0, arg1)


    def SetSplineOrder(self, _arg: 'unsigned int const') -> "void":
        """SetSplineOrder(itkBSplineExponentialDiffeomorphicTransformD2 self, unsigned int const _arg)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetSplineOrder(self, _arg)


    def GetSplineOrder(self) -> "unsigned int":
        """GetSplineOrder(itkBSplineExponentialDiffeomorphicTransformD2 self) -> unsigned int"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetSplineOrder(self)


    def SetNumberOfControlPointsForTheConstantVelocityField(self, _arg: 'itkFixedArrayUI2') -> "void":
        """SetNumberOfControlPointsForTheConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD2 self, itkFixedArrayUI2 _arg)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetNumberOfControlPointsForTheConstantVelocityField(self, _arg)


    def GetNumberOfControlPointsForTheConstantVelocityField(self) -> "itkFixedArrayUI2":
        """GetNumberOfControlPointsForTheConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD2 self) -> itkFixedArrayUI2"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetNumberOfControlPointsForTheConstantVelocityField(self)


    def SetNumberOfControlPointsForTheUpdateField(self, _arg: 'itkFixedArrayUI2') -> "void":
        """SetNumberOfControlPointsForTheUpdateField(itkBSplineExponentialDiffeomorphicTransformD2 self, itkFixedArrayUI2 _arg)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetNumberOfControlPointsForTheUpdateField(self, _arg)


    def GetNumberOfControlPointsForTheUpdateField(self) -> "itkFixedArrayUI2":
        """GetNumberOfControlPointsForTheUpdateField(itkBSplineExponentialDiffeomorphicTransformD2 self) -> itkFixedArrayUI2"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetNumberOfControlPointsForTheUpdateField(self)


    def SetMeshSizeForTheConstantVelocityField(self, arg0: 'itkFixedArrayUI2') -> "void":
        """SetMeshSizeForTheConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD2 self, itkFixedArrayUI2 arg0)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetMeshSizeForTheConstantVelocityField(self, arg0)


    def SetMeshSizeForTheUpdateField(self, arg0: 'itkFixedArrayUI2') -> "void":
        """SetMeshSizeForTheUpdateField(itkBSplineExponentialDiffeomorphicTransformD2 self, itkFixedArrayUI2 arg0)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetMeshSizeForTheUpdateField(self, arg0)

    __swig_destroy__ = _itkBSplineExponentialDiffeomorphicTransformPython.delete_itkBSplineExponentialDiffeomorphicTransformD2

    def cast(obj: 'itkLightObject') -> "itkBSplineExponentialDiffeomorphicTransformD2 *":
        """cast(itkLightObject obj) -> itkBSplineExponentialDiffeomorphicTransformD2"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineExponentialDiffeomorphicTransformD2 *":
        """GetPointer(itkBSplineExponentialDiffeomorphicTransformD2 self) -> itkBSplineExponentialDiffeomorphicTransformD2"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineExponentialDiffeomorphicTransformD2

        Create a new object of the class itkBSplineExponentialDiffeomorphicTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineExponentialDiffeomorphicTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineExponentialDiffeomorphicTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineExponentialDiffeomorphicTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineExponentialDiffeomorphicTransformD2.Clone = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_Clone, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.UpdateTransformParameters = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_UpdateTransformParameters, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.BSplineSmoothConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_BSplineSmoothConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.SetSplineOrder = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetSplineOrder, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.GetSplineOrder = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetSplineOrder, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.SetNumberOfControlPointsForTheConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetNumberOfControlPointsForTheConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.GetNumberOfControlPointsForTheConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetNumberOfControlPointsForTheConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.SetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetNumberOfControlPointsForTheUpdateField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.GetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetNumberOfControlPointsForTheUpdateField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.SetMeshSizeForTheConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetMeshSizeForTheConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.SetMeshSizeForTheUpdateField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetMeshSizeForTheUpdateField, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2.GetPointer = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetPointer, None, itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2_swigregister = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_swigregister
itkBSplineExponentialDiffeomorphicTransformD2_swigregister(itkBSplineExponentialDiffeomorphicTransformD2)

def itkBSplineExponentialDiffeomorphicTransformD2___New_orig__() -> "itkBSplineExponentialDiffeomorphicTransformD2_Pointer":
    """itkBSplineExponentialDiffeomorphicTransformD2___New_orig__() -> itkBSplineExponentialDiffeomorphicTransformD2_Pointer"""
    return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2___New_orig__()

def itkBSplineExponentialDiffeomorphicTransformD2_cast(obj: 'itkLightObject') -> "itkBSplineExponentialDiffeomorphicTransformD2 *":
    """itkBSplineExponentialDiffeomorphicTransformD2_cast(itkLightObject obj) -> itkBSplineExponentialDiffeomorphicTransformD2"""
    return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_cast(obj)

class itkBSplineExponentialDiffeomorphicTransformD3(itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3):
    """Proxy of C++ itkBSplineExponentialDiffeomorphicTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineExponentialDiffeomorphicTransformD3_Pointer":
        """__New_orig__() -> itkBSplineExponentialDiffeomorphicTransformD3_Pointer"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineExponentialDiffeomorphicTransformD3_Pointer":
        """Clone(itkBSplineExponentialDiffeomorphicTransformD3 self) -> itkBSplineExponentialDiffeomorphicTransformD3_Pointer"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineExponentialDiffeomorphicTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineExponentialDiffeomorphicTransformD3 self, itkArrayD update)
        """
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_UpdateTransformParameters(self, update, factor)


    def BSplineSmoothConstantVelocityField(self, arg0: 'itkImageVD33', arg1: 'itkFixedArrayUI3') -> "itkImageVD33_Pointer":
        """BSplineSmoothConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD3 self, itkImageVD33 arg0, itkFixedArrayUI3 arg1) -> itkImageVD33_Pointer"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_BSplineSmoothConstantVelocityField(self, arg0, arg1)


    def SetSplineOrder(self, _arg: 'unsigned int const') -> "void":
        """SetSplineOrder(itkBSplineExponentialDiffeomorphicTransformD3 self, unsigned int const _arg)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetSplineOrder(self, _arg)


    def GetSplineOrder(self) -> "unsigned int":
        """GetSplineOrder(itkBSplineExponentialDiffeomorphicTransformD3 self) -> unsigned int"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetSplineOrder(self)


    def SetNumberOfControlPointsForTheConstantVelocityField(self, _arg: 'itkFixedArrayUI3') -> "void":
        """SetNumberOfControlPointsForTheConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD3 self, itkFixedArrayUI3 _arg)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetNumberOfControlPointsForTheConstantVelocityField(self, _arg)


    def GetNumberOfControlPointsForTheConstantVelocityField(self) -> "itkFixedArrayUI3":
        """GetNumberOfControlPointsForTheConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD3 self) -> itkFixedArrayUI3"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetNumberOfControlPointsForTheConstantVelocityField(self)


    def SetNumberOfControlPointsForTheUpdateField(self, _arg: 'itkFixedArrayUI3') -> "void":
        """SetNumberOfControlPointsForTheUpdateField(itkBSplineExponentialDiffeomorphicTransformD3 self, itkFixedArrayUI3 _arg)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetNumberOfControlPointsForTheUpdateField(self, _arg)


    def GetNumberOfControlPointsForTheUpdateField(self) -> "itkFixedArrayUI3":
        """GetNumberOfControlPointsForTheUpdateField(itkBSplineExponentialDiffeomorphicTransformD3 self) -> itkFixedArrayUI3"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetNumberOfControlPointsForTheUpdateField(self)


    def SetMeshSizeForTheConstantVelocityField(self, arg0: 'itkFixedArrayUI3') -> "void":
        """SetMeshSizeForTheConstantVelocityField(itkBSplineExponentialDiffeomorphicTransformD3 self, itkFixedArrayUI3 arg0)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetMeshSizeForTheConstantVelocityField(self, arg0)


    def SetMeshSizeForTheUpdateField(self, arg0: 'itkFixedArrayUI3') -> "void":
        """SetMeshSizeForTheUpdateField(itkBSplineExponentialDiffeomorphicTransformD3 self, itkFixedArrayUI3 arg0)"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetMeshSizeForTheUpdateField(self, arg0)

    __swig_destroy__ = _itkBSplineExponentialDiffeomorphicTransformPython.delete_itkBSplineExponentialDiffeomorphicTransformD3

    def cast(obj: 'itkLightObject') -> "itkBSplineExponentialDiffeomorphicTransformD3 *":
        """cast(itkLightObject obj) -> itkBSplineExponentialDiffeomorphicTransformD3"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineExponentialDiffeomorphicTransformD3 *":
        """GetPointer(itkBSplineExponentialDiffeomorphicTransformD3 self) -> itkBSplineExponentialDiffeomorphicTransformD3"""
        return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineExponentialDiffeomorphicTransformD3

        Create a new object of the class itkBSplineExponentialDiffeomorphicTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineExponentialDiffeomorphicTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineExponentialDiffeomorphicTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineExponentialDiffeomorphicTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineExponentialDiffeomorphicTransformD3.Clone = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_Clone, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.UpdateTransformParameters = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_UpdateTransformParameters, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.BSplineSmoothConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_BSplineSmoothConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.SetSplineOrder = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetSplineOrder, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.GetSplineOrder = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetSplineOrder, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.SetNumberOfControlPointsForTheConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetNumberOfControlPointsForTheConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.GetNumberOfControlPointsForTheConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetNumberOfControlPointsForTheConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.SetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetNumberOfControlPointsForTheUpdateField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.GetNumberOfControlPointsForTheUpdateField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetNumberOfControlPointsForTheUpdateField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.SetMeshSizeForTheConstantVelocityField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetMeshSizeForTheConstantVelocityField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.SetMeshSizeForTheUpdateField = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetMeshSizeForTheUpdateField, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3.GetPointer = new_instancemethod(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetPointer, None, itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3_swigregister = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_swigregister
itkBSplineExponentialDiffeomorphicTransformD3_swigregister(itkBSplineExponentialDiffeomorphicTransformD3)

def itkBSplineExponentialDiffeomorphicTransformD3___New_orig__() -> "itkBSplineExponentialDiffeomorphicTransformD3_Pointer":
    """itkBSplineExponentialDiffeomorphicTransformD3___New_orig__() -> itkBSplineExponentialDiffeomorphicTransformD3_Pointer"""
    return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3___New_orig__()

def itkBSplineExponentialDiffeomorphicTransformD3_cast(obj: 'itkLightObject') -> "itkBSplineExponentialDiffeomorphicTransformD3 *":
    """itkBSplineExponentialDiffeomorphicTransformD3_cast(itkLightObject obj) -> itkBSplineExponentialDiffeomorphicTransformD3"""
    return _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_cast(obj)



