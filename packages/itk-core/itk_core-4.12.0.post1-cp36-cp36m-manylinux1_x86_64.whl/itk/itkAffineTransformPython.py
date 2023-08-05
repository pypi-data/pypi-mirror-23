# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAffineTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkAffineTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkAffineTransformPython')
    _itkAffineTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAffineTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkAffineTransformPython
            return _itkAffineTransformPython
        try:
            _mod = imp.load_module('_itkAffineTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkAffineTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAffineTransformPython
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


import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkPointPython
import itkOptimizerParametersPython
import ITKCommonBasePython
import itkArrayPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkArray2DPython

def itkAffineTransformD3_New():
  return itkAffineTransformD3.New()


def itkAffineTransformD2_New():
  return itkAffineTransformD2.New()

class itkAffineTransformD2(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD22):
    """Proxy of C++ itkAffineTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAffineTransformD2_Pointer":
        """__New_orig__() -> itkAffineTransformD2_Pointer"""
        return _itkAffineTransformPython.itkAffineTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAffineTransformD2_Pointer":
        """Clone(itkAffineTransformD2 self) -> itkAffineTransformD2_Pointer"""
        return _itkAffineTransformPython.itkAffineTransformD2_Clone(self)


    def Translate(self, offset: 'itkVectorD2', pre: 'bool'=False) -> "void":
        """
        Translate(itkAffineTransformD2 self, itkVectorD2 offset, bool pre=False)
        Translate(itkAffineTransformD2 self, itkVectorD2 offset)
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Translate(self, offset, pre)


    def Scale(self, *args) -> "void":
        """
        Scale(itkAffineTransformD2 self, itkVectorD2 factor, bool pre=False)
        Scale(itkAffineTransformD2 self, itkVectorD2 factor)
        Scale(itkAffineTransformD2 self, double const & factor, bool pre=False)
        Scale(itkAffineTransformD2 self, double const & factor)
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Scale(self, *args)


    def Rotate(self, axis1: 'int', axis2: 'int', angle: 'double', pre: 'bool'=False) -> "void":
        """
        Rotate(itkAffineTransformD2 self, int axis1, int axis2, double angle, bool pre=False)
        Rotate(itkAffineTransformD2 self, int axis1, int axis2, double angle)
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Rotate(self, axis1, axis2, angle, pre)


    def Rotate2D(self, angle: 'double', pre: 'bool'=False) -> "void":
        """
        Rotate2D(itkAffineTransformD2 self, double angle, bool pre=False)
        Rotate2D(itkAffineTransformD2 self, double angle)
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Rotate2D(self, angle, pre)


    def Rotate3D(self, axis: 'itkVectorD2', angle: 'double', pre: 'bool'=False) -> "void":
        """
        Rotate3D(itkAffineTransformD2 self, itkVectorD2 axis, double angle, bool pre=False)
        Rotate3D(itkAffineTransformD2 self, itkVectorD2 axis, double angle)
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Rotate3D(self, axis, angle, pre)


    def Shear(self, axis1: 'int', axis2: 'int', coef: 'double', pre: 'bool'=False) -> "void":
        """
        Shear(itkAffineTransformD2 self, int axis1, int axis2, double coef, bool pre=False)
        Shear(itkAffineTransformD2 self, int axis1, int axis2, double coef)
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Shear(self, axis1, axis2, coef, pre)


    def GetInverse(self, inverse: 'itkAffineTransformD2') -> "bool":
        """GetInverse(itkAffineTransformD2 self, itkAffineTransformD2 inverse) -> bool"""
        return _itkAffineTransformPython.itkAffineTransformD2_GetInverse(self, inverse)


    def BackTransform(self, *args) -> "itkCovariantVectorD2":
        """
        BackTransform(itkAffineTransformD2 self, itkPointD2 point) -> itkPointD2
        BackTransform(itkAffineTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        BackTransform(itkAffineTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        BackTransform(itkAffineTransformD2 self, itkCovariantVectorD2 vector) -> itkCovariantVectorD2
        """
        return _itkAffineTransformPython.itkAffineTransformD2_BackTransform(self, *args)


    def BackTransformPoint(self, point: 'itkPointD2') -> "itkPointD2":
        """BackTransformPoint(itkAffineTransformD2 self, itkPointD2 point) -> itkPointD2"""
        return _itkAffineTransformPython.itkAffineTransformD2_BackTransformPoint(self, point)


    def Metric(self, *args) -> "double":
        """
        Metric(itkAffineTransformD2 self, itkAffineTransformD2 other) -> double
        Metric(itkAffineTransformD2 self) -> double
        """
        return _itkAffineTransformPython.itkAffineTransformD2_Metric(self, *args)

    __swig_destroy__ = _itkAffineTransformPython.delete_itkAffineTransformD2

    def cast(obj: 'itkLightObject') -> "itkAffineTransformD2 *":
        """cast(itkLightObject obj) -> itkAffineTransformD2"""
        return _itkAffineTransformPython.itkAffineTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAffineTransformD2 *":
        """GetPointer(itkAffineTransformD2 self) -> itkAffineTransformD2"""
        return _itkAffineTransformPython.itkAffineTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAffineTransformD2

        Create a new object of the class itkAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAffineTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAffineTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAffineTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAffineTransformD2.Clone = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Clone, None, itkAffineTransformD2)
itkAffineTransformD2.Translate = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Translate, None, itkAffineTransformD2)
itkAffineTransformD2.Scale = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Scale, None, itkAffineTransformD2)
itkAffineTransformD2.Rotate = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Rotate, None, itkAffineTransformD2)
itkAffineTransformD2.Rotate2D = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Rotate2D, None, itkAffineTransformD2)
itkAffineTransformD2.Rotate3D = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Rotate3D, None, itkAffineTransformD2)
itkAffineTransformD2.Shear = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Shear, None, itkAffineTransformD2)
itkAffineTransformD2.GetInverse = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_GetInverse, None, itkAffineTransformD2)
itkAffineTransformD2.BackTransform = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_BackTransform, None, itkAffineTransformD2)
itkAffineTransformD2.BackTransformPoint = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_BackTransformPoint, None, itkAffineTransformD2)
itkAffineTransformD2.Metric = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_Metric, None, itkAffineTransformD2)
itkAffineTransformD2.GetPointer = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD2_GetPointer, None, itkAffineTransformD2)
itkAffineTransformD2_swigregister = _itkAffineTransformPython.itkAffineTransformD2_swigregister
itkAffineTransformD2_swigregister(itkAffineTransformD2)

def itkAffineTransformD2___New_orig__() -> "itkAffineTransformD2_Pointer":
    """itkAffineTransformD2___New_orig__() -> itkAffineTransformD2_Pointer"""
    return _itkAffineTransformPython.itkAffineTransformD2___New_orig__()

def itkAffineTransformD2_cast(obj: 'itkLightObject') -> "itkAffineTransformD2 *":
    """itkAffineTransformD2_cast(itkLightObject obj) -> itkAffineTransformD2"""
    return _itkAffineTransformPython.itkAffineTransformD2_cast(obj)

class itkAffineTransformD3(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD33):
    """Proxy of C++ itkAffineTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAffineTransformD3_Pointer":
        """__New_orig__() -> itkAffineTransformD3_Pointer"""
        return _itkAffineTransformPython.itkAffineTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAffineTransformD3_Pointer":
        """Clone(itkAffineTransformD3 self) -> itkAffineTransformD3_Pointer"""
        return _itkAffineTransformPython.itkAffineTransformD3_Clone(self)


    def Translate(self, offset: 'itkVectorD3', pre: 'bool'=False) -> "void":
        """
        Translate(itkAffineTransformD3 self, itkVectorD3 offset, bool pre=False)
        Translate(itkAffineTransformD3 self, itkVectorD3 offset)
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Translate(self, offset, pre)


    def Scale(self, *args) -> "void":
        """
        Scale(itkAffineTransformD3 self, itkVectorD3 factor, bool pre=False)
        Scale(itkAffineTransformD3 self, itkVectorD3 factor)
        Scale(itkAffineTransformD3 self, double const & factor, bool pre=False)
        Scale(itkAffineTransformD3 self, double const & factor)
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Scale(self, *args)


    def Rotate(self, axis1: 'int', axis2: 'int', angle: 'double', pre: 'bool'=False) -> "void":
        """
        Rotate(itkAffineTransformD3 self, int axis1, int axis2, double angle, bool pre=False)
        Rotate(itkAffineTransformD3 self, int axis1, int axis2, double angle)
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Rotate(self, axis1, axis2, angle, pre)


    def Rotate2D(self, angle: 'double', pre: 'bool'=False) -> "void":
        """
        Rotate2D(itkAffineTransformD3 self, double angle, bool pre=False)
        Rotate2D(itkAffineTransformD3 self, double angle)
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Rotate2D(self, angle, pre)


    def Rotate3D(self, axis: 'itkVectorD3', angle: 'double', pre: 'bool'=False) -> "void":
        """
        Rotate3D(itkAffineTransformD3 self, itkVectorD3 axis, double angle, bool pre=False)
        Rotate3D(itkAffineTransformD3 self, itkVectorD3 axis, double angle)
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Rotate3D(self, axis, angle, pre)


    def Shear(self, axis1: 'int', axis2: 'int', coef: 'double', pre: 'bool'=False) -> "void":
        """
        Shear(itkAffineTransformD3 self, int axis1, int axis2, double coef, bool pre=False)
        Shear(itkAffineTransformD3 self, int axis1, int axis2, double coef)
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Shear(self, axis1, axis2, coef, pre)


    def GetInverse(self, inverse: 'itkAffineTransformD3') -> "bool":
        """GetInverse(itkAffineTransformD3 self, itkAffineTransformD3 inverse) -> bool"""
        return _itkAffineTransformPython.itkAffineTransformD3_GetInverse(self, inverse)


    def BackTransform(self, *args) -> "itkCovariantVectorD3":
        """
        BackTransform(itkAffineTransformD3 self, itkPointD3 point) -> itkPointD3
        BackTransform(itkAffineTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        BackTransform(itkAffineTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        BackTransform(itkAffineTransformD3 self, itkCovariantVectorD3 vector) -> itkCovariantVectorD3
        """
        return _itkAffineTransformPython.itkAffineTransformD3_BackTransform(self, *args)


    def BackTransformPoint(self, point: 'itkPointD3') -> "itkPointD3":
        """BackTransformPoint(itkAffineTransformD3 self, itkPointD3 point) -> itkPointD3"""
        return _itkAffineTransformPython.itkAffineTransformD3_BackTransformPoint(self, point)


    def Metric(self, *args) -> "double":
        """
        Metric(itkAffineTransformD3 self, itkAffineTransformD3 other) -> double
        Metric(itkAffineTransformD3 self) -> double
        """
        return _itkAffineTransformPython.itkAffineTransformD3_Metric(self, *args)

    __swig_destroy__ = _itkAffineTransformPython.delete_itkAffineTransformD3

    def cast(obj: 'itkLightObject') -> "itkAffineTransformD3 *":
        """cast(itkLightObject obj) -> itkAffineTransformD3"""
        return _itkAffineTransformPython.itkAffineTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkAffineTransformD3 *":
        """GetPointer(itkAffineTransformD3 self) -> itkAffineTransformD3"""
        return _itkAffineTransformPython.itkAffineTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkAffineTransformD3

        Create a new object of the class itkAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAffineTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAffineTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAffineTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAffineTransformD3.Clone = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Clone, None, itkAffineTransformD3)
itkAffineTransformD3.Translate = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Translate, None, itkAffineTransformD3)
itkAffineTransformD3.Scale = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Scale, None, itkAffineTransformD3)
itkAffineTransformD3.Rotate = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Rotate, None, itkAffineTransformD3)
itkAffineTransformD3.Rotate2D = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Rotate2D, None, itkAffineTransformD3)
itkAffineTransformD3.Rotate3D = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Rotate3D, None, itkAffineTransformD3)
itkAffineTransformD3.Shear = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Shear, None, itkAffineTransformD3)
itkAffineTransformD3.GetInverse = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_GetInverse, None, itkAffineTransformD3)
itkAffineTransformD3.BackTransform = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_BackTransform, None, itkAffineTransformD3)
itkAffineTransformD3.BackTransformPoint = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_BackTransformPoint, None, itkAffineTransformD3)
itkAffineTransformD3.Metric = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_Metric, None, itkAffineTransformD3)
itkAffineTransformD3.GetPointer = new_instancemethod(_itkAffineTransformPython.itkAffineTransformD3_GetPointer, None, itkAffineTransformD3)
itkAffineTransformD3_swigregister = _itkAffineTransformPython.itkAffineTransformD3_swigregister
itkAffineTransformD3_swigregister(itkAffineTransformD3)

def itkAffineTransformD3___New_orig__() -> "itkAffineTransformD3_Pointer":
    """itkAffineTransformD3___New_orig__() -> itkAffineTransformD3_Pointer"""
    return _itkAffineTransformPython.itkAffineTransformD3___New_orig__()

def itkAffineTransformD3_cast(obj: 'itkLightObject') -> "itkAffineTransformD3 *":
    """itkAffineTransformD3_cast(itkLightObject obj) -> itkAffineTransformD3"""
    return _itkAffineTransformPython.itkAffineTransformD3_cast(obj)



