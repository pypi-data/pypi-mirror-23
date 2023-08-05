# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBoxImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBoxImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBoxImageFilterPython')
    _itkBoxImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBoxImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBoxImageFilterPython
            return _itkBoxImageFilterPython
        try:
            _mod = imp.load_module('_itkBoxImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBoxImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBoxImageFilterPython
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


import itkImageToImageFilterAPython
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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkBoxImageFilterIF3IF3_New():
  return itkBoxImageFilterIF3IF3.New()


def itkBoxImageFilterIF2IF2_New():
  return itkBoxImageFilterIF2IF2.New()


def itkBoxImageFilterIUC3IUC3_New():
  return itkBoxImageFilterIUC3IUC3.New()


def itkBoxImageFilterIUC2IUC2_New():
  return itkBoxImageFilterIUC2IUC2.New()


def itkBoxImageFilterISS3ISS3_New():
  return itkBoxImageFilterISS3ISS3.New()


def itkBoxImageFilterISS2ISS2_New():
  return itkBoxImageFilterISS2ISS2.New()

class itkBoxImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """Proxy of C++ itkBoxImageFilterIF2IF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxImageFilterIF2IF2_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxImageFilterIF2IF2 self) -> itkBoxImageFilterIF2IF2_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_Clone(self)


    def SetRadius(self, *args):
        """
        SetRadius(itkBoxImageFilterIF2IF2 self, itkSize2 radius)
        SetRadius(itkBoxImageFilterIF2IF2 self, unsigned long const & radius)
        """
        return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_SetRadius(self, *args)


    def GetRadius(self):
        """GetRadius(itkBoxImageFilterIF2IF2 self) -> itkSize2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_GetRadius(self)

    __swig_destroy__ = _itkBoxImageFilterPython.delete_itkBoxImageFilterIF2IF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxImageFilterIF2IF2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxImageFilterIF2IF2 self) -> itkBoxImageFilterIF2IF2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxImageFilterIF2IF2

        Create a new object of the class itkBoxImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxImageFilterIF2IF2.Clone = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_Clone, None, itkBoxImageFilterIF2IF2)
itkBoxImageFilterIF2IF2.SetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_SetRadius, None, itkBoxImageFilterIF2IF2)
itkBoxImageFilterIF2IF2.GetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_GetRadius, None, itkBoxImageFilterIF2IF2)
itkBoxImageFilterIF2IF2.GetPointer = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_GetPointer, None, itkBoxImageFilterIF2IF2)
itkBoxImageFilterIF2IF2_swigregister = _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_swigregister
itkBoxImageFilterIF2IF2_swigregister(itkBoxImageFilterIF2IF2)

def itkBoxImageFilterIF2IF2___New_orig__():
    """itkBoxImageFilterIF2IF2___New_orig__() -> itkBoxImageFilterIF2IF2_Pointer"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2___New_orig__()

def itkBoxImageFilterIF2IF2_cast(obj):
    """itkBoxImageFilterIF2IF2_cast(itkLightObject obj) -> itkBoxImageFilterIF2IF2"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIF2IF2_cast(obj)

class itkBoxImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """Proxy of C++ itkBoxImageFilterIF3IF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxImageFilterIF3IF3_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxImageFilterIF3IF3 self) -> itkBoxImageFilterIF3IF3_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_Clone(self)


    def SetRadius(self, *args):
        """
        SetRadius(itkBoxImageFilterIF3IF3 self, itkSize3 radius)
        SetRadius(itkBoxImageFilterIF3IF3 self, unsigned long const & radius)
        """
        return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_SetRadius(self, *args)


    def GetRadius(self):
        """GetRadius(itkBoxImageFilterIF3IF3 self) -> itkSize3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_GetRadius(self)

    __swig_destroy__ = _itkBoxImageFilterPython.delete_itkBoxImageFilterIF3IF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxImageFilterIF3IF3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxImageFilterIF3IF3 self) -> itkBoxImageFilterIF3IF3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxImageFilterIF3IF3

        Create a new object of the class itkBoxImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxImageFilterIF3IF3.Clone = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_Clone, None, itkBoxImageFilterIF3IF3)
itkBoxImageFilterIF3IF3.SetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_SetRadius, None, itkBoxImageFilterIF3IF3)
itkBoxImageFilterIF3IF3.GetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_GetRadius, None, itkBoxImageFilterIF3IF3)
itkBoxImageFilterIF3IF3.GetPointer = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_GetPointer, None, itkBoxImageFilterIF3IF3)
itkBoxImageFilterIF3IF3_swigregister = _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_swigregister
itkBoxImageFilterIF3IF3_swigregister(itkBoxImageFilterIF3IF3)

