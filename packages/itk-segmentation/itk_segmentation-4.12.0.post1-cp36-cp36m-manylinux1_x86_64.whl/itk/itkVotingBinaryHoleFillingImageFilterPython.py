# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVotingBinaryHoleFillingImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkVotingBinaryHoleFillingImageFilterPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkVotingBinaryHoleFillingImageFilterPython')
    _itkVotingBinaryHoleFillingImageFilterPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVotingBinaryHoleFillingImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkVotingBinaryHoleFillingImageFilterPython
            return _itkVotingBinaryHoleFillingImageFilterPython
        try:
            _mod = imp.load_module('_itkVotingBinaryHoleFillingImageFilterPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkVotingBinaryHoleFillingImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVotingBinaryHoleFillingImageFilterPython
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


import itkImageRegionPython
import itkIndexPython
import itkSizePython
import pyBasePython
import itkOffsetPython
import ITKCommonBasePython
import itkVotingBinaryImageFilterPython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkVotingBinaryHoleFillingImageFilterISS3ISS3_New():
  return itkVotingBinaryHoleFillingImageFilterISS3ISS3.New()


def itkVotingBinaryHoleFillingImageFilterISS2ISS2_New():
  return itkVotingBinaryHoleFillingImageFilterISS2ISS2.New()


def itkVotingBinaryHoleFillingImageFilterIUC3IUC3_New():
  return itkVotingBinaryHoleFillingImageFilterIUC3IUC3.New()


def itkVotingBinaryHoleFillingImageFilterIUC2IUC2_New():
  return itkVotingBinaryHoleFillingImageFilterIUC2IUC2.New()

class itkVotingBinaryHoleFillingImageFilterISS2ISS2(itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterISS2ISS2):
    """Proxy of C++ itkVotingBinaryHoleFillingImageFilterISS2ISS2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVotingBinaryHoleFillingImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkVotingBinaryHoleFillingImageFilterISS2ISS2_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVotingBinaryHoleFillingImageFilterISS2ISS2_Pointer":
        """Clone(itkVotingBinaryHoleFillingImageFilterISS2ISS2 self) -> itkVotingBinaryHoleFillingImageFilterISS2ISS2_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_Clone(self)


    def GetMajorityThreshold(self) -> "unsigned int const &":
        """GetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterISS2ISS2 self) -> unsigned int const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetMajorityThreshold(self)


    def SetMajorityThreshold(self, _arg: 'unsigned int const') -> "void":
        """SetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterISS2ISS2 self, unsigned int const _arg)"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_SetMajorityThreshold(self, _arg)


    def GetNumberOfPixelsChanged(self) -> "unsigned long const &":
        """GetNumberOfPixelsChanged(itkVotingBinaryHoleFillingImageFilterISS2ISS2 self) -> unsigned long const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetNumberOfPixelsChanged(self)

    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_IntConvertibleToInputCheck
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_UnsignedIntConvertibleToInputCheck
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterISS2ISS2"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVotingBinaryHoleFillingImageFilterISS2ISS2 *":
        """GetPointer(itkVotingBinaryHoleFillingImageFilterISS2ISS2 self) -> itkVotingBinaryHoleFillingImageFilterISS2ISS2"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterISS2ISS2

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVotingBinaryHoleFillingImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVotingBinaryHoleFillingImageFilterISS2ISS2.Clone = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_Clone, None, itkVotingBinaryHoleFillingImageFilterISS2ISS2)
itkVotingBinaryHoleFillingImageFilterISS2ISS2.GetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterISS2ISS2)
itkVotingBinaryHoleFillingImageFilterISS2ISS2.SetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_SetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterISS2ISS2)
itkVotingBinaryHoleFillingImageFilterISS2ISS2.GetNumberOfPixelsChanged = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetNumberOfPixelsChanged, None, itkVotingBinaryHoleFillingImageFilterISS2ISS2)
itkVotingBinaryHoleFillingImageFilterISS2ISS2.GetPointer = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetPointer, None, itkVotingBinaryHoleFillingImageFilterISS2ISS2)
itkVotingBinaryHoleFillingImageFilterISS2ISS2_swigregister = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_swigregister
itkVotingBinaryHoleFillingImageFilterISS2ISS2_swigregister(itkVotingBinaryHoleFillingImageFilterISS2ISS2)

def itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__() -> "itkVotingBinaryHoleFillingImageFilterISS2ISS2_Pointer":
    """itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__() -> itkVotingBinaryHoleFillingImageFilterISS2ISS2_Pointer"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__()

def itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterISS2ISS2 *":
    """itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterISS2ISS2"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast(obj)

class itkVotingBinaryHoleFillingImageFilterISS3ISS3(itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterISS3ISS3):
    """Proxy of C++ itkVotingBinaryHoleFillingImageFilterISS3ISS3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVotingBinaryHoleFillingImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkVotingBinaryHoleFillingImageFilterISS3ISS3_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVotingBinaryHoleFillingImageFilterISS3ISS3_Pointer":
        """Clone(itkVotingBinaryHoleFillingImageFilterISS3ISS3 self) -> itkVotingBinaryHoleFillingImageFilterISS3ISS3_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_Clone(self)


    def GetMajorityThreshold(self) -> "unsigned int const &":
        """GetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterISS3ISS3 self) -> unsigned int const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetMajorityThreshold(self)


    def SetMajorityThreshold(self, _arg: 'unsigned int const') -> "void":
        """SetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterISS3ISS3 self, unsigned int const _arg)"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_SetMajorityThreshold(self, _arg)


    def GetNumberOfPixelsChanged(self) -> "unsigned long const &":
        """GetNumberOfPixelsChanged(itkVotingBinaryHoleFillingImageFilterISS3ISS3 self) -> unsigned long const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetNumberOfPixelsChanged(self)

    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_IntConvertibleToInputCheck
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_UnsignedIntConvertibleToInputCheck
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterISS3ISS3"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVotingBinaryHoleFillingImageFilterISS3ISS3 *":
        """GetPointer(itkVotingBinaryHoleFillingImageFilterISS3ISS3 self) -> itkVotingBinaryHoleFillingImageFilterISS3ISS3"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterISS3ISS3

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVotingBinaryHoleFillingImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVotingBinaryHoleFillingImageFilterISS3ISS3.Clone = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_Clone, None, itkVotingBinaryHoleFillingImageFilterISS3ISS3)
itkVotingBinaryHoleFillingImageFilterISS3ISS3.GetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterISS3ISS3)
itkVotingBinaryHoleFillingImageFilterISS3ISS3.SetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_SetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterISS3ISS3)
itkVotingBinaryHoleFillingImageFilterISS3ISS3.GetNumberOfPixelsChanged = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetNumberOfPixelsChanged, None, itkVotingBinaryHoleFillingImageFilterISS3ISS3)
itkVotingBinaryHoleFillingImageFilterISS3ISS3.GetPointer = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetPointer, None, itkVotingBinaryHoleFillingImageFilterISS3ISS3)
itkVotingBinaryHoleFillingImageFilterISS3ISS3_swigregister = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_swigregister
itkVotingBinaryHoleFillingImageFilterISS3ISS3_swigregister(itkVotingBinaryHoleFillingImageFilterISS3ISS3)

def itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__() -> "itkVotingBinaryHoleFillingImageFilterISS3ISS3_Pointer":
    """itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__() -> itkVotingBinaryHoleFillingImageFilterISS3ISS3_Pointer"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__()

def itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterISS3ISS3 *":
    """itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterISS3ISS3"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast(obj)

class itkVotingBinaryHoleFillingImageFilterIUC2IUC2(itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUC2IUC2):
    """Proxy of C++ itkVotingBinaryHoleFillingImageFilterIUC2IUC2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Pointer":
        """Clone(itkVotingBinaryHoleFillingImageFilterIUC2IUC2 self) -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Clone(self)


    def GetMajorityThreshold(self) -> "unsigned int const &":
        """GetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterIUC2IUC2 self) -> unsigned int const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetMajorityThreshold(self)


    def SetMajorityThreshold(self, _arg: 'unsigned int const') -> "void":
        """SetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterIUC2IUC2 self, unsigned int const _arg)"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_SetMajorityThreshold(self, _arg)


    def GetNumberOfPixelsChanged(self) -> "unsigned long const &":
        """GetNumberOfPixelsChanged(itkVotingBinaryHoleFillingImageFilterIUC2IUC2 self) -> unsigned long const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetNumberOfPixelsChanged(self)

    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_IntConvertibleToInputCheck
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_UnsignedIntConvertibleToInputCheck
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVotingBinaryHoleFillingImageFilterIUC2IUC2 *":
        """GetPointer(itkVotingBinaryHoleFillingImageFilterIUC2IUC2 self) -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVotingBinaryHoleFillingImageFilterIUC2IUC2.Clone = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Clone, None, itkVotingBinaryHoleFillingImageFilterIUC2IUC2)
