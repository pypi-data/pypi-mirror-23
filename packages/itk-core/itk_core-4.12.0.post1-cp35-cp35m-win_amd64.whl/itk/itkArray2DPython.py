# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkArray2DPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkArray2DPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkArray2DPython')
    _itkArray2DPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkArray2DPython', [dirname(__file__)])
        except ImportError:
            import _itkArray2DPython
            return _itkArray2DPython
        try:
            _mod = imp.load_module('_itkArray2DPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkArray2DPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkArray2DPython
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


import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
class itkArray2DD(vnl_matrixPython.vnl_matrixD):
    """Proxy of C++ itkArray2DD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkArray2DD self) -> itkArray2DD
        __init__(itkArray2DD self, unsigned int rows, unsigned int cols) -> itkArray2DD
        __init__(itkArray2DD self, itkArray2DD array) -> itkArray2DD
        __init__(itkArray2DD self, vnl_matrixD matrix) -> itkArray2DD
        """
        _itkArray2DPython.itkArray2DD_swiginit(self, _itkArray2DPython.new_itkArray2DD(*args))

    def Fill(self, v: 'double const &') -> "void":
        """Fill(itkArray2DD self, double const & v)"""
        return _itkArray2DPython.itkArray2DD_Fill(self, v)


    def GetElement(self, row: 'unsigned long long', col: 'unsigned long long') -> "double const &":
        """GetElement(itkArray2DD self, unsigned long long row, unsigned long long col) -> double const &"""
        return _itkArray2DPython.itkArray2DD_GetElement(self, row, col)


    def SetElement(self, row: 'unsigned long long', col: 'unsigned long long', value: 'double const &') -> "void":
        """SetElement(itkArray2DD self, unsigned long long row, unsigned long long col, double const & value)"""
        return _itkArray2DPython.itkArray2DD_SetElement(self, row, col, value)


    def SetSize(self, m: 'unsigned int', n: 'unsigned int') -> "void":
        """SetSize(itkArray2DD self, unsigned int m, unsigned int n)"""
        return _itkArray2DPython.itkArray2DD_SetSize(self, m, n)

    __swig_destroy__ = _itkArray2DPython.delete_itkArray2DD
itkArray2DD.Fill = new_instancemethod(_itkArray2DPython.itkArray2DD_Fill, None, itkArray2DD)
itkArray2DD.GetElement = new_instancemethod(_itkArray2DPython.itkArray2DD_GetElement, None, itkArray2DD)
itkArray2DD.SetElement = new_instancemethod(_itkArray2DPython.itkArray2DD_SetElement, None, itkArray2DD)
itkArray2DD.SetSize = new_instancemethod(_itkArray2DPython.itkArray2DD_SetSize, None, itkArray2DD)
itkArray2DD_swigregister = _itkArray2DPython.itkArray2DD_swigregister
itkArray2DD_swigregister(itkArray2DD)

class itkArray2DF(vnl_matrixPython.vnl_matrixF):
    """Proxy of C++ itkArray2DF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkArray2DF self) -> itkArray2DF
        __init__(itkArray2DF self, unsigned int rows, unsigned int cols) -> itkArray2DF
        __init__(itkArray2DF self, itkArray2DF array) -> itkArray2DF
        __init__(itkArray2DF self, vnl_matrixF matrix) -> itkArray2DF
        """
        _itkArray2DPython.itkArray2DF_swiginit(self, _itkArray2DPython.new_itkArray2DF(*args))

    def Fill(self, v: 'float const &') -> "void":
        """Fill(itkArray2DF self, float const & v)"""
        return _itkArray2DPython.itkArray2DF_Fill(self, v)


    def GetElement(self, row: 'unsigned long long', col: 'unsigned long long') -> "float const &":
        """GetElement(itkArray2DF self, unsigned long long row, unsigned long long col) -> float const &"""
        return _itkArray2DPython.itkArray2DF_GetElement(self, row, col)


    def SetElement(self, row: 'unsigned long long', col: 'unsigned long long', value: 'float const &') -> "void":
        """SetElement(itkArray2DF self, unsigned long long row, unsigned long long col, float const & value)"""
        return _itkArray2DPython.itkArray2DF_SetElement(self, row, col, value)


    def SetSize(self, m: 'unsigned int', n: 'unsigned int') -> "void":
        """SetSize(itkArray2DF self, unsigned int m, unsigned int n)"""
        return _itkArray2DPython.itkArray2DF_SetSize(self, m, n)

    __swig_destroy__ = _itkArray2DPython.delete_itkArray2DF
itkArray2DF.Fill = new_instancemethod(_itkArray2DPython.itkArray2DF_Fill, None, itkArray2DF)
itkArray2DF.GetElement = new_instancemethod(_itkArray2DPython.itkArray2DF_GetElement, None, itkArray2DF)
itkArray2DF.SetElement = new_instancemethod(_itkArray2DPython.itkArray2DF_SetElement, None, itkArray2DF)
itkArray2DF.SetSize = new_instancemethod(_itkArray2DPython.itkArray2DF_SetSize, None, itkArray2DF)
itkArray2DF_swigregister = _itkArray2DPython.itkArray2DF_swigregister
itkArray2DF_swigregister(itkArray2DF)

class itkArray2DUI(vnl_matrixPython.vnl_matrixUI):
    """Proxy of C++ itkArray2DUI class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkArray2DUI self) -> itkArray2DUI
        __init__(itkArray2DUI self, unsigned int rows, unsigned int cols) -> itkArray2DUI
        __init__(itkArray2DUI self, itkArray2DUI array) -> itkArray2DUI
        __init__(itkArray2DUI self, vnl_matrixUI matrix) -> itkArray2DUI
        """
        _itkArray2DPython.itkArray2DUI_swiginit(self, _itkArray2DPython.new_itkArray2DUI(*args))

    def Fill(self, v: 'unsigned int const &') -> "void":
        """Fill(itkArray2DUI self, unsigned int const & v)"""
        return _itkArray2DPython.itkArray2DUI_Fill(self, v)


    def GetElement(self, row: 'unsigned long long', col: 'unsigned long long') -> "unsigned int const &":
        """GetElement(itkArray2DUI self, unsigned long long row, unsigned long long col) -> unsigned int const &"""
        return _itkArray2DPython.itkArray2DUI_GetElement(self, row, col)


    def SetElement(self, row: 'unsigned long long', col: 'unsigned long long', value: 'unsigned int const &') -> "void":
        """SetElement(itkArray2DUI self, unsigned long long row, unsigned long long col, unsigned int const & value)"""
        return _itkArray2DPython.itkArray2DUI_SetElement(self, row, col, value)


    def SetSize(self, m: 'unsigned int', n: 'unsigned int') -> "void":
        """SetSize(itkArray2DUI self, unsigned int m, unsigned int n)"""
        return _itkArray2DPython.itkArray2DUI_SetSize(self, m, n)

    __swig_destroy__ = _itkArray2DPython.delete_itkArray2DUI
itkArray2DUI.Fill = new_instancemethod(_itkArray2DPython.itkArray2DUI_Fill, None, itkArray2DUI)
itkArray2DUI.GetElement = new_instancemethod(_itkArray2DPython.itkArray2DUI_GetElement, None, itkArray2DUI)
itkArray2DUI.SetElement = new_instancemethod(_itkArray2DPython.itkArray2DUI_SetElement, None, itkArray2DUI)
itkArray2DUI.SetSize = new_instancemethod(_itkArray2DPython.itkArray2DUI_SetSize, None, itkArray2DUI)
itkArray2DUI_swigregister = _itkArray2DPython.itkArray2DUI_swigregister
itkArray2DUI_swigregister(itkArray2DUI)



