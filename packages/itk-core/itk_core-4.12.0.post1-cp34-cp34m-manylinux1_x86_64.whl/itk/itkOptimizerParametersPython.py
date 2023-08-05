# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkOptimizerParametersPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkOptimizerParametersPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkOptimizerParametersPython')
    _itkOptimizerParametersPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkOptimizerParametersPython', [dirname(__file__)])
        except ImportError:
            import _itkOptimizerParametersPython
            return _itkOptimizerParametersPython
        try:
            _mod = imp.load_module('_itkOptimizerParametersPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkOptimizerParametersPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkOptimizerParametersPython
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
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython
import itkArrayPython
class itkOptimizerParametersD(itkArrayPython.itkArrayD):
    """Proxy of C++ itkOptimizerParametersD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkOptimizerParametersD self) -> itkOptimizerParametersD
        __init__(itkOptimizerParametersD self, itkOptimizerParametersD rhs) -> itkOptimizerParametersD
        __init__(itkOptimizerParametersD self, unsigned long dimension) -> itkOptimizerParametersD
        __init__(itkOptimizerParametersD self, itkArrayD array) -> itkOptimizerParametersD
        """
        _itkOptimizerParametersPython.itkOptimizerParametersD_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersD(*args))

    def Initialize(self) -> "void":
        """Initialize(itkOptimizerParametersD self)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersD_Initialize(self)


    def MoveDataPointer(self, pointer: 'double *') -> "void":
        """MoveDataPointer(itkOptimizerParametersD self, double * pointer)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersD_MoveDataPointer(self, pointer)


    def SetParametersObject(self, object: 'itkLightObject') -> "void":
        """SetParametersObject(itkOptimizerParametersD self, itkLightObject object)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersD_SetParametersObject(self, object)


    def SetHelper(self, helper: 'itkOptimizerParametersHelperD') -> "void":
        """SetHelper(itkOptimizerParametersD self, itkOptimizerParametersHelperD helper)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersD_SetHelper(self, helper)


    def GetHelper(self) -> "itkOptimizerParametersHelperD *":
        """GetHelper(itkOptimizerParametersD self) -> itkOptimizerParametersHelperD"""
        return _itkOptimizerParametersPython.itkOptimizerParametersD_GetHelper(self)

    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersD
itkOptimizerParametersD.Initialize = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersD_Initialize, None, itkOptimizerParametersD)
itkOptimizerParametersD.MoveDataPointer = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersD_MoveDataPointer, None, itkOptimizerParametersD)
itkOptimizerParametersD.SetParametersObject = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersD_SetParametersObject, None, itkOptimizerParametersD)
itkOptimizerParametersD.SetHelper = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersD_SetHelper, None, itkOptimizerParametersD)
itkOptimizerParametersD.GetHelper = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersD_GetHelper, None, itkOptimizerParametersD)
itkOptimizerParametersD_swigregister = _itkOptimizerParametersPython.itkOptimizerParametersD_swigregister
itkOptimizerParametersD_swigregister(itkOptimizerParametersD)

class itkOptimizerParametersF(itkArrayPython.itkArrayF):
    """Proxy of C++ itkOptimizerParametersF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkOptimizerParametersF self) -> itkOptimizerParametersF
        __init__(itkOptimizerParametersF self, itkOptimizerParametersF rhs) -> itkOptimizerParametersF
        __init__(itkOptimizerParametersF self, unsigned long dimension) -> itkOptimizerParametersF
        __init__(itkOptimizerParametersF self, itkArrayF array) -> itkOptimizerParametersF
        """
        _itkOptimizerParametersPython.itkOptimizerParametersF_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersF(*args))

    def Initialize(self) -> "void":
        """Initialize(itkOptimizerParametersF self)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersF_Initialize(self)


    def MoveDataPointer(self, pointer: 'float *') -> "void":
        """MoveDataPointer(itkOptimizerParametersF self, float * pointer)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersF_MoveDataPointer(self, pointer)


    def SetParametersObject(self, object: 'itkLightObject') -> "void":
        """SetParametersObject(itkOptimizerParametersF self, itkLightObject object)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersF_SetParametersObject(self, object)


    def SetHelper(self, helper: 'itkOptimizerParametersHelperF') -> "void":
        """SetHelper(itkOptimizerParametersF self, itkOptimizerParametersHelperF helper)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersF_SetHelper(self, helper)


    def GetHelper(self) -> "itkOptimizerParametersHelperF *":
        """GetHelper(itkOptimizerParametersF self) -> itkOptimizerParametersHelperF"""
        return _itkOptimizerParametersPython.itkOptimizerParametersF_GetHelper(self)

    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersF
