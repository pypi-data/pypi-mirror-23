# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _vnl_unary_functionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_vnl_unary_functionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_vnl_unary_functionPython')
    _vnl_unary_functionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vnl_unary_functionPython', [dirname(__file__)])
        except ImportError:
            import _vnl_unary_functionPython
            return _vnl_unary_functionPython
        try:
            _mod = imp.load_module('_vnl_unary_functionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _vnl_unary_functionPython = swig_import_helper()
    del swig_import_helper
else:
    import _vnl_unary_functionPython
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


import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
class vnl_unary_functionD_vnl_vectorD(object):
    """Proxy of C++ vnl_unary_functionD_vnl_vectorD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def f(self, i: 'vnl_vectorD') -> "double":
        """f(vnl_unary_functionD_vnl_vectorD self, vnl_vectorD i) -> double"""
        return _vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_f(self, i)


    def get_range_min(self) -> "double":
        """get_range_min(vnl_unary_functionD_vnl_vectorD self) -> double"""
        return _vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_get_range_min(self)


    def get_range_max(self) -> "double":
        """get_range_max(vnl_unary_functionD_vnl_vectorD self) -> double"""
        return _vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_get_range_max(self)


    def Copy(self) -> "vnl_unary_functionD_vnl_vectorD *":
        """Copy(vnl_unary_functionD_vnl_vectorD self) -> vnl_unary_functionD_vnl_vectorD"""
        return _vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_Copy(self)

    __swig_destroy__ = _vnl_unary_functionPython.delete_vnl_unary_functionD_vnl_vectorD
vnl_unary_functionD_vnl_vectorD.f = new_instancemethod(_vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_f, None, vnl_unary_functionD_vnl_vectorD)
vnl_unary_functionD_vnl_vectorD.get_range_min = new_instancemethod(_vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_get_range_min, None, vnl_unary_functionD_vnl_vectorD)
vnl_unary_functionD_vnl_vectorD.get_range_max = new_instancemethod(_vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_get_range_max, None, vnl_unary_functionD_vnl_vectorD)
vnl_unary_functionD_vnl_vectorD.Copy = new_instancemethod(_vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_Copy, None, vnl_unary_functionD_vnl_vectorD)
vnl_unary_functionD_vnl_vectorD_swigregister = _vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD_swigregister
vnl_unary_functionD_vnl_vectorD_swigregister(vnl_unary_functionD_vnl_vectorD)



