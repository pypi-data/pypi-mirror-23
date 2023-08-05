# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkImageToPathFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkImageToPathFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkImageToPathFilterPython')
    _itkImageToPathFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkImageToPathFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkImageToPathFilterPython
            return _itkImageToPathFilterPython
        try:
            _mod = imp.load_module('_itkImageToPathFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkImageToPathFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkImageToPathFilterPython
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


import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkOffsetPython
import itkSizePython
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
import itkIndexPython
import ITKCommonBasePython
import itkImageRegionPython
import itkPathSourcePython
import itkPolyLineParametricPathPython
import itkContinuousIndexPython
import itkParametricPathPython
import itkPathBasePython
import itkVectorContainerPython

def itkImageToPathFilterIF3PLPP3_New():
  return itkImageToPathFilterIF3PLPP3.New()


def itkImageToPathFilterIUC3PLPP3_New():
  return itkImageToPathFilterIUC3PLPP3.New()


def itkImageToPathFilterISS3PLPP3_New():
  return itkImageToPathFilterISS3PLPP3.New()


def itkImageToPathFilterIF2PLPP2_New():
  return itkImageToPathFilterIF2PLPP2.New()


def itkImageToPathFilterIUC2PLPP2_New():
  return itkImageToPathFilterIUC2PLPP2.New()


def itkImageToPathFilterISS2PLPP2_New():
  return itkImageToPathFilterISS2PLPP2.New()

class itkImageToPathFilterIF2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    """Proxy of C++ itkImageToPathFilterIF2PLPP2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToPathFilterIF2PLPP2 self, itkImageF2 image)
        SetInput(itkImageToPathFilterIF2PLPP2 self, unsigned int arg0, itkImageF2 image)
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageF2 const *":
        """
        GetInput(itkImageToPathFilterIF2PLPP2 self) -> itkImageF2
        GetInput(itkImageToPathFilterIF2PLPP2 self, unsigned int idx) -> itkImageF2
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_GetInput(self, *args)

    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIF2PLPP2

    def cast(obj: 'itkLightObject') -> "itkImageToPathFilterIF2PLPP2 *":
        """cast(itkLightObject obj) -> itkImageToPathFilterIF2PLPP2"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageToPathFilterIF2PLPP2 *":
        """GetPointer(itkImageToPathFilterIF2PLPP2 self) -> itkImageToPathFilterIF2PLPP2"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIF2PLPP2

        Create a new object of the class itkImageToPathFilterIF2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIF2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIF2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIF2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToPathFilterIF2PLPP2.SetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_SetInput, None, itkImageToPathFilterIF2PLPP2)
itkImageToPathFilterIF2PLPP2.GetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_GetInput, None, itkImageToPathFilterIF2PLPP2)
itkImageToPathFilterIF2PLPP2.GetPointer = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_GetPointer, None, itkImageToPathFilterIF2PLPP2)
itkImageToPathFilterIF2PLPP2_swigregister = _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_swigregister
itkImageToPathFilterIF2PLPP2_swigregister(itkImageToPathFilterIF2PLPP2)

def itkImageToPathFilterIF2PLPP2_cast(obj: 'itkLightObject') -> "itkImageToPathFilterIF2PLPP2 *":
    """itkImageToPathFilterIF2PLPP2_cast(itkLightObject obj) -> itkImageToPathFilterIF2PLPP2"""
    return _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_cast(obj)

class itkImageToPathFilterIF3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    """Proxy of C++ itkImageToPathFilterIF3PLPP3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToPathFilterIF3PLPP3 self, itkImageF3 image)
        SetInput(itkImageToPathFilterIF3PLPP3 self, unsigned int arg0, itkImageF3 image)
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageF3 const *":
        """
        GetInput(itkImageToPathFilterIF3PLPP3 self) -> itkImageF3
        GetInput(itkImageToPathFilterIF3PLPP3 self, unsigned int idx) -> itkImageF3
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_GetInput(self, *args)

    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIF3PLPP3

    def cast(obj: 'itkLightObject') -> "itkImageToPathFilterIF3PLPP3 *":
        """cast(itkLightObject obj) -> itkImageToPathFilterIF3PLPP3"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageToPathFilterIF3PLPP3 *":
        """GetPointer(itkImageToPathFilterIF3PLPP3 self) -> itkImageToPathFilterIF3PLPP3"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIF3PLPP3

        Create a new object of the class itkImageToPathFilterIF3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIF3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIF3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIF3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToPathFilterIF3PLPP3.SetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_SetInput, None, itkImageToPathFilterIF3PLPP3)
