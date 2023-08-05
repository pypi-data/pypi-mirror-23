# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRecursiveSeparableImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRecursiveSeparableImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRecursiveSeparableImageFilterPython')
    _itkRecursiveSeparableImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRecursiveSeparableImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRecursiveSeparableImageFilterPython
            return _itkRecursiveSeparableImageFilterPython
        try:
            _mod = imp.load_module('_itkRecursiveSeparableImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRecursiveSeparableImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRecursiveSeparableImageFilterPython
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


import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkRecursiveSeparableImageFilterIF3IF3_New():
  return itkRecursiveSeparableImageFilterIF3IF3.New()


def itkRecursiveSeparableImageFilterIF2IF2_New():
  return itkRecursiveSeparableImageFilterIF2IF2.New()


def itkRecursiveSeparableImageFilterIUC3IUC3_New():
  return itkRecursiveSeparableImageFilterIUC3IUC3.New()


def itkRecursiveSeparableImageFilterIUC2IUC2_New():
  return itkRecursiveSeparableImageFilterIUC2IUC2.New()


def itkRecursiveSeparableImageFilterISS3ISS3_New():
  return itkRecursiveSeparableImageFilterISS3ISS3.New()


def itkRecursiveSeparableImageFilterISS2ISS2_New():
  return itkRecursiveSeparableImageFilterISS2ISS2.New()

class itkRecursiveSeparableImageFilterIF2IF2(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF2IF2):
    """Proxy of C++ itkRecursiveSeparableImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkRecursiveSeparableImageFilterIF2IF2 self) -> unsigned int"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetDirection(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkRecursiveSeparableImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_SetDirection(self, _arg)


    def SetInputImage(self, arg0: 'itkImageF2') -> "void":
        """SetInputImage(itkRecursiveSeparableImageFilterIF2IF2 self, itkImageF2 arg0)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_SetInputImage(self, arg0)


    def GetInputImage(self) -> "itkImageF2 const *":
        """GetInputImage(itkRecursiveSeparableImageFilterIF2IF2 self) -> itkImageF2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetInputImage(self)

    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIF2IF2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveSeparableImageFilterIF2IF2 *":
        """GetPointer(itkRecursiveSeparableImageFilterIF2IF2 self) -> itkRecursiveSeparableImageFilterIF2IF2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveSeparableImageFilterIF2IF2

        Create a new object of the class itkRecursiveSeparableImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveSeparableImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveSeparableImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveSeparableImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveSeparableImageFilterIF2IF2.GetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetDirection, None, itkRecursiveSeparableImageFilterIF2IF2)
itkRecursiveSeparableImageFilterIF2IF2.SetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_SetDirection, None, itkRecursiveSeparableImageFilterIF2IF2)
itkRecursiveSeparableImageFilterIF2IF2.SetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_SetInputImage, None, itkRecursiveSeparableImageFilterIF2IF2)
itkRecursiveSeparableImageFilterIF2IF2.GetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetInputImage, None, itkRecursiveSeparableImageFilterIF2IF2)
itkRecursiveSeparableImageFilterIF2IF2.GetPointer = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetPointer, None, itkRecursiveSeparableImageFilterIF2IF2)
itkRecursiveSeparableImageFilterIF2IF2_swigregister = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_swigregister
itkRecursiveSeparableImageFilterIF2IF2_swigregister(itkRecursiveSeparableImageFilterIF2IF2)

def itkRecursiveSeparableImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIF2IF2 *":
    """itkRecursiveSeparableImageFilterIF2IF2_cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIF2IF2"""
    return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_cast(obj)

