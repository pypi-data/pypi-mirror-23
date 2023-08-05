# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPermuteAxesImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPermuteAxesImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPermuteAxesImageFilterPython')
    _itkPermuteAxesImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPermuteAxesImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkPermuteAxesImageFilterPython
            return _itkPermuteAxesImageFilterPython
        try:
            _mod = imp.load_module('_itkPermuteAxesImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPermuteAxesImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPermuteAxesImageFilterPython
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
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkImageToImageFilterAPython
import itkImagePython
import stdcomplexPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
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

def itkPermuteAxesImageFilterIF3_New():
  return itkPermuteAxesImageFilterIF3.New()


def itkPermuteAxesImageFilterIF2_New():
  return itkPermuteAxesImageFilterIF2.New()


def itkPermuteAxesImageFilterIUC3_New():
  return itkPermuteAxesImageFilterIUC3.New()


def itkPermuteAxesImageFilterIUC2_New():
  return itkPermuteAxesImageFilterIUC2.New()


def itkPermuteAxesImageFilterISS3_New():
  return itkPermuteAxesImageFilterISS3.New()


def itkPermuteAxesImageFilterISS2_New():
  return itkPermuteAxesImageFilterISS2.New()

class itkPermuteAxesImageFilterIF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkPermuteAxesImageFilterIF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPermuteAxesImageFilterIF2_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPermuteAxesImageFilterIF2 self) -> itkPermuteAxesImageFilterIF2_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_Clone(self)


    def SetOrder(self, order):
        """SetOrder(itkPermuteAxesImageFilterIF2 self, itkFixedArrayUI2 order)"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_SetOrder(self, order)


    def GetOrder(self):
        """GetOrder(itkPermuteAxesImageFilterIF2 self) -> itkFixedArrayUI2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_GetOrder(self)


    def GetInverseOrder(self):
        """GetInverseOrder(itkPermuteAxesImageFilterIF2 self) -> itkFixedArrayUI2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_GetInverseOrder(self)

    __swig_destroy__ = _itkPermuteAxesImageFilterPython.delete_itkPermuteAxesImageFilterIF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkPermuteAxesImageFilterIF2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPermuteAxesImageFilterIF2 self) -> itkPermuteAxesImageFilterIF2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPermuteAxesImageFilterIF2

        Create a new object of the class itkPermuteAxesImageFilterIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPermuteAxesImageFilterIF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPermuteAxesImageFilterIF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPermuteAxesImageFilterIF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPermuteAxesImageFilterIF2.Clone = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_Clone, None, itkPermuteAxesImageFilterIF2)
itkPermuteAxesImageFilterIF2.SetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_SetOrder, None, itkPermuteAxesImageFilterIF2)
itkPermuteAxesImageFilterIF2.GetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_GetOrder, None, itkPermuteAxesImageFilterIF2)
itkPermuteAxesImageFilterIF2.GetInverseOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_GetInverseOrder, None, itkPermuteAxesImageFilterIF2)
itkPermuteAxesImageFilterIF2.GetPointer = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_GetPointer, None, itkPermuteAxesImageFilterIF2)
itkPermuteAxesImageFilterIF2_swigregister = _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_swigregister
itkPermuteAxesImageFilterIF2_swigregister(itkPermuteAxesImageFilterIF2)

def itkPermuteAxesImageFilterIF2___New_orig__():
    """itkPermuteAxesImageFilterIF2___New_orig__() -> itkPermuteAxesImageFilterIF2_Pointer"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2___New_orig__()