itkImageToPathFilterIF3PLPP3.GetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_GetInput, None, itkImageToPathFilterIF3PLPP3)
itkImageToPathFilterIF3PLPP3.GetPointer = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_GetPointer, None, itkImageToPathFilterIF3PLPP3)
itkImageToPathFilterIF3PLPP3_swigregister = _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_swigregister
itkImageToPathFilterIF3PLPP3_swigregister(itkImageToPathFilterIF3PLPP3)

def itkImageToPathFilterIF3PLPP3_cast(obj: 'itkLightObject') -> "itkImageToPathFilterIF3PLPP3 *":
    """itkImageToPathFilterIF3PLPP3_cast(itkLightObject obj) -> itkImageToPathFilterIF3PLPP3"""
    return _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_cast(obj)

class itkImageToPathFilterISS2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    """Proxy of C++ itkImageToPathFilterISS2PLPP2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToPathFilterISS2PLPP2 self, itkImageSS2 image)
        SetInput(itkImageToPathFilterISS2PLPP2 self, unsigned int arg0, itkImageSS2 image)
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageSS2 const *":
        """
        GetInput(itkImageToPathFilterISS2PLPP2 self) -> itkImageSS2
        GetInput(itkImageToPathFilterISS2PLPP2 self, unsigned int idx) -> itkImageSS2
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_GetInput(self, *args)

    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterISS2PLPP2

    def cast(obj: 'itkLightObject') -> "itkImageToPathFilterISS2PLPP2 *":
        """cast(itkLightObject obj) -> itkImageToPathFilterISS2PLPP2"""
        return _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageToPathFilterISS2PLPP2 *":
        """GetPointer(itkImageToPathFilterISS2PLPP2 self) -> itkImageToPathFilterISS2PLPP2"""
        return _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToPathFilterISS2PLPP2

        Create a new object of the class itkImageToPathFilterISS2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterISS2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterISS2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterISS2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToPathFilterISS2PLPP2.SetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_SetInput, None, itkImageToPathFilterISS2PLPP2)
itkImageToPathFilterISS2PLPP2.GetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_GetInput, None, itkImageToPathFilterISS2PLPP2)
itkImageToPathFilterISS2PLPP2.GetPointer = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_GetPointer, None, itkImageToPathFilterISS2PLPP2)
itkImageToPathFilterISS2PLPP2_swigregister = _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_swigregister
itkImageToPathFilterISS2PLPP2_swigregister(itkImageToPathFilterISS2PLPP2)

def itkImageToPathFilterISS2PLPP2_cast(obj: 'itkLightObject') -> "itkImageToPathFilterISS2PLPP2 *":
    """itkImageToPathFilterISS2PLPP2_cast(itkLightObject obj) -> itkImageToPathFilterISS2PLPP2"""
    return _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_cast(obj)

class itkImageToPathFilterISS3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    """Proxy of C++ itkImageToPathFilterISS3PLPP3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToPathFilterISS3PLPP3 self, itkImageSS3 image)
        SetInput(itkImageToPathFilterISS3PLPP3 self, unsigned int arg0, itkImageSS3 image)
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageSS3 const *":
        """
        GetInput(itkImageToPathFilterISS3PLPP3 self) -> itkImageSS3
        GetInput(itkImageToPathFilterISS3PLPP3 self, unsigned int idx) -> itkImageSS3
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_GetInput(self, *args)

    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterISS3PLPP3

    def cast(obj: 'itkLightObject') -> "itkImageToPathFilterISS3PLPP3 *":
        """cast(itkLightObject obj) -> itkImageToPathFilterISS3PLPP3"""
        return _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageToPathFilterISS3PLPP3 *":
        """GetPointer(itkImageToPathFilterISS3PLPP3 self) -> itkImageToPathFilterISS3PLPP3"""
        return _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToPathFilterISS3PLPP3

        Create a new object of the class itkImageToPathFilterISS3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterISS3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterISS3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterISS3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToPathFilterISS3PLPP3.SetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_SetInput, None, itkImageToPathFilterISS3PLPP3)
itkImageToPathFilterISS3PLPP3.GetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_GetInput, None, itkImageToPathFilterISS3PLPP3)
itkImageToPathFilterISS3PLPP3.GetPointer = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_GetPointer, None, itkImageToPathFilterISS3PLPP3)
itkImageToPathFilterISS3PLPP3_swigregister = _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_swigregister
itkImageToPathFilterISS3PLPP3_swigregister(itkImageToPathFilterISS3PLPP3)

