# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkElasticBodySplineKernelTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkElasticBodySplineKernelTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkElasticBodySplineKernelTransformPython')
    _itkElasticBodySplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkElasticBodySplineKernelTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkElasticBodySplineKernelTransformPython
            return _itkElasticBodySplineKernelTransformPython
        try:
            _mod = imp.load_module('_itkElasticBodySplineKernelTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkElasticBodySplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkElasticBodySplineKernelTransformPython
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
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import ITKCommonBasePython
import itkKernelTransformPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkPointPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkPointSetPython
import itkMapContainerPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython

def itkElasticBodySplineKernelTransformD3_New():
  return itkElasticBodySplineKernelTransformD3.New()


def itkElasticBodySplineKernelTransformD2_New():
  return itkElasticBodySplineKernelTransformD2.New()

class itkElasticBodySplineKernelTransformD2(itkKernelTransformPython.itkKernelTransformD2):
    """Proxy of C++ itkElasticBodySplineKernelTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkElasticBodySplineKernelTransformD2_Pointer":
        """__New_orig__() -> itkElasticBodySplineKernelTransformD2_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkElasticBodySplineKernelTransformD2_Pointer":
        """Clone(itkElasticBodySplineKernelTransformD2 self) -> itkElasticBodySplineKernelTransformD2_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_Clone(self)


    def SetAlpha(self, _arg: 'double const') -> "void":
        """SetAlpha(itkElasticBodySplineKernelTransformD2 self, double const _arg)"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_SetAlpha(self, _arg)


    def GetAlpha(self) -> "double":
        """GetAlpha(itkElasticBodySplineKernelTransformD2 self) -> double"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetAlpha(self)

    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD2

    def cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD2 *":
        """cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD2"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkElasticBodySplineKernelTransformD2 *":
        """GetPointer(itkElasticBodySplineKernelTransformD2 self) -> itkElasticBodySplineKernelTransformD2"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD2

        Create a new object of the class itkElasticBodySplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkElasticBodySplineKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkElasticBodySplineKernelTransformD2.Clone = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_Clone, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2.SetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_SetAlpha, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2.GetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetAlpha, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2.GetPointer = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetPointer, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2_swigregister = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_swigregister
itkElasticBodySplineKernelTransformD2_swigregister(itkElasticBodySplineKernelTransformD2)

def itkElasticBodySplineKernelTransformD2___New_orig__() -> "itkElasticBodySplineKernelTransformD2_Pointer":
    """itkElasticBodySplineKernelTransformD2___New_orig__() -> itkElasticBodySplineKernelTransformD2_Pointer"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2___New_orig__()

def itkElasticBodySplineKernelTransformD2_cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD2 *":
    """itkElasticBodySplineKernelTransformD2_cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD2"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_cast(obj)

class itkElasticBodySplineKernelTransformD3(itkKernelTransformPython.itkKernelTransformD3):
    """Proxy of C++ itkElasticBodySplineKernelTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkElasticBodySplineKernelTransformD3_Pointer":
        """__New_orig__() -> itkElasticBodySplineKernelTransformD3_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkElasticBodySplineKernelTransformD3_Pointer":
        """Clone(itkElasticBodySplineKernelTransformD3 self) -> itkElasticBodySplineKernelTransformD3_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_Clone(self)


    def SetAlpha(self, _arg: 'double const') -> "void":
        """SetAlpha(itkElasticBodySplineKernelTransformD3 self, double const _arg)"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_SetAlpha(self, _arg)


    def GetAlpha(self) -> "double":
        """GetAlpha(itkElasticBodySplineKernelTransformD3 self) -> double"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetAlpha(self)

    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD3

    def cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD3 *":
        """cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD3"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkElasticBodySplineKernelTransformD3 *":
        """GetPointer(itkElasticBodySplineKernelTransformD3 self) -> itkElasticBodySplineKernelTransformD3"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD3

        Create a new object of the class itkElasticBodySplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkElasticBodySplineKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkElasticBodySplineKernelTransformD3.Clone = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_Clone, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3.SetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_SetAlpha, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3.GetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetAlpha, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3.GetPointer = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetPointer, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3_swigregister = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_swigregister
itkElasticBodySplineKernelTransformD3_swigregister(itkElasticBodySplineKernelTransformD3)

def itkElasticBodySplineKernelTransformD3___New_orig__() -> "itkElasticBodySplineKernelTransformD3_Pointer":
    """itkElasticBodySplineKernelTransformD3___New_orig__() -> itkElasticBodySplineKernelTransformD3_Pointer"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3___New_orig__()

def itkElasticBodySplineKernelTransformD3_cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD3 *":
    """itkElasticBodySplineKernelTransformD3_cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD3"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_cast(obj)



