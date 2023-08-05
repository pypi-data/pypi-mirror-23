# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBMPImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkBMPImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkBMPImageIOPython')
    _itkBMPImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBMPImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkBMPImageIOPython
            return _itkBMPImageIOPython
        try:
            _mod = imp.load_module('_itkBMPImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkBMPImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBMPImageIOPython
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
import itkRGBPixelPython
import itkFixedArrayPython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython

def itkBMPImageIOFactory_New():
  return itkBMPImageIOFactory.New()


def itkBMPImageIO_New():
  return itkBMPImageIO.New()

class itkBMPImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkBMPImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBMPImageIO_Pointer"""
        return _itkBMPImageIOPython.itkBMPImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkBMPImageIO self) -> itkBMPImageIO_Pointer"""
        return _itkBMPImageIOPython.itkBMPImageIO_Clone(self)


    def GetFileLowerLeft(self):
        """GetFileLowerLeft(itkBMPImageIO self) -> bool"""
        return _itkBMPImageIOPython.itkBMPImageIO_GetFileLowerLeft(self)


    def GetBMPCompression(self):
        """GetBMPCompression(itkBMPImageIO self) -> long"""
        return _itkBMPImageIOPython.itkBMPImageIO_GetBMPCompression(self)


    def GetColorPalette(self):
        """GetColorPalette(itkBMPImageIO self) -> std::vector< itkRGBPixelUC,std::allocator< itkRGBPixelUC > > const &"""
        return _itkBMPImageIOPython.itkBMPImageIO_GetColorPalette(self)


    def __init__(self):
        """__init__(itkBMPImageIO self) -> itkBMPImageIO"""
        _itkBMPImageIOPython.itkBMPImageIO_swiginit(self, _itkBMPImageIOPython.new_itkBMPImageIO())

    def PrintSelf(self, os, indent):
        """PrintSelf(itkBMPImageIO self, ostream os, itkIndent indent)"""
        return _itkBMPImageIOPython.itkBMPImageIO_PrintSelf(self, os, indent)

    __swig_destroy__ = _itkBMPImageIOPython.delete_itkBMPImageIO

    def cast(obj):
        """cast(itkLightObject obj) -> itkBMPImageIO"""
        return _itkBMPImageIOPython.itkBMPImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBMPImageIO self) -> itkBMPImageIO"""
        return _itkBMPImageIOPython.itkBMPImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBMPImageIO

        Create a new object of the class itkBMPImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBMPImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBMPImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBMPImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBMPImageIO.Clone = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_Clone, None, itkBMPImageIO)
itkBMPImageIO.GetFileLowerLeft = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetFileLowerLeft, None, itkBMPImageIO)
itkBMPImageIO.GetBMPCompression = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetBMPCompression, None, itkBMPImageIO)
itkBMPImageIO.GetColorPalette = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetColorPalette, None, itkBMPImageIO)
itkBMPImageIO.PrintSelf = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_PrintSelf, None, itkBMPImageIO)
itkBMPImageIO.GetPointer = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetPointer, None, itkBMPImageIO)
itkBMPImageIO_swigregister = _itkBMPImageIOPython.itkBMPImageIO_swigregister
itkBMPImageIO_swigregister(itkBMPImageIO)

def itkBMPImageIO___New_orig__():
    """itkBMPImageIO___New_orig__() -> itkBMPImageIO_Pointer"""
    return _itkBMPImageIOPython.itkBMPImageIO___New_orig__()

def itkBMPImageIO_cast(obj):
    """itkBMPImageIO_cast(itkLightObject obj) -> itkBMPImageIO"""
    return _itkBMPImageIOPython.itkBMPImageIO_cast(obj)

class itkBMPImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """Proxy of C++ itkBMPImageIOFactory class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkBMPImageIOFactory_Pointer"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory():
        """RegisterOneFactory()"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkBMPImageIOPython.delete_itkBMPImageIOFactory

    def cast(obj):
        """cast(itkLightObject obj) -> itkBMPImageIOFactory"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkBMPImageIOFactory self) -> itkBMPImageIOFactory"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkBMPImageIOFactory

        Create a new object of the class itkBMPImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBMPImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBMPImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBMPImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBMPImageIOFactory.GetPointer = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIOFactory_GetPointer, None, itkBMPImageIOFactory)
itkBMPImageIOFactory_swigregister = _itkBMPImageIOPython.itkBMPImageIOFactory_swigregister
itkBMPImageIOFactory_swigregister(itkBMPImageIOFactory)

def itkBMPImageIOFactory___New_orig__():
    """itkBMPImageIOFactory___New_orig__() -> itkBMPImageIOFactory_Pointer"""
    return _itkBMPImageIOPython.itkBMPImageIOFactory___New_orig__()

def itkBMPImageIOFactory_RegisterOneFactory():
    """itkBMPImageIOFactory_RegisterOneFactory()"""
    return _itkBMPImageIOPython.itkBMPImageIOFactory_RegisterOneFactory()

def itkBMPImageIOFactory_cast(obj):
    """itkBMPImageIOFactory_cast(itkLightObject obj) -> itkBMPImageIOFactory"""
    return _itkBMPImageIOPython.itkBMPImageIOFactory_cast(obj)



