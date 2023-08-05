# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkComplexToImaginaryImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkComplexToImaginaryImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkComplexToImaginaryImageFilterPython')
    _itkComplexToImaginaryImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkComplexToImaginaryImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkComplexToImaginaryImageFilterPython
            return _itkComplexToImaginaryImageFilterPython
        try:
            _mod = imp.load_module('_itkComplexToImaginaryImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkComplexToImaginaryImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkComplexToImaginaryImageFilterPython
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
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkComplexToImaginaryImageFilterICF3IF3_New():
  return itkComplexToImaginaryImageFilterICF3IF3.New()


def itkComplexToImaginaryImageFilterICF3IF3_Superclass_New():
  return itkComplexToImaginaryImageFilterICF3IF3_Superclass.New()


def itkComplexToImaginaryImageFilterICF2IF2_New():
  return itkComplexToImaginaryImageFilterICF2IF2.New()


def itkComplexToImaginaryImageFilterICF2IF2_Superclass_New():
  return itkComplexToImaginaryImageFilterICF2IF2_Superclass.New()

class itkComplexToImaginaryImageFilterICF2IF2_Superclass(itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF2IF2):
    """Proxy of C++ itkComplexToImaginaryImageFilterICF2IF2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToImaginaryImageFilterICF2IF2_Superclass_Pointer":
        """__New_orig__() -> itkComplexToImaginaryImageFilterICF2IF2_Superclass_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToImaginaryImageFilterICF2IF2_Superclass_Pointer":
        """Clone(itkComplexToImaginaryImageFilterICF2IF2_Superclass self) -> itkComplexToImaginaryImageFilterICF2IF2_Superclass_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_Clone(self)


    def GetFunctor(self, *args) -> "itk::Functor::ComplexToImaginary< std::complex< float >,float > const &":
        """
        GetFunctor(itkComplexToImaginaryImageFilterICF2IF2_Superclass self) -> itk::Functor::ComplexToImaginary< std::complex< float >,float >
        GetFunctor(itkComplexToImaginaryImageFilterICF2IF2_Superclass self) -> itk::Functor::ComplexToImaginary< std::complex< float >,float > const &
        """
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor: 'itk::Functor::ComplexToImaginary< std::complex< float >,float > const &') -> "void":
        """SetFunctor(itkComplexToImaginaryImageFilterICF2IF2_Superclass self, itk::Functor::ComplexToImaginary< std::complex< float >,float > const & functor)"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF2IF2_Superclass

    def cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF2IF2_Superclass *":
        """cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF2IF2_Superclass"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToImaginaryImageFilterICF2IF2_Superclass *":
        """GetPointer(itkComplexToImaginaryImageFilterICF2IF2_Superclass self) -> itkComplexToImaginaryImageFilterICF2IF2_Superclass"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF2IF2_Superclass

        Create a new object of the class itkComplexToImaginaryImageFilterICF2IF2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF2IF2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF2IF2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToImaginaryImageFilterICF2IF2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToImaginaryImageFilterICF2IF2_Superclass.Clone = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_Clone, None, itkComplexToImaginaryImageFilterICF2IF2_Superclass)
itkComplexToImaginaryImageFilterICF2IF2_Superclass.GetFunctor = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_GetFunctor, None, itkComplexToImaginaryImageFilterICF2IF2_Superclass)
itkComplexToImaginaryImageFilterICF2IF2_Superclass.SetFunctor = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_SetFunctor, None, itkComplexToImaginaryImageFilterICF2IF2_Superclass)
itkComplexToImaginaryImageFilterICF2IF2_Superclass.GetPointer = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_GetPointer, None, itkComplexToImaginaryImageFilterICF2IF2_Superclass)
itkComplexToImaginaryImageFilterICF2IF2_Superclass_swigregister = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_swigregister
itkComplexToImaginaryImageFilterICF2IF2_Superclass_swigregister(itkComplexToImaginaryImageFilterICF2IF2_Superclass)

