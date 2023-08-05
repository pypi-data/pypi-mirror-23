# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRegularStepGradientDescentOptimizerv4Python.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRegularStepGradientDescentOptimizerv4Python')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRegularStepGradientDescentOptimizerv4Python')
    _itkRegularStepGradientDescentOptimizerv4Python = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRegularStepGradientDescentOptimizerv4Python', [dirname(__file__)])
        except ImportError:
            import _itkRegularStepGradientDescentOptimizerv4Python
            return _itkRegularStepGradientDescentOptimizerv4Python
        try:
            _mod = imp.load_module('_itkRegularStepGradientDescentOptimizerv4Python', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRegularStepGradientDescentOptimizerv4Python = swig_import_helper()
    del swig_import_helper
else:
    import _itkRegularStepGradientDescentOptimizerv4Python
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


import itkGradientDescentOptimizerv4Python
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkGradientDescentOptimizerBasev4Python
import itkObjectToObjectOptimizerBasePython
import itkOptimizerParameterScalesEstimatorPython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkObjectToObjectMetricBasePython
import itkSingleValuedCostFunctionv4Python
import itkCostFunctionPython

def itkRegularStepGradientDescentOptimizerv4F_New():
  return itkRegularStepGradientDescentOptimizerv4F.New()


def itkRegularStepGradientDescentOptimizerv4D_New():
  return itkRegularStepGradientDescentOptimizerv4D.New()

class itkRegularStepGradientDescentOptimizerv4D(itkGradientDescentOptimizerv4Python.itkGradientDescentOptimizerv4TemplateD):
    """Proxy of C++ itkRegularStepGradientDescentOptimizerv4D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRegularStepGradientDescentOptimizerv4D_Pointer":
        """__New_orig__() -> itkRegularStepGradientDescentOptimizerv4D_Pointer"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRegularStepGradientDescentOptimizerv4D_Pointer":
        """Clone(itkRegularStepGradientDescentOptimizerv4D self) -> itkRegularStepGradientDescentOptimizerv4D_Pointer"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_Clone(self)


    def SetMinimumStepLength(self, _arg: 'double const') -> "void":
        """SetMinimumStepLength(itkRegularStepGradientDescentOptimizerv4D self, double const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetMinimumStepLength(self, _arg)


    def GetMinimumStepLength(self) -> "double const &":
        """GetMinimumStepLength(itkRegularStepGradientDescentOptimizerv4D self) -> double const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetMinimumStepLength(self)


    def SetRelaxationFactor(self, _arg: 'double const') -> "void":
        """SetRelaxationFactor(itkRegularStepGradientDescentOptimizerv4D self, double const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetRelaxationFactor(self, _arg)


    def GetRelaxationFactor(self) -> "double const &":
        """GetRelaxationFactor(itkRegularStepGradientDescentOptimizerv4D self) -> double const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetRelaxationFactor(self)


    def SetGradientMagnitudeTolerance(self, _arg: 'double const') -> "void":
        """SetGradientMagnitudeTolerance(itkRegularStepGradientDescentOptimizerv4D self, double const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetGradientMagnitudeTolerance(self, _arg)


    def GetGradientMagnitudeTolerance(self) -> "double const &":
        """GetGradientMagnitudeTolerance(itkRegularStepGradientDescentOptimizerv4D self) -> double const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetGradientMagnitudeTolerance(self)


    def SetCurrentLearningRateRelaxation(self, _arg: 'double const') -> "void":
        """SetCurrentLearningRateRelaxation(itkRegularStepGradientDescentOptimizerv4D self, double const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetCurrentLearningRateRelaxation(self, _arg)


    def GetCurrentLearningRateRelaxation(self) -> "double const &":
        """GetCurrentLearningRateRelaxation(itkRegularStepGradientDescentOptimizerv4D self) -> double const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetCurrentLearningRateRelaxation(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkRegularStepGradientDescentOptimizerv4D self, bool doOnlyInitialization=False)
        StartOptimization(itkRegularStepGradientDescentOptimizerv4D self)
        """
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_StartOptimization(self, doOnlyInitialization)


    def GetCurrentStepLength(self) -> "double":
        """GetCurrentStepLength(itkRegularStepGradientDescentOptimizerv4D self) -> double"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetCurrentStepLength(self)

    __swig_destroy__ = _itkRegularStepGradientDescentOptimizerv4Python.delete_itkRegularStepGradientDescentOptimizerv4D

    def cast(obj: 'itkLightObject') -> "itkRegularStepGradientDescentOptimizerv4D *":
        """cast(itkLightObject obj) -> itkRegularStepGradientDescentOptimizerv4D"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRegularStepGradientDescentOptimizerv4D *":
        """GetPointer(itkRegularStepGradientDescentOptimizerv4D self) -> itkRegularStepGradientDescentOptimizerv4D"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRegularStepGradientDescentOptimizerv4D

        Create a new object of the class itkRegularStepGradientDescentOptimizerv4D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularStepGradientDescentOptimizerv4D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRegularStepGradientDescentOptimizerv4D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRegularStepGradientDescentOptimizerv4D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRegularStepGradientDescentOptimizerv4D.Clone = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_Clone, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.SetMinimumStepLength = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetMinimumStepLength, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.GetMinimumStepLength = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetMinimumStepLength, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.SetRelaxationFactor = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetRelaxationFactor, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.GetRelaxationFactor = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetRelaxationFactor, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.SetGradientMagnitudeTolerance = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetGradientMagnitudeTolerance, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.GetGradientMagnitudeTolerance = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetGradientMagnitudeTolerance, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.SetCurrentLearningRateRelaxation = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_SetCurrentLearningRateRelaxation, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.GetCurrentLearningRateRelaxation = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetCurrentLearningRateRelaxation, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.StartOptimization = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_StartOptimization, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.GetCurrentStepLength = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetCurrentStepLength, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D.GetPointer = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_GetPointer, None, itkRegularStepGradientDescentOptimizerv4D)
itkRegularStepGradientDescentOptimizerv4D_swigregister = _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_swigregister
itkRegularStepGradientDescentOptimizerv4D_swigregister(itkRegularStepGradientDescentOptimizerv4D)

def itkRegularStepGradientDescentOptimizerv4D___New_orig__() -> "itkRegularStepGradientDescentOptimizerv4D_Pointer":
    """itkRegularStepGradientDescentOptimizerv4D___New_orig__() -> itkRegularStepGradientDescentOptimizerv4D_Pointer"""
    return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D___New_orig__()

def itkRegularStepGradientDescentOptimizerv4D_cast(obj: 'itkLightObject') -> "itkRegularStepGradientDescentOptimizerv4D *":
    """itkRegularStepGradientDescentOptimizerv4D_cast(itkLightObject obj) -> itkRegularStepGradientDescentOptimizerv4D"""
    return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4D_cast(obj)

class itkRegularStepGradientDescentOptimizerv4F(itkGradientDescentOptimizerv4Python.itkGradientDescentOptimizerv4TemplateF):
    """Proxy of C++ itkRegularStepGradientDescentOptimizerv4F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRegularStepGradientDescentOptimizerv4F_Pointer":
        """__New_orig__() -> itkRegularStepGradientDescentOptimizerv4F_Pointer"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRegularStepGradientDescentOptimizerv4F_Pointer":
        """Clone(itkRegularStepGradientDescentOptimizerv4F self) -> itkRegularStepGradientDescentOptimizerv4F_Pointer"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_Clone(self)


    def SetMinimumStepLength(self, _arg: 'float const') -> "void":
        """SetMinimumStepLength(itkRegularStepGradientDescentOptimizerv4F self, float const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetMinimumStepLength(self, _arg)


    def GetMinimumStepLength(self) -> "float const &":
        """GetMinimumStepLength(itkRegularStepGradientDescentOptimizerv4F self) -> float const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetMinimumStepLength(self)


    def SetRelaxationFactor(self, _arg: 'float const') -> "void":
        """SetRelaxationFactor(itkRegularStepGradientDescentOptimizerv4F self, float const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetRelaxationFactor(self, _arg)


    def GetRelaxationFactor(self) -> "float const &":
        """GetRelaxationFactor(itkRegularStepGradientDescentOptimizerv4F self) -> float const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetRelaxationFactor(self)


    def SetGradientMagnitudeTolerance(self, _arg: 'float const') -> "void":
        """SetGradientMagnitudeTolerance(itkRegularStepGradientDescentOptimizerv4F self, float const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetGradientMagnitudeTolerance(self, _arg)


    def GetGradientMagnitudeTolerance(self) -> "float const &":
        """GetGradientMagnitudeTolerance(itkRegularStepGradientDescentOptimizerv4F self) -> float const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetGradientMagnitudeTolerance(self)


    def SetCurrentLearningRateRelaxation(self, _arg: 'float const') -> "void":
        """SetCurrentLearningRateRelaxation(itkRegularStepGradientDescentOptimizerv4F self, float const _arg)"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetCurrentLearningRateRelaxation(self, _arg)


    def GetCurrentLearningRateRelaxation(self) -> "float const &":
        """GetCurrentLearningRateRelaxation(itkRegularStepGradientDescentOptimizerv4F self) -> float const &"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetCurrentLearningRateRelaxation(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkRegularStepGradientDescentOptimizerv4F self, bool doOnlyInitialization=False)
        StartOptimization(itkRegularStepGradientDescentOptimizerv4F self)
        """
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_StartOptimization(self, doOnlyInitialization)


    def GetCurrentStepLength(self) -> "double":
        """GetCurrentStepLength(itkRegularStepGradientDescentOptimizerv4F self) -> double"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetCurrentStepLength(self)

    __swig_destroy__ = _itkRegularStepGradientDescentOptimizerv4Python.delete_itkRegularStepGradientDescentOptimizerv4F

    def cast(obj: 'itkLightObject') -> "itkRegularStepGradientDescentOptimizerv4F *":
        """cast(itkLightObject obj) -> itkRegularStepGradientDescentOptimizerv4F"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRegularStepGradientDescentOptimizerv4F *":
        """GetPointer(itkRegularStepGradientDescentOptimizerv4F self) -> itkRegularStepGradientDescentOptimizerv4F"""
        return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRegularStepGradientDescentOptimizerv4F

        Create a new object of the class itkRegularStepGradientDescentOptimizerv4F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularStepGradientDescentOptimizerv4F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRegularStepGradientDescentOptimizerv4F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRegularStepGradientDescentOptimizerv4F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRegularStepGradientDescentOptimizerv4F.Clone = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_Clone, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.SetMinimumStepLength = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetMinimumStepLength, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.GetMinimumStepLength = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetMinimumStepLength, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.SetRelaxationFactor = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetRelaxationFactor, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.GetRelaxationFactor = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetRelaxationFactor, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.SetGradientMagnitudeTolerance = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetGradientMagnitudeTolerance, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.GetGradientMagnitudeTolerance = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetGradientMagnitudeTolerance, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.SetCurrentLearningRateRelaxation = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_SetCurrentLearningRateRelaxation, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.GetCurrentLearningRateRelaxation = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetCurrentLearningRateRelaxation, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.StartOptimization = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_StartOptimization, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.GetCurrentStepLength = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetCurrentStepLength, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F.GetPointer = new_instancemethod(_itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_GetPointer, None, itkRegularStepGradientDescentOptimizerv4F)
itkRegularStepGradientDescentOptimizerv4F_swigregister = _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_swigregister
itkRegularStepGradientDescentOptimizerv4F_swigregister(itkRegularStepGradientDescentOptimizerv4F)

def itkRegularStepGradientDescentOptimizerv4F___New_orig__() -> "itkRegularStepGradientDescentOptimizerv4F_Pointer":
    """itkRegularStepGradientDescentOptimizerv4F___New_orig__() -> itkRegularStepGradientDescentOptimizerv4F_Pointer"""
    return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F___New_orig__()

def itkRegularStepGradientDescentOptimizerv4F_cast(obj: 'itkLightObject') -> "itkRegularStepGradientDescentOptimizerv4F *":
    """itkRegularStepGradientDescentOptimizerv4F_cast(itkLightObject obj) -> itkRegularStepGradientDescentOptimizerv4F"""
    return _itkRegularStepGradientDescentOptimizerv4Python.itkRegularStepGradientDescentOptimizerv4F_cast(obj)



