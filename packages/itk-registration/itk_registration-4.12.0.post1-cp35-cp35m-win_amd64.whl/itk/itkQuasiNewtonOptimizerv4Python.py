# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkQuasiNewtonOptimizerv4Python.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkQuasiNewtonOptimizerv4Python')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkQuasiNewtonOptimizerv4Python')
    _itkQuasiNewtonOptimizerv4Python = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkQuasiNewtonOptimizerv4Python', [dirname(__file__)])
        except ImportError:
            import _itkQuasiNewtonOptimizerv4Python
            return _itkQuasiNewtonOptimizerv4Python
        try:
            _mod = imp.load_module('_itkQuasiNewtonOptimizerv4Python', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkQuasiNewtonOptimizerv4Python = swig_import_helper()
    del swig_import_helper
else:
    import _itkQuasiNewtonOptimizerv4Python
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


import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import itkGradientDescentOptimizerv4Python
import ITKCommonBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkGradientDescentOptimizerBasev4Python
import itkObjectToObjectOptimizerBasePython
import itkOptimizerParametersPython
import itkOptimizerParameterScalesEstimatorPython
import itkObjectToObjectMetricBasePython
import itkSingleValuedCostFunctionv4Python
import itkCostFunctionPython

def itkQuasiNewtonOptimizerv4TemplateF_New():
  return itkQuasiNewtonOptimizerv4TemplateF.New()

class itkQuasiNewtonOptimizerv4TemplateF(itkGradientDescentOptimizerv4Python.itkGradientDescentOptimizerv4TemplateF):
    """Proxy of C++ itkQuasiNewtonOptimizerv4TemplateF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkQuasiNewtonOptimizerv4TemplateF_Pointer":
        """__New_orig__() -> itkQuasiNewtonOptimizerv4TemplateF_Pointer"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkQuasiNewtonOptimizerv4TemplateF_Pointer":
        """Clone(itkQuasiNewtonOptimizerv4TemplateF self) -> itkQuasiNewtonOptimizerv4TemplateF_Pointer"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_Clone(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkQuasiNewtonOptimizerv4TemplateF self, bool doOnlyInitialization=False)
        StartOptimization(itkQuasiNewtonOptimizerv4TemplateF self)
        """
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_StartOptimization(self, doOnlyInitialization)


    def SetMaximumIterationsWithoutProgress(self, _arg: 'unsigned long long const') -> "void":
        """SetMaximumIterationsWithoutProgress(itkQuasiNewtonOptimizerv4TemplateF self, unsigned long long const _arg)"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_SetMaximumIterationsWithoutProgress(self, _arg)


    def SetMaximumNewtonStepSizeInPhysicalUnits(self, _arg: 'float const') -> "void":
        """SetMaximumNewtonStepSizeInPhysicalUnits(itkQuasiNewtonOptimizerv4TemplateF self, float const _arg)"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_SetMaximumNewtonStepSizeInPhysicalUnits(self, _arg)


    def GetNewtonStep(self) -> "itkArrayF const &":
        """GetNewtonStep(itkQuasiNewtonOptimizerv4TemplateF self) -> itkArrayF"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_GetNewtonStep(self)


    def EstimateNewtonStepOverSubRange(self, subrange: 'itkIndex2') -> "void":
        """EstimateNewtonStepOverSubRange(itkQuasiNewtonOptimizerv4TemplateF self, itkIndex2 subrange)"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_EstimateNewtonStepOverSubRange(self, subrange)

    __swig_destroy__ = _itkQuasiNewtonOptimizerv4Python.delete_itkQuasiNewtonOptimizerv4TemplateF

    def cast(obj: 'itkLightObject') -> "itkQuasiNewtonOptimizerv4TemplateF *":
        """cast(itkLightObject obj) -> itkQuasiNewtonOptimizerv4TemplateF"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkQuasiNewtonOptimizerv4TemplateF *":
        """GetPointer(itkQuasiNewtonOptimizerv4TemplateF self) -> itkQuasiNewtonOptimizerv4TemplateF"""
        return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkQuasiNewtonOptimizerv4TemplateF

        Create a new object of the class itkQuasiNewtonOptimizerv4TemplateF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkQuasiNewtonOptimizerv4TemplateF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkQuasiNewtonOptimizerv4TemplateF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkQuasiNewtonOptimizerv4TemplateF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkQuasiNewtonOptimizerv4TemplateF.Clone = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_Clone, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF.StartOptimization = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_StartOptimization, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF.SetMaximumIterationsWithoutProgress = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_SetMaximumIterationsWithoutProgress, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF.SetMaximumNewtonStepSizeInPhysicalUnits = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_SetMaximumNewtonStepSizeInPhysicalUnits, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF.GetNewtonStep = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_GetNewtonStep, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF.EstimateNewtonStepOverSubRange = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_EstimateNewtonStepOverSubRange, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF.GetPointer = new_instancemethod(_itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_GetPointer, None, itkQuasiNewtonOptimizerv4TemplateF)
itkQuasiNewtonOptimizerv4TemplateF_swigregister = _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_swigregister
itkQuasiNewtonOptimizerv4TemplateF_swigregister(itkQuasiNewtonOptimizerv4TemplateF)

def itkQuasiNewtonOptimizerv4TemplateF___New_orig__() -> "itkQuasiNewtonOptimizerv4TemplateF_Pointer":
    """itkQuasiNewtonOptimizerv4TemplateF___New_orig__() -> itkQuasiNewtonOptimizerv4TemplateF_Pointer"""
    return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF___New_orig__()

def itkQuasiNewtonOptimizerv4TemplateF_cast(obj: 'itkLightObject') -> "itkQuasiNewtonOptimizerv4TemplateF *":
    """itkQuasiNewtonOptimizerv4TemplateF_cast(itkLightObject obj) -> itkQuasiNewtonOptimizerv4TemplateF"""
    return _itkQuasiNewtonOptimizerv4Python.itkQuasiNewtonOptimizerv4TemplateF_cast(obj)



