# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTriangleHelperPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTriangleHelperPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTriangleHelperPython')
    _itkTriangleHelperPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTriangleHelperPython', [dirname(__file__)])
        except ImportError:
            import _itkTriangleHelperPython
            return _itkTriangleHelperPython
        try:
            _mod = imp.load_module('_itkTriangleHelperPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTriangleHelperPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTriangleHelperPython
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


import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkPointPython
class itkTriangleHelperPD2(object):
    """Proxy of C++ itkTriangleHelperPD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def IsObtuse(iA: 'itkPointD2', iB: 'itkPointD2', iC: 'itkPointD2') -> "bool":
        """IsObtuse(itkPointD2 iA, itkPointD2 iB, itkPointD2 iC) -> bool"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_IsObtuse(iA, iB, iC)

    IsObtuse = staticmethod(IsObtuse)

    def ComputeNormal(iA: 'itkPointD2', iB: 'itkPointD2', iC: 'itkPointD2') -> "itkVectorD2":
        """ComputeNormal(itkPointD2 iA, itkPointD2 iB, itkPointD2 iC) -> itkVectorD2"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeNormal(iA, iB, iC)

    ComputeNormal = staticmethod(ComputeNormal)

    def Cotangent(iA: 'itkPointD2', iB: 'itkPointD2', iC: 'itkPointD2') -> "double":
        """Cotangent(itkPointD2 iA, itkPointD2 iB, itkPointD2 iC) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_Cotangent(iA, iB, iC)

    Cotangent = staticmethod(Cotangent)

    def ComputeBarycenter(iA1: 'double const &', iP1: 'itkPointD2', iA2: 'double const &', iP2: 'itkPointD2', iA3: 'double const &', iP3: 'itkPointD2') -> "itkPointD2":
        """ComputeBarycenter(double const & iA1, itkPointD2 iP1, double const & iA2, itkPointD2 iP2, double const & iA3, itkPointD2 iP3) -> itkPointD2"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

    ComputeBarycenter = staticmethod(ComputeBarycenter)

    def ComputeAngle(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "double":
        """ComputeAngle(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeAngle(iP1, iP2, iP3)

    ComputeAngle = staticmethod(ComputeAngle)

    def ComputeGravityCenter(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "itkPointD2":
        """ComputeGravityCenter(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> itkPointD2"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeGravityCenter(iP1, iP2, iP3)

    ComputeGravityCenter = staticmethod(ComputeGravityCenter)

    def ComputeCircumCenter(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "itkPointD2":
        """ComputeCircumCenter(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> itkPointD2"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeCircumCenter(iP1, iP2, iP3)

    ComputeCircumCenter = staticmethod(ComputeCircumCenter)

    def ComputeConstrainedCircumCenter(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "itkPointD2":
        """ComputeConstrainedCircumCenter(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> itkPointD2"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

    ComputeConstrainedCircumCenter = staticmethod(ComputeConstrainedCircumCenter)

    def ComputeArea(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "double":
        """ComputeArea(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeArea(iP1, iP2, iP3)

    ComputeArea = staticmethod(ComputeArea)

    def ComputeMixedArea(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "double":
        """ComputeMixedArea(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeMixedArea(iP1, iP2, iP3)

    ComputeMixedArea = staticmethod(ComputeMixedArea)

    def __init__(self, *args):
        """
        __init__(itkTriangleHelperPD2 self) -> itkTriangleHelperPD2
        __init__(itkTriangleHelperPD2 self, itkTriangleHelperPD2 arg0) -> itkTriangleHelperPD2
        """
        _itkTriangleHelperPython.itkTriangleHelperPD2_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPD2(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPD2
itkTriangleHelperPD2_swigregister = _itkTriangleHelperPython.itkTriangleHelperPD2_swigregister
itkTriangleHelperPD2_swigregister(itkTriangleHelperPD2)

def itkTriangleHelperPD2_IsObtuse(iA: 'itkPointD2', iB: 'itkPointD2', iC: 'itkPointD2') -> "bool":
    """itkTriangleHelperPD2_IsObtuse(itkPointD2 iA, itkPointD2 iB, itkPointD2 iC) -> bool"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_IsObtuse(iA, iB, iC)

def itkTriangleHelperPD2_ComputeNormal(iA: 'itkPointD2', iB: 'itkPointD2', iC: 'itkPointD2') -> "itkVectorD2":
    """itkTriangleHelperPD2_ComputeNormal(itkPointD2 iA, itkPointD2 iB, itkPointD2 iC) -> itkVectorD2"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeNormal(iA, iB, iC)

def itkTriangleHelperPD2_Cotangent(iA: 'itkPointD2', iB: 'itkPointD2', iC: 'itkPointD2') -> "double":
    """itkTriangleHelperPD2_Cotangent(itkPointD2 iA, itkPointD2 iB, itkPointD2 iC) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_Cotangent(iA, iB, iC)

def itkTriangleHelperPD2_ComputeBarycenter(iA1: 'double const &', iP1: 'itkPointD2', iA2: 'double const &', iP2: 'itkPointD2', iA3: 'double const &', iP3: 'itkPointD2') -> "itkPointD2":
    """itkTriangleHelperPD2_ComputeBarycenter(double const & iA1, itkPointD2 iP1, double const & iA2, itkPointD2 iP2, double const & iA3, itkPointD2 iP3) -> itkPointD2"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

def itkTriangleHelperPD2_ComputeAngle(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "double":
    """itkTriangleHelperPD2_ComputeAngle(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeAngle(iP1, iP2, iP3)

def itkTriangleHelperPD2_ComputeGravityCenter(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "itkPointD2":
    """itkTriangleHelperPD2_ComputeGravityCenter(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> itkPointD2"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeGravityCenter(iP1, iP2, iP3)

def itkTriangleHelperPD2_ComputeCircumCenter(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "itkPointD2":
    """itkTriangleHelperPD2_ComputeCircumCenter(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> itkPointD2"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPD2_ComputeConstrainedCircumCenter(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "itkPointD2":
    """itkTriangleHelperPD2_ComputeConstrainedCircumCenter(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> itkPointD2"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPD2_ComputeArea(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "double":
    """itkTriangleHelperPD2_ComputeArea(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeArea(iP1, iP2, iP3)

def itkTriangleHelperPD2_ComputeMixedArea(iP1: 'itkPointD2', iP2: 'itkPointD2', iP3: 'itkPointD2') -> "double":
    """itkTriangleHelperPD2_ComputeMixedArea(itkPointD2 iP1, itkPointD2 iP2, itkPointD2 iP3) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeMixedArea(iP1, iP2, iP3)

class itkTriangleHelperPD3(object):
    """Proxy of C++ itkTriangleHelperPD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def IsObtuse(iA: 'itkPointD3', iB: 'itkPointD3', iC: 'itkPointD3') -> "bool":
        """IsObtuse(itkPointD3 iA, itkPointD3 iB, itkPointD3 iC) -> bool"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_IsObtuse(iA, iB, iC)

    IsObtuse = staticmethod(IsObtuse)

    def ComputeNormal(iA: 'itkPointD3', iB: 'itkPointD3', iC: 'itkPointD3') -> "itkVectorD3":
        """ComputeNormal(itkPointD3 iA, itkPointD3 iB, itkPointD3 iC) -> itkVectorD3"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeNormal(iA, iB, iC)

    ComputeNormal = staticmethod(ComputeNormal)

    def Cotangent(iA: 'itkPointD3', iB: 'itkPointD3', iC: 'itkPointD3') -> "double":
        """Cotangent(itkPointD3 iA, itkPointD3 iB, itkPointD3 iC) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_Cotangent(iA, iB, iC)

    Cotangent = staticmethod(Cotangent)

    def ComputeBarycenter(iA1: 'double const &', iP1: 'itkPointD3', iA2: 'double const &', iP2: 'itkPointD3', iA3: 'double const &', iP3: 'itkPointD3') -> "itkPointD3":
        """ComputeBarycenter(double const & iA1, itkPointD3 iP1, double const & iA2, itkPointD3 iP2, double const & iA3, itkPointD3 iP3) -> itkPointD3"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

    ComputeBarycenter = staticmethod(ComputeBarycenter)

    def ComputeAngle(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "double":
        """ComputeAngle(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeAngle(iP1, iP2, iP3)

    ComputeAngle = staticmethod(ComputeAngle)

    def ComputeGravityCenter(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "itkPointD3":
        """ComputeGravityCenter(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> itkPointD3"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeGravityCenter(iP1, iP2, iP3)

    ComputeGravityCenter = staticmethod(ComputeGravityCenter)

    def ComputeCircumCenter(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "itkPointD3":
        """ComputeCircumCenter(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> itkPointD3"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeCircumCenter(iP1, iP2, iP3)

    ComputeCircumCenter = staticmethod(ComputeCircumCenter)

    def ComputeConstrainedCircumCenter(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "itkPointD3":
        """ComputeConstrainedCircumCenter(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> itkPointD3"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

    ComputeConstrainedCircumCenter = staticmethod(ComputeConstrainedCircumCenter)

    def ComputeArea(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "double":
        """ComputeArea(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeArea(iP1, iP2, iP3)

    ComputeArea = staticmethod(ComputeArea)

    def ComputeMixedArea(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "double":
        """ComputeMixedArea(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> double"""
        return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeMixedArea(iP1, iP2, iP3)

    ComputeMixedArea = staticmethod(ComputeMixedArea)

    def __init__(self, *args):
        """
        __init__(itkTriangleHelperPD3 self) -> itkTriangleHelperPD3
        __init__(itkTriangleHelperPD3 self, itkTriangleHelperPD3 arg0) -> itkTriangleHelperPD3
        """
        _itkTriangleHelperPython.itkTriangleHelperPD3_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPD3(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPD3
itkTriangleHelperPD3_swigregister = _itkTriangleHelperPython.itkTriangleHelperPD3_swigregister
itkTriangleHelperPD3_swigregister(itkTriangleHelperPD3)

def itkTriangleHelperPD3_IsObtuse(iA: 'itkPointD3', iB: 'itkPointD3', iC: 'itkPointD3') -> "bool":
    """itkTriangleHelperPD3_IsObtuse(itkPointD3 iA, itkPointD3 iB, itkPointD3 iC) -> bool"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_IsObtuse(iA, iB, iC)

def itkTriangleHelperPD3_ComputeNormal(iA: 'itkPointD3', iB: 'itkPointD3', iC: 'itkPointD3') -> "itkVectorD3":
    """itkTriangleHelperPD3_ComputeNormal(itkPointD3 iA, itkPointD3 iB, itkPointD3 iC) -> itkVectorD3"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeNormal(iA, iB, iC)

def itkTriangleHelperPD3_Cotangent(iA: 'itkPointD3', iB: 'itkPointD3', iC: 'itkPointD3') -> "double":
    """itkTriangleHelperPD3_Cotangent(itkPointD3 iA, itkPointD3 iB, itkPointD3 iC) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_Cotangent(iA, iB, iC)

def itkTriangleHelperPD3_ComputeBarycenter(iA1: 'double const &', iP1: 'itkPointD3', iA2: 'double const &', iP2: 'itkPointD3', iA3: 'double const &', iP3: 'itkPointD3') -> "itkPointD3":
    """itkTriangleHelperPD3_ComputeBarycenter(double const & iA1, itkPointD3 iP1, double const & iA2, itkPointD3 iP2, double const & iA3, itkPointD3 iP3) -> itkPointD3"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

def itkTriangleHelperPD3_ComputeAngle(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "double":
    """itkTriangleHelperPD3_ComputeAngle(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeAngle(iP1, iP2, iP3)

def itkTriangleHelperPD3_ComputeGravityCenter(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "itkPointD3":
    """itkTriangleHelperPD3_ComputeGravityCenter(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> itkPointD3"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeGravityCenter(iP1, iP2, iP3)

def itkTriangleHelperPD3_ComputeCircumCenter(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "itkPointD3":
    """itkTriangleHelperPD3_ComputeCircumCenter(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> itkPointD3"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPD3_ComputeConstrainedCircumCenter(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "itkPointD3":
    """itkTriangleHelperPD3_ComputeConstrainedCircumCenter(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> itkPointD3"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPD3_ComputeArea(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "double":
    """itkTriangleHelperPD3_ComputeArea(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeArea(iP1, iP2, iP3)

def itkTriangleHelperPD3_ComputeMixedArea(iP1: 'itkPointD3', iP2: 'itkPointD3', iP3: 'itkPointD3') -> "double":
    """itkTriangleHelperPD3_ComputeMixedArea(itkPointD3 iP1, itkPointD3 iP2, itkPointD3 iP3) -> double"""
    return _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeMixedArea(iP1, iP2, iP3)

class itkTriangleHelperPF2(object):
    """Proxy of C++ itkTriangleHelperPF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def IsObtuse(iA: 'itkPointF2', iB: 'itkPointF2', iC: 'itkPointF2') -> "bool":
        """IsObtuse(itkPointF2 iA, itkPointF2 iB, itkPointF2 iC) -> bool"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_IsObtuse(iA, iB, iC)

    IsObtuse = staticmethod(IsObtuse)

    def ComputeNormal(iA: 'itkPointF2', iB: 'itkPointF2', iC: 'itkPointF2') -> "itkVectorF2":
        """ComputeNormal(itkPointF2 iA, itkPointF2 iB, itkPointF2 iC) -> itkVectorF2"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeNormal(iA, iB, iC)

    ComputeNormal = staticmethod(ComputeNormal)

    def Cotangent(iA: 'itkPointF2', iB: 'itkPointF2', iC: 'itkPointF2') -> "float":
        """Cotangent(itkPointF2 iA, itkPointF2 iB, itkPointF2 iC) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_Cotangent(iA, iB, iC)

    Cotangent = staticmethod(Cotangent)

    def ComputeBarycenter(iA1: 'float const &', iP1: 'itkPointF2', iA2: 'float const &', iP2: 'itkPointF2', iA3: 'float const &', iP3: 'itkPointF2') -> "itkPointF2":
        """ComputeBarycenter(float const & iA1, itkPointF2 iP1, float const & iA2, itkPointF2 iP2, float const & iA3, itkPointF2 iP3) -> itkPointF2"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

    ComputeBarycenter = staticmethod(ComputeBarycenter)

    def ComputeAngle(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "float":
        """ComputeAngle(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeAngle(iP1, iP2, iP3)

    ComputeAngle = staticmethod(ComputeAngle)

    def ComputeGravityCenter(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "itkPointF2":
        """ComputeGravityCenter(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> itkPointF2"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeGravityCenter(iP1, iP2, iP3)

    ComputeGravityCenter = staticmethod(ComputeGravityCenter)

    def ComputeCircumCenter(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "itkPointF2":
        """ComputeCircumCenter(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> itkPointF2"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeCircumCenter(iP1, iP2, iP3)

    ComputeCircumCenter = staticmethod(ComputeCircumCenter)

    def ComputeConstrainedCircumCenter(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "itkPointF2":
        """ComputeConstrainedCircumCenter(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> itkPointF2"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

    ComputeConstrainedCircumCenter = staticmethod(ComputeConstrainedCircumCenter)

    def ComputeArea(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "float":
        """ComputeArea(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeArea(iP1, iP2, iP3)

    ComputeArea = staticmethod(ComputeArea)

    def ComputeMixedArea(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "float":
        """ComputeMixedArea(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeMixedArea(iP1, iP2, iP3)

    ComputeMixedArea = staticmethod(ComputeMixedArea)

    def __init__(self, *args):
        """
        __init__(itkTriangleHelperPF2 self) -> itkTriangleHelperPF2
        __init__(itkTriangleHelperPF2 self, itkTriangleHelperPF2 arg0) -> itkTriangleHelperPF2
        """
        _itkTriangleHelperPython.itkTriangleHelperPF2_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPF2(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPF2
itkTriangleHelperPF2_swigregister = _itkTriangleHelperPython.itkTriangleHelperPF2_swigregister
itkTriangleHelperPF2_swigregister(itkTriangleHelperPF2)

def itkTriangleHelperPF2_IsObtuse(iA: 'itkPointF2', iB: 'itkPointF2', iC: 'itkPointF2') -> "bool":
    """itkTriangleHelperPF2_IsObtuse(itkPointF2 iA, itkPointF2 iB, itkPointF2 iC) -> bool"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_IsObtuse(iA, iB, iC)

def itkTriangleHelperPF2_ComputeNormal(iA: 'itkPointF2', iB: 'itkPointF2', iC: 'itkPointF2') -> "itkVectorF2":
    """itkTriangleHelperPF2_ComputeNormal(itkPointF2 iA, itkPointF2 iB, itkPointF2 iC) -> itkVectorF2"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeNormal(iA, iB, iC)

def itkTriangleHelperPF2_Cotangent(iA: 'itkPointF2', iB: 'itkPointF2', iC: 'itkPointF2') -> "float":
    """itkTriangleHelperPF2_Cotangent(itkPointF2 iA, itkPointF2 iB, itkPointF2 iC) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_Cotangent(iA, iB, iC)

def itkTriangleHelperPF2_ComputeBarycenter(iA1: 'float const &', iP1: 'itkPointF2', iA2: 'float const &', iP2: 'itkPointF2', iA3: 'float const &', iP3: 'itkPointF2') -> "itkPointF2":
    """itkTriangleHelperPF2_ComputeBarycenter(float const & iA1, itkPointF2 iP1, float const & iA2, itkPointF2 iP2, float const & iA3, itkPointF2 iP3) -> itkPointF2"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

def itkTriangleHelperPF2_ComputeAngle(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "float":
    """itkTriangleHelperPF2_ComputeAngle(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeAngle(iP1, iP2, iP3)

def itkTriangleHelperPF2_ComputeGravityCenter(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "itkPointF2":
    """itkTriangleHelperPF2_ComputeGravityCenter(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> itkPointF2"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeGravityCenter(iP1, iP2, iP3)

def itkTriangleHelperPF2_ComputeCircumCenter(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "itkPointF2":
    """itkTriangleHelperPF2_ComputeCircumCenter(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> itkPointF2"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPF2_ComputeConstrainedCircumCenter(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "itkPointF2":
    """itkTriangleHelperPF2_ComputeConstrainedCircumCenter(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> itkPointF2"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPF2_ComputeArea(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "float":
    """itkTriangleHelperPF2_ComputeArea(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeArea(iP1, iP2, iP3)

def itkTriangleHelperPF2_ComputeMixedArea(iP1: 'itkPointF2', iP2: 'itkPointF2', iP3: 'itkPointF2') -> "float":
    """itkTriangleHelperPF2_ComputeMixedArea(itkPointF2 iP1, itkPointF2 iP2, itkPointF2 iP3) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeMixedArea(iP1, iP2, iP3)

class itkTriangleHelperPF3(object):
    """Proxy of C++ itkTriangleHelperPF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def IsObtuse(iA: 'itkPointF3', iB: 'itkPointF3', iC: 'itkPointF3') -> "bool":
        """IsObtuse(itkPointF3 iA, itkPointF3 iB, itkPointF3 iC) -> bool"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_IsObtuse(iA, iB, iC)

    IsObtuse = staticmethod(IsObtuse)

    def ComputeNormal(iA: 'itkPointF3', iB: 'itkPointF3', iC: 'itkPointF3') -> "itkVectorF3":
        """ComputeNormal(itkPointF3 iA, itkPointF3 iB, itkPointF3 iC) -> itkVectorF3"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeNormal(iA, iB, iC)

    ComputeNormal = staticmethod(ComputeNormal)

    def Cotangent(iA: 'itkPointF3', iB: 'itkPointF3', iC: 'itkPointF3') -> "float":
        """Cotangent(itkPointF3 iA, itkPointF3 iB, itkPointF3 iC) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_Cotangent(iA, iB, iC)

    Cotangent = staticmethod(Cotangent)

    def ComputeBarycenter(iA1: 'float const &', iP1: 'itkPointF3', iA2: 'float const &', iP2: 'itkPointF3', iA3: 'float const &', iP3: 'itkPointF3') -> "itkPointF3":
        """ComputeBarycenter(float const & iA1, itkPointF3 iP1, float const & iA2, itkPointF3 iP2, float const & iA3, itkPointF3 iP3) -> itkPointF3"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

    ComputeBarycenter = staticmethod(ComputeBarycenter)

    def ComputeAngle(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "float":
        """ComputeAngle(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeAngle(iP1, iP2, iP3)

    ComputeAngle = staticmethod(ComputeAngle)

    def ComputeGravityCenter(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "itkPointF3":
        """ComputeGravityCenter(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> itkPointF3"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeGravityCenter(iP1, iP2, iP3)

    ComputeGravityCenter = staticmethod(ComputeGravityCenter)

    def ComputeCircumCenter(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "itkPointF3":
        """ComputeCircumCenter(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> itkPointF3"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeCircumCenter(iP1, iP2, iP3)

    ComputeCircumCenter = staticmethod(ComputeCircumCenter)

    def ComputeConstrainedCircumCenter(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "itkPointF3":
        """ComputeConstrainedCircumCenter(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> itkPointF3"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

    ComputeConstrainedCircumCenter = staticmethod(ComputeConstrainedCircumCenter)

    def ComputeArea(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "float":
        """ComputeArea(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeArea(iP1, iP2, iP3)

    ComputeArea = staticmethod(ComputeArea)

    def ComputeMixedArea(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "float":
        """ComputeMixedArea(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> float"""
        return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeMixedArea(iP1, iP2, iP3)

    ComputeMixedArea = staticmethod(ComputeMixedArea)

    def __init__(self, *args):
        """
        __init__(itkTriangleHelperPF3 self) -> itkTriangleHelperPF3
        __init__(itkTriangleHelperPF3 self, itkTriangleHelperPF3 arg0) -> itkTriangleHelperPF3
        """
        _itkTriangleHelperPython.itkTriangleHelperPF3_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPF3(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPF3
itkTriangleHelperPF3_swigregister = _itkTriangleHelperPython.itkTriangleHelperPF3_swigregister
itkTriangleHelperPF3_swigregister(itkTriangleHelperPF3)

def itkTriangleHelperPF3_IsObtuse(iA: 'itkPointF3', iB: 'itkPointF3', iC: 'itkPointF3') -> "bool":
    """itkTriangleHelperPF3_IsObtuse(itkPointF3 iA, itkPointF3 iB, itkPointF3 iC) -> bool"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_IsObtuse(iA, iB, iC)

def itkTriangleHelperPF3_ComputeNormal(iA: 'itkPointF3', iB: 'itkPointF3', iC: 'itkPointF3') -> "itkVectorF3":
    """itkTriangleHelperPF3_ComputeNormal(itkPointF3 iA, itkPointF3 iB, itkPointF3 iC) -> itkVectorF3"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeNormal(iA, iB, iC)

def itkTriangleHelperPF3_Cotangent(iA: 'itkPointF3', iB: 'itkPointF3', iC: 'itkPointF3') -> "float":
    """itkTriangleHelperPF3_Cotangent(itkPointF3 iA, itkPointF3 iB, itkPointF3 iC) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_Cotangent(iA, iB, iC)

def itkTriangleHelperPF3_ComputeBarycenter(iA1: 'float const &', iP1: 'itkPointF3', iA2: 'float const &', iP2: 'itkPointF3', iA3: 'float const &', iP3: 'itkPointF3') -> "itkPointF3":
    """itkTriangleHelperPF3_ComputeBarycenter(float const & iA1, itkPointF3 iP1, float const & iA2, itkPointF3 iP2, float const & iA3, itkPointF3 iP3) -> itkPointF3"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeBarycenter(iA1, iP1, iA2, iP2, iA3, iP3)

def itkTriangleHelperPF3_ComputeAngle(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "float":
    """itkTriangleHelperPF3_ComputeAngle(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeAngle(iP1, iP2, iP3)

def itkTriangleHelperPF3_ComputeGravityCenter(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "itkPointF3":
    """itkTriangleHelperPF3_ComputeGravityCenter(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> itkPointF3"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeGravityCenter(iP1, iP2, iP3)

def itkTriangleHelperPF3_ComputeCircumCenter(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "itkPointF3":
    """itkTriangleHelperPF3_ComputeCircumCenter(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> itkPointF3"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPF3_ComputeConstrainedCircumCenter(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "itkPointF3":
    """itkTriangleHelperPF3_ComputeConstrainedCircumCenter(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> itkPointF3"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeConstrainedCircumCenter(iP1, iP2, iP3)

def itkTriangleHelperPF3_ComputeArea(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "float":
    """itkTriangleHelperPF3_ComputeArea(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeArea(iP1, iP2, iP3)

def itkTriangleHelperPF3_ComputeMixedArea(iP1: 'itkPointF3', iP2: 'itkPointF3', iP3: 'itkPointF3') -> "float":
    """itkTriangleHelperPF3_ComputeMixedArea(itkPointF3 iP1, itkPointF3 iP2, itkPointF3 iP3) -> float"""
    return _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeMixedArea(iP1, iP2, iP3)



