# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineResampleImageFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBSplineResampleImageFunctionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBSplineResampleImageFunctionPython')
    _itkBSplineResampleImageFunctionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineResampleImageFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineResampleImageFunctionPython
            return _itkBSplineResampleImageFunctionPython
        try:
            _mod = imp.load_module('_itkBSplineResampleImageFunctionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBSplineResampleImageFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineResampleImageFunctionPython
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


import itkImagePython
import stdcomplexPython
import pyBasePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkBSplineInterpolateImageFunctionPython
import itkInterpolateImageFunctionPython
import itkImageFunctionBasePython
import itkFunctionBasePython
import itkArrayPython
import itkContinuousIndexPython

def itkBSplineResampleImageFunctionIF3D_New():
  return itkBSplineResampleImageFunctionIF3D.New()


def itkBSplineResampleImageFunctionIUC3D_New():
  return itkBSplineResampleImageFunctionIUC3D.New()


def itkBSplineResampleImageFunctionISS3D_New():
  return itkBSplineResampleImageFunctionISS3D.New()


def itkBSplineResampleImageFunctionIF2D_New():
  return itkBSplineResampleImageFunctionIF2D.New()


def itkBSplineResampleImageFunctionIUC2D_New():
  return itkBSplineResampleImageFunctionIUC2D.New()


def itkBSplineResampleImageFunctionISS2D_New():
  return itkBSplineResampleImageFunctionISS2D.New()

class itkBSplineResampleImageFunctionIF2D(itkBSplineInterpolateImageFunctionPython.itkBSplineInterpolateImageFunctionIF2DF):
    """Proxy of C++ itkBSplineResampleImageFunctionIF2D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBSplineResampleImageFunctionIF2D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBSplineResampleImageFunctionIF2D self) -> itkBSplineResampleImageFunctionIF2D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_Clone(self)

    __swig_destroy__ = _itkBSplineResampleImageFunctionPython.delete_itkBSplineResampleImageFunctionIF2D

    def cast(obj):
        """cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIF2D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBSplineResampleImageFunctionIF2D self) -> itkBSplineResampleImageFunctionIF2D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineResampleImageFunctionIF2D

        Create a new object of the class itkBSplineResampleImageFunctionIF2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineResampleImageFunctionIF2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineResampleImageFunctionIF2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineResampleImageFunctionIF2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineResampleImageFunctionIF2D.Clone = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_Clone, None, itkBSplineResampleImageFunctionIF2D)
itkBSplineResampleImageFunctionIF2D.GetPointer = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_GetPointer, None, itkBSplineResampleImageFunctionIF2D)
itkBSplineResampleImageFunctionIF2D_swigregister = _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_swigregister
itkBSplineResampleImageFunctionIF2D_swigregister(itkBSplineResampleImageFunctionIF2D)

def itkBSplineResampleImageFunctionIF2D___New_orig__():
    """itkBSplineResampleImageFunctionIF2D___New_orig__() -> itkBSplineResampleImageFunctionIF2D_Pointer"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D___New_orig__()

def itkBSplineResampleImageFunctionIF2D_cast(obj):
    """itkBSplineResampleImageFunctionIF2D_cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIF2D"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF2D_cast(obj)

class itkBSplineResampleImageFunctionIF3D(itkBSplineInterpolateImageFunctionPython.itkBSplineInterpolateImageFunctionIF3DF):
    """Proxy of C++ itkBSplineResampleImageFunctionIF3D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBSplineResampleImageFunctionIF3D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBSplineResampleImageFunctionIF3D self) -> itkBSplineResampleImageFunctionIF3D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_Clone(self)

    __swig_destroy__ = _itkBSplineResampleImageFunctionPython.delete_itkBSplineResampleImageFunctionIF3D

    def cast(obj):
        """cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIF3D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBSplineResampleImageFunctionIF3D self) -> itkBSplineResampleImageFunctionIF3D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineResampleImageFunctionIF3D

        Create a new object of the class itkBSplineResampleImageFunctionIF3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineResampleImageFunctionIF3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineResampleImageFunctionIF3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineResampleImageFunctionIF3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineResampleImageFunctionIF3D.Clone = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_Clone, None, itkBSplineResampleImageFunctionIF3D)
