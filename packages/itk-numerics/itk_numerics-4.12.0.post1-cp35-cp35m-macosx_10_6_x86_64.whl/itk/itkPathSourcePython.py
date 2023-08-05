# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPathSourcePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPathSourcePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPathSourcePython')
    _itkPathSourcePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPathSourcePython', [dirname(__file__)])
        except ImportError:
            import _itkPathSourcePython
            return _itkPathSourcePython
        try:
            _mod = imp.load_module('_itkPathSourcePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPathSourcePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPathSourcePython
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
import itkPolyLineParametricPathPython
import itkContinuousIndexPython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkParametricPathPython
import itkPathBasePython
import itkVectorContainerPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython

def itkPathSourcePLPP3_New():
  return itkPathSourcePLPP3.New()


def itkPathSourcePLPP2_New():
  return itkPathSourcePLPP2.New()

class itkPathSourcePLPP2(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkPathSourcePLPP2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPathSourcePLPP2_Pointer":
        """__New_orig__() -> itkPathSourcePLPP2_Pointer"""
        return _itkPathSourcePython.itkPathSourcePLPP2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPathSourcePLPP2_Pointer":
        """Clone(itkPathSourcePLPP2 self) -> itkPathSourcePLPP2_Pointer"""
        return _itkPathSourcePython.itkPathSourcePLPP2_Clone(self)


    def GetOutput(self, *args) -> "itkPolyLineParametricPath2 *":
        """
        GetOutput(itkPathSourcePLPP2 self) -> itkPolyLineParametricPath2
        GetOutput(itkPathSourcePLPP2 self, unsigned int idx) -> itkPolyLineParametricPath2
        """
        return _itkPathSourcePython.itkPathSourcePLPP2_GetOutput(self, *args)


    def GraftOutput(self, output: 'itkPolyLineParametricPath2') -> "void":
        """GraftOutput(itkPathSourcePLPP2 self, itkPolyLineParametricPath2 output)"""
        return _itkPathSourcePython.itkPathSourcePLPP2_GraftOutput(self, output)


    def GraftNthOutput(self, idx: 'unsigned int', output: 'itkPolyLineParametricPath2') -> "void":
        """GraftNthOutput(itkPathSourcePLPP2 self, unsigned int idx, itkPolyLineParametricPath2 output)"""
        return _itkPathSourcePython.itkPathSourcePLPP2_GraftNthOutput(self, idx, output)

    __swig_destroy__ = _itkPathSourcePython.delete_itkPathSourcePLPP2

    def cast(obj: 'itkLightObject') -> "itkPathSourcePLPP2 *":
        """cast(itkLightObject obj) -> itkPathSourcePLPP2"""
        return _itkPathSourcePython.itkPathSourcePLPP2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPathSourcePLPP2 *":
        """GetPointer(itkPathSourcePLPP2 self) -> itkPathSourcePLPP2"""
        return _itkPathSourcePython.itkPathSourcePLPP2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPathSourcePLPP2

        Create a new object of the class itkPathSourcePLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathSourcePLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPathSourcePLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPathSourcePLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPathSourcePLPP2.Clone = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP2_Clone, None, itkPathSourcePLPP2)
itkPathSourcePLPP2.GetOutput = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP2_GetOutput, None, itkPathSourcePLPP2)
itkPathSourcePLPP2.GraftOutput = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP2_GraftOutput, None, itkPathSourcePLPP2)
itkPathSourcePLPP2.GraftNthOutput = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP2_GraftNthOutput, None, itkPathSourcePLPP2)
itkPathSourcePLPP2.GetPointer = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP2_GetPointer, None, itkPathSourcePLPP2)
itkPathSourcePLPP2_swigregister = _itkPathSourcePython.itkPathSourcePLPP2_swigregister
itkPathSourcePLPP2_swigregister(itkPathSourcePLPP2)

def itkPathSourcePLPP2___New_orig__() -> "itkPathSourcePLPP2_Pointer":
    """itkPathSourcePLPP2___New_orig__() -> itkPathSourcePLPP2_Pointer"""
    return _itkPathSourcePython.itkPathSourcePLPP2___New_orig__()