def itkPermuteAxesImageFilterIF2_cast(obj):
    """itkPermuteAxesImageFilterIF2_cast(itkLightObject obj) -> itkPermuteAxesImageFilterIF2"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF2_cast(obj)

class itkPermuteAxesImageFilterIF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkPermuteAxesImageFilterIF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPermuteAxesImageFilterIF3_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPermuteAxesImageFilterIF3 self) -> itkPermuteAxesImageFilterIF3_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_Clone(self)


    def SetOrder(self, order):
        """SetOrder(itkPermuteAxesImageFilterIF3 self, itkFixedArrayUI3 order)"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_SetOrder(self, order)


    def GetOrder(self):
        """GetOrder(itkPermuteAxesImageFilterIF3 self) -> itkFixedArrayUI3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_GetOrder(self)


    def GetInverseOrder(self):
        """GetInverseOrder(itkPermuteAxesImageFilterIF3 self) -> itkFixedArrayUI3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_GetInverseOrder(self)

    __swig_destroy__ = _itkPermuteAxesImageFilterPython.delete_itkPermuteAxesImageFilterIF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkPermuteAxesImageFilterIF3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPermuteAxesImageFilterIF3 self) -> itkPermuteAxesImageFilterIF3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPermuteAxesImageFilterIF3

        Create a new object of the class itkPermuteAxesImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPermuteAxesImageFilterIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPermuteAxesImageFilterIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPermuteAxesImageFilterIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPermuteAxesImageFilterIF3.Clone = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_Clone, None, itkPermuteAxesImageFilterIF3)
itkPermuteAxesImageFilterIF3.SetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_SetOrder, None, itkPermuteAxesImageFilterIF3)
itkPermuteAxesImageFilterIF3.GetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_GetOrder, None, itkPermuteAxesImageFilterIF3)
itkPermuteAxesImageFilterIF3.GetInverseOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_GetInverseOrder, None, itkPermuteAxesImageFilterIF3)
itkPermuteAxesImageFilterIF3.GetPointer = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_GetPointer, None, itkPermuteAxesImageFilterIF3)
itkPermuteAxesImageFilterIF3_swigregister = _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_swigregister
itkPermuteAxesImageFilterIF3_swigregister(itkPermuteAxesImageFilterIF3)

def itkPermuteAxesImageFilterIF3___New_orig__():
    """itkPermuteAxesImageFilterIF3___New_orig__() -> itkPermuteAxesImageFilterIF3_Pointer"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3___New_orig__()

def itkPermuteAxesImageFilterIF3_cast(obj):
    """itkPermuteAxesImageFilterIF3_cast(itkLightObject obj) -> itkPermuteAxesImageFilterIF3"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIF3_cast(obj)

class itkPermuteAxesImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkPermuteAxesImageFilterISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPermuteAxesImageFilterISS2_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPermuteAxesImageFilterISS2 self) -> itkPermuteAxesImageFilterISS2_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_Clone(self)


    def SetOrder(self, order):
        """SetOrder(itkPermuteAxesImageFilterISS2 self, itkFixedArrayUI2 order)"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_SetOrder(self, order)


    def GetOrder(self):
        """GetOrder(itkPermuteAxesImageFilterISS2 self) -> itkFixedArrayUI2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_GetOrder(self)


    def GetInverseOrder(self):
        """GetInverseOrder(itkPermuteAxesImageFilterISS2 self) -> itkFixedArrayUI2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_GetInverseOrder(self)

    __swig_destroy__ = _itkPermuteAxesImageFilterPython.delete_itkPermuteAxesImageFilterISS2

    def cast(obj):
        """cast(itkLightObject obj) -> itkPermuteAxesImageFilterISS2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPermuteAxesImageFilterISS2 self) -> itkPermuteAxesImageFilterISS2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPermuteAxesImageFilterISS2

        Create a new object of the class itkPermuteAxesImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPermuteAxesImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPermuteAxesImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPermuteAxesImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPermuteAxesImageFilterISS2.Clone = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_Clone, None, itkPermuteAxesImageFilterISS2)
itkPermuteAxesImageFilterISS2.SetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_SetOrder, None, itkPermuteAxesImageFilterISS2)
itkPermuteAxesImageFilterISS2.GetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_GetOrder, None, itkPermuteAxesImageFilterISS2)
itkPermuteAxesImageFilterISS2.GetInverseOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_GetInverseOrder, None, itkPermuteAxesImageFilterISS2)
itkPermuteAxesImageFilterISS2.GetPointer = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_GetPointer, None, itkPermuteAxesImageFilterISS2)
itkPermuteAxesImageFilterISS2_swigregister = _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_swigregister
itkPermuteAxesImageFilterISS2_swigregister(itkPermuteAxesImageFilterISS2)

