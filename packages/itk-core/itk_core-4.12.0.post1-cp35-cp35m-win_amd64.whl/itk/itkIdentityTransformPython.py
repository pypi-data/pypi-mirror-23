# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIdentityTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkIdentityTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkIdentityTransformPython')
    _itkIdentityTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIdentityTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkIdentityTransformPython
            return _itkIdentityTransformPython
        try:
            _mod = imp.load_module('_itkIdentityTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkIdentityTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIdentityTransformPython
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
import itkArray2DPython
import ITKCommonBasePython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkVariableLengthVectorPython

def itkIdentityTransformD3_New():
  return itkIdentityTransformD3.New()


def itkIdentityTransformD2_New():
  return itkIdentityTransformD2.New()

class itkIdentityTransformD2(itkTransformBasePython.itkTransformD22):
    """Proxy of C++ itkIdentityTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIdentityTransformD2_Pointer":
        """__New_orig__() -> itkIdentityTransformD2_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIdentityTransformD2_Pointer":
        """Clone(itkIdentityTransformD2 self) -> itkIdentityTransformD2_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_Clone(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkIdentityTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        TransformVector(itkIdentityTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        """
        return _itkIdentityTransformPython.itkIdentityTransformD2_TransformVector(self, *args)


    def SetIdentity(self) -> "void":
        """SetIdentity(itkIdentityTransformD2 self)"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_SetIdentity(self)


    def GetInverse(self, inverseTransform: 'itkIdentityTransformD2') -> "bool":
        """GetInverse(itkIdentityTransformD2 self, itkIdentityTransformD2 inverseTransform) -> bool"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_GetInverse(self, inverseTransform)

    __swig_destroy__ = _itkIdentityTransformPython.delete_itkIdentityTransformD2

    def cast(obj: 'itkLightObject') -> "itkIdentityTransformD2 *":
        """cast(itkLightObject obj) -> itkIdentityTransformD2"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIdentityTransformD2 *":
        """GetPointer(itkIdentityTransformD2 self) -> itkIdentityTransformD2"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIdentityTransformD2

        Create a new object of the class itkIdentityTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIdentityTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIdentityTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIdentityTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIdentityTransformD2.Clone = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_Clone, None, itkIdentityTransformD2)
itkIdentityTransformD2.TransformVector = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_TransformVector, None, itkIdentityTransformD2)
itkIdentityTransformD2.SetIdentity = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_SetIdentity, None, itkIdentityTransformD2)
itkIdentityTransformD2.GetInverse = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_GetInverse, None, itkIdentityTransformD2)
itkIdentityTransformD2.GetPointer = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_GetPointer, None, itkIdentityTransformD2)
itkIdentityTransformD2_swigregister = _itkIdentityTransformPython.itkIdentityTransformD2_swigregister
itkIdentityTransformD2_swigregister(itkIdentityTransformD2)

def itkIdentityTransformD2___New_orig__() -> "itkIdentityTransformD2_Pointer":
    """itkIdentityTransformD2___New_orig__() -> itkIdentityTransformD2_Pointer"""
    return _itkIdentityTransformPython.itkIdentityTransformD2___New_orig__()

def itkIdentityTransformD2_cast(obj: 'itkLightObject') -> "itkIdentityTransformD2 *":
    """itkIdentityTransformD2_cast(itkLightObject obj) -> itkIdentityTransformD2"""
    return _itkIdentityTransformPython.itkIdentityTransformD2_cast(obj)

class itkIdentityTransformD3(itkTransformBasePython.itkTransformD33):
    """Proxy of C++ itkIdentityTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIdentityTransformD3_Pointer":
        """__New_orig__() -> itkIdentityTransformD3_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIdentityTransformD3_Pointer":
        """Clone(itkIdentityTransformD3 self) -> itkIdentityTransformD3_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_Clone(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkIdentityTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        TransformVector(itkIdentityTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        """
        return _itkIdentityTransformPython.itkIdentityTransformD3_TransformVector(self, *args)


    def SetIdentity(self) -> "void":
        """SetIdentity(itkIdentityTransformD3 self)"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_SetIdentity(self)


    def GetInverse(self, inverseTransform: 'itkIdentityTransformD3') -> "bool":
        """GetInverse(itkIdentityTransformD3 self, itkIdentityTransformD3 inverseTransform) -> bool"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_GetInverse(self, inverseTransform)

    __swig_destroy__ = _itkIdentityTransformPython.delete_itkIdentityTransformD3

    def cast(obj: 'itkLightObject') -> "itkIdentityTransformD3 *":
        """cast(itkLightObject obj) -> itkIdentityTransformD3"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIdentityTransformD3 *":
        """GetPointer(itkIdentityTransformD3 self) -> itkIdentityTransformD3"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIdentityTransformD3

        Create a new object of the class itkIdentityTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIdentityTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIdentityTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIdentityTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIdentityTransformD3.Clone = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_Clone, None, itkIdentityTransformD3)
itkIdentityTransformD3.TransformVector = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_TransformVector, None, itkIdentityTransformD3)
itkIdentityTransformD3.SetIdentity = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_SetIdentity, None, itkIdentityTransformD3)
itkIdentityTransformD3.GetInverse = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_GetInverse, None, itkIdentityTransformD3)
itkIdentityTransformD3.GetPointer = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_GetPointer, None, itkIdentityTransformD3)
itkIdentityTransformD3_swigregister = _itkIdentityTransformPython.itkIdentityTransformD3_swigregister
itkIdentityTransformD3_swigregister(itkIdentityTransformD3)

def itkIdentityTransformD3___New_orig__() -> "itkIdentityTransformD3_Pointer":
    """itkIdentityTransformD3___New_orig__() -> itkIdentityTransformD3_Pointer"""
    return _itkIdentityTransformPython.itkIdentityTransformD3___New_orig__()

def itkIdentityTransformD3_cast(obj: 'itkLightObject') -> "itkIdentityTransformD3 *":
    """itkIdentityTransformD3_cast(itkLightObject obj) -> itkIdentityTransformD3"""
    return _itkIdentityTransformPython.itkIdentityTransformD3_cast(obj)