def itkPathSourcePLPP2_cast(obj: 'itkLightObject') -> "itkPathSourcePLPP2 *":
    """itkPathSourcePLPP2_cast(itkLightObject obj) -> itkPathSourcePLPP2"""
    return _itkPathSourcePython.itkPathSourcePLPP2_cast(obj)

class itkPathSourcePLPP3(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkPathSourcePLPP3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPathSourcePLPP3_Pointer":
        """__New_orig__() -> itkPathSourcePLPP3_Pointer"""
        return _itkPathSourcePython.itkPathSourcePLPP3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPathSourcePLPP3_Pointer":
        """Clone(itkPathSourcePLPP3 self) -> itkPathSourcePLPP3_Pointer"""
        return _itkPathSourcePython.itkPathSourcePLPP3_Clone(self)


    def GetOutput(self, *args) -> "itkPolyLineParametricPath3 *":
        """
        GetOutput(itkPathSourcePLPP3 self) -> itkPolyLineParametricPath3
        GetOutput(itkPathSourcePLPP3 self, unsigned int idx) -> itkPolyLineParametricPath3
        """
        return _itkPathSourcePython.itkPathSourcePLPP3_GetOutput(self, *args)


    def GraftOutput(self, output: 'itkPolyLineParametricPath3') -> "void":
        """GraftOutput(itkPathSourcePLPP3 self, itkPolyLineParametricPath3 output)"""
        return _itkPathSourcePython.itkPathSourcePLPP3_GraftOutput(self, output)


    def GraftNthOutput(self, idx: 'unsigned int', output: 'itkPolyLineParametricPath3') -> "void":
        """GraftNthOutput(itkPathSourcePLPP3 self, unsigned int idx, itkPolyLineParametricPath3 output)"""
        return _itkPathSourcePython.itkPathSourcePLPP3_GraftNthOutput(self, idx, output)

    __swig_destroy__ = _itkPathSourcePython.delete_itkPathSourcePLPP3

    def cast(obj: 'itkLightObject') -> "itkPathSourcePLPP3 *":
        """cast(itkLightObject obj) -> itkPathSourcePLPP3"""
        return _itkPathSourcePython.itkPathSourcePLPP3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkPathSourcePLPP3 *":
        """GetPointer(itkPathSourcePLPP3 self) -> itkPathSourcePLPP3"""
        return _itkPathSourcePython.itkPathSourcePLPP3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPathSourcePLPP3

        Create a new object of the class itkPathSourcePLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathSourcePLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPathSourcePLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPathSourcePLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPathSourcePLPP3.Clone = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP3_Clone, None, itkPathSourcePLPP3)
itkPathSourcePLPP3.GetOutput = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP3_GetOutput, None, itkPathSourcePLPP3)
itkPathSourcePLPP3.GraftOutput = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP3_GraftOutput, None, itkPathSourcePLPP3)
itkPathSourcePLPP3.GraftNthOutput = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP3_GraftNthOutput, None, itkPathSourcePLPP3)
itkPathSourcePLPP3.GetPointer = new_instancemethod(_itkPathSourcePython.itkPathSourcePLPP3_GetPointer, None, itkPathSourcePLPP3)
itkPathSourcePLPP3_swigregister = _itkPathSourcePython.itkPathSourcePLPP3_swigregister
itkPathSourcePLPP3_swigregister(itkPathSourcePLPP3)

def itkPathSourcePLPP3___New_orig__() -> "itkPathSourcePLPP3_Pointer":
    """itkPathSourcePLPP3___New_orig__() -> itkPathSourcePLPP3_Pointer"""
    return _itkPathSourcePython.itkPathSourcePLPP3___New_orig__()

def itkPathSourcePLPP3_cast(obj: 'itkLightObject') -> "itkPathSourcePLPP3 *":
    """itkPathSourcePLPP3_cast(itkLightObject obj) -> itkPathSourcePLPP3"""
    return _itkPathSourcePython.itkPathSourcePLPP3_cast(obj)