itkVotingBinaryHoleFillingImageFilterIUC2IUC2.GetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterIUC2IUC2)
itkVotingBinaryHoleFillingImageFilterIUC2IUC2.SetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_SetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterIUC2IUC2)
itkVotingBinaryHoleFillingImageFilterIUC2IUC2.GetNumberOfPixelsChanged = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetNumberOfPixelsChanged, None, itkVotingBinaryHoleFillingImageFilterIUC2IUC2)
itkVotingBinaryHoleFillingImageFilterIUC2IUC2.GetPointer = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetPointer, None, itkVotingBinaryHoleFillingImageFilterIUC2IUC2)
itkVotingBinaryHoleFillingImageFilterIUC2IUC2_swigregister = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_swigregister
itkVotingBinaryHoleFillingImageFilterIUC2IUC2_swigregister(itkVotingBinaryHoleFillingImageFilterIUC2IUC2)

def itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__() -> "itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Pointer":
    """itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__() -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Pointer"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__()

def itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterIUC2IUC2 *":
    """itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast(obj)

class itkVotingBinaryHoleFillingImageFilterIUC3IUC3(itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUC3IUC3):
    """Proxy of C++ itkVotingBinaryHoleFillingImageFilterIUC3IUC3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Pointer":
        """Clone(itkVotingBinaryHoleFillingImageFilterIUC3IUC3 self) -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Pointer"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Clone(self)


    def GetMajorityThreshold(self) -> "unsigned int const &":
        """GetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterIUC3IUC3 self) -> unsigned int const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetMajorityThreshold(self)


    def SetMajorityThreshold(self, _arg: 'unsigned int const') -> "void":
        """SetMajorityThreshold(itkVotingBinaryHoleFillingImageFilterIUC3IUC3 self, unsigned int const _arg)"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_SetMajorityThreshold(self, _arg)


    def GetNumberOfPixelsChanged(self) -> "unsigned long const &":
        """GetNumberOfPixelsChanged(itkVotingBinaryHoleFillingImageFilterIUC3IUC3 self) -> unsigned long const &"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetNumberOfPixelsChanged(self)

    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_IntConvertibleToInputCheck
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_UnsignedIntConvertibleToInputCheck
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkVotingBinaryHoleFillingImageFilterIUC3IUC3 *":
        """GetPointer(itkVotingBinaryHoleFillingImageFilterIUC3IUC3 self) -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3"""
        return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVotingBinaryHoleFillingImageFilterIUC3IUC3.Clone = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Clone, None, itkVotingBinaryHoleFillingImageFilterIUC3IUC3)
itkVotingBinaryHoleFillingImageFilterIUC3IUC3.GetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterIUC3IUC3)
itkVotingBinaryHoleFillingImageFilterIUC3IUC3.SetMajorityThreshold = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_SetMajorityThreshold, None, itkVotingBinaryHoleFillingImageFilterIUC3IUC3)
itkVotingBinaryHoleFillingImageFilterIUC3IUC3.GetNumberOfPixelsChanged = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetNumberOfPixelsChanged, None, itkVotingBinaryHoleFillingImageFilterIUC3IUC3)
itkVotingBinaryHoleFillingImageFilterIUC3IUC3.GetPointer = new_instancemethod(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetPointer, None, itkVotingBinaryHoleFillingImageFilterIUC3IUC3)
itkVotingBinaryHoleFillingImageFilterIUC3IUC3_swigregister = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_swigregister
itkVotingBinaryHoleFillingImageFilterIUC3IUC3_swigregister(itkVotingBinaryHoleFillingImageFilterIUC3IUC3)

def itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__() -> "itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Pointer":
    """itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__() -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Pointer"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__()

def itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkVotingBinaryHoleFillingImageFilterIUC3IUC3 *":
    """itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3"""
    return _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast(obj)



