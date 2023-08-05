# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNearestNeighborInterpolateImageFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNearestNeighborInterpolateImageFunctionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNearestNeighborInterpolateImageFunctionPython')
    _itkNearestNeighborInterpolateImageFunctionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNearestNeighborInterpolateImageFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkNearestNeighborInterpolateImageFunctionPython
            return _itkNearestNeighborInterpolateImageFunctionPython
        try:
            _mod = imp.load_module('_itkNearestNeighborInterpolateImageFunctionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNearestNeighborInterpolateImageFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNearestNeighborInterpolateImageFunctionPython
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


import itkContinuousIndexPython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkInterpolateImageFunctionPython
import itkImageFunctionBasePython
import itkImagePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import ITKCommonBasePython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkFunctionBasePython
import itkArrayPython

def itkNearestNeighborInterpolateImageFunctionIF3D_New():
  return itkNearestNeighborInterpolateImageFunctionIF3D.New()


def itkNearestNeighborInterpolateImageFunctionIUC3D_New():
  return itkNearestNeighborInterpolateImageFunctionIUC3D.New()


def itkNearestNeighborInterpolateImageFunctionISS3D_New():
  return itkNearestNeighborInterpolateImageFunctionISS3D.New()


def itkNearestNeighborInterpolateImageFunctionIF2D_New():
  return itkNearestNeighborInterpolateImageFunctionIF2D.New()


def itkNearestNeighborInterpolateImageFunctionIUC2D_New():
  return itkNearestNeighborInterpolateImageFunctionIUC2D.New()


def itkNearestNeighborInterpolateImageFunctionISS2D_New():
  return itkNearestNeighborInterpolateImageFunctionISS2D.New()

class itkNearestNeighborInterpolateImageFunctionIF2D(itkInterpolateImageFunctionPython.itkInterpolateImageFunctionIF2D):
    """Proxy of C++ itkNearestNeighborInterpolateImageFunctionIF2D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIF2D_Pointer":
        """__New_orig__() -> itkNearestNeighborInterpolateImageFunctionIF2D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNearestNeighborInterpolateImageFunctionIF2D_Pointer":
        """Clone(itkNearestNeighborInterpolateImageFunctionIF2D self) -> itkNearestNeighborInterpolateImageFunctionIF2D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_Clone(self)

    __swig_destroy__ = _itkNearestNeighborInterpolateImageFunctionPython.delete_itkNearestNeighborInterpolateImageFunctionIF2D

    def cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIF2D *":
        """cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIF2D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNearestNeighborInterpolateImageFunctionIF2D *":
        """GetPointer(itkNearestNeighborInterpolateImageFunctionIF2D self) -> itkNearestNeighborInterpolateImageFunctionIF2D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNearestNeighborInterpolateImageFunctionIF2D

        Create a new object of the class itkNearestNeighborInterpolateImageFunctionIF2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNearestNeighborInterpolateImageFunctionIF2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNearestNeighborInterpolateImageFunctionIF2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNearestNeighborInterpolateImageFunctionIF2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNearestNeighborInterpolateImageFunctionIF2D.Clone = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_Clone, None, itkNearestNeighborInterpolateImageFunctionIF2D)
itkNearestNeighborInterpolateImageFunctionIF2D.GetPointer = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_GetPointer, None, itkNearestNeighborInterpolateImageFunctionIF2D)
itkNearestNeighborInterpolateImageFunctionIF2D_swigregister = _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_swigregister
itkNearestNeighborInterpolateImageFunctionIF2D_swigregister(itkNearestNeighborInterpolateImageFunctionIF2D)

def itkNearestNeighborInterpolateImageFunctionIF2D___New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIF2D_Pointer":
    """itkNearestNeighborInterpolateImageFunctionIF2D___New_orig__() -> itkNearestNeighborInterpolateImageFunctionIF2D_Pointer"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D___New_orig__()

def itkNearestNeighborInterpolateImageFunctionIF2D_cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIF2D *":
    """itkNearestNeighborInterpolateImageFunctionIF2D_cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIF2D"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF2D_cast(obj)

class itkNearestNeighborInterpolateImageFunctionIF3D(itkInterpolateImageFunctionPython.itkInterpolateImageFunctionIF3D):
    """Proxy of C++ itkNearestNeighborInterpolateImageFunctionIF3D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIF3D_Pointer":
        """__New_orig__() -> itkNearestNeighborInterpolateImageFunctionIF3D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNearestNeighborInterpolateImageFunctionIF3D_Pointer":
        """Clone(itkNearestNeighborInterpolateImageFunctionIF3D self) -> itkNearestNeighborInterpolateImageFunctionIF3D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_Clone(self)

    __swig_destroy__ = _itkNearestNeighborInterpolateImageFunctionPython.delete_itkNearestNeighborInterpolateImageFunctionIF3D

    def cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIF3D *":
        """cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIF3D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNearestNeighborInterpolateImageFunctionIF3D *":
        """GetPointer(itkNearestNeighborInterpolateImageFunctionIF3D self) -> itkNearestNeighborInterpolateImageFunctionIF3D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNearestNeighborInterpolateImageFunctionIF3D

        Create a new object of the class itkNearestNeighborInterpolateImageFunctionIF3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNearestNeighborInterpolateImageFunctionIF3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNearestNeighborInterpolateImageFunctionIF3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNearestNeighborInterpolateImageFunctionIF3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNearestNeighborInterpolateImageFunctionIF3D.Clone = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_Clone, None, itkNearestNeighborInterpolateImageFunctionIF3D)
