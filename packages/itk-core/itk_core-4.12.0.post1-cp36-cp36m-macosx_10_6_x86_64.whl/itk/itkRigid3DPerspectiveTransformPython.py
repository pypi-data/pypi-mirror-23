# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRigid3DPerspectiveTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRigid3DPerspectiveTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRigid3DPerspectiveTransformPython')
    _itkRigid3DPerspectiveTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRigid3DPerspectiveTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkRigid3DPerspectiveTransformPython
            return _itkRigid3DPerspectiveTransformPython
        try:
            _mod = imp.load_module('_itkRigid3DPerspectiveTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRigid3DPerspectiveTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRigid3DPerspectiveTransformPython
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
import itkVersorPython
import itkMatrixPython
import itkPointPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import ITKCommonBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython

def itkRigid3DPerspectiveTransformD_New():
  return itkRigid3DPerspectiveTransformD.New()

class itkRigid3DPerspectiveTransformD(itkTransformBasePython.itkTransformD32):
    """Proxy of C++ itkRigid3DPerspectiveTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRigid3DPerspectiveTransformD_Pointer":
        """__New_orig__() -> itkRigid3DPerspectiveTransformD_Pointer"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRigid3DPerspectiveTransformD_Pointer":
        """Clone(itkRigid3DPerspectiveTransformD self) -> itkRigid3DPerspectiveTransformD_Pointer"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_Clone(self)


    def GetOffset(self) -> "itkVectorD3 const &":
        """GetOffset(itkRigid3DPerspectiveTransformD self) -> itkVectorD3"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetOffset(self)


    def GetRotation(self) -> "itkVersorD const &":
        """GetRotation(itkRigid3DPerspectiveTransformD self) -> itkVersorD"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotation(self)


    def SetOffset(self, offset: 'itkVectorD3') -> "void":
        """SetOffset(itkRigid3DPerspectiveTransformD self, itkVectorD3 offset)"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetOffset(self, offset)


    def SetRotation(self, *args) -> "void":
        """
        SetRotation(itkRigid3DPerspectiveTransformD self, itkVersorD rotation)
        SetRotation(itkRigid3DPerspectiveTransformD self, itkVectorD3 axis, double angle)
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetRotation(self, *args)


    def SetFocalDistance(self, focalDistance: 'double') -> "void":
        """SetFocalDistance(itkRigid3DPerspectiveTransformD self, double focalDistance)"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFocalDistance(self, focalDistance)


    def GetFocalDistance(self) -> "double":
        """GetFocalDistance(itkRigid3DPerspectiveTransformD self) -> double"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFocalDistance(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkRigid3DPerspectiveTransformD self, itkVectorD3 arg0) -> itkVectorD2
        TransformVector(itkRigid3DPerspectiveTransformD self, vnl_vector_fixed< double,3 > const & arg0) -> vnl_vector_fixed< double,2 >
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_TransformVector(self, *args)


    def GetRotationMatrix(self) -> "itkMatrixD33 const &":
        """GetRotationMatrix(itkRigid3DPerspectiveTransformD self) -> itkMatrixD33"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotationMatrix(self)


    def ComputeMatrix(self) -> "void":
        """ComputeMatrix(itkRigid3DPerspectiveTransformD self)"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_ComputeMatrix(self)


    def GetFixedOffset(self) -> "itkVectorD3 const &":
        """GetFixedOffset(itkRigid3DPerspectiveTransformD self) -> itkVectorD3"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFixedOffset(self)


    def SetFixedOffset(self, _arg: 'itkVectorD3') -> "void":
        """SetFixedOffset(itkRigid3DPerspectiveTransformD self, itkVectorD3 _arg)"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFixedOffset(self, _arg)


    def SetCenterOfRotation(self, _arg: 'itkPointD3') -> "void":
        """SetCenterOfRotation(itkRigid3DPerspectiveTransformD self, itkPointD3 _arg)"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetCenterOfRotation(self, _arg)


    def GetCenterOfRotation(self) -> "itkPointD3 const &":
        """GetCenterOfRotation(itkRigid3DPerspectiveTransformD self) -> itkPointD3"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetCenterOfRotation(self)

    __swig_destroy__ = _itkRigid3DPerspectiveTransformPython.delete_itkRigid3DPerspectiveTransformD

    def cast(obj: 'itkLightObject') -> "itkRigid3DPerspectiveTransformD *":
        """cast(itkLightObject obj) -> itkRigid3DPerspectiveTransformD"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRigid3DPerspectiveTransformD *":
        """GetPointer(itkRigid3DPerspectiveTransformD self) -> itkRigid3DPerspectiveTransformD"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRigid3DPerspectiveTransformD

        Create a new object of the class itkRigid3DPerspectiveTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid3DPerspectiveTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRigid3DPerspectiveTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRigid3DPerspectiveTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRigid3DPerspectiveTransformD.Clone = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_Clone, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetFocalDistance = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFocalDistance, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetFocalDistance = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFocalDistance, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.TransformVector = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_TransformVector, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetRotationMatrix = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotationMatrix, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.ComputeMatrix = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_ComputeMatrix, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetFixedOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFixedOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetFixedOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFixedOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetCenterOfRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetCenterOfRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetCenterOfRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetCenterOfRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetPointer = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetPointer, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD_swigregister = _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_swigregister
itkRigid3DPerspectiveTransformD_swigregister(itkRigid3DPerspectiveTransformD)

def itkRigid3DPerspectiveTransformD___New_orig__() -> "itkRigid3DPerspectiveTransformD_Pointer":
    """itkRigid3DPerspectiveTransformD___New_orig__() -> itkRigid3DPerspectiveTransformD_Pointer"""
    return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD___New_orig__()

def itkRigid3DPerspectiveTransformD_cast(obj: 'itkLightObject') -> "itkRigid3DPerspectiveTransformD *":
    """itkRigid3DPerspectiveTransformD_cast(itkLightObject obj) -> itkRigid3DPerspectiveTransformD"""
    return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_cast(obj)



