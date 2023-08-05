# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVariableSizeMatrixPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVariableSizeMatrixPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVariableSizeMatrixPython')
    _itkVariableSizeMatrixPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVariableSizeMatrixPython', [dirname(__file__)])
        except ImportError:
            import _itkVariableSizeMatrixPython
            return _itkVariableSizeMatrixPython
        try:
            _mod = imp.load_module('_itkVariableSizeMatrixPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVariableSizeMatrixPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVariableSizeMatrixPython
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


import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
class itkVariableSizeMatrixD(object):
    """Proxy of C++ itkVariableSizeMatrixD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __add__(self, matrix):
        """__add__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___add__(self, matrix)


    def __iadd__(self, matrix):
        """__iadd__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___iadd__(self, matrix)


    def __sub__(self, matrix):
        """__sub__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___sub__(self, matrix)


    def __isub__(self, matrix):
        """__isub__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___isub__(self, matrix)


    def __neg__(self):
        """__neg__(itkVariableSizeMatrixD self) -> itkVariableSizeMatrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___neg__(self)


    def __imul__(self, *args):
        """
        __imul__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix)
        __imul__(itkVariableSizeMatrixD self, vnl_matrixD matrix)
        __imul__(itkVariableSizeMatrixD self, double const & value)
        """
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___imul__(self, *args)


    def __mul__(self, *args):
        """
        __mul__(itkVariableSizeMatrixD self, itkArrayD vector) -> itkArrayD
        __mul__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD
        __mul__(itkVariableSizeMatrixD self, vnl_matrixD matrix) -> vnl_matrixD
        __mul__(itkVariableSizeMatrixD self, vnl_vectorD matrix) -> vnl_vectorD
        __mul__(itkVariableSizeMatrixD self, double const & value) -> itkVariableSizeMatrixD
        """
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___mul__(self, *args)


    def __itruediv__(self, *args):
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def __truediv__(self, *args):
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___truediv__(self, *args)
    __div__ = __truediv__



    def __call__(self, *args):
        """
        __call__(itkVariableSizeMatrixD self, unsigned int row, unsigned int col) -> double
        __call__(itkVariableSizeMatrixD self, unsigned int row, unsigned int col) -> double const &
        """
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___call__(self, *args)


    def GetVnlMatrix(self, *args):
        """
        GetVnlMatrix(itkVariableSizeMatrixD self) -> vnl_matrixD
        GetVnlMatrix(itkVariableSizeMatrixD self) -> vnl_matrixD
        """
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetVnlMatrix(self, *args)


    def SetIdentity(self):
        """SetIdentity(itkVariableSizeMatrixD self)"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_SetIdentity(self)


    def Fill(self, value):
        """Fill(itkVariableSizeMatrixD self, double const & value)"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Fill(self, value)


    def __eq__(self, matrix):
        """__eq__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> bool"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___eq__(self, matrix)


    def __ne__(self, matrix):
        """__ne__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> bool"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___ne__(self, matrix)


    def GetInverse(self):
        """GetInverse(itkVariableSizeMatrixD self) -> vnl_matrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetInverse(self)


    def GetTranspose(self):
        """GetTranspose(itkVariableSizeMatrixD self) -> vnl_matrixD"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetTranspose(self)


    def __init__(self, *args):
        """
        __init__(itkVariableSizeMatrixD self) -> itkVariableSizeMatrixD
        __init__(itkVariableSizeMatrixD self, unsigned int rows, unsigned int cols) -> itkVariableSizeMatrixD
        __init__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD
        """
        _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_swiginit(self, _itkVariableSizeMatrixPython.new_itkVariableSizeMatrixD(*args))

    def Rows(self):
        """Rows(itkVariableSizeMatrixD self) -> unsigned int"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Rows(self)


    def Cols(self):
        """Cols(itkVariableSizeMatrixD self) -> unsigned int"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Cols(self)


    def SetSize(self, r, c):
        """SetSize(itkVariableSizeMatrixD self, unsigned int r, unsigned int c) -> bool"""
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_SetSize(self, r, c)

    __swig_destroy__ = _itkVariableSizeMatrixPython.delete_itkVariableSizeMatrixD
itkVariableSizeMatrixD.__add__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___add__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__iadd__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___iadd__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__sub__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___sub__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__isub__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___isub__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__neg__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___neg__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__imul__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___imul__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__mul__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___mul__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__call__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___call__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.GetVnlMatrix = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetVnlMatrix, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.SetIdentity = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_SetIdentity, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.Fill = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Fill, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__eq__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___eq__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.__ne__ = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___ne__, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.GetInverse = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetInverse, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.GetTranspose = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetTranspose, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.Rows = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Rows, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.Cols = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Cols, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD.SetSize = new_instancemethod(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_SetSize, None, itkVariableSizeMatrixD)
itkVariableSizeMatrixD_swigregister = _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_swigregister
itkVariableSizeMatrixD_swigregister(itkVariableSizeMatrixD)