def itkImageToPathFilterISS3PLPP3_cast(obj: 'itkLightObject') -> "itkImageToPathFilterISS3PLPP3 *":
    """itkImageToPathFilterISS3PLPP3_cast(itkLightObject obj) -> itkImageToPathFilterISS3PLPP3"""
    return _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_cast(obj)

class itkImageToPathFilterIUC2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    """Proxy of C++ itkImageToPathFilterIUC2PLPP2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToPathFilterIUC2PLPP2 self, itkImageUC2 image)
        SetInput(itkImageToPathFilterIUC2PLPP2 self, unsigned int arg0, itkImageUC2 image)
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageUC2 const *":
        """
        GetInput(itkImageToPathFilterIUC2PLPP2 self) -> itkImageUC2
        GetInput(itkImageToPathFilterIUC2PLPP2 self, unsigned int idx) -> itkImageUC2
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_GetInput(self, *args)

    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIUC2PLPP2

    def cast(obj: 'itkLightObject') -> "itkImageToPathFilterIUC2PLPP2 *":
        """cast(itkLightObject obj) -> itkImageToPathFilterIUC2PLPP2"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageToPathFilterIUC2PLPP2 *":
        """GetPointer(itkImageToPathFilterIUC2PLPP2 self) -> itkImageToPathFilterIUC2PLPP2"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIUC2PLPP2

        Create a new object of the class itkImageToPathFilterIUC2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIUC2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIUC2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIUC2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToPathFilterIUC2PLPP2.SetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_SetInput, None, itkImageToPathFilterIUC2PLPP2)
itkImageToPathFilterIUC2PLPP2.GetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_GetInput, None, itkImageToPathFilterIUC2PLPP2)
itkImageToPathFilterIUC2PLPP2.GetPointer = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_GetPointer, None, itkImageToPathFilterIUC2PLPP2)
itkImageToPathFilterIUC2PLPP2_swigregister = _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_swigregister
itkImageToPathFilterIUC2PLPP2_swigregister(itkImageToPathFilterIUC2PLPP2)

def itkImageToPathFilterIUC2PLPP2_cast(obj: 'itkLightObject') -> "itkImageToPathFilterIUC2PLPP2 *":
    """itkImageToPathFilterIUC2PLPP2_cast(itkLightObject obj) -> itkImageToPathFilterIUC2PLPP2"""
    return _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_cast(obj)

class itkImageToPathFilterIUC3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    """Proxy of C++ itkImageToPathFilterIUC3PLPP3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToPathFilterIUC3PLPP3 self, itkImageUC3 image)
        SetInput(itkImageToPathFilterIUC3PLPP3 self, unsigned int arg0, itkImageUC3 image)
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageUC3 const *":
        """
        GetInput(itkImageToPathFilterIUC3PLPP3 self) -> itkImageUC3
        GetInput(itkImageToPathFilterIUC3PLPP3 self, unsigned int idx) -> itkImageUC3
        """
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_GetInput(self, *args)

    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIUC3PLPP3

    def cast(obj: 'itkLightObject') -> "itkImageToPathFilterIUC3PLPP3 *":
        """cast(itkLightObject obj) -> itkImageToPathFilterIUC3PLPP3"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkImageToPathFilterIUC3PLPP3 *":
        """GetPointer(itkImageToPathFilterIUC3PLPP3 self) -> itkImageToPathFilterIUC3PLPP3"""
        return _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIUC3PLPP3

        Create a new object of the class itkImageToPathFilterIUC3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIUC3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIUC3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIUC3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToPathFilterIUC3PLPP3.SetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_SetInput, None, itkImageToPathFilterIUC3PLPP3)
itkImageToPathFilterIUC3PLPP3.GetInput = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_GetInput, None, itkImageToPathFilterIUC3PLPP3)
itkImageToPathFilterIUC3PLPP3.GetPointer = new_instancemethod(_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_GetPointer, None, itkImageToPathFilterIUC3PLPP3)
itkImageToPathFilterIUC3PLPP3_swigregister = _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_swigregister
itkImageToPathFilterIUC3PLPP3_swigregister(itkImageToPathFilterIUC3PLPP3)

def itkImageToPathFilterIUC3PLPP3_cast(obj: 'itkLightObject') -> "itkImageToPathFilterIUC3PLPP3 *":
    """itkImageToPathFilterIUC3PLPP3_cast(itkLightObject obj) -> itkImageToPathFilterIUC3PLPP3"""
    return _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_cast(obj)



