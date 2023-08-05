# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMultiTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMultiTransformPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMultiTransformPython')
    _itkMultiTransformPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMultiTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkMultiTransformPython
            return _itkMultiTransformPython
        try:
            _mod = imp.load_module('_itkMultiTransformPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMultiTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMultiTransformPython
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


import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkTransformBasePython
import itkArray2DPython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython

def itkMultiTransformD33_New():
  return itkMultiTransformD33.New()


def itkMultiTransformD22_New():
  return itkMultiTransformD22.New()

class itkMultiTransformD22(itkTransformBasePython.itkTransformD22):
    """Proxy of C++ itkMultiTransformD22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def AddTransform(self, t: 'itkTransformD22') -> "void":
        """AddTransform(itkMultiTransformD22 self, itkTransformD22 t)"""
        return _itkMultiTransformPython.itkMultiTransformD22_AddTransform(self, t)


    def AppendTransform(self, t: 'itkTransformD22') -> "void":
        """AppendTransform(itkMultiTransformD22 self, itkTransformD22 t)"""
        return _itkMultiTransformPython.itkMultiTransformD22_AppendTransform(self, t)


    def PrependTransform(self, t: 'itkTransformD22') -> "void":
        """PrependTransform(itkMultiTransformD22 self, itkTransformD22 t)"""
        return _itkMultiTransformPython.itkMultiTransformD22_PrependTransform(self, t)


    def RemoveTransform(self) -> "void":
        """RemoveTransform(itkMultiTransformD22 self)"""
        return _itkMultiTransformPython.itkMultiTransformD22_RemoveTransform(self)


    def GetFrontTransform(self) -> "itkTransformD22 const *":
        """GetFrontTransform(itkMultiTransformD22 self) -> itkTransformD22"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetFrontTransform(self)


    def GetBackTransform(self) -> "itkTransformD22 const *":
        """GetBackTransform(itkMultiTransformD22 self) -> itkTransformD22"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetBackTransform(self)


    def GetNthTransform(self, n: 'unsigned long long') -> "itkTransformD22_Pointer const":
        """GetNthTransform(itkMultiTransformD22 self, unsigned long long n) -> itkTransformD22_Pointer const"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetNthTransform(self, n)


    def GetNthTransformModifiablePointer(self, n: 'unsigned long long const') -> "itkTransformD22 *":
        """GetNthTransformModifiablePointer(itkMultiTransformD22 self, unsigned long long const n) -> itkTransformD22"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetNthTransformModifiablePointer(self, n)


    def GetNthTransformConstPointer(self, n: 'unsigned long long const') -> "itkTransformD22 const *":
        """GetNthTransformConstPointer(itkMultiTransformD22 self, unsigned long long const n) -> itkTransformD22"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetNthTransformConstPointer(self, n)


    def GetTransformQueue(self) -> "std::deque< itkTransformD22_Pointer > const &":
        """GetTransformQueue(itkMultiTransformD22 self) -> std::deque< itkTransformD22_Pointer > const &"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetTransformQueue(self)


    def IsTransformQueueEmpty(self) -> "bool":
        """IsTransformQueueEmpty(itkMultiTransformD22 self) -> bool"""
        return _itkMultiTransformPython.itkMultiTransformD22_IsTransformQueueEmpty(self)


    def GetNumberOfTransforms(self) -> "unsigned long long":
        """GetNumberOfTransforms(itkMultiTransformD22 self) -> unsigned long long"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetNumberOfTransforms(self)


    def ClearTransformQueue(self) -> "void":
        """ClearTransformQueue(itkMultiTransformD22 self)"""
        return _itkMultiTransformPython.itkMultiTransformD22_ClearTransformQueue(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkMultiTransformD22 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkMultiTransformD22 self, itkArrayD update)
        """
        return _itkMultiTransformPython.itkMultiTransformD22_UpdateTransformParameters(self, update, factor)


    def GetInverse(self, inverse: 'itkMultiTransformD22') -> "bool":
        """GetInverse(itkMultiTransformD22 self, itkMultiTransformD22 inverse) -> bool"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetInverse(self, inverse)

    __swig_destroy__ = _itkMultiTransformPython.delete_itkMultiTransformD22

    def cast(obj: 'itkLightObject') -> "itkMultiTransformD22 *":
        """cast(itkLightObject obj) -> itkMultiTransformD22"""
        return _itkMultiTransformPython.itkMultiTransformD22_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMultiTransformD22 *":
        """GetPointer(itkMultiTransformD22 self) -> itkMultiTransformD22"""
        return _itkMultiTransformPython.itkMultiTransformD22_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMultiTransformD22

        Create a new object of the class itkMultiTransformD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultiTransformD22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultiTransformD22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultiTransformD22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMultiTransformD22.AddTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_AddTransform, None, itkMultiTransformD22)
