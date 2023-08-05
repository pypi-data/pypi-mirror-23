# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkImageToMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkImageToMeshFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkImageToMeshFilterPython')
    _itkImageToMeshFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkImageToMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkImageToMeshFilterPython
            return _itkImageToMeshFilterPython
        try:
            _mod = imp.load_module('_itkImageToMeshFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkImageToMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkImageToMeshFilterPython
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


import itkMeshBasePython
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkMapContainerPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkPointPython
import ITKCommonBasePython
import itkPointSetPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkBoundingBoxPython
import itkImagePython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkMeshSourcePython

def itkImageToMeshFilterIUC3MD3STD33DD_New():
  return itkImageToMeshFilterIUC3MD3STD33DD.New()


def itkImageToMeshFilterISS3MD3STD33DD_New():
  return itkImageToMeshFilterISS3MD3STD33DD.New()


def itkImageToMeshFilterIF3MF3STF33FF_New():
  return itkImageToMeshFilterIF3MF3STF33FF.New()


def itkImageToMeshFilterIF2MF2STF22FF_New():
  return itkImageToMeshFilterIF2MF2STF22FF.New()

class itkImageToMeshFilterIF2MF2STF22FF(itkMeshSourcePython.itkMeshSourceMF2STF22FF):
    """Proxy of C++ itkImageToMeshFilterIF2MF2STF22FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args):
        """
        SetInput(itkImageToMeshFilterIF2MF2STF22FF self, unsigned int idx, itkImageF2 input)
        SetInput(itkImageToMeshFilterIF2MF2STF22FF self, itkImageF2 input)
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_SetInput(self, *args)


    def GetInput(self, *args):
        """
        GetInput(itkImageToMeshFilterIF2MF2STF22FF self, unsigned int idx) -> itkImageF2
        GetInput(itkImageToMeshFilterIF2MF2STF22FF self) -> itkImageF2
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GetInput(self, *args)


    def GetOutput(self):
        """GetOutput(itkImageToMeshFilterIF2MF2STF22FF self) -> itkMeshF2STF22FF"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GetOutput(self)


    def GenerateOutputInformation(self):
        """GenerateOutputInformation(itkImageToMeshFilterIF2MF2STF22FF self)"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GenerateOutputInformation(self)

    __swig_destroy__ = _itkImageToMeshFilterPython.delete_itkImageToMeshFilterIF2MF2STF22FF

    def cast(obj):
        """cast(itkLightObject obj) -> itkImageToMeshFilterIF2MF2STF22FF"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkImageToMeshFilterIF2MF2STF22FF self) -> itkImageToMeshFilterIF2MF2STF22FF"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToMeshFilterIF2MF2STF22FF

        Create a new object of the class itkImageToMeshFilterIF2MF2STF22FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToMeshFilterIF2MF2STF22FF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToMeshFilterIF2MF2STF22FF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToMeshFilterIF2MF2STF22FF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToMeshFilterIF2MF2STF22FF.SetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_SetInput, None, itkImageToMeshFilterIF2MF2STF22FF)
itkImageToMeshFilterIF2MF2STF22FF.GetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GetInput, None, itkImageToMeshFilterIF2MF2STF22FF)
itkImageToMeshFilterIF2MF2STF22FF.GetOutput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GetOutput, None, itkImageToMeshFilterIF2MF2STF22FF)
itkImageToMeshFilterIF2MF2STF22FF.GenerateOutputInformation = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GenerateOutputInformation, None, itkImageToMeshFilterIF2MF2STF22FF)
itkImageToMeshFilterIF2MF2STF22FF.GetPointer = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_GetPointer, None, itkImageToMeshFilterIF2MF2STF22FF)
itkImageToMeshFilterIF2MF2STF22FF_swigregister = _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_swigregister
itkImageToMeshFilterIF2MF2STF22FF_swigregister(itkImageToMeshFilterIF2MF2STF22FF)

def itkImageToMeshFilterIF2MF2STF22FF_cast(obj):
    """itkImageToMeshFilterIF2MF2STF22FF_cast(itkLightObject obj) -> itkImageToMeshFilterIF2MF2STF22FF"""
    return _itkImageToMeshFilterPython.itkImageToMeshFilterIF2MF2STF22FF_cast(obj)

