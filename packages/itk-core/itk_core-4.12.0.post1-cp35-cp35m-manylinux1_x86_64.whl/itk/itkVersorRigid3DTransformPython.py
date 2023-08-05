# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVersorRigid3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVersorRigid3DTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVersorRigid3DTransformPython')
    _itkVersorRigid3DTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVersorRigid3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkVersorRigid3DTransformPython
            return _itkVersorRigid3DTransformPython
        try:
            _mod = imp.load_module('_itkVersorRigid3DTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVersorRigid3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVersorRigid3DTransformPython
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
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkOptimizerParametersPython
import ITKCommonBasePython
import itkArray2DPython
import itkVersorTransformPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkVersorPython

def itkVersorRigid3DTransformD_New():
  return itkVersorRigid3DTransformD.New()

class itkVersorRigid3DTransformD(itkVersorTransformPython.itkVersorTransformD):
    """Proxy of C++ itkVersorRigid3DTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVersorRigid3DTransformD_Pointer":
        """__New_orig__() -> itkVersorRigid3DTransformD_Pointer"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVersorRigid3DTransformD_Pointer":
        """Clone(itkVersorRigid3DTransformD self) -> itkVersorRigid3DTransformD_Pointer"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkVersorRigid3DTransformD self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkVersorRigid3DTransformD self, itkArrayD update)
        """
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_UpdateTransformParameters(self, update, factor)

    __swig_destroy__ = _itkVersorRigid3DTransformPython.delete_itkVersorRigid3DTransformD

    def cast(obj: 'itkLightObject') -> "itkVersorRigid3DTransformD *":
        """cast(itkLightObject obj) -> itkVersorRigid3DTransformD"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVersorRigid3DTransformD *":
        """GetPointer(itkVersorRigid3DTransformD self) -> itkVersorRigid3DTransformD"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVersorRigid3DTransformD

        Create a new object of the class itkVersorRigid3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVersorRigid3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVersorRigid3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVersorRigid3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVersorRigid3DTransformD.Clone = new_instancemethod(_itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_Clone, None, itkVersorRigid3DTransformD)
itkVersorRigid3DTransformD.UpdateTransformParameters = new_instancemethod(_itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_UpdateTransformParameters, None, itkVersorRigid3DTransformD)
itkVersorRigid3DTransformD.GetPointer = new_instancemethod(_itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_GetPointer, None, itkVersorRigid3DTransformD)
itkVersorRigid3DTransformD_swigregister = _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_swigregister
itkVersorRigid3DTransformD_swigregister(itkVersorRigid3DTransformD)

def itkVersorRigid3DTransformD___New_orig__() -> "itkVersorRigid3DTransformD_Pointer":
    """itkVersorRigid3DTransformD___New_orig__() -> itkVersorRigid3DTransformD_Pointer"""
    return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD___New_orig__()

def itkVersorRigid3DTransformD_cast(obj: 'itkLightObject') -> "itkVersorRigid3DTransformD *":
    """itkVersorRigid3DTransformD_cast(itkLightObject obj) -> itkVersorRigid3DTransformD"""
    return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_cast(obj)



