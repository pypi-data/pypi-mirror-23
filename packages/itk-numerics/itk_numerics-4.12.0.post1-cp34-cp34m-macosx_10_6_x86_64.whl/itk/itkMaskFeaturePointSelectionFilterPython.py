# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMaskFeaturePointSelectionFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMaskFeaturePointSelectionFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMaskFeaturePointSelectionFilterPython')
    _itkMaskFeaturePointSelectionFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMaskFeaturePointSelectionFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMaskFeaturePointSelectionFilterPython
            return _itkMaskFeaturePointSelectionFilterPython
        try:
            _mod = imp.load_module('_itkMaskFeaturePointSelectionFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMaskFeaturePointSelectionFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMaskFeaturePointSelectionFilterPython
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
import itkPointSetPython
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython

def itkMaskFeaturePointSelectionFilterIF3_New():
  return itkMaskFeaturePointSelectionFilterIF3.New()


def itkMaskFeaturePointSelectionFilterIF3_Superclass_New():
  return itkMaskFeaturePointSelectionFilterIF3_Superclass.New()


def itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_New():
  return itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New()

class itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Pointer":
        """__New_orig__() -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Pointer"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Pointer":
        """Clone(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self) -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Pointer"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Clone(self)


    def GetOutput(self, *args) -> "itkPointSetMD33STMD3333FFMD33 *":
        """
        GetOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self) -> itkPointSetMD33STMD3333FFMD33
        GetOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self, unsigned int idx) -> itkPointSetMD33STMD3333FFMD33
        """
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GetOutput(self, *args)


    def SetOutput(self, output: 'itkPointSetMD33STMD3333FFMD33') -> "void":
        """SetOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self, itkPointSetMD33STMD3333FFMD33 output)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_SetOutput(self, output)


    def GraftOutput(self, *args) -> "void":
        """
        GraftOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self, itkDataObject output)
        GraftOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self, std::string const & key, itkDataObject output)
        """
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftOutput(self, *args)


    def GraftNthOutput(self, idx: 'unsigned int', output: 'itkDataObject') -> "void":
        """GraftNthOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self, unsigned int idx, itkDataObject output)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftNthOutput(self, idx, output)

    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass

    def cast(obj: 'itkLightObject') -> "itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass *":
        """cast(itkLightObject obj) -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass *":
        """GetPointer(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass self) -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.Clone = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Clone, None, itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.GetOutput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GetOutput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.SetOutput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_SetOutput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.GraftOutput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftOutput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.GraftNthOutput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftNthOutput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.GetPointer = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GetPointer, None, itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_swigregister = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_swigregister
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_swigregister(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)

def itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__() -> "itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Pointer":
    """itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__() -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Pointer"""
    return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__()

def itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast(obj: 'itkLightObject') -> "itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass *":
    """itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast(itkLightObject obj) -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass"""
    return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast(obj)

