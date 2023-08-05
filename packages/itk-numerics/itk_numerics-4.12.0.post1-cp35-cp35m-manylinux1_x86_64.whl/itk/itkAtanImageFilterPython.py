# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAtanImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkAtanImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkAtanImageFilterPython')
    _itkAtanImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAtanImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAtanImageFilterPython
            return _itkAtanImageFilterPython
        try:
            _mod = imp.load_module('_itkAtanImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkAtanImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAtanImageFilterPython
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
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import stdcomplexPython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkAtanImageFilterIF3IF3_New():
  return itkAtanImageFilterIF3IF3.New()


def itkAtanImageFilterIF3IF3_Superclass_New():
  return itkAtanImageFilterIF3IF3_Superclass.New()


def itkAtanImageFilterIF2IF2_New():
  return itkAtanImageFilterIF2IF2.New()


def itkAtanImageFilterIF2IF2_Superclass_New():
  return itkAtanImageFilterIF2IF2_Superclass.New()

class itkAtanImageFilterIF2IF2_Superclass(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF2IF2):
    """Proxy of C++ itkAtanImageFilterIF2IF2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterIF2IF2_Superclass_Pointer":
        """__New_orig__() -> itkAtanImageFilterIF2IF2_Superclass_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterIF2IF2_Superclass_Pointer":
        """Clone(itkAtanImageFilterIF2IF2_Superclass self) -> itkAtanImageFilterIF2IF2_Superclass_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_Clone(self)


    def GetFunctor(self, *args) -> "itk::Functor::Atan< float,float > const &":
        """
        GetFunctor(itkAtanImageFilterIF2IF2_Superclass self) -> itk::Functor::Atan< float,float >
        GetFunctor(itkAtanImageFilterIF2IF2_Superclass self) -> itk::Functor::Atan< float,float > const &
        """
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor: 'itk::Functor::Atan< float,float > const &') -> "void":
        """SetFunctor(itkAtanImageFilterIF2IF2_Superclass self, itk::Functor::Atan< float,float > const & functor)"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterIF2IF2_Superclass

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF2IF2_Superclass *":
        """cast(itkLightObject obj) -> itkAtanImageFilterIF2IF2_Superclass"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAtanImageFilterIF2IF2_Superclass *":
        """GetPointer(itkAtanImageFilterIF2IF2_Superclass self) -> itkAtanImageFilterIF2IF2_Superclass"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAtanImageFilterIF2IF2_Superclass

        Create a new object of the class itkAtanImageFilterIF2IF2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterIF2IF2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterIF2IF2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterIF2IF2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterIF2IF2_Superclass.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_Clone, None, itkAtanImageFilterIF2IF2_Superclass)
itkAtanImageFilterIF2IF2_Superclass.GetFunctor = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_GetFunctor, None, itkAtanImageFilterIF2IF2_Superclass)
itkAtanImageFilterIF2IF2_Superclass.SetFunctor = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_SetFunctor, None, itkAtanImageFilterIF2IF2_Superclass)
itkAtanImageFilterIF2IF2_Superclass.GetPointer = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_GetPointer, None, itkAtanImageFilterIF2IF2_Superclass)
itkAtanImageFilterIF2IF2_Superclass_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_swigregister
itkAtanImageFilterIF2IF2_Superclass_swigregister(itkAtanImageFilterIF2IF2_Superclass)

def itkAtanImageFilterIF2IF2_Superclass___New_orig__() -> "itkAtanImageFilterIF2IF2_Superclass_Pointer":
    """itkAtanImageFilterIF2IF2_Superclass___New_orig__() -> itkAtanImageFilterIF2IF2_Superclass_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass___New_orig__()

def itkAtanImageFilterIF2IF2_Superclass_cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF2IF2_Superclass *":
    """itkAtanImageFilterIF2IF2_Superclass_cast(itkLightObject obj) -> itkAtanImageFilterIF2IF2_Superclass"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Superclass_cast(obj)

class itkAtanImageFilterIF3IF3_Superclass(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF3IF3):
    """Proxy of C++ itkAtanImageFilterIF3IF3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterIF3IF3_Superclass_Pointer":
        """__New_orig__() -> itkAtanImageFilterIF3IF3_Superclass_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterIF3IF3_Superclass_Pointer":
        """Clone(itkAtanImageFilterIF3IF3_Superclass self) -> itkAtanImageFilterIF3IF3_Superclass_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_Clone(self)


    def GetFunctor(self, *args) -> "itk::Functor::Atan< float,float > const &":
        """
        GetFunctor(itkAtanImageFilterIF3IF3_Superclass self) -> itk::Functor::Atan< float,float >
        GetFunctor(itkAtanImageFilterIF3IF3_Superclass self) -> itk::Functor::Atan< float,float > const &
        """
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor: 'itk::Functor::Atan< float,float > const &') -> "void":
        """SetFunctor(itkAtanImageFilterIF3IF3_Superclass self, itk::Functor::Atan< float,float > const & functor)"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterIF3IF3_Superclass

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF3IF3_Superclass *":
        """cast(itkLightObject obj) -> itkAtanImageFilterIF3IF3_Superclass"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAtanImageFilterIF3IF3_Superclass *":
        """GetPointer(itkAtanImageFilterIF3IF3_Superclass self) -> itkAtanImageFilterIF3IF3_Superclass"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAtanImageFilterIF3IF3_Superclass

        Create a new object of the class itkAtanImageFilterIF3IF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterIF3IF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterIF3IF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterIF3IF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterIF3IF3_Superclass.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_Clone, None, itkAtanImageFilterIF3IF3_Superclass)