def itkPermuteAxesImageFilterISS2___New_orig__():
    """itkPermuteAxesImageFilterISS2___New_orig__() -> itkPermuteAxesImageFilterISS2_Pointer"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2___New_orig__()

def itkPermuteAxesImageFilterISS2_cast(obj):
    """itkPermuteAxesImageFilterISS2_cast(itkLightObject obj) -> itkPermuteAxesImageFilterISS2"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS2_cast(obj)

class itkPermuteAxesImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkPermuteAxesImageFilterISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPermuteAxesImageFilterISS3_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPermuteAxesImageFilterISS3 self) -> itkPermuteAxesImageFilterISS3_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_Clone(self)


    def SetOrder(self, order):
        """SetOrder(itkPermuteAxesImageFilterISS3 self, itkFixedArrayUI3 order)"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_SetOrder(self, order)


    def GetOrder(self):
        """GetOrder(itkPermuteAxesImageFilterISS3 self) -> itkFixedArrayUI3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_GetOrder(self)


    def GetInverseOrder(self):
        """GetInverseOrder(itkPermuteAxesImageFilterISS3 self) -> itkFixedArrayUI3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_GetInverseOrder(self)

    __swig_destroy__ = _itkPermuteAxesImageFilterPython.delete_itkPermuteAxesImageFilterISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkPermuteAxesImageFilterISS3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPermuteAxesImageFilterISS3 self) -> itkPermuteAxesImageFilterISS3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPermuteAxesImageFilterISS3

        Create a new object of the class itkPermuteAxesImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPermuteAxesImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPermuteAxesImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPermuteAxesImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPermuteAxesImageFilterISS3.Clone = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_Clone, None, itkPermuteAxesImageFilterISS3)
itkPermuteAxesImageFilterISS3.SetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_SetOrder, None, itkPermuteAxesImageFilterISS3)
itkPermuteAxesImageFilterISS3.GetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_GetOrder, None, itkPermuteAxesImageFilterISS3)
itkPermuteAxesImageFilterISS3.GetInverseOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_GetInverseOrder, None, itkPermuteAxesImageFilterISS3)
itkPermuteAxesImageFilterISS3.GetPointer = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_GetPointer, None, itkPermuteAxesImageFilterISS3)
itkPermuteAxesImageFilterISS3_swigregister = _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_swigregister
itkPermuteAxesImageFilterISS3_swigregister(itkPermuteAxesImageFilterISS3)

def itkPermuteAxesImageFilterISS3___New_orig__():
    """itkPermuteAxesImageFilterISS3___New_orig__() -> itkPermuteAxesImageFilterISS3_Pointer"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3___New_orig__()

def itkPermuteAxesImageFilterISS3_cast(obj):
    """itkPermuteAxesImageFilterISS3_cast(itkLightObject obj) -> itkPermuteAxesImageFilterISS3"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterISS3_cast(obj)

class itkPermuteAxesImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkPermuteAxesImageFilterIUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPermuteAxesImageFilterIUC2_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPermuteAxesImageFilterIUC2 self) -> itkPermuteAxesImageFilterIUC2_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_Clone(self)


    def SetOrder(self, order):
        """SetOrder(itkPermuteAxesImageFilterIUC2 self, itkFixedArrayUI2 order)"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_SetOrder(self, order)


    def GetOrder(self):
        """GetOrder(itkPermuteAxesImageFilterIUC2 self) -> itkFixedArrayUI2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_GetOrder(self)


    def GetInverseOrder(self):
        """GetInverseOrder(itkPermuteAxesImageFilterIUC2 self) -> itkFixedArrayUI2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_GetInverseOrder(self)

    __swig_destroy__ = _itkPermuteAxesImageFilterPython.delete_itkPermuteAxesImageFilterIUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkPermuteAxesImageFilterIUC2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPermuteAxesImageFilterIUC2 self) -> itkPermuteAxesImageFilterIUC2"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPermuteAxesImageFilterIUC2

        Create a new object of the class itkPermuteAxesImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPermuteAxesImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPermuteAxesImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPermuteAxesImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPermuteAxesImageFilterIUC2.Clone = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_Clone, None, itkPermuteAxesImageFilterIUC2)
