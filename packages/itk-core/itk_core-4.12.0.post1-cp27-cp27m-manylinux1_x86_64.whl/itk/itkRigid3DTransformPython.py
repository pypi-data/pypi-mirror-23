# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRigid3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRigid3DTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRigid3DTransformPython')
    _itkRigid3DTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRigid3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkRigid3DTransformPython
            return _itkRigid3DTransformPython
        try:
            _mod = imp.load_module('_itkRigid3DTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRigid3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRigid3DTransformPython
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


import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython

def itkRigid3DTransformD_New():
  return itkRigid3DTransformD.New()

class itkRigid3DTransformD(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD33):
    """Proxy of C++ itkRigid3DTransformD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetMatrix(self, *args):
        """
        SetMatrix(itkRigid3DTransformD self, itkMatrixD33 matrix)
        SetMatrix(itkRigid3DTransformD self, itkMatrixD33 matrix, double const tolerance)
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_SetMatrix(self, *args)


    def Translate(self, offset, pre=False):
        """
        Translate(itkRigid3DTransformD self, itkVectorD3 offset, bool pre=False)
        Translate(itkRigid3DTransformD self, itkVectorD3 offset)
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_Translate(self, offset, pre)


    def MatrixIsOrthogonal(self, *args):
        """
        MatrixIsOrthogonal(itkRigid3DTransformD self, itkMatrixD33 matrix, double const tolerance) -> bool
        MatrixIsOrthogonal(itkRigid3DTransformD self, itkMatrixD33 matrix) -> bool
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_MatrixIsOrthogonal(self, *args)


    def BackTransform(self, *args):
        """
        BackTransform(itkRigid3DTransformD self, itkPointD3 point) -> itkPointD3
        BackTransform(itkRigid3DTransformD self, itkVectorD3 vector) -> itkVectorD3
        BackTransform(itkRigid3DTransformD self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        BackTransform(itkRigid3DTransformD self, itkCovariantVectorD3 vector) -> itkCovariantVectorD3
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_BackTransform(self, *args)

    __swig_destroy__ = _itkRigid3DTransformPython.delete_itkRigid3DTransformD

    def cast(obj):
        """cast(itkLightObject obj) -> itkRigid3DTransformD"""
        return _itkRigid3DTransformPython.itkRigid3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkRigid3DTransformD self) -> itkRigid3DTransformD"""
        return _itkRigid3DTransformPython.itkRigid3DTransformD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRigid3DTransformD

        Create a new object of the class itkRigid3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRigid3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRigid3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRigid3DTransformD.SetMatrix = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_SetMatrix, None, itkRigid3DTransformD)
itkRigid3DTransformD.Translate = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_Translate, None, itkRigid3DTransformD)
itkRigid3DTransformD.MatrixIsOrthogonal = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_MatrixIsOrthogonal, None, itkRigid3DTransformD)
itkRigid3DTransformD.BackTransform = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_BackTransform, None, itkRigid3DTransformD)
itkRigid3DTransformD.GetPointer = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_GetPointer, None, itkRigid3DTransformD)
itkRigid3DTransformD_swigregister = _itkRigid3DTransformPython.itkRigid3DTransformD_swigregister
itkRigid3DTransformD_swigregister(itkRigid3DTransformD)

def itkRigid3DTransformD_cast(obj):
    """itkRigid3DTransformD_cast(itkLightObject obj) -> itkRigid3DTransformD"""
    return _itkRigid3DTransformPython.itkRigid3DTransformD_cast(obj)