itkNearestNeighborInterpolateImageFunctionIF3D.GetPointer = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_GetPointer, None, itkNearestNeighborInterpolateImageFunctionIF3D)
itkNearestNeighborInterpolateImageFunctionIF3D_swigregister = _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_swigregister
itkNearestNeighborInterpolateImageFunctionIF3D_swigregister(itkNearestNeighborInterpolateImageFunctionIF3D)

def itkNearestNeighborInterpolateImageFunctionIF3D___New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIF3D_Pointer":
    """itkNearestNeighborInterpolateImageFunctionIF3D___New_orig__() -> itkNearestNeighborInterpolateImageFunctionIF3D_Pointer"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D___New_orig__()

def itkNearestNeighborInterpolateImageFunctionIF3D_cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIF3D *":
    """itkNearestNeighborInterpolateImageFunctionIF3D_cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIF3D"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIF3D_cast(obj)

class itkNearestNeighborInterpolateImageFunctionISS2D(itkInterpolateImageFunctionPython.itkInterpolateImageFunctionISS2D):
    """Proxy of C++ itkNearestNeighborInterpolateImageFunctionISS2D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNearestNeighborInterpolateImageFunctionISS2D_Pointer":
        """__New_orig__() -> itkNearestNeighborInterpolateImageFunctionISS2D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNearestNeighborInterpolateImageFunctionISS2D_Pointer":
        """Clone(itkNearestNeighborInterpolateImageFunctionISS2D self) -> itkNearestNeighborInterpolateImageFunctionISS2D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_Clone(self)

    __swig_destroy__ = _itkNearestNeighborInterpolateImageFunctionPython.delete_itkNearestNeighborInterpolateImageFunctionISS2D

    def cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionISS2D *":
        """cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionISS2D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNearestNeighborInterpolateImageFunctionISS2D *":
        """GetPointer(itkNearestNeighborInterpolateImageFunctionISS2D self) -> itkNearestNeighborInterpolateImageFunctionISS2D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNearestNeighborInterpolateImageFunctionISS2D

        Create a new object of the class itkNearestNeighborInterpolateImageFunctionISS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNearestNeighborInterpolateImageFunctionISS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNearestNeighborInterpolateImageFunctionISS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNearestNeighborInterpolateImageFunctionISS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNearestNeighborInterpolateImageFunctionISS2D.Clone = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_Clone, None, itkNearestNeighborInterpolateImageFunctionISS2D)
itkNearestNeighborInterpolateImageFunctionISS2D.GetPointer = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_GetPointer, None, itkNearestNeighborInterpolateImageFunctionISS2D)
itkNearestNeighborInterpolateImageFunctionISS2D_swigregister = _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_swigregister
itkNearestNeighborInterpolateImageFunctionISS2D_swigregister(itkNearestNeighborInterpolateImageFunctionISS2D)

def itkNearestNeighborInterpolateImageFunctionISS2D___New_orig__() -> "itkNearestNeighborInterpolateImageFunctionISS2D_Pointer":
    """itkNearestNeighborInterpolateImageFunctionISS2D___New_orig__() -> itkNearestNeighborInterpolateImageFunctionISS2D_Pointer"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D___New_orig__()

