# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSinImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSinImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSinImageFilterPython')
    _itkSinImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSinImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSinImageFilterPython
            return _itkSinImageFilterPython
        try:
            _mod = imp.load_module('_itkSinImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSinImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSinImageFilterPython
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
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImagePython
import stdcomplexPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkSinImageFilterIF3IF3_New():
  return itkSinImageFilterIF3IF3.New()


def itkSinImageFilterIF3IF3_Superclass_New():
  return itkSinImageFilterIF3IF3_Superclass.New()


def itkSinImageFilterIF2IF2_New():
  return itkSinImageFilterIF2IF2.New()


def itkSinImageFilterIF2IF2_Superclass_New():
  return itkSinImageFilterIF2IF2_Superclass.New()

class itkSinImageFilterIF2IF2_Superclass(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF2IF2):
    """Proxy of C++ itkSinImageFilterIF2IF2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkSinImageFilterIF2IF2_Superclass_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkSinImageFilterIF2IF2_Superclass self) -> itkSinImageFilterIF2IF2_Superclass_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_Clone(self)


    def GetFunctor(self, *args):
        """
        GetFunctor(itkSinImageFilterIF2IF2_Superclass self) -> itk::Functor::Sin< float,float >
        GetFunctor(itkSinImageFilterIF2IF2_Superclass self) -> itk::Functor::Sin< float,float > const &
        """
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor):
        """SetFunctor(itkSinImageFilterIF2IF2_Superclass self, itk::Functor::Sin< float,float > const & functor)"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF2IF2_Superclass

    def cast(obj):
        """cast(itkLightObject obj) -> itkSinImageFilterIF2IF2_Superclass"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkSinImageFilterIF2IF2_Superclass self) -> itkSinImageFilterIF2IF2_Superclass"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSinImageFilterIF2IF2_Superclass

        Create a new object of the class itkSinImageFilterIF2IF2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterIF2IF2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterIF2IF2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterIF2IF2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterIF2IF2_Superclass.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_Clone, None, itkSinImageFilterIF2IF2_Superclass)
itkSinImageFilterIF2IF2_Superclass.GetFunctor = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_GetFunctor, None, itkSinImageFilterIF2IF2_Superclass)
itkSinImageFilterIF2IF2_Superclass.SetFunctor = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_SetFunctor, None, itkSinImageFilterIF2IF2_Superclass)
itkSinImageFilterIF2IF2_Superclass.GetPointer = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_GetPointer, None, itkSinImageFilterIF2IF2_Superclass)
itkSinImageFilterIF2IF2_Superclass_swigregister = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_swigregister
itkSinImageFilterIF2IF2_Superclass_swigregister(itkSinImageFilterIF2IF2_Superclass)

def itkSinImageFilterIF2IF2_Superclass___New_orig__():
    """itkSinImageFilterIF2IF2_Superclass___New_orig__() -> itkSinImageFilterIF2IF2_Superclass_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass___New_orig__()

def itkSinImageFilterIF2IF2_Superclass_cast(obj):
    """itkSinImageFilterIF2IF2_Superclass_cast(itkLightObject obj) -> itkSinImageFilterIF2IF2_Superclass"""
    return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Superclass_cast(obj)

class itkSinImageFilterIF3IF3_Superclass(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF3IF3):
    """Proxy of C++ itkSinImageFilterIF3IF3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkSinImageFilterIF3IF3_Superclass_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkSinImageFilterIF3IF3_Superclass self) -> itkSinImageFilterIF3IF3_Superclass_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_Clone(self)


    def GetFunctor(self, *args):
        """
        GetFunctor(itkSinImageFilterIF3IF3_Superclass self) -> itk::Functor::Sin< float,float >
        GetFunctor(itkSinImageFilterIF3IF3_Superclass self) -> itk::Functor::Sin< float,float > const &
        """
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_GetFunctor(self, *args)


    def SetFunctor(self, functor):
        """SetFunctor(itkSinImageFilterIF3IF3_Superclass self, itk::Functor::Sin< float,float > const & functor)"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_SetFunctor(self, functor)

    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF3IF3_Superclass

    def cast(obj):
        """cast(itkLightObject obj) -> itkSinImageFilterIF3IF3_Superclass"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkSinImageFilterIF3IF3_Superclass self) -> itkSinImageFilterIF3IF3_Superclass"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSinImageFilterIF3IF3_Superclass

        Create a new object of the class itkSinImageFilterIF3IF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterIF3IF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterIF3IF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterIF3IF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterIF3IF3_Superclass.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_Clone, None, itkSinImageFilterIF3IF3_Superclass)
itkSinImageFilterIF3IF3_Superclass.GetFunctor = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_GetFunctor, None, itkSinImageFilterIF3IF3_Superclass)
itkSinImageFilterIF3IF3_Superclass.SetFunctor = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_SetFunctor, None, itkSinImageFilterIF3IF3_Superclass)
itkSinImageFilterIF3IF3_Superclass.GetPointer = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_GetPointer, None, itkSinImageFilterIF3IF3_Superclass)
itkSinImageFilterIF3IF3_Superclass_swigregister = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_swigregister
itkSinImageFilterIF3IF3_Superclass_swigregister(itkSinImageFilterIF3IF3_Superclass)

def itkSinImageFilterIF3IF3_Superclass___New_orig__():
    """itkSinImageFilterIF3IF3_Superclass___New_orig__() -> itkSinImageFilterIF3IF3_Superclass_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass___New_orig__()

def itkSinImageFilterIF3IF3_Superclass_cast(obj):
    """itkSinImageFilterIF3IF3_Superclass_cast(itkLightObject obj) -> itkSinImageFilterIF3IF3_Superclass"""
    return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Superclass_cast(obj)

class itkSinImageFilterIF2IF2(itkSinImageFilterIF2IF2_Superclass):
    """Proxy of C++ itkSinImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkSinImageFilterIF2IF2_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkSinImageFilterIF2IF2 self) -> itkSinImageFilterIF2IF2_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkSinImageFilterIF2IF2"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkSinImageFilterIF2IF2 self) -> itkSinImageFilterIF2IF2"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSinImageFilterIF2IF2

        Create a new object of the class itkSinImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterIF2IF2.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Clone, None, itkSinImageFilterIF2IF2)
itkSinImageFilterIF2IF2.GetPointer = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_GetPointer, None, itkSinImageFilterIF2IF2)
itkSinImageFilterIF2IF2_swigregister = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_swigregister
itkSinImageFilterIF2IF2_swigregister(itkSinImageFilterIF2IF2)

def itkSinImageFilterIF2IF2___New_orig__():
    """itkSinImageFilterIF2IF2___New_orig__() -> itkSinImageFilterIF2IF2_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterIF2IF2___New_orig__()

def itkSinImageFilterIF2IF2_cast(obj):
    """itkSinImageFilterIF2IF2_cast(itkLightObject obj) -> itkSinImageFilterIF2IF2"""
    return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_cast(obj)

class itkSinImageFilterIF3IF3(itkSinImageFilterIF3IF3_Superclass):
    """Proxy of C++ itkSinImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkSinImageFilterIF3IF3_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkSinImageFilterIF3IF3 self) -> itkSinImageFilterIF3IF3_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkSinImageFilterIF3IF3"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkSinImageFilterIF3IF3 self) -> itkSinImageFilterIF3IF3"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSinImageFilterIF3IF3

        Create a new object of the class itkSinImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterIF3IF3.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Clone, None, itkSinImageFilterIF3IF3)
itkSinImageFilterIF3IF3.GetPointer = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_GetPointer, None, itkSinImageFilterIF3IF3)
itkSinImageFilterIF3IF3_swigregister = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_swigregister
itkSinImageFilterIF3IF3_swigregister(itkSinImageFilterIF3IF3)

def itkSinImageFilterIF3IF3___New_orig__():
    """itkSinImageFilterIF3IF3___New_orig__() -> itkSinImageFilterIF3IF3_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterIF3IF3___New_orig__()

def itkSinImageFilterIF3IF3_cast(obj):
    """itkSinImageFilterIF3IF3_cast(itkLightObject obj) -> itkSinImageFilterIF3IF3"""
    return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_cast(obj)



