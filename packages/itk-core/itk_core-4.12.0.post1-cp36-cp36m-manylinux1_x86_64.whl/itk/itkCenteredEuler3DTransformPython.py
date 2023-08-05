# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCenteredEuler3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkCenteredEuler3DTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkCenteredEuler3DTransformPython')
    _itkCenteredEuler3DTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCenteredEuler3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkCenteredEuler3DTransformPython
            return _itkCenteredEuler3DTransformPython
        try:
            _mod = imp.load_module('_itkCenteredEuler3DTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkCenteredEuler3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCenteredEuler3DTransformPython
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


import itkOptimizerParametersPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import ITKCommonBasePython
import itkArrayPython
import itkEuler3DTransformPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkPointPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkArray2DPython

def itkCenteredEuler3DTransformD_New():
  return itkCenteredEuler3DTransformD.New()

class itkCenteredEuler3DTransformD(itkEuler3DTransformPython.itkEuler3DTransformD):
    """Proxy of C++ itkCenteredEuler3DTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCenteredEuler3DTransformD_Pointer":
        """__New_orig__() -> itkCenteredEuler3DTransformD_Pointer"""
        return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCenteredEuler3DTransformD_Pointer":
        """Clone(itkCenteredEuler3DTransformD self) -> itkCenteredEuler3DTransformD_Pointer"""
        return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_Clone(self)


    def GetInverse(self, inverse: 'itkCenteredEuler3DTransformD') -> "bool":
        """GetInverse(itkCenteredEuler3DTransformD self, itkCenteredEuler3DTransformD inverse) -> bool"""
        return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_GetInverse(self, inverse)

    __swig_destroy__ = _itkCenteredEuler3DTransformPython.delete_itkCenteredEuler3DTransformD

    def cast(obj: 'itkLightObject') -> "itkCenteredEuler3DTransformD *":
        """cast(itkLightObject obj) -> itkCenteredEuler3DTransformD"""
        return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkCenteredEuler3DTransformD *":
        """GetPointer(itkCenteredEuler3DTransformD self) -> itkCenteredEuler3DTransformD"""
        return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCenteredEuler3DTransformD

        Create a new object of the class itkCenteredEuler3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredEuler3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredEuler3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredEuler3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredEuler3DTransformD.Clone = new_instancemethod(_itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_Clone, None, itkCenteredEuler3DTransformD)
itkCenteredEuler3DTransformD.GetInverse = new_instancemethod(_itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_GetInverse, None, itkCenteredEuler3DTransformD)
itkCenteredEuler3DTransformD.GetPointer = new_instancemethod(_itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_GetPointer, None, itkCenteredEuler3DTransformD)
itkCenteredEuler3DTransformD_swigregister = _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_swigregister
itkCenteredEuler3DTransformD_swigregister(itkCenteredEuler3DTransformD)

def itkCenteredEuler3DTransformD___New_orig__() -> "itkCenteredEuler3DTransformD_Pointer":
    """itkCenteredEuler3DTransformD___New_orig__() -> itkCenteredEuler3DTransformD_Pointer"""
    return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD___New_orig__()

def itkCenteredEuler3DTransformD_cast(obj: 'itkLightObject') -> "itkCenteredEuler3DTransformD *":
    """itkCenteredEuler3DTransformD_cast(itkLightObject obj) -> itkCenteredEuler3DTransformD"""
    return _itkCenteredEuler3DTransformPython.itkCenteredEuler3DTransformD_cast(obj)



