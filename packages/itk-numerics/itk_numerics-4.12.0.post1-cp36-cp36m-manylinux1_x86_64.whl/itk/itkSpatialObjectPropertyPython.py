# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSpatialObjectPropertyPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSpatialObjectPropertyPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSpatialObjectPropertyPython')
    _itkSpatialObjectPropertyPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSpatialObjectPropertyPython', [dirname(__file__)])
        except ImportError:
            import _itkSpatialObjectPropertyPython
            return _itkSpatialObjectPropertyPython
        try:
            _mod = imp.load_module('_itkSpatialObjectPropertyPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSpatialObjectPropertyPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSpatialObjectPropertyPython
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


import itkRGBAPixelPython
import itkFixedArrayPython
import pyBasePython
import ITKCommonBasePython

def itkSpatialObjectPropertyF_New():
  return itkSpatialObjectPropertyF.New()

class itkSpatialObjectPropertyF(ITKCommonBasePython.itkLightObject):
    """Proxy of C++ itkSpatialObjectPropertyF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpatialObjectPropertyF_Pointer":
        """__New_orig__() -> itkSpatialObjectPropertyF_Pointer"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpatialObjectPropertyF_Pointer":
        """Clone(itkSpatialObjectPropertyF self) -> itkSpatialObjectPropertyF_Pointer"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_Clone(self)


    def GetColor(self) -> "itkRGBAPixelF const &":
        """GetColor(itkSpatialObjectPropertyF self) -> itkRGBAPixelF"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetColor(self)


    def SetColor(self, *args) -> "void":
        """
        SetColor(itkSpatialObjectPropertyF self, itkRGBAPixelF color)
        SetColor(itkSpatialObjectPropertyF self, float r, float g, float b)
        """
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetColor(self, *args)


    def SetRed(self, r: 'float') -> "void":
        """SetRed(itkSpatialObjectPropertyF self, float r)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetRed(self, r)


    def GetRed(self) -> "float":
        """GetRed(itkSpatialObjectPropertyF self) -> float"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetRed(self)


    def SetGreen(self, g: 'float') -> "void":
        """SetGreen(itkSpatialObjectPropertyF self, float g)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetGreen(self, g)


    def GetGreen(self) -> "float":
        """GetGreen(itkSpatialObjectPropertyF self) -> float"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetGreen(self)


    def SetBlue(self, b: 'float') -> "void":
        """SetBlue(itkSpatialObjectPropertyF self, float b)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetBlue(self, b)


    def GetBlue(self) -> "float":
        """GetBlue(itkSpatialObjectPropertyF self) -> float"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetBlue(self)


    def SetAlpha(self, a: 'float') -> "void":
        """SetAlpha(itkSpatialObjectPropertyF self, float a)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetAlpha(self, a)


    def GetAlpha(self) -> "float":
        """GetAlpha(itkSpatialObjectPropertyF self) -> float"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetAlpha(self)


    def __init__(self):
        """__init__(itkSpatialObjectPropertyF self) -> itkSpatialObjectPropertyF"""
        _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_swiginit(self, _itkSpatialObjectPropertyPython.new_itkSpatialObjectPropertyF())

    def SetName(self, name: 'char const *') -> "void":
        """SetName(itkSpatialObjectPropertyF self, char const * name)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetName(self, name)


    def GetName(self) -> "std::string":
        """GetName(itkSpatialObjectPropertyF self) -> std::string"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetName(self)


    def GetMTime(self) -> "unsigned long":
        """GetMTime(itkSpatialObjectPropertyF self) -> unsigned long"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetMTime(self)

    __swig_destroy__ = _itkSpatialObjectPropertyPython.delete_itkSpatialObjectPropertyF

    def cast(obj: 'itkLightObject') -> "itkSpatialObjectPropertyF *":
        """cast(itkLightObject obj) -> itkSpatialObjectPropertyF"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSpatialObjectPropertyF *":
        """GetPointer(itkSpatialObjectPropertyF self) -> itkSpatialObjectPropertyF"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSpatialObjectPropertyF

        Create a new object of the class itkSpatialObjectPropertyF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpatialObjectPropertyF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpatialObjectPropertyF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpatialObjectPropertyF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpatialObjectPropertyF.Clone = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_Clone, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetColor = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetColor, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.SetColor = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetColor, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.SetRed = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetRed, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetRed = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetRed, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.SetGreen = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetGreen, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetGreen = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetGreen, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.SetBlue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetBlue, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetBlue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetBlue, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.SetAlpha = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetAlpha, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetAlpha = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetAlpha, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.SetName = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_SetName, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetName = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetName, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetMTime = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetMTime, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF.GetPointer = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_GetPointer, None, itkSpatialObjectPropertyF)
itkSpatialObjectPropertyF_swigregister = _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_swigregister
itkSpatialObjectPropertyF_swigregister(itkSpatialObjectPropertyF)

def itkSpatialObjectPropertyF___New_orig__() -> "itkSpatialObjectPropertyF_Pointer":
    """itkSpatialObjectPropertyF___New_orig__() -> itkSpatialObjectPropertyF_Pointer"""
    return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF___New_orig__()

def itkSpatialObjectPropertyF_cast(obj: 'itkLightObject') -> "itkSpatialObjectPropertyF *":
    """itkSpatialObjectPropertyF_cast(itkLightObject obj) -> itkSpatialObjectPropertyF"""
    return _itkSpatialObjectPropertyPython.itkSpatialObjectPropertyF_cast(obj)



