# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNiftiImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNiftiImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNiftiImageIOPython')
    _itkNiftiImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNiftiImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkNiftiImageIOPython
            return _itkNiftiImageIOPython
        try:
            _mod = imp.load_module('_itkNiftiImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNiftiImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNiftiImageIOPython
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

def itkNiftiImageIOFactory_New():
  return itkNiftiImageIOFactory.New()


def itkNiftiImageIO_New():
  return itkNiftiImageIO.New()

class itkNiftiImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkNiftiImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNiftiImageIO_Pointer":
        """__New_orig__() -> itkNiftiImageIO_Pointer"""
        return _itkNiftiImageIOPython.itkNiftiImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNiftiImageIO_Pointer":
        """Clone(itkNiftiImageIO self) -> itkNiftiImageIO_Pointer"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_Clone(self)


    def SetLegacyAnalyze75Mode(self, _arg: 'bool const') -> "void":
        """SetLegacyAnalyze75Mode(itkNiftiImageIO self, bool const _arg)"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_SetLegacyAnalyze75Mode(self, _arg)


    def GetLegacyAnalyze75Mode(self) -> "bool":
        """GetLegacyAnalyze75Mode(itkNiftiImageIO self) -> bool"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_GetLegacyAnalyze75Mode(self)

    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIO

    def cast(obj: 'itkLightObject') -> "itkNiftiImageIO *":
        """cast(itkLightObject obj) -> itkNiftiImageIO"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNiftiImageIO *":
        """GetPointer(itkNiftiImageIO self) -> itkNiftiImageIO"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNiftiImageIO

        Create a new object of the class itkNiftiImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNiftiImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNiftiImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNiftiImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNiftiImageIO.Clone = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_Clone, None, itkNiftiImageIO)
itkNiftiImageIO.SetLegacyAnalyze75Mode = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_SetLegacyAnalyze75Mode, None, itkNiftiImageIO)
itkNiftiImageIO.GetLegacyAnalyze75Mode = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_GetLegacyAnalyze75Mode, None, itkNiftiImageIO)
itkNiftiImageIO.GetPointer = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_GetPointer, None, itkNiftiImageIO)
itkNiftiImageIO_swigregister = _itkNiftiImageIOPython.itkNiftiImageIO_swigregister
itkNiftiImageIO_swigregister(itkNiftiImageIO)

def itkNiftiImageIO___New_orig__() -> "itkNiftiImageIO_Pointer":
    """itkNiftiImageIO___New_orig__() -> itkNiftiImageIO_Pointer"""
    return _itkNiftiImageIOPython.itkNiftiImageIO___New_orig__()

def itkNiftiImageIO_cast(obj: 'itkLightObject') -> "itkNiftiImageIO *":
    """itkNiftiImageIO_cast(itkLightObject obj) -> itkNiftiImageIO"""
    return _itkNiftiImageIOPython.itkNiftiImageIO_cast(obj)

class itkNiftiImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """Proxy of C++ itkNiftiImageIOFactory class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNiftiImageIOFactory_Pointer":
        """__New_orig__() -> itkNiftiImageIOFactory_Pointer"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIOFactory

    def cast(obj: 'itkLightObject') -> "itkNiftiImageIOFactory *":
        """cast(itkLightObject obj) -> itkNiftiImageIOFactory"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkNiftiImageIOFactory *":
        """GetPointer(itkNiftiImageIOFactory self) -> itkNiftiImageIOFactory"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNiftiImageIOFactory

        Create a new object of the class itkNiftiImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNiftiImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNiftiImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNiftiImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNiftiImageIOFactory.GetPointer = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIOFactory_GetPointer, None, itkNiftiImageIOFactory)
itkNiftiImageIOFactory_swigregister = _itkNiftiImageIOPython.itkNiftiImageIOFactory_swigregister
itkNiftiImageIOFactory_swigregister(itkNiftiImageIOFactory)

def itkNiftiImageIOFactory___New_orig__() -> "itkNiftiImageIOFactory_Pointer":
    """itkNiftiImageIOFactory___New_orig__() -> itkNiftiImageIOFactory_Pointer"""
    return _itkNiftiImageIOPython.itkNiftiImageIOFactory___New_orig__()

def itkNiftiImageIOFactory_RegisterOneFactory() -> "void":
    """itkNiftiImageIOFactory_RegisterOneFactory()"""
    return _itkNiftiImageIOPython.itkNiftiImageIOFactory_RegisterOneFactory()

def itkNiftiImageIOFactory_cast(obj: 'itkLightObject') -> "itkNiftiImageIOFactory *":
    """itkNiftiImageIOFactory_cast(itkLightObject obj) -> itkNiftiImageIOFactory"""
    return _itkNiftiImageIOPython.itkNiftiImageIOFactory_cast(obj)



