# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCenteredAffineTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkCenteredAffineTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkCenteredAffineTransformPython')
    _itkCenteredAffineTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCenteredAffineTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkCenteredAffineTransformPython
            return _itkCenteredAffineTransformPython
        try:
            _mod = imp.load_module('_itkCenteredAffineTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkCenteredAffineTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCenteredAffineTransformPython
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


import itkOptimizerParametersPython
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import ITKCommonBasePython
import itkAffineTransformPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkTransformBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython

def itkCenteredAffineTransformD3_New():
  return itkCenteredAffineTransformD3.New()


def itkCenteredAffineTransformD2_New():
  return itkCenteredAffineTransformD2.New()

class itkCenteredAffineTransformD2(itkAffineTransformPython.itkAffineTransformD2):
    """Proxy of C++ itkCenteredAffineTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkCenteredAffineTransformD2_Pointer"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkCenteredAffineTransformD2 self) -> itkCenteredAffineTransformD2_Pointer"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_Clone(self)


    def GetInverse(self, inverse):
        """GetInverse(itkCenteredAffineTransformD2 self, itkCenteredAffineTransformD2 inverse) -> bool"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_GetInverse(self, inverse)

    __swig_destroy__ = _itkCenteredAffineTransformPython.delete_itkCenteredAffineTransformD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkCenteredAffineTransformD2"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkCenteredAffineTransformD2 self) -> itkCenteredAffineTransformD2"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCenteredAffineTransformD2

        Create a new object of the class itkCenteredAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredAffineTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredAffineTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredAffineTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredAffineTransformD2.Clone = new_instancemethod(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_Clone, None, itkCenteredAffineTransformD2)
itkCenteredAffineTransformD2.GetInverse = new_instancemethod(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_GetInverse, None, itkCenteredAffineTransformD2)
itkCenteredAffineTransformD2.GetPointer = new_instancemethod(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_GetPointer, None, itkCenteredAffineTransformD2)
itkCenteredAffineTransformD2_swigregister = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_swigregister
itkCenteredAffineTransformD2_swigregister(itkCenteredAffineTransformD2)

def itkCenteredAffineTransformD2___New_orig__():
    """itkCenteredAffineTransformD2___New_orig__() -> itkCenteredAffineTransformD2_Pointer"""
    return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2___New_orig__()

def itkCenteredAffineTransformD2_cast(obj):
    """itkCenteredAffineTransformD2_cast(itkLightObject obj) -> itkCenteredAffineTransformD2"""
    return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_cast(obj)

class itkCenteredAffineTransformD3(itkAffineTransformPython.itkAffineTransformD3):
    """Proxy of C++ itkCenteredAffineTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkCenteredAffineTransformD3_Pointer"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkCenteredAffineTransformD3 self) -> itkCenteredAffineTransformD3_Pointer"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_Clone(self)


    def GetInverse(self, inverse):
        """GetInverse(itkCenteredAffineTransformD3 self, itkCenteredAffineTransformD3 inverse) -> bool"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_GetInverse(self, inverse)

    __swig_destroy__ = _itkCenteredAffineTransformPython.delete_itkCenteredAffineTransformD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkCenteredAffineTransformD3"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkCenteredAffineTransformD3 self) -> itkCenteredAffineTransformD3"""
        return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkCenteredAffineTransformD3

        Create a new object of the class itkCenteredAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredAffineTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredAffineTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredAffineTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredAffineTransformD3.Clone = new_instancemethod(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_Clone, None, itkCenteredAffineTransformD3)
itkCenteredAffineTransformD3.GetInverse = new_instancemethod(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_GetInverse, None, itkCenteredAffineTransformD3)
itkCenteredAffineTransformD3.GetPointer = new_instancemethod(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_GetPointer, None, itkCenteredAffineTransformD3)
itkCenteredAffineTransformD3_swigregister = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_swigregister
itkCenteredAffineTransformD3_swigregister(itkCenteredAffineTransformD3)

def itkCenteredAffineTransformD3___New_orig__():
    """itkCenteredAffineTransformD3___New_orig__() -> itkCenteredAffineTransformD3_Pointer"""
    return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3___New_orig__()

def itkCenteredAffineTransformD3_cast(obj):
    """itkCenteredAffineTransformD3_cast(itkLightObject obj) -> itkCenteredAffineTransformD3"""
    return _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_cast(obj)



