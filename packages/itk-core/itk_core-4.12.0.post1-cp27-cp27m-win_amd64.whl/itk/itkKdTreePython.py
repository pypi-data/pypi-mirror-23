# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkKdTreePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkKdTreePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkKdTreePython')
    _itkKdTreePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkKdTreePython', [dirname(__file__)])
        except ImportError:
            import _itkKdTreePython
            return _itkKdTreePython
        try:
            _mod = imp.load_module('_itkKdTreePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkKdTreePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkKdTreePython
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


import itkListSamplePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkSamplePython
import ITKCommonBasePython
import itkArrayPython
import itkEuclideanDistanceMetricPython
import itkDistanceMetricPython
import itkFunctionBasePython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkPointPython
import itkRGBAPixelPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkImageRegionPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkSymmetricSecondRankTensorPython

def itkKdTreeLSVF3_New():
  return itkKdTreeLSVF3.New()


def itkKdTreeLSVF2_New():
  return itkKdTreeLSVF2.New()

class itkKdTreeLSVF2(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkKdTreeLSVF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkKdTreeLSVF2_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkKdTreeLSVF2 self) -> itkKdTreeLSVF2_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF2_Clone(self)


    def GetMeasurementVectorSize(self):
        """GetMeasurementVectorSize(itkKdTreeLSVF2 self) -> unsigned int"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVectorSize(self)


    def SetBucketSize(self, arg0):
        """SetBucketSize(itkKdTreeLSVF2 self, unsigned int arg0)"""
        return _itkKdTreePython.itkKdTreeLSVF2_SetBucketSize(self, arg0)


    def SetSample(self, arg0):
        """SetSample(itkKdTreeLSVF2 self, itkListSampleVF2 arg0)"""
        return _itkKdTreePython.itkKdTreeLSVF2_SetSample(self, arg0)


    def GetSample(self):
        """GetSample(itkKdTreeLSVF2 self) -> itkListSampleVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetSample(self)


    def Size(self):
        """Size(itkKdTreeLSVF2 self) -> unsigned long long"""
        return _itkKdTreePython.itkKdTreeLSVF2_Size(self)


    def GetEmptyTerminalNode(self):
        """GetEmptyTerminalNode(itkKdTreeLSVF2 self) -> itkKdTreeNodeLSVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetEmptyTerminalNode(self)


    def SetRoot(self, root):
        """SetRoot(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 root)"""
        return _itkKdTreePython.itkKdTreeLSVF2_SetRoot(self, root)


    def GetRoot(self):
        """GetRoot(itkKdTreeLSVF2 self) -> itkKdTreeNodeLSVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetRoot(self)


    def GetMeasurementVector(self, id):
        """GetMeasurementVector(itkKdTreeLSVF2 self, unsigned long long id) -> itkVectorF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVector(self, id)


    def GetFrequency(self, id):
        """GetFrequency(itkKdTreeLSVF2 self, unsigned long long id) -> unsigned long long"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetFrequency(self, id)


    def GetDistanceMetric(self):
        """GetDistanceMetric(itkKdTreeLSVF2 self) -> itkEuclideanDistanceMetricVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetDistanceMetric(self)


    def Search(self, *args):
        """
        Search(itkKdTreeLSVF2 self, itkVectorF2 arg0, unsigned int arg1, std::vector< unsigned long long,std::allocator< unsigned long long > > & arg2)
        Search(itkKdTreeLSVF2 self, itkVectorF2 arg0, unsigned int arg1, std::vector< unsigned long long,std::allocator< unsigned long long > > & arg2, vectorD arg3)
        Search(itkKdTreeLSVF2 self, itkVectorF2 arg0, double arg1, std::vector< unsigned long long,std::allocator< unsigned long long > > & arg2)
        """
        return _itkKdTreePython.itkKdTreeLSVF2_Search(self, *args)


    def BallWithinBounds(self, arg0, arg1, arg2, arg3):
        """BallWithinBounds(itkKdTreeLSVF2 self, itkVectorF2 arg0, itkVectorF2 arg1, itkVectorF2 arg2, double arg3) -> bool"""
        return _itkKdTreePython.itkKdTreeLSVF2_BallWithinBounds(self, arg0, arg1, arg2, arg3)


    def BoundsOverlapBall(self, arg0, arg1, arg2, arg3):
        """BoundsOverlapBall(itkKdTreeLSVF2 self, itkVectorF2 arg0, itkVectorF2 arg1, itkVectorF2 arg2, double arg3) -> bool"""
        return _itkKdTreePython.itkKdTreeLSVF2_BoundsOverlapBall(self, arg0, arg1, arg2, arg3)


    def DeleteNode(self, arg0):
        """DeleteNode(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 arg0)"""
        return _itkKdTreePython.itkKdTreeLSVF2_DeleteNode(self, arg0)


    def PrintTree(self, *args):
        """
        PrintTree(itkKdTreeLSVF2 self, ostream arg0)
        PrintTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 arg0, unsigned int arg1, unsigned int arg2, ostream os)
        PrintTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 arg0, unsigned int arg1, unsigned int arg2)
        """
        return _itkKdTreePython.itkKdTreeLSVF2_PrintTree(self, *args)


    def PlotTree(self, *args):
        """
        PlotTree(itkKdTreeLSVF2 self, ostream os)
        PlotTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 node, ostream os)
        PlotTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 node)
        """
        return _itkKdTreePython.itkKdTreeLSVF2_PlotTree(self, *args)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF2

    def cast(obj):
        """cast(itkLightObject obj) -> itkKdTreeLSVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkKdTreeLSVF2 self) -> itkKdTreeLSVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF2

        Create a new object of the class itkKdTreeLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKdTreeLSVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKdTreeLSVF2.Clone = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_Clone, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetMeasurementVectorSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVectorSize, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.SetBucketSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_SetBucketSize, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.SetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_SetSample, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetSample, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.Size = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_Size, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetEmptyTerminalNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetEmptyTerminalNode, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.SetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_SetRoot, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetRoot, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetMeasurementVector = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVector, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetFrequency = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetFrequency, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetDistanceMetric = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetDistanceMetric, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.Search = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_Search, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.BallWithinBounds = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_BallWithinBounds, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.BoundsOverlapBall = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_BoundsOverlapBall, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.DeleteNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_DeleteNode, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.PrintTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_PrintTree, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.PlotTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_PlotTree, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetPointer = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetPointer, None, itkKdTreeLSVF2)
