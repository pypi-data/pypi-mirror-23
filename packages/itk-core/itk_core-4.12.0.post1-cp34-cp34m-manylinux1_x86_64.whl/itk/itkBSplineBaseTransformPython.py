# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineBaseTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBSplineBaseTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBSplineBaseTransformPython')
    _itkBSplineBaseTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineBaseTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineBaseTransformPython
            return _itkBSplineBaseTransformPython
        try:
            _mod = imp.load_module('_itkBSplineBaseTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBSplineBaseTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineBaseTransformPython
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
import itkContinuousIndexPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkArrayPython
import itkOptimizerParametersPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkBSplineInterpolationWeightFunctionPython
import itkFunctionBasePython
import itkImagePython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython

def itkBSplineBaseTransformD33_New():
  return itkBSplineBaseTransformD33.New()


def itkBSplineBaseTransformD22_New():
  return itkBSplineBaseTransformD22.New()

class itkBSplineBaseTransformD22(itkTransformBasePython.itkTransformD22):
    """Proxy of C++ itkBSplineBaseTransformD22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Clone(self) -> "itkBSplineBaseTransformD22_Pointer":
        """Clone(itkBSplineBaseTransformD22 self) -> itkBSplineBaseTransformD22_Pointer"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_Clone(self)


    def SetIdentity(self) -> "void":
        """SetIdentity(itkBSplineBaseTransformD22 self)"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_SetIdentity(self)


    def SetCoefficientImages(self, images: 'itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const &') -> "void":
        """SetCoefficientImages(itkBSplineBaseTransformD22 self, itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const & images)"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_SetCoefficientImages(self, images)


    def GetCoefficientImages(self) -> "itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const":
        """GetCoefficientImages(itkBSplineBaseTransformD22 self) -> itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetCoefficientImages(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineBaseTransformD22 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineBaseTransformD22 self, itkArrayD update)
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_UpdateTransformParameters(self, update, factor)


    def TransformPoint(self, *args) -> "void":
        """
        TransformPoint(itkBSplineBaseTransformD22 self, itkPointD2 point) -> itkPointD2
        TransformPoint(itkBSplineBaseTransformD22 self, itkPointD2 inputPoint, itkPointD2 outputPoint, itkArrayD weights, itkArrayUL indices, bool & inside)
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_TransformPoint(self, *args)


    def GetNumberOfWeights(self) -> "unsigned long":
        """GetNumberOfWeights(itkBSplineBaseTransformD22 self) -> unsigned long"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetNumberOfWeights(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkBSplineBaseTransformD22 self, itkVectorD2 arg0) -> itkVectorD2
        TransformVector(itkBSplineBaseTransformD22 self, vnl_vector_fixed< double,2 > const & arg0) -> vnl_vector_fixed< double,2 >
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_TransformVector(self, *args)


    def ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0: 'itkPointD2', arg1: 'itkArrayD', arg2: 'itkArrayUL') -> "void":
        """ComputeJacobianFromBSplineWeightsWithRespectToPosition(itkBSplineBaseTransformD22 self, itkPointD2 arg0, itkArrayD arg1, itkArrayUL arg2)"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0, arg1, arg2)


    def GetNumberOfParametersPerDimension(self) -> "unsigned long":
        """GetNumberOfParametersPerDimension(itkBSplineBaseTransformD22 self) -> unsigned long"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetNumberOfParametersPerDimension(self)


    def GetNumberOfAffectedWeights(self) -> "unsigned int":
        """GetNumberOfAffectedWeights(itkBSplineBaseTransformD22 self) -> unsigned int"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetNumberOfAffectedWeights(self)

    __swig_destroy__ = _itkBSplineBaseTransformPython.delete_itkBSplineBaseTransformD22

    def cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD22 *":
        """cast(itkLightObject obj) -> itkBSplineBaseTransformD22"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineBaseTransformD22 *":
        """GetPointer(itkBSplineBaseTransformD22 self) -> itkBSplineBaseTransformD22"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineBaseTransformD22

        Create a new object of the class itkBSplineBaseTransformD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineBaseTransformD22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineBaseTransformD22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineBaseTransformD22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineBaseTransformD22.Clone = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_Clone, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.SetIdentity = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_SetIdentity, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.SetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_SetCoefficientImages, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.GetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetCoefficientImages, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.UpdateTransformParameters = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_UpdateTransformParameters, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.TransformPoint = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_TransformPoint, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.GetNumberOfWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetNumberOfWeights, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.TransformVector = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_TransformVector, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.ComputeJacobianFromBSplineWeightsWithRespectToPosition = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_ComputeJacobianFromBSplineWeightsWithRespectToPosition, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.GetNumberOfParametersPerDimension = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetNumberOfParametersPerDimension, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.GetNumberOfAffectedWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetNumberOfAffectedWeights, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22.GetPointer = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_GetPointer, None, itkBSplineBaseTransformD22)
