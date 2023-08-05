# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkComplexToPhaseImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkComplexToPhaseImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkComplexToPhaseImageFilterPython')
    _itkComplexToPhaseImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkComplexToPhaseImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkComplexToPhaseImageFilterPython
            return _itkComplexToPhaseImageFilterPython
        try:
            _mod = imp.load_module('_itkComplexToPhaseImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkComplexToPhaseImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkComplexToPhaseImageFilterPython
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


import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkComplexToPhaseImageFilterICF3IF3_New():
  return itkComplexToPhaseImageFilterICF3IF3.New()


def itkComplexToPhaseImageFilterICF3IF3_Superclass_New():
  return itkComplexToPhaseImageFilterICF3IF3_Superclass.New()


def itkComplexToPhaseImageFilterICF2IF2_New():
  return itkComplexToPhaseImageFilterICF2IF2.New()


def itkComplexToPhaseImageFilterICF2IF2_Superclass_New():
  return itkComplexToPhaseImageFilterICF2IF2_Superclass.New()

class itkComplexToPhaseImageFilterICF2IF2_Superclass(itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF2IF2):
    """Proxy of C++ itkComplexToPhaseImageFilterICF2IF2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToPhaseImageFilterICF2IF2_Superclass_Pointer":
        """__New_orig__() -> itkComplexToPhaseImageFilterICF2IF2_Superclass_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToPhaseImageFilterICF2IF2_Superclass_Pointer":
        """Clone(itkComplexToPhaseImageFilterICF2IF2_Superclass self) -> itkComplexToPhaseImageFilterICF2IF2_Superclass_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_Clone(self)


    def GetFunctor(self, *args) -> "itk::Functor::ComplexToPhase< std::complex< float >,float > const &":
        """
        GetFunctor(itkComplexToPhaseImageFilterICF2IF2_Superclass self) -> itk::Functor::ComplexToPhase< std::complex< float >,float >
        GetFunctor(itkComplexToPhaseImageFilterICF2IF2_Superclass self) -> itk::Functor::ComplexToPhase< std::complex< float >,float > const &
        """
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor: 'itk::Functor::ComplexToPhase< std::complex< float >,float > const &') -> "void":
        """SetFunctor(itkComplexToPhaseImageFilterICF2IF2_Superclass self, itk::Functor::ComplexToPhase< std::complex< float >,float > const & functor)"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkComplexToPhaseImageFilterPython.delete_itkComplexToPhaseImageFilterICF2IF2_Superclass

    def cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF2IF2_Superclass *":
        """cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF2IF2_Superclass"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToPhaseImageFilterICF2IF2_Superclass *":
        """GetPointer(itkComplexToPhaseImageFilterICF2IF2_Superclass self) -> itkComplexToPhaseImageFilterICF2IF2_Superclass"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToPhaseImageFilterICF2IF2_Superclass

        Create a new object of the class itkComplexToPhaseImageFilterICF2IF2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToPhaseImageFilterICF2IF2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToPhaseImageFilterICF2IF2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToPhaseImageFilterICF2IF2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToPhaseImageFilterICF2IF2_Superclass.Clone = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_Clone, None, itkComplexToPhaseImageFilterICF2IF2_Superclass)
itkComplexToPhaseImageFilterICF2IF2_Superclass.GetFunctor = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_GetFunctor, None, itkComplexToPhaseImageFilterICF2IF2_Superclass)
itkComplexToPhaseImageFilterICF2IF2_Superclass.SetFunctor = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_SetFunctor, None, itkComplexToPhaseImageFilterICF2IF2_Superclass)
itkComplexToPhaseImageFilterICF2IF2_Superclass.GetPointer = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_GetPointer, None, itkComplexToPhaseImageFilterICF2IF2_Superclass)
itkComplexToPhaseImageFilterICF2IF2_Superclass_swigregister = _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_swigregister
itkComplexToPhaseImageFilterICF2IF2_Superclass_swigregister(itkComplexToPhaseImageFilterICF2IF2_Superclass)