itkKdTreeLSVF2_swigregister = _itkKdTreePython.itkKdTreeLSVF2_swigregister
itkKdTreeLSVF2_swigregister(itkKdTreeLSVF2)

def itkKdTreeLSVF2___New_orig__():
    """itkKdTreeLSVF2___New_orig__() -> itkKdTreeLSVF2_Pointer"""
    return _itkKdTreePython.itkKdTreeLSVF2___New_orig__()

def itkKdTreeLSVF2_cast(obj):
    """itkKdTreeLSVF2_cast(itkLightObject obj) -> itkKdTreeLSVF2"""
    return _itkKdTreePython.itkKdTreeLSVF2_cast(obj)

class itkKdTreeLSVF3(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkKdTreeLSVF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkKdTreeLSVF3_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkKdTreeLSVF3 self) -> itkKdTreeLSVF3_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF3_Clone(self)


    def GetMeasurementVectorSize(self):
        """GetMeasurementVectorSize(itkKdTreeLSVF3 self) -> unsigned int"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVectorSize(self)


    def SetBucketSize(self, arg0):
        """SetBucketSize(itkKdTreeLSVF3 self, unsigned int arg0)"""
        return _itkKdTreePython.itkKdTreeLSVF3_SetBucketSize(self, arg0)


    def SetSample(self, arg0):
        """SetSample(itkKdTreeLSVF3 self, itkListSampleVF3 arg0)"""
        return _itkKdTreePython.itkKdTreeLSVF3_SetSample(self, arg0)


    def GetSample(self):
        """GetSample(itkKdTreeLSVF3 self) -> itkListSampleVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetSample(self)


    def Size(self):
        """Size(itkKdTreeLSVF3 self) -> unsigned long long"""
        return _itkKdTreePython.itkKdTreeLSVF3_Size(self)


    def GetEmptyTerminalNode(self):
        """GetEmptyTerminalNode(itkKdTreeLSVF3 self) -> itkKdTreeNodeLSVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetEmptyTerminalNode(self)


    def SetRoot(self, root):
        """SetRoot(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 root)"""
        return _itkKdTreePython.itkKdTreeLSVF3_SetRoot(self, root)


    def GetRoot(self):
        """GetRoot(itkKdTreeLSVF3 self) -> itkKdTreeNodeLSVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetRoot(self)


    def GetMeasurementVector(self, id):
        """GetMeasurementVector(itkKdTreeLSVF3 self, unsigned long long id) -> itkVectorF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVector(self, id)


    def GetFrequency(self, id):
        """GetFrequency(itkKdTreeLSVF3 self, unsigned long long id) -> unsigned long long"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetFrequency(self, id)


    def GetDistanceMetric(self):
        """GetDistanceMetric(itkKdTreeLSVF3 self) -> itkEuclideanDistanceMetricVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetDistanceMetric(self)


    def Search(self, *args):
        """
        Search(itkKdTreeLSVF3 self, itkVectorF3 arg0, unsigned int arg1, std::vector< unsigned long long,std::allocator< unsigned long long > > & arg2)
        Search(itkKdTreeLSVF3 self, itkVectorF3 arg0, unsigned int arg1, std::vector< unsigned long long,std::allocator< unsigned long long > > & arg2, vectorD arg3)
        Search(itkKdTreeLSVF3 self, itkVectorF3 arg0, double arg1, std::vector< unsigned long long,std::allocator< unsigned long long > > & arg2)
        """
        return _itkKdTreePython.itkKdTreeLSVF3_Search(self, *args)


    def BallWithinBounds(self, arg0, arg1, arg2, arg3):
        """BallWithinBounds(itkKdTreeLSVF3 self, itkVectorF3 arg0, itkVectorF3 arg1, itkVectorF3 arg2, double arg3) -> bool"""
        return _itkKdTreePython.itkKdTreeLSVF3_BallWithinBounds(self, arg0, arg1, arg2, arg3)


    def BoundsOverlapBall(self, arg0, arg1, arg2, arg3):
        """BoundsOverlapBall(itkKdTreeLSVF3 self, itkVectorF3 arg0, itkVectorF3 arg1, itkVectorF3 arg2, double arg3) -> bool"""
        return _itkKdTreePython.itkKdTreeLSVF3_BoundsOverlapBall(self, arg0, arg1, arg2, arg3)


    def DeleteNode(self, arg0):
        """DeleteNode(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 arg0)"""
        return _itkKdTreePython.itkKdTreeLSVF3_DeleteNode(self, arg0)


    def PrintTree(self, *args):
        """
        PrintTree(itkKdTreeLSVF3 self, ostream arg0)
        PrintTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 arg0, unsigned int arg1, unsigned int arg2, ostream os)
        PrintTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 arg0, unsigned int arg1, unsigned int arg2)
        """
        return _itkKdTreePython.itkKdTreeLSVF3_PrintTree(self, *args)


    def PlotTree(self, *args):
        """
        PlotTree(itkKdTreeLSVF3 self, ostream os)
        PlotTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 node, ostream os)
        PlotTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 node)
        """
        return _itkKdTreePython.itkKdTreeLSVF3_PlotTree(self, *args)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF3

    def cast(obj):
        """cast(itkLightObject obj) -> itkKdTreeLSVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkKdTreeLSVF3 self) -> itkKdTreeLSVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF3

        Create a new object of the class itkKdTreeLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKdTreeLSVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKdTreeLSVF3.Clone = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_Clone, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetMeasurementVectorSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVectorSize, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.SetBucketSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_SetBucketSize, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.SetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_SetSample, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetSample, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.Size = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_Size, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetEmptyTerminalNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetEmptyTerminalNode, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.SetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_SetRoot, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetRoot, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetMeasurementVector = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVector, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetFrequency = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetFrequency, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetDistanceMetric = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetDistanceMetric, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.Search = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_Search, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.BallWithinBounds = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_BallWithinBounds, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.BoundsOverlapBall = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_BoundsOverlapBall, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.DeleteNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_DeleteNode, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.PrintTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_PrintTree, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.PlotTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_PlotTree, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetPointer = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetPointer, None, itkKdTreeLSVF3)
