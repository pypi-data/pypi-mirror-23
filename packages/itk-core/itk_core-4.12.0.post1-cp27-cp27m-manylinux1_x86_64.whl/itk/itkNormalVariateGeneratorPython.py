# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNormalVariateGeneratorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkNormalVariateGeneratorPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkNormalVariateGeneratorPython')
    _itkNormalVariateGeneratorPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNormalVariateGeneratorPython', [dirname(__file__)])
        except ImportError:
            import _itkNormalVariateGeneratorPython
            return _itkNormalVariateGeneratorPython
        try:
            _mod = imp.load_module('_itkNormalVariateGeneratorPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkNormalVariateGeneratorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNormalVariateGeneratorPython
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

def itkNormalVariateGenerator_New():
  return itkNormalVariateGenerator.New()

class itkNormalVariateGenerator(ITKCommonBasePython.itkRandomVariateGeneratorBase):
    """Proxy of C++ itkNormalVariateGenerator class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkNormalVariateGenerator_Pointer"""
        return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkNormalVariateGenerator self) -> itkNormalVariateGenerator_Pointer"""
        return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator_Clone(self)


    def Initialize(self, randomSeed):
        """Initialize(itkNormalVariateGenerator self, int randomSeed)"""
        return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator_Initialize(self, randomSeed)

    __swig_destroy__ = _itkNormalVariateGeneratorPython.delete_itkNormalVariateGenerator

    def cast(obj):
        """cast(itkLightObject obj) -> itkNormalVariateGenerator"""
        return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkNormalVariateGenerator self) -> itkNormalVariateGenerator"""
        return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkNormalVariateGenerator

        Create a new object of the class itkNormalVariateGenerator and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNormalVariateGenerator.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNormalVariateGenerator.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNormalVariateGenerator.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNormalVariateGenerator.Clone = new_instancemethod(_itkNormalVariateGeneratorPython.itkNormalVariateGenerator_Clone, None, itkNormalVariateGenerator)
itkNormalVariateGenerator.Initialize = new_instancemethod(_itkNormalVariateGeneratorPython.itkNormalVariateGenerator_Initialize, None, itkNormalVariateGenerator)
itkNormalVariateGenerator.GetPointer = new_instancemethod(_itkNormalVariateGeneratorPython.itkNormalVariateGenerator_GetPointer, None, itkNormalVariateGenerator)
itkNormalVariateGenerator_swigregister = _itkNormalVariateGeneratorPython.itkNormalVariateGenerator_swigregister
itkNormalVariateGenerator_swigregister(itkNormalVariateGenerator)

def itkNormalVariateGenerator___New_orig__():
    """itkNormalVariateGenerator___New_orig__() -> itkNormalVariateGenerator_Pointer"""
    return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator___New_orig__()

def itkNormalVariateGenerator_cast(obj):
    """itkNormalVariateGenerator_cast(itkLightObject obj) -> itkNormalVariateGenerator"""
    return _itkNormalVariateGeneratorPython.itkNormalVariateGenerator_cast(obj)



