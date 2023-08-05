# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _vnl_cost_functionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_vnl_cost_functionPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_vnl_cost_functionPython')
    _vnl_cost_functionPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vnl_cost_functionPython', [dirname(__file__)])
        except ImportError:
            import _vnl_cost_functionPython
            return _vnl_cost_functionPython
        try:
            _mod = imp.load_module('_vnl_cost_functionPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _vnl_cost_functionPython = swig_import_helper()
    del swig_import_helper
else:
    import _vnl_cost_functionPython
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
import vnl_unary_functionPython
class vnl_cost_function(vnl_unary_functionPython.vnl_unary_functionD_vnl_vectorD):
    """Proxy of C++ vnl_cost_function class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_cost_functionPython.delete_vnl_cost_function

    def compute(self, x: 'vnl_vectorD', f: 'double *', g: 'vnl_vectorD') -> "void":
        """compute(vnl_cost_function self, vnl_vectorD x, double * f, vnl_vectorD g)"""
        return _vnl_cost_functionPython.vnl_cost_function_compute(self, x, f, g)


    def get_number_of_unknowns(self) -> "int":
        """get_number_of_unknowns(vnl_cost_function self) -> int"""
        return _vnl_cost_functionPython.vnl_cost_function_get_number_of_unknowns(self)


    def reported_error(self, f_value: 'double') -> "double":
        """reported_error(vnl_cost_function self, double f_value) -> double"""
        return _vnl_cost_functionPython.vnl_cost_function_reported_error(self, f_value)


    def gradf(self, *args) -> "vnl_vectorD":
        """
        gradf(vnl_cost_function self, vnl_vectorD x, vnl_vectorD gradient)
        gradf(vnl_cost_function self, vnl_vectorD x) -> vnl_vectorD
        """
        return _vnl_cost_functionPython.vnl_cost_function_gradf(self, *args)


    def fdgradf(self, *args) -> "vnl_vectorD":
        """
        fdgradf(vnl_cost_function self, vnl_vectorD x, vnl_vectorD gradient, double stepsize=1.0000000000000001E-5)
        fdgradf(vnl_cost_function self, vnl_vectorD x, vnl_vectorD gradient)
        fdgradf(vnl_cost_function self, vnl_vectorD x) -> vnl_vectorD
        """
        return _vnl_cost_functionPython.vnl_cost_function_fdgradf(self, *args)


    def __init__(self, *args):
        """
        __init__(vnl_cost_function self) -> vnl_cost_function
        __init__(vnl_cost_function self, int number_of_unknowns) -> vnl_cost_function
        __init__(vnl_cost_function self, vnl_cost_function arg0) -> vnl_cost_function
        """
        _vnl_cost_functionPython.vnl_cost_function_swiginit(self, _vnl_cost_functionPython.new_vnl_cost_function(*args))
vnl_cost_function.compute = new_instancemethod(_vnl_cost_functionPython.vnl_cost_function_compute, None, vnl_cost_function)
vnl_cost_function.get_number_of_unknowns = new_instancemethod(_vnl_cost_functionPython.vnl_cost_function_get_number_of_unknowns, None, vnl_cost_function)
vnl_cost_function.reported_error = new_instancemethod(_vnl_cost_functionPython.vnl_cost_function_reported_error, None, vnl_cost_function)
vnl_cost_function.gradf = new_instancemethod(_vnl_cost_functionPython.vnl_cost_function_gradf, None, vnl_cost_function)
vnl_cost_function.fdgradf = new_instancemethod(_vnl_cost_functionPython.vnl_cost_function_fdgradf, None, vnl_cost_function)
vnl_cost_function_swigregister = _vnl_cost_functionPython.vnl_cost_function_swigregister
vnl_cost_function_swigregister(vnl_cost_function)



