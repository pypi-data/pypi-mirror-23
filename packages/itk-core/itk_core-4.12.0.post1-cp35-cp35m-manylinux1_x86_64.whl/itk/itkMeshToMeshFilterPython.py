# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMeshToMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkMeshToMeshFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkMeshToMeshFilterPython')
    _itkMeshToMeshFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMeshToMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMeshToMeshFilterPython
            return _itkMeshToMeshFilterPython
        try:
            _mod = imp.load_module('_itkMeshToMeshFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkMeshToMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMeshToMeshFilterPython
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


import itkMeshBasePython
import ITKCommonBasePython
import pyBasePython
import itkMapContainerPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkVectorContainerPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkBoundingBoxPython
import itkArrayPython
import itkPointSetPython
import itkMeshSourcePython

def itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_New():
  return itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.New()


def itkMeshToMeshFilterMF3STF33FMF3STF33FF_New():
  return itkMeshToMeshFilterMF3STF33FMF3STF33FF.New()


def itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_New():
  return itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.New()


def itkMeshToMeshFilterMF2STF22FMF2STF22FF_New():
  return itkMeshToMeshFilterMF2STF22FMF2STF22FF.New()

class itkMeshToMeshFilterMF2DTF22FMF2DTF22FF(itkMeshSourcePython.itkMeshSourceMF2DTF22FF):
    """Proxy of C++ itkMeshToMeshFilterMF2DTF22FMF2DTF22FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Pointer":
        """Clone(itkMeshToMeshFilterMF2DTF22FMF2DTF22FF self) -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Clone(self)


    def SetInput(self, input: 'itkMeshF2DTF22FF') -> "void":
        """SetInput(itkMeshToMeshFilterMF2DTF22FMF2DTF22FF self, itkMeshF2DTF22FF input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshF2DTF22FF const *":
        """
        GetInput(itkMeshToMeshFilterMF2DTF22FMF2DTF22FF self) -> itkMeshF2DTF22FF
        GetInput(itkMeshToMeshFilterMF2DTF22FMF2DTF22FF self, unsigned int idx) -> itkMeshF2DTF22FF
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF2DTF22FMF2DTF22FF

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF2DTF22FMF2DTF22FF *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMeshToMeshFilterMF2DTF22FMF2DTF22FF *":
        """GetPointer(itkMeshToMeshFilterMF2DTF22FMF2DTF22FF self) -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF

        Create a new object of the class itkMeshToMeshFilterMF2DTF22FMF2DTF22FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Clone, None, itkMeshToMeshFilterMF2DTF22FMF2DTF22FF)
itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_SetInput, None, itkMeshToMeshFilterMF2DTF22FMF2DTF22FF)
itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_GetInput, None, itkMeshToMeshFilterMF2DTF22FMF2DTF22FF)
itkMeshToMeshFilterMF2DTF22FMF2DTF22FF.GetPointer = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_GetPointer, None, itkMeshToMeshFilterMF2DTF22FMF2DTF22FF)
itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_swigregister
itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_swigregister(itkMeshToMeshFilterMF2DTF22FMF2DTF22FF)

def itkMeshToMeshFilterMF2DTF22FMF2DTF22FF___New_orig__() -> "itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Pointer":
    """itkMeshToMeshFilterMF2DTF22FMF2DTF22FF___New_orig__() -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF___New_orig__()

def itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF2DTF22FMF2DTF22FF *":
    """itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_cast(itkLightObject obj) -> itkMeshToMeshFilterMF2DTF22FMF2DTF22FF"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2DTF22FMF2DTF22FF_cast(obj)

class itkMeshToMeshFilterMF2STF22FMF2STF22FF(itkMeshSourcePython.itkMeshSourceMF2STF22FF):
    """Proxy of C++ itkMeshToMeshFilterMF2STF22FMF2STF22FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMF2STF22FMF2STF22FF_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMF2STF22FMF2STF22FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMF2STF22FMF2STF22FF_Pointer":
        """Clone(itkMeshToMeshFilterMF2STF22FMF2STF22FF self) -> itkMeshToMeshFilterMF2STF22FMF2STF22FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_Clone(self)


    def SetInput(self, input: 'itkMeshF2STF22FF') -> "void":
        """SetInput(itkMeshToMeshFilterMF2STF22FMF2STF22FF self, itkMeshF2STF22FF input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshF2STF22FF const *":
        """
        GetInput(itkMeshToMeshFilterMF2STF22FMF2STF22FF self) -> itkMeshF2STF22FF
        GetInput(itkMeshToMeshFilterMF2STF22FMF2STF22FF self, unsigned int idx) -> itkMeshF2STF22FF
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF2STF22FMF2STF22FF

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF2STF22FMF2STF22FF *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMF2STF22FMF2STF22FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMeshToMeshFilterMF2STF22FMF2STF22FF *":
        """GetPointer(itkMeshToMeshFilterMF2STF22FMF2STF22FF self) -> itkMeshToMeshFilterMF2STF22FMF2STF22FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF2STF22FMF2STF22FF

        Create a new object of the class itkMeshToMeshFilterMF2STF22FMF2STF22FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF2STF22FMF2STF22FF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF2STF22FMF2STF22FF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMF2STF22FMF2STF22FF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMF2STF22FMF2STF22FF.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_Clone, None, itkMeshToMeshFilterMF2STF22FMF2STF22FF)
itkMeshToMeshFilterMF2STF22FMF2STF22FF.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_SetInput, None, itkMeshToMeshFilterMF2STF22FMF2STF22FF)
itkMeshToMeshFilterMF2STF22FMF2STF22FF.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_GetInput, None, itkMeshToMeshFilterMF2STF22FMF2STF22FF)
itkMeshToMeshFilterMF2STF22FMF2STF22FF.GetPointer = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_GetPointer, None, itkMeshToMeshFilterMF2STF22FMF2STF22FF)
itkMeshToMeshFilterMF2STF22FMF2STF22FF_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_swigregister
itkMeshToMeshFilterMF2STF22FMF2STF22FF_swigregister(itkMeshToMeshFilterMF2STF22FMF2STF22FF)