itkMultiTransformD22.AppendTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_AppendTransform, None, itkMultiTransformD22)
itkMultiTransformD22.PrependTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_PrependTransform, None, itkMultiTransformD22)
itkMultiTransformD22.RemoveTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_RemoveTransform, None, itkMultiTransformD22)
itkMultiTransformD22.GetFrontTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetFrontTransform, None, itkMultiTransformD22)
itkMultiTransformD22.GetBackTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetBackTransform, None, itkMultiTransformD22)
itkMultiTransformD22.GetNthTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetNthTransform, None, itkMultiTransformD22)
itkMultiTransformD22.GetNthTransformModifiablePointer = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetNthTransformModifiablePointer, None, itkMultiTransformD22)
itkMultiTransformD22.GetNthTransformConstPointer = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetNthTransformConstPointer, None, itkMultiTransformD22)
itkMultiTransformD22.GetTransformQueue = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetTransformQueue, None, itkMultiTransformD22)
itkMultiTransformD22.IsTransformQueueEmpty = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_IsTransformQueueEmpty, None, itkMultiTransformD22)
itkMultiTransformD22.GetNumberOfTransforms = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetNumberOfTransforms, None, itkMultiTransformD22)
itkMultiTransformD22.ClearTransformQueue = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_ClearTransformQueue, None, itkMultiTransformD22)
itkMultiTransformD22.UpdateTransformParameters = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_UpdateTransformParameters, None, itkMultiTransformD22)
itkMultiTransformD22.GetInverse = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetInverse, None, itkMultiTransformD22)
itkMultiTransformD22.GetPointer = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD22_GetPointer, None, itkMultiTransformD22)
itkMultiTransformD22_swigregister = _itkMultiTransformPython.itkMultiTransformD22_swigregister
itkMultiTransformD22_swigregister(itkMultiTransformD22)

def itkMultiTransformD22_cast(obj: 'itkLightObject') -> "itkMultiTransformD22 *":
    """itkMultiTransformD22_cast(itkLightObject obj) -> itkMultiTransformD22"""
    return _itkMultiTransformPython.itkMultiTransformD22_cast(obj)

