# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkKernelFunctionBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkKernelFunctionBasePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkKernelFunctionBasePython')
    _itkKernelFunctionBasePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkKernelFunctionBasePython', [dirname(__file__)])
        except ImportError:
            import _itkKernelFunctionBasePython
            return _itkKernelFunctionBasePython
        try:
            _mod = imp.load_module('_itkKernelFunctionBasePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkKernelFunctionBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkKernelFunctionBasePython
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


import itkFunctionBasePython
import ITKCommonBasePython
import pyBasePython
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkImagePython
import itkImageRegionPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython

def itkKernelFunctionBaseF_New():
  return itkKernelFunctionBaseF.New()

class itkKernelFunctionBaseF(itkFunctionBasePython.itkFunctionBaseFF):
    """Proxy of C++ itkKernelFunctionBaseF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkKernelFunctionBasePython.delete_itkKernelFunctionBaseF

    def cast(obj: 'itkLightObject') -> "itkKernelFunctionBaseF *":
        """cast(itkLightObject obj) -> itkKernelFunctionBaseF"""
        return _itkKernelFunctionBasePython.itkKernelFunctionBaseF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkKernelFunctionBaseF *":
        """GetPointer(itkKernelFunctionBaseF self) -> itkKernelFunctionBaseF"""
        return _itkKernelFunctionBasePython.itkKernelFunctionBaseF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKernelFunctionBaseF

        Create a new object of the class itkKernelFunctionBaseF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelFunctionBaseF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKernelFunctionBaseF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKernelFunctionBaseF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKernelFunctionBaseF.GetPointer = new_instancemethod(_itkKernelFunctionBasePython.itkKernelFunctionBaseF_GetPointer, None, itkKernelFunctionBaseF)
itkKernelFunctionBaseF_swigregister = _itkKernelFunctionBasePython.itkKernelFunctionBaseF_swigregister
itkKernelFunctionBaseF_swigregister(itkKernelFunctionBaseF)

def itkKernelFunctionBaseF_cast(obj: 'itkLightObject') -> "itkKernelFunctionBaseF *":
    """itkKernelFunctionBaseF_cast(itkLightObject obj) -> itkKernelFunctionBaseF"""
    return _itkKernelFunctionBasePython.itkKernelFunctionBaseF_cast(obj)



