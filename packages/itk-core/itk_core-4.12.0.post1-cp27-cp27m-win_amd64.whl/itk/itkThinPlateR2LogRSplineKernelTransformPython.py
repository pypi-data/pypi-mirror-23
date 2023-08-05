# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkThinPlateR2LogRSplineKernelTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkThinPlateR2LogRSplineKernelTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkThinPlateR2LogRSplineKernelTransformPython')
    _itkThinPlateR2LogRSplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkThinPlateR2LogRSplineKernelTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkThinPlateR2LogRSplineKernelTransformPython
            return _itkThinPlateR2LogRSplineKernelTransformPython
        try:
            _mod = imp.load_module('_itkThinPlateR2LogRSplineKernelTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkThinPlateR2LogRSplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkThinPlateR2LogRSplineKernelTransformPython
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
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkKernelTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkPointSetPython
import itkMapContainerPython

def itkThinPlateR2LogRSplineKernelTransformD3_New():
  return itkThinPlateR2LogRSplineKernelTransformD3.New()


def itkThinPlateR2LogRSplineKernelTransformD2_New():
  return itkThinPlateR2LogRSplineKernelTransformD2.New()

class itkThinPlateR2LogRSplineKernelTransformD2(itkKernelTransformPython.itkKernelTransformD2):
    """Proxy of C++ itkThinPlateR2LogRSplineKernelTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkThinPlateR2LogRSplineKernelTransformD2_Pointer"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkThinPlateR2LogRSplineKernelTransformD2 self) -> itkThinPlateR2LogRSplineKernelTransformD2_Pointer"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_Clone(self)

    __swig_destroy__ = _itkThinPlateR2LogRSplineKernelTransformPython.delete_itkThinPlateR2LogRSplineKernelTransformD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkThinPlateR2LogRSplineKernelTransformD2"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkThinPlateR2LogRSplineKernelTransformD2 self) -> itkThinPlateR2LogRSplineKernelTransformD2"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkThinPlateR2LogRSplineKernelTransformD2

        Create a new object of the class itkThinPlateR2LogRSplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkThinPlateR2LogRSplineKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkThinPlateR2LogRSplineKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkThinPlateR2LogRSplineKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkThinPlateR2LogRSplineKernelTransformD2.Clone = new_instancemethod(_itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_Clone, None, itkThinPlateR2LogRSplineKernelTransformD2)
itkThinPlateR2LogRSplineKernelTransformD2.GetPointer = new_instancemethod(_itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_GetPointer, None, itkThinPlateR2LogRSplineKernelTransformD2)
itkThinPlateR2LogRSplineKernelTransformD2_swigregister = _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_swigregister
itkThinPlateR2LogRSplineKernelTransformD2_swigregister(itkThinPlateR2LogRSplineKernelTransformD2)

def itkThinPlateR2LogRSplineKernelTransformD2___New_orig__():
    """itkThinPlateR2LogRSplineKernelTransformD2___New_orig__() -> itkThinPlateR2LogRSplineKernelTransformD2_Pointer"""
    return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2___New_orig__()

def itkThinPlateR2LogRSplineKernelTransformD2_cast(obj):
    """itkThinPlateR2LogRSplineKernelTransformD2_cast(itkLightObject obj) -> itkThinPlateR2LogRSplineKernelTransformD2"""
    return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD2_cast(obj)

class itkThinPlateR2LogRSplineKernelTransformD3(itkKernelTransformPython.itkKernelTransformD3):
    """Proxy of C++ itkThinPlateR2LogRSplineKernelTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkThinPlateR2LogRSplineKernelTransformD3_Pointer"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkThinPlateR2LogRSplineKernelTransformD3 self) -> itkThinPlateR2LogRSplineKernelTransformD3_Pointer"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_Clone(self)

    __swig_destroy__ = _itkThinPlateR2LogRSplineKernelTransformPython.delete_itkThinPlateR2LogRSplineKernelTransformD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkThinPlateR2LogRSplineKernelTransformD3"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkThinPlateR2LogRSplineKernelTransformD3 self) -> itkThinPlateR2LogRSplineKernelTransformD3"""
        return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkThinPlateR2LogRSplineKernelTransformD3

        Create a new object of the class itkThinPlateR2LogRSplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkThinPlateR2LogRSplineKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkThinPlateR2LogRSplineKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkThinPlateR2LogRSplineKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkThinPlateR2LogRSplineKernelTransformD3.Clone = new_instancemethod(_itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_Clone, None, itkThinPlateR2LogRSplineKernelTransformD3)
itkThinPlateR2LogRSplineKernelTransformD3.GetPointer = new_instancemethod(_itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_GetPointer, None, itkThinPlateR2LogRSplineKernelTransformD3)
itkThinPlateR2LogRSplineKernelTransformD3_swigregister = _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_swigregister
itkThinPlateR2LogRSplineKernelTransformD3_swigregister(itkThinPlateR2LogRSplineKernelTransformD3)

def itkThinPlateR2LogRSplineKernelTransformD3___New_orig__():
    """itkThinPlateR2LogRSplineKernelTransformD3___New_orig__() -> itkThinPlateR2LogRSplineKernelTransformD3_Pointer"""
    return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3___New_orig__()

def itkThinPlateR2LogRSplineKernelTransformD3_cast(obj):
    """itkThinPlateR2LogRSplineKernelTransformD3_cast(itkLightObject obj) -> itkThinPlateR2LogRSplineKernelTransformD3"""
    return _itkThinPlateR2LogRSplineKernelTransformPython.itkThinPlateR2LogRSplineKernelTransformD3_cast(obj)