class itkRecursiveSeparableImageFilterIF3IF3(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF3IF3):
    """Proxy of C++ itkRecursiveSeparableImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkRecursiveSeparableImageFilterIF3IF3 self) -> unsigned int"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetDirection(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkRecursiveSeparableImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_SetDirection(self, _arg)


    def SetInputImage(self, arg0: 'itkImageF3') -> "void":
        """SetInputImage(itkRecursiveSeparableImageFilterIF3IF3 self, itkImageF3 arg0)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_SetInputImage(self, arg0)


    def GetInputImage(self) -> "itkImageF3 const *":
        """GetInputImage(itkRecursiveSeparableImageFilterIF3IF3 self) -> itkImageF3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetInputImage(self)

    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIF3IF3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveSeparableImageFilterIF3IF3 *":
        """GetPointer(itkRecursiveSeparableImageFilterIF3IF3 self) -> itkRecursiveSeparableImageFilterIF3IF3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveSeparableImageFilterIF3IF3

        Create a new object of the class itkRecursiveSeparableImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveSeparableImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveSeparableImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveSeparableImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveSeparableImageFilterIF3IF3.GetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetDirection, None, itkRecursiveSeparableImageFilterIF3IF3)
itkRecursiveSeparableImageFilterIF3IF3.SetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_SetDirection, None, itkRecursiveSeparableImageFilterIF3IF3)
itkRecursiveSeparableImageFilterIF3IF3.SetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_SetInputImage, None, itkRecursiveSeparableImageFilterIF3IF3)
itkRecursiveSeparableImageFilterIF3IF3.GetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetInputImage, None, itkRecursiveSeparableImageFilterIF3IF3)
itkRecursiveSeparableImageFilterIF3IF3.GetPointer = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetPointer, None, itkRecursiveSeparableImageFilterIF3IF3)
itkRecursiveSeparableImageFilterIF3IF3_swigregister = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_swigregister
itkRecursiveSeparableImageFilterIF3IF3_swigregister(itkRecursiveSeparableImageFilterIF3IF3)

def itkRecursiveSeparableImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIF3IF3 *":
    """itkRecursiveSeparableImageFilterIF3IF3_cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIF3IF3"""
    return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_cast(obj)

class itkRecursiveSeparableImageFilterISS2ISS2(itkInPlaceImageFilterAPython.itkInPlaceImageFilterISS2ISS2):
    """Proxy of C++ itkRecursiveSeparableImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkRecursiveSeparableImageFilterISS2ISS2 self) -> unsigned int"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetDirection(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkRecursiveSeparableImageFilterISS2ISS2 self, unsigned int const _arg)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_SetDirection(self, _arg)


    def SetInputImage(self, arg0: 'itkImageSS2') -> "void":
        """SetInputImage(itkRecursiveSeparableImageFilterISS2ISS2 self, itkImageSS2 arg0)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_SetInputImage(self, arg0)


    def GetInputImage(self) -> "itkImageSS2 const *":
        """GetInputImage(itkRecursiveSeparableImageFilterISS2ISS2 self) -> itkImageSS2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetInputImage(self)

    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterISS2ISS2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveSeparableImageFilterISS2ISS2 *":
        """GetPointer(itkRecursiveSeparableImageFilterISS2ISS2 self) -> itkRecursiveSeparableImageFilterISS2ISS2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveSeparableImageFilterISS2ISS2

        Create a new object of the class itkRecursiveSeparableImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveSeparableImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveSeparableImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveSeparableImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveSeparableImageFilterISS2ISS2.GetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetDirection, None, itkRecursiveSeparableImageFilterISS2ISS2)
itkRecursiveSeparableImageFilterISS2ISS2.SetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_SetDirection, None, itkRecursiveSeparableImageFilterISS2ISS2)
itkRecursiveSeparableImageFilterISS2ISS2.SetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_SetInputImage, None, itkRecursiveSeparableImageFilterISS2ISS2)
itkRecursiveSeparableImageFilterISS2ISS2.GetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetInputImage, None, itkRecursiveSeparableImageFilterISS2ISS2)
itkRecursiveSeparableImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetPointer, None, itkRecursiveSeparableImageFilterISS2ISS2)
itkRecursiveSeparableImageFilterISS2ISS2_swigregister = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_swigregister
itkRecursiveSeparableImageFilterISS2ISS2_swigregister(itkRecursiveSeparableImageFilterISS2ISS2)

def itkRecursiveSeparableImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterISS2ISS2 *":
    """itkRecursiveSeparableImageFilterISS2ISS2_cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterISS2ISS2"""
    return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_cast(obj)

class itkRecursiveSeparableImageFilterISS3ISS3(itkInPlaceImageFilterAPython.itkInPlaceImageFilterISS3ISS3):
    """Proxy of C++ itkRecursiveSeparableImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkRecursiveSeparableImageFilterISS3ISS3 self) -> unsigned int"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetDirection(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkRecursiveSeparableImageFilterISS3ISS3 self, unsigned int const _arg)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_SetDirection(self, _arg)


    def SetInputImage(self, arg0: 'itkImageSS3') -> "void":
        """SetInputImage(itkRecursiveSeparableImageFilterISS3ISS3 self, itkImageSS3 arg0)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_SetInputImage(self, arg0)


    def GetInputImage(self) -> "itkImageSS3 const *":
        """GetInputImage(itkRecursiveSeparableImageFilterISS3ISS3 self) -> itkImageSS3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetInputImage(self)

    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterISS3ISS3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveSeparableImageFilterISS3ISS3 *":
        """GetPointer(itkRecursiveSeparableImageFilterISS3ISS3 self) -> itkRecursiveSeparableImageFilterISS3ISS3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveSeparableImageFilterISS3ISS3

        Create a new object of the class itkRecursiveSeparableImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveSeparableImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveSeparableImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveSeparableImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveSeparableImageFilterISS3ISS3.GetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetDirection, None, itkRecursiveSeparableImageFilterISS3ISS3)
itkRecursiveSeparableImageFilterISS3ISS3.SetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_SetDirection, None, itkRecursiveSeparableImageFilterISS3ISS3)
itkRecursiveSeparableImageFilterISS3ISS3.SetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_SetInputImage, None, itkRecursiveSeparableImageFilterISS3ISS3)
itkRecursiveSeparableImageFilterISS3ISS3.GetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetInputImage, None, itkRecursiveSeparableImageFilterISS3ISS3)
itkRecursiveSeparableImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetPointer, None, itkRecursiveSeparableImageFilterISS3ISS3)
itkRecursiveSeparableImageFilterISS3ISS3_swigregister = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_swigregister
itkRecursiveSeparableImageFilterISS3ISS3_swigregister(itkRecursiveSeparableImageFilterISS3ISS3)

def itkRecursiveSeparableImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterISS3ISS3 *":
    """itkRecursiveSeparableImageFilterISS3ISS3_cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterISS3ISS3"""
    return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_cast(obj)

class itkRecursiveSeparableImageFilterIUC2IUC2(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUC2IUC2):
    """Proxy of C++ itkRecursiveSeparableImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkRecursiveSeparableImageFilterIUC2IUC2 self) -> unsigned int"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetDirection(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkRecursiveSeparableImageFilterIUC2IUC2 self, unsigned int const _arg)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_SetDirection(self, _arg)


    def SetInputImage(self, arg0: 'itkImageUC2') -> "void":
        """SetInputImage(itkRecursiveSeparableImageFilterIUC2IUC2 self, itkImageUC2 arg0)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_SetInputImage(self, arg0)


    def GetInputImage(self) -> "itkImageUC2 const *":
        """GetInputImage(itkRecursiveSeparableImageFilterIUC2IUC2 self) -> itkImageUC2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetInputImage(self)

    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIUC2IUC2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveSeparableImageFilterIUC2IUC2 *":
        """GetPointer(itkRecursiveSeparableImageFilterIUC2IUC2 self) -> itkRecursiveSeparableImageFilterIUC2IUC2"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveSeparableImageFilterIUC2IUC2

        Create a new object of the class itkRecursiveSeparableImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveSeparableImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveSeparableImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveSeparableImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveSeparableImageFilterIUC2IUC2.GetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetDirection, None, itkRecursiveSeparableImageFilterIUC2IUC2)
