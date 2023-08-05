# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRawImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkRawImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkRawImageIOPython')
    _itkRawImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRawImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkRawImageIOPython
            return _itkRawImageIOPython
        try:
            _mod = imp.load_module('_itkRawImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkRawImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRawImageIOPython
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


import ITKIOImageBaseBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython

def itkRawImageIOF3_New():
  return itkRawImageIOF3.New()


def itkRawImageIOF2_New():
  return itkRawImageIOF2.New()

class itkRawImageIOF2(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkRawImageIOF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRawImageIOF2_Pointer":
        """__New_orig__() -> itkRawImageIOF2_Pointer"""
        return _itkRawImageIOPython.itkRawImageIOF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRawImageIOF2_Pointer":
        """Clone(itkRawImageIOF2 self) -> itkRawImageIOF2_Pointer"""
        return _itkRawImageIOPython.itkRawImageIOF2_Clone(self)


    def SetHeaderSize(self, size: 'unsigned long long') -> "void":
        """SetHeaderSize(itkRawImageIOF2 self, unsigned long long size)"""
        return _itkRawImageIOPython.itkRawImageIOF2_SetHeaderSize(self, size)


    def GetHeaderSize(self) -> "unsigned long long":
        """GetHeaderSize(itkRawImageIOF2 self) -> unsigned long long"""
        return _itkRawImageIOPython.itkRawImageIOF2_GetHeaderSize(self)


    def SetFileDimensionality(self, _arg: 'unsigned long const') -> "void":
        """SetFileDimensionality(itkRawImageIOF2 self, unsigned long const _arg)"""
        return _itkRawImageIOPython.itkRawImageIOF2_SetFileDimensionality(self, _arg)


    def GetFileDimensionality(self) -> "unsigned long":
        """GetFileDimensionality(itkRawImageIOF2 self) -> unsigned long"""
        return _itkRawImageIOPython.itkRawImageIOF2_GetFileDimensionality(self)


    def GetImageMask(self) -> "unsigned short const &":
        """GetImageMask(itkRawImageIOF2 self) -> unsigned short const &"""
        return _itkRawImageIOPython.itkRawImageIOF2_GetImageMask(self)


    def SetImageMask(self, val: 'unsigned long') -> "void":
        """SetImageMask(itkRawImageIOF2 self, unsigned long val)"""
        return _itkRawImageIOPython.itkRawImageIOF2_SetImageMask(self, val)


    def ReadHeader(self, *args) -> "void":
        """
        ReadHeader(itkRawImageIOF2 self, std::string const arg0)
        ReadHeader(itkRawImageIOF2 self)
        """
        return _itkRawImageIOPython.itkRawImageIOF2_ReadHeader(self, *args)

    __swig_destroy__ = _itkRawImageIOPython.delete_itkRawImageIOF2

    def cast(obj: 'itkLightObject') -> "itkRawImageIOF2 *":
        """cast(itkLightObject obj) -> itkRawImageIOF2"""
        return _itkRawImageIOPython.itkRawImageIOF2_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRawImageIOF2 *":
        """GetPointer(itkRawImageIOF2 self) -> itkRawImageIOF2"""
        return _itkRawImageIOPython.itkRawImageIOF2_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRawImageIOF2

        Create a new object of the class itkRawImageIOF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRawImageIOF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRawImageIOF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRawImageIOF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRawImageIOF2.Clone = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_Clone, None, itkRawImageIOF2)
itkRawImageIOF2.SetHeaderSize = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_SetHeaderSize, None, itkRawImageIOF2)
itkRawImageIOF2.GetHeaderSize = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_GetHeaderSize, None, itkRawImageIOF2)
itkRawImageIOF2.SetFileDimensionality = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_SetFileDimensionality, None, itkRawImageIOF2)
itkRawImageIOF2.GetFileDimensionality = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_GetFileDimensionality, None, itkRawImageIOF2)
itkRawImageIOF2.GetImageMask = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_GetImageMask, None, itkRawImageIOF2)
itkRawImageIOF2.SetImageMask = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_SetImageMask, None, itkRawImageIOF2)
itkRawImageIOF2.ReadHeader = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_ReadHeader, None, itkRawImageIOF2)
itkRawImageIOF2.GetPointer = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF2_GetPointer, None, itkRawImageIOF2)
itkRawImageIOF2_swigregister = _itkRawImageIOPython.itkRawImageIOF2_swigregister
itkRawImageIOF2_swigregister(itkRawImageIOF2)

def itkRawImageIOF2___New_orig__() -> "itkRawImageIOF2_Pointer":
    """itkRawImageIOF2___New_orig__() -> itkRawImageIOF2_Pointer"""
    return _itkRawImageIOPython.itkRawImageIOF2___New_orig__()

