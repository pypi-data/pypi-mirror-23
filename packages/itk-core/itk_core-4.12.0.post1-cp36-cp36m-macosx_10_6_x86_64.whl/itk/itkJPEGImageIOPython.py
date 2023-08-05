# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkJPEGImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkJPEGImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkJPEGImageIOPython')
    _itkJPEGImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkJPEGImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkJPEGImageIOPython
            return _itkJPEGImageIOPython
        try:
            _mod = imp.load_module('_itkJPEGImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkJPEGImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkJPEGImageIOPython
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


import ITKCommonBasePython
import pyBasePython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython

def itkJPEGImageIOFactory_New():
  return itkJPEGImageIOFactory.New()


def itkJPEGImageIO_New():
  return itkJPEGImageIO.New()

class itkJPEGImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkJPEGImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJPEGImageIO_Pointer":
        """__New_orig__() -> itkJPEGImageIO_Pointer"""
        return _itkJPEGImageIOPython.itkJPEGImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkJPEGImageIO_Pointer":
        """Clone(itkJPEGImageIO self) -> itkJPEGImageIO_Pointer"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_Clone(self)


    def SetQuality(self, _arg: 'int const') -> "void":
        """SetQuality(itkJPEGImageIO self, int const _arg)"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_SetQuality(self, _arg)


    def GetQuality(self) -> "int":
        """GetQuality(itkJPEGImageIO self) -> int"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_GetQuality(self)


    def SetProgressive(self, _arg: 'bool const') -> "void":
        """SetProgressive(itkJPEGImageIO self, bool const _arg)"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_SetProgressive(self, _arg)


    def GetProgressive(self) -> "bool":
        """GetProgressive(itkJPEGImageIO self) -> bool"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_GetProgressive(self)


    def ReadVolume(self, buffer: 'void *') -> "void":
        """ReadVolume(itkJPEGImageIO self, void * buffer)"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_ReadVolume(self, buffer)

    __swig_destroy__ = _itkJPEGImageIOPython.delete_itkJPEGImageIO

    def cast(obj: 'itkLightObject') -> "itkJPEGImageIO *":
        """cast(itkLightObject obj) -> itkJPEGImageIO"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkJPEGImageIO *":
        """GetPointer(itkJPEGImageIO self) -> itkJPEGImageIO"""
        return _itkJPEGImageIOPython.itkJPEGImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkJPEGImageIO

        Create a new object of the class itkJPEGImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJPEGImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJPEGImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJPEGImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJPEGImageIO.Clone = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_Clone, None, itkJPEGImageIO)
itkJPEGImageIO.SetQuality = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_SetQuality, None, itkJPEGImageIO)
itkJPEGImageIO.GetQuality = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_GetQuality, None, itkJPEGImageIO)
itkJPEGImageIO.SetProgressive = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_SetProgressive, None, itkJPEGImageIO)
itkJPEGImageIO.GetProgressive = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_GetProgressive, None, itkJPEGImageIO)
itkJPEGImageIO.ReadVolume = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_ReadVolume, None, itkJPEGImageIO)
itkJPEGImageIO.GetPointer = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIO_GetPointer, None, itkJPEGImageIO)
itkJPEGImageIO_swigregister = _itkJPEGImageIOPython.itkJPEGImageIO_swigregister
itkJPEGImageIO_swigregister(itkJPEGImageIO)

def itkJPEGImageIO___New_orig__() -> "itkJPEGImageIO_Pointer":
    """itkJPEGImageIO___New_orig__() -> itkJPEGImageIO_Pointer"""
    return _itkJPEGImageIOPython.itkJPEGImageIO___New_orig__()

def itkJPEGImageIO_cast(obj: 'itkLightObject') -> "itkJPEGImageIO *":
    """itkJPEGImageIO_cast(itkLightObject obj) -> itkJPEGImageIO"""
    return _itkJPEGImageIOPython.itkJPEGImageIO_cast(obj)

class itkJPEGImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """Proxy of C++ itkJPEGImageIOFactory class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJPEGImageIOFactory_Pointer":
        """__New_orig__() -> itkJPEGImageIOFactory_Pointer"""
        return _itkJPEGImageIOPython.itkJPEGImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def FactoryNew() -> "itkJPEGImageIOFactory *":
        """FactoryNew() -> itkJPEGImageIOFactory"""
        return _itkJPEGImageIOPython.itkJPEGImageIOFactory_FactoryNew()

    FactoryNew = staticmethod(FactoryNew)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkJPEGImageIOPython.itkJPEGImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkJPEGImageIOPython.delete_itkJPEGImageIOFactory

    def cast(obj: 'itkLightObject') -> "itkJPEGImageIOFactory *":
        """cast(itkLightObject obj) -> itkJPEGImageIOFactory"""
        return _itkJPEGImageIOPython.itkJPEGImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkJPEGImageIOFactory *":
        """GetPointer(itkJPEGImageIOFactory self) -> itkJPEGImageIOFactory"""
        return _itkJPEGImageIOPython.itkJPEGImageIOFactory_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkJPEGImageIOFactory

        Create a new object of the class itkJPEGImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJPEGImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJPEGImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJPEGImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJPEGImageIOFactory.GetPointer = new_instancemethod(_itkJPEGImageIOPython.itkJPEGImageIOFactory_GetPointer, None, itkJPEGImageIOFactory)
itkJPEGImageIOFactory_swigregister = _itkJPEGImageIOPython.itkJPEGImageIOFactory_swigregister
itkJPEGImageIOFactory_swigregister(itkJPEGImageIOFactory)

def itkJPEGImageIOFactory___New_orig__() -> "itkJPEGImageIOFactory_Pointer":
    """itkJPEGImageIOFactory___New_orig__() -> itkJPEGImageIOFactory_Pointer"""
    return _itkJPEGImageIOPython.itkJPEGImageIOFactory___New_orig__()

def itkJPEGImageIOFactory_FactoryNew() -> "itkJPEGImageIOFactory *":
    """itkJPEGImageIOFactory_FactoryNew() -> itkJPEGImageIOFactory"""
    return _itkJPEGImageIOPython.itkJPEGImageIOFactory_FactoryNew()

def itkJPEGImageIOFactory_RegisterOneFactory() -> "void":
    """itkJPEGImageIOFactory_RegisterOneFactory()"""
    return _itkJPEGImageIOPython.itkJPEGImageIOFactory_RegisterOneFactory()

def itkJPEGImageIOFactory_cast(obj: 'itkLightObject') -> "itkJPEGImageIOFactory *":
    """itkJPEGImageIOFactory_cast(itkLightObject obj) -> itkJPEGImageIOFactory"""
    return _itkJPEGImageIOPython.itkJPEGImageIOFactory_cast(obj)



