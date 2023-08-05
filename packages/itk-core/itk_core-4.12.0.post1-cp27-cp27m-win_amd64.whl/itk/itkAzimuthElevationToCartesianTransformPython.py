# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAzimuthElevationToCartesianTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkAzimuthElevationToCartesianTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkAzimuthElevationToCartesianTransformPython')
    _itkAzimuthElevationToCartesianTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAzimuthElevationToCartesianTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkAzimuthElevationToCartesianTransformPython
            return _itkAzimuthElevationToCartesianTransformPython
        try:
            _mod = imp.load_module('_itkAzimuthElevationToCartesianTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkAzimuthElevationToCartesianTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAzimuthElevationToCartesianTransformPython
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


import itkAffineTransformPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython

def itkAzimuthElevationToCartesianTransformD3_New():
  return itkAzimuthElevationToCartesianTransformD3.New()


def itkAzimuthElevationToCartesianTransformD2_New():
  return itkAzimuthElevationToCartesianTransformD2.New()

class itkAzimuthElevationToCartesianTransformD2(itkAffineTransformPython.itkAffineTransformD2):
    """Proxy of C++ itkAzimuthElevationToCartesianTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkAzimuthElevationToCartesianTransformD2_Pointer"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkAzimuthElevationToCartesianTransformD2 self) -> itkAzimuthElevationToCartesianTransformD2_Pointer"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_Clone(self)


    def SetAzimuthElevationToCartesianParameters(self, *args):
        """
        SetAzimuthElevationToCartesianParameters(itkAzimuthElevationToCartesianTransformD2 self, double const sampleSize, double const blanking, long const maxAzimuth, long const maxElevation, double const azimuthAngleSeparation, double const elevationAngleSeparation)
        SetAzimuthElevationToCartesianParameters(itkAzimuthElevationToCartesianTransformD2 self, double const sampleSize, double const blanking, long const maxAzimuth, long const maxElevation)
        """
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetAzimuthElevationToCartesianParameters(self, *args)


    def BackTransform(self, point):
        """BackTransform(itkAzimuthElevationToCartesianTransformD2 self, itkPointD2 point) -> itkPointD2"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_BackTransform(self, point)


    def BackTransformPoint(self, point):
        """BackTransformPoint(itkAzimuthElevationToCartesianTransformD2 self, itkPointD2 point) -> itkPointD2"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_BackTransformPoint(self, point)


    def SetForwardAzimuthElevationToCartesian(self):
        """SetForwardAzimuthElevationToCartesian(itkAzimuthElevationToCartesianTransformD2 self)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetForwardAzimuthElevationToCartesian(self)


    def SetForwardCartesianToAzimuthElevation(self):
        """SetForwardCartesianToAzimuthElevation(itkAzimuthElevationToCartesianTransformD2 self)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetForwardCartesianToAzimuthElevation(self)


    def TransformAzElToCartesian(self, point):
        """TransformAzElToCartesian(itkAzimuthElevationToCartesianTransformD2 self, itkPointD2 point) -> itkPointD2"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_TransformAzElToCartesian(self, point)


    def TransformCartesianToAzEl(self, point):
        """TransformCartesianToAzEl(itkAzimuthElevationToCartesianTransformD2 self, itkPointD2 point) -> itkPointD2"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_TransformCartesianToAzEl(self, point)


    def SetMaxAzimuth(self, _arg):
        """SetMaxAzimuth(itkAzimuthElevationToCartesianTransformD2 self, long const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetMaxAzimuth(self, _arg)


    def GetMaxAzimuth(self):
        """GetMaxAzimuth(itkAzimuthElevationToCartesianTransformD2 self) -> long"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetMaxAzimuth(self)


    def SetMaxElevation(self, _arg):
        """SetMaxElevation(itkAzimuthElevationToCartesianTransformD2 self, long const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetMaxElevation(self, _arg)


    def GetMaxElevation(self):
        """GetMaxElevation(itkAzimuthElevationToCartesianTransformD2 self) -> long"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetMaxElevation(self)


    def SetRadiusSampleSize(self, _arg):
        """SetRadiusSampleSize(itkAzimuthElevationToCartesianTransformD2 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetRadiusSampleSize(self, _arg)


    def GetRadiusSampleSize(self):
        """GetRadiusSampleSize(itkAzimuthElevationToCartesianTransformD2 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetRadiusSampleSize(self)


    def SetAzimuthAngularSeparation(self, _arg):
        """SetAzimuthAngularSeparation(itkAzimuthElevationToCartesianTransformD2 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetAzimuthAngularSeparation(self, _arg)


    def GetAzimuthAngularSeparation(self):
        """GetAzimuthAngularSeparation(itkAzimuthElevationToCartesianTransformD2 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetAzimuthAngularSeparation(self)


    def SetElevationAngularSeparation(self, _arg):
        """SetElevationAngularSeparation(itkAzimuthElevationToCartesianTransformD2 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetElevationAngularSeparation(self, _arg)


    def GetElevationAngularSeparation(self):
        """GetElevationAngularSeparation(itkAzimuthElevationToCartesianTransformD2 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetElevationAngularSeparation(self)


    def SetFirstSampleDistance(self, _arg):
        """SetFirstSampleDistance(itkAzimuthElevationToCartesianTransformD2 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetFirstSampleDistance(self, _arg)


    def GetFirstSampleDistance(self):
        """GetFirstSampleDistance(itkAzimuthElevationToCartesianTransformD2 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetFirstSampleDistance(self)

    __swig_destroy__ = _itkAzimuthElevationToCartesianTransformPython.delete_itkAzimuthElevationToCartesianTransformD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkAzimuthElevationToCartesianTransformD2"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkAzimuthElevationToCartesianTransformD2 self) -> itkAzimuthElevationToCartesianTransformD2"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAzimuthElevationToCartesianTransformD2

        Create a new object of the class itkAzimuthElevationToCartesianTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAzimuthElevationToCartesianTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAzimuthElevationToCartesianTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAzimuthElevationToCartesianTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAzimuthElevationToCartesianTransformD2.Clone = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_Clone, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetAzimuthElevationToCartesianParameters = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetAzimuthElevationToCartesianParameters, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.BackTransform = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_BackTransform, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.BackTransformPoint = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_BackTransformPoint, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetForwardAzimuthElevationToCartesian = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetForwardAzimuthElevationToCartesian, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetForwardCartesianToAzimuthElevation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetForwardCartesianToAzimuthElevation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.TransformAzElToCartesian = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_TransformAzElToCartesian, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.TransformCartesianToAzEl = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_TransformCartesianToAzEl, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetMaxAzimuth = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetMaxAzimuth, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetMaxAzimuth = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetMaxAzimuth, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetMaxElevation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetMaxElevation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetMaxElevation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetMaxElevation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetRadiusSampleSize = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetRadiusSampleSize, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetRadiusSampleSize = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetRadiusSampleSize, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetAzimuthAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetAzimuthAngularSeparation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetAzimuthAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetAzimuthAngularSeparation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetElevationAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetElevationAngularSeparation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetElevationAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetElevationAngularSeparation, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.SetFirstSampleDistance = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetFirstSampleDistance, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetFirstSampleDistance = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetFirstSampleDistance, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2.GetPointer = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetPointer, None, itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2_swigregister = _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_swigregister
itkAzimuthElevationToCartesianTransformD2_swigregister(itkAzimuthElevationToCartesianTransformD2)

def itkAzimuthElevationToCartesianTransformD2___New_orig__():
    """itkAzimuthElevationToCartesianTransformD2___New_orig__() -> itkAzimuthElevationToCartesianTransformD2_Pointer"""
    return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2___New_orig__()

def itkAzimuthElevationToCartesianTransformD2_cast(obj):
    """itkAzimuthElevationToCartesianTransformD2_cast(itkLightObject obj) -> itkAzimuthElevationToCartesianTransformD2"""
    return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_cast(obj)

class itkAzimuthElevationToCartesianTransformD3(itkAffineTransformPython.itkAffineTransformD3):
    """Proxy of C++ itkAzimuthElevationToCartesianTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkAzimuthElevationToCartesianTransformD3_Pointer"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkAzimuthElevationToCartesianTransformD3 self) -> itkAzimuthElevationToCartesianTransformD3_Pointer"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_Clone(self)


    def SetAzimuthElevationToCartesianParameters(self, *args):
        """
        SetAzimuthElevationToCartesianParameters(itkAzimuthElevationToCartesianTransformD3 self, double const sampleSize, double const blanking, long const maxAzimuth, long const maxElevation, double const azimuthAngleSeparation, double const elevationAngleSeparation)
        SetAzimuthElevationToCartesianParameters(itkAzimuthElevationToCartesianTransformD3 self, double const sampleSize, double const blanking, long const maxAzimuth, long const maxElevation)
        """
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetAzimuthElevationToCartesianParameters(self, *args)


    def BackTransform(self, point):
        """BackTransform(itkAzimuthElevationToCartesianTransformD3 self, itkPointD3 point) -> itkPointD3"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_BackTransform(self, point)


    def BackTransformPoint(self, point):
        """BackTransformPoint(itkAzimuthElevationToCartesianTransformD3 self, itkPointD3 point) -> itkPointD3"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_BackTransformPoint(self, point)


    def SetForwardAzimuthElevationToCartesian(self):
        """SetForwardAzimuthElevationToCartesian(itkAzimuthElevationToCartesianTransformD3 self)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetForwardAzimuthElevationToCartesian(self)


    def SetForwardCartesianToAzimuthElevation(self):
        """SetForwardCartesianToAzimuthElevation(itkAzimuthElevationToCartesianTransformD3 self)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetForwardCartesianToAzimuthElevation(self)


    def TransformAzElToCartesian(self, point):
        """TransformAzElToCartesian(itkAzimuthElevationToCartesianTransformD3 self, itkPointD3 point) -> itkPointD3"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_TransformAzElToCartesian(self, point)


    def TransformCartesianToAzEl(self, point):
        """TransformCartesianToAzEl(itkAzimuthElevationToCartesianTransformD3 self, itkPointD3 point) -> itkPointD3"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_TransformCartesianToAzEl(self, point)


    def SetMaxAzimuth(self, _arg):
        """SetMaxAzimuth(itkAzimuthElevationToCartesianTransformD3 self, long const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetMaxAzimuth(self, _arg)


    def GetMaxAzimuth(self):
        """GetMaxAzimuth(itkAzimuthElevationToCartesianTransformD3 self) -> long"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetMaxAzimuth(self)


    def SetMaxElevation(self, _arg):
        """SetMaxElevation(itkAzimuthElevationToCartesianTransformD3 self, long const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetMaxElevation(self, _arg)


    def GetMaxElevation(self):
        """GetMaxElevation(itkAzimuthElevationToCartesianTransformD3 self) -> long"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetMaxElevation(self)


    def SetRadiusSampleSize(self, _arg):
        """SetRadiusSampleSize(itkAzimuthElevationToCartesianTransformD3 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetRadiusSampleSize(self, _arg)


    def GetRadiusSampleSize(self):
        """GetRadiusSampleSize(itkAzimuthElevationToCartesianTransformD3 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetRadiusSampleSize(self)


    def SetAzimuthAngularSeparation(self, _arg):
        """SetAzimuthAngularSeparation(itkAzimuthElevationToCartesianTransformD3 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetAzimuthAngularSeparation(self, _arg)


    def GetAzimuthAngularSeparation(self):
        """GetAzimuthAngularSeparation(itkAzimuthElevationToCartesianTransformD3 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetAzimuthAngularSeparation(self)


    def SetElevationAngularSeparation(self, _arg):
        """SetElevationAngularSeparation(itkAzimuthElevationToCartesianTransformD3 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetElevationAngularSeparation(self, _arg)


    def GetElevationAngularSeparation(self):
        """GetElevationAngularSeparation(itkAzimuthElevationToCartesianTransformD3 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetElevationAngularSeparation(self)


    def SetFirstSampleDistance(self, _arg):
        """SetFirstSampleDistance(itkAzimuthElevationToCartesianTransformD3 self, double const _arg)"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetFirstSampleDistance(self, _arg)


    def GetFirstSampleDistance(self):
        """GetFirstSampleDistance(itkAzimuthElevationToCartesianTransformD3 self) -> double"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetFirstSampleDistance(self)

    __swig_destroy__ = _itkAzimuthElevationToCartesianTransformPython.delete_itkAzimuthElevationToCartesianTransformD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkAzimuthElevationToCartesianTransformD3"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkAzimuthElevationToCartesianTransformD3 self) -> itkAzimuthElevationToCartesianTransformD3"""
        return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAzimuthElevationToCartesianTransformD3

        Create a new object of the class itkAzimuthElevationToCartesianTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAzimuthElevationToCartesianTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAzimuthElevationToCartesianTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAzimuthElevationToCartesianTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAzimuthElevationToCartesianTransformD3.Clone = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_Clone, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetAzimuthElevationToCartesianParameters = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetAzimuthElevationToCartesianParameters, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.BackTransform = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_BackTransform, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.BackTransformPoint = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_BackTransformPoint, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetForwardAzimuthElevationToCartesian = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetForwardAzimuthElevationToCartesian, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetForwardCartesianToAzimuthElevation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetForwardCartesianToAzimuthElevation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.TransformAzElToCartesian = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_TransformAzElToCartesian, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.TransformCartesianToAzEl = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_TransformCartesianToAzEl, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetMaxAzimuth = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetMaxAzimuth, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetMaxAzimuth = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetMaxAzimuth, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetMaxElevation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetMaxElevation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetMaxElevation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetMaxElevation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetRadiusSampleSize = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetRadiusSampleSize, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetRadiusSampleSize = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetRadiusSampleSize, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetAzimuthAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetAzimuthAngularSeparation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetAzimuthAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetAzimuthAngularSeparation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetElevationAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetElevationAngularSeparation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetElevationAngularSeparation = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetElevationAngularSeparation, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.SetFirstSampleDistance = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetFirstSampleDistance, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetFirstSampleDistance = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetFirstSampleDistance, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3.GetPointer = new_instancemethod(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetPointer, None, itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3_swigregister = _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_swigregister
itkAzimuthElevationToCartesianTransformD3_swigregister(itkAzimuthElevationToCartesianTransformD3)

def itkAzimuthElevationToCartesianTransformD3___New_orig__():
    """itkAzimuthElevationToCartesianTransformD3___New_orig__() -> itkAzimuthElevationToCartesianTransformD3_Pointer"""
    return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3___New_orig__()

def itkAzimuthElevationToCartesianTransformD3_cast(obj):
    """itkAzimuthElevationToCartesianTransformD3_cast(itkLightObject obj) -> itkAzimuthElevationToCartesianTransformD3"""
    return _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_cast(obj)



