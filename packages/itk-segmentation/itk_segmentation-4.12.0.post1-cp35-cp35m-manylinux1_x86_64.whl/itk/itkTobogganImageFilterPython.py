# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTobogganImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTobogganImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTobogganImageFilterPython')
    _itkTobogganImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTobogganImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkTobogganImageFilterPython
            return _itkTobogganImageFilterPython
        try:
            _mod = imp.load_module('_itkTobogganImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTobogganImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTobogganImageFilterPython
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


import itkImageToImageFilterAPython
import itkVectorImagePython
import ITKCommonBasePython
import pyBasePython
import stdcomplexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkTobogganImageFilterIF3_New():
  return itkTobogganImageFilterIF3.New()


def itkTobogganImageFilterIF2_New():
  return itkTobogganImageFilterIF2.New()


def itkTobogganImageFilterIUC3_New():
  return itkTobogganImageFilterIUC3.New()


def itkTobogganImageFilterIUC2_New():
  return itkTobogganImageFilterIUC2.New()


def itkTobogganImageFilterISS3_New():
  return itkTobogganImageFilterISS3.New()


def itkTobogganImageFilterISS2_New():
  return itkTobogganImageFilterISS2.New()

class itkTobogganImageFilterIF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IUL2):
    """Proxy of C++ itkTobogganImageFilterIF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ImageDimension = _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_ImageDimension

    def __New_orig__() -> "itkTobogganImageFilterIF2_Pointer":
        """__New_orig__() -> itkTobogganImageFilterIF2_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTobogganImageFilterIF2_Pointer":
        """Clone(itkTobogganImageFilterIF2 self) -> itkTobogganImageFilterIF2_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkTobogganImageFilterIF2 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_GenerateData(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkTobogganImageFilterIF2 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_GenerateInputRequestedRegion(self)

    LessThanComparableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_LessThanComparableCheck
    OStreamWritableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_OStreamWritableCheck
    __swig_destroy__ = _itkTobogganImageFilterPython.delete_itkTobogganImageFilterIF2

    def cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIF2 *":
        """cast(itkLightObject obj) -> itkTobogganImageFilterIF2"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTobogganImageFilterIF2 *":
        """GetPointer(itkTobogganImageFilterIF2 self) -> itkTobogganImageFilterIF2"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTobogganImageFilterIF2

        Create a new object of the class itkTobogganImageFilterIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTobogganImageFilterIF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTobogganImageFilterIF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTobogganImageFilterIF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTobogganImageFilterIF2.Clone = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF2_Clone, None, itkTobogganImageFilterIF2)
itkTobogganImageFilterIF2.GenerateData = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF2_GenerateData, None, itkTobogganImageFilterIF2)
itkTobogganImageFilterIF2.GenerateInputRequestedRegion = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF2_GenerateInputRequestedRegion, None, itkTobogganImageFilterIF2)
itkTobogganImageFilterIF2.GetPointer = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF2_GetPointer, None, itkTobogganImageFilterIF2)
itkTobogganImageFilterIF2_swigregister = _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_swigregister
itkTobogganImageFilterIF2_swigregister(itkTobogganImageFilterIF2)

def itkTobogganImageFilterIF2___New_orig__() -> "itkTobogganImageFilterIF2_Pointer":
    """itkTobogganImageFilterIF2___New_orig__() -> itkTobogganImageFilterIF2_Pointer"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2___New_orig__()

