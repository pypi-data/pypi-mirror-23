# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkContinuousIndexPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkContinuousIndexPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkContinuousIndexPython')
    _itkContinuousIndexPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkContinuousIndexPython', [dirname(__file__)])
        except ImportError:
            import _itkContinuousIndexPython
            return _itkContinuousIndexPython
        try:
            _mod = imp.load_module('_itkContinuousIndexPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkContinuousIndexPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkContinuousIndexPython
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


import itkPointPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
class itkContinuousIndexD2(itkPointPython.itkPointD2):
    """Proxy of C++ itkContinuousIndexD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkContinuousIndexD2 self) -> itkContinuousIndexD2
        __init__(itkContinuousIndexD2 self, itkContinuousIndexD2 r) -> itkContinuousIndexD2
        __init__(itkContinuousIndexD2 self, double const * r) -> itkContinuousIndexD2
        __init__(itkContinuousIndexD2 self, itkIndex2 index) -> itkContinuousIndexD2
        """
        _itkContinuousIndexPython.itkContinuousIndexD2_swiginit(self, _itkContinuousIndexPython.new_itkContinuousIndexD2(*args))
    __swig_destroy__ = _itkContinuousIndexPython.delete_itkContinuousIndexD2

    def __getitem__(self, d: 'unsigned long') -> "double":
        """__getitem__(itkContinuousIndexD2 self, unsigned long d) -> double"""
        return _itkContinuousIndexPython.itkContinuousIndexD2___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'double') -> "void":
        """__setitem__(itkContinuousIndexD2 self, unsigned long d, double v)"""
        return _itkContinuousIndexPython.itkContinuousIndexD2___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkContinuousIndexPython.itkContinuousIndexD2___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkContinuousIndexD2 self) -> std::string"""
        return _itkContinuousIndexPython.itkContinuousIndexD2___repr__(self)

itkContinuousIndexD2.__getitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD2___getitem__, None, itkContinuousIndexD2)
itkContinuousIndexD2.__setitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD2___setitem__, None, itkContinuousIndexD2)
itkContinuousIndexD2.__repr__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD2___repr__, None, itkContinuousIndexD2)
itkContinuousIndexD2_swigregister = _itkContinuousIndexPython.itkContinuousIndexD2_swigregister
itkContinuousIndexD2_swigregister(itkContinuousIndexD2)

def itkContinuousIndexD2___len__() -> "unsigned int":
    """itkContinuousIndexD2___len__() -> unsigned int"""
    return _itkContinuousIndexPython.itkContinuousIndexD2___len__()

class itkContinuousIndexD3(itkPointPython.itkPointD3):
    """Proxy of C++ itkContinuousIndexD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkContinuousIndexD3 self) -> itkContinuousIndexD3
        __init__(itkContinuousIndexD3 self, itkContinuousIndexD3 r) -> itkContinuousIndexD3
        __init__(itkContinuousIndexD3 self, double const * r) -> itkContinuousIndexD3
        __init__(itkContinuousIndexD3 self, itkIndex3 index) -> itkContinuousIndexD3
        """
        _itkContinuousIndexPython.itkContinuousIndexD3_swiginit(self, _itkContinuousIndexPython.new_itkContinuousIndexD3(*args))
    __swig_destroy__ = _itkContinuousIndexPython.delete_itkContinuousIndexD3

    def __getitem__(self, d: 'unsigned long') -> "double":
        """__getitem__(itkContinuousIndexD3 self, unsigned long d) -> double"""
        return _itkContinuousIndexPython.itkContinuousIndexD3___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'double') -> "void":
        """__setitem__(itkContinuousIndexD3 self, unsigned long d, double v)"""
        return _itkContinuousIndexPython.itkContinuousIndexD3___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkContinuousIndexPython.itkContinuousIndexD3___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkContinuousIndexD3 self) -> std::string"""
        return _itkContinuousIndexPython.itkContinuousIndexD3___repr__(self)

itkContinuousIndexD3.__getitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD3___getitem__, None, itkContinuousIndexD3)
itkContinuousIndexD3.__setitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD3___setitem__, None, itkContinuousIndexD3)
itkContinuousIndexD3.__repr__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD3___repr__, None, itkContinuousIndexD3)
itkContinuousIndexD3_swigregister = _itkContinuousIndexPython.itkContinuousIndexD3_swigregister
itkContinuousIndexD3_swigregister(itkContinuousIndexD3)