itkAtanImageFilterIF3IF3_Superclass.GetFunctor = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_GetFunctor, None, itkAtanImageFilterIF3IF3_Superclass)
itkAtanImageFilterIF3IF3_Superclass.SetFunctor = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_SetFunctor, None, itkAtanImageFilterIF3IF3_Superclass)
itkAtanImageFilterIF3IF3_Superclass.GetPointer = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_GetPointer, None, itkAtanImageFilterIF3IF3_Superclass)
itkAtanImageFilterIF3IF3_Superclass_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_swigregister
itkAtanImageFilterIF3IF3_Superclass_swigregister(itkAtanImageFilterIF3IF3_Superclass)

def itkAtanImageFilterIF3IF3_Superclass___New_orig__() -> "itkAtanImageFilterIF3IF3_Superclass_Pointer":
    """itkAtanImageFilterIF3IF3_Superclass___New_orig__() -> itkAtanImageFilterIF3IF3_Superclass_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass___New_orig__()

def itkAtanImageFilterIF3IF3_Superclass_cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF3IF3_Superclass *":
    """itkAtanImageFilterIF3IF3_Superclass_cast(itkLightObject obj) -> itkAtanImageFilterIF3IF3_Superclass"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Superclass_cast(obj)

class itkAtanImageFilterIF2IF2(itkAtanImageFilterIF2IF2_Superclass):
    """Proxy of C++ itkAtanImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkAtanImageFilterIF2IF2_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterIF2IF2_Pointer":
        """Clone(itkAtanImageFilterIF2IF2 self) -> itkAtanImageFilterIF2IF2_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkAtanImageFilterIF2IF2"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAtanImageFilterIF2IF2 *":
        """GetPointer(itkAtanImageFilterIF2IF2 self) -> itkAtanImageFilterIF2IF2"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAtanImageFilterIF2IF2

        Create a new object of the class itkAtanImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterIF2IF2.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Clone, None, itkAtanImageFilterIF2IF2)
itkAtanImageFilterIF2IF2.GetPointer = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_GetPointer, None, itkAtanImageFilterIF2IF2)
itkAtanImageFilterIF2IF2_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_swigregister
itkAtanImageFilterIF2IF2_swigregister(itkAtanImageFilterIF2IF2)

def itkAtanImageFilterIF2IF2___New_orig__() -> "itkAtanImageFilterIF2IF2_Pointer":
    """itkAtanImageFilterIF2IF2___New_orig__() -> itkAtanImageFilterIF2IF2_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2___New_orig__()

def itkAtanImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF2IF2 *":
    """itkAtanImageFilterIF2IF2_cast(itkLightObject obj) -> itkAtanImageFilterIF2IF2"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_cast(obj)

class itkAtanImageFilterIF3IF3(itkAtanImageFilterIF3IF3_Superclass):
    """Proxy of C++ itkAtanImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkAtanImageFilterIF3IF3_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterIF3IF3_Pointer":
        """Clone(itkAtanImageFilterIF3IF3 self) -> itkAtanImageFilterIF3IF3_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkAtanImageFilterIF3IF3"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAtanImageFilterIF3IF3 *":
        """GetPointer(itkAtanImageFilterIF3IF3 self) -> itkAtanImageFilterIF3IF3"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAtanImageFilterIF3IF3

        Create a new object of the class itkAtanImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterIF3IF3.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Clone, None, itkAtanImageFilterIF3IF3)
itkAtanImageFilterIF3IF3.GetPointer = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_GetPointer, None, itkAtanImageFilterIF3IF3)
itkAtanImageFilterIF3IF3_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_swigregister
itkAtanImageFilterIF3IF3_swigregister(itkAtanImageFilterIF3IF3)

def itkAtanImageFilterIF3IF3___New_orig__() -> "itkAtanImageFilterIF3IF3_Pointer":
    """itkAtanImageFilterIF3IF3___New_orig__() -> itkAtanImageFilterIF3IF3_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3___New_orig__()

def itkAtanImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF3IF3 *":
    """itkAtanImageFilterIF3IF3_cast(itkLightObject obj) -> itkAtanImageFilterIF3IF3"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_cast(obj)



