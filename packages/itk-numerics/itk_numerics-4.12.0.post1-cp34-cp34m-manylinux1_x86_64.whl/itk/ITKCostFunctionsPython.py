# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ITKCostFunctionsPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ITKCostFunctionsPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ITKCostFunctionsPython')
    _ITKCostFunctionsPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ITKCostFunctionsPython', [dirname(__file__)])
        except ImportError:
            import _ITKCostFunctionsPython
            return _ITKCostFunctionsPython
        try:
            _mod = imp.load_module('_ITKCostFunctionsPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ITKCostFunctionsPython = swig_import_helper()
    del swig_import_helper
else:
    import _ITKCostFunctionsPython
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


import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_cost_functionPython
import vnl_unary_functionPython
import itkCostFunctionPython
import ITKCommonBasePython
import itkArray2DPython
import itkArrayPython
import vnl_least_squares_functionPython
import itkOptimizerParametersPython

def itkCumulativeGaussianCostFunction_New():
  return itkCumulativeGaussianCostFunction.New()


def itkMultipleValuedCostFunction_New():
  return itkMultipleValuedCostFunction.New()


def itkSingleValuedCostFunction_New():
  return itkSingleValuedCostFunction.New()

class itkMultipleValuedCostFunction(itkCostFunctionPython.itkCostFunctionTemplateD):
    """Proxy of C++ itkMultipleValuedCostFunction class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetValue(self, parameters: 'itkOptimizerParametersD') -> "itkArrayD":
        """GetValue(itkMultipleValuedCostFunction self, itkOptimizerParametersD parameters) -> itkArrayD"""
        return _ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetValue(self, parameters)


    def GetNumberOfValues(self) -> "unsigned int":
        """GetNumberOfValues(itkMultipleValuedCostFunction self) -> unsigned int"""
        return _ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetNumberOfValues(self)


    def GetDerivative(self, parameters: 'itkOptimizerParametersD', derivative: 'itkArray2DD') -> "void":
        """GetDerivative(itkMultipleValuedCostFunction self, itkOptimizerParametersD parameters, itkArray2DD derivative)"""
        return _ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetDerivative(self, parameters, derivative)

    __swig_destroy__ = _ITKCostFunctionsPython.delete_itkMultipleValuedCostFunction

    def cast(obj: 'itkLightObject') -> "itkMultipleValuedCostFunction *":
        """cast(itkLightObject obj) -> itkMultipleValuedCostFunction"""
        return _ITKCostFunctionsPython.itkMultipleValuedCostFunction_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMultipleValuedCostFunction *":
        """GetPointer(itkMultipleValuedCostFunction self) -> itkMultipleValuedCostFunction"""
        return _ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMultipleValuedCostFunction

        Create a new object of the class itkMultipleValuedCostFunction and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultipleValuedCostFunction.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultipleValuedCostFunction.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultipleValuedCostFunction.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMultipleValuedCostFunction.GetValue = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetValue, None, itkMultipleValuedCostFunction)
itkMultipleValuedCostFunction.GetNumberOfValues = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetNumberOfValues, None, itkMultipleValuedCostFunction)
itkMultipleValuedCostFunction.GetDerivative = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetDerivative, None, itkMultipleValuedCostFunction)
itkMultipleValuedCostFunction.GetPointer = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedCostFunction_GetPointer, None, itkMultipleValuedCostFunction)
itkMultipleValuedCostFunction_swigregister = _ITKCostFunctionsPython.itkMultipleValuedCostFunction_swigregister
itkMultipleValuedCostFunction_swigregister(itkMultipleValuedCostFunction)

def itkMultipleValuedCostFunction_cast(obj: 'itkLightObject') -> "itkMultipleValuedCostFunction *":
    """itkMultipleValuedCostFunction_cast(itkLightObject obj) -> itkMultipleValuedCostFunction"""
    return _ITKCostFunctionsPython.itkMultipleValuedCostFunction_cast(obj)

class itkMultipleValuedVnlCostFunctionAdaptor(vnl_least_squares_functionPython.vnl_least_squares_function):
    """Proxy of C++ itkMultipleValuedVnlCostFunctionAdaptor class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetCostFunction(self, costFunction: 'itkMultipleValuedCostFunction') -> "void":
        """SetCostFunction(itkMultipleValuedVnlCostFunctionAdaptor self, itkMultipleValuedCostFunction costFunction)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_SetCostFunction(self, costFunction)


    def GetCostFunction(self) -> "itkMultipleValuedCostFunction const *":
        """GetCostFunction(itkMultipleValuedVnlCostFunctionAdaptor self) -> itkMultipleValuedCostFunction"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCostFunction(self)


    def compute(self, x: 'vnl_vectorD', f: 'vnl_vectorD', g: 'vnl_matrixD') -> "void":
        """compute(itkMultipleValuedVnlCostFunctionAdaptor self, vnl_vectorD x, vnl_vectorD f, vnl_matrixD g)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_compute(self, x, f, g)


    def ConvertExternalToInternalGradient(self, input: 'itkArray2DD', output: 'vnl_matrixD') -> "void":
        """ConvertExternalToInternalGradient(itkMultipleValuedVnlCostFunctionAdaptor self, itkArray2DD input, vnl_matrixD output)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_ConvertExternalToInternalGradient(self, input, output)


    def ConvertExternalToInternalMeasures(self, input: 'itkArrayD', output: 'vnl_vectorD') -> "void":
        """ConvertExternalToInternalMeasures(itkMultipleValuedVnlCostFunctionAdaptor self, itkArrayD input, vnl_vectorD output)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_ConvertExternalToInternalMeasures(self, input, output)


    def SetUseGradient(self, arg0: 'bool') -> "void":
        """SetUseGradient(itkMultipleValuedVnlCostFunctionAdaptor self, bool arg0)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_SetUseGradient(self, arg0)


    def UseGradientOn(self) -> "void":
        """UseGradientOn(itkMultipleValuedVnlCostFunctionAdaptor self)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_UseGradientOn(self)


    def UseGradientOff(self) -> "void":
        """UseGradientOff(itkMultipleValuedVnlCostFunctionAdaptor self)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_UseGradientOff(self)


    def GetUseGradient(self) -> "bool":
        """GetUseGradient(itkMultipleValuedVnlCostFunctionAdaptor self) -> bool"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetUseGradient(self)


    def SetScales(self, scales: 'itkArrayD') -> "void":
        """SetScales(itkMultipleValuedVnlCostFunctionAdaptor self, itkArrayD scales)"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_SetScales(self, scales)


    def AddObserver(self, event: 'itkEventObject', arg1: 'itkCommand') -> "unsigned long":
        """AddObserver(itkMultipleValuedVnlCostFunctionAdaptor self, itkEventObject event, itkCommand arg1) -> unsigned long"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_AddObserver(self, event, arg1)


    def GetCachedValue(self) -> "itkArrayD const &":
        """GetCachedValue(itkMultipleValuedVnlCostFunctionAdaptor self) -> itkArrayD"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCachedValue(self)


    def GetCachedDerivative(self) -> "itkArray2DD const &":
        """GetCachedDerivative(itkMultipleValuedVnlCostFunctionAdaptor self) -> itkArray2DD"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCachedDerivative(self)


    def GetCachedCurrentParameters(self) -> "itkOptimizerParametersD const &":
        """GetCachedCurrentParameters(itkMultipleValuedVnlCostFunctionAdaptor self) -> itkOptimizerParametersD"""
        return _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCachedCurrentParameters(self)


    def __init__(self, *args):
        """
        __init__(itkMultipleValuedVnlCostFunctionAdaptor self, unsigned int spaceDimension, unsigned int numberOfValues) -> itkMultipleValuedVnlCostFunctionAdaptor
        __init__(itkMultipleValuedVnlCostFunctionAdaptor self, itkMultipleValuedVnlCostFunctionAdaptor arg0) -> itkMultipleValuedVnlCostFunctionAdaptor
        """
        _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_swiginit(self, _ITKCostFunctionsPython.new_itkMultipleValuedVnlCostFunctionAdaptor(*args))
    __swig_destroy__ = _ITKCostFunctionsPython.delete_itkMultipleValuedVnlCostFunctionAdaptor
itkMultipleValuedVnlCostFunctionAdaptor.SetCostFunction = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_SetCostFunction, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.GetCostFunction = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCostFunction, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.compute = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_compute, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.ConvertExternalToInternalGradient = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_ConvertExternalToInternalGradient, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.ConvertExternalToInternalMeasures = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_ConvertExternalToInternalMeasures, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.SetUseGradient = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_SetUseGradient, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.UseGradientOn = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_UseGradientOn, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.UseGradientOff = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_UseGradientOff, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.GetUseGradient = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetUseGradient, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.SetScales = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_SetScales, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.AddObserver = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_AddObserver, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.GetCachedValue = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCachedValue, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.GetCachedDerivative = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCachedDerivative, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor.GetCachedCurrentParameters = new_instancemethod(_ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_GetCachedCurrentParameters, None, itkMultipleValuedVnlCostFunctionAdaptor)
itkMultipleValuedVnlCostFunctionAdaptor_swigregister = _ITKCostFunctionsPython.itkMultipleValuedVnlCostFunctionAdaptor_swigregister
itkMultipleValuedVnlCostFunctionAdaptor_swigregister(itkMultipleValuedVnlCostFunctionAdaptor)

class itkSingleValuedCostFunction(itkCostFunctionPython.itkCostFunctionTemplateD):
    """Proxy of C++ itkSingleValuedCostFunction class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetValue(self, parameters: 'itkOptimizerParametersD') -> "double":
        """GetValue(itkSingleValuedCostFunction self, itkOptimizerParametersD parameters) -> double"""
        return _ITKCostFunctionsPython.itkSingleValuedCostFunction_GetValue(self, parameters)


    def GetDerivative(self, parameters: 'itkOptimizerParametersD', derivative: 'itkArrayD') -> "void":
        """GetDerivative(itkSingleValuedCostFunction self, itkOptimizerParametersD parameters, itkArrayD derivative)"""
        return _ITKCostFunctionsPython.itkSingleValuedCostFunction_GetDerivative(self, parameters, derivative)


    def GetValueAndDerivative(self, parameters: 'itkOptimizerParametersD', value: 'double &', derivative: 'itkArrayD') -> "void":
        """GetValueAndDerivative(itkSingleValuedCostFunction self, itkOptimizerParametersD parameters, double & value, itkArrayD derivative)"""
        return _ITKCostFunctionsPython.itkSingleValuedCostFunction_GetValueAndDerivative(self, parameters, value, derivative)

    __swig_destroy__ = _ITKCostFunctionsPython.delete_itkSingleValuedCostFunction

    def cast(obj: 'itkLightObject') -> "itkSingleValuedCostFunction *":
        """cast(itkLightObject obj) -> itkSingleValuedCostFunction"""
        return _ITKCostFunctionsPython.itkSingleValuedCostFunction_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSingleValuedCostFunction *":
        """GetPointer(itkSingleValuedCostFunction self) -> itkSingleValuedCostFunction"""
        return _ITKCostFunctionsPython.itkSingleValuedCostFunction_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSingleValuedCostFunction

        Create a new object of the class itkSingleValuedCostFunction and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSingleValuedCostFunction.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSingleValuedCostFunction.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSingleValuedCostFunction.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSingleValuedCostFunction.GetValue = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedCostFunction_GetValue, None, itkSingleValuedCostFunction)