def itkContinuousIndexD3___len__() -> "unsigned int":
    """itkContinuousIndexD3___len__() -> unsigned int"""
    return _itkContinuousIndexPython.itkContinuousIndexD3___len__()

class itkContinuousIndexD4(itkPointPython.itkPointD4):
    """Proxy of C++ itkContinuousIndexD4 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkContinuousIndexD4 self) -> itkContinuousIndexD4
        __init__(itkContinuousIndexD4 self, itkContinuousIndexD4 r) -> itkContinuousIndexD4
        __init__(itkContinuousIndexD4 self, double const * r) -> itkContinuousIndexD4
        __init__(itkContinuousIndexD4 self, itkIndex4 index) -> itkContinuousIndexD4
        """
        _itkContinuousIndexPython.itkContinuousIndexD4_swiginit(self, _itkContinuousIndexPython.new_itkContinuousIndexD4(*args))
    __swig_destroy__ = _itkContinuousIndexPython.delete_itkContinuousIndexD4

    def __getitem__(self, d: 'unsigned long') -> "double":
        """__getitem__(itkContinuousIndexD4 self, unsigned long d) -> double"""
        return _itkContinuousIndexPython.itkContinuousIndexD4___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'double') -> "void":
        """__setitem__(itkContinuousIndexD4 self, unsigned long d, double v)"""
        return _itkContinuousIndexPython.itkContinuousIndexD4___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkContinuousIndexPython.itkContinuousIndexD4___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkContinuousIndexD4 self) -> std::string"""
        return _itkContinuousIndexPython.itkContinuousIndexD4___repr__(self)

itkContinuousIndexD4.__getitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD4___getitem__, None, itkContinuousIndexD4)
itkContinuousIndexD4.__setitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD4___setitem__, None, itkContinuousIndexD4)
itkContinuousIndexD4.__repr__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexD4___repr__, None, itkContinuousIndexD4)
itkContinuousIndexD4_swigregister = _itkContinuousIndexPython.itkContinuousIndexD4_swigregister
itkContinuousIndexD4_swigregister(itkContinuousIndexD4)

def itkContinuousIndexD4___len__() -> "unsigned int":
    """itkContinuousIndexD4___len__() -> unsigned int"""
    return _itkContinuousIndexPython.itkContinuousIndexD4___len__()

class itkContinuousIndexF2(itkPointPython.itkPointF2):
    """Proxy of C++ itkContinuousIndexF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkContinuousIndexF2 self) -> itkContinuousIndexF2
        __init__(itkContinuousIndexF2 self, itkContinuousIndexF2 r) -> itkContinuousIndexF2
        __init__(itkContinuousIndexF2 self, float const * r) -> itkContinuousIndexF2
        __init__(itkContinuousIndexF2 self, itkIndex2 index) -> itkContinuousIndexF2
        """
        _itkContinuousIndexPython.itkContinuousIndexF2_swiginit(self, _itkContinuousIndexPython.new_itkContinuousIndexF2(*args))
    __swig_destroy__ = _itkContinuousIndexPython.delete_itkContinuousIndexF2

    def __getitem__(self, d: 'unsigned long') -> "float":
        """__getitem__(itkContinuousIndexF2 self, unsigned long d) -> float"""
        return _itkContinuousIndexPython.itkContinuousIndexF2___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'float') -> "void":
        """__setitem__(itkContinuousIndexF2 self, unsigned long d, float v)"""
        return _itkContinuousIndexPython.itkContinuousIndexF2___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkContinuousIndexPython.itkContinuousIndexF2___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkContinuousIndexF2 self) -> std::string"""
        return _itkContinuousIndexPython.itkContinuousIndexF2___repr__(self)

itkContinuousIndexF2.__getitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF2___getitem__, None, itkContinuousIndexF2)
itkContinuousIndexF2.__setitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF2___setitem__, None, itkContinuousIndexF2)
itkContinuousIndexF2.__repr__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF2___repr__, None, itkContinuousIndexF2)
itkContinuousIndexF2_swigregister = _itkContinuousIndexPython.itkContinuousIndexF2_swigregister
itkContinuousIndexF2_swigregister(itkContinuousIndexF2)

def itkContinuousIndexF2___len__() -> "unsigned int":
    """itkContinuousIndexF2___len__() -> unsigned int"""
    return _itkContinuousIndexPython.itkContinuousIndexF2___len__()