itkKdTreeLSVF3_swigregister = _itkKdTreePython.itkKdTreeLSVF3_swigregister
itkKdTreeLSVF3_swigregister(itkKdTreeLSVF3)

def itkKdTreeLSVF3___New_orig__():
    """itkKdTreeLSVF3___New_orig__() -> itkKdTreeLSVF3_Pointer"""
    return _itkKdTreePython.itkKdTreeLSVF3___New_orig__()

def itkKdTreeLSVF3_cast(obj):
    """itkKdTreeLSVF3_cast(itkLightObject obj) -> itkKdTreeLSVF3"""
    return _itkKdTreePython.itkKdTreeLSVF3_cast(obj)

class itkKdTreeNodeLSVF2(object):
    """Proxy of C++ itkKdTreeNodeLSVF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def IsTerminal(self):
        """IsTerminal(itkKdTreeNodeLSVF2 self) -> bool"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_IsTerminal(self)


    def GetParameters(self, arg0, arg1):
        """GetParameters(itkKdTreeNodeLSVF2 self, unsigned int & arg0, float & arg1)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetParameters(self, arg0, arg1)


    def Left(self, *args):
        """
        Left(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        Left(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF2_Left(self, *args)


    def Right(self, *args):
        """
        Right(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        Right(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF2_Right(self, *args)


    def Size(self):
        """Size(itkKdTreeNodeLSVF2 self) -> unsigned int"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_Size(self)


    def GetWeightedCentroid(self, arg0):
        """GetWeightedCentroid(itkKdTreeNodeLSVF2 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetWeightedCentroid(self, arg0)


    def GetCentroid(self, arg0):
        """GetCentroid(itkKdTreeNodeLSVF2 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetCentroid(self, arg0)


    def GetInstanceIdentifier(self, arg0):
        """GetInstanceIdentifier(itkKdTreeNodeLSVF2 self, unsigned long long arg0) -> unsigned long long"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetInstanceIdentifier(self, arg0)


    def AddInstanceIdentifier(self, arg0):
        """AddInstanceIdentifier(itkKdTreeNodeLSVF2 self, unsigned long long arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_AddInstanceIdentifier(self, arg0)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF2
itkKdTreeNodeLSVF2.IsTerminal = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_IsTerminal, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetParameters = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetParameters, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.Left = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_Left, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.Right = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_Right, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.Size = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_Size, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetWeightedCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetWeightedCentroid, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetCentroid, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetInstanceIdentifier, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.AddInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_AddInstanceIdentifier, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2_swigregister = _itkKdTreePython.itkKdTreeNodeLSVF2_swigregister
itkKdTreeNodeLSVF2_swigregister(itkKdTreeNodeLSVF2)

class itkKdTreeNodeLSVF3(object):
    """Proxy of C++ itkKdTreeNodeLSVF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def IsTerminal(self):
        """IsTerminal(itkKdTreeNodeLSVF3 self) -> bool"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_IsTerminal(self)


    def GetParameters(self, arg0, arg1):
        """GetParameters(itkKdTreeNodeLSVF3 self, unsigned int & arg0, float & arg1)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetParameters(self, arg0, arg1)


    def Left(self, *args):
        """
        Left(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        Left(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF3_Left(self, *args)


    def Right(self, *args):
        """
        Right(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        Right(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF3_Right(self, *args)


    def Size(self):
        """Size(itkKdTreeNodeLSVF3 self) -> unsigned int"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_Size(self)


    def GetWeightedCentroid(self, arg0):
        """GetWeightedCentroid(itkKdTreeNodeLSVF3 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetWeightedCentroid(self, arg0)


    def GetCentroid(self, arg0):
        """GetCentroid(itkKdTreeNodeLSVF3 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetCentroid(self, arg0)


    def GetInstanceIdentifier(self, arg0):
        """GetInstanceIdentifier(itkKdTreeNodeLSVF3 self, unsigned long long arg0) -> unsigned long long"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetInstanceIdentifier(self, arg0)


    def AddInstanceIdentifier(self, arg0):
        """AddInstanceIdentifier(itkKdTreeNodeLSVF3 self, unsigned long long arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_AddInstanceIdentifier(self, arg0)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF3
itkKdTreeNodeLSVF3.IsTerminal = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_IsTerminal, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetParameters = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetParameters, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.Left = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_Left, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.Right = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_Right, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.Size = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_Size, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetWeightedCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetWeightedCentroid, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetCentroid, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetInstanceIdentifier, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.AddInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_AddInstanceIdentifier, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3_swigregister = _itkKdTreePython.itkKdTreeNodeLSVF3_swigregister
itkKdTreeNodeLSVF3_swigregister(itkKdTreeNodeLSVF3)



