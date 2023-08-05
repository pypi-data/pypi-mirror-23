# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPathBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPathBasePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPathBasePython')
    _itkPathBasePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPathBasePython', [dirname(__file__)])
        except ImportError:
            import _itkPathBasePython
            return _itkPathBasePython
        try:
            _mod = imp.load_module('_itkPathBasePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPathBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPathBasePython
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


import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkContinuousIndexPython
import itkPointPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkFixedArrayPython
import vnl_vector_refPython

def itkPathDCID33_New():
  return itkPathDCID33.New()


def itkPathDCID22_New():
  return itkPathDCID22.New()

class itkPathDCID22(ITKCommonBasePython.itkDataObject):
    """Proxy of C++ itkPathDCID22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def StartOfInput(self) -> "double":
        """StartOfInput(itkPathDCID22 self) -> double"""
        return _itkPathBasePython.itkPathDCID22_StartOfInput(self)


    def EndOfInput(self) -> "double":
        """EndOfInput(itkPathDCID22 self) -> double"""
        return _itkPathBasePython.itkPathDCID22_EndOfInput(self)


    def Evaluate(self, input: 'double const &') -> "itkContinuousIndexD2":
        """Evaluate(itkPathDCID22 self, double const & input) -> itkContinuousIndexD2"""
        return _itkPathBasePython.itkPathDCID22_Evaluate(self, input)


    def EvaluateToIndex(self, input: 'double const &') -> "itkIndex2":
        """EvaluateToIndex(itkPathDCID22 self, double const & input) -> itkIndex2"""
        return _itkPathBasePython.itkPathDCID22_EvaluateToIndex(self, input)


    def IncrementInput(self, input: 'double &') -> "itkOffset2":
        """IncrementInput(itkPathDCID22 self, double & input) -> itkOffset2"""
        return _itkPathBasePython.itkPathDCID22_IncrementInput(self, input)

    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID22

    def cast(obj: 'itkLightObject') -> "itkPathDCID22 *":
        """cast(itkLightObject obj) -> itkPathDCID22"""
        return _itkPathBasePython.itkPathDCID22_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPathDCID22 *":
        """GetPointer(itkPathDCID22 self) -> itkPathDCID22"""
        return _itkPathBasePython.itkPathDCID22_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPathDCID22

        Create a new object of the class itkPathDCID22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathDCID22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPathDCID22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPathDCID22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPathDCID22.StartOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID22_StartOfInput, None, itkPathDCID22)
itkPathDCID22.EndOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID22_EndOfInput, None, itkPathDCID22)
itkPathDCID22.Evaluate = new_instancemethod(_itkPathBasePython.itkPathDCID22_Evaluate, None, itkPathDCID22)
itkPathDCID22.EvaluateToIndex = new_instancemethod(_itkPathBasePython.itkPathDCID22_EvaluateToIndex, None, itkPathDCID22)
itkPathDCID22.IncrementInput = new_instancemethod(_itkPathBasePython.itkPathDCID22_IncrementInput, None, itkPathDCID22)
itkPathDCID22.GetPointer = new_instancemethod(_itkPathBasePython.itkPathDCID22_GetPointer, None, itkPathDCID22)
itkPathDCID22_swigregister = _itkPathBasePython.itkPathDCID22_swigregister
itkPathDCID22_swigregister(itkPathDCID22)

def itkPathDCID22_cast(obj: 'itkLightObject') -> "itkPathDCID22 *":
    """itkPathDCID22_cast(itkLightObject obj) -> itkPathDCID22"""
    return _itkPathBasePython.itkPathDCID22_cast(obj)

class itkPathDCID33(ITKCommonBasePython.itkDataObject):
    """Proxy of C++ itkPathDCID33 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def StartOfInput(self) -> "double":
        """StartOfInput(itkPathDCID33 self) -> double"""
        return _itkPathBasePython.itkPathDCID33_StartOfInput(self)


    def EndOfInput(self) -> "double":
        """EndOfInput(itkPathDCID33 self) -> double"""
        return _itkPathBasePython.itkPathDCID33_EndOfInput(self)


    def Evaluate(self, input: 'double const &') -> "itkContinuousIndexD3":
        """Evaluate(itkPathDCID33 self, double const & input) -> itkContinuousIndexD3"""
        return _itkPathBasePython.itkPathDCID33_Evaluate(self, input)


    def EvaluateToIndex(self, input: 'double const &') -> "itkIndex3":
        """EvaluateToIndex(itkPathDCID33 self, double const & input) -> itkIndex3"""
        return _itkPathBasePython.itkPathDCID33_EvaluateToIndex(self, input)


    def IncrementInput(self, input: 'double &') -> "itkOffset3":
        """IncrementInput(itkPathDCID33 self, double & input) -> itkOffset3"""
        return _itkPathBasePython.itkPathDCID33_IncrementInput(self, input)

    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID33

    def cast(obj: 'itkLightObject') -> "itkPathDCID33 *":
        """cast(itkLightObject obj) -> itkPathDCID33"""
        return _itkPathBasePython.itkPathDCID33_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPathDCID33 *":
        """GetPointer(itkPathDCID33 self) -> itkPathDCID33"""
        return _itkPathBasePython.itkPathDCID33_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPathDCID33

        Create a new object of the class itkPathDCID33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathDCID33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPathDCID33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPathDCID33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPathDCID33.StartOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID33_StartOfInput, None, itkPathDCID33)
itkPathDCID33.EndOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID33_EndOfInput, None, itkPathDCID33)
itkPathDCID33.Evaluate = new_instancemethod(_itkPathBasePython.itkPathDCID33_Evaluate, None, itkPathDCID33)
itkPathDCID33.EvaluateToIndex = new_instancemethod(_itkPathBasePython.itkPathDCID33_EvaluateToIndex, None, itkPathDCID33)
itkPathDCID33.IncrementInput = new_instancemethod(_itkPathBasePython.itkPathDCID33_IncrementInput, None, itkPathDCID33)
itkPathDCID33.GetPointer = new_instancemethod(_itkPathBasePython.itkPathDCID33_GetPointer, None, itkPathDCID33)
itkPathDCID33_swigregister = _itkPathBasePython.itkPathDCID33_swigregister
itkPathDCID33_swigregister(itkPathDCID33)

def itkPathDCID33_cast(obj: 'itkLightObject') -> "itkPathDCID33 *":
    """itkPathDCID33_cast(itkLightObject obj) -> itkPathDCID33"""
    return _itkPathBasePython.itkPathDCID33_cast(obj)



