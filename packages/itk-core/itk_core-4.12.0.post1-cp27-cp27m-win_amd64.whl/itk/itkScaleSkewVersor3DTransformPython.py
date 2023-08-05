# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkScaleSkewVersor3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkScaleSkewVersor3DTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkScaleSkewVersor3DTransformPython')
    _itkScaleSkewVersor3DTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkScaleSkewVersor3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkScaleSkewVersor3DTransformPython
            return _itkScaleSkewVersor3DTransformPython
        try:
            _mod = imp.load_module('_itkScaleSkewVersor3DTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkScaleSkewVersor3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkScaleSkewVersor3DTransformPython
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
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import ITKCommonBasePython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkArray2DPython
import itkVersorRigid3DTransformPython
import itkVersorTransformPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkVersorPython

def itkScaleSkewVersor3DTransformD_New():
  return itkScaleSkewVersor3DTransformD.New()

class itkScaleSkewVersor3DTransformD(itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD):
    """Proxy of C++ itkScaleSkewVersor3DTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkScaleSkewVersor3DTransformD_Pointer"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkScaleSkewVersor3DTransformD self) -> itkScaleSkewVersor3DTransformD_Pointer"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_Clone(self)


    def SetMatrix(self, *args):
        """
        SetMatrix(itkScaleSkewVersor3DTransformD self, itkMatrixD33 matrix)
        SetMatrix(itkScaleSkewVersor3DTransformD self, itkMatrixD33 matrix, double const tolerance)
        """
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetMatrix(self, *args)


    def SetScale(self, scale):
        """SetScale(itkScaleSkewVersor3DTransformD self, itkVectorD3 scale)"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetScale(self, scale)


    def GetScale(self):
        """GetScale(itkScaleSkewVersor3DTransformD self) -> itkVectorD3"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetScale(self)


    def SetSkew(self, skew):
        """SetSkew(itkScaleSkewVersor3DTransformD self, itkVectorD6 skew)"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetSkew(self, skew)


    def GetSkew(self):
        """GetSkew(itkScaleSkewVersor3DTransformD self) -> itkVectorD6"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetSkew(self)

    __swig_destroy__ = _itkScaleSkewVersor3DTransformPython.delete_itkScaleSkewVersor3DTransformD

    def cast(obj):
        """cast(itkLightObject obj) -> itkScaleSkewVersor3DTransformD"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkScaleSkewVersor3DTransformD self) -> itkScaleSkewVersor3DTransformD"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkScaleSkewVersor3DTransformD

        Create a new object of the class itkScaleSkewVersor3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleSkewVersor3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleSkewVersor3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleSkewVersor3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleSkewVersor3DTransformD.Clone = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_Clone, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.SetMatrix = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetMatrix, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.SetScale = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetScale, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.GetScale = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetScale, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.SetSkew = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetSkew, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.GetSkew = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetSkew, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.GetPointer = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetPointer, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD_swigregister = _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_swigregister
itkScaleSkewVersor3DTransformD_swigregister(itkScaleSkewVersor3DTransformD)

def itkScaleSkewVersor3DTransformD___New_orig__():
    """itkScaleSkewVersor3DTransformD___New_orig__() -> itkScaleSkewVersor3DTransformD_Pointer"""
    return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD___New_orig__()

def itkScaleSkewVersor3DTransformD_cast(obj):
    """itkScaleSkewVersor3DTransformD_cast(itkLightObject obj) -> itkScaleSkewVersor3DTransformD"""
    return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_cast(obj)



