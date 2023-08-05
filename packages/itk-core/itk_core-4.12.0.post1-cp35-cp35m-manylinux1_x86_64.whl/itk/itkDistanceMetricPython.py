# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDistanceMetricPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDistanceMetricPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDistanceMetricPython')
    _itkDistanceMetricPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDistanceMetricPython', [dirname(__file__)])
        except ImportError:
            import _itkDistanceMetricPython
            return _itkDistanceMetricPython
        try:
            _mod = imp.load_module('_itkDistanceMetricPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDistanceMetricPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDistanceMetricPython
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
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkArrayPython
import ITKCommonBasePython
import itkFunctionBasePython
import itkRGBPixelPython
import itkContinuousIndexPython
import itkPointPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkImagePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython

def itkDistanceMetricVF3_New():
  return itkDistanceMetricVF3.New()


def itkDistanceMetricVF2_New():
  return itkDistanceMetricVF2.New()

class itkDistanceMetricVF2(itkFunctionBasePython.itkFunctionBaseVF2D):
    """Proxy of C++ itkDistanceMetricVF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOrigin(self, x: 'itkArrayD') -> "void":
        """SetOrigin(itkDistanceMetricVF2 self, itkArrayD x)"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_SetOrigin(self, x)


    def GetOrigin(self) -> "itkArrayD const &":
        """GetOrigin(itkDistanceMetricVF2 self) -> itkArrayD"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_GetOrigin(self)


    def Evaluate(self, *args) -> "double":
        """
        Evaluate(itkDistanceMetricVF2 self, itkVectorF2 x) -> double
        Evaluate(itkDistanceMetricVF2 self, itkVectorF2 x1, itkVectorF2 x2) -> double
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF2_Evaluate(self, *args)


    def SetMeasurementVectorSize(self, s: 'unsigned int') -> "void":
        """SetMeasurementVectorSize(itkDistanceMetricVF2 self, unsigned int s)"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_SetMeasurementVectorSize(self, s)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """GetMeasurementVectorSize(itkDistanceMetricVF2 self) -> unsigned int"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_GetMeasurementVectorSize(self)

    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF2

    def cast(obj: 'itkLightObject') -> "itkDistanceMetricVF2 *":
        """cast(itkLightObject obj) -> itkDistanceMetricVF2"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDistanceMetricVF2 *":
        """GetPointer(itkDistanceMetricVF2 self) -> itkDistanceMetricVF2"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDistanceMetricVF2

        Create a new object of the class itkDistanceMetricVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDistanceMetricVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDistanceMetricVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDistanceMetricVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDistanceMetricVF2.SetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_SetOrigin, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.GetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_GetOrigin, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.Evaluate = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_Evaluate, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.SetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_SetMeasurementVectorSize, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.GetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_GetMeasurementVectorSize, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.GetPointer = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_GetPointer, None, itkDistanceMetricVF2)
itkDistanceMetricVF2_swigregister = _itkDistanceMetricPython.itkDistanceMetricVF2_swigregister
itkDistanceMetricVF2_swigregister(itkDistanceMetricVF2)

def itkDistanceMetricVF2_cast(obj: 'itkLightObject') -> "itkDistanceMetricVF2 *":
    """itkDistanceMetricVF2_cast(itkLightObject obj) -> itkDistanceMetricVF2"""
    return _itkDistanceMetricPython.itkDistanceMetricVF2_cast(obj)

class itkDistanceMetricVF3(itkFunctionBasePython.itkFunctionBaseVF3D):
    """Proxy of C++ itkDistanceMetricVF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOrigin(self, x: 'itkArrayD') -> "void":
        """SetOrigin(itkDistanceMetricVF3 self, itkArrayD x)"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_SetOrigin(self, x)


    def GetOrigin(self) -> "itkArrayD const &":
        """GetOrigin(itkDistanceMetricVF3 self) -> itkArrayD"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_GetOrigin(self)


    def Evaluate(self, *args) -> "double":
        """
        Evaluate(itkDistanceMetricVF3 self, itkVectorF3 x) -> double
        Evaluate(itkDistanceMetricVF3 self, itkVectorF3 x1, itkVectorF3 x2) -> double
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF3_Evaluate(self, *args)


    def SetMeasurementVectorSize(self, s: 'unsigned int') -> "void":
        """SetMeasurementVectorSize(itkDistanceMetricVF3 self, unsigned int s)"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_SetMeasurementVectorSize(self, s)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """GetMeasurementVectorSize(itkDistanceMetricVF3 self) -> unsigned int"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_GetMeasurementVectorSize(self)

    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF3

    def cast(obj: 'itkLightObject') -> "itkDistanceMetricVF3 *":
        """cast(itkLightObject obj) -> itkDistanceMetricVF3"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkDistanceMetricVF3 *":
        """GetPointer(itkDistanceMetricVF3 self) -> itkDistanceMetricVF3"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkDistanceMetricVF3

        Create a new object of the class itkDistanceMetricVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDistanceMetricVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDistanceMetricVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDistanceMetricVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDistanceMetricVF3.SetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_SetOrigin, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.GetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_GetOrigin, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.Evaluate = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_Evaluate, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.SetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_SetMeasurementVectorSize, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.GetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_GetMeasurementVectorSize, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.GetPointer = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_GetPointer, None, itkDistanceMetricVF3)
itkDistanceMetricVF3_swigregister = _itkDistanceMetricPython.itkDistanceMetricVF3_swigregister
itkDistanceMetricVF3_swigregister(itkDistanceMetricVF3)

def itkDistanceMetricVF3_cast(obj: 'itkLightObject') -> "itkDistanceMetricVF3 *":
    """itkDistanceMetricVF3_cast(itkLightObject obj) -> itkDistanceMetricVF3"""
    return _itkDistanceMetricPython.itkDistanceMetricVF3_cast(obj)