itkOptimizerParametersF.Initialize = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersF_Initialize, None, itkOptimizerParametersF)
itkOptimizerParametersF.MoveDataPointer = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersF_MoveDataPointer, None, itkOptimizerParametersF)
itkOptimizerParametersF.SetParametersObject = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersF_SetParametersObject, None, itkOptimizerParametersF)
itkOptimizerParametersF.SetHelper = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersF_SetHelper, None, itkOptimizerParametersF)
itkOptimizerParametersF.GetHelper = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersF_GetHelper, None, itkOptimizerParametersF)
itkOptimizerParametersF_swigregister = _itkOptimizerParametersPython.itkOptimizerParametersF_swigregister
itkOptimizerParametersF_swigregister(itkOptimizerParametersF)

class itkOptimizerParametersHelperD(object):
    """Proxy of C++ itkOptimizerParametersHelperD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def MoveDataPointer(self, container: 'itkArrayD', pointer: 'double *') -> "void":
        """MoveDataPointer(itkOptimizerParametersHelperD self, itkArrayD container, double * pointer)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersHelperD_MoveDataPointer(self, container, pointer)


    def SetParametersObject(self, arg0: 'itkArrayD', arg1: 'itkLightObject') -> "void":
        """SetParametersObject(itkOptimizerParametersHelperD self, itkArrayD arg0, itkLightObject arg1)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersHelperD_SetParametersObject(self, arg0, arg1)

    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersHelperD

    def __init__(self, *args):
        """
        __init__(itkOptimizerParametersHelperD self) -> itkOptimizerParametersHelperD
        __init__(itkOptimizerParametersHelperD self, itkOptimizerParametersHelperD arg0) -> itkOptimizerParametersHelperD
        """
        _itkOptimizerParametersPython.itkOptimizerParametersHelperD_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersHelperD(*args))
itkOptimizerParametersHelperD.MoveDataPointer = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersHelperD_MoveDataPointer, None, itkOptimizerParametersHelperD)
itkOptimizerParametersHelperD.SetParametersObject = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersHelperD_SetParametersObject, None, itkOptimizerParametersHelperD)
itkOptimizerParametersHelperD_swigregister = _itkOptimizerParametersPython.itkOptimizerParametersHelperD_swigregister
itkOptimizerParametersHelperD_swigregister(itkOptimizerParametersHelperD)

class itkOptimizerParametersHelperF(object):
    """Proxy of C++ itkOptimizerParametersHelperF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def MoveDataPointer(self, container: 'itkArrayF', pointer: 'float *') -> "void":
        """MoveDataPointer(itkOptimizerParametersHelperF self, itkArrayF container, float * pointer)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersHelperF_MoveDataPointer(self, container, pointer)


    def SetParametersObject(self, arg0: 'itkArrayF', arg1: 'itkLightObject') -> "void":
        """SetParametersObject(itkOptimizerParametersHelperF self, itkArrayF arg0, itkLightObject arg1)"""
        return _itkOptimizerParametersPython.itkOptimizerParametersHelperF_SetParametersObject(self, arg0, arg1)

    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersHelperF

    def __init__(self, *args):
        """
        __init__(itkOptimizerParametersHelperF self) -> itkOptimizerParametersHelperF
        __init__(itkOptimizerParametersHelperF self, itkOptimizerParametersHelperF arg0) -> itkOptimizerParametersHelperF
        """
        _itkOptimizerParametersPython.itkOptimizerParametersHelperF_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersHelperF(*args))
itkOptimizerParametersHelperF.MoveDataPointer = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersHelperF_MoveDataPointer, None, itkOptimizerParametersHelperF)
itkOptimizerParametersHelperF.SetParametersObject = new_instancemethod(_itkOptimizerParametersPython.itkOptimizerParametersHelperF_SetParametersObject, None, itkOptimizerParametersHelperF)
itkOptimizerParametersHelperF_swigregister = _itkOptimizerParametersPython.itkOptimizerParametersHelperF_swigregister
itkOptimizerParametersHelperF_swigregister(itkOptimizerParametersHelperF)