def itkTobogganImageFilterIF2_cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIF2 *":
    """itkTobogganImageFilterIF2_cast(itkLightObject obj) -> itkTobogganImageFilterIF2"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIF2_cast(obj)

class itkTobogganImageFilterIF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IUL3):
    """Proxy of C++ itkTobogganImageFilterIF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ImageDimension = _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_ImageDimension

    def __New_orig__() -> "itkTobogganImageFilterIF3_Pointer":
        """__New_orig__() -> itkTobogganImageFilterIF3_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTobogganImageFilterIF3_Pointer":
        """Clone(itkTobogganImageFilterIF3 self) -> itkTobogganImageFilterIF3_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkTobogganImageFilterIF3 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_GenerateData(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkTobogganImageFilterIF3 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_GenerateInputRequestedRegion(self)

    LessThanComparableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_LessThanComparableCheck
    OStreamWritableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_OStreamWritableCheck
    __swig_destroy__ = _itkTobogganImageFilterPython.delete_itkTobogganImageFilterIF3

    def cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIF3 *":
        """cast(itkLightObject obj) -> itkTobogganImageFilterIF3"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTobogganImageFilterIF3 *":
        """GetPointer(itkTobogganImageFilterIF3 self) -> itkTobogganImageFilterIF3"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTobogganImageFilterIF3

        Create a new object of the class itkTobogganImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTobogganImageFilterIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTobogganImageFilterIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTobogganImageFilterIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTobogganImageFilterIF3.Clone = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF3_Clone, None, itkTobogganImageFilterIF3)
itkTobogganImageFilterIF3.GenerateData = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF3_GenerateData, None, itkTobogganImageFilterIF3)
itkTobogganImageFilterIF3.GenerateInputRequestedRegion = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF3_GenerateInputRequestedRegion, None, itkTobogganImageFilterIF3)
itkTobogganImageFilterIF3.GetPointer = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIF3_GetPointer, None, itkTobogganImageFilterIF3)
itkTobogganImageFilterIF3_swigregister = _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_swigregister
itkTobogganImageFilterIF3_swigregister(itkTobogganImageFilterIF3)

def itkTobogganImageFilterIF3___New_orig__() -> "itkTobogganImageFilterIF3_Pointer":
    """itkTobogganImageFilterIF3___New_orig__() -> itkTobogganImageFilterIF3_Pointer"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3___New_orig__()

def itkTobogganImageFilterIF3_cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIF3 *":
    """itkTobogganImageFilterIF3_cast(itkLightObject obj) -> itkTobogganImageFilterIF3"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIF3_cast(obj)

class itkTobogganImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2IUL2):
    """Proxy of C++ itkTobogganImageFilterISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ImageDimension = _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_ImageDimension

    def __New_orig__() -> "itkTobogganImageFilterISS2_Pointer":
        """__New_orig__() -> itkTobogganImageFilterISS2_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTobogganImageFilterISS2_Pointer":
        """Clone(itkTobogganImageFilterISS2 self) -> itkTobogganImageFilterISS2_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkTobogganImageFilterISS2 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_GenerateData(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkTobogganImageFilterISS2 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_GenerateInputRequestedRegion(self)

    LessThanComparableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_LessThanComparableCheck
    OStreamWritableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_OStreamWritableCheck
    __swig_destroy__ = _itkTobogganImageFilterPython.delete_itkTobogganImageFilterISS2

    def cast(obj: 'itkLightObject') -> "itkTobogganImageFilterISS2 *":
        """cast(itkLightObject obj) -> itkTobogganImageFilterISS2"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTobogganImageFilterISS2 *":
        """GetPointer(itkTobogganImageFilterISS2 self) -> itkTobogganImageFilterISS2"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTobogganImageFilterISS2

        Create a new object of the class itkTobogganImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTobogganImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTobogganImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTobogganImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTobogganImageFilterISS2.Clone = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS2_Clone, None, itkTobogganImageFilterISS2)
itkTobogganImageFilterISS2.GenerateData = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS2_GenerateData, None, itkTobogganImageFilterISS2)
itkTobogganImageFilterISS2.GenerateInputRequestedRegion = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS2_GenerateInputRequestedRegion, None, itkTobogganImageFilterISS2)
itkTobogganImageFilterISS2.GetPointer = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS2_GetPointer, None, itkTobogganImageFilterISS2)
itkTobogganImageFilterISS2_swigregister = _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_swigregister
itkTobogganImageFilterISS2_swigregister(itkTobogganImageFilterISS2)

def itkTobogganImageFilterISS2___New_orig__() -> "itkTobogganImageFilterISS2_Pointer":
    """itkTobogganImageFilterISS2___New_orig__() -> itkTobogganImageFilterISS2_Pointer"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2___New_orig__()

