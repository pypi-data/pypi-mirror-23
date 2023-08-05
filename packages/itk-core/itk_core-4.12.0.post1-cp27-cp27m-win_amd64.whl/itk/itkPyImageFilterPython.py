# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPyImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPyImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPyImageFilterPython')
    _itkPyImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPyImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkPyImageFilterPython
            return _itkPyImageFilterPython
        try:
            _mod = imp.load_module('_itkPyImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPyImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPyImageFilterPython
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

def itkPyImageFilterIUC3IUC3_New():
  return itkPyImageFilterIUC3IUC3.New()


def itkPyImageFilterIUC2IUC2_New():
  return itkPyImageFilterIUC2IUC2.New()

class itkPyImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkPyImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPyImageFilterIUC2IUC2_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPyImageFilterIUC2IUC2 self) -> itkPyImageFilterIUC2IUC2_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_Clone(self)


    def SetPyGenerateData(self, obj):
        """SetPyGenerateData(itkPyImageFilterIUC2IUC2 self, PyObject * obj)"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_SetPyGenerateData(self, obj)

    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC2IUC2

    def cast(obj):
        """cast(itkLightObject obj) -> itkPyImageFilterIUC2IUC2"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPyImageFilterIUC2IUC2 self) -> itkPyImageFilterIUC2IUC2"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC2IUC2

        Create a new object of the class itkPyImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyImageFilterIUC2IUC2.Clone = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_Clone, None, itkPyImageFilterIUC2IUC2)
itkPyImageFilterIUC2IUC2.SetPyGenerateData = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_SetPyGenerateData, None, itkPyImageFilterIUC2IUC2)
itkPyImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_GetPointer, None, itkPyImageFilterIUC2IUC2)
itkPyImageFilterIUC2IUC2_swigregister = _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_swigregister
itkPyImageFilterIUC2IUC2_swigregister(itkPyImageFilterIUC2IUC2)

def itkPyImageFilterIUC2IUC2___New_orig__():
    """itkPyImageFilterIUC2IUC2___New_orig__() -> itkPyImageFilterIUC2IUC2_Pointer"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2___New_orig__()

def itkPyImageFilterIUC2IUC2_cast(obj):
    """itkPyImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkPyImageFilterIUC2IUC2"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_cast(obj)

class itkPyImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkPyImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPyImageFilterIUC3IUC3_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPyImageFilterIUC3IUC3 self) -> itkPyImageFilterIUC3IUC3_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_Clone(self)


    def SetPyGenerateData(self, obj):
        """SetPyGenerateData(itkPyImageFilterIUC3IUC3 self, PyObject * obj)"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_SetPyGenerateData(self, obj)

    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC3IUC3

    def cast(obj):
        """cast(itkLightObject obj) -> itkPyImageFilterIUC3IUC3"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPyImageFilterIUC3IUC3 self) -> itkPyImageFilterIUC3IUC3"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC3IUC3

        Create a new object of the class itkPyImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyImageFilterIUC3IUC3.Clone = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_Clone, None, itkPyImageFilterIUC3IUC3)
itkPyImageFilterIUC3IUC3.SetPyGenerateData = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_SetPyGenerateData, None, itkPyImageFilterIUC3IUC3)
itkPyImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_GetPointer, None, itkPyImageFilterIUC3IUC3)
itkPyImageFilterIUC3IUC3_swigregister = _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_swigregister
itkPyImageFilterIUC3IUC3_swigregister(itkPyImageFilterIUC3IUC3)

def itkPyImageFilterIUC3IUC3___New_orig__():
    """itkPyImageFilterIUC3IUC3___New_orig__() -> itkPyImageFilterIUC3IUC3_Pointer"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3___New_orig__()

def itkPyImageFilterIUC3IUC3_cast(obj):
    """itkPyImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkPyImageFilterIUC3IUC3"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_cast(obj)