class itkImageToMeshFilterIF3MF3STF33FF(itkMeshSourcePython.itkMeshSourceMF3STF33FF):
    """Proxy of C++ itkImageToMeshFilterIF3MF3STF33FF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args):
        """
        SetInput(itkImageToMeshFilterIF3MF3STF33FF self, unsigned int idx, itkImageF3 input)
        SetInput(itkImageToMeshFilterIF3MF3STF33FF self, itkImageF3 input)
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_SetInput(self, *args)


    def GetInput(self, *args):
        """
        GetInput(itkImageToMeshFilterIF3MF3STF33FF self, unsigned int idx) -> itkImageF3
        GetInput(itkImageToMeshFilterIF3MF3STF33FF self) -> itkImageF3
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GetInput(self, *args)


    def GetOutput(self):
        """GetOutput(itkImageToMeshFilterIF3MF3STF33FF self) -> itkMeshF3STF33FF"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GetOutput(self)


    def GenerateOutputInformation(self):
        """GenerateOutputInformation(itkImageToMeshFilterIF3MF3STF33FF self)"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GenerateOutputInformation(self)

    __swig_destroy__ = _itkImageToMeshFilterPython.delete_itkImageToMeshFilterIF3MF3STF33FF

    def cast(obj):
        """cast(itkLightObject obj) -> itkImageToMeshFilterIF3MF3STF33FF"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkImageToMeshFilterIF3MF3STF33FF self) -> itkImageToMeshFilterIF3MF3STF33FF"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToMeshFilterIF3MF3STF33FF

        Create a new object of the class itkImageToMeshFilterIF3MF3STF33FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToMeshFilterIF3MF3STF33FF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToMeshFilterIF3MF3STF33FF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToMeshFilterIF3MF3STF33FF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToMeshFilterIF3MF3STF33FF.SetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_SetInput, None, itkImageToMeshFilterIF3MF3STF33FF)
itkImageToMeshFilterIF3MF3STF33FF.GetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GetInput, None, itkImageToMeshFilterIF3MF3STF33FF)
itkImageToMeshFilterIF3MF3STF33FF.GetOutput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GetOutput, None, itkImageToMeshFilterIF3MF3STF33FF)
itkImageToMeshFilterIF3MF3STF33FF.GenerateOutputInformation = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GenerateOutputInformation, None, itkImageToMeshFilterIF3MF3STF33FF)
itkImageToMeshFilterIF3MF3STF33FF.GetPointer = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_GetPointer, None, itkImageToMeshFilterIF3MF3STF33FF)
itkImageToMeshFilterIF3MF3STF33FF_swigregister = _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_swigregister
itkImageToMeshFilterIF3MF3STF33FF_swigregister(itkImageToMeshFilterIF3MF3STF33FF)

def itkImageToMeshFilterIF3MF3STF33FF_cast(obj):
    """itkImageToMeshFilterIF3MF3STF33FF_cast(itkLightObject obj) -> itkImageToMeshFilterIF3MF3STF33FF"""
    return _itkImageToMeshFilterPython.itkImageToMeshFilterIF3MF3STF33FF_cast(obj)

class itkImageToMeshFilterISS3MD3STD33DD(itkMeshSourcePython.itkMeshSourceMD3STD33DD):
    """Proxy of C++ itkImageToMeshFilterISS3MD3STD33DD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args):
        """
        SetInput(itkImageToMeshFilterISS3MD3STD33DD self, unsigned int idx, itkImageSS3 input)
        SetInput(itkImageToMeshFilterISS3MD3STD33DD self, itkImageSS3 input)
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_SetInput(self, *args)


    def GetInput(self, *args):
        """
        GetInput(itkImageToMeshFilterISS3MD3STD33DD self, unsigned int idx) -> itkImageSS3
        GetInput(itkImageToMeshFilterISS3MD3STD33DD self) -> itkImageSS3
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GetInput(self, *args)


    def GetOutput(self):
        """GetOutput(itkImageToMeshFilterISS3MD3STD33DD self) -> itkMeshD3STD33DD"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GetOutput(self)


    def GenerateOutputInformation(self):
        """GenerateOutputInformation(itkImageToMeshFilterISS3MD3STD33DD self)"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GenerateOutputInformation(self)

    __swig_destroy__ = _itkImageToMeshFilterPython.delete_itkImageToMeshFilterISS3MD3STD33DD

    def cast(obj):
        """cast(itkLightObject obj) -> itkImageToMeshFilterISS3MD3STD33DD"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkImageToMeshFilterISS3MD3STD33DD self) -> itkImageToMeshFilterISS3MD3STD33DD"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToMeshFilterISS3MD3STD33DD

        Create a new object of the class itkImageToMeshFilterISS3MD3STD33DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToMeshFilterISS3MD3STD33DD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToMeshFilterISS3MD3STD33DD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToMeshFilterISS3MD3STD33DD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToMeshFilterISS3MD3STD33DD.SetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_SetInput, None, itkImageToMeshFilterISS3MD3STD33DD)
