# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTranslationTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTranslationTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTranslationTransformPython')
    _itkTranslationTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTranslationTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkTranslationTransformPython
            return _itkTranslationTransformPython
        try:
            _mod = imp.load_module('_itkTranslationTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTranslationTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTranslationTransformPython
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


import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkArray2DPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkVariableLengthVectorPython

def itkTranslationTransformD3_New():
  return itkTranslationTransformD3.New()


def itkTranslationTransformD2_New():
  return itkTranslationTransformD2.New()

class itkTranslationTransformD2(itkTransformBasePython.itkTransformD22):
    """Proxy of C++ itkTranslationTransformD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTranslationTransformD2_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTranslationTransformD2 self) -> itkTranslationTransformD2_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_Clone(self)


    def GetOffset(self):
        """GetOffset(itkTranslationTransformD2 self) -> itkVectorD2"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_GetOffset(self)


    def SetOffset(self, offset):
        """SetOffset(itkTranslationTransformD2 self, itkVectorD2 offset)"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_SetOffset(self, offset)


    def Compose(self, other, pre=False):
        """
        Compose(itkTranslationTransformD2 self, itkTranslationTransformD2 other, bool pre=False)
        Compose(itkTranslationTransformD2 self, itkTranslationTransformD2 other)
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_Compose(self, other, pre)


    def Translate(self, offset, pre=False):
        """
        Translate(itkTranslationTransformD2 self, itkVectorD2 offset, bool pre=False)
        Translate(itkTranslationTransformD2 self, itkVectorD2 offset)
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_Translate(self, offset, pre)


    def TransformVector(self, *args):
        """
        TransformVector(itkTranslationTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        TransformVector(itkTranslationTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_TransformVector(self, *args)


    def BackTransform(self, *args):
        """
        BackTransform(itkTranslationTransformD2 self, itkPointD2 point) -> itkPointD2
        BackTransform(itkTranslationTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        BackTransform(itkTranslationTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        BackTransform(itkTranslationTransformD2 self, itkCovariantVectorD2 vector) -> itkCovariantVectorD2
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_BackTransform(self, *args)


    def GetInverse(self, inverse):
        """GetInverse(itkTranslationTransformD2 self, itkTranslationTransformD2 inverse) -> bool"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_GetInverse(self, inverse)


    def SetIdentity(self):
        """SetIdentity(itkTranslationTransformD2 self)"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_SetIdentity(self)

    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD2

    def cast(obj):
        """cast(itkLightObject obj) -> itkTranslationTransformD2"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTranslationTransformD2 self) -> itkTranslationTransformD2"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTranslationTransformD2

        Create a new object of the class itkTranslationTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTranslationTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTranslationTransformD2.Clone = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_Clone, None, itkTranslationTransformD2)
itkTranslationTransformD2.GetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_GetOffset, None, itkTranslationTransformD2)
itkTranslationTransformD2.SetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_SetOffset, None, itkTranslationTransformD2)
itkTranslationTransformD2.Compose = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_Compose, None, itkTranslationTransformD2)
itkTranslationTransformD2.Translate = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_Translate, None, itkTranslationTransformD2)
itkTranslationTransformD2.TransformVector = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_TransformVector, None, itkTranslationTransformD2)
itkTranslationTransformD2.BackTransform = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_BackTransform, None, itkTranslationTransformD2)
itkTranslationTransformD2.GetInverse = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_GetInverse, None, itkTranslationTransformD2)
itkTranslationTransformD2.SetIdentity = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_SetIdentity, None, itkTranslationTransformD2)
itkTranslationTransformD2.GetPointer = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_GetPointer, None, itkTranslationTransformD2)
itkTranslationTransformD2_swigregister = _itkTranslationTransformPython.itkTranslationTransformD2_swigregister
itkTranslationTransformD2_swigregister(itkTranslationTransformD2)

def itkTranslationTransformD2___New_orig__():
    """itkTranslationTransformD2___New_orig__() -> itkTranslationTransformD2_Pointer"""
    return _itkTranslationTransformPython.itkTranslationTransformD2___New_orig__()

