# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGiplImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkGiplImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkGiplImageIOPython')
    _itkGiplImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGiplImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkGiplImageIOPython
            return _itkGiplImageIOPython
        try:
            _mod = imp.load_module('_itkGiplImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkGiplImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGiplImageIOPython
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

def itkGiplImageIOFactory_New():
  return itkGiplImageIOFactory.New()


def itkGiplImageIO_New():
  return itkGiplImageIO.New()

class itkGiplImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkGiplImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkGiplImageIO_Pointer"""
        return _itkGiplImageIOPython.itkGiplImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkGiplImageIO self) -> itkGiplImageIO_Pointer"""
        return _itkGiplImageIOPython.itkGiplImageIO_Clone(self)


    def __init__(self):
        """__init__(itkGiplImageIO self) -> itkGiplImageIO"""
        _itkGiplImageIOPython.itkGiplImageIO_swiginit(self, _itkGiplImageIOPython.new_itkGiplImageIO())

    def PrintSelf(self, os, indent):
        """PrintSelf(itkGiplImageIO self, ostream os, itkIndent indent)"""
        return _itkGiplImageIOPython.itkGiplImageIO_PrintSelf(self, os, indent)

    __swig_destroy__ = _itkGiplImageIOPython.delete_itkGiplImageIO

    def cast(obj):
        """cast(itkLightObject obj) -> itkGiplImageIO"""
        return _itkGiplImageIOPython.itkGiplImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkGiplImageIO self) -> itkGiplImageIO"""
        return _itkGiplImageIOPython.itkGiplImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGiplImageIO

        Create a new object of the class itkGiplImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGiplImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGiplImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGiplImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGiplImageIO.Clone = new_instancemethod(_itkGiplImageIOPython.itkGiplImageIO_Clone, None, itkGiplImageIO)
itkGiplImageIO.PrintSelf = new_instancemethod(_itkGiplImageIOPython.itkGiplImageIO_PrintSelf, None, itkGiplImageIO)
itkGiplImageIO.GetPointer = new_instancemethod(_itkGiplImageIOPython.itkGiplImageIO_GetPointer, None, itkGiplImageIO)
itkGiplImageIO_swigregister = _itkGiplImageIOPython.itkGiplImageIO_swigregister
itkGiplImageIO_swigregister(itkGiplImageIO)

def itkGiplImageIO___New_orig__():
    """itkGiplImageIO___New_orig__() -> itkGiplImageIO_Pointer"""
    return _itkGiplImageIOPython.itkGiplImageIO___New_orig__()

def itkGiplImageIO_cast(obj):
    """itkGiplImageIO_cast(itkLightObject obj) -> itkGiplImageIO"""
    return _itkGiplImageIOPython.itkGiplImageIO_cast(obj)

class itkGiplImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """Proxy of C++ itkGiplImageIOFactory class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkGiplImageIOFactory_Pointer"""
        return _itkGiplImageIOPython.itkGiplImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory():
        """RegisterOneFactory()"""
        return _itkGiplImageIOPython.itkGiplImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkGiplImageIOPython.delete_itkGiplImageIOFactory

    def cast(obj):
        """cast(itkLightObject obj) -> itkGiplImageIOFactory"""
        return _itkGiplImageIOPython.itkGiplImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkGiplImageIOFactory self) -> itkGiplImageIOFactory"""
        return _itkGiplImageIOPython.itkGiplImageIOFactory_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkGiplImageIOFactory

        Create a new object of the class itkGiplImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGiplImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGiplImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGiplImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGiplImageIOFactory.GetPointer = new_instancemethod(_itkGiplImageIOPython.itkGiplImageIOFactory_GetPointer, None, itkGiplImageIOFactory)
itkGiplImageIOFactory_swigregister = _itkGiplImageIOPython.itkGiplImageIOFactory_swigregister
itkGiplImageIOFactory_swigregister(itkGiplImageIOFactory)

def itkGiplImageIOFactory___New_orig__():
    """itkGiplImageIOFactory___New_orig__() -> itkGiplImageIOFactory_Pointer"""
    return _itkGiplImageIOPython.itkGiplImageIOFactory___New_orig__()

def itkGiplImageIOFactory_RegisterOneFactory():
    """itkGiplImageIOFactory_RegisterOneFactory()"""
    return _itkGiplImageIOPython.itkGiplImageIOFactory_RegisterOneFactory()

def itkGiplImageIOFactory_cast(obj):
    """itkGiplImageIOFactory_cast(itkLightObject obj) -> itkGiplImageIOFactory"""
    return _itkGiplImageIOPython.itkGiplImageIOFactory_cast(obj)