itkImageToMeshFilterISS3MD3STD33DD.GetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GetInput, None, itkImageToMeshFilterISS3MD3STD33DD)
itkImageToMeshFilterISS3MD3STD33DD.GetOutput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GetOutput, None, itkImageToMeshFilterISS3MD3STD33DD)
itkImageToMeshFilterISS3MD3STD33DD.GenerateOutputInformation = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GenerateOutputInformation, None, itkImageToMeshFilterISS3MD3STD33DD)
itkImageToMeshFilterISS3MD3STD33DD.GetPointer = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_GetPointer, None, itkImageToMeshFilterISS3MD3STD33DD)
itkImageToMeshFilterISS3MD3STD33DD_swigregister = _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_swigregister
itkImageToMeshFilterISS3MD3STD33DD_swigregister(itkImageToMeshFilterISS3MD3STD33DD)

def itkImageToMeshFilterISS3MD3STD33DD_cast(obj):
    """itkImageToMeshFilterISS3MD3STD33DD_cast(itkLightObject obj) -> itkImageToMeshFilterISS3MD3STD33DD"""
    return _itkImageToMeshFilterPython.itkImageToMeshFilterISS3MD3STD33DD_cast(obj)

class itkImageToMeshFilterIUC3MD3STD33DD(itkMeshSourcePython.itkMeshSourceMD3STD33DD):
    """Proxy of C++ itkImageToMeshFilterIUC3MD3STD33DD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args):
        """
        SetInput(itkImageToMeshFilterIUC3MD3STD33DD self, unsigned int idx, itkImageUC3 input)
        SetInput(itkImageToMeshFilterIUC3MD3STD33DD self, itkImageUC3 input)
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_SetInput(self, *args)


    def GetInput(self, *args):
        """
        GetInput(itkImageToMeshFilterIUC3MD3STD33DD self, unsigned int idx) -> itkImageUC3
        GetInput(itkImageToMeshFilterIUC3MD3STD33DD self) -> itkImageUC3
        """
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GetInput(self, *args)


    def GetOutput(self):
        """GetOutput(itkImageToMeshFilterIUC3MD3STD33DD self) -> itkMeshD3STD33DD"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GetOutput(self)


    def GenerateOutputInformation(self):
        """GenerateOutputInformation(itkImageToMeshFilterIUC3MD3STD33DD self)"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GenerateOutputInformation(self)

    __swig_destroy__ = _itkImageToMeshFilterPython.delete_itkImageToMeshFilterIUC3MD3STD33DD

    def cast(obj):
        """cast(itkLightObject obj) -> itkImageToMeshFilterIUC3MD3STD33DD"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkImageToMeshFilterIUC3MD3STD33DD self) -> itkImageToMeshFilterIUC3MD3STD33DD"""
        return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkImageToMeshFilterIUC3MD3STD33DD

        Create a new object of the class itkImageToMeshFilterIUC3MD3STD33DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToMeshFilterIUC3MD3STD33DD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToMeshFilterIUC3MD3STD33DD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToMeshFilterIUC3MD3STD33DD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToMeshFilterIUC3MD3STD33DD.SetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_SetInput, None, itkImageToMeshFilterIUC3MD3STD33DD)
itkImageToMeshFilterIUC3MD3STD33DD.GetInput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GetInput, None, itkImageToMeshFilterIUC3MD3STD33DD)
itkImageToMeshFilterIUC3MD3STD33DD.GetOutput = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GetOutput, None, itkImageToMeshFilterIUC3MD3STD33DD)
itkImageToMeshFilterIUC3MD3STD33DD.GenerateOutputInformation = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GenerateOutputInformation, None, itkImageToMeshFilterIUC3MD3STD33DD)
itkImageToMeshFilterIUC3MD3STD33DD.GetPointer = new_instancemethod(_itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_GetPointer, None, itkImageToMeshFilterIUC3MD3STD33DD)
itkImageToMeshFilterIUC3MD3STD33DD_swigregister = _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_swigregister
itkImageToMeshFilterIUC3MD3STD33DD_swigregister(itkImageToMeshFilterIUC3MD3STD33DD)

def itkImageToMeshFilterIUC3MD3STD33DD_cast(obj):
    """itkImageToMeshFilterIUC3MD3STD33DD_cast(itkLightObject obj) -> itkImageToMeshFilterIUC3MD3STD33DD"""
    return _itkImageToMeshFilterPython.itkImageToMeshFilterIUC3MD3STD33DD_cast(obj)