class itkMultiTransformD33(itkTransformBasePython.itkTransformD33):
    """Proxy of C++ itkMultiTransformD33 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def AddTransform(self, t: 'itkTransformD33') -> "void":
        """AddTransform(itkMultiTransformD33 self, itkTransformD33 t)"""
        return _itkMultiTransformPython.itkMultiTransformD33_AddTransform(self, t)


    def AppendTransform(self, t: 'itkTransformD33') -> "void":
        """AppendTransform(itkMultiTransformD33 self, itkTransformD33 t)"""
        return _itkMultiTransformPython.itkMultiTransformD33_AppendTransform(self, t)


    def PrependTransform(self, t: 'itkTransformD33') -> "void":
        """PrependTransform(itkMultiTransformD33 self, itkTransformD33 t)"""
        return _itkMultiTransformPython.itkMultiTransformD33_PrependTransform(self, t)


    def RemoveTransform(self) -> "void":
        """RemoveTransform(itkMultiTransformD33 self)"""
        return _itkMultiTransformPython.itkMultiTransformD33_RemoveTransform(self)


    def GetFrontTransform(self) -> "itkTransformD33 const *":
        """GetFrontTransform(itkMultiTransformD33 self) -> itkTransformD33"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetFrontTransform(self)


    def GetBackTransform(self) -> "itkTransformD33 const *":
        """GetBackTransform(itkMultiTransformD33 self) -> itkTransformD33"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetBackTransform(self)


    def GetNthTransform(self, n: 'unsigned long long') -> "itkTransformD33_Pointer const":
        """GetNthTransform(itkMultiTransformD33 self, unsigned long long n) -> itkTransformD33_Pointer const"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetNthTransform(self, n)


    def GetNthTransformModifiablePointer(self, n: 'unsigned long long const') -> "itkTransformD33 *":
        """GetNthTransformModifiablePointer(itkMultiTransformD33 self, unsigned long long const n) -> itkTransformD33"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetNthTransformModifiablePointer(self, n)


    def GetNthTransformConstPointer(self, n: 'unsigned long long const') -> "itkTransformD33 const *":
        """GetNthTransformConstPointer(itkMultiTransformD33 self, unsigned long long const n) -> itkTransformD33"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetNthTransformConstPointer(self, n)


    def GetTransformQueue(self) -> "std::deque< itkTransformD33_Pointer > const &":
        """GetTransformQueue(itkMultiTransformD33 self) -> std::deque< itkTransformD33_Pointer > const &"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetTransformQueue(self)


    def IsTransformQueueEmpty(self) -> "bool":
        """IsTransformQueueEmpty(itkMultiTransformD33 self) -> bool"""
        return _itkMultiTransformPython.itkMultiTransformD33_IsTransformQueueEmpty(self)


    def GetNumberOfTransforms(self) -> "unsigned long long":
        """GetNumberOfTransforms(itkMultiTransformD33 self) -> unsigned long long"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetNumberOfTransforms(self)


    def ClearTransformQueue(self) -> "void":
        """ClearTransformQueue(itkMultiTransformD33 self)"""
        return _itkMultiTransformPython.itkMultiTransformD33_ClearTransformQueue(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkMultiTransformD33 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkMultiTransformD33 self, itkArrayD update)
        """
        return _itkMultiTransformPython.itkMultiTransformD33_UpdateTransformParameters(self, update, factor)


    def GetInverse(self, inverse: 'itkMultiTransformD33') -> "bool":
        """GetInverse(itkMultiTransformD33 self, itkMultiTransformD33 inverse) -> bool"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetInverse(self, inverse)

    __swig_destroy__ = _itkMultiTransformPython.delete_itkMultiTransformD33

    def cast(obj: 'itkLightObject') -> "itkMultiTransformD33 *":
        """cast(itkLightObject obj) -> itkMultiTransformD33"""
        return _itkMultiTransformPython.itkMultiTransformD33_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMultiTransformD33 *":
        """GetPointer(itkMultiTransformD33 self) -> itkMultiTransformD33"""
        return _itkMultiTransformPython.itkMultiTransformD33_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMultiTransformD33

        Create a new object of the class itkMultiTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultiTransformD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultiTransformD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultiTransformD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMultiTransformD33.AddTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_AddTransform, None, itkMultiTransformD33)
itkMultiTransformD33.AppendTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_AppendTransform, None, itkMultiTransformD33)
itkMultiTransformD33.PrependTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_PrependTransform, None, itkMultiTransformD33)
itkMultiTransformD33.RemoveTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_RemoveTransform, None, itkMultiTransformD33)
itkMultiTransformD33.GetFrontTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetFrontTransform, None, itkMultiTransformD33)
itkMultiTransformD33.GetBackTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetBackTransform, None, itkMultiTransformD33)
itkMultiTransformD33.GetNthTransform = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetNthTransform, None, itkMultiTransformD33)
itkMultiTransformD33.GetNthTransformModifiablePointer = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetNthTransformModifiablePointer, None, itkMultiTransformD33)
itkMultiTransformD33.GetNthTransformConstPointer = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetNthTransformConstPointer, None, itkMultiTransformD33)
itkMultiTransformD33.GetTransformQueue = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetTransformQueue, None, itkMultiTransformD33)
itkMultiTransformD33.IsTransformQueueEmpty = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_IsTransformQueueEmpty, None, itkMultiTransformD33)
itkMultiTransformD33.GetNumberOfTransforms = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetNumberOfTransforms, None, itkMultiTransformD33)
itkMultiTransformD33.ClearTransformQueue = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_ClearTransformQueue, None, itkMultiTransformD33)
itkMultiTransformD33.UpdateTransformParameters = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_UpdateTransformParameters, None, itkMultiTransformD33)
itkMultiTransformD33.GetInverse = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetInverse, None, itkMultiTransformD33)
itkMultiTransformD33.GetPointer = new_instancemethod(_itkMultiTransformPython.itkMultiTransformD33_GetPointer, None, itkMultiTransformD33)
itkMultiTransformD33_swigregister = _itkMultiTransformPython.itkMultiTransformD33_swigregister
itkMultiTransformD33_swigregister(itkMultiTransformD33)

def itkMultiTransformD33_cast(obj: 'itkLightObject') -> "itkMultiTransformD33 *":
    """itkMultiTransformD33_cast(itkLightObject obj) -> itkMultiTransformD33"""
    return _itkMultiTransformPython.itkMultiTransformD33_cast(obj)



