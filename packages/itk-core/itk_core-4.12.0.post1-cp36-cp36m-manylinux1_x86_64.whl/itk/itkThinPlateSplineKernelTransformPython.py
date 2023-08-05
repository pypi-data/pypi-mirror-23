# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkThinPlateSplineKernelTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkThinPlateSplineKernelTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkThinPlateSplineKernelTransformPython')
    _itkThinPlateSplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkThinPlateSplineKernelTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkThinPlateSplineKernelTransformPython
            return _itkThinPlateSplineKernelTransformPython
        try:
            _mod = imp.load_module('_itkThinPlateSplineKernelTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkThinPlateSplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkThinPlateSplineKernelTransformPython
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


import vnl_matrix_fixedPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkKernelTransformPython
import itkOptimizerParametersPython
import ITKCommonBasePython
import itkArrayPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkPointPython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkPointSetPython
import itkMapContainerPython

def itkThinPlateSplineKernelTransformD3_New():
  return itkThinPlateSplineKernelTransformD3.New()


def itkThinPlateSplineKernelTransformD2_New():
  return itkThinPlateSplineKernelTransformD2.New()

class itkThinPlateSplineKernelTransformD2(itkKernelTransformPython.itkKernelTransformD2):
    """Proxy of C++ itkThinPlateSplineKernelTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkThinPlateSplineKernelTransformD2_Pointer":
        """__New_orig__() -> itkThinPlateSplineKernelTransformD2_Pointer"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkThinPlateSplineKernelTransformD2_Pointer":
        """Clone(itkThinPlateSplineKernelTransformD2 self) -> itkThinPlateSplineKernelTransformD2_Pointer"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_Clone(self)

    __swig_destroy__ = _itkThinPlateSplineKernelTransformPython.delete_itkThinPlateSplineKernelTransformD2

    def cast(obj: 'itkLightObject') -> "itkThinPlateSplineKernelTransformD2 *":
        """cast(itkLightObject obj) -> itkThinPlateSplineKernelTransformD2"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkThinPlateSplineKernelTransformD2 *":
        """GetPointer(itkThinPlateSplineKernelTransformD2 self) -> itkThinPlateSplineKernelTransformD2"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkThinPlateSplineKernelTransformD2

        Create a new object of the class itkThinPlateSplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkThinPlateSplineKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkThinPlateSplineKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkThinPlateSplineKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkThinPlateSplineKernelTransformD2.Clone = new_instancemethod(_itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_Clone, None, itkThinPlateSplineKernelTransformD2)
itkThinPlateSplineKernelTransformD2.GetPointer = new_instancemethod(_itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_GetPointer, None, itkThinPlateSplineKernelTransformD2)
itkThinPlateSplineKernelTransformD2_swigregister = _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_swigregister
itkThinPlateSplineKernelTransformD2_swigregister(itkThinPlateSplineKernelTransformD2)

def itkThinPlateSplineKernelTransformD2___New_orig__() -> "itkThinPlateSplineKernelTransformD2_Pointer":
    """itkThinPlateSplineKernelTransformD2___New_orig__() -> itkThinPlateSplineKernelTransformD2_Pointer"""
    return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2___New_orig__()

def itkThinPlateSplineKernelTransformD2_cast(obj: 'itkLightObject') -> "itkThinPlateSplineKernelTransformD2 *":
    """itkThinPlateSplineKernelTransformD2_cast(itkLightObject obj) -> itkThinPlateSplineKernelTransformD2"""
    return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD2_cast(obj)

class itkThinPlateSplineKernelTransformD3(itkKernelTransformPython.itkKernelTransformD3):
    """Proxy of C++ itkThinPlateSplineKernelTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkThinPlateSplineKernelTransformD3_Pointer":
        """__New_orig__() -> itkThinPlateSplineKernelTransformD3_Pointer"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkThinPlateSplineKernelTransformD3_Pointer":
        """Clone(itkThinPlateSplineKernelTransformD3 self) -> itkThinPlateSplineKernelTransformD3_Pointer"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_Clone(self)

    __swig_destroy__ = _itkThinPlateSplineKernelTransformPython.delete_itkThinPlateSplineKernelTransformD3

    def cast(obj: 'itkLightObject') -> "itkThinPlateSplineKernelTransformD3 *":
        """cast(itkLightObject obj) -> itkThinPlateSplineKernelTransformD3"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkThinPlateSplineKernelTransformD3 *":
        """GetPointer(itkThinPlateSplineKernelTransformD3 self) -> itkThinPlateSplineKernelTransformD3"""
        return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkThinPlateSplineKernelTransformD3

        Create a new object of the class itkThinPlateSplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkThinPlateSplineKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkThinPlateSplineKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkThinPlateSplineKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkThinPlateSplineKernelTransformD3.Clone = new_instancemethod(_itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_Clone, None, itkThinPlateSplineKernelTransformD3)
itkThinPlateSplineKernelTransformD3.GetPointer = new_instancemethod(_itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_GetPointer, None, itkThinPlateSplineKernelTransformD3)
itkThinPlateSplineKernelTransformD3_swigregister = _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_swigregister
itkThinPlateSplineKernelTransformD3_swigregister(itkThinPlateSplineKernelTransformD3)

def itkThinPlateSplineKernelTransformD3___New_orig__() -> "itkThinPlateSplineKernelTransformD3_Pointer":
    """itkThinPlateSplineKernelTransformD3___New_orig__() -> itkThinPlateSplineKernelTransformD3_Pointer"""
    return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3___New_orig__()

def itkThinPlateSplineKernelTransformD3_cast(obj: 'itkLightObject') -> "itkThinPlateSplineKernelTransformD3 *":
    """itkThinPlateSplineKernelTransformD3_cast(itkLightObject obj) -> itkThinPlateSplineKernelTransformD3"""
    return _itkThinPlateSplineKernelTransformPython.itkThinPlateSplineKernelTransformD3_cast(obj)