def itkNearestNeighborInterpolateImageFunctionISS2D_cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionISS2D *":
    """itkNearestNeighborInterpolateImageFunctionISS2D_cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionISS2D"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS2D_cast(obj)

class itkNearestNeighborInterpolateImageFunctionISS3D(itkInterpolateImageFunctionPython.itkInterpolateImageFunctionISS3D):
    """Proxy of C++ itkNearestNeighborInterpolateImageFunctionISS3D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNearestNeighborInterpolateImageFunctionISS3D_Pointer":
        """__New_orig__() -> itkNearestNeighborInterpolateImageFunctionISS3D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNearestNeighborInterpolateImageFunctionISS3D_Pointer":
        """Clone(itkNearestNeighborInterpolateImageFunctionISS3D self) -> itkNearestNeighborInterpolateImageFunctionISS3D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_Clone(self)

    __swig_destroy__ = _itkNearestNeighborInterpolateImageFunctionPython.delete_itkNearestNeighborInterpolateImageFunctionISS3D

    def cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionISS3D *":
        """cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionISS3D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNearestNeighborInterpolateImageFunctionISS3D *":
        """GetPointer(itkNearestNeighborInterpolateImageFunctionISS3D self) -> itkNearestNeighborInterpolateImageFunctionISS3D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNearestNeighborInterpolateImageFunctionISS3D

        Create a new object of the class itkNearestNeighborInterpolateImageFunctionISS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNearestNeighborInterpolateImageFunctionISS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNearestNeighborInterpolateImageFunctionISS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNearestNeighborInterpolateImageFunctionISS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNearestNeighborInterpolateImageFunctionISS3D.Clone = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_Clone, None, itkNearestNeighborInterpolateImageFunctionISS3D)
itkNearestNeighborInterpolateImageFunctionISS3D.GetPointer = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_GetPointer, None, itkNearestNeighborInterpolateImageFunctionISS3D)
itkNearestNeighborInterpolateImageFunctionISS3D_swigregister = _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_swigregister
itkNearestNeighborInterpolateImageFunctionISS3D_swigregister(itkNearestNeighborInterpolateImageFunctionISS3D)

def itkNearestNeighborInterpolateImageFunctionISS3D___New_orig__() -> "itkNearestNeighborInterpolateImageFunctionISS3D_Pointer":
    """itkNearestNeighborInterpolateImageFunctionISS3D___New_orig__() -> itkNearestNeighborInterpolateImageFunctionISS3D_Pointer"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D___New_orig__()

def itkNearestNeighborInterpolateImageFunctionISS3D_cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionISS3D *":
    """itkNearestNeighborInterpolateImageFunctionISS3D_cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionISS3D"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionISS3D_cast(obj)

class itkNearestNeighborInterpolateImageFunctionIUC2D(itkInterpolateImageFunctionPython.itkInterpolateImageFunctionIUC2D):
    """Proxy of C++ itkNearestNeighborInterpolateImageFunctionIUC2D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIUC2D_Pointer":
        """__New_orig__() -> itkNearestNeighborInterpolateImageFunctionIUC2D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNearestNeighborInterpolateImageFunctionIUC2D_Pointer":
        """Clone(itkNearestNeighborInterpolateImageFunctionIUC2D self) -> itkNearestNeighborInterpolateImageFunctionIUC2D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_Clone(self)

    __swig_destroy__ = _itkNearestNeighborInterpolateImageFunctionPython.delete_itkNearestNeighborInterpolateImageFunctionIUC2D

    def cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIUC2D *":
        """cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIUC2D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNearestNeighborInterpolateImageFunctionIUC2D *":
        """GetPointer(itkNearestNeighborInterpolateImageFunctionIUC2D self) -> itkNearestNeighborInterpolateImageFunctionIUC2D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNearestNeighborInterpolateImageFunctionIUC2D

        Create a new object of the class itkNearestNeighborInterpolateImageFunctionIUC2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNearestNeighborInterpolateImageFunctionIUC2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNearestNeighborInterpolateImageFunctionIUC2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNearestNeighborInterpolateImageFunctionIUC2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNearestNeighborInterpolateImageFunctionIUC2D.Clone = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_Clone, None, itkNearestNeighborInterpolateImageFunctionIUC2D)
itkNearestNeighborInterpolateImageFunctionIUC2D.GetPointer = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_GetPointer, None, itkNearestNeighborInterpolateImageFunctionIUC2D)
itkNearestNeighborInterpolateImageFunctionIUC2D_swigregister = _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_swigregister
itkNearestNeighborInterpolateImageFunctionIUC2D_swigregister(itkNearestNeighborInterpolateImageFunctionIUC2D)

def itkNearestNeighborInterpolateImageFunctionIUC2D___New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIUC2D_Pointer":
    """itkNearestNeighborInterpolateImageFunctionIUC2D___New_orig__() -> itkNearestNeighborInterpolateImageFunctionIUC2D_Pointer"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D___New_orig__()