itkPermuteAxesImageFilterIUC2.SetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_SetOrder, None, itkPermuteAxesImageFilterIUC2)
itkPermuteAxesImageFilterIUC2.GetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_GetOrder, None, itkPermuteAxesImageFilterIUC2)
itkPermuteAxesImageFilterIUC2.GetInverseOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_GetInverseOrder, None, itkPermuteAxesImageFilterIUC2)
itkPermuteAxesImageFilterIUC2.GetPointer = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_GetPointer, None, itkPermuteAxesImageFilterIUC2)
itkPermuteAxesImageFilterIUC2_swigregister = _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_swigregister
itkPermuteAxesImageFilterIUC2_swigregister(itkPermuteAxesImageFilterIUC2)

def itkPermuteAxesImageFilterIUC2___New_orig__():
    """itkPermuteAxesImageFilterIUC2___New_orig__() -> itkPermuteAxesImageFilterIUC2_Pointer"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2___New_orig__()

def itkPermuteAxesImageFilterIUC2_cast(obj):
    """itkPermuteAxesImageFilterIUC2_cast(itkLightObject obj) -> itkPermuteAxesImageFilterIUC2"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC2_cast(obj)

class itkPermuteAxesImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkPermuteAxesImageFilterIUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPermuteAxesImageFilterIUC3_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPermuteAxesImageFilterIUC3 self) -> itkPermuteAxesImageFilterIUC3_Pointer"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_Clone(self)


    def SetOrder(self, order):
        """SetOrder(itkPermuteAxesImageFilterIUC3 self, itkFixedArrayUI3 order)"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_SetOrder(self, order)


    def GetOrder(self):
        """GetOrder(itkPermuteAxesImageFilterIUC3 self) -> itkFixedArrayUI3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_GetOrder(self)


    def GetInverseOrder(self):
        """GetInverseOrder(itkPermuteAxesImageFilterIUC3 self) -> itkFixedArrayUI3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_GetInverseOrder(self)

    __swig_destroy__ = _itkPermuteAxesImageFilterPython.delete_itkPermuteAxesImageFilterIUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkPermuteAxesImageFilterIUC3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPermuteAxesImageFilterIUC3 self) -> itkPermuteAxesImageFilterIUC3"""
        return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPermuteAxesImageFilterIUC3

        Create a new object of the class itkPermuteAxesImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPermuteAxesImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPermuteAxesImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPermuteAxesImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPermuteAxesImageFilterIUC3.Clone = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_Clone, None, itkPermuteAxesImageFilterIUC3)
itkPermuteAxesImageFilterIUC3.SetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_SetOrder, None, itkPermuteAxesImageFilterIUC3)
itkPermuteAxesImageFilterIUC3.GetOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_GetOrder, None, itkPermuteAxesImageFilterIUC3)
itkPermuteAxesImageFilterIUC3.GetInverseOrder = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_GetInverseOrder, None, itkPermuteAxesImageFilterIUC3)
itkPermuteAxesImageFilterIUC3.GetPointer = new_instancemethod(_itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_GetPointer, None, itkPermuteAxesImageFilterIUC3)
itkPermuteAxesImageFilterIUC3_swigregister = _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_swigregister
itkPermuteAxesImageFilterIUC3_swigregister(itkPermuteAxesImageFilterIUC3)

def itkPermuteAxesImageFilterIUC3___New_orig__():
    """itkPermuteAxesImageFilterIUC3___New_orig__() -> itkPermuteAxesImageFilterIUC3_Pointer"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3___New_orig__()

def itkPermuteAxesImageFilterIUC3_cast(obj):
    """itkPermuteAxesImageFilterIUC3_cast(itkLightObject obj) -> itkPermuteAxesImageFilterIUC3"""
    return _itkPermuteAxesImageFilterPython.itkPermuteAxesImageFilterIUC3_cast(obj)



