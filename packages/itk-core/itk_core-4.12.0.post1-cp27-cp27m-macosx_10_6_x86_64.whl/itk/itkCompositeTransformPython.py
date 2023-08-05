# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCompositeTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkCompositeTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkCompositeTransformPython')
    _itkCompositeTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCompositeTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkCompositeTransformPython
            return _itkCompositeTransformPython
        try:
            _mod = imp.load_module('_itkCompositeTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkCompositeTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCompositeTransformPython
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
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkMultiTransformPython

def itkCompositeTransformD3_New():
  return itkCompositeTransformD3.New()


def itkCompositeTransformD2_New():
  return itkCompositeTransformD2.New()

class itkCompositeTransformD2(itkMultiTransformPython.itkMultiTransformD22):
    """Proxy of C++ itkCompositeTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkCompositeTransformD2_Pointer"""
        return _itkCompositeTransformPython.itkCompositeTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkCompositeTransformD2 self) -> itkCompositeTransformD2_Pointer"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_Clone(self)


    def SetNthTransformToOptimize(self, i, state):
        """SetNthTransformToOptimize(itkCompositeTransformD2 self, unsigned long i, bool state)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimize(self, i, state)


    def SetNthTransformToOptimizeOn(self, i):
        """SetNthTransformToOptimizeOn(itkCompositeTransformD2 self, unsigned long i)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOn(self, i)


    def SetNthTransformToOptimizeOff(self, i):
        """SetNthTransformToOptimizeOff(itkCompositeTransformD2 self, unsigned long i)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOff(self, i)


    def SetAllTransformsToOptimize(self, state):
        """SetAllTransformsToOptimize(itkCompositeTransformD2 self, bool state)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimize(self, state)


    def SetAllTransformsToOptimizeOn(self):
        """SetAllTransformsToOptimizeOn(itkCompositeTransformD2 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOn(self)


    def SetAllTransformsToOptimizeOff(self):
        """SetAllTransformsToOptimizeOff(itkCompositeTransformD2 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOff(self)


    def SetOnlyMostRecentTransformToOptimizeOn(self):
        """SetOnlyMostRecentTransformToOptimizeOn(itkCompositeTransformD2 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_SetOnlyMostRecentTransformToOptimizeOn(self)


    def GetNthTransformToOptimize(self, i):
        """GetNthTransformToOptimize(itkCompositeTransformD2 self, unsigned long i) -> bool"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_GetNthTransformToOptimize(self, i)


    def GetTransformsToOptimizeFlags(self):
        """GetTransformsToOptimizeFlags(itkCompositeTransformD2 self) -> std::deque< bool > const &"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_GetTransformsToOptimizeFlags(self)


    def GetInverse(self, inverse):
        """GetInverse(itkCompositeTransformD2 self, itkCompositeTransformD2 inverse) -> bool"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_GetInverse(self, inverse)


    def TransformVector(self, *args):
        """
        TransformVector(itkCompositeTransformD2 self, itkVectorD2 arg0) -> itkVectorD2
        TransformVector(itkCompositeTransformD2 self, vnl_vector_fixed< double,2 > const & inputVector) -> vnl_vector_fixed< double,2 >
        TransformVector(itkCompositeTransformD2 self, itkVariableLengthVectorD inputVector) -> itkVariableLengthVectorD
        TransformVector(itkCompositeTransformD2 self, itkVectorD2 inputVector, itkPointD2 inputPoint) -> itkVectorD2
        TransformVector(itkCompositeTransformD2 self, vnl_vector_fixed< double,2 > const & inputVector, itkPointD2 inputPoint) -> vnl_vector_fixed< double,2 >
        TransformVector(itkCompositeTransformD2 self, itkVariableLengthVectorD inputVector, itkPointD2 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD2_TransformVector(self, *args)


    def TransformCovariantVector(self, *args):
        """
        TransformCovariantVector(itkCompositeTransformD2 self, itkCovariantVectorD2 arg0) -> itkCovariantVectorD2
        TransformCovariantVector(itkCompositeTransformD2 self, itkVariableLengthVectorD arg0) -> itkVariableLengthVectorD
        TransformCovariantVector(itkCompositeTransformD2 self, itkCovariantVectorD2 inputVector, itkPointD2 inputPoint) -> itkCovariantVectorD2
        TransformCovariantVector(itkCompositeTransformD2 self, itkVariableLengthVectorD inputVector, itkPointD2 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD2_TransformCovariantVector(self, *args)


    def TransformDiffusionTensor3D(self, *args):
        """
        TransformDiffusionTensor3D(itkCompositeTransformD2 self, itkDiffusionTensor3DD inputTensor) -> itkDiffusionTensor3DD
        TransformDiffusionTensor3D(itkCompositeTransformD2 self, itkVariableLengthVectorD inputTensor) -> itkVariableLengthVectorD
        TransformDiffusionTensor3D(itkCompositeTransformD2 self, itkDiffusionTensor3DD inputTensor, itkPointD2 inputPoint) -> itkDiffusionTensor3DD
        TransformDiffusionTensor3D(itkCompositeTransformD2 self, itkVariableLengthVectorD inputTensor, itkPointD2 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD2_TransformDiffusionTensor3D(self, *args)


    def TransformSymmetricSecondRankTensor(self, *args):
        """
        TransformSymmetricSecondRankTensor(itkCompositeTransformD2 self, itkSymmetricSecondRankTensorD2 inputTensor) -> itkSymmetricSecondRankTensorD2
        TransformSymmetricSecondRankTensor(itkCompositeTransformD2 self, itkVariableLengthVectorD inputTensor) -> itkVariableLengthVectorD
        TransformSymmetricSecondRankTensor(itkCompositeTransformD2 self, itkSymmetricSecondRankTensorD2 inputTensor, itkPointD2 inputPoint) -> itkSymmetricSecondRankTensorD2
        TransformSymmetricSecondRankTensor(itkCompositeTransformD2 self, itkVariableLengthVectorD inputTensor, itkPointD2 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD2_TransformSymmetricSecondRankTensor(self, *args)


    def UpdateTransformParameters(self, update, factor=1.):
        """
        UpdateTransformParameters(itkCompositeTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkCompositeTransformD2 self, itkArrayD update)
        """
        return _itkCompositeTransformPython.itkCompositeTransformD2_UpdateTransformParameters(self, update, factor)


    def FlattenTransformQueue(self):
        """FlattenTransformQueue(itkCompositeTransformD2 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_FlattenTransformQueue(self)

    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkCompositeTransformD2"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkCompositeTransformD2 self) -> itkCompositeTransformD2"""
        return _itkCompositeTransformPython.itkCompositeTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCompositeTransformD2

        Create a new object of the class itkCompositeTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCompositeTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCompositeTransformD2.Clone = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_Clone, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetNthTransformToOptimize = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimize, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetNthTransformToOptimizeOn = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOn, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetNthTransformToOptimizeOff = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOff, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetAllTransformsToOptimize = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimize, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetAllTransformsToOptimizeOn = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOn, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetAllTransformsToOptimizeOff = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOff, None, itkCompositeTransformD2)
itkCompositeTransformD2.SetOnlyMostRecentTransformToOptimizeOn = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_SetOnlyMostRecentTransformToOptimizeOn, None, itkCompositeTransformD2)
itkCompositeTransformD2.GetNthTransformToOptimize = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_GetNthTransformToOptimize, None, itkCompositeTransformD2)
itkCompositeTransformD2.GetTransformsToOptimizeFlags = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_GetTransformsToOptimizeFlags, None, itkCompositeTransformD2)
itkCompositeTransformD2.GetInverse = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_GetInverse, None, itkCompositeTransformD2)
itkCompositeTransformD2.TransformVector = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_TransformVector, None, itkCompositeTransformD2)
itkCompositeTransformD2.TransformCovariantVector = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_TransformCovariantVector, None, itkCompositeTransformD2)
itkCompositeTransformD2.TransformDiffusionTensor3D = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_TransformDiffusionTensor3D, None, itkCompositeTransformD2)
itkCompositeTransformD2.TransformSymmetricSecondRankTensor = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_TransformSymmetricSecondRankTensor, None, itkCompositeTransformD2)
itkCompositeTransformD2.UpdateTransformParameters = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_UpdateTransformParameters, None, itkCompositeTransformD2)
itkCompositeTransformD2.FlattenTransformQueue = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_FlattenTransformQueue, None, itkCompositeTransformD2)
itkCompositeTransformD2.GetPointer = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD2_GetPointer, None, itkCompositeTransformD2)
itkCompositeTransformD2_swigregister = _itkCompositeTransformPython.itkCompositeTransformD2_swigregister
itkCompositeTransformD2_swigregister(itkCompositeTransformD2)