def itkNearestNeighborInterpolateImageFunctionIUC2D_cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIUC2D *":
    """itkNearestNeighborInterpolateImageFunctionIUC2D_cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIUC2D"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC2D_cast(obj)

class itkNearestNeighborInterpolateImageFunctionIUC3D(itkInterpolateImageFunctionPython.itkInterpolateImageFunctionIUC3D):
    """Proxy of C++ itkNearestNeighborInterpolateImageFunctionIUC3D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIUC3D_Pointer":
        """__New_orig__() -> itkNearestNeighborInterpolateImageFunctionIUC3D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNearestNeighborInterpolateImageFunctionIUC3D_Pointer":
        """Clone(itkNearestNeighborInterpolateImageFunctionIUC3D self) -> itkNearestNeighborInterpolateImageFunctionIUC3D_Pointer"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_Clone(self)

    __swig_destroy__ = _itkNearestNeighborInterpolateImageFunctionPython.delete_itkNearestNeighborInterpolateImageFunctionIUC3D

    def cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIUC3D *":
        """cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIUC3D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNearestNeighborInterpolateImageFunctionIUC3D *":
        """GetPointer(itkNearestNeighborInterpolateImageFunctionIUC3D self) -> itkNearestNeighborInterpolateImageFunctionIUC3D"""
        return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNearestNeighborInterpolateImageFunctionIUC3D

        Create a new object of the class itkNearestNeighborInterpolateImageFunctionIUC3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNearestNeighborInterpolateImageFunctionIUC3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNearestNeighborInterpolateImageFunctionIUC3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNearestNeighborInterpolateImageFunctionIUC3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNearestNeighborInterpolateImageFunctionIUC3D.Clone = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_Clone, None, itkNearestNeighborInterpolateImageFunctionIUC3D)
itkNearestNeighborInterpolateImageFunctionIUC3D.GetPointer = new_instancemethod(_itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_GetPointer, None, itkNearestNeighborInterpolateImageFunctionIUC3D)
itkNearestNeighborInterpolateImageFunctionIUC3D_swigregister = _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_swigregister
itkNearestNeighborInterpolateImageFunctionIUC3D_swigregister(itkNearestNeighborInterpolateImageFunctionIUC3D)

def itkNearestNeighborInterpolateImageFunctionIUC3D___New_orig__() -> "itkNearestNeighborInterpolateImageFunctionIUC3D_Pointer":
    """itkNearestNeighborInterpolateImageFunctionIUC3D___New_orig__() -> itkNearestNeighborInterpolateImageFunctionIUC3D_Pointer"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D___New_orig__()

def itkNearestNeighborInterpolateImageFunctionIUC3D_cast(obj: 'itkLightObject') -> "itkNearestNeighborInterpolateImageFunctionIUC3D *":
    """itkNearestNeighborInterpolateImageFunctionIUC3D_cast(itkLightObject obj) -> itkNearestNeighborInterpolateImageFunctionIUC3D"""
    return _itkNearestNeighborInterpolateImageFunctionPython.itkNearestNeighborInterpolateImageFunctionIUC3D_cast(obj)