def itkBoxImageFilterIF3IF3___New_orig__():
    """itkBoxImageFilterIF3IF3___New_orig__() -> itkBoxImageFilterIF3IF3_Pointer"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3___New_orig__()

def itkBoxImageFilterIF3IF3_cast(obj):
    """itkBoxImageFilterIF3IF3_cast(itkLightObject obj) -> itkBoxImageFilterIF3IF3"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIF3IF3_cast(obj)

class itkBoxImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """Proxy of C++ itkBoxImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxImageFilterISS2ISS2_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxImageFilterISS2ISS2 self) -> itkBoxImageFilterISS2ISS2_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_Clone(self)


    def SetRadius(self, *args):
        """
        SetRadius(itkBoxImageFilterISS2ISS2 self, itkSize2 radius)
        SetRadius(itkBoxImageFilterISS2ISS2 self, unsigned long const & radius)
        """
        return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_SetRadius(self, *args)


    def GetRadius(self):
        """GetRadius(itkBoxImageFilterISS2ISS2 self) -> itkSize2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_GetRadius(self)

    __swig_destroy__ = _itkBoxImageFilterPython.delete_itkBoxImageFilterISS2ISS2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxImageFilterISS2ISS2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxImageFilterISS2ISS2 self) -> itkBoxImageFilterISS2ISS2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxImageFilterISS2ISS2

        Create a new object of the class itkBoxImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxImageFilterISS2ISS2.Clone = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_Clone, None, itkBoxImageFilterISS2ISS2)
itkBoxImageFilterISS2ISS2.SetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_SetRadius, None, itkBoxImageFilterISS2ISS2)
itkBoxImageFilterISS2ISS2.GetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_GetRadius, None, itkBoxImageFilterISS2ISS2)
itkBoxImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_GetPointer, None, itkBoxImageFilterISS2ISS2)
itkBoxImageFilterISS2ISS2_swigregister = _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_swigregister
itkBoxImageFilterISS2ISS2_swigregister(itkBoxImageFilterISS2ISS2)

def itkBoxImageFilterISS2ISS2___New_orig__():
    """itkBoxImageFilterISS2ISS2___New_orig__() -> itkBoxImageFilterISS2ISS2_Pointer"""
    return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2___New_orig__()

def itkBoxImageFilterISS2ISS2_cast(obj):
    """itkBoxImageFilterISS2ISS2_cast(itkLightObject obj) -> itkBoxImageFilterISS2ISS2"""
    return _itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2_cast(obj)

class itkBoxImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    """Proxy of C++ itkBoxImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxImageFilterISS3ISS3_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxImageFilterISS3ISS3 self) -> itkBoxImageFilterISS3ISS3_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_Clone(self)


    def SetRadius(self, *args):
        """
        SetRadius(itkBoxImageFilterISS3ISS3 self, itkSize3 radius)
        SetRadius(itkBoxImageFilterISS3ISS3 self, unsigned long const & radius)
        """
        return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_SetRadius(self, *args)


    def GetRadius(self):
        """GetRadius(itkBoxImageFilterISS3ISS3 self) -> itkSize3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_GetRadius(self)

    __swig_destroy__ = _itkBoxImageFilterPython.delete_itkBoxImageFilterISS3ISS3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxImageFilterISS3ISS3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxImageFilterISS3ISS3 self) -> itkBoxImageFilterISS3ISS3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxImageFilterISS3ISS3

        Create a new object of the class itkBoxImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxImageFilterISS3ISS3.Clone = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_Clone, None, itkBoxImageFilterISS3ISS3)
itkBoxImageFilterISS3ISS3.SetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_SetRadius, None, itkBoxImageFilterISS3ISS3)
itkBoxImageFilterISS3ISS3.GetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_GetRadius, None, itkBoxImageFilterISS3ISS3)
itkBoxImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_GetPointer, None, itkBoxImageFilterISS3ISS3)
itkBoxImageFilterISS3ISS3_swigregister = _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_swigregister
itkBoxImageFilterISS3ISS3_swigregister(itkBoxImageFilterISS3ISS3)

