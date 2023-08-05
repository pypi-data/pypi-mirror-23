# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDefaultDynamicMeshTraitsPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkDefaultDynamicMeshTraitsPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkDefaultDynamicMeshTraitsPython')
    _itkDefaultDynamicMeshTraitsPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDefaultDynamicMeshTraitsPython', [dirname(__file__)])
        except ImportError:
            import _itkDefaultDynamicMeshTraitsPython
            return _itkDefaultDynamicMeshTraitsPython
        try:
            _mod = imp.load_module('_itkDefaultDynamicMeshTraitsPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkDefaultDynamicMeshTraitsPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDefaultDynamicMeshTraitsPython
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


import pyBasePython
class itkDefaultDynamicMeshTraitsD22D(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD22D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD22D self) -> itkDefaultDynamicMeshTraitsD22D
        __init__(itkDefaultDynamicMeshTraitsD22D self, itkDefaultDynamicMeshTraitsD22D arg0) -> itkDefaultDynamicMeshTraitsD22D
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22D_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD22D(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD22D
itkDefaultDynamicMeshTraitsD22D_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22D_swigregister
itkDefaultDynamicMeshTraitsD22D_swigregister(itkDefaultDynamicMeshTraitsD22D)

class itkDefaultDynamicMeshTraitsD22DD(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD22DD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD22DD self) -> itkDefaultDynamicMeshTraitsD22DD
        __init__(itkDefaultDynamicMeshTraitsD22DD self, itkDefaultDynamicMeshTraitsD22DD arg0) -> itkDefaultDynamicMeshTraitsD22DD
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22DD_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD22DD(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD22DD
itkDefaultDynamicMeshTraitsD22DD_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22DD_swigregister
itkDefaultDynamicMeshTraitsD22DD_swigregister(itkDefaultDynamicMeshTraitsD22DD)

class itkDefaultDynamicMeshTraitsD22DDD(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD22DDD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD22DDD self) -> itkDefaultDynamicMeshTraitsD22DDD
        __init__(itkDefaultDynamicMeshTraitsD22DDD self, itkDefaultDynamicMeshTraitsD22DD arg0) -> itkDefaultDynamicMeshTraitsD22DDD
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22DDD_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD22DDD(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD22DDD
itkDefaultDynamicMeshTraitsD22DDD_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22DDD_swigregister
itkDefaultDynamicMeshTraitsD22DDD_swigregister(itkDefaultDynamicMeshTraitsD22DDD)

class itkDefaultDynamicMeshTraitsD22DFD(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD22DFD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD22DFD self) -> itkDefaultDynamicMeshTraitsD22DFD
        __init__(itkDefaultDynamicMeshTraitsD22DFD self, itkDefaultDynamicMeshTraitsD22D arg0) -> itkDefaultDynamicMeshTraitsD22DFD
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22DFD_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD22DFD(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD22DFD
itkDefaultDynamicMeshTraitsD22DFD_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD22DFD_swigregister
itkDefaultDynamicMeshTraitsD22DFD_swigregister(itkDefaultDynamicMeshTraitsD22DFD)

class itkDefaultDynamicMeshTraitsD33D(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD33D class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD33D self) -> itkDefaultDynamicMeshTraitsD33D
        __init__(itkDefaultDynamicMeshTraitsD33D self, itkDefaultDynamicMeshTraitsD33D arg0) -> itkDefaultDynamicMeshTraitsD33D
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33D_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD33D(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD33D
itkDefaultDynamicMeshTraitsD33D_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33D_swigregister
itkDefaultDynamicMeshTraitsD33D_swigregister(itkDefaultDynamicMeshTraitsD33D)

class itkDefaultDynamicMeshTraitsD33DD(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD33DD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD33DD self) -> itkDefaultDynamicMeshTraitsD33DD
        __init__(itkDefaultDynamicMeshTraitsD33DD self, itkDefaultDynamicMeshTraitsD33DD arg0) -> itkDefaultDynamicMeshTraitsD33DD
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33DD_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD33DD(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD33DD
itkDefaultDynamicMeshTraitsD33DD_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33DD_swigregister
itkDefaultDynamicMeshTraitsD33DD_swigregister(itkDefaultDynamicMeshTraitsD33DD)

class itkDefaultDynamicMeshTraitsD33DDD(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD33DDD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD33DDD self) -> itkDefaultDynamicMeshTraitsD33DDD
        __init__(itkDefaultDynamicMeshTraitsD33DDD self, itkDefaultDynamicMeshTraitsD33DD arg0) -> itkDefaultDynamicMeshTraitsD33DDD
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33DDD_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD33DDD(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD33DDD
itkDefaultDynamicMeshTraitsD33DDD_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33DDD_swigregister
itkDefaultDynamicMeshTraitsD33DDD_swigregister(itkDefaultDynamicMeshTraitsD33DDD)

class itkDefaultDynamicMeshTraitsD33DFD(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsD33DFD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsD33DFD self) -> itkDefaultDynamicMeshTraitsD33DFD
        __init__(itkDefaultDynamicMeshTraitsD33DFD self, itkDefaultDynamicMeshTraitsD33D arg0) -> itkDefaultDynamicMeshTraitsD33DFD
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33DFD_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsD33DFD(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsD33DFD
itkDefaultDynamicMeshTraitsD33DFD_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsD33DFD_swigregister
itkDefaultDynamicMeshTraitsD33DFD_swigregister(itkDefaultDynamicMeshTraitsD33DFD)

class itkDefaultDynamicMeshTraitsF22F(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsF22F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsF22F self) -> itkDefaultDynamicMeshTraitsF22F
        __init__(itkDefaultDynamicMeshTraitsF22F self, itkDefaultDynamicMeshTraitsF22F arg0) -> itkDefaultDynamicMeshTraitsF22F
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF22F_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsF22F(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsF22F
itkDefaultDynamicMeshTraitsF22F_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF22F_swigregister
itkDefaultDynamicMeshTraitsF22F_swigregister(itkDefaultDynamicMeshTraitsF22F)

class itkDefaultDynamicMeshTraitsF22FF(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsF22FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsF22FF self) -> itkDefaultDynamicMeshTraitsF22FF
        __init__(itkDefaultDynamicMeshTraitsF22FF self, itkDefaultDynamicMeshTraitsF22F arg0) -> itkDefaultDynamicMeshTraitsF22FF
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF22FF_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsF22FF(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsF22FF
itkDefaultDynamicMeshTraitsF22FF_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF22FF_swigregister
itkDefaultDynamicMeshTraitsF22FF_swigregister(itkDefaultDynamicMeshTraitsF22FF)

class itkDefaultDynamicMeshTraitsF22FFF(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsF22FFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsF22FFF self) -> itkDefaultDynamicMeshTraitsF22FFF
        __init__(itkDefaultDynamicMeshTraitsF22FFF self, itkDefaultDynamicMeshTraitsF22F arg0) -> itkDefaultDynamicMeshTraitsF22FFF
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF22FFF_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsF22FFF(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsF22FFF
itkDefaultDynamicMeshTraitsF22FFF_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF22FFF_swigregister
itkDefaultDynamicMeshTraitsF22FFF_swigregister(itkDefaultDynamicMeshTraitsF22FFF)

class itkDefaultDynamicMeshTraitsF33F(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsF33F class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsF33F self) -> itkDefaultDynamicMeshTraitsF33F
        __init__(itkDefaultDynamicMeshTraitsF33F self, itkDefaultDynamicMeshTraitsF33F arg0) -> itkDefaultDynamicMeshTraitsF33F
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF33F_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsF33F(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsF33F
itkDefaultDynamicMeshTraitsF33F_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF33F_swigregister
itkDefaultDynamicMeshTraitsF33F_swigregister(itkDefaultDynamicMeshTraitsF33F)

class itkDefaultDynamicMeshTraitsF33FF(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsF33FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsF33FF self) -> itkDefaultDynamicMeshTraitsF33FF
        __init__(itkDefaultDynamicMeshTraitsF33FF self, itkDefaultDynamicMeshTraitsF33F arg0) -> itkDefaultDynamicMeshTraitsF33FF
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF33FF_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsF33FF(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsF33FF
itkDefaultDynamicMeshTraitsF33FF_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF33FF_swigregister
itkDefaultDynamicMeshTraitsF33FF_swigregister(itkDefaultDynamicMeshTraitsF33FF)

class itkDefaultDynamicMeshTraitsF33FFF(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsF33FFF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsF33FFF self) -> itkDefaultDynamicMeshTraitsF33FFF
        __init__(itkDefaultDynamicMeshTraitsF33FFF self, itkDefaultDynamicMeshTraitsF33F arg0) -> itkDefaultDynamicMeshTraitsF33FFF
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF33FFF_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsF33FFF(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsF33FFF
itkDefaultDynamicMeshTraitsF33FFF_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsF33FFF_swigregister
itkDefaultDynamicMeshTraitsF33FFF_swigregister(itkDefaultDynamicMeshTraitsF33FFF)

class itkDefaultDynamicMeshTraitsMD2222FFMD22(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsMD2222FFMD22 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsMD2222FFMD22 self) -> itkDefaultDynamicMeshTraitsMD2222FFMD22
        __init__(itkDefaultDynamicMeshTraitsMD2222FFMD22 self, itkDefaultDynamicMeshTraitsMD2222FFMD22 arg0) -> itkDefaultDynamicMeshTraitsMD2222FFMD22
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsMD2222FFMD22_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsMD2222FFMD22(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsMD2222FFMD22
itkDefaultDynamicMeshTraitsMD2222FFMD22_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsMD2222FFMD22_swigregister
itkDefaultDynamicMeshTraitsMD2222FFMD22_swigregister(itkDefaultDynamicMeshTraitsMD2222FFMD22)

class itkDefaultDynamicMeshTraitsMD3333FFMD33(object):
    """Proxy of C++ itkDefaultDynamicMeshTraitsMD3333FFMD33 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkDefaultDynamicMeshTraitsMD3333FFMD33 self) -> itkDefaultDynamicMeshTraitsMD3333FFMD33
        __init__(itkDefaultDynamicMeshTraitsMD3333FFMD33 self, itkDefaultDynamicMeshTraitsMD3333FFMD33 arg0) -> itkDefaultDynamicMeshTraitsMD3333FFMD33
        """
        _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsMD3333FFMD33_swiginit(self, _itkDefaultDynamicMeshTraitsPython.new_itkDefaultDynamicMeshTraitsMD3333FFMD33(*args))
    __swig_destroy__ = _itkDefaultDynamicMeshTraitsPython.delete_itkDefaultDynamicMeshTraitsMD3333FFMD33
itkDefaultDynamicMeshTraitsMD3333FFMD33_swigregister = _itkDefaultDynamicMeshTraitsPython.itkDefaultDynamicMeshTraitsMD3333FFMD33_swigregister
itkDefaultDynamicMeshTraitsMD3333FFMD33_swigregister(itkDefaultDynamicMeshTraitsMD3333FFMD33)