itkSingleValuedCostFunction.GetDerivative = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedCostFunction_GetDerivative, None, itkSingleValuedCostFunction)
itkSingleValuedCostFunction.GetValueAndDerivative = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedCostFunction_GetValueAndDerivative, None, itkSingleValuedCostFunction)
itkSingleValuedCostFunction.GetPointer = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedCostFunction_GetPointer, None, itkSingleValuedCostFunction)
itkSingleValuedCostFunction_swigregister = _ITKCostFunctionsPython.itkSingleValuedCostFunction_swigregister
itkSingleValuedCostFunction_swigregister(itkSingleValuedCostFunction)

def itkSingleValuedCostFunction_cast(obj: 'itkLightObject') -> "itkSingleValuedCostFunction *":
    """itkSingleValuedCostFunction_cast(itkLightObject obj) -> itkSingleValuedCostFunction"""
    return _ITKCostFunctionsPython.itkSingleValuedCostFunction_cast(obj)

class itkSingleValuedVnlCostFunctionAdaptor(vnl_cost_functionPython.vnl_cost_function):
    """Proxy of C++ itkSingleValuedVnlCostFunctionAdaptor class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetCostFunction(self, costFunction: 'itkSingleValuedCostFunction') -> "void":
        """SetCostFunction(itkSingleValuedVnlCostFunctionAdaptor self, itkSingleValuedCostFunction costFunction)"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_SetCostFunction(self, costFunction)


    def GetCostFunction(self) -> "itkSingleValuedCostFunction const *":
        """GetCostFunction(itkSingleValuedVnlCostFunctionAdaptor self) -> itkSingleValuedCostFunction"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCostFunction(self)


    def ConvertExternalToInternalGradient(self, input: 'itkArrayD', output: 'vnl_vectorD') -> "void":
        """ConvertExternalToInternalGradient(itkSingleValuedVnlCostFunctionAdaptor self, itkArrayD input, vnl_vectorD output)"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_ConvertExternalToInternalGradient(self, input, output)


    def SetScales(self, scales: 'itkArrayD') -> "void":
        """SetScales(itkSingleValuedVnlCostFunctionAdaptor self, itkArrayD scales)"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_SetScales(self, scales)


    def SetNegateCostFunction(self, value: 'bool') -> "void":
        """SetNegateCostFunction(itkSingleValuedVnlCostFunctionAdaptor self, bool value)"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_SetNegateCostFunction(self, value)


    def GetNegateCostFunction(self) -> "bool":
        """GetNegateCostFunction(itkSingleValuedVnlCostFunctionAdaptor self) -> bool"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetNegateCostFunction(self)


    def NegateCostFunctionOn(self) -> "void":
        """NegateCostFunctionOn(itkSingleValuedVnlCostFunctionAdaptor self)"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_NegateCostFunctionOn(self)


    def NegateCostFunctionOff(self) -> "void":
        """NegateCostFunctionOff(itkSingleValuedVnlCostFunctionAdaptor self)"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_NegateCostFunctionOff(self)


    def AddObserver(self, event: 'itkEventObject', arg1: 'itkCommand') -> "unsigned long":
        """AddObserver(itkSingleValuedVnlCostFunctionAdaptor self, itkEventObject event, itkCommand arg1) -> unsigned long"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_AddObserver(self, event, arg1)


    def GetCachedValue(self) -> "double const &":
        """GetCachedValue(itkSingleValuedVnlCostFunctionAdaptor self) -> double const &"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCachedValue(self)


    def GetCachedDerivative(self) -> "itkArrayD const &":
        """GetCachedDerivative(itkSingleValuedVnlCostFunctionAdaptor self) -> itkArrayD"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCachedDerivative(self)


    def GetCachedCurrentParameters(self) -> "itkOptimizerParametersD const &":
        """GetCachedCurrentParameters(itkSingleValuedVnlCostFunctionAdaptor self) -> itkOptimizerParametersD"""
        return _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCachedCurrentParameters(self)


    def __init__(self, *args):
        """
        __init__(itkSingleValuedVnlCostFunctionAdaptor self, unsigned int spaceDimension) -> itkSingleValuedVnlCostFunctionAdaptor
        __init__(itkSingleValuedVnlCostFunctionAdaptor self, itkSingleValuedVnlCostFunctionAdaptor arg0) -> itkSingleValuedVnlCostFunctionAdaptor
        """
        _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_swiginit(self, _ITKCostFunctionsPython.new_itkSingleValuedVnlCostFunctionAdaptor(*args))
    __swig_destroy__ = _ITKCostFunctionsPython.delete_itkSingleValuedVnlCostFunctionAdaptor
