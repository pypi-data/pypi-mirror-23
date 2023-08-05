# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkParametricPathPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkParametricPathPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkParametricPathPython')
    _itkParametricPathPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkParametricPathPython', [dirname(__file__)])
        except ImportError:
            import _itkParametricPathPython
            return _itkParametricPathPython
        try:
            _mod = imp.load_module('_itkParametricPathPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkParametricPathPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkParametricPathPython
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
import itkOffsetPython
import itkSizePython
import itkPathBasePython
import itkContinuousIndexPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkIndexPython

def itkParametricPath3_New():
  return itkParametricPath3.New()


def itkParametricPath2_New():
  return itkParametricPath2.New()

class itkParametricPath2(itkPathBasePython.itkPathDCID22):
    """Proxy of C++ itkParametricPath2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def EvaluateDerivative(self, input: 'double const &') -> "itkVectorD2":
        """EvaluateDerivative(itkParametricPath2 self, double const & input) -> itkVectorD2"""
        return _itkParametricPathPython.itkParametricPath2_EvaluateDerivative(self, input)


    def SetDefaultInputStepSize(self, _arg: 'double const') -> "void":
        """SetDefaultInputStepSize(itkParametricPath2 self, double const _arg)"""
        return _itkParametricPathPython.itkParametricPath2_SetDefaultInputStepSize(self, _arg)


    def GetDefaultInputStepSize(self) -> "double const &":
        """GetDefaultInputStepSize(itkParametricPath2 self) -> double const &"""
        return _itkParametricPathPython.itkParametricPath2_GetDefaultInputStepSize(self)

    __swig_destroy__ = _itkParametricPathPython.delete_itkParametricPath2

    def cast(obj: 'itkLightObject') -> "itkParametricPath2 *":
        """cast(itkLightObject obj) -> itkParametricPath2"""
        return _itkParametricPathPython.itkParametricPath2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkParametricPath2 *":
        """GetPointer(itkParametricPath2 self) -> itkParametricPath2"""
        return _itkParametricPathPython.itkParametricPath2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkParametricPath2

        Create a new object of the class itkParametricPath2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParametricPath2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParametricPath2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParametricPath2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkParametricPath2.EvaluateDerivative = new_instancemethod(_itkParametricPathPython.itkParametricPath2_EvaluateDerivative, None, itkParametricPath2)
itkParametricPath2.SetDefaultInputStepSize = new_instancemethod(_itkParametricPathPython.itkParametricPath2_SetDefaultInputStepSize, None, itkParametricPath2)
itkParametricPath2.GetDefaultInputStepSize = new_instancemethod(_itkParametricPathPython.itkParametricPath2_GetDefaultInputStepSize, None, itkParametricPath2)
itkParametricPath2.GetPointer = new_instancemethod(_itkParametricPathPython.itkParametricPath2_GetPointer, None, itkParametricPath2)
itkParametricPath2_swigregister = _itkParametricPathPython.itkParametricPath2_swigregister
itkParametricPath2_swigregister(itkParametricPath2)

def itkParametricPath2_cast(obj: 'itkLightObject') -> "itkParametricPath2 *":
    """itkParametricPath2_cast(itkLightObject obj) -> itkParametricPath2"""
    return _itkParametricPathPython.itkParametricPath2_cast(obj)

class itkParametricPath3(itkPathBasePython.itkPathDCID33):
    """Proxy of C++ itkParametricPath3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def EvaluateDerivative(self, input: 'double const &') -> "itkVectorD3":
        """EvaluateDerivative(itkParametricPath3 self, double const & input) -> itkVectorD3"""
        return _itkParametricPathPython.itkParametricPath3_EvaluateDerivative(self, input)


    def SetDefaultInputStepSize(self, _arg: 'double const') -> "void":
        """SetDefaultInputStepSize(itkParametricPath3 self, double const _arg)"""
        return _itkParametricPathPython.itkParametricPath3_SetDefaultInputStepSize(self, _arg)


    def GetDefaultInputStepSize(self) -> "double const &":
        """GetDefaultInputStepSize(itkParametricPath3 self) -> double const &"""
        return _itkParametricPathPython.itkParametricPath3_GetDefaultInputStepSize(self)

    __swig_destroy__ = _itkParametricPathPython.delete_itkParametricPath3

    def cast(obj: 'itkLightObject') -> "itkParametricPath3 *":
        """cast(itkLightObject obj) -> itkParametricPath3"""
        return _itkParametricPathPython.itkParametricPath3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkParametricPath3 *":
        """GetPointer(itkParametricPath3 self) -> itkParametricPath3"""
        return _itkParametricPathPython.itkParametricPath3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkParametricPath3

        Create a new object of the class itkParametricPath3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParametricPath3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParametricPath3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParametricPath3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkParametricPath3.EvaluateDerivative = new_instancemethod(_itkParametricPathPython.itkParametricPath3_EvaluateDerivative, None, itkParametricPath3)
itkParametricPath3.SetDefaultInputStepSize = new_instancemethod(_itkParametricPathPython.itkParametricPath3_SetDefaultInputStepSize, None, itkParametricPath3)
itkParametricPath3.GetDefaultInputStepSize = new_instancemethod(_itkParametricPathPython.itkParametricPath3_GetDefaultInputStepSize, None, itkParametricPath3)
itkParametricPath3.GetPointer = new_instancemethod(_itkParametricPathPython.itkParametricPath3_GetPointer, None, itkParametricPath3)
itkParametricPath3_swigregister = _itkParametricPathPython.itkParametricPath3_swigregister
itkParametricPath3_swigregister(itkParametricPath3)

def itkParametricPath3_cast(obj: 'itkLightObject') -> "itkParametricPath3 *":
    """itkParametricPath3_cast(itkLightObject obj) -> itkParametricPath3"""
    return _itkParametricPathPython.itkParametricPath3_cast(obj)



