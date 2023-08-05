# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkArrayPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkArrayPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkArrayPython')
    _itkArrayPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkArrayPython', [dirname(__file__)])
        except ImportError:
            import _itkArrayPython
            return _itkArrayPython
        try:
            _mod = imp.load_module('_itkArrayPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkArrayPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkArrayPython
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
class itkArrayD(vnl_vectorPython.vnl_vectorD):
    """Proxy of C++ itkArrayD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkArrayD self) -> itkArrayD
        __init__(itkArrayD self, itkArrayD arg0) -> itkArrayD
        __init__(itkArrayD self, unsigned long dimension) -> itkArrayD
        __init__(itkArrayD self, double * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayD
        __init__(itkArrayD self, double * data, unsigned long sz) -> itkArrayD
        __init__(itkArrayD self, double const * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayD
        __init__(itkArrayD self, double const * data, unsigned long sz) -> itkArrayD
        """
        _itkArrayPython.itkArrayD_swiginit(self, _itkArrayPython.new_itkArrayD(*args))

    def Fill(self, v: 'double const &') -> "void":
        """Fill(itkArrayD self, double const & v)"""
        return _itkArrayPython.itkArrayD_Fill(self, v)


    def Size(self) -> "unsigned long":
        """Size(itkArrayD self) -> unsigned long"""
        return _itkArrayPython.itkArrayD_Size(self)


    def GetNumberOfElements(self) -> "unsigned int":
        """GetNumberOfElements(itkArrayD self) -> unsigned int"""
        return _itkArrayPython.itkArrayD_GetNumberOfElements(self)


    def GetElement(self, i: 'unsigned long') -> "double const &":
        """GetElement(itkArrayD self, unsigned long i) -> double const &"""
        return _itkArrayPython.itkArrayD_GetElement(self, i)


    def SetElement(self, i: 'unsigned long', value: 'double const &') -> "void":
        """SetElement(itkArrayD self, unsigned long i, double const & value)"""
        return _itkArrayPython.itkArrayD_SetElement(self, i, value)


    def SetSize(self, sz: 'unsigned long') -> "void":
        """SetSize(itkArrayD self, unsigned long sz)"""
        return _itkArrayPython.itkArrayD_SetSize(self, sz)


    def GetSize(self) -> "unsigned long":
        """GetSize(itkArrayD self) -> unsigned long"""
        return _itkArrayPython.itkArrayD_GetSize(self)


    def SetDataSameSize(self, data: 'double *', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetDataSameSize(itkArrayD self, double * data, bool LetArrayManageMemory=False)
        SetDataSameSize(itkArrayD self, double * data)
        """
        return _itkArrayPython.itkArrayD_SetDataSameSize(self, data, LetArrayManageMemory)


    def SetData(self, data: 'double *', sz: 'unsigned long', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetData(itkArrayD self, double * data, unsigned long sz, bool LetArrayManageMemory=False)
        SetData(itkArrayD self, double * data, unsigned long sz)
        """
        return _itkArrayPython.itkArrayD_SetData(self, data, sz, LetArrayManageMemory)

    __swig_destroy__ = _itkArrayPython.delete_itkArrayD

    def swap(self, other: 'itkArrayD') -> "void":
        """swap(itkArrayD self, itkArrayD other)"""
        return _itkArrayPython.itkArrayD_swap(self, other)


    def Swap(self, other: 'itkArrayD') -> "void":
        """Swap(itkArrayD self, itkArrayD other)"""
        return _itkArrayPython.itkArrayD_Swap(self, other)


    def __getitem__(self, dim: 'unsigned long') -> "double":
        """__getitem__(itkArrayD self, unsigned long dim) -> double"""
        return _itkArrayPython.itkArrayD___getitem__(self, dim)


    def __setitem__(self, dim: 'unsigned long', v: 'double') -> "void":
        """__setitem__(itkArrayD self, unsigned long dim, double v)"""
        return _itkArrayPython.itkArrayD___setitem__(self, dim, v)


    def __len__(self) -> "unsigned int":
        """__len__(itkArrayD self) -> unsigned int"""
        return _itkArrayPython.itkArrayD___len__(self)


    def __repr__(self) -> "std::string":
        """__repr__(itkArrayD self) -> std::string"""
        return _itkArrayPython.itkArrayD___repr__(self)

itkArrayD.Fill = new_instancemethod(_itkArrayPython.itkArrayD_Fill, None, itkArrayD)
itkArrayD.Size = new_instancemethod(_itkArrayPython.itkArrayD_Size, None, itkArrayD)
itkArrayD.GetNumberOfElements = new_instancemethod(_itkArrayPython.itkArrayD_GetNumberOfElements, None, itkArrayD)
itkArrayD.GetElement = new_instancemethod(_itkArrayPython.itkArrayD_GetElement, None, itkArrayD)
itkArrayD.SetElement = new_instancemethod(_itkArrayPython.itkArrayD_SetElement, None, itkArrayD)
itkArrayD.SetSize = new_instancemethod(_itkArrayPython.itkArrayD_SetSize, None, itkArrayD)
itkArrayD.GetSize = new_instancemethod(_itkArrayPython.itkArrayD_GetSize, None, itkArrayD)
itkArrayD.SetDataSameSize = new_instancemethod(_itkArrayPython.itkArrayD_SetDataSameSize, None, itkArrayD)
itkArrayD.SetData = new_instancemethod(_itkArrayPython.itkArrayD_SetData, None, itkArrayD)
itkArrayD.swap = new_instancemethod(_itkArrayPython.itkArrayD_swap, None, itkArrayD)
itkArrayD.Swap = new_instancemethod(_itkArrayPython.itkArrayD_Swap, None, itkArrayD)
itkArrayD.__getitem__ = new_instancemethod(_itkArrayPython.itkArrayD___getitem__, None, itkArrayD)
itkArrayD.__setitem__ = new_instancemethod(_itkArrayPython.itkArrayD___setitem__, None, itkArrayD)
itkArrayD.__len__ = new_instancemethod(_itkArrayPython.itkArrayD___len__, None, itkArrayD)
itkArrayD.__repr__ = new_instancemethod(_itkArrayPython.itkArrayD___repr__, None, itkArrayD)
itkArrayD_swigregister = _itkArrayPython.itkArrayD_swigregister
itkArrayD_swigregister(itkArrayD)

class itkArrayF(vnl_vectorPython.vnl_vectorF):
    """Proxy of C++ itkArrayF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkArrayF self) -> itkArrayF
        __init__(itkArrayF self, itkArrayF arg0) -> itkArrayF
        __init__(itkArrayF self, unsigned long dimension) -> itkArrayF
        __init__(itkArrayF self, float * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayF
        __init__(itkArrayF self, float * data, unsigned long sz) -> itkArrayF
        __init__(itkArrayF self, float const * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayF
        __init__(itkArrayF self, float const * data, unsigned long sz) -> itkArrayF
        """
        _itkArrayPython.itkArrayF_swiginit(self, _itkArrayPython.new_itkArrayF(*args))

    def Fill(self, v: 'float const &') -> "void":
        """Fill(itkArrayF self, float const & v)"""
        return _itkArrayPython.itkArrayF_Fill(self, v)


    def Size(self) -> "unsigned long":
        """Size(itkArrayF self) -> unsigned long"""
        return _itkArrayPython.itkArrayF_Size(self)


    def GetNumberOfElements(self) -> "unsigned int":
        """GetNumberOfElements(itkArrayF self) -> unsigned int"""
        return _itkArrayPython.itkArrayF_GetNumberOfElements(self)


    def GetElement(self, i: 'unsigned long') -> "float const &":
        """GetElement(itkArrayF self, unsigned long i) -> float const &"""
        return _itkArrayPython.itkArrayF_GetElement(self, i)


    def SetElement(self, i: 'unsigned long', value: 'float const &') -> "void":
        """SetElement(itkArrayF self, unsigned long i, float const & value)"""
        return _itkArrayPython.itkArrayF_SetElement(self, i, value)


    def SetSize(self, sz: 'unsigned long') -> "void":
        """SetSize(itkArrayF self, unsigned long sz)"""
        return _itkArrayPython.itkArrayF_SetSize(self, sz)


    def GetSize(self) -> "unsigned long":
        """GetSize(itkArrayF self) -> unsigned long"""
        return _itkArrayPython.itkArrayF_GetSize(self)


    def SetDataSameSize(self, data: 'float *', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetDataSameSize(itkArrayF self, float * data, bool LetArrayManageMemory=False)
        SetDataSameSize(itkArrayF self, float * data)
        """
        return _itkArrayPython.itkArrayF_SetDataSameSize(self, data, LetArrayManageMemory)


    def SetData(self, data: 'float *', sz: 'unsigned long', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetData(itkArrayF self, float * data, unsigned long sz, bool LetArrayManageMemory=False)
        SetData(itkArrayF self, float * data, unsigned long sz)
        """
        return _itkArrayPython.itkArrayF_SetData(self, data, sz, LetArrayManageMemory)

    __swig_destroy__ = _itkArrayPython.delete_itkArrayF

    def swap(self, other: 'itkArrayF') -> "void":
        """swap(itkArrayF self, itkArrayF other)"""
        return _itkArrayPython.itkArrayF_swap(self, other)


    def Swap(self, other: 'itkArrayF') -> "void":
        """Swap(itkArrayF self, itkArrayF other)"""
        return _itkArrayPython.itkArrayF_Swap(self, other)


    def __getitem__(self, dim: 'unsigned long') -> "float":
        """__getitem__(itkArrayF self, unsigned long dim) -> float"""
        return _itkArrayPython.itkArrayF___getitem__(self, dim)


    def __setitem__(self, dim: 'unsigned long', v: 'float') -> "void":
        """__setitem__(itkArrayF self, unsigned long dim, float v)"""
        return _itkArrayPython.itkArrayF___setitem__(self, dim, v)


    def __len__(self) -> "unsigned int":
        """__len__(itkArrayF self) -> unsigned int"""
        return _itkArrayPython.itkArrayF___len__(self)


    def __repr__(self) -> "std::string":
        """__repr__(itkArrayF self) -> std::string"""
        return _itkArrayPython.itkArrayF___repr__(self)

itkArrayF.Fill = new_instancemethod(_itkArrayPython.itkArrayF_Fill, None, itkArrayF)
itkArrayF.Size = new_instancemethod(_itkArrayPython.itkArrayF_Size, None, itkArrayF)
itkArrayF.GetNumberOfElements = new_instancemethod(_itkArrayPython.itkArrayF_GetNumberOfElements, None, itkArrayF)
itkArrayF.GetElement = new_instancemethod(_itkArrayPython.itkArrayF_GetElement, None, itkArrayF)
itkArrayF.SetElement = new_instancemethod(_itkArrayPython.itkArrayF_SetElement, None, itkArrayF)
itkArrayF.SetSize = new_instancemethod(_itkArrayPython.itkArrayF_SetSize, None, itkArrayF)
itkArrayF.GetSize = new_instancemethod(_itkArrayPython.itkArrayF_GetSize, None, itkArrayF)
itkArrayF.SetDataSameSize = new_instancemethod(_itkArrayPython.itkArrayF_SetDataSameSize, None, itkArrayF)
itkArrayF.SetData = new_instancemethod(_itkArrayPython.itkArrayF_SetData, None, itkArrayF)
itkArrayF.swap = new_instancemethod(_itkArrayPython.itkArrayF_swap, None, itkArrayF)
itkArrayF.Swap = new_instancemethod(_itkArrayPython.itkArrayF_Swap, None, itkArrayF)
itkArrayF.__getitem__ = new_instancemethod(_itkArrayPython.itkArrayF___getitem__, None, itkArrayF)
itkArrayF.__setitem__ = new_instancemethod(_itkArrayPython.itkArrayF___setitem__, None, itkArrayF)
itkArrayF.__len__ = new_instancemethod(_itkArrayPython.itkArrayF___len__, None, itkArrayF)
itkArrayF.__repr__ = new_instancemethod(_itkArrayPython.itkArrayF___repr__, None, itkArrayF)
itkArrayF_swigregister = _itkArrayPython.itkArrayF_swigregister
itkArrayF_swigregister(itkArrayF)

class itkArraySL(vnl_vectorPython.vnl_vectorSL):
    """Proxy of C++ itkArraySL class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkArraySL self) -> itkArraySL
        __init__(itkArraySL self, itkArraySL arg0) -> itkArraySL
        __init__(itkArraySL self, unsigned long dimension) -> itkArraySL
        __init__(itkArraySL self, long * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArraySL
        __init__(itkArraySL self, long * data, unsigned long sz) -> itkArraySL
        __init__(itkArraySL self, long const * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArraySL
        __init__(itkArraySL self, long const * data, unsigned long sz) -> itkArraySL
        """
        _itkArrayPython.itkArraySL_swiginit(self, _itkArrayPython.new_itkArraySL(*args))

    def Fill(self, v: 'long const &') -> "void":
        """Fill(itkArraySL self, long const & v)"""
        return _itkArrayPython.itkArraySL_Fill(self, v)


    def Size(self) -> "unsigned long":
        """Size(itkArraySL self) -> unsigned long"""
        return _itkArrayPython.itkArraySL_Size(self)


    def GetNumberOfElements(self) -> "unsigned int":
        """GetNumberOfElements(itkArraySL self) -> unsigned int"""
        return _itkArrayPython.itkArraySL_GetNumberOfElements(self)


    def GetElement(self, i: 'unsigned long') -> "long const &":
        """GetElement(itkArraySL self, unsigned long i) -> long const &"""
        return _itkArrayPython.itkArraySL_GetElement(self, i)


    def SetElement(self, i: 'unsigned long', value: 'long const &') -> "void":
        """SetElement(itkArraySL self, unsigned long i, long const & value)"""
        return _itkArrayPython.itkArraySL_SetElement(self, i, value)


    def SetSize(self, sz: 'unsigned long') -> "void":
        """SetSize(itkArraySL self, unsigned long sz)"""
        return _itkArrayPython.itkArraySL_SetSize(self, sz)


    def GetSize(self) -> "unsigned long":
        """GetSize(itkArraySL self) -> unsigned long"""
        return _itkArrayPython.itkArraySL_GetSize(self)


    def SetDataSameSize(self, data: 'long *', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetDataSameSize(itkArraySL self, long * data, bool LetArrayManageMemory=False)
        SetDataSameSize(itkArraySL self, long * data)
        """
        return _itkArrayPython.itkArraySL_SetDataSameSize(self, data, LetArrayManageMemory)


    def SetData(self, data: 'long *', sz: 'unsigned long', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetData(itkArraySL self, long * data, unsigned long sz, bool LetArrayManageMemory=False)
        SetData(itkArraySL self, long * data, unsigned long sz)
        """
        return _itkArrayPython.itkArraySL_SetData(self, data, sz, LetArrayManageMemory)

    __swig_destroy__ = _itkArrayPython.delete_itkArraySL

    def swap(self, other: 'itkArraySL') -> "void":
        """swap(itkArraySL self, itkArraySL other)"""
        return _itkArrayPython.itkArraySL_swap(self, other)


    def Swap(self, other: 'itkArraySL') -> "void":
        """Swap(itkArraySL self, itkArraySL other)"""
        return _itkArrayPython.itkArraySL_Swap(self, other)


    def __getitem__(self, dim: 'unsigned long') -> "long":
        """__getitem__(itkArraySL self, unsigned long dim) -> long"""
        return _itkArrayPython.itkArraySL___getitem__(self, dim)


    def __setitem__(self, dim: 'unsigned long', v: 'long') -> "void":
        """__setitem__(itkArraySL self, unsigned long dim, long v)"""
        return _itkArrayPython.itkArraySL___setitem__(self, dim, v)


    def __len__(self) -> "unsigned int":
        """__len__(itkArraySL self) -> unsigned int"""
        return _itkArrayPython.itkArraySL___len__(self)


    def __repr__(self) -> "std::string":
        """__repr__(itkArraySL self) -> std::string"""
        return _itkArrayPython.itkArraySL___repr__(self)

itkArraySL.Fill = new_instancemethod(_itkArrayPython.itkArraySL_Fill, None, itkArraySL)
itkArraySL.Size = new_instancemethod(_itkArrayPython.itkArraySL_Size, None, itkArraySL)
itkArraySL.GetNumberOfElements = new_instancemethod(_itkArrayPython.itkArraySL_GetNumberOfElements, None, itkArraySL)
itkArraySL.GetElement = new_instancemethod(_itkArrayPython.itkArraySL_GetElement, None, itkArraySL)
itkArraySL.SetElement = new_instancemethod(_itkArrayPython.itkArraySL_SetElement, None, itkArraySL)
itkArraySL.SetSize = new_instancemethod(_itkArrayPython.itkArraySL_SetSize, None, itkArraySL)
itkArraySL.GetSize = new_instancemethod(_itkArrayPython.itkArraySL_GetSize, None, itkArraySL)
itkArraySL.SetDataSameSize = new_instancemethod(_itkArrayPython.itkArraySL_SetDataSameSize, None, itkArraySL)
itkArraySL.SetData = new_instancemethod(_itkArrayPython.itkArraySL_SetData, None, itkArraySL)
itkArraySL.swap = new_instancemethod(_itkArrayPython.itkArraySL_swap, None, itkArraySL)
itkArraySL.Swap = new_instancemethod(_itkArrayPython.itkArraySL_Swap, None, itkArraySL)
itkArraySL.__getitem__ = new_instancemethod(_itkArrayPython.itkArraySL___getitem__, None, itkArraySL)
itkArraySL.__setitem__ = new_instancemethod(_itkArrayPython.itkArraySL___setitem__, None, itkArraySL)
itkArraySL.__len__ = new_instancemethod(_itkArrayPython.itkArraySL___len__, None, itkArraySL)
itkArraySL.__repr__ = new_instancemethod(_itkArrayPython.itkArraySL___repr__, None, itkArraySL)
itkArraySL_swigregister = _itkArrayPython.itkArraySL_swigregister
itkArraySL_swigregister(itkArraySL)

class itkArrayUI(vnl_vectorPython.vnl_vectorUI):
    """Proxy of C++ itkArrayUI class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkArrayUI self) -> itkArrayUI
        __init__(itkArrayUI self, itkArrayUI arg0) -> itkArrayUI
        __init__(itkArrayUI self, unsigned long dimension) -> itkArrayUI
        __init__(itkArrayUI self, unsigned int * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayUI
        __init__(itkArrayUI self, unsigned int * data, unsigned long sz) -> itkArrayUI
        __init__(itkArrayUI self, unsigned int const * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayUI
        __init__(itkArrayUI self, unsigned int const * data, unsigned long sz) -> itkArrayUI
        """
        _itkArrayPython.itkArrayUI_swiginit(self, _itkArrayPython.new_itkArrayUI(*args))

    def Fill(self, v: 'unsigned int const &') -> "void":
        """Fill(itkArrayUI self, unsigned int const & v)"""
        return _itkArrayPython.itkArrayUI_Fill(self, v)


    def Size(self) -> "unsigned long":
        """Size(itkArrayUI self) -> unsigned long"""
        return _itkArrayPython.itkArrayUI_Size(self)


    def GetNumberOfElements(self) -> "unsigned int":
        """GetNumberOfElements(itkArrayUI self) -> unsigned int"""
        return _itkArrayPython.itkArrayUI_GetNumberOfElements(self)


    def GetElement(self, i: 'unsigned long') -> "unsigned int const &":
        """GetElement(itkArrayUI self, unsigned long i) -> unsigned int const &"""
        return _itkArrayPython.itkArrayUI_GetElement(self, i)


    def SetElement(self, i: 'unsigned long', value: 'unsigned int const &') -> "void":
        """SetElement(itkArrayUI self, unsigned long i, unsigned int const & value)"""
        return _itkArrayPython.itkArrayUI_SetElement(self, i, value)


    def SetSize(self, sz: 'unsigned long') -> "void":
        """SetSize(itkArrayUI self, unsigned long sz)"""
        return _itkArrayPython.itkArrayUI_SetSize(self, sz)


    def GetSize(self) -> "unsigned long":
        """GetSize(itkArrayUI self) -> unsigned long"""
        return _itkArrayPython.itkArrayUI_GetSize(self)


    def SetDataSameSize(self, data: 'unsigned int *', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetDataSameSize(itkArrayUI self, unsigned int * data, bool LetArrayManageMemory=False)
        SetDataSameSize(itkArrayUI self, unsigned int * data)
        """
        return _itkArrayPython.itkArrayUI_SetDataSameSize(self, data, LetArrayManageMemory)


    def SetData(self, data: 'unsigned int *', sz: 'unsigned long', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetData(itkArrayUI self, unsigned int * data, unsigned long sz, bool LetArrayManageMemory=False)
        SetData(itkArrayUI self, unsigned int * data, unsigned long sz)
        """
        return _itkArrayPython.itkArrayUI_SetData(self, data, sz, LetArrayManageMemory)

    __swig_destroy__ = _itkArrayPython.delete_itkArrayUI

    def swap(self, other: 'itkArrayUI') -> "void":
        """swap(itkArrayUI self, itkArrayUI other)"""
        return _itkArrayPython.itkArrayUI_swap(self, other)


    def Swap(self, other: 'itkArrayUI') -> "void":
        """Swap(itkArrayUI self, itkArrayUI other)"""
        return _itkArrayPython.itkArrayUI_Swap(self, other)


    def __getitem__(self, dim: 'unsigned long') -> "unsigned int":
        """__getitem__(itkArrayUI self, unsigned long dim) -> unsigned int"""
        return _itkArrayPython.itkArrayUI___getitem__(self, dim)


    def __setitem__(self, dim: 'unsigned long', v: 'unsigned int') -> "void":
        """__setitem__(itkArrayUI self, unsigned long dim, unsigned int v)"""
        return _itkArrayPython.itkArrayUI___setitem__(self, dim, v)


    def __len__(self) -> "unsigned int":
        """__len__(itkArrayUI self) -> unsigned int"""
        return _itkArrayPython.itkArrayUI___len__(self)


    def __repr__(self) -> "std::string":
        """__repr__(itkArrayUI self) -> std::string"""
        return _itkArrayPython.itkArrayUI___repr__(self)

itkArrayUI.Fill = new_instancemethod(_itkArrayPython.itkArrayUI_Fill, None, itkArrayUI)
itkArrayUI.Size = new_instancemethod(_itkArrayPython.itkArrayUI_Size, None, itkArrayUI)
itkArrayUI.GetNumberOfElements = new_instancemethod(_itkArrayPython.itkArrayUI_GetNumberOfElements, None, itkArrayUI)
itkArrayUI.GetElement = new_instancemethod(_itkArrayPython.itkArrayUI_GetElement, None, itkArrayUI)
itkArrayUI.SetElement = new_instancemethod(_itkArrayPython.itkArrayUI_SetElement, None, itkArrayUI)
itkArrayUI.SetSize = new_instancemethod(_itkArrayPython.itkArrayUI_SetSize, None, itkArrayUI)
itkArrayUI.GetSize = new_instancemethod(_itkArrayPython.itkArrayUI_GetSize, None, itkArrayUI)
itkArrayUI.SetDataSameSize = new_instancemethod(_itkArrayPython.itkArrayUI_SetDataSameSize, None, itkArrayUI)
itkArrayUI.SetData = new_instancemethod(_itkArrayPython.itkArrayUI_SetData, None, itkArrayUI)
itkArrayUI.swap = new_instancemethod(_itkArrayPython.itkArrayUI_swap, None, itkArrayUI)
itkArrayUI.Swap = new_instancemethod(_itkArrayPython.itkArrayUI_Swap, None, itkArrayUI)
itkArrayUI.__getitem__ = new_instancemethod(_itkArrayPython.itkArrayUI___getitem__, None, itkArrayUI)
itkArrayUI.__setitem__ = new_instancemethod(_itkArrayPython.itkArrayUI___setitem__, None, itkArrayUI)
itkArrayUI.__len__ = new_instancemethod(_itkArrayPython.itkArrayUI___len__, None, itkArrayUI)
itkArrayUI.__repr__ = new_instancemethod(_itkArrayPython.itkArrayUI___repr__, None, itkArrayUI)
itkArrayUI_swigregister = _itkArrayPython.itkArrayUI_swigregister
itkArrayUI_swigregister(itkArrayUI)

class itkArrayUL(vnl_vectorPython.vnl_vectorUL):
    """Proxy of C++ itkArrayUL class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args):
        """
        __init__(itkArrayUL self) -> itkArrayUL
        __init__(itkArrayUL self, itkArrayUL arg0) -> itkArrayUL
        __init__(itkArrayUL self, unsigned long dimension) -> itkArrayUL
        __init__(itkArrayUL self, unsigned long * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayUL
        __init__(itkArrayUL self, unsigned long * data, unsigned long sz) -> itkArrayUL
        __init__(itkArrayUL self, unsigned long const * data, unsigned long sz, bool LetArrayManageMemory=False) -> itkArrayUL
        __init__(itkArrayUL self, unsigned long const * data, unsigned long sz) -> itkArrayUL
        """
        _itkArrayPython.itkArrayUL_swiginit(self, _itkArrayPython.new_itkArrayUL(*args))

    def Fill(self, v: 'unsigned long const &') -> "void":
        """Fill(itkArrayUL self, unsigned long const & v)"""
        return _itkArrayPython.itkArrayUL_Fill(self, v)


    def Size(self) -> "unsigned long":
        """Size(itkArrayUL self) -> unsigned long"""
        return _itkArrayPython.itkArrayUL_Size(self)


    def GetNumberOfElements(self) -> "unsigned int":
        """GetNumberOfElements(itkArrayUL self) -> unsigned int"""
        return _itkArrayPython.itkArrayUL_GetNumberOfElements(self)


    def GetElement(self, i: 'unsigned long') -> "unsigned long const &":
        """GetElement(itkArrayUL self, unsigned long i) -> unsigned long const &"""
        return _itkArrayPython.itkArrayUL_GetElement(self, i)


    def SetElement(self, i: 'unsigned long', value: 'unsigned long const &') -> "void":
        """SetElement(itkArrayUL self, unsigned long i, unsigned long const & value)"""
        return _itkArrayPython.itkArrayUL_SetElement(self, i, value)


    def SetSize(self, sz: 'unsigned long') -> "void":
        """SetSize(itkArrayUL self, unsigned long sz)"""
        return _itkArrayPython.itkArrayUL_SetSize(self, sz)


    def GetSize(self) -> "unsigned long":
        """GetSize(itkArrayUL self) -> unsigned long"""
        return _itkArrayPython.itkArrayUL_GetSize(self)


    def SetDataSameSize(self, data: 'unsigned long *', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetDataSameSize(itkArrayUL self, unsigned long * data, bool LetArrayManageMemory=False)
        SetDataSameSize(itkArrayUL self, unsigned long * data)
        """
        return _itkArrayPython.itkArrayUL_SetDataSameSize(self, data, LetArrayManageMemory)


    def SetData(self, data: 'unsigned long *', sz: 'unsigned long', LetArrayManageMemory: 'bool'=False) -> "void":
        """
        SetData(itkArrayUL self, unsigned long * data, unsigned long sz, bool LetArrayManageMemory=False)
        SetData(itkArrayUL self, unsigned long * data, unsigned long sz)
        """
        return _itkArrayPython.itkArrayUL_SetData(self, data, sz, LetArrayManageMemory)

    __swig_destroy__ = _itkArrayPython.delete_itkArrayUL

    def swap(self, other: 'itkArrayUL') -> "void":
        """swap(itkArrayUL self, itkArrayUL other)"""
        return _itkArrayPython.itkArrayUL_swap(self, other)


    def Swap(self, other: 'itkArrayUL') -> "void":
        """Swap(itkArrayUL self, itkArrayUL other)"""
        return _itkArrayPython.itkArrayUL_Swap(self, other)


    def __getitem__(self, dim: 'unsigned long') -> "unsigned long":
        """__getitem__(itkArrayUL self, unsigned long dim) -> unsigned long"""
        return _itkArrayPython.itkArrayUL___getitem__(self, dim)


    def __setitem__(self, dim: 'unsigned long', v: 'unsigned long') -> "void":
        """__setitem__(itkArrayUL self, unsigned long dim, unsigned long v)"""
        return _itkArrayPython.itkArrayUL___setitem__(self, dim, v)


    def __len__(self) -> "unsigned int":
        """__len__(itkArrayUL self) -> unsigned int"""
        return _itkArrayPython.itkArrayUL___len__(self)


    def __repr__(self) -> "std::string":
        """__repr__(itkArrayUL self) -> std::string"""
        return _itkArrayPython.itkArrayUL___repr__(self)

itkArrayUL.Fill = new_instancemethod(_itkArrayPython.itkArrayUL_Fill, None, itkArrayUL)
itkArrayUL.Size = new_instancemethod(_itkArrayPython.itkArrayUL_Size, None, itkArrayUL)
itkArrayUL.GetNumberOfElements = new_instancemethod(_itkArrayPython.itkArrayUL_GetNumberOfElements, None, itkArrayUL)
itkArrayUL.GetElement = new_instancemethod(_itkArrayPython.itkArrayUL_GetElement, None, itkArrayUL)
itkArrayUL.SetElement = new_instancemethod(_itkArrayPython.itkArrayUL_SetElement, None, itkArrayUL)
itkArrayUL.SetSize = new_instancemethod(_itkArrayPython.itkArrayUL_SetSize, None, itkArrayUL)
itkArrayUL.GetSize = new_instancemethod(_itkArrayPython.itkArrayUL_GetSize, None, itkArrayUL)
itkArrayUL.SetDataSameSize = new_instancemethod(_itkArrayPython.itkArrayUL_SetDataSameSize, None, itkArrayUL)
itkArrayUL.SetData = new_instancemethod(_itkArrayPython.itkArrayUL_SetData, None, itkArrayUL)
itkArrayUL.swap = new_instancemethod(_itkArrayPython.itkArrayUL_swap, None, itkArrayUL)
itkArrayUL.Swap = new_instancemethod(_itkArrayPython.itkArrayUL_Swap, None, itkArrayUL)
itkArrayUL.__getitem__ = new_instancemethod(_itkArrayPython.itkArrayUL___getitem__, None, itkArrayUL)
itkArrayUL.__setitem__ = new_instancemethod(_itkArrayPython.itkArrayUL___setitem__, None, itkArrayUL)
itkArrayUL.__len__ = new_instancemethod(_itkArrayPython.itkArrayUL___len__, None, itkArrayUL)
itkArrayUL.__repr__ = new_instancemethod(_itkArrayPython.itkArrayUL___repr__, None, itkArrayUL)
itkArrayUL_swigregister = _itkArrayPython.itkArrayUL_swigregister
itkArrayUL_swigregister(itkArrayUL)



