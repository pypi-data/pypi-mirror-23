# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHistogramToTextureFeaturesFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkHistogramToTextureFeaturesFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkHistogramToTextureFeaturesFilterPython')
    _itkHistogramToTextureFeaturesFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHistogramToTextureFeaturesFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHistogramToTextureFeaturesFilterPython
            return _itkHistogramToTextureFeaturesFilterPython
        try:
            _mod = imp.load_module('_itkHistogramToTextureFeaturesFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkHistogramToTextureFeaturesFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHistogramToTextureFeaturesFilterPython
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
import itkHistogramPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSamplePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython

def itkHistogramToTextureFeaturesFilterHF_New():
  return itkHistogramToTextureFeaturesFilterHF.New()


def itkHistogramToTextureFeaturesFilterHD_New():
  return itkHistogramToTextureFeaturesFilterHD.New()

class itkHistogramToTextureFeaturesFilterHD(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkHistogramToTextureFeaturesFilterHD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHistogramToTextureFeaturesFilterHD_Pointer":
        """__New_orig__() -> itkHistogramToTextureFeaturesFilterHD_Pointer"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHistogramToTextureFeaturesFilterHD_Pointer":
        """Clone(itkHistogramToTextureFeaturesFilterHD self) -> itkHistogramToTextureFeaturesFilterHD_Pointer"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Clone(self)


    def SetInput(self, histogram: 'itkHistogramD') -> "void":
        """SetInput(itkHistogramToTextureFeaturesFilterHD self, itkHistogramD histogram)"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_SetInput(self, histogram)


    def GetInput(self) -> "itkHistogramD const *":
        """GetInput(itkHistogramToTextureFeaturesFilterHD self) -> itkHistogramD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInput(self)


    def GetEnergy(self) -> "double":
        """GetEnergy(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergy(self)


    def GetEnergyOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetEnergyOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergyOutput(self)


    def GetEntropy(self) -> "double":
        """GetEntropy(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropy(self)


    def GetEntropyOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetEntropyOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropyOutput(self)


    def GetCorrelation(self) -> "double":
        """GetCorrelation(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelation(self)


    def GetCorrelationOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetCorrelationOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelationOutput(self)


    def GetInverseDifferenceMoment(self) -> "double":
        """GetInverseDifferenceMoment(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMoment(self)


    def GetInverseDifferenceMomentOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetInverseDifferenceMomentOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMomentOutput(self)


    def GetInertia(self) -> "double":
        """GetInertia(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertia(self)


    def GetInertiaOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetInertiaOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertiaOutput(self)


    def GetClusterShade(self) -> "double":
        """GetClusterShade(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShade(self)


    def GetClusterShadeOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetClusterShadeOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShadeOutput(self)


    def GetClusterProminence(self) -> "double":
        """GetClusterProminence(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminence(self)


    def GetClusterProminenceOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetClusterProminenceOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminenceOutput(self)


    def GetHaralickCorrelation(self) -> "double":
        """GetHaralickCorrelation(itkHistogramToTextureFeaturesFilterHD self) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelation(self)


    def GetHaralickCorrelationOutput(self) -> "itkSimpleDataObjectDecoratorD const *":
        """GetHaralickCorrelationOutput(itkHistogramToTextureFeaturesFilterHD self) -> itkSimpleDataObjectDecoratorD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelationOutput(self)

    Energy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Energy
    Entropy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Entropy
    Correlation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Correlation
    InverseDifferenceMoment = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_InverseDifferenceMoment
    Inertia = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Inertia
    ClusterShade = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_ClusterShade
    ClusterProminence = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_ClusterProminence
    HaralickCorrelation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_HaralickCorrelation
    InvalidFeatureName = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_InvalidFeatureName

    def GetFeature(self, name: 'itkHistogramToTextureFeaturesFilterHD::TextureFeatureName') -> "double":
        """GetFeature(itkHistogramToTextureFeaturesFilterHD self, itkHistogramToTextureFeaturesFilterHD::TextureFeatureName name) -> double"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetFeature(self, name)

    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterHD

    def cast(obj: 'itkLightObject') -> "itkHistogramToTextureFeaturesFilterHD *":
        """cast(itkLightObject obj) -> itkHistogramToTextureFeaturesFilterHD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHistogramToTextureFeaturesFilterHD *":
        """GetPointer(itkHistogramToTextureFeaturesFilterHD self) -> itkHistogramToTextureFeaturesFilterHD"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHistogramToTextureFeaturesFilterHD

        Create a new object of the class itkHistogramToTextureFeaturesFilterHD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToTextureFeaturesFilterHD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHistogramToTextureFeaturesFilterHD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHistogramToTextureFeaturesFilterHD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHistogramToTextureFeaturesFilterHD.Clone = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Clone, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.SetInput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_SetInput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetInput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetEnergy = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergy, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetEnergyOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergyOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetEntropy = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropy, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetEntropyOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropyOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetCorrelation = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelation, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetCorrelationOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelationOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetInverseDifferenceMoment = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMoment, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetInverseDifferenceMomentOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMomentOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetInertia = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertia, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetInertiaOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertiaOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetClusterShade = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShade, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetClusterShadeOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShadeOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetClusterProminence = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminence, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetClusterProminenceOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminenceOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetHaralickCorrelation = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelation, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetHaralickCorrelationOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelationOutput, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetFeature = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetFeature, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD.GetPointer = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetPointer, None, itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD_swigregister = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_swigregister
itkHistogramToTextureFeaturesFilterHD_swigregister(itkHistogramToTextureFeaturesFilterHD)

def itkHistogramToTextureFeaturesFilterHD___New_orig__() -> "itkHistogramToTextureFeaturesFilterHD_Pointer":
    """itkHistogramToTextureFeaturesFilterHD___New_orig__() -> itkHistogramToTextureFeaturesFilterHD_Pointer"""
    return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD___New_orig__()

def itkHistogramToTextureFeaturesFilterHD_cast(obj: 'itkLightObject') -> "itkHistogramToTextureFeaturesFilterHD *":
    """itkHistogramToTextureFeaturesFilterHD_cast(itkLightObject obj) -> itkHistogramToTextureFeaturesFilterHD"""
    return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_cast(obj)

class itkHistogramToTextureFeaturesFilterHF(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkHistogramToTextureFeaturesFilterHF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHistogramToTextureFeaturesFilterHF_Pointer":
        """__New_orig__() -> itkHistogramToTextureFeaturesFilterHF_Pointer"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHistogramToTextureFeaturesFilterHF_Pointer":
        """Clone(itkHistogramToTextureFeaturesFilterHF self) -> itkHistogramToTextureFeaturesFilterHF_Pointer"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Clone(self)


    def SetInput(self, histogram: 'itkHistogramF') -> "void":
        """SetInput(itkHistogramToTextureFeaturesFilterHF self, itkHistogramF histogram)"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_SetInput(self, histogram)


    def GetInput(self) -> "itkHistogramF const *":
        """GetInput(itkHistogramToTextureFeaturesFilterHF self) -> itkHistogramF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInput(self)


    def GetEnergy(self) -> "float":
        """GetEnergy(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergy(self)


    def GetEnergyOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetEnergyOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergyOutput(self)


    def GetEntropy(self) -> "float":
        """GetEntropy(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropy(self)


    def GetEntropyOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetEntropyOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropyOutput(self)


    def GetCorrelation(self) -> "float":
        """GetCorrelation(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelation(self)


    def GetCorrelationOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetCorrelationOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelationOutput(self)


    def GetInverseDifferenceMoment(self) -> "float":
        """GetInverseDifferenceMoment(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMoment(self)


    def GetInverseDifferenceMomentOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetInverseDifferenceMomentOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMomentOutput(self)


    def GetInertia(self) -> "float":
        """GetInertia(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertia(self)


    def GetInertiaOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetInertiaOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertiaOutput(self)


    def GetClusterShade(self) -> "float":
        """GetClusterShade(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShade(self)


    def GetClusterShadeOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetClusterShadeOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShadeOutput(self)


    def GetClusterProminence(self) -> "float":
        """GetClusterProminence(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminence(self)


    def GetClusterProminenceOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetClusterProminenceOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminenceOutput(self)


    def GetHaralickCorrelation(self) -> "float":
        """GetHaralickCorrelation(itkHistogramToTextureFeaturesFilterHF self) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelation(self)


    def GetHaralickCorrelationOutput(self) -> "itkSimpleDataObjectDecoratorF const *":
        """GetHaralickCorrelationOutput(itkHistogramToTextureFeaturesFilterHF self) -> itkSimpleDataObjectDecoratorF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelationOutput(self)

    Energy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Energy
    Entropy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Entropy
    Correlation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Correlation
    InverseDifferenceMoment = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_InverseDifferenceMoment
    Inertia = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Inertia
    ClusterShade = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_ClusterShade
    ClusterProminence = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_ClusterProminence
    HaralickCorrelation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_HaralickCorrelation
    InvalidFeatureName = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_InvalidFeatureName

    def GetFeature(self, name: 'itkHistogramToTextureFeaturesFilterHF::TextureFeatureName') -> "float":
        """GetFeature(itkHistogramToTextureFeaturesFilterHF self, itkHistogramToTextureFeaturesFilterHF::TextureFeatureName name) -> float"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetFeature(self, name)

    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterHF

    def cast(obj: 'itkLightObject') -> "itkHistogramToTextureFeaturesFilterHF *":
        """cast(itkLightObject obj) -> itkHistogramToTextureFeaturesFilterHF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkHistogramToTextureFeaturesFilterHF *":
        """GetPointer(itkHistogramToTextureFeaturesFilterHF self) -> itkHistogramToTextureFeaturesFilterHF"""
        return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHistogramToTextureFeaturesFilterHF

        Create a new object of the class itkHistogramToTextureFeaturesFilterHF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToTextureFeaturesFilterHF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHistogramToTextureFeaturesFilterHF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHistogramToTextureFeaturesFilterHF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHistogramToTextureFeaturesFilterHF.Clone = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Clone, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.SetInput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_SetInput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetInput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetEnergy = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergy, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetEnergyOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergyOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetEntropy = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropy, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetEntropyOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropyOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetCorrelation = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelation, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetCorrelationOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelationOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetInverseDifferenceMoment = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMoment, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetInverseDifferenceMomentOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMomentOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetInertia = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertia, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetInertiaOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertiaOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetClusterShade = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShade, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetClusterShadeOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShadeOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetClusterProminence = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminence, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetClusterProminenceOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminenceOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetHaralickCorrelation = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelation, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetHaralickCorrelationOutput = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelationOutput, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetFeature = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetFeature, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF.GetPointer = new_instancemethod(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetPointer, None, itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF_swigregister = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_swigregister
itkHistogramToTextureFeaturesFilterHF_swigregister(itkHistogramToTextureFeaturesFilterHF)

def itkHistogramToTextureFeaturesFilterHF___New_orig__() -> "itkHistogramToTextureFeaturesFilterHF_Pointer":
    """itkHistogramToTextureFeaturesFilterHF___New_orig__() -> itkHistogramToTextureFeaturesFilterHF_Pointer"""
    return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF___New_orig__()

def itkHistogramToTextureFeaturesFilterHF_cast(obj: 'itkLightObject') -> "itkHistogramToTextureFeaturesFilterHF *":
    """itkHistogramToTextureFeaturesFilterHF_cast(itkLightObject obj) -> itkHistogramToTextureFeaturesFilterHF"""
    return _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_cast(obj)