def itkComplexToImaginaryImageFilterICF2IF2_Superclass___New_orig__() -> "itkComplexToImaginaryImageFilterICF2IF2_Superclass_Pointer":
    """itkComplexToImaginaryImageFilterICF2IF2_Superclass___New_orig__() -> itkComplexToImaginaryImageFilterICF2IF2_Superclass_Pointer"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass___New_orig__()

def itkComplexToImaginaryImageFilterICF2IF2_Superclass_cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF2IF2_Superclass *":
    """itkComplexToImaginaryImageFilterICF2IF2_Superclass_cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF2IF2_Superclass"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Superclass_cast(obj)

class itkComplexToImaginaryImageFilterICF3IF3_Superclass(itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF3IF3):
    """Proxy of C++ itkComplexToImaginaryImageFilterICF3IF3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToImaginaryImageFilterICF3IF3_Superclass_Pointer":
        """__New_orig__() -> itkComplexToImaginaryImageFilterICF3IF3_Superclass_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToImaginaryImageFilterICF3IF3_Superclass_Pointer":
        """Clone(itkComplexToImaginaryImageFilterICF3IF3_Superclass self) -> itkComplexToImaginaryImageFilterICF3IF3_Superclass_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_Clone(self)


    def GetFunctor(self, *args) -> "itk::Functor::ComplexToImaginary< std::complex< float >,float > const &":
        """
        GetFunctor(itkComplexToImaginaryImageFilterICF3IF3_Superclass self) -> itk::Functor::ComplexToImaginary< std::complex< float >,float >
        GetFunctor(itkComplexToImaginaryImageFilterICF3IF3_Superclass self) -> itk::Functor::ComplexToImaginary< std::complex< float >,float > const &
        """
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor: 'itk::Functor::ComplexToImaginary< std::complex< float >,float > const &') -> "void":
        """SetFunctor(itkComplexToImaginaryImageFilterICF3IF3_Superclass self, itk::Functor::ComplexToImaginary< std::complex< float >,float > const & functor)"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF3IF3_Superclass

    def cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF3IF3_Superclass *":
        """cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF3IF3_Superclass"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToImaginaryImageFilterICF3IF3_Superclass *":
        """GetPointer(itkComplexToImaginaryImageFilterICF3IF3_Superclass self) -> itkComplexToImaginaryImageFilterICF3IF3_Superclass"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF3IF3_Superclass

        Create a new object of the class itkComplexToImaginaryImageFilterICF3IF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF3IF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF3IF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToImaginaryImageFilterICF3IF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToImaginaryImageFilterICF3IF3_Superclass.Clone = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_Clone, None, itkComplexToImaginaryImageFilterICF3IF3_Superclass)
itkComplexToImaginaryImageFilterICF3IF3_Superclass.GetFunctor = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_GetFunctor, None, itkComplexToImaginaryImageFilterICF3IF3_Superclass)
itkComplexToImaginaryImageFilterICF3IF3_Superclass.SetFunctor = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_SetFunctor, None, itkComplexToImaginaryImageFilterICF3IF3_Superclass)
itkComplexToImaginaryImageFilterICF3IF3_Superclass.GetPointer = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_GetPointer, None, itkComplexToImaginaryImageFilterICF3IF3_Superclass)
itkComplexToImaginaryImageFilterICF3IF3_Superclass_swigregister = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_swigregister
itkComplexToImaginaryImageFilterICF3IF3_Superclass_swigregister(itkComplexToImaginaryImageFilterICF3IF3_Superclass)

def itkComplexToImaginaryImageFilterICF3IF3_Superclass___New_orig__() -> "itkComplexToImaginaryImageFilterICF3IF3_Superclass_Pointer":
    """itkComplexToImaginaryImageFilterICF3IF3_Superclass___New_orig__() -> itkComplexToImaginaryImageFilterICF3IF3_Superclass_Pointer"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass___New_orig__()

def itkComplexToImaginaryImageFilterICF3IF3_Superclass_cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF3IF3_Superclass *":
    """itkComplexToImaginaryImageFilterICF3IF3_Superclass_cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF3IF3_Superclass"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Superclass_cast(obj)

