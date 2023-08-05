# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSimilarity2DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSimilarity2DTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSimilarity2DTransformPython')
    _itkSimilarity2DTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSimilarity2DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkSimilarity2DTransformPython
            return _itkSimilarity2DTransformPython
        try:
            _mod = imp.load_module('_itkSimilarity2DTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSimilarity2DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSimilarity2DTransformPython
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
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import itkOptimizerParametersPython
import itkArrayPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkRigid2DTransformPython
import itkMatrixOffsetTransformBasePython

def itkSimilarity2DTransformD_New():
  return itkSimilarity2DTransformD.New()

class itkSimilarity2DTransformD(itkRigid2DTransformPython.itkRigid2DTransformD):
    """Proxy of C++ itkSimilarity2DTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSimilarity2DTransformD_Pointer":
        """__New_orig__() -> itkSimilarity2DTransformD_Pointer"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSimilarity2DTransformD_Pointer":
        """Clone(itkSimilarity2DTransformD self) -> itkSimilarity2DTransformD_Pointer"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_Clone(self)


    def SetScale(self, scale: 'double') -> "void":
        """SetScale(itkSimilarity2DTransformD self, double scale)"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_SetScale(self, scale)


    def GetScale(self) -> "double const &":
        """GetScale(itkSimilarity2DTransformD self) -> double const &"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetScale(self)


    def CloneInverseTo(self, newinverse: 'itkSimilarity2DTransformD_Pointer &') -> "void":
        """CloneInverseTo(itkSimilarity2DTransformD self, itkSimilarity2DTransformD_Pointer & newinverse)"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_CloneInverseTo(self, newinverse)


    def GetInverse(self, inverse: 'itkSimilarity2DTransformD') -> "bool":
        """GetInverse(itkSimilarity2DTransformD self, itkSimilarity2DTransformD inverse) -> bool"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetInverse(self, inverse)


    def CloneTo(self, clone: 'itkSimilarity2DTransformD_Pointer &') -> "void":
        """CloneTo(itkSimilarity2DTransformD self, itkSimilarity2DTransformD_Pointer & clone)"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_CloneTo(self, clone)


    def SetMatrix(self, *args) -> "void":
        """
        SetMatrix(itkSimilarity2DTransformD self, itkMatrixD22 matrix)
        SetMatrix(itkSimilarity2DTransformD self, itkMatrixD22 matrix, double const tolerance)
        """
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_SetMatrix(self, *args)

    __swig_destroy__ = _itkSimilarity2DTransformPython.delete_itkSimilarity2DTransformD

    def cast(obj: 'itkLightObject') -> "itkSimilarity2DTransformD *":
        """cast(itkLightObject obj) -> itkSimilarity2DTransformD"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkSimilarity2DTransformD *":
        """GetPointer(itkSimilarity2DTransformD self) -> itkSimilarity2DTransformD"""
        return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkSimilarity2DTransformD

        Create a new object of the class itkSimilarity2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarity2DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarity2DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarity2DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSimilarity2DTransformD.Clone = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_Clone, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.SetScale = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_SetScale, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.GetScale = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetScale, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.CloneInverseTo = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_CloneInverseTo, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.GetInverse = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetInverse, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.CloneTo = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_CloneTo, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.SetMatrix = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_SetMatrix, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD.GetPointer = new_instancemethod(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetPointer, None, itkSimilarity2DTransformD)
itkSimilarity2DTransformD_swigregister = _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_swigregister
itkSimilarity2DTransformD_swigregister(itkSimilarity2DTransformD)

def itkSimilarity2DTransformD___New_orig__() -> "itkSimilarity2DTransformD_Pointer":
    """itkSimilarity2DTransformD___New_orig__() -> itkSimilarity2DTransformD_Pointer"""
    return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD___New_orig__()

def itkSimilarity2DTransformD_cast(obj: 'itkLightObject') -> "itkSimilarity2DTransformD *":
    """itkSimilarity2DTransformD_cast(itkLightObject obj) -> itkSimilarity2DTransformD"""
    return _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_cast(obj)



