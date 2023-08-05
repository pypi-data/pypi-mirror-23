# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBSplineTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBSplineTransformPython')
    _itkBSplineTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineTransformPython
            return _itkBSplineTransformPython
        try:
            _mod = imp.load_module('_itkBSplineTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBSplineTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineTransformPython
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
import ITKCommonBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkMatrixPython
import itkPointPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkContinuousIndexPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkBSplineBaseTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkBSplineInterpolationWeightFunctionPython
import itkFunctionBasePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImagePython
import itkImageRegionPython

def itkBSplineTransformD33_New():
  return itkBSplineTransformD33.New()


def itkBSplineTransformD22_New():
  return itkBSplineTransformD22.New()

class itkBSplineTransformD22(itkBSplineBaseTransformPython.itkBSplineBaseTransformD22):
    """Proxy of C++ itkBSplineTransformD22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineTransformD22_Pointer":
        """__New_orig__() -> itkBSplineTransformD22_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD22___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineTransformD22_Pointer":
        """Clone(itkBSplineTransformD22 self) -> itkBSplineTransformD22_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_Clone(self)


    def SetTransformDomainOrigin(self, arg0: 'itkPointD2') -> "void":
        """SetTransformDomainOrigin(itkBSplineTransformD22 self, itkPointD2 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainOrigin(self, arg0)


    def GetTransformDomainOrigin(self) -> "itkPointD2":
        """GetTransformDomainOrigin(itkBSplineTransformD22 self) -> itkPointD2"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainOrigin(self)


    def SetTransformDomainPhysicalDimensions(self, arg0: 'itkVectorD2') -> "void":
        """SetTransformDomainPhysicalDimensions(itkBSplineTransformD22 self, itkVectorD2 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainPhysicalDimensions(self, arg0)


    def GetTransformDomainPhysicalDimensions(self) -> "itkVectorD2":
        """GetTransformDomainPhysicalDimensions(itkBSplineTransformD22 self) -> itkVectorD2"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainPhysicalDimensions(self)


    def SetTransformDomainDirection(self, arg0: 'itkMatrixD22') -> "void":
        """SetTransformDomainDirection(itkBSplineTransformD22 self, itkMatrixD22 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainDirection(self, arg0)


    def GetTransformDomainDirection(self) -> "itkMatrixD22":
        """GetTransformDomainDirection(itkBSplineTransformD22 self) -> itkMatrixD22"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainDirection(self)


    def SetTransformDomainMeshSize(self, arg0: 'itkSize2') -> "void":
        """SetTransformDomainMeshSize(itkBSplineTransformD22 self, itkSize2 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainMeshSize(self, arg0)


    def GetTransformDomainMeshSize(self) -> "itkSize2":
        """GetTransformDomainMeshSize(itkBSplineTransformD22 self) -> itkSize2"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainMeshSize(self)

    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD22

    def cast(obj: 'itkLightObject') -> "itkBSplineTransformD22 *":
        """cast(itkLightObject obj) -> itkBSplineTransformD22"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineTransformD22 *":
        """GetPointer(itkBSplineTransformD22 self) -> itkBSplineTransformD22"""
        return _itkBSplineTransformPython.itkBSplineTransformD22_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineTransformD22

        Create a new object of the class itkBSplineTransformD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformD22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineTransformD22.Clone = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_Clone, None, itkBSplineTransformD22)
itkBSplineTransformD22.SetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainOrigin, None, itkBSplineTransformD22)
itkBSplineTransformD22.GetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainOrigin, None, itkBSplineTransformD22)
itkBSplineTransformD22.SetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainPhysicalDimensions, None, itkBSplineTransformD22)
itkBSplineTransformD22.GetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainPhysicalDimensions, None, itkBSplineTransformD22)
itkBSplineTransformD22.SetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainDirection, None, itkBSplineTransformD22)
itkBSplineTransformD22.GetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainDirection, None, itkBSplineTransformD22)
itkBSplineTransformD22.SetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_SetTransformDomainMeshSize, None, itkBSplineTransformD22)
itkBSplineTransformD22.GetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_GetTransformDomainMeshSize, None, itkBSplineTransformD22)
itkBSplineTransformD22.GetPointer = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD22_GetPointer, None, itkBSplineTransformD22)
itkBSplineTransformD22_swigregister = _itkBSplineTransformPython.itkBSplineTransformD22_swigregister
itkBSplineTransformD22_swigregister(itkBSplineTransformD22)