class itkComplexToImaginaryImageFilterICF2IF2(itkComplexToImaginaryImageFilterICF2IF2_Superclass):
    """Proxy of C++ itkComplexToImaginaryImageFilterICF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToImaginaryImageFilterICF2IF2_Pointer":
        """__New_orig__() -> itkComplexToImaginaryImageFilterICF2IF2_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToImaginaryImageFilterICF2IF2_Pointer":
        """Clone(itkComplexToImaginaryImageFilterICF2IF2 self) -> itkComplexToImaginaryImageFilterICF2IF2_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Clone(self)

    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF2IF2

    def cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF2IF2 *":
        """cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF2IF2"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToImaginaryImageFilterICF2IF2 *":
        """GetPointer(itkComplexToImaginaryImageFilterICF2IF2 self) -> itkComplexToImaginaryImageFilterICF2IF2"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF2IF2

        Create a new object of the class itkComplexToImaginaryImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToImaginaryImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToImaginaryImageFilterICF2IF2.Clone = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Clone, None, itkComplexToImaginaryImageFilterICF2IF2)
itkComplexToImaginaryImageFilterICF2IF2.GetPointer = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_GetPointer, None, itkComplexToImaginaryImageFilterICF2IF2)
itkComplexToImaginaryImageFilterICF2IF2_swigregister = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_swigregister
itkComplexToImaginaryImageFilterICF2IF2_swigregister(itkComplexToImaginaryImageFilterICF2IF2)

def itkComplexToImaginaryImageFilterICF2IF2___New_orig__() -> "itkComplexToImaginaryImageFilterICF2IF2_Pointer":
    """itkComplexToImaginaryImageFilterICF2IF2___New_orig__() -> itkComplexToImaginaryImageFilterICF2IF2_Pointer"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2___New_orig__()

def itkComplexToImaginaryImageFilterICF2IF2_cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF2IF2 *":
    """itkComplexToImaginaryImageFilterICF2IF2_cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF2IF2"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_cast(obj)

class itkComplexToImaginaryImageFilterICF3IF3(itkComplexToImaginaryImageFilterICF3IF3_Superclass):
    """Proxy of C++ itkComplexToImaginaryImageFilterICF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToImaginaryImageFilterICF3IF3_Pointer":
        """__New_orig__() -> itkComplexToImaginaryImageFilterICF3IF3_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToImaginaryImageFilterICF3IF3_Pointer":
        """Clone(itkComplexToImaginaryImageFilterICF3IF3 self) -> itkComplexToImaginaryImageFilterICF3IF3_Pointer"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Clone(self)

    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF3IF3

    def cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF3IF3 *":
        """cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF3IF3"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkComplexToImaginaryImageFilterICF3IF3 *":
        """GetPointer(itkComplexToImaginaryImageFilterICF3IF3 self) -> itkComplexToImaginaryImageFilterICF3IF3"""
        return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF3IF3

        Create a new object of the class itkComplexToImaginaryImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToImaginaryImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToImaginaryImageFilterICF3IF3.Clone = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Clone, None, itkComplexToImaginaryImageFilterICF3IF3)
itkComplexToImaginaryImageFilterICF3IF3.GetPointer = new_instancemethod(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_GetPointer, None, itkComplexToImaginaryImageFilterICF3IF3)
itkComplexToImaginaryImageFilterICF3IF3_swigregister = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_swigregister
itkComplexToImaginaryImageFilterICF3IF3_swigregister(itkComplexToImaginaryImageFilterICF3IF3)

def itkComplexToImaginaryImageFilterICF3IF3___New_orig__() -> "itkComplexToImaginaryImageFilterICF3IF3_Pointer":
    """itkComplexToImaginaryImageFilterICF3IF3___New_orig__() -> itkComplexToImaginaryImageFilterICF3IF3_Pointer"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3___New_orig__()

def itkComplexToImaginaryImageFilterICF3IF3_cast(obj: 'itkLightObject') -> "itkComplexToImaginaryImageFilterICF3IF3 *":
    """itkComplexToImaginaryImageFilterICF3IF3_cast(itkLightObject obj) -> itkComplexToImaginaryImageFilterICF3IF3"""
    return _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_cast(obj)