itkRecursiveSeparableImageFilterIUC2IUC2.SetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_SetDirection, None, itkRecursiveSeparableImageFilterIUC2IUC2)
itkRecursiveSeparableImageFilterIUC2IUC2.SetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_SetInputImage, None, itkRecursiveSeparableImageFilterIUC2IUC2)
itkRecursiveSeparableImageFilterIUC2IUC2.GetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetInputImage, None, itkRecursiveSeparableImageFilterIUC2IUC2)
itkRecursiveSeparableImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetPointer, None, itkRecursiveSeparableImageFilterIUC2IUC2)
itkRecursiveSeparableImageFilterIUC2IUC2_swigregister = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_swigregister
itkRecursiveSeparableImageFilterIUC2IUC2_swigregister(itkRecursiveSeparableImageFilterIUC2IUC2)

def itkRecursiveSeparableImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIUC2IUC2 *":
    """itkRecursiveSeparableImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIUC2IUC2"""
    return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_cast(obj)

class itkRecursiveSeparableImageFilterIUC3IUC3(itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUC3IUC3):
    """Proxy of C++ itkRecursiveSeparableImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDirection(self) -> "unsigned int":
        """GetDirection(itkRecursiveSeparableImageFilterIUC3IUC3 self) -> unsigned int"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetDirection(self)


    def SetDirection(self, _arg: 'unsigned int const') -> "void":
        """SetDirection(itkRecursiveSeparableImageFilterIUC3IUC3 self, unsigned int const _arg)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_SetDirection(self, _arg)


    def SetInputImage(self, arg0: 'itkImageUC3') -> "void":
        """SetInputImage(itkRecursiveSeparableImageFilterIUC3IUC3 self, itkImageUC3 arg0)"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_SetInputImage(self, arg0)


    def GetInputImage(self) -> "itkImageUC3 const *":
        """GetInputImage(itkRecursiveSeparableImageFilterIUC3IUC3 self) -> itkImageUC3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetInputImage(self)

    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIUC3IUC3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRecursiveSeparableImageFilterIUC3IUC3 *":
        """GetPointer(itkRecursiveSeparableImageFilterIUC3IUC3 self) -> itkRecursiveSeparableImageFilterIUC3IUC3"""
        return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRecursiveSeparableImageFilterIUC3IUC3

        Create a new object of the class itkRecursiveSeparableImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRecursiveSeparableImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRecursiveSeparableImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRecursiveSeparableImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRecursiveSeparableImageFilterIUC3IUC3.GetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetDirection, None, itkRecursiveSeparableImageFilterIUC3IUC3)
itkRecursiveSeparableImageFilterIUC3IUC3.SetDirection = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_SetDirection, None, itkRecursiveSeparableImageFilterIUC3IUC3)
itkRecursiveSeparableImageFilterIUC3IUC3.SetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_SetInputImage, None, itkRecursiveSeparableImageFilterIUC3IUC3)
itkRecursiveSeparableImageFilterIUC3IUC3.GetInputImage = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetInputImage, None, itkRecursiveSeparableImageFilterIUC3IUC3)
itkRecursiveSeparableImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetPointer, None, itkRecursiveSeparableImageFilterIUC3IUC3)
itkRecursiveSeparableImageFilterIUC3IUC3_swigregister = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_swigregister
itkRecursiveSeparableImageFilterIUC3IUC3_swigregister(itkRecursiveSeparableImageFilterIUC3IUC3)

def itkRecursiveSeparableImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkRecursiveSeparableImageFilterIUC3IUC3 *":
    """itkRecursiveSeparableImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkRecursiveSeparableImageFilterIUC3IUC3"""
    return _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_cast(obj)