def itkBSplineTransformD22___New_orig__() -> "itkBSplineTransformD22_Pointer":
    """itkBSplineTransformD22___New_orig__() -> itkBSplineTransformD22_Pointer"""
    return _itkBSplineTransformPython.itkBSplineTransformD22___New_orig__()

def itkBSplineTransformD22_cast(obj: 'itkLightObject') -> "itkBSplineTransformD22 *":
    """itkBSplineTransformD22_cast(itkLightObject obj) -> itkBSplineTransformD22"""
    return _itkBSplineTransformPython.itkBSplineTransformD22_cast(obj)

class itkBSplineTransformD33(itkBSplineBaseTransformPython.itkBSplineBaseTransformD33):
    """Proxy of C++ itkBSplineTransformD33 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineTransformD33_Pointer":
        """__New_orig__() -> itkBSplineTransformD33_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD33___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineTransformD33_Pointer":
        """Clone(itkBSplineTransformD33 self) -> itkBSplineTransformD33_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_Clone(self)


    def SetTransformDomainOrigin(self, arg0: 'itkPointD3') -> "void":
        """SetTransformDomainOrigin(itkBSplineTransformD33 self, itkPointD3 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainOrigin(self, arg0)


    def GetTransformDomainOrigin(self) -> "itkPointD3":
        """GetTransformDomainOrigin(itkBSplineTransformD33 self) -> itkPointD3"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainOrigin(self)


    def SetTransformDomainPhysicalDimensions(self, arg0: 'itkVectorD3') -> "void":
        """SetTransformDomainPhysicalDimensions(itkBSplineTransformD33 self, itkVectorD3 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainPhysicalDimensions(self, arg0)


    def GetTransformDomainPhysicalDimensions(self) -> "itkVectorD3":
        """GetTransformDomainPhysicalDimensions(itkBSplineTransformD33 self) -> itkVectorD3"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainPhysicalDimensions(self)


    def SetTransformDomainDirection(self, arg0: 'itkMatrixD33') -> "void":
        """SetTransformDomainDirection(itkBSplineTransformD33 self, itkMatrixD33 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainDirection(self, arg0)


    def GetTransformDomainDirection(self) -> "itkMatrixD33":
        """GetTransformDomainDirection(itkBSplineTransformD33 self) -> itkMatrixD33"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainDirection(self)


    def SetTransformDomainMeshSize(self, arg0: 'itkSize3') -> "void":
        """SetTransformDomainMeshSize(itkBSplineTransformD33 self, itkSize3 arg0)"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainMeshSize(self, arg0)


    def GetTransformDomainMeshSize(self) -> "itkSize3":
        """GetTransformDomainMeshSize(itkBSplineTransformD33 self) -> itkSize3"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainMeshSize(self)

    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD33

    def cast(obj: 'itkLightObject') -> "itkBSplineTransformD33 *":
        """cast(itkLightObject obj) -> itkBSplineTransformD33"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkBSplineTransformD33 *":
        """GetPointer(itkBSplineTransformD33 self) -> itkBSplineTransformD33"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineTransformD33

        Create a new object of the class itkBSplineTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineTransformD33.Clone = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_Clone, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainOrigin, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainOrigin, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainPhysicalDimensions, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainPhysicalDimensions, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainDirection, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainDirection, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainMeshSize, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainMeshSize, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetPointer = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetPointer, None, itkBSplineTransformD33)
itkBSplineTransformD33_swigregister = _itkBSplineTransformPython.itkBSplineTransformD33_swigregister
itkBSplineTransformD33_swigregister(itkBSplineTransformD33)

def itkBSplineTransformD33___New_orig__() -> "itkBSplineTransformD33_Pointer":
    """itkBSplineTransformD33___New_orig__() -> itkBSplineTransformD33_Pointer"""
    return _itkBSplineTransformPython.itkBSplineTransformD33___New_orig__()

def itkBSplineTransformD33_cast(obj: 'itkLightObject') -> "itkBSplineTransformD33 *":
    """itkBSplineTransformD33_cast(itkLightObject obj) -> itkBSplineTransformD33"""
    return _itkBSplineTransformPython.itkBSplineTransformD33_cast(obj)