def itkBoxImageFilterISS3ISS3___New_orig__():
    """itkBoxImageFilterISS3ISS3___New_orig__() -> itkBoxImageFilterISS3ISS3_Pointer"""
    return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3___New_orig__()

def itkBoxImageFilterISS3ISS3_cast(obj):
    """itkBoxImageFilterISS3ISS3_cast(itkLightObject obj) -> itkBoxImageFilterISS3ISS3"""
    return _itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3_cast(obj)

class itkBoxImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkBoxImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxImageFilterIUC2IUC2_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxImageFilterIUC2IUC2 self) -> itkBoxImageFilterIUC2IUC2_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_Clone(self)


    def SetRadius(self, *args):
        """
        SetRadius(itkBoxImageFilterIUC2IUC2 self, itkSize2 radius)
        SetRadius(itkBoxImageFilterIUC2IUC2 self, unsigned long const & radius)
        """
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_SetRadius(self, *args)


    def GetRadius(self):
        """GetRadius(itkBoxImageFilterIUC2IUC2 self) -> itkSize2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_GetRadius(self)

    __swig_destroy__ = _itkBoxImageFilterPython.delete_itkBoxImageFilterIUC2IUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxImageFilterIUC2IUC2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxImageFilterIUC2IUC2 self) -> itkBoxImageFilterIUC2IUC2"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxImageFilterIUC2IUC2

        Create a new object of the class itkBoxImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxImageFilterIUC2IUC2.Clone = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_Clone, None, itkBoxImageFilterIUC2IUC2)
itkBoxImageFilterIUC2IUC2.SetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_SetRadius, None, itkBoxImageFilterIUC2IUC2)
itkBoxImageFilterIUC2IUC2.GetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_GetRadius, None, itkBoxImageFilterIUC2IUC2)
itkBoxImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_GetPointer, None, itkBoxImageFilterIUC2IUC2)
itkBoxImageFilterIUC2IUC2_swigregister = _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_swigregister
itkBoxImageFilterIUC2IUC2_swigregister(itkBoxImageFilterIUC2IUC2)

def itkBoxImageFilterIUC2IUC2___New_orig__():
    """itkBoxImageFilterIUC2IUC2___New_orig__() -> itkBoxImageFilterIUC2IUC2_Pointer"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2___New_orig__()

def itkBoxImageFilterIUC2IUC2_cast(obj):
    """itkBoxImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkBoxImageFilterIUC2IUC2"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2_cast(obj)

class itkBoxImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkBoxImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBoxImageFilterIUC3IUC3_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBoxImageFilterIUC3IUC3 self) -> itkBoxImageFilterIUC3IUC3_Pointer"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_Clone(self)


    def SetRadius(self, *args):
        """
        SetRadius(itkBoxImageFilterIUC3IUC3 self, itkSize3 radius)
        SetRadius(itkBoxImageFilterIUC3IUC3 self, unsigned long const & radius)
        """
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_SetRadius(self, *args)


    def GetRadius(self):
        """GetRadius(itkBoxImageFilterIUC3IUC3 self) -> itkSize3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_GetRadius(self)

    __swig_destroy__ = _itkBoxImageFilterPython.delete_itkBoxImageFilterIUC3IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkBoxImageFilterIUC3IUC3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBoxImageFilterIUC3IUC3 self) -> itkBoxImageFilterIUC3IUC3"""
        return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBoxImageFilterIUC3IUC3

        Create a new object of the class itkBoxImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBoxImageFilterIUC3IUC3.Clone = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_Clone, None, itkBoxImageFilterIUC3IUC3)
itkBoxImageFilterIUC3IUC3.SetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_SetRadius, None, itkBoxImageFilterIUC3IUC3)
itkBoxImageFilterIUC3IUC3.GetRadius = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_GetRadius, None, itkBoxImageFilterIUC3IUC3)
itkBoxImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_GetPointer, None, itkBoxImageFilterIUC3IUC3)
itkBoxImageFilterIUC3IUC3_swigregister = _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_swigregister
itkBoxImageFilterIUC3IUC3_swigregister(itkBoxImageFilterIUC3IUC3)

def itkBoxImageFilterIUC3IUC3___New_orig__():
    """itkBoxImageFilterIUC3IUC3___New_orig__() -> itkBoxImageFilterIUC3IUC3_Pointer"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3___New_orig__()

def itkBoxImageFilterIUC3IUC3_cast(obj):
    """itkBoxImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkBoxImageFilterIUC3IUC3"""
    return _itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3_cast(obj)



