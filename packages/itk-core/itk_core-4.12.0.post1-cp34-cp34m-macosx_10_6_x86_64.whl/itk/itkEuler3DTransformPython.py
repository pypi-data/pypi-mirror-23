# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkEuler3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkEuler3DTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkEuler3DTransformPython')
    _itkEuler3DTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkEuler3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkEuler3DTransformPython
            return _itkEuler3DTransformPython
        try:
            _mod = imp.load_module('_itkEuler3DTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkEuler3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkEuler3DTransformPython
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


import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkRigid3DTransformPython
import ITKCommonBasePython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython

def itkEuler3DTransformD_New():
  return itkEuler3DTransformD.New()

class itkEuler3DTransformD(itkRigid3DTransformPython.itkRigid3DTransformD):
    """Proxy of C++ itkEuler3DTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEuler3DTransformD_Pointer":
        """__New_orig__() -> itkEuler3DTransformD_Pointer"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEuler3DTransformD_Pointer":
        """Clone(itkEuler3DTransformD self) -> itkEuler3DTransformD_Pointer"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_Clone(self)


    def SetRotation(self, angleX: 'double', angleY: 'double', angleZ: 'double') -> "void":
        """SetRotation(itkEuler3DTransformD self, double angleX, double angleY, double angleZ)"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_SetRotation(self, angleX, angleY, angleZ)


    def GetAngleX(self) -> "double":
        """GetAngleX(itkEuler3DTransformD self) -> double"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_GetAngleX(self)


    def GetAngleY(self) -> "double":
        """GetAngleY(itkEuler3DTransformD self) -> double"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_GetAngleY(self)


    def GetAngleZ(self) -> "double":
        """GetAngleZ(itkEuler3DTransformD self) -> double"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_GetAngleZ(self)


    def SetComputeZYX(self, flag: 'bool const') -> "void":
        """SetComputeZYX(itkEuler3DTransformD self, bool const flag)"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_SetComputeZYX(self, flag)


    def GetComputeZYX(self) -> "bool":
        """GetComputeZYX(itkEuler3DTransformD self) -> bool"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_GetComputeZYX(self)

    __swig_destroy__ = _itkEuler3DTransformPython.delete_itkEuler3DTransformD

    def cast(obj: 'itkLightObject') -> "itkEuler3DTransformD *":
        """cast(itkLightObject obj) -> itkEuler3DTransformD"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkEuler3DTransformD *":
        """GetPointer(itkEuler3DTransformD self) -> itkEuler3DTransformD"""
        return _itkEuler3DTransformPython.itkEuler3DTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkEuler3DTransformD

        Create a new object of the class itkEuler3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuler3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEuler3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEuler3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEuler3DTransformD.Clone = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_Clone, None, itkEuler3DTransformD)
itkEuler3DTransformD.SetRotation = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_SetRotation, None, itkEuler3DTransformD)
itkEuler3DTransformD.GetAngleX = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_GetAngleX, None, itkEuler3DTransformD)
itkEuler3DTransformD.GetAngleY = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_GetAngleY, None, itkEuler3DTransformD)
itkEuler3DTransformD.GetAngleZ = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_GetAngleZ, None, itkEuler3DTransformD)
itkEuler3DTransformD.SetComputeZYX = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_SetComputeZYX, None, itkEuler3DTransformD)
itkEuler3DTransformD.GetComputeZYX = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_GetComputeZYX, None, itkEuler3DTransformD)
itkEuler3DTransformD.GetPointer = new_instancemethod(_itkEuler3DTransformPython.itkEuler3DTransformD_GetPointer, None, itkEuler3DTransformD)
itkEuler3DTransformD_swigregister = _itkEuler3DTransformPython.itkEuler3DTransformD_swigregister
itkEuler3DTransformD_swigregister(itkEuler3DTransformD)

def itkEuler3DTransformD___New_orig__() -> "itkEuler3DTransformD_Pointer":
    """itkEuler3DTransformD___New_orig__() -> itkEuler3DTransformD_Pointer"""
    return _itkEuler3DTransformPython.itkEuler3DTransformD___New_orig__()

def itkEuler3DTransformD_cast(obj: 'itkLightObject') -> "itkEuler3DTransformD *":
    """itkEuler3DTransformD_cast(itkLightObject obj) -> itkEuler3DTransformD"""
    return _itkEuler3DTransformPython.itkEuler3DTransformD_cast(obj)