def itkTranslationTransformD2_cast(obj):
    """itkTranslationTransformD2_cast(itkLightObject obj) -> itkTranslationTransformD2"""
    return _itkTranslationTransformPython.itkTranslationTransformD2_cast(obj)

class itkTranslationTransformD3(itkTransformBasePython.itkTransformD33):
    """Proxy of C++ itkTranslationTransformD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkTranslationTransformD3_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkTranslationTransformD3 self) -> itkTranslationTransformD3_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_Clone(self)


    def GetOffset(self):
        """GetOffset(itkTranslationTransformD3 self) -> itkVectorD3"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_GetOffset(self)


    def SetOffset(self, offset):
        """SetOffset(itkTranslationTransformD3 self, itkVectorD3 offset)"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_SetOffset(self, offset)


    def Compose(self, other, pre=False):
        """
        Compose(itkTranslationTransformD3 self, itkTranslationTransformD3 other, bool pre=False)
        Compose(itkTranslationTransformD3 self, itkTranslationTransformD3 other)
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_Compose(self, other, pre)


    def Translate(self, offset, pre=False):
        """
        Translate(itkTranslationTransformD3 self, itkVectorD3 offset, bool pre=False)
        Translate(itkTranslationTransformD3 self, itkVectorD3 offset)
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_Translate(self, offset, pre)


    def TransformVector(self, *args):
        """
        TransformVector(itkTranslationTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        TransformVector(itkTranslationTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_TransformVector(self, *args)


    def BackTransform(self, *args):
        """
        BackTransform(itkTranslationTransformD3 self, itkPointD3 point) -> itkPointD3
        BackTransform(itkTranslationTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        BackTransform(itkTranslationTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        BackTransform(itkTranslationTransformD3 self, itkCovariantVectorD3 vector) -> itkCovariantVectorD3
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_BackTransform(self, *args)


    def GetInverse(self, inverse):
        """GetInverse(itkTranslationTransformD3 self, itkTranslationTransformD3 inverse) -> bool"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_GetInverse(self, inverse)


    def SetIdentity(self):
        """SetIdentity(itkTranslationTransformD3 self)"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_SetIdentity(self)

    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD3

    def cast(obj):
        """cast(itkLightObject obj) -> itkTranslationTransformD3"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkTranslationTransformD3 self) -> itkTranslationTransformD3"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTranslationTransformD3

        Create a new object of the class itkTranslationTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTranslationTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTranslationTransformD3.Clone = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_Clone, None, itkTranslationTransformD3)
itkTranslationTransformD3.GetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_GetOffset, None, itkTranslationTransformD3)
itkTranslationTransformD3.SetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_SetOffset, None, itkTranslationTransformD3)
itkTranslationTransformD3.Compose = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_Compose, None, itkTranslationTransformD3)
itkTranslationTransformD3.Translate = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_Translate, None, itkTranslationTransformD3)
itkTranslationTransformD3.TransformVector = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_TransformVector, None, itkTranslationTransformD3)
itkTranslationTransformD3.BackTransform = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_BackTransform, None, itkTranslationTransformD3)
itkTranslationTransformD3.GetInverse = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_GetInverse, None, itkTranslationTransformD3)
itkTranslationTransformD3.SetIdentity = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_SetIdentity, None, itkTranslationTransformD3)
itkTranslationTransformD3.GetPointer = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_GetPointer, None, itkTranslationTransformD3)
itkTranslationTransformD3_swigregister = _itkTranslationTransformPython.itkTranslationTransformD3_swigregister
itkTranslationTransformD3_swigregister(itkTranslationTransformD3)

def itkTranslationTransformD3___New_orig__():
    """itkTranslationTransformD3___New_orig__() -> itkTranslationTransformD3_Pointer"""
    return _itkTranslationTransformPython.itkTranslationTransformD3___New_orig__()

def itkTranslationTransformD3_cast(obj):
    """itkTranslationTransformD3_cast(itkLightObject obj) -> itkTranslationTransformD3"""
    return _itkTranslationTransformPython.itkTranslationTransformD3_cast(obj)