itkBSplineResampleImageFunctionIF3D.GetPointer = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_GetPointer, None, itkBSplineResampleImageFunctionIF3D)
itkBSplineResampleImageFunctionIF3D_swigregister = _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_swigregister
itkBSplineResampleImageFunctionIF3D_swigregister(itkBSplineResampleImageFunctionIF3D)

def itkBSplineResampleImageFunctionIF3D___New_orig__():
    """itkBSplineResampleImageFunctionIF3D___New_orig__() -> itkBSplineResampleImageFunctionIF3D_Pointer"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D___New_orig__()

def itkBSplineResampleImageFunctionIF3D_cast(obj):
    """itkBSplineResampleImageFunctionIF3D_cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIF3D"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIF3D_cast(obj)

class itkBSplineResampleImageFunctionISS2D(itkBSplineInterpolateImageFunctionPython.itkBSplineInterpolateImageFunctionISS2DSS):
    """Proxy of C++ itkBSplineResampleImageFunctionISS2D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBSplineResampleImageFunctionISS2D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBSplineResampleImageFunctionISS2D self) -> itkBSplineResampleImageFunctionISS2D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_Clone(self)

    __swig_destroy__ = _itkBSplineResampleImageFunctionPython.delete_itkBSplineResampleImageFunctionISS2D

    def cast(obj):
        """cast(itkLightObject obj) -> itkBSplineResampleImageFunctionISS2D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBSplineResampleImageFunctionISS2D self) -> itkBSplineResampleImageFunctionISS2D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineResampleImageFunctionISS2D

        Create a new object of the class itkBSplineResampleImageFunctionISS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineResampleImageFunctionISS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineResampleImageFunctionISS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineResampleImageFunctionISS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineResampleImageFunctionISS2D.Clone = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_Clone, None, itkBSplineResampleImageFunctionISS2D)
itkBSplineResampleImageFunctionISS2D.GetPointer = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_GetPointer, None, itkBSplineResampleImageFunctionISS2D)
itkBSplineResampleImageFunctionISS2D_swigregister = _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_swigregister
itkBSplineResampleImageFunctionISS2D_swigregister(itkBSplineResampleImageFunctionISS2D)

def itkBSplineResampleImageFunctionISS2D___New_orig__():
    """itkBSplineResampleImageFunctionISS2D___New_orig__() -> itkBSplineResampleImageFunctionISS2D_Pointer"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D___New_orig__()

def itkBSplineResampleImageFunctionISS2D_cast(obj):
    """itkBSplineResampleImageFunctionISS2D_cast(itkLightObject obj) -> itkBSplineResampleImageFunctionISS2D"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS2D_cast(obj)

class itkBSplineResampleImageFunctionISS3D(itkBSplineInterpolateImageFunctionPython.itkBSplineInterpolateImageFunctionISS3DSS):
    """Proxy of C++ itkBSplineResampleImageFunctionISS3D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBSplineResampleImageFunctionISS3D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBSplineResampleImageFunctionISS3D self) -> itkBSplineResampleImageFunctionISS3D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_Clone(self)

    __swig_destroy__ = _itkBSplineResampleImageFunctionPython.delete_itkBSplineResampleImageFunctionISS3D

    def cast(obj):
        """cast(itkLightObject obj) -> itkBSplineResampleImageFunctionISS3D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBSplineResampleImageFunctionISS3D self) -> itkBSplineResampleImageFunctionISS3D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineResampleImageFunctionISS3D

        Create a new object of the class itkBSplineResampleImageFunctionISS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineResampleImageFunctionISS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineResampleImageFunctionISS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineResampleImageFunctionISS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineResampleImageFunctionISS3D.Clone = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_Clone, None, itkBSplineResampleImageFunctionISS3D)
itkBSplineResampleImageFunctionISS3D.GetPointer = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_GetPointer, None, itkBSplineResampleImageFunctionISS3D)
itkBSplineResampleImageFunctionISS3D_swigregister = _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_swigregister
itkBSplineResampleImageFunctionISS3D_swigregister(itkBSplineResampleImageFunctionISS3D)

