# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkObjectToObjectMetricPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkObjectToObjectMetricPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkObjectToObjectMetricPython')
    _itkObjectToObjectMetricPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkObjectToObjectMetricPython', [dirname(__file__)])
        except ImportError:
            import _itkObjectToObjectMetricPython
            return _itkObjectToObjectMetricPython
        try:
            _mod = imp.load_module('_itkObjectToObjectMetricPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkObjectToObjectMetricPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkObjectToObjectMetricPython
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


import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkObjectToObjectMetricBasePython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkArrayPython
import itkSingleValuedCostFunctionv4Python
import itkCostFunctionPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkOffsetPython
import itkSizePython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBAPixelPython
import itkDisplacementFieldTransformPython
import itkArray2DPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython

def itkObjectToObjectMetric33_New():
  return itkObjectToObjectMetric33.New()


def itkObjectToObjectMetric22_New():
  return itkObjectToObjectMetric22.New()

class itkObjectToObjectMetric22(itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD):
    """Proxy of C++ itkObjectToObjectMetric22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetFixedTransform(self, _arg: 'itkTransformD22') -> "void":
        """SetFixedTransform(itkObjectToObjectMetric22 self, itkTransformD22 _arg)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetFixedTransform(self, _arg)


    def GetModifiableFixedTransform(self) -> "itkTransformD22 *":
        """GetModifiableFixedTransform(itkObjectToObjectMetric22 self) -> itkTransformD22"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableFixedTransform(self)


    def GetFixedTransform(self, *args) -> "itkTransformD22 *":
        """
        GetFixedTransform(itkObjectToObjectMetric22 self) -> itkTransformD22
        GetFixedTransform(itkObjectToObjectMetric22 self) -> itkTransformD22
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetFixedTransform(self, *args)


    def SetMovingTransform(self, _arg: 'itkTransformD22') -> "void":
        """SetMovingTransform(itkObjectToObjectMetric22 self, itkTransformD22 _arg)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetMovingTransform(self, _arg)


    def GetModifiableMovingTransform(self) -> "itkTransformD22 *":
        """GetModifiableMovingTransform(itkObjectToObjectMetric22 self) -> itkTransformD22"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableMovingTransform(self)


    def GetMovingTransform(self, *args) -> "itkTransformD22 *":
        """
        GetMovingTransform(itkObjectToObjectMetric22 self) -> itkTransformD22
        GetMovingTransform(itkObjectToObjectMetric22 self) -> itkTransformD22
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetMovingTransform(self, *args)


    def SetTransform(self, transform: 'itkTransformD22') -> "void":
        """SetTransform(itkObjectToObjectMetric22 self, itkTransformD22 transform)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetTransform(self, transform)


    def GetTransform(self) -> "itkTransformD22 const *":
        """GetTransform(itkObjectToObjectMetric22 self) -> itkTransformD22"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetTransform(self)


    def GetNumberOfValidPoints(self) -> "unsigned long":
        """GetNumberOfValidPoints(itkObjectToObjectMetric22 self) -> unsigned long"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetNumberOfValidPoints(self)


    def SetVirtualDomain(self, spacing: 'itkVectorD2', origin: 'itkPointD2', direction: 'itkMatrixD22', region: 'itkImageRegion2') -> "void":
        """SetVirtualDomain(itkObjectToObjectMetric22 self, itkVectorD2 spacing, itkPointD2 origin, itkMatrixD22 direction, itkImageRegion2 region)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetVirtualDomain(self, spacing, origin, direction, region)


    def SetVirtualDomainFromImage(self, virtualImage: 'itkImageD2') -> "void":
        """SetVirtualDomainFromImage(itkObjectToObjectMetric22 self, itkImageD2 virtualImage)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetVirtualDomainFromImage(self, virtualImage)


    def SupportsArbitraryVirtualDomainSamples(self) -> "bool":
        """SupportsArbitraryVirtualDomainSamples(itkObjectToObjectMetric22 self) -> bool"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SupportsArbitraryVirtualDomainSamples(self)


    def GetVirtualDomainTimeStamp(self) -> "itkTimeStamp const &":
        """GetVirtualDomainTimeStamp(itkObjectToObjectMetric22 self) -> itkTimeStamp"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualDomainTimeStamp(self)


    def GetVirtualSpacing(self) -> "itkVectorD2":
        """GetVirtualSpacing(itkObjectToObjectMetric22 self) -> itkVectorD2"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualSpacing(self)


    def GetVirtualOrigin(self) -> "itkPointD2":
        """GetVirtualOrigin(itkObjectToObjectMetric22 self) -> itkPointD2"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualOrigin(self)


    def GetVirtualDirection(self) -> "itkMatrixD22":
        """GetVirtualDirection(itkObjectToObjectMetric22 self) -> itkMatrixD22"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualDirection(self)


    def GetVirtualRegion(self) -> "itkImageRegion2 const &":
        """GetVirtualRegion(itkObjectToObjectMetric22 self) -> itkImageRegion2"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualRegion(self)


    def GetModifiableVirtualImage(self) -> "itkImageD2 *":
        """GetModifiableVirtualImage(itkObjectToObjectMetric22 self) -> itkImageD2"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableVirtualImage(self)


    def GetVirtualImage(self, *args) -> "itkImageD2 *":
        """
        GetVirtualImage(itkObjectToObjectMetric22 self) -> itkImageD2
        GetVirtualImage(itkObjectToObjectMetric22 self) -> itkImageD2
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualImage(self, *args)


    def ComputeParameterOffsetFromVirtualIndex(self, index: 'itkIndex2', numberOfLocalParameters: 'unsigned int const &') -> "long":
        """ComputeParameterOffsetFromVirtualIndex(itkObjectToObjectMetric22 self, itkIndex2 index, unsigned int const & numberOfLocalParameters) -> long"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_ComputeParameterOffsetFromVirtualIndex(self, index, numberOfLocalParameters)


    def ComputeParameterOffsetFromVirtualPoint(self, point: 'itkPointD2', numberOfLocalParameters: 'unsigned int const &') -> "long":
        """ComputeParameterOffsetFromVirtualPoint(itkObjectToObjectMetric22 self, itkPointD2 point, unsigned int const & numberOfLocalParameters) -> long"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_ComputeParameterOffsetFromVirtualPoint(self, point, numberOfLocalParameters)


    def IsInsideVirtualDomain(self, *args) -> "bool":
        """
        IsInsideVirtualDomain(itkObjectToObjectMetric22 self, itkPointD2 point) -> bool
        IsInsideVirtualDomain(itkObjectToObjectMetric22 self, itkIndex2 index) -> bool
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_IsInsideVirtualDomain(self, *args)

    __swig_destroy__ = _itkObjectToObjectMetricPython.delete_itkObjectToObjectMetric22

    def cast(obj: 'itkLightObject') -> "itkObjectToObjectMetric22 *":
        """cast(itkLightObject obj) -> itkObjectToObjectMetric22"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkObjectToObjectMetric22 *":
        """GetPointer(itkObjectToObjectMetric22 self) -> itkObjectToObjectMetric22"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkObjectToObjectMetric22

        Create a new object of the class itkObjectToObjectMetric22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectToObjectMetric22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectToObjectMetric22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectToObjectMetric22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkObjectToObjectMetric22.SetFixedTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetFixedTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetModifiableFixedTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableFixedTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetFixedTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetFixedTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.SetMovingTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetMovingTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetModifiableMovingTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableMovingTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetMovingTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetMovingTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.SetTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetTransform, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetNumberOfValidPoints = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetNumberOfValidPoints, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.SetVirtualDomain = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetVirtualDomain, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.SetVirtualDomainFromImage = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetVirtualDomainFromImage, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.SupportsArbitraryVirtualDomainSamples = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SupportsArbitraryVirtualDomainSamples, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetVirtualDomainTimeStamp = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualDomainTimeStamp, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetVirtualSpacing = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualSpacing, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetVirtualOrigin = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualOrigin, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetVirtualDirection = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualDirection, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetVirtualRegion = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualRegion, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetModifiableVirtualImage = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableVirtualImage, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetVirtualImage = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualImage, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.ComputeParameterOffsetFromVirtualIndex = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_ComputeParameterOffsetFromVirtualIndex, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.ComputeParameterOffsetFromVirtualPoint = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_ComputeParameterOffsetFromVirtualPoint, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.IsInsideVirtualDomain = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_IsInsideVirtualDomain, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22.GetPointer = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetPointer, None, itkObjectToObjectMetric22)
itkObjectToObjectMetric22_swigregister = _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_swigregister
itkObjectToObjectMetric22_swigregister(itkObjectToObjectMetric22)

def itkObjectToObjectMetric22_cast(obj: 'itkLightObject') -> "itkObjectToObjectMetric22 *":
    """itkObjectToObjectMetric22_cast(itkLightObject obj) -> itkObjectToObjectMetric22"""
    return _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_cast(obj)

class itkObjectToObjectMetric33(itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD):
    """Proxy of C++ itkObjectToObjectMetric33 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetFixedTransform(self, _arg: 'itkTransformD33') -> "void":
        """SetFixedTransform(itkObjectToObjectMetric33 self, itkTransformD33 _arg)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetFixedTransform(self, _arg)


    def GetModifiableFixedTransform(self) -> "itkTransformD33 *":
        """GetModifiableFixedTransform(itkObjectToObjectMetric33 self) -> itkTransformD33"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableFixedTransform(self)


    def GetFixedTransform(self, *args) -> "itkTransformD33 *":
        """
        GetFixedTransform(itkObjectToObjectMetric33 self) -> itkTransformD33
        GetFixedTransform(itkObjectToObjectMetric33 self) -> itkTransformD33
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetFixedTransform(self, *args)


    def SetMovingTransform(self, _arg: 'itkTransformD33') -> "void":
        """SetMovingTransform(itkObjectToObjectMetric33 self, itkTransformD33 _arg)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetMovingTransform(self, _arg)


    def GetModifiableMovingTransform(self) -> "itkTransformD33 *":
        """GetModifiableMovingTransform(itkObjectToObjectMetric33 self) -> itkTransformD33"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableMovingTransform(self)


    def GetMovingTransform(self, *args) -> "itkTransformD33 *":
        """
        GetMovingTransform(itkObjectToObjectMetric33 self) -> itkTransformD33
        GetMovingTransform(itkObjectToObjectMetric33 self) -> itkTransformD33
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetMovingTransform(self, *args)


    def SetTransform(self, transform: 'itkTransformD33') -> "void":
        """SetTransform(itkObjectToObjectMetric33 self, itkTransformD33 transform)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetTransform(self, transform)


    def GetTransform(self) -> "itkTransformD33 const *":
        """GetTransform(itkObjectToObjectMetric33 self) -> itkTransformD33"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetTransform(self)


    def GetNumberOfValidPoints(self) -> "unsigned long":
        """GetNumberOfValidPoints(itkObjectToObjectMetric33 self) -> unsigned long"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetNumberOfValidPoints(self)


    def SetVirtualDomain(self, spacing: 'itkVectorD3', origin: 'itkPointD3', direction: 'itkMatrixD33', region: 'itkImageRegion3') -> "void":
        """SetVirtualDomain(itkObjectToObjectMetric33 self, itkVectorD3 spacing, itkPointD3 origin, itkMatrixD33 direction, itkImageRegion3 region)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetVirtualDomain(self, spacing, origin, direction, region)


    def SetVirtualDomainFromImage(self, virtualImage: 'itkImageD3') -> "void":
        """SetVirtualDomainFromImage(itkObjectToObjectMetric33 self, itkImageD3 virtualImage)"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetVirtualDomainFromImage(self, virtualImage)


    def SupportsArbitraryVirtualDomainSamples(self) -> "bool":
        """SupportsArbitraryVirtualDomainSamples(itkObjectToObjectMetric33 self) -> bool"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SupportsArbitraryVirtualDomainSamples(self)


    def GetVirtualDomainTimeStamp(self) -> "itkTimeStamp const &":
        """GetVirtualDomainTimeStamp(itkObjectToObjectMetric33 self) -> itkTimeStamp"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualDomainTimeStamp(self)


    def GetVirtualSpacing(self) -> "itkVectorD3":
        """GetVirtualSpacing(itkObjectToObjectMetric33 self) -> itkVectorD3"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualSpacing(self)


    def GetVirtualOrigin(self) -> "itkPointD3":
        """GetVirtualOrigin(itkObjectToObjectMetric33 self) -> itkPointD3"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualOrigin(self)


    def GetVirtualDirection(self) -> "itkMatrixD33":
        """GetVirtualDirection(itkObjectToObjectMetric33 self) -> itkMatrixD33"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualDirection(self)


    def GetVirtualRegion(self) -> "itkImageRegion3 const &":
        """GetVirtualRegion(itkObjectToObjectMetric33 self) -> itkImageRegion3"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualRegion(self)


    def GetModifiableVirtualImage(self) -> "itkImageD3 *":
        """GetModifiableVirtualImage(itkObjectToObjectMetric33 self) -> itkImageD3"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableVirtualImage(self)


    def GetVirtualImage(self, *args) -> "itkImageD3 *":
        """
        GetVirtualImage(itkObjectToObjectMetric33 self) -> itkImageD3
        GetVirtualImage(itkObjectToObjectMetric33 self) -> itkImageD3
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualImage(self, *args)


    def ComputeParameterOffsetFromVirtualIndex(self, index: 'itkIndex3', numberOfLocalParameters: 'unsigned int const &') -> "long":
        """ComputeParameterOffsetFromVirtualIndex(itkObjectToObjectMetric33 self, itkIndex3 index, unsigned int const & numberOfLocalParameters) -> long"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_ComputeParameterOffsetFromVirtualIndex(self, index, numberOfLocalParameters)


    def ComputeParameterOffsetFromVirtualPoint(self, point: 'itkPointD3', numberOfLocalParameters: 'unsigned int const &') -> "long":
        """ComputeParameterOffsetFromVirtualPoint(itkObjectToObjectMetric33 self, itkPointD3 point, unsigned int const & numberOfLocalParameters) -> long"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_ComputeParameterOffsetFromVirtualPoint(self, point, numberOfLocalParameters)


    def IsInsideVirtualDomain(self, *args) -> "bool":
        """
        IsInsideVirtualDomain(itkObjectToObjectMetric33 self, itkPointD3 point) -> bool
        IsInsideVirtualDomain(itkObjectToObjectMetric33 self, itkIndex3 index) -> bool
        """
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_IsInsideVirtualDomain(self, *args)

    __swig_destroy__ = _itkObjectToObjectMetricPython.delete_itkObjectToObjectMetric33

    def cast(obj: 'itkLightObject') -> "itkObjectToObjectMetric33 *":
        """cast(itkLightObject obj) -> itkObjectToObjectMetric33"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkObjectToObjectMetric33 *":
        """GetPointer(itkObjectToObjectMetric33 self) -> itkObjectToObjectMetric33"""
        return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkObjectToObjectMetric33

        Create a new object of the class itkObjectToObjectMetric33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectToObjectMetric33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectToObjectMetric33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectToObjectMetric33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkObjectToObjectMetric33.SetFixedTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetFixedTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetModifiableFixedTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableFixedTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetFixedTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetFixedTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.SetMovingTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetMovingTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetModifiableMovingTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableMovingTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetMovingTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetMovingTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.SetTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetTransform = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetTransform, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetNumberOfValidPoints = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetNumberOfValidPoints, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.SetVirtualDomain = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetVirtualDomain, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.SetVirtualDomainFromImage = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetVirtualDomainFromImage, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.SupportsArbitraryVirtualDomainSamples = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SupportsArbitraryVirtualDomainSamples, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetVirtualDomainTimeStamp = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualDomainTimeStamp, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetVirtualSpacing = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualSpacing, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetVirtualOrigin = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualOrigin, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetVirtualDirection = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualDirection, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetVirtualRegion = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualRegion, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetModifiableVirtualImage = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableVirtualImage, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetVirtualImage = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualImage, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.ComputeParameterOffsetFromVirtualIndex = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_ComputeParameterOffsetFromVirtualIndex, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.ComputeParameterOffsetFromVirtualPoint = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_ComputeParameterOffsetFromVirtualPoint, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.IsInsideVirtualDomain = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_IsInsideVirtualDomain, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33.GetPointer = new_instancemethod(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetPointer, None, itkObjectToObjectMetric33)
itkObjectToObjectMetric33_swigregister = _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_swigregister
itkObjectToObjectMetric33_swigregister(itkObjectToObjectMetric33)

def itkObjectToObjectMetric33_cast(obj: 'itkLightObject') -> "itkObjectToObjectMetric33 *":
    """itkObjectToObjectMetric33_cast(itkLightObject obj) -> itkObjectToObjectMetric33"""
    return _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_cast(obj)



