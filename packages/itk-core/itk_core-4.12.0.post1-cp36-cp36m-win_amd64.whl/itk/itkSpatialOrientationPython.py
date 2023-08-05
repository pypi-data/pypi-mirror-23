# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSpatialOrientationPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkSpatialOrientationPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkSpatialOrientationPython')
    _itkSpatialOrientationPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSpatialOrientationPython', [dirname(__file__)])
        except ImportError:
            import _itkSpatialOrientationPython
            return _itkSpatialOrientationPython
        try:
            _mod = imp.load_module('_itkSpatialOrientationPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkSpatialOrientationPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSpatialOrientationPython
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
ITK_COORDINATE_ORIENTATION_INVALID = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_INVALID
ITK_COORDINATE_ORIENTATION_RIP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RIP
ITK_COORDINATE_ORIENTATION_LIP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LIP
ITK_COORDINATE_ORIENTATION_RSP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RSP
ITK_COORDINATE_ORIENTATION_LSP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LSP
ITK_COORDINATE_ORIENTATION_RIA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RIA
ITK_COORDINATE_ORIENTATION_LIA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LIA
ITK_COORDINATE_ORIENTATION_RSA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RSA
ITK_COORDINATE_ORIENTATION_LSA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LSA
ITK_COORDINATE_ORIENTATION_IRP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_IRP
ITK_COORDINATE_ORIENTATION_ILP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ILP
ITK_COORDINATE_ORIENTATION_SRP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SRP
ITK_COORDINATE_ORIENTATION_SLP = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SLP
ITK_COORDINATE_ORIENTATION_IRA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_IRA
ITK_COORDINATE_ORIENTATION_ILA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ILA
ITK_COORDINATE_ORIENTATION_SRA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SRA
ITK_COORDINATE_ORIENTATION_SLA = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SLA
ITK_COORDINATE_ORIENTATION_RPI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RPI
ITK_COORDINATE_ORIENTATION_LPI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LPI
ITK_COORDINATE_ORIENTATION_RAI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RAI
ITK_COORDINATE_ORIENTATION_LAI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LAI
ITK_COORDINATE_ORIENTATION_RPS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RPS
ITK_COORDINATE_ORIENTATION_LPS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LPS
ITK_COORDINATE_ORIENTATION_RAS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_RAS
ITK_COORDINATE_ORIENTATION_LAS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_LAS
ITK_COORDINATE_ORIENTATION_PRI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PRI
ITK_COORDINATE_ORIENTATION_PLI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PLI
ITK_COORDINATE_ORIENTATION_ARI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ARI
ITK_COORDINATE_ORIENTATION_ALI = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ALI
ITK_COORDINATE_ORIENTATION_PRS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PRS
ITK_COORDINATE_ORIENTATION_PLS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PLS
ITK_COORDINATE_ORIENTATION_ARS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ARS
ITK_COORDINATE_ORIENTATION_ALS = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ALS
ITK_COORDINATE_ORIENTATION_IPR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_IPR
ITK_COORDINATE_ORIENTATION_SPR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SPR
ITK_COORDINATE_ORIENTATION_IAR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_IAR
ITK_COORDINATE_ORIENTATION_SAR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SAR
ITK_COORDINATE_ORIENTATION_IPL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_IPL
ITK_COORDINATE_ORIENTATION_SPL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SPL
ITK_COORDINATE_ORIENTATION_IAL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_IAL
ITK_COORDINATE_ORIENTATION_SAL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_SAL
ITK_COORDINATE_ORIENTATION_PIR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PIR
ITK_COORDINATE_ORIENTATION_PSR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PSR
ITK_COORDINATE_ORIENTATION_AIR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_AIR
ITK_COORDINATE_ORIENTATION_ASR = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ASR
ITK_COORDINATE_ORIENTATION_PIL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PIL
ITK_COORDINATE_ORIENTATION_PSL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_PSL
ITK_COORDINATE_ORIENTATION_AIL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_AIL
ITK_COORDINATE_ORIENTATION_ASL = _itkSpatialOrientationPython.ITK_COORDINATE_ORIENTATION_ASL