def itkMeshToMeshFilterMF2STF22FMF2STF22FF___New_orig__() -> "itkMeshToMeshFilterMF2STF22FMF2STF22FF_Pointer":
    """itkMeshToMeshFilterMF2STF22FMF2STF22FF___New_orig__() -> itkMeshToMeshFilterMF2STF22FMF2STF22FF_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF___New_orig__()

def itkMeshToMeshFilterMF2STF22FMF2STF22FF_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF2STF22FMF2STF22FF *":
    """itkMeshToMeshFilterMF2STF22FMF2STF22FF_cast(itkLightObject obj) -> itkMeshToMeshFilterMF2STF22FMF2STF22FF"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2STF22FMF2STF22FF_cast(obj)

class itkMeshToMeshFilterMF3DTF33FMF3DTF33FF(itkMeshSourcePython.itkMeshSourceMF3DTF33FF):
    """Proxy of C++ itkMeshToMeshFilterMF3DTF33FMF3DTF33FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Pointer":
        """Clone(itkMeshToMeshFilterMF3DTF33FMF3DTF33FF self) -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Clone(self)


    def SetInput(self, input: 'itkMeshF3DTF33FF') -> "void":
        """SetInput(itkMeshToMeshFilterMF3DTF33FMF3DTF33FF self, itkMeshF3DTF33FF input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshF3DTF33FF const *":
        """
        GetInput(itkMeshToMeshFilterMF3DTF33FMF3DTF33FF self) -> itkMeshF3DTF33FF
        GetInput(itkMeshToMeshFilterMF3DTF33FMF3DTF33FF self, unsigned int idx) -> itkMeshF3DTF33FF
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF3DTF33FMF3DTF33FF

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF3DTF33FMF3DTF33FF *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMeshToMeshFilterMF3DTF33FMF3DTF33FF *":
        """GetPointer(itkMeshToMeshFilterMF3DTF33FMF3DTF33FF self) -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF

        Create a new object of the class itkMeshToMeshFilterMF3DTF33FMF3DTF33FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Clone, None, itkMeshToMeshFilterMF3DTF33FMF3DTF33FF)
itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_SetInput, None, itkMeshToMeshFilterMF3DTF33FMF3DTF33FF)
itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_GetInput, None, itkMeshToMeshFilterMF3DTF33FMF3DTF33FF)
itkMeshToMeshFilterMF3DTF33FMF3DTF33FF.GetPointer = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_GetPointer, None, itkMeshToMeshFilterMF3DTF33FMF3DTF33FF)
itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_swigregister
itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_swigregister(itkMeshToMeshFilterMF3DTF33FMF3DTF33FF)

def itkMeshToMeshFilterMF3DTF33FMF3DTF33FF___New_orig__() -> "itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Pointer":
    """itkMeshToMeshFilterMF3DTF33FMF3DTF33FF___New_orig__() -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF___New_orig__()

def itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF3DTF33FMF3DTF33FF *":
    """itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_cast(itkLightObject obj) -> itkMeshToMeshFilterMF3DTF33FMF3DTF33FF"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3DTF33FMF3DTF33FF_cast(obj)

class itkMeshToMeshFilterMF3STF33FMF3STF33FF(itkMeshSourcePython.itkMeshSourceMF3STF33FF):
    """Proxy of C++ itkMeshToMeshFilterMF3STF33FMF3STF33FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMF3STF33FMF3STF33FF_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMF3STF33FMF3STF33FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMF3STF33FMF3STF33FF_Pointer":
        """Clone(itkMeshToMeshFilterMF3STF33FMF3STF33FF self) -> itkMeshToMeshFilterMF3STF33FMF3STF33FF_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_Clone(self)


    def SetInput(self, input: 'itkMeshF3STF33FF') -> "void":
        """SetInput(itkMeshToMeshFilterMF3STF33FMF3STF33FF self, itkMeshF3STF33FF input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshF3STF33FF const *":
        """
        GetInput(itkMeshToMeshFilterMF3STF33FMF3STF33FF self) -> itkMeshF3STF33FF
        GetInput(itkMeshToMeshFilterMF3STF33FMF3STF33FF self, unsigned int idx) -> itkMeshF3STF33FF
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF3STF33FMF3STF33FF

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF3STF33FMF3STF33FF *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMF3STF33FMF3STF33FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkMeshToMeshFilterMF3STF33FMF3STF33FF *":
        """GetPointer(itkMeshToMeshFilterMF3STF33FMF3STF33FF self) -> itkMeshToMeshFilterMF3STF33FMF3STF33FF"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF3STF33FMF3STF33FF

        Create a new object of the class itkMeshToMeshFilterMF3STF33FMF3STF33FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF3STF33FMF3STF33FF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF3STF33FMF3STF33FF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMF3STF33FMF3STF33FF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMF3STF33FMF3STF33FF.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_Clone, None, itkMeshToMeshFilterMF3STF33FMF3STF33FF)
itkMeshToMeshFilterMF3STF33FMF3STF33FF.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_SetInput, None, itkMeshToMeshFilterMF3STF33FMF3STF33FF)
itkMeshToMeshFilterMF3STF33FMF3STF33FF.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_GetInput, None, itkMeshToMeshFilterMF3STF33FMF3STF33FF)
itkMeshToMeshFilterMF3STF33FMF3STF33FF.GetPointer = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_GetPointer, None, itkMeshToMeshFilterMF3STF33FMF3STF33FF)
itkMeshToMeshFilterMF3STF33FMF3STF33FF_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_swigregister
itkMeshToMeshFilterMF3STF33FMF3STF33FF_swigregister(itkMeshToMeshFilterMF3STF33FMF3STF33FF)

def itkMeshToMeshFilterMF3STF33FMF3STF33FF___New_orig__() -> "itkMeshToMeshFilterMF3STF33FMF3STF33FF_Pointer":
    """itkMeshToMeshFilterMF3STF33FMF3STF33FF___New_orig__() -> itkMeshToMeshFilterMF3STF33FMF3STF33FF_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF___New_orig__()

def itkMeshToMeshFilterMF3STF33FMF3STF33FF_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF3STF33FMF3STF33FF *":
    """itkMeshToMeshFilterMF3STF33FMF3STF33FF_cast(itkLightObject obj) -> itkMeshToMeshFilterMF3STF33FMF3STF33FF"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3STF33FMF3STF33FF_cast(obj)



