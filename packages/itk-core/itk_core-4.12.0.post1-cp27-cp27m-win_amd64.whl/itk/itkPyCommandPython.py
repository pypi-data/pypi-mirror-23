# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPyCommandPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkPyCommandPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkPyCommandPython')
    _itkPyCommandPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPyCommandPython', [dirname(__file__)])
        except ImportError:
            import _itkPyCommandPython
            return _itkPyCommandPython
        try:
            _mod = imp.load_module('_itkPyCommandPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkPyCommandPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPyCommandPython
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

def itkPyCommand_New():
  return itkPyCommand.New()

class itkPyCommand(ITKCommonBasePython.itkCommand):
    """Proxy of C++ itkPyCommand class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkPyCommand_Pointer"""
        return _itkPyCommandPython.itkPyCommand___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkPyCommand self) -> itkPyCommand_Pointer"""
        return _itkPyCommandPython.itkPyCommand_Clone(self)


    def SetCommandCallable(self, obj):
        """SetCommandCallable(itkPyCommand self, PyObject * obj)"""
        return _itkPyCommandPython.itkPyCommand_SetCommandCallable(self, obj)


    def GetCommandCallable(self):
        """GetCommandCallable(itkPyCommand self) -> PyObject *"""
        return _itkPyCommandPython.itkPyCommand_GetCommandCallable(self)


    def Execute(self, *args):
        """
        Execute(itkPyCommand self, itkObject arg0, itkEventObject arg1)
        Execute(itkPyCommand self, itkObject arg0, itkEventObject arg1)
        """
        return _itkPyCommandPython.itkPyCommand_Execute(self, *args)

    __swig_destroy__ = _itkPyCommandPython.delete_itkPyCommand

    def cast(obj):
        """cast(itkLightObject obj) -> itkPyCommand"""
        return _itkPyCommandPython.itkPyCommand_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkPyCommand self) -> itkPyCommand"""
        return _itkPyCommandPython.itkPyCommand_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkPyCommand

        Create a new object of the class itkPyCommand and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyCommand.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyCommand.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyCommand.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyCommand.Clone = new_instancemethod(_itkPyCommandPython.itkPyCommand_Clone, None, itkPyCommand)
itkPyCommand.SetCommandCallable = new_instancemethod(_itkPyCommandPython.itkPyCommand_SetCommandCallable, None, itkPyCommand)
itkPyCommand.GetCommandCallable = new_instancemethod(_itkPyCommandPython.itkPyCommand_GetCommandCallable, None, itkPyCommand)
itkPyCommand.Execute = new_instancemethod(_itkPyCommandPython.itkPyCommand_Execute, None, itkPyCommand)
itkPyCommand.GetPointer = new_instancemethod(_itkPyCommandPython.itkPyCommand_GetPointer, None, itkPyCommand)
itkPyCommand_swigregister = _itkPyCommandPython.itkPyCommand_swigregister
itkPyCommand_swigregister(itkPyCommand)

def itkPyCommand___New_orig__():
    """itkPyCommand___New_orig__() -> itkPyCommand_Pointer"""
    return _itkPyCommandPython.itkPyCommand___New_orig__()

def itkPyCommand_cast(obj):
    """itkPyCommand_cast(itkLightObject obj) -> itkPyCommand"""
    return _itkPyCommandPython.itkPyCommand_cast(obj)