itkSingleValuedVnlCostFunctionAdaptor.SetCostFunction = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_SetCostFunction, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.GetCostFunction = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCostFunction, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.ConvertExternalToInternalGradient = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_ConvertExternalToInternalGradient, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.SetScales = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_SetScales, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.SetNegateCostFunction = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_SetNegateCostFunction, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.GetNegateCostFunction = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetNegateCostFunction, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.NegateCostFunctionOn = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_NegateCostFunctionOn, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.NegateCostFunctionOff = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_NegateCostFunctionOff, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.AddObserver = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_AddObserver, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.GetCachedValue = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCachedValue, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.GetCachedDerivative = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCachedDerivative, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor.GetCachedCurrentParameters = new_instancemethod(_ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_GetCachedCurrentParameters, None, itkSingleValuedVnlCostFunctionAdaptor)
itkSingleValuedVnlCostFunctionAdaptor_swigregister = _ITKCostFunctionsPython.itkSingleValuedVnlCostFunctionAdaptor_swigregister
itkSingleValuedVnlCostFunctionAdaptor_swigregister(itkSingleValuedVnlCostFunctionAdaptor)

class itkCumulativeGaussianCostFunction(itkMultipleValuedCostFunction):
    """Proxy of C++ itkCumulativeGaussianCostFunction class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCumulativeGaussianCostFunction_Pointer":
        """__New_orig__() -> itkCumulativeGaussianCostFunction_Pointer"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCumulativeGaussianCostFunction_Pointer":
        """Clone(itkCumulativeGaussianCostFunction self) -> itkCumulativeGaussianCostFunction_Pointer"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_Clone(self)

    SpaceDimension = _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_SpaceDimension

    def GetValuePointer(self, parameters: 'itkOptimizerParametersD') -> "itkArrayD *":
        """GetValuePointer(itkCumulativeGaussianCostFunction self, itkOptimizerParametersD parameters) -> itkArrayD"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_GetValuePointer(self, parameters)


    def CalculateFitError(self, setTestArray: 'itkArrayD') -> "double":
        """CalculateFitError(itkCumulativeGaussianCostFunction self, itkArrayD setTestArray) -> double"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_CalculateFitError(self, setTestArray)


    def EvaluateCumulativeGaussian(self, argument: 'double') -> "double":
        """EvaluateCumulativeGaussian(itkCumulativeGaussianCostFunction self, double argument) -> double"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_EvaluateCumulativeGaussian(self, argument)


    def Initialize(self, rangeDimension: 'unsigned int') -> "void":
        """Initialize(itkCumulativeGaussianCostFunction self, unsigned int rangeDimension)"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_Initialize(self, rangeDimension)


    def SetOriginalDataArray(self, setOriginalDataArray: 'itkArrayD') -> "void":
        """SetOriginalDataArray(itkCumulativeGaussianCostFunction self, itkArrayD setOriginalDataArray)"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_SetOriginalDataArray(self, setOriginalDataArray)

    __swig_destroy__ = _ITKCostFunctionsPython.delete_itkCumulativeGaussianCostFunction

    def cast(obj: 'itkLightObject') -> "itkCumulativeGaussianCostFunction *":
        """cast(itkLightObject obj) -> itkCumulativeGaussianCostFunction"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkCumulativeGaussianCostFunction *":
        """GetPointer(itkCumulativeGaussianCostFunction self) -> itkCumulativeGaussianCostFunction"""
        return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCumulativeGaussianCostFunction

        Create a new object of the class itkCumulativeGaussianCostFunction and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCumulativeGaussianCostFunction.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCumulativeGaussianCostFunction.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCumulativeGaussianCostFunction.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCumulativeGaussianCostFunction.Clone = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_Clone, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction.GetValuePointer = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_GetValuePointer, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction.CalculateFitError = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_CalculateFitError, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction.EvaluateCumulativeGaussian = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_EvaluateCumulativeGaussian, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction.Initialize = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_Initialize, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction.SetOriginalDataArray = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_SetOriginalDataArray, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction.GetPointer = new_instancemethod(_ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_GetPointer, None, itkCumulativeGaussianCostFunction)
itkCumulativeGaussianCostFunction_swigregister = _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_swigregister
itkCumulativeGaussianCostFunction_swigregister(itkCumulativeGaussianCostFunction)

def itkCumulativeGaussianCostFunction___New_orig__() -> "itkCumulativeGaussianCostFunction_Pointer":
    """itkCumulativeGaussianCostFunction___New_orig__() -> itkCumulativeGaussianCostFunction_Pointer"""
    return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction___New_orig__()

def itkCumulativeGaussianCostFunction_cast(obj: 'itkLightObject') -> "itkCumulativeGaussianCostFunction *":
    """itkCumulativeGaussianCostFunction_cast(itkLightObject obj) -> itkCumulativeGaussianCostFunction"""
    return _ITKCostFunctionsPython.itkCumulativeGaussianCostFunction_cast(obj)