itkBSplineBaseTransformD22_swigregister = _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_swigregister
itkBSplineBaseTransformD22_swigregister(itkBSplineBaseTransformD22)

def itkBSplineBaseTransformD22_cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD22 *":
    """itkBSplineBaseTransformD22_cast(itkLightObject obj) -> itkBSplineBaseTransformD22"""
    return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD22_cast(obj)

class itkBSplineBaseTransformD33(itkTransformBasePython.itkTransformD33):
    """Proxy of C++ itkBSplineBaseTransformD33 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Clone(self) -> "itkBSplineBaseTransformD33_Pointer":
        """Clone(itkBSplineBaseTransformD33 self) -> itkBSplineBaseTransformD33_Pointer"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_Clone(self)


    def SetIdentity(self) -> "void":
        """SetIdentity(itkBSplineBaseTransformD33 self)"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetIdentity(self)


    def SetCoefficientImages(self, images: 'itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const &') -> "void":
        """SetCoefficientImages(itkBSplineBaseTransformD33 self, itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const & images)"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetCoefficientImages(self, images)


    def GetCoefficientImages(self) -> "itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const":
        """GetCoefficientImages(itkBSplineBaseTransformD33 self) -> itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetCoefficientImages(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineBaseTransformD33 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineBaseTransformD33 self, itkArrayD update)
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_UpdateTransformParameters(self, update, factor)


    def TransformPoint(self, *args) -> "void":
        """
        TransformPoint(itkBSplineBaseTransformD33 self, itkPointD3 point) -> itkPointD3
        TransformPoint(itkBSplineBaseTransformD33 self, itkPointD3 inputPoint, itkPointD3 outputPoint, itkArrayD weights, itkArrayUL indices, bool & inside)
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformPoint(self, *args)


    def GetNumberOfWeights(self) -> "unsigned long":
        """GetNumberOfWeights(itkBSplineBaseTransformD33 self) -> unsigned long"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfWeights(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkBSplineBaseTransformD33 self, itkVectorD3 arg0) -> itkVectorD3
        TransformVector(itkBSplineBaseTransformD33 self, vnl_vector_fixed< double,3 > const & arg0) -> vnl_vector_fixed< double,3 >
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformVector(self, *args)


    def ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0: 'itkPointD3', arg1: 'itkArrayD', arg2: 'itkArrayUL') -> "void":
        """ComputeJacobianFromBSplineWeightsWithRespectToPosition(itkBSplineBaseTransformD33 self, itkPointD3 arg0, itkArrayD arg1, itkArrayUL arg2)"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0, arg1, arg2)


    def GetNumberOfParametersPerDimension(self) -> "unsigned long":
        """GetNumberOfParametersPerDimension(itkBSplineBaseTransformD33 self) -> unsigned long"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfParametersPerDimension(self)


    def GetNumberOfAffectedWeights(self) -> "unsigned int":
        """GetNumberOfAffectedWeights(itkBSplineBaseTransformD33 self) -> unsigned int"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfAffectedWeights(self)

    __swig_destroy__ = _itkBSplineBaseTransformPython.delete_itkBSplineBaseTransformD33

    def cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD33 *":
        """cast(itkLightObject obj) -> itkBSplineBaseTransformD33"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineBaseTransformD33 *":
        """GetPointer(itkBSplineBaseTransformD33 self) -> itkBSplineBaseTransformD33"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineBaseTransformD33

        Create a new object of the class itkBSplineBaseTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineBaseTransformD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineBaseTransformD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineBaseTransformD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineBaseTransformD33.Clone = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_Clone, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.SetIdentity = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetIdentity, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.SetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetCoefficientImages, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetCoefficientImages, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.UpdateTransformParameters = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_UpdateTransformParameters, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.TransformPoint = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformPoint, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetNumberOfWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfWeights, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.TransformVector = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformVector, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.ComputeJacobianFromBSplineWeightsWithRespectToPosition = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_ComputeJacobianFromBSplineWeightsWithRespectToPosition, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetNumberOfParametersPerDimension = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfParametersPerDimension, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetNumberOfAffectedWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfAffectedWeights, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetPointer = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetPointer, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33_swigregister = _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_swigregister
itkBSplineBaseTransformD33_swigregister(itkBSplineBaseTransformD33)

def itkBSplineBaseTransformD33_cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD33 *":
    """itkBSplineBaseTransformD33_cast(itkLightObject obj) -> itkBSplineBaseTransformD33"""
    return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_cast(obj)