def itkTobogganImageFilterISS2_cast(obj: 'itkLightObject') -> "itkTobogganImageFilterISS2 *":
    """itkTobogganImageFilterISS2_cast(itkLightObject obj) -> itkTobogganImageFilterISS2"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterISS2_cast(obj)

class itkTobogganImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3IUL3):
    """Proxy of C++ itkTobogganImageFilterISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ImageDimension = _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_ImageDimension

    def __New_orig__() -> "itkTobogganImageFilterISS3_Pointer":
        """__New_orig__() -> itkTobogganImageFilterISS3_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTobogganImageFilterISS3_Pointer":
        """Clone(itkTobogganImageFilterISS3 self) -> itkTobogganImageFilterISS3_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkTobogganImageFilterISS3 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_GenerateData(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkTobogganImageFilterISS3 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_GenerateInputRequestedRegion(self)

    LessThanComparableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_LessThanComparableCheck
    OStreamWritableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_OStreamWritableCheck
    __swig_destroy__ = _itkTobogganImageFilterPython.delete_itkTobogganImageFilterISS3

    def cast(obj: 'itkLightObject') -> "itkTobogganImageFilterISS3 *":
        """cast(itkLightObject obj) -> itkTobogganImageFilterISS3"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTobogganImageFilterISS3 *":
        """GetPointer(itkTobogganImageFilterISS3 self) -> itkTobogganImageFilterISS3"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTobogganImageFilterISS3

        Create a new object of the class itkTobogganImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTobogganImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTobogganImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTobogganImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTobogganImageFilterISS3.Clone = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS3_Clone, None, itkTobogganImageFilterISS3)
itkTobogganImageFilterISS3.GenerateData = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS3_GenerateData, None, itkTobogganImageFilterISS3)
itkTobogganImageFilterISS3.GenerateInputRequestedRegion = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS3_GenerateInputRequestedRegion, None, itkTobogganImageFilterISS3)
itkTobogganImageFilterISS3.GetPointer = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterISS3_GetPointer, None, itkTobogganImageFilterISS3)
itkTobogganImageFilterISS3_swigregister = _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_swigregister
itkTobogganImageFilterISS3_swigregister(itkTobogganImageFilterISS3)

def itkTobogganImageFilterISS3___New_orig__() -> "itkTobogganImageFilterISS3_Pointer":
    """itkTobogganImageFilterISS3___New_orig__() -> itkTobogganImageFilterISS3_Pointer"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3___New_orig__()

def itkTobogganImageFilterISS3_cast(obj: 'itkLightObject') -> "itkTobogganImageFilterISS3 *":
    """itkTobogganImageFilterISS3_cast(itkLightObject obj) -> itkTobogganImageFilterISS3"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterISS3_cast(obj)

class itkTobogganImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUL2):
    """Proxy of C++ itkTobogganImageFilterIUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ImageDimension = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_ImageDimension

    def __New_orig__() -> "itkTobogganImageFilterIUC2_Pointer":
        """__New_orig__() -> itkTobogganImageFilterIUC2_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTobogganImageFilterIUC2_Pointer":
        """Clone(itkTobogganImageFilterIUC2 self) -> itkTobogganImageFilterIUC2_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkTobogganImageFilterIUC2 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_GenerateData(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkTobogganImageFilterIUC2 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_GenerateInputRequestedRegion(self)

    LessThanComparableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_LessThanComparableCheck
    OStreamWritableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_OStreamWritableCheck
    __swig_destroy__ = _itkTobogganImageFilterPython.delete_itkTobogganImageFilterIUC2

    def cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIUC2 *":
        """cast(itkLightObject obj) -> itkTobogganImageFilterIUC2"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTobogganImageFilterIUC2 *":
        """GetPointer(itkTobogganImageFilterIUC2 self) -> itkTobogganImageFilterIUC2"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTobogganImageFilterIUC2

        Create a new object of the class itkTobogganImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTobogganImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTobogganImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTobogganImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTobogganImageFilterIUC2.Clone = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_Clone, None, itkTobogganImageFilterIUC2)
itkTobogganImageFilterIUC2.GenerateData = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_GenerateData, None, itkTobogganImageFilterIUC2)
itkTobogganImageFilterIUC2.GenerateInputRequestedRegion = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_GenerateInputRequestedRegion, None, itkTobogganImageFilterIUC2)
itkTobogganImageFilterIUC2.GetPointer = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_GetPointer, None, itkTobogganImageFilterIUC2)
itkTobogganImageFilterIUC2_swigregister = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_swigregister
itkTobogganImageFilterIUC2_swigregister(itkTobogganImageFilterIUC2)

def itkTobogganImageFilterIUC2___New_orig__() -> "itkTobogganImageFilterIUC2_Pointer":
    """itkTobogganImageFilterIUC2___New_orig__() -> itkTobogganImageFilterIUC2_Pointer"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2___New_orig__()

def itkTobogganImageFilterIUC2_cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIUC2 *":
    """itkTobogganImageFilterIUC2_cast(itkLightObject obj) -> itkTobogganImageFilterIUC2"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC2_cast(obj)

class itkTobogganImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUL3):
    """Proxy of C++ itkTobogganImageFilterIUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    ImageDimension = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_ImageDimension

    def __New_orig__() -> "itkTobogganImageFilterIUC3_Pointer":
        """__New_orig__() -> itkTobogganImageFilterIUC3_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTobogganImageFilterIUC3_Pointer":
        """Clone(itkTobogganImageFilterIUC3 self) -> itkTobogganImageFilterIUC3_Pointer"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_Clone(self)


    def GenerateData(self) -> "void":
        """GenerateData(itkTobogganImageFilterIUC3 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_GenerateData(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkTobogganImageFilterIUC3 self)"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_GenerateInputRequestedRegion(self)

    LessThanComparableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_LessThanComparableCheck
    OStreamWritableCheck = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_OStreamWritableCheck
    __swig_destroy__ = _itkTobogganImageFilterPython.delete_itkTobogganImageFilterIUC3

    def cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIUC3 *":
        """cast(itkLightObject obj) -> itkTobogganImageFilterIUC3"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTobogganImageFilterIUC3 *":
        """GetPointer(itkTobogganImageFilterIUC3 self) -> itkTobogganImageFilterIUC3"""
        return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTobogganImageFilterIUC3

        Create a new object of the class itkTobogganImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTobogganImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTobogganImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTobogganImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTobogganImageFilterIUC3.Clone = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_Clone, None, itkTobogganImageFilterIUC3)
itkTobogganImageFilterIUC3.GenerateData = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_GenerateData, None, itkTobogganImageFilterIUC3)
itkTobogganImageFilterIUC3.GenerateInputRequestedRegion = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_GenerateInputRequestedRegion, None, itkTobogganImageFilterIUC3)
itkTobogganImageFilterIUC3.GetPointer = new_instancemethod(_itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_GetPointer, None, itkTobogganImageFilterIUC3)
itkTobogganImageFilterIUC3_swigregister = _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_swigregister
itkTobogganImageFilterIUC3_swigregister(itkTobogganImageFilterIUC3)

def itkTobogganImageFilterIUC3___New_orig__() -> "itkTobogganImageFilterIUC3_Pointer":
    """itkTobogganImageFilterIUC3___New_orig__() -> itkTobogganImageFilterIUC3_Pointer"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3___New_orig__()

def itkTobogganImageFilterIUC3_cast(obj: 'itkLightObject') -> "itkTobogganImageFilterIUC3 *":
    """itkTobogganImageFilterIUC3_cast(itkLightObject obj) -> itkTobogganImageFilterIUC3"""
    return _itkTobogganImageFilterPython.itkTobogganImageFilterIUC3_cast(obj)