def itkCompositeTransformD2___New_orig__():
    """itkCompositeTransformD2___New_orig__() -> itkCompositeTransformD2_Pointer"""
    return _itkCompositeTransformPython.itkCompositeTransformD2___New_orig__()

def itkCompositeTransformD2_cast(obj):
    """itkCompositeTransformD2_cast(itkLightObject obj) -> itkCompositeTransformD2"""
    return _itkCompositeTransformPython.itkCompositeTransformD2_cast(obj)

class itkCompositeTransformD3(itkMultiTransformPython.itkMultiTransformD33):
    """Proxy of C++ itkCompositeTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkCompositeTransformD3_Pointer"""
        return _itkCompositeTransformPython.itkCompositeTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkCompositeTransformD3 self) -> itkCompositeTransformD3_Pointer"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_Clone(self)


    def SetNthTransformToOptimize(self, i, state):
        """SetNthTransformToOptimize(itkCompositeTransformD3 self, unsigned long i, bool state)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimize(self, i, state)


    def SetNthTransformToOptimizeOn(self, i):
        """SetNthTransformToOptimizeOn(itkCompositeTransformD3 self, unsigned long i)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOn(self, i)


    def SetNthTransformToOptimizeOff(self, i):
        """SetNthTransformToOptimizeOff(itkCompositeTransformD3 self, unsigned long i)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOff(self, i)


    def SetAllTransformsToOptimize(self, state):
        """SetAllTransformsToOptimize(itkCompositeTransformD3 self, bool state)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimize(self, state)


    def SetAllTransformsToOptimizeOn(self):
        """SetAllTransformsToOptimizeOn(itkCompositeTransformD3 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOn(self)


    def SetAllTransformsToOptimizeOff(self):
        """SetAllTransformsToOptimizeOff(itkCompositeTransformD3 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOff(self)


    def SetOnlyMostRecentTransformToOptimizeOn(self):
        """SetOnlyMostRecentTransformToOptimizeOn(itkCompositeTransformD3 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_SetOnlyMostRecentTransformToOptimizeOn(self)


    def GetNthTransformToOptimize(self, i):
        """GetNthTransformToOptimize(itkCompositeTransformD3 self, unsigned long i) -> bool"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_GetNthTransformToOptimize(self, i)


    def GetTransformsToOptimizeFlags(self):
        """GetTransformsToOptimizeFlags(itkCompositeTransformD3 self) -> std::deque< bool > const &"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_GetTransformsToOptimizeFlags(self)


    def GetInverse(self, inverse):
        """GetInverse(itkCompositeTransformD3 self, itkCompositeTransformD3 inverse) -> bool"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_GetInverse(self, inverse)


    def TransformVector(self, *args):
        """
        TransformVector(itkCompositeTransformD3 self, itkVectorD3 arg0) -> itkVectorD3
        TransformVector(itkCompositeTransformD3 self, vnl_vector_fixed< double,3 > const & inputVector) -> vnl_vector_fixed< double,3 >
        TransformVector(itkCompositeTransformD3 self, itkVariableLengthVectorD inputVector) -> itkVariableLengthVectorD
        TransformVector(itkCompositeTransformD3 self, itkVectorD3 inputVector, itkPointD3 inputPoint) -> itkVectorD3
        TransformVector(itkCompositeTransformD3 self, vnl_vector_fixed< double,3 > const & inputVector, itkPointD3 inputPoint) -> vnl_vector_fixed< double,3 >
        TransformVector(itkCompositeTransformD3 self, itkVariableLengthVectorD inputVector, itkPointD3 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD3_TransformVector(self, *args)


    def TransformCovariantVector(self, *args):
        """
        TransformCovariantVector(itkCompositeTransformD3 self, itkCovariantVectorD3 arg0) -> itkCovariantVectorD3
        TransformCovariantVector(itkCompositeTransformD3 self, itkVariableLengthVectorD arg0) -> itkVariableLengthVectorD
        TransformCovariantVector(itkCompositeTransformD3 self, itkCovariantVectorD3 inputVector, itkPointD3 inputPoint) -> itkCovariantVectorD3
        TransformCovariantVector(itkCompositeTransformD3 self, itkVariableLengthVectorD inputVector, itkPointD3 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD3_TransformCovariantVector(self, *args)


    def TransformDiffusionTensor3D(self, *args):
        """
        TransformDiffusionTensor3D(itkCompositeTransformD3 self, itkDiffusionTensor3DD inputTensor) -> itkDiffusionTensor3DD
        TransformDiffusionTensor3D(itkCompositeTransformD3 self, itkVariableLengthVectorD inputTensor) -> itkVariableLengthVectorD
        TransformDiffusionTensor3D(itkCompositeTransformD3 self, itkDiffusionTensor3DD inputTensor, itkPointD3 inputPoint) -> itkDiffusionTensor3DD
        TransformDiffusionTensor3D(itkCompositeTransformD3 self, itkVariableLengthVectorD inputTensor, itkPointD3 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD3_TransformDiffusionTensor3D(self, *args)


    def TransformSymmetricSecondRankTensor(self, *args):
        """
        TransformSymmetricSecondRankTensor(itkCompositeTransformD3 self, itkSymmetricSecondRankTensorD3 inputTensor) -> itkSymmetricSecondRankTensorD3
        TransformSymmetricSecondRankTensor(itkCompositeTransformD3 self, itkVariableLengthVectorD inputTensor) -> itkVariableLengthVectorD
        TransformSymmetricSecondRankTensor(itkCompositeTransformD3 self, itkSymmetricSecondRankTensorD3 inputTensor, itkPointD3 inputPoint) -> itkSymmetricSecondRankTensorD3
        TransformSymmetricSecondRankTensor(itkCompositeTransformD3 self, itkVariableLengthVectorD inputTensor, itkPointD3 inputPoint) -> itkVariableLengthVectorD
        """
        return _itkCompositeTransformPython.itkCompositeTransformD3_TransformSymmetricSecondRankTensor(self, *args)


    def UpdateTransformParameters(self, update, factor=1.):
        """
        UpdateTransformParameters(itkCompositeTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkCompositeTransformD3 self, itkArrayD update)
        """
        return _itkCompositeTransformPython.itkCompositeTransformD3_UpdateTransformParameters(self, update, factor)


    def FlattenTransformQueue(self):
        """FlattenTransformQueue(itkCompositeTransformD3 self)"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_FlattenTransformQueue(self)

    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkCompositeTransformD3"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkCompositeTransformD3 self) -> itkCompositeTransformD3"""
        return _itkCompositeTransformPython.itkCompositeTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCompositeTransformD3

        Create a new object of the class itkCompositeTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCompositeTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCompositeTransformD3.Clone = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_Clone, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetNthTransformToOptimize = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimize, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetNthTransformToOptimizeOn = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOn, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetNthTransformToOptimizeOff = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOff, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetAllTransformsToOptimize = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimize, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetAllTransformsToOptimizeOn = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOn, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetAllTransformsToOptimizeOff = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOff, None, itkCompositeTransformD3)
itkCompositeTransformD3.SetOnlyMostRecentTransformToOptimizeOn = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_SetOnlyMostRecentTransformToOptimizeOn, None, itkCompositeTransformD3)
itkCompositeTransformD3.GetNthTransformToOptimize = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_GetNthTransformToOptimize, None, itkCompositeTransformD3)
itkCompositeTransformD3.GetTransformsToOptimizeFlags = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_GetTransformsToOptimizeFlags, None, itkCompositeTransformD3)
itkCompositeTransformD3.GetInverse = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_GetInverse, None, itkCompositeTransformD3)
itkCompositeTransformD3.TransformVector = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_TransformVector, None, itkCompositeTransformD3)
itkCompositeTransformD3.TransformCovariantVector = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_TransformCovariantVector, None, itkCompositeTransformD3)
itkCompositeTransformD3.TransformDiffusionTensor3D = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_TransformDiffusionTensor3D, None, itkCompositeTransformD3)
itkCompositeTransformD3.TransformSymmetricSecondRankTensor = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_TransformSymmetricSecondRankTensor, None, itkCompositeTransformD3)
itkCompositeTransformD3.UpdateTransformParameters = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_UpdateTransformParameters, None, itkCompositeTransformD3)
itkCompositeTransformD3.FlattenTransformQueue = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_FlattenTransformQueue, None, itkCompositeTransformD3)
itkCompositeTransformD3.GetPointer = new_instancemethod(_itkCompositeTransformPython.itkCompositeTransformD3_GetPointer, None, itkCompositeTransformD3)
itkCompositeTransformD3_swigregister = _itkCompositeTransformPython.itkCompositeTransformD3_swigregister
itkCompositeTransformD3_swigregister(itkCompositeTransformD3)

def itkCompositeTransformD3___New_orig__():
    """itkCompositeTransformD3___New_orig__() -> itkCompositeTransformD3_Pointer"""
    return _itkCompositeTransformPython.itkCompositeTransformD3___New_orig__()

def itkCompositeTransformD3_cast(obj):
    """itkCompositeTransformD3_cast(itkLightObject obj) -> itkCompositeTransformD3"""
    return _itkCompositeTransformPython.itkCompositeTransformD3_cast(obj)