def itkBSplineResampleImageFunctionISS3D___New_orig__():
    """itkBSplineResampleImageFunctionISS3D___New_orig__() -> itkBSplineResampleImageFunctionISS3D_Pointer"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D___New_orig__()

def itkBSplineResampleImageFunctionISS3D_cast(obj):
    """itkBSplineResampleImageFunctionISS3D_cast(itkLightObject obj) -> itkBSplineResampleImageFunctionISS3D"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionISS3D_cast(obj)

class itkBSplineResampleImageFunctionIUC2D(itkBSplineInterpolateImageFunctionPython.itkBSplineInterpolateImageFunctionIUC2DUC):
    """Proxy of C++ itkBSplineResampleImageFunctionIUC2D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBSplineResampleImageFunctionIUC2D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBSplineResampleImageFunctionIUC2D self) -> itkBSplineResampleImageFunctionIUC2D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_Clone(self)

    __swig_destroy__ = _itkBSplineResampleImageFunctionPython.delete_itkBSplineResampleImageFunctionIUC2D

    def cast(obj):
        """cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIUC2D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBSplineResampleImageFunctionIUC2D self) -> itkBSplineResampleImageFunctionIUC2D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineResampleImageFunctionIUC2D

        Create a new object of the class itkBSplineResampleImageFunctionIUC2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineResampleImageFunctionIUC2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineResampleImageFunctionIUC2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineResampleImageFunctionIUC2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineResampleImageFunctionIUC2D.Clone = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_Clone, None, itkBSplineResampleImageFunctionIUC2D)
itkBSplineResampleImageFunctionIUC2D.GetPointer = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_GetPointer, None, itkBSplineResampleImageFunctionIUC2D)
itkBSplineResampleImageFunctionIUC2D_swigregister = _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_swigregister
itkBSplineResampleImageFunctionIUC2D_swigregister(itkBSplineResampleImageFunctionIUC2D)

def itkBSplineResampleImageFunctionIUC2D___New_orig__():
    """itkBSplineResampleImageFunctionIUC2D___New_orig__() -> itkBSplineResampleImageFunctionIUC2D_Pointer"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D___New_orig__()

def itkBSplineResampleImageFunctionIUC2D_cast(obj):
    """itkBSplineResampleImageFunctionIUC2D_cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIUC2D"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC2D_cast(obj)

class itkBSplineResampleImageFunctionIUC3D(itkBSplineInterpolateImageFunctionPython.itkBSplineInterpolateImageFunctionIUC3DUC):
    """Proxy of C++ itkBSplineResampleImageFunctionIUC3D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBSplineResampleImageFunctionIUC3D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBSplineResampleImageFunctionIUC3D self) -> itkBSplineResampleImageFunctionIUC3D_Pointer"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_Clone(self)

    __swig_destroy__ = _itkBSplineResampleImageFunctionPython.delete_itkBSplineResampleImageFunctionIUC3D

    def cast(obj):
        """cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIUC3D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBSplineResampleImageFunctionIUC3D self) -> itkBSplineResampleImageFunctionIUC3D"""
        return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBSplineResampleImageFunctionIUC3D

        Create a new object of the class itkBSplineResampleImageFunctionIUC3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineResampleImageFunctionIUC3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineResampleImageFunctionIUC3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineResampleImageFunctionIUC3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineResampleImageFunctionIUC3D.Clone = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_Clone, None, itkBSplineResampleImageFunctionIUC3D)
itkBSplineResampleImageFunctionIUC3D.GetPointer = new_instancemethod(_itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_GetPointer, None, itkBSplineResampleImageFunctionIUC3D)
itkBSplineResampleImageFunctionIUC3D_swigregister = _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_swigregister
itkBSplineResampleImageFunctionIUC3D_swigregister(itkBSplineResampleImageFunctionIUC3D)

def itkBSplineResampleImageFunctionIUC3D___New_orig__():
    """itkBSplineResampleImageFunctionIUC3D___New_orig__() -> itkBSplineResampleImageFunctionIUC3D_Pointer"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D___New_orig__()

def itkBSplineResampleImageFunctionIUC3D_cast(obj):
    """itkBSplineResampleImageFunctionIUC3D_cast(itkLightObject obj) -> itkBSplineResampleImageFunctionIUC3D"""
    return _itkBSplineResampleImageFunctionPython.itkBSplineResampleImageFunctionIUC3D_cast(obj)