def itkComplexToPhaseImageFilterICF2IF2_Superclass___New_orig__() -> "itkComplexToPhaseImageFilterICF2IF2_Superclass_Pointer":
    """itkComplexToPhaseImageFilterICF2IF2_Superclass___New_orig__() -> itkComplexToPhaseImageFilterICF2IF2_Superclass_Pointer"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass___New_orig__()

def itkComplexToPhaseImageFilterICF2IF2_Superclass_cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF2IF2_Superclass *":
    """itkComplexToPhaseImageFilterICF2IF2_Superclass_cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF2IF2_Superclass"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Superclass_cast(obj)

class itkComplexToPhaseImageFilterICF3IF3_Superclass(itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF3IF3):
    """Proxy of C++ itkComplexToPhaseImageFilterICF3IF3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToPhaseImageFilterICF3IF3_Superclass_Pointer":
        """__New_orig__() -> itkComplexToPhaseImageFilterICF3IF3_Superclass_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToPhaseImageFilterICF3IF3_Superclass_Pointer":
        """Clone(itkComplexToPhaseImageFilterICF3IF3_Superclass self) -> itkComplexToPhaseImageFilterICF3IF3_Superclass_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_Clone(self)


    def GetFunctor(self, *args) -> "itk::Functor::ComplexToPhase< std::complex< float >,float > const &":
        """
        GetFunctor(itkComplexToPhaseImageFilterICF3IF3_Superclass self) -> itk::Functor::ComplexToPhase< std::complex< float >,float >
        GetFunctor(itkComplexToPhaseImageFilterICF3IF3_Superclass self) -> itk::Functor::ComplexToPhase< std::complex< float >,float > const &
        """
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor: 'itk::Functor::ComplexToPhase< std::complex< float >,float > const &') -> "void":
        """SetFunctor(itkComplexToPhaseImageFilterICF3IF3_Superclass self, itk::Functor::ComplexToPhase< std::complex< float >,float > const & functor)"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkComplexToPhaseImageFilterPython.delete_itkComplexToPhaseImageFilterICF3IF3_Superclass

    def cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF3IF3_Superclass *":
        """cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF3IF3_Superclass"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToPhaseImageFilterICF3IF3_Superclass *":
        """GetPointer(itkComplexToPhaseImageFilterICF3IF3_Superclass self) -> itkComplexToPhaseImageFilterICF3IF3_Superclass"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToPhaseImageFilterICF3IF3_Superclass

        Create a new object of the class itkComplexToPhaseImageFilterICF3IF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToPhaseImageFilterICF3IF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToPhaseImageFilterICF3IF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToPhaseImageFilterICF3IF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToPhaseImageFilterICF3IF3_Superclass.Clone = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_Clone, None, itkComplexToPhaseImageFilterICF3IF3_Superclass)
itkComplexToPhaseImageFilterICF3IF3_Superclass.GetFunctor = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_GetFunctor, None, itkComplexToPhaseImageFilterICF3IF3_Superclass)
itkComplexToPhaseImageFilterICF3IF3_Superclass.SetFunctor = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_SetFunctor, None, itkComplexToPhaseImageFilterICF3IF3_Superclass)
itkComplexToPhaseImageFilterICF3IF3_Superclass.GetPointer = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_GetPointer, None, itkComplexToPhaseImageFilterICF3IF3_Superclass)
itkComplexToPhaseImageFilterICF3IF3_Superclass_swigregister = _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_swigregister
itkComplexToPhaseImageFilterICF3IF3_Superclass_swigregister(itkComplexToPhaseImageFilterICF3IF3_Superclass)

def itkComplexToPhaseImageFilterICF3IF3_Superclass___New_orig__() -> "itkComplexToPhaseImageFilterICF3IF3_Superclass_Pointer":
    """itkComplexToPhaseImageFilterICF3IF3_Superclass___New_orig__() -> itkComplexToPhaseImageFilterICF3IF3_Superclass_Pointer"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass___New_orig__()

def itkComplexToPhaseImageFilterICF3IF3_Superclass_cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF3IF3_Superclass *":
    """itkComplexToPhaseImageFilterICF3IF3_Superclass_cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF3IF3_Superclass"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Superclass_cast(obj)

