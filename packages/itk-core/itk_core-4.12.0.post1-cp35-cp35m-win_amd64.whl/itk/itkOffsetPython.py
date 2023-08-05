# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkOffsetPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkOffsetPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkOffsetPython')
    _itkOffsetPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkOffsetPython', [dirname(__file__)])
        except ImportError:
            import _itkOffsetPython
            return _itkOffsetPython
        try:
            _mod = imp.load_module('_itkOffsetPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkOffsetPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkOffsetPython
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


import itkSizePython
import pyBasePython
class itkOffset1(object):
    """Proxy of C++ itkOffset1 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def GetOffsetDimension() -> "unsigned int":
        """GetOffsetDimension() -> unsigned int"""
        return _itkOffsetPython.itkOffset1_GetOffsetDimension()

    GetOffsetDimension = staticmethod(GetOffsetDimension)

    def __add__(self, *args) -> "itkOffset1 const":
        """
        __add__(itkOffset1 self, itkOffset1 offset) -> itkOffset1
        __add__(itkOffset1 self, itkSize1 size) -> itkOffset1
        """
        return _itkOffsetPython.itkOffset1___add__(self, *args)


    def __sub__(self, vec: 'itkOffset1') -> "itkOffset1 const":
        """__sub__(itkOffset1 self, itkOffset1 vec) -> itkOffset1"""
        return _itkOffsetPython.itkOffset1___sub__(self, vec)


    def __iadd__(self, *args) -> "itkOffset1 const &":
        """
        __iadd__(itkOffset1 self, itkSize1 size) -> itkOffset1
        __iadd__(itkOffset1 self, itkOffset1 vec) -> itkOffset1
        """
        return _itkOffsetPython.itkOffset1___iadd__(self, *args)


    def __isub__(self, *args) -> "itkOffset1 const &":
        """
        __isub__(itkOffset1 self, itkSize1 size) -> itkOffset1
        __isub__(itkOffset1 self, itkOffset1 vec) -> itkOffset1
        """
        return _itkOffsetPython.itkOffset1___isub__(self, *args)


    def __eq__(self, vec: 'itkOffset1') -> "bool":
        """__eq__(itkOffset1 self, itkOffset1 vec) -> bool"""
        return _itkOffsetPython.itkOffset1___eq__(self, vec)


    def __ne__(self, vec: 'itkOffset1') -> "bool":
        """__ne__(itkOffset1 self, itkOffset1 vec) -> bool"""
        return _itkOffsetPython.itkOffset1___ne__(self, vec)


    def GetOffset(self) -> "long long const *":
        """GetOffset(itkOffset1 self) -> long long const *"""
        return _itkOffsetPython.itkOffset1_GetOffset(self)


    def SetOffset(self, val: 'long long const *') -> "void":
        """SetOffset(itkOffset1 self, long long const * val)"""
        return _itkOffsetPython.itkOffset1_SetOffset(self, val)


    def GetBasisOffset(dim: 'unsigned int') -> "itkOffset1":
        """GetBasisOffset(unsigned int dim) -> itkOffset1"""
        return _itkOffsetPython.itkOffset1_GetBasisOffset(dim)

    GetBasisOffset = staticmethod(GetBasisOffset)

    def Fill(self, value: 'long long') -> "void":
        """Fill(itkOffset1 self, long long value)"""
        return _itkOffsetPython.itkOffset1_Fill(self, value)


    def __init__(self, *args):
        """
        __init__(itkOffset1 self) -> itkOffset1
        __init__(itkOffset1 self, itkOffset1 arg0) -> itkOffset1
        """
        _itkOffsetPython.itkOffset1_swiginit(self, _itkOffsetPython.new_itkOffset1(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset1

    def __getitem__(self, d: 'unsigned long') -> "long":
        """__getitem__(itkOffset1 self, unsigned long d) -> long"""
        return _itkOffsetPython.itkOffset1___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'long') -> "void":
        """__setitem__(itkOffset1 self, unsigned long d, long v)"""
        return _itkOffsetPython.itkOffset1___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkOffsetPython.itkOffset1___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkOffset1 self) -> std::string"""
        return _itkOffsetPython.itkOffset1___repr__(self)

itkOffset1.__add__ = new_instancemethod(_itkOffsetPython.itkOffset1___add__, None, itkOffset1)
itkOffset1.__sub__ = new_instancemethod(_itkOffsetPython.itkOffset1___sub__, None, itkOffset1)
itkOffset1.__iadd__ = new_instancemethod(_itkOffsetPython.itkOffset1___iadd__, None, itkOffset1)
itkOffset1.__isub__ = new_instancemethod(_itkOffsetPython.itkOffset1___isub__, None, itkOffset1)
itkOffset1.__eq__ = new_instancemethod(_itkOffsetPython.itkOffset1___eq__, None, itkOffset1)
itkOffset1.__ne__ = new_instancemethod(_itkOffsetPython.itkOffset1___ne__, None, itkOffset1)
itkOffset1.GetOffset = new_instancemethod(_itkOffsetPython.itkOffset1_GetOffset, None, itkOffset1)
itkOffset1.SetOffset = new_instancemethod(_itkOffsetPython.itkOffset1_SetOffset, None, itkOffset1)
itkOffset1.Fill = new_instancemethod(_itkOffsetPython.itkOffset1_Fill, None, itkOffset1)
itkOffset1.__getitem__ = new_instancemethod(_itkOffsetPython.itkOffset1___getitem__, None, itkOffset1)
itkOffset1.__setitem__ = new_instancemethod(_itkOffsetPython.itkOffset1___setitem__, None, itkOffset1)
itkOffset1.__repr__ = new_instancemethod(_itkOffsetPython.itkOffset1___repr__, None, itkOffset1)
itkOffset1_swigregister = _itkOffsetPython.itkOffset1_swigregister
itkOffset1_swigregister(itkOffset1)

def itkOffset1_GetOffsetDimension() -> "unsigned int":
    """itkOffset1_GetOffsetDimension() -> unsigned int"""
    return _itkOffsetPython.itkOffset1_GetOffsetDimension()

def itkOffset1_GetBasisOffset(dim: 'unsigned int') -> "itkOffset1":
    """itkOffset1_GetBasisOffset(unsigned int dim) -> itkOffset1"""
    return _itkOffsetPython.itkOffset1_GetBasisOffset(dim)

def itkOffset1___len__() -> "unsigned int":
    """itkOffset1___len__() -> unsigned int"""
    return _itkOffsetPython.itkOffset1___len__()

class itkOffset2(object):
    """Proxy of C++ itkOffset2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def GetOffsetDimension() -> "unsigned int":
        """GetOffsetDimension() -> unsigned int"""
        return _itkOffsetPython.itkOffset2_GetOffsetDimension()

    GetOffsetDimension = staticmethod(GetOffsetDimension)

    def __add__(self, *args) -> "itkOffset2 const":
        """
        __add__(itkOffset2 self, itkOffset2 offset) -> itkOffset2
        __add__(itkOffset2 self, itkSize2 size) -> itkOffset2
        """
        return _itkOffsetPython.itkOffset2___add__(self, *args)


    def __sub__(self, vec: 'itkOffset2') -> "itkOffset2 const":
        """__sub__(itkOffset2 self, itkOffset2 vec) -> itkOffset2"""
        return _itkOffsetPython.itkOffset2___sub__(self, vec)


    def __iadd__(self, *args) -> "itkOffset2 const &":
        """
        __iadd__(itkOffset2 self, itkSize2 size) -> itkOffset2
        __iadd__(itkOffset2 self, itkOffset2 vec) -> itkOffset2
        """
        return _itkOffsetPython.itkOffset2___iadd__(self, *args)


    def __isub__(self, *args) -> "itkOffset2 const &":
        """
        __isub__(itkOffset2 self, itkSize2 size) -> itkOffset2
        __isub__(itkOffset2 self, itkOffset2 vec) -> itkOffset2
        """
        return _itkOffsetPython.itkOffset2___isub__(self, *args)


    def __eq__(self, vec: 'itkOffset2') -> "bool":
        """__eq__(itkOffset2 self, itkOffset2 vec) -> bool"""
        return _itkOffsetPython.itkOffset2___eq__(self, vec)


    def __ne__(self, vec: 'itkOffset2') -> "bool":
        """__ne__(itkOffset2 self, itkOffset2 vec) -> bool"""
        return _itkOffsetPython.itkOffset2___ne__(self, vec)


    def GetOffset(self) -> "long long const *":
        """GetOffset(itkOffset2 self) -> long long const *"""
        return _itkOffsetPython.itkOffset2_GetOffset(self)


    def SetOffset(self, val: 'long long const *') -> "void":
        """SetOffset(itkOffset2 self, long long const * val)"""
        return _itkOffsetPython.itkOffset2_SetOffset(self, val)


    def GetBasisOffset(dim: 'unsigned int') -> "itkOffset2":
        """GetBasisOffset(unsigned int dim) -> itkOffset2"""
        return _itkOffsetPython.itkOffset2_GetBasisOffset(dim)

    GetBasisOffset = staticmethod(GetBasisOffset)

    def Fill(self, value: 'long long') -> "void":
        """Fill(itkOffset2 self, long long value)"""
        return _itkOffsetPython.itkOffset2_Fill(self, value)


    def __init__(self, *args):
        """
        __init__(itkOffset2 self) -> itkOffset2
        __init__(itkOffset2 self, itkOffset2 arg0) -> itkOffset2
        """
        _itkOffsetPython.itkOffset2_swiginit(self, _itkOffsetPython.new_itkOffset2(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset2

    def __getitem__(self, d: 'unsigned long') -> "long":
        """__getitem__(itkOffset2 self, unsigned long d) -> long"""
        return _itkOffsetPython.itkOffset2___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'long') -> "void":
        """__setitem__(itkOffset2 self, unsigned long d, long v)"""
        return _itkOffsetPython.itkOffset2___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkOffsetPython.itkOffset2___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkOffset2 self) -> std::string"""
        return _itkOffsetPython.itkOffset2___repr__(self)

itkOffset2.__add__ = new_instancemethod(_itkOffsetPython.itkOffset2___add__, None, itkOffset2)
itkOffset2.__sub__ = new_instancemethod(_itkOffsetPython.itkOffset2___sub__, None, itkOffset2)
itkOffset2.__iadd__ = new_instancemethod(_itkOffsetPython.itkOffset2___iadd__, None, itkOffset2)
itkOffset2.__isub__ = new_instancemethod(_itkOffsetPython.itkOffset2___isub__, None, itkOffset2)
itkOffset2.__eq__ = new_instancemethod(_itkOffsetPython.itkOffset2___eq__, None, itkOffset2)
itkOffset2.__ne__ = new_instancemethod(_itkOffsetPython.itkOffset2___ne__, None, itkOffset2)
itkOffset2.GetOffset = new_instancemethod(_itkOffsetPython.itkOffset2_GetOffset, None, itkOffset2)
itkOffset2.SetOffset = new_instancemethod(_itkOffsetPython.itkOffset2_SetOffset, None, itkOffset2)
itkOffset2.Fill = new_instancemethod(_itkOffsetPython.itkOffset2_Fill, None, itkOffset2)
itkOffset2.__getitem__ = new_instancemethod(_itkOffsetPython.itkOffset2___getitem__, None, itkOffset2)
itkOffset2.__setitem__ = new_instancemethod(_itkOffsetPython.itkOffset2___setitem__, None, itkOffset2)
itkOffset2.__repr__ = new_instancemethod(_itkOffsetPython.itkOffset2___repr__, None, itkOffset2)
itkOffset2_swigregister = _itkOffsetPython.itkOffset2_swigregister
itkOffset2_swigregister(itkOffset2)

def itkOffset2_GetOffsetDimension() -> "unsigned int":
    """itkOffset2_GetOffsetDimension() -> unsigned int"""
    return _itkOffsetPython.itkOffset2_GetOffsetDimension()

def itkOffset2_GetBasisOffset(dim: 'unsigned int') -> "itkOffset2":
    """itkOffset2_GetBasisOffset(unsigned int dim) -> itkOffset2"""
    return _itkOffsetPython.itkOffset2_GetBasisOffset(dim)

def itkOffset2___len__() -> "unsigned int":
    """itkOffset2___len__() -> unsigned int"""
    return _itkOffsetPython.itkOffset2___len__()

class itkOffset3(object):
    """Proxy of C++ itkOffset3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def GetOffsetDimension() -> "unsigned int":
        """GetOffsetDimension() -> unsigned int"""
        return _itkOffsetPython.itkOffset3_GetOffsetDimension()

    GetOffsetDimension = staticmethod(GetOffsetDimension)

    def __add__(self, *args) -> "itkOffset3 const":
        """
        __add__(itkOffset3 self, itkOffset3 offset) -> itkOffset3
        __add__(itkOffset3 self, itkSize3 size) -> itkOffset3
        """
        return _itkOffsetPython.itkOffset3___add__(self, *args)


    def __sub__(self, vec: 'itkOffset3') -> "itkOffset3 const":
        """__sub__(itkOffset3 self, itkOffset3 vec) -> itkOffset3"""
        return _itkOffsetPython.itkOffset3___sub__(self, vec)


    def __iadd__(self, *args) -> "itkOffset3 const &":
        """
        __iadd__(itkOffset3 self, itkSize3 size) -> itkOffset3
        __iadd__(itkOffset3 self, itkOffset3 vec) -> itkOffset3
        """
        return _itkOffsetPython.itkOffset3___iadd__(self, *args)


    def __isub__(self, *args) -> "itkOffset3 const &":
        """
        __isub__(itkOffset3 self, itkSize3 size) -> itkOffset3
        __isub__(itkOffset3 self, itkOffset3 vec) -> itkOffset3
        """
        return _itkOffsetPython.itkOffset3___isub__(self, *args)


    def __eq__(self, vec: 'itkOffset3') -> "bool":
        """__eq__(itkOffset3 self, itkOffset3 vec) -> bool"""
        return _itkOffsetPython.itkOffset3___eq__(self, vec)


    def __ne__(self, vec: 'itkOffset3') -> "bool":
        """__ne__(itkOffset3 self, itkOffset3 vec) -> bool"""
        return _itkOffsetPython.itkOffset3___ne__(self, vec)


    def GetOffset(self) -> "long long const *":
        """GetOffset(itkOffset3 self) -> long long const *"""
        return _itkOffsetPython.itkOffset3_GetOffset(self)


    def SetOffset(self, val: 'long long const *') -> "void":
        """SetOffset(itkOffset3 self, long long const * val)"""
        return _itkOffsetPython.itkOffset3_SetOffset(self, val)


    def GetBasisOffset(dim: 'unsigned int') -> "itkOffset3":
        """GetBasisOffset(unsigned int dim) -> itkOffset3"""
        return _itkOffsetPython.itkOffset3_GetBasisOffset(dim)

    GetBasisOffset = staticmethod(GetBasisOffset)

    def Fill(self, value: 'long long') -> "void":
        """Fill(itkOffset3 self, long long value)"""
        return _itkOffsetPython.itkOffset3_Fill(self, value)


    def __init__(self, *args):
        """
        __init__(itkOffset3 self) -> itkOffset3
        __init__(itkOffset3 self, itkOffset3 arg0) -> itkOffset3
        """
        _itkOffsetPython.itkOffset3_swiginit(self, _itkOffsetPython.new_itkOffset3(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset3

    def __getitem__(self, d: 'unsigned long') -> "long":
        """__getitem__(itkOffset3 self, unsigned long d) -> long"""
        return _itkOffsetPython.itkOffset3___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'long') -> "void":
        """__setitem__(itkOffset3 self, unsigned long d, long v)"""
        return _itkOffsetPython.itkOffset3___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkOffsetPython.itkOffset3___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkOffset3 self) -> std::string"""
        return _itkOffsetPython.itkOffset3___repr__(self)

itkOffset3.__add__ = new_instancemethod(_itkOffsetPython.itkOffset3___add__, None, itkOffset3)
itkOffset3.__sub__ = new_instancemethod(_itkOffsetPython.itkOffset3___sub__, None, itkOffset3)
itkOffset3.__iadd__ = new_instancemethod(_itkOffsetPython.itkOffset3___iadd__, None, itkOffset3)
itkOffset3.__isub__ = new_instancemethod(_itkOffsetPython.itkOffset3___isub__, None, itkOffset3)
itkOffset3.__eq__ = new_instancemethod(_itkOffsetPython.itkOffset3___eq__, None, itkOffset3)
itkOffset3.__ne__ = new_instancemethod(_itkOffsetPython.itkOffset3___ne__, None, itkOffset3)
itkOffset3.GetOffset = new_instancemethod(_itkOffsetPython.itkOffset3_GetOffset, None, itkOffset3)
itkOffset3.SetOffset = new_instancemethod(_itkOffsetPython.itkOffset3_SetOffset, None, itkOffset3)
itkOffset3.Fill = new_instancemethod(_itkOffsetPython.itkOffset3_Fill, None, itkOffset3)
itkOffset3.__getitem__ = new_instancemethod(_itkOffsetPython.itkOffset3___getitem__, None, itkOffset3)
itkOffset3.__setitem__ = new_instancemethod(_itkOffsetPython.itkOffset3___setitem__, None, itkOffset3)
itkOffset3.__repr__ = new_instancemethod(_itkOffsetPython.itkOffset3___repr__, None, itkOffset3)
itkOffset3_swigregister = _itkOffsetPython.itkOffset3_swigregister
itkOffset3_swigregister(itkOffset3)

def itkOffset3_GetOffsetDimension() -> "unsigned int":
    """itkOffset3_GetOffsetDimension() -> unsigned int"""
    return _itkOffsetPython.itkOffset3_GetOffsetDimension()

def itkOffset3_GetBasisOffset(dim: 'unsigned int') -> "itkOffset3":
    """itkOffset3_GetBasisOffset(unsigned int dim) -> itkOffset3"""
    return _itkOffsetPython.itkOffset3_GetBasisOffset(dim)

def itkOffset3___len__() -> "unsigned int":
    """itkOffset3___len__() -> unsigned int"""
    return _itkOffsetPython.itkOffset3___len__()

class itkOffset4(object):
    """Proxy of C++ itkOffset4 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def GetOffsetDimension() -> "unsigned int":
        """GetOffsetDimension() -> unsigned int"""
        return _itkOffsetPython.itkOffset4_GetOffsetDimension()

    GetOffsetDimension = staticmethod(GetOffsetDimension)

    def __add__(self, *args) -> "itkOffset4 const":
        """
        __add__(itkOffset4 self, itkOffset4 offset) -> itkOffset4
        __add__(itkOffset4 self, itkSize4 size) -> itkOffset4
        """
        return _itkOffsetPython.itkOffset4___add__(self, *args)


    def __sub__(self, vec: 'itkOffset4') -> "itkOffset4 const":
        """__sub__(itkOffset4 self, itkOffset4 vec) -> itkOffset4"""
        return _itkOffsetPython.itkOffset4___sub__(self, vec)


    def __iadd__(self, *args) -> "itkOffset4 const &":
        """
        __iadd__(itkOffset4 self, itkSize4 size) -> itkOffset4
        __iadd__(itkOffset4 self, itkOffset4 vec) -> itkOffset4
        """
        return _itkOffsetPython.itkOffset4___iadd__(self, *args)


    def __isub__(self, *args) -> "itkOffset4 const &":
        """
        __isub__(itkOffset4 self, itkSize4 size) -> itkOffset4
        __isub__(itkOffset4 self, itkOffset4 vec) -> itkOffset4
        """
        return _itkOffsetPython.itkOffset4___isub__(self, *args)


    def __eq__(self, vec: 'itkOffset4') -> "bool":
        """__eq__(itkOffset4 self, itkOffset4 vec) -> bool"""
        return _itkOffsetPython.itkOffset4___eq__(self, vec)


    def __ne__(self, vec: 'itkOffset4') -> "bool":
        """__ne__(itkOffset4 self, itkOffset4 vec) -> bool"""
        return _itkOffsetPython.itkOffset4___ne__(self, vec)


    def GetOffset(self) -> "long long const *":
        """GetOffset(itkOffset4 self) -> long long const *"""
        return _itkOffsetPython.itkOffset4_GetOffset(self)


    def SetOffset(self, val: 'long long const *') -> "void":
        """SetOffset(itkOffset4 self, long long const * val)"""
        return _itkOffsetPython.itkOffset4_SetOffset(self, val)


    def GetBasisOffset(dim: 'unsigned int') -> "itkOffset4":
        """GetBasisOffset(unsigned int dim) -> itkOffset4"""
        return _itkOffsetPython.itkOffset4_GetBasisOffset(dim)

    GetBasisOffset = staticmethod(GetBasisOffset)

    def Fill(self, value: 'long long') -> "void":
        """Fill(itkOffset4 self, long long value)"""
        return _itkOffsetPython.itkOffset4_Fill(self, value)


    def __init__(self, *args):
        """
        __init__(itkOffset4 self) -> itkOffset4
        __init__(itkOffset4 self, itkOffset4 arg0) -> itkOffset4
        """
        _itkOffsetPython.itkOffset4_swiginit(self, _itkOffsetPython.new_itkOffset4(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset4

    def __getitem__(self, d: 'unsigned long') -> "long":
        """__getitem__(itkOffset4 self, unsigned long d) -> long"""
        return _itkOffsetPython.itkOffset4___getitem__(self, d)


    def __setitem__(self, d: 'unsigned long', v: 'long') -> "void":
        """__setitem__(itkOffset4 self, unsigned long d, long v)"""
        return _itkOffsetPython.itkOffset4___setitem__(self, d, v)


    def __len__() -> "unsigned int":
        """__len__() -> unsigned int"""
        return _itkOffsetPython.itkOffset4___len__()

    __len__ = staticmethod(__len__)

    def __repr__(self) -> "std::string":
        """__repr__(itkOffset4 self) -> std::string"""
        return _itkOffsetPython.itkOffset4___repr__(self)

itkOffset4.__add__ = new_instancemethod(_itkOffsetPython.itkOffset4___add__, None, itkOffset4)
itkOffset4.__sub__ = new_instancemethod(_itkOffsetPython.itkOffset4___sub__, None, itkOffset4)
itkOffset4.__iadd__ = new_instancemethod(_itkOffsetPython.itkOffset4___iadd__, None, itkOffset4)
itkOffset4.__isub__ = new_instancemethod(_itkOffsetPython.itkOffset4___isub__, None, itkOffset4)
itkOffset4.__eq__ = new_instancemethod(_itkOffsetPython.itkOffset4___eq__, None, itkOffset4)
itkOffset4.__ne__ = new_instancemethod(_itkOffsetPython.itkOffset4___ne__, None, itkOffset4)
itkOffset4.GetOffset = new_instancemethod(_itkOffsetPython.itkOffset4_GetOffset, None, itkOffset4)
itkOffset4.SetOffset = new_instancemethod(_itkOffsetPython.itkOffset4_SetOffset, None, itkOffset4)
itkOffset4.Fill = new_instancemethod(_itkOffsetPython.itkOffset4_Fill, None, itkOffset4)
itkOffset4.__getitem__ = new_instancemethod(_itkOffsetPython.itkOffset4___getitem__, None, itkOffset4)
itkOffset4.__setitem__ = new_instancemethod(_itkOffsetPython.itkOffset4___setitem__, None, itkOffset4)
itkOffset4.__repr__ = new_instancemethod(_itkOffsetPython.itkOffset4___repr__, None, itkOffset4)
itkOffset4_swigregister = _itkOffsetPython.itkOffset4_swigregister
itkOffset4_swigregister(itkOffset4)

def itkOffset4_GetOffsetDimension() -> "unsigned int":
    """itkOffset4_GetOffsetDimension() -> unsigned int"""
    return _itkOffsetPython.itkOffset4_GetOffsetDimension()

def itkOffset4_GetBasisOffset(dim: 'unsigned int') -> "itkOffset4":
    """itkOffset4_GetBasisOffset(unsigned int dim) -> itkOffset4"""
    return _itkOffsetPython.itkOffset4_GetBasisOffset(dim)

def itkOffset4___len__() -> "unsigned int":
    """itkOffset4___len__() -> unsigned int"""
    return _itkOffsetPython.itkOffset4___len__()