def itkRawImageIOF2_cast(obj: 'itkLightObject') -> "itkRawImageIOF2 *":
    """itkRawImageIOF2_cast(itkLightObject obj) -> itkRawImageIOF2"""
    return _itkRawImageIOPython.itkRawImageIOF2_cast(obj)

class itkRawImageIOF3(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkRawImageIOF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRawImageIOF3_Pointer":
        """__New_orig__() -> itkRawImageIOF3_Pointer"""
        return _itkRawImageIOPython.itkRawImageIOF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRawImageIOF3_Pointer":
        """Clone(itkRawImageIOF3 self) -> itkRawImageIOF3_Pointer"""
        return _itkRawImageIOPython.itkRawImageIOF3_Clone(self)


    def SetHeaderSize(self, size: 'unsigned long long') -> "void":
        """SetHeaderSize(itkRawImageIOF3 self, unsigned long long size)"""
        return _itkRawImageIOPython.itkRawImageIOF3_SetHeaderSize(self, size)


    def GetHeaderSize(self) -> "unsigned long long":
        """GetHeaderSize(itkRawImageIOF3 self) -> unsigned long long"""
        return _itkRawImageIOPython.itkRawImageIOF3_GetHeaderSize(self)


    def SetFileDimensionality(self, _arg: 'unsigned long const') -> "void":
        """SetFileDimensionality(itkRawImageIOF3 self, unsigned long const _arg)"""
        return _itkRawImageIOPython.itkRawImageIOF3_SetFileDimensionality(self, _arg)


    def GetFileDimensionality(self) -> "unsigned long":
        """GetFileDimensionality(itkRawImageIOF3 self) -> unsigned long"""
        return _itkRawImageIOPython.itkRawImageIOF3_GetFileDimensionality(self)


    def GetImageMask(self) -> "unsigned short const &":
        """GetImageMask(itkRawImageIOF3 self) -> unsigned short const &"""
        return _itkRawImageIOPython.itkRawImageIOF3_GetImageMask(self)


    def SetImageMask(self, val: 'unsigned long') -> "void":
        """SetImageMask(itkRawImageIOF3 self, unsigned long val)"""
        return _itkRawImageIOPython.itkRawImageIOF3_SetImageMask(self, val)


    def ReadHeader(self, *args) -> "void":
        """
        ReadHeader(itkRawImageIOF3 self, std::string const arg0)
        ReadHeader(itkRawImageIOF3 self)
        """
        return _itkRawImageIOPython.itkRawImageIOF3_ReadHeader(self, *args)

    __swig_destroy__ = _itkRawImageIOPython.delete_itkRawImageIOF3

    def cast(obj: 'itkLightObject') -> "itkRawImageIOF3 *":
        """cast(itkLightObject obj) -> itkRawImageIOF3"""
        return _itkRawImageIOPython.itkRawImageIOF3_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkRawImageIOF3 *":
        """GetPointer(itkRawImageIOF3 self) -> itkRawImageIOF3"""
        return _itkRawImageIOPython.itkRawImageIOF3_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkRawImageIOF3

        Create a new object of the class itkRawImageIOF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRawImageIOF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRawImageIOF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRawImageIOF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRawImageIOF3.Clone = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_Clone, None, itkRawImageIOF3)
itkRawImageIOF3.SetHeaderSize = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_SetHeaderSize, None, itkRawImageIOF3)
itkRawImageIOF3.GetHeaderSize = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_GetHeaderSize, None, itkRawImageIOF3)
itkRawImageIOF3.SetFileDimensionality = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_SetFileDimensionality, None, itkRawImageIOF3)
itkRawImageIOF3.GetFileDimensionality = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_GetFileDimensionality, None, itkRawImageIOF3)
itkRawImageIOF3.GetImageMask = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_GetImageMask, None, itkRawImageIOF3)
itkRawImageIOF3.SetImageMask = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_SetImageMask, None, itkRawImageIOF3)
itkRawImageIOF3.ReadHeader = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_ReadHeader, None, itkRawImageIOF3)
itkRawImageIOF3.GetPointer = new_instancemethod(_itkRawImageIOPython.itkRawImageIOF3_GetPointer, None, itkRawImageIOF3)
itkRawImageIOF3_swigregister = _itkRawImageIOPython.itkRawImageIOF3_swigregister
itkRawImageIOF3_swigregister(itkRawImageIOF3)

def itkRawImageIOF3___New_orig__() -> "itkRawImageIOF3_Pointer":
    """itkRawImageIOF3___New_orig__() -> itkRawImageIOF3_Pointer"""
    return _itkRawImageIOPython.itkRawImageIOF3___New_orig__()

def itkRawImageIOF3_cast(obj: 'itkLightObject') -> "itkRawImageIOF3 *":
    """itkRawImageIOF3_cast(itkLightObject obj) -> itkRawImageIOF3"""
    return _itkRawImageIOPython.itkRawImageIOF3_cast(obj)