class itkComplexToPhaseImageFilterICF2IF2(itkComplexToPhaseImageFilterICF2IF2_Superclass):
    """Proxy of C++ itkComplexToPhaseImageFilterICF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToPhaseImageFilterICF2IF2_Pointer":
        """__New_orig__() -> itkComplexToPhaseImageFilterICF2IF2_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToPhaseImageFilterICF2IF2_Pointer":
        """Clone(itkComplexToPhaseImageFilterICF2IF2 self) -> itkComplexToPhaseImageFilterICF2IF2_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Clone(self)

    InputConvertibleToOutputCheck = _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkComplexToPhaseImageFilterPython.delete_itkComplexToPhaseImageFilterICF2IF2

    def cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF2IF2 *":
        """cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF2IF2"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToPhaseImageFilterICF2IF2 *":
        """GetPointer(itkComplexToPhaseImageFilterICF2IF2 self) -> itkComplexToPhaseImageFilterICF2IF2"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToPhaseImageFilterICF2IF2

        Create a new object of the class itkComplexToPhaseImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToPhaseImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToPhaseImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToPhaseImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToPhaseImageFilterICF2IF2.Clone = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_Clone, None, itkComplexToPhaseImageFilterICF2IF2)
itkComplexToPhaseImageFilterICF2IF2.GetPointer = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_GetPointer, None, itkComplexToPhaseImageFilterICF2IF2)
itkComplexToPhaseImageFilterICF2IF2_swigregister = _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_swigregister
itkComplexToPhaseImageFilterICF2IF2_swigregister(itkComplexToPhaseImageFilterICF2IF2)

def itkComplexToPhaseImageFilterICF2IF2___New_orig__() -> "itkComplexToPhaseImageFilterICF2IF2_Pointer":
    """itkComplexToPhaseImageFilterICF2IF2___New_orig__() -> itkComplexToPhaseImageFilterICF2IF2_Pointer"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2___New_orig__()

def itkComplexToPhaseImageFilterICF2IF2_cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF2IF2 *":
    """itkComplexToPhaseImageFilterICF2IF2_cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF2IF2"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF2IF2_cast(obj)

class itkComplexToPhaseImageFilterICF3IF3(itkComplexToPhaseImageFilterICF3IF3_Superclass):
    """Proxy of C++ itkComplexToPhaseImageFilterICF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToPhaseImageFilterICF3IF3_Pointer":
        """__New_orig__() -> itkComplexToPhaseImageFilterICF3IF3_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToPhaseImageFilterICF3IF3_Pointer":
        """Clone(itkComplexToPhaseImageFilterICF3IF3 self) -> itkComplexToPhaseImageFilterICF3IF3_Pointer"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Clone(self)

    InputConvertibleToOutputCheck = _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkComplexToPhaseImageFilterPython.delete_itkComplexToPhaseImageFilterICF3IF3

    def cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF3IF3 *":
        """cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF3IF3"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToPhaseImageFilterICF3IF3 *":
        """GetPointer(itkComplexToPhaseImageFilterICF3IF3 self) -> itkComplexToPhaseImageFilterICF3IF3"""
        return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToPhaseImageFilterICF3IF3

        Create a new object of the class itkComplexToPhaseImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToPhaseImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToPhaseImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToPhaseImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToPhaseImageFilterICF3IF3.Clone = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_Clone, None, itkComplexToPhaseImageFilterICF3IF3)
itkComplexToPhaseImageFilterICF3IF3.GetPointer = new_instancemethod(_itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_GetPointer, None, itkComplexToPhaseImageFilterICF3IF3)
itkComplexToPhaseImageFilterICF3IF3_swigregister = _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_swigregister
itkComplexToPhaseImageFilterICF3IF3_swigregister(itkComplexToPhaseImageFilterICF3IF3)

def itkComplexToPhaseImageFilterICF3IF3___New_orig__() -> "itkComplexToPhaseImageFilterICF3IF3_Pointer":
    """itkComplexToPhaseImageFilterICF3IF3___New_orig__() -> itkComplexToPhaseImageFilterICF3IF3_Pointer"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3___New_orig__()

def itkComplexToPhaseImageFilterICF3IF3_cast(obj: 'itkLightObject') -> "itkComplexToPhaseImageFilterICF3IF3 *":
    """itkComplexToPhaseImageFilterICF3IF3_cast(itkLightObject obj) -> itkComplexToPhaseImageFilterICF3IF3"""
    return _itkComplexToPhaseImageFilterPython.itkComplexToPhaseImageFilterICF3IF3_cast(obj)



