# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelVotingImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkLabelVotingImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkLabelVotingImageFilterPython')
    _itkLabelVotingImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelVotingImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelVotingImageFilterPython
            return _itkLabelVotingImageFilterPython
        try:
            _mod = imp.load_module('_itkLabelVotingImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkLabelVotingImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelVotingImageFilterPython
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
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkOffsetPython
import itkSizePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkIndexPython
import ITKCommonBasePython
import itkImageRegionPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkLabelVotingImageFilterIUC3IUC3_New():
  return itkLabelVotingImageFilterIUC3IUC3.New()


def itkLabelVotingImageFilterIUC2IUC2_New():
  return itkLabelVotingImageFilterIUC2IUC2.New()

class itkLabelVotingImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """Proxy of C++ itkLabelVotingImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelVotingImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkLabelVotingImageFilterIUC2IUC2_Pointer"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelVotingImageFilterIUC2IUC2_Pointer":
        """Clone(itkLabelVotingImageFilterIUC2IUC2 self) -> itkLabelVotingImageFilterIUC2IUC2_Pointer"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_Clone(self)


    def SetLabelForUndecidedPixels(self, l: 'unsigned char const') -> "void":
        """SetLabelForUndecidedPixels(itkLabelVotingImageFilterIUC2IUC2 self, unsigned char const l)"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_SetLabelForUndecidedPixels(self, l)


    def GetLabelForUndecidedPixels(self) -> "unsigned char":
        """GetLabelForUndecidedPixels(itkLabelVotingImageFilterIUC2IUC2 self) -> unsigned char"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_GetLabelForUndecidedPixels(self)


    def UnsetLabelForUndecidedPixels(self) -> "void":
        """UnsetLabelForUndecidedPixels(itkLabelVotingImageFilterIUC2IUC2 self)"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_UnsetLabelForUndecidedPixels(self)

    InputConvertibleToOutputCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    IntConvertibleToInputCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_IntConvertibleToInputCheck
    SameDimensionCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_SameDimensionCheck
    InputUnsignedIntCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_InputUnsignedIntCheck
    IntConvertibleToOutputPixelType = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_IntConvertibleToOutputPixelType
    InputPlusIntCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_InputPlusIntCheck
    InputIncrementDecrementOperatorsCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_InputIncrementDecrementOperatorsCheck
    OutputOStreamWritableCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_OutputOStreamWritableCheck
    __swig_destroy__ = _itkLabelVotingImageFilterPython.delete_itkLabelVotingImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkLabelVotingImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkLabelVotingImageFilterIUC2IUC2"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelVotingImageFilterIUC2IUC2 *":
        """GetPointer(itkLabelVotingImageFilterIUC2IUC2 self) -> itkLabelVotingImageFilterIUC2IUC2"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelVotingImageFilterIUC2IUC2

        Create a new object of the class itkLabelVotingImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelVotingImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelVotingImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelVotingImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelVotingImageFilterIUC2IUC2.Clone = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_Clone, None, itkLabelVotingImageFilterIUC2IUC2)
itkLabelVotingImageFilterIUC2IUC2.SetLabelForUndecidedPixels = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_SetLabelForUndecidedPixels, None, itkLabelVotingImageFilterIUC2IUC2)
itkLabelVotingImageFilterIUC2IUC2.GetLabelForUndecidedPixels = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_GetLabelForUndecidedPixels, None, itkLabelVotingImageFilterIUC2IUC2)
itkLabelVotingImageFilterIUC2IUC2.UnsetLabelForUndecidedPixels = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_UnsetLabelForUndecidedPixels, None, itkLabelVotingImageFilterIUC2IUC2)
itkLabelVotingImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_GetPointer, None, itkLabelVotingImageFilterIUC2IUC2)
itkLabelVotingImageFilterIUC2IUC2_swigregister = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_swigregister
itkLabelVotingImageFilterIUC2IUC2_swigregister(itkLabelVotingImageFilterIUC2IUC2)

def itkLabelVotingImageFilterIUC2IUC2___New_orig__() -> "itkLabelVotingImageFilterIUC2IUC2_Pointer":
    """itkLabelVotingImageFilterIUC2IUC2___New_orig__() -> itkLabelVotingImageFilterIUC2IUC2_Pointer"""
    return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2___New_orig__()

def itkLabelVotingImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkLabelVotingImageFilterIUC2IUC2 *":
    """itkLabelVotingImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkLabelVotingImageFilterIUC2IUC2"""
    return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC2IUC2_cast(obj)

class itkLabelVotingImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """Proxy of C++ itkLabelVotingImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelVotingImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkLabelVotingImageFilterIUC3IUC3_Pointer"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelVotingImageFilterIUC3IUC3_Pointer":
        """Clone(itkLabelVotingImageFilterIUC3IUC3 self) -> itkLabelVotingImageFilterIUC3IUC3_Pointer"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_Clone(self)


    def SetLabelForUndecidedPixels(self, l: 'unsigned char const') -> "void":
        """SetLabelForUndecidedPixels(itkLabelVotingImageFilterIUC3IUC3 self, unsigned char const l)"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_SetLabelForUndecidedPixels(self, l)


    def GetLabelForUndecidedPixels(self) -> "unsigned char":
        """GetLabelForUndecidedPixels(itkLabelVotingImageFilterIUC3IUC3 self) -> unsigned char"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_GetLabelForUndecidedPixels(self)


    def UnsetLabelForUndecidedPixels(self) -> "void":
        """UnsetLabelForUndecidedPixels(itkLabelVotingImageFilterIUC3IUC3 self)"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_UnsetLabelForUndecidedPixels(self)

    InputConvertibleToOutputCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    IntConvertibleToInputCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_IntConvertibleToInputCheck
    SameDimensionCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_SameDimensionCheck
    InputUnsignedIntCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_InputUnsignedIntCheck
    IntConvertibleToOutputPixelType = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_IntConvertibleToOutputPixelType
    InputPlusIntCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_InputPlusIntCheck
    InputIncrementDecrementOperatorsCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_InputIncrementDecrementOperatorsCheck
    OutputOStreamWritableCheck = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_OutputOStreamWritableCheck
    __swig_destroy__ = _itkLabelVotingImageFilterPython.delete_itkLabelVotingImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkLabelVotingImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkLabelVotingImageFilterIUC3IUC3"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkLabelVotingImageFilterIUC3IUC3 *":
        """GetPointer(itkLabelVotingImageFilterIUC3IUC3 self) -> itkLabelVotingImageFilterIUC3IUC3"""
        return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkLabelVotingImageFilterIUC3IUC3

        Create a new object of the class itkLabelVotingImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelVotingImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelVotingImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelVotingImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelVotingImageFilterIUC3IUC3.Clone = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_Clone, None, itkLabelVotingImageFilterIUC3IUC3)
itkLabelVotingImageFilterIUC3IUC3.SetLabelForUndecidedPixels = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_SetLabelForUndecidedPixels, None, itkLabelVotingImageFilterIUC3IUC3)
itkLabelVotingImageFilterIUC3IUC3.GetLabelForUndecidedPixels = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_GetLabelForUndecidedPixels, None, itkLabelVotingImageFilterIUC3IUC3)
itkLabelVotingImageFilterIUC3IUC3.UnsetLabelForUndecidedPixels = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_UnsetLabelForUndecidedPixels, None, itkLabelVotingImageFilterIUC3IUC3)
itkLabelVotingImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_GetPointer, None, itkLabelVotingImageFilterIUC3IUC3)
itkLabelVotingImageFilterIUC3IUC3_swigregister = _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_swigregister
itkLabelVotingImageFilterIUC3IUC3_swigregister(itkLabelVotingImageFilterIUC3IUC3)

def itkLabelVotingImageFilterIUC3IUC3___New_orig__() -> "itkLabelVotingImageFilterIUC3IUC3_Pointer":
    """itkLabelVotingImageFilterIUC3IUC3___New_orig__() -> itkLabelVotingImageFilterIUC3IUC3_Pointer"""
    return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3___New_orig__()

def itkLabelVotingImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkLabelVotingImageFilterIUC3IUC3 *":
    """itkLabelVotingImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkLabelVotingImageFilterIUC3IUC3"""
    return _itkLabelVotingImageFilterPython.itkLabelVotingImageFilterIUC3IUC3_cast(obj)