class itkMaskFeaturePointSelectionFilterIF3_Superclass(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass):
    """Proxy of C++ itkMaskFeaturePointSelectionFilterIF3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkMaskFeaturePointSelectionFilterIF3_Superclass self, unsigned int idx, itkImageF3 input)
        SetInput(itkMaskFeaturePointSelectionFilterIF3_Superclass self, itkImageF3 input)
        """
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageF3 const *":
        """
        GetInput(itkMaskFeaturePointSelectionFilterIF3_Superclass self, unsigned int idx) -> itkImageF3
        GetInput(itkMaskFeaturePointSelectionFilterIF3_Superclass self) -> itkImageF3
        """
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetInput(self, *args)


    def GetOutput(self) -> "itkPointSetMD33STMD3333FFMD33 *":
        """GetOutput(itkMaskFeaturePointSelectionFilterIF3_Superclass self) -> itkPointSetMD33STMD3333FFMD33"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetOutput(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkMaskFeaturePointSelectionFilterIF3_Superclass self)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GenerateOutputInformation(self)

    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3_Superclass

    def cast(obj: 'itkLightObject') -> "itkMaskFeaturePointSelectionFilterIF3_Superclass *":
        """cast(itkLightObject obj) -> itkMaskFeaturePointSelectionFilterIF3_Superclass"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMaskFeaturePointSelectionFilterIF3_Superclass *":
        """GetPointer(itkMaskFeaturePointSelectionFilterIF3_Superclass self) -> itkMaskFeaturePointSelectionFilterIF3_Superclass"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterIF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMaskFeaturePointSelectionFilterIF3_Superclass.SetInput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_SetInput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass.GetInput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetInput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass.GetOutput = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetOutput, None, itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass.GenerateOutputInformation = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GenerateOutputInformation, None, itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass.GetPointer = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetPointer, None, itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_swigregister = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_swigregister
itkMaskFeaturePointSelectionFilterIF3_Superclass_swigregister(itkMaskFeaturePointSelectionFilterIF3_Superclass)

def itkMaskFeaturePointSelectionFilterIF3_Superclass_cast(obj: 'itkLightObject') -> "itkMaskFeaturePointSelectionFilterIF3_Superclass *":
    """itkMaskFeaturePointSelectionFilterIF3_Superclass_cast(itkLightObject obj) -> itkMaskFeaturePointSelectionFilterIF3_Superclass"""
    return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_cast(obj)

class itkMaskFeaturePointSelectionFilterIF3(itkMaskFeaturePointSelectionFilterIF3_Superclass):
    """Proxy of C++ itkMaskFeaturePointSelectionFilterIF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMaskFeaturePointSelectionFilterIF3_Pointer":
        """__New_orig__() -> itkMaskFeaturePointSelectionFilterIF3_Pointer"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMaskFeaturePointSelectionFilterIF3_Pointer":
        """Clone(itkMaskFeaturePointSelectionFilterIF3 self) -> itkMaskFeaturePointSelectionFilterIF3_Pointer"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Clone(self)

    VERTEX_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_VERTEX_CONNECTIVITY
    EDGE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_EDGE_CONNECTIVITY
    FACE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_FACE_CONNECTIVITY

    def SetNonConnectivity(self, _arg: 'unsigned int const') -> "void":
        """SetNonConnectivity(itkMaskFeaturePointSelectionFilterIF3 self, unsigned int const _arg)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetNonConnectivity(self, _arg)


    def GetNonConnectivity(self) -> "unsigned int":
        """GetNonConnectivity(itkMaskFeaturePointSelectionFilterIF3 self) -> unsigned int"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetNonConnectivity(self)


    def SetMaskImage(self, _arg: 'itkImageF3') -> "void":
        """SetMaskImage(itkMaskFeaturePointSelectionFilterIF3 self, itkImageF3 _arg)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetMaskImage(self, _arg)


    def GetMaskImage(self) -> "itkImageF3 const *":
        """GetMaskImage(itkMaskFeaturePointSelectionFilterIF3 self) -> itkImageF3"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetMaskImage(self)


    def SetBlockRadius(self, _arg: 'itkSize3') -> "void":
        """SetBlockRadius(itkMaskFeaturePointSelectionFilterIF3 self, itkSize3 _arg)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetBlockRadius(self, _arg)


    def GetBlockRadius(self) -> "itkSize3 const &":
        """GetBlockRadius(itkMaskFeaturePointSelectionFilterIF3 self) -> itkSize3"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetBlockRadius(self)


    def SetComputeStructureTensors(self, _arg: 'bool const') -> "void":
        """SetComputeStructureTensors(itkMaskFeaturePointSelectionFilterIF3 self, bool const _arg)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetComputeStructureTensors(self, _arg)


    def GetComputeStructureTensors(self) -> "bool":
        """GetComputeStructureTensors(itkMaskFeaturePointSelectionFilterIF3 self) -> bool"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetComputeStructureTensors(self)


    def ComputeStructureTensorsOn(self) -> "void":
        """ComputeStructureTensorsOn(itkMaskFeaturePointSelectionFilterIF3 self)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOn(self)


    def ComputeStructureTensorsOff(self) -> "void":
        """ComputeStructureTensorsOff(itkMaskFeaturePointSelectionFilterIF3 self)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOff(self)


    def SetSelectFraction(self, _arg: 'double') -> "void":
        """SetSelectFraction(itkMaskFeaturePointSelectionFilterIF3 self, double _arg)"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetSelectFraction(self, _arg)


    def GetSelectFraction(self) -> "double":
        """GetSelectFraction(itkMaskFeaturePointSelectionFilterIF3 self) -> double"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetSelectFraction(self)

    ImageDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ImageDimensionShouldBe3
    MaskDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_MaskDimensionShouldBe3
    PointDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_PointDimensionShouldBe3
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3

    def cast(obj: 'itkLightObject') -> "itkMaskFeaturePointSelectionFilterIF3 *":
        """cast(itkLightObject obj) -> itkMaskFeaturePointSelectionFilterIF3"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMaskFeaturePointSelectionFilterIF3 *":
        """GetPointer(itkMaskFeaturePointSelectionFilterIF3 self) -> itkMaskFeaturePointSelectionFilterIF3"""
        return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMaskFeaturePointSelectionFilterIF3.Clone = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Clone, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.SetNonConnectivity = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetNonConnectivity, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.GetNonConnectivity = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetNonConnectivity, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.SetMaskImage = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetMaskImage, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.GetMaskImage = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetMaskImage, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.SetBlockRadius = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetBlockRadius, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.GetBlockRadius = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetBlockRadius, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.SetComputeStructureTensors = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetComputeStructureTensors, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.GetComputeStructureTensors = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetComputeStructureTensors, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.ComputeStructureTensorsOn = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOn, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.ComputeStructureTensorsOff = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOff, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.SetSelectFraction = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetSelectFraction, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.GetSelectFraction = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetSelectFraction, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3.GetPointer = new_instancemethod(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetPointer, None, itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3_swigregister = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_swigregister
itkMaskFeaturePointSelectionFilterIF3_swigregister(itkMaskFeaturePointSelectionFilterIF3)

def itkMaskFeaturePointSelectionFilterIF3___New_orig__() -> "itkMaskFeaturePointSelectionFilterIF3_Pointer":
    """itkMaskFeaturePointSelectionFilterIF3___New_orig__() -> itkMaskFeaturePointSelectionFilterIF3_Pointer"""
    return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3___New_orig__()

def itkMaskFeaturePointSelectionFilterIF3_cast(obj: 'itkLightObject') -> "itkMaskFeaturePointSelectionFilterIF3 *":
    """itkMaskFeaturePointSelectionFilterIF3_cast(itkLightObject obj) -> itkMaskFeaturePointSelectionFilterIF3"""
    return _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_cast(obj)