class itkContinuousIndexF3(itkPointPython.itkPointF3):
    """Proxy of C++ itkContinuousIndexF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkContinuousIndexF3 self) -> itkContinuousIndexF3
        __init__(itkContinuousIndexF3 self, itkContinuousIndexF3 r) -> itkContinuousIndexF3
        __init__(itkContinuousIndexF3 self, float const * r) -> itkContinuousIndexF3
        __init__(itkContinuousIndexF3 self, itkIndex3 index) -> itkContinuousIndexF3
        """
        _itkContinuousIndexPython.itkContinuousIndexF3_swiginit(self, _itkContinuousIndexPython.new_itkContinuousIndexF3(*args))
    __swig_destroy__ = _itkContinuousIndexPython.delete_itkContinuousIndexF3

    def __getitem__(self, d: 'unsigned long') -> "float":
        """__getitem__(itkContinuousIndexF3 self, unsigned long d) -> float"""
        return _itkContinuousIndexPython.itkContinuousIndexF3___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'float') -> "void":
        """__setitem__(itkContinuousIndexF3 self, unsigned long d, float v)"""
        return _itkContinuousIndexPython.itkContinuousIndexF3___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkContinuousIndexPython.itkContinuousIndexF3___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkContinuousIndexF3 self) -> std::string"""
        return _itkContinuousIndexPython.itkContinuousIndexF3___repr__(self)

itkContinuousIndexF3.__getitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF3___getitem__, None, itkContinuousIndexF3)
itkContinuousIndexF3.__setitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF3___setitem__, None, itkContinuousIndexF3)
itkContinuousIndexF3.__repr__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF3___repr__, None, itkContinuousIndexF3)
itkContinuousIndexF3_swigregister = _itkContinuousIndexPython.itkContinuousIndexF3_swigregister
itkContinuousIndexF3_swigregister(itkContinuousIndexF3)

def itkContinuousIndexF3___len__() -> "unsigned int":
    """itkContinuousIndexF3___len__() -> unsigned int"""
    return _itkContinuousIndexPython.itkContinuousIndexF3___len__()

class itkContinuousIndexF4(itkPointPython.itkPointF4):
    """Proxy of C++ itkContinuousIndexF4 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkContinuousIndexF4 self) -> itkContinuousIndexF4
        __init__(itkContinuousIndexF4 self, itkContinuousIndexF4 r) -> itkContinuousIndexF4
        __init__(itkContinuousIndexF4 self, float const * r) -> itkContinuousIndexF4
        __init__(itkContinuousIndexF4 self, itkIndex4 index) -> itkContinuousIndexF4
        """
        _itkContinuousIndexPython.itkContinuousIndexF4_swiginit(self, _itkContinuousIndexPython.new_itkContinuousIndexF4(*args))
    __swig_destroy__ = _itkContinuousIndexPython.delete_itkContinuousIndexF4

    def __getitem__(self, d: 'unsigned long') -> "float":
        """__getitem__(itkContinuousIndexF4 self, unsigned long d) -> float"""
        return _itkContinuousIndexPython.itkContinuousIndexF4___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'float') -> "void":
        """__setitem__(itkContinuousIndexF4 self, unsigned long d, float v)"""
        return _itkContinuousIndexPython.itkContinuousIndexF4___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkContinuousIndexPython.itkContinuousIndexF4___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkContinuousIndexF4 self) -> std::string"""
        return _itkContinuousIndexPython.itkContinuousIndexF4___repr__(self)

itkContinuousIndexF4.__getitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF4___getitem__, None, itkContinuousIndexF4)
itkContinuousIndexF4.__setitem__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF4___setitem__, None, itkContinuousIndexF4)
itkContinuousIndexF4.__repr__ = new_instancemethod(_itkContinuousIndexPython.itkContinuousIndexF4___repr__, None, itkContinuousIndexF4)
itkContinuousIndexF4_swigregister = _itkContinuousIndexPython.itkContinuousIndexF4_swigregister
itkContinuousIndexF4_swigregister(itkContinuousIndexF4)

def itkContinuousIndexF4___len__() -> "unsigned int":
    """itkContinuousIndexF4___len__() -> unsigned int"""
    return _itkContinuousIndexPython.itkContinuousIndexF4___len__()



