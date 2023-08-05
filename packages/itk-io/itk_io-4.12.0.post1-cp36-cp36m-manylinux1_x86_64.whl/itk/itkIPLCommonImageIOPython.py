# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIPLCommonImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkIPLCommonImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkIPLCommonImageIOPython')
    _itkIPLCommonImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIPLCommonImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkIPLCommonImageIOPython
            return _itkIPLCommonImageIOPython
        try:
            _mod = imp.load_module('_itkIPLCommonImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkIPLCommonImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIPLCommonImageIOPython
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


import ITKCommonBasePython
import pyBasePython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython

def itkIPLCommonImageIO_New():
  return itkIPLCommonImageIO.New()

class itkIPLCommonImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkIPLCommonImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIPLCommonImageIO_Pointer":
        """__New_orig__() -> itkIPLCommonImageIO_Pointer"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIPLCommonImageIO_Pointer":
        """Clone(itkIPLCommonImageIO self) -> itkIPLCommonImageIO_Pointer"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_Clone(self)


    def ModifyImageInformation(self) -> "void":
        """ModifyImageInformation(itkIPLCommonImageIO self)"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_ModifyImageInformation(self)


    def SortImageListByNameAscend(self) -> "void":
        """SortImageListByNameAscend(itkIPLCommonImageIO self)"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_SortImageListByNameAscend(self)


    def SortImageListByNameDescend(self) -> "void":
        """SortImageListByNameDescend(itkIPLCommonImageIO self)"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_SortImageListByNameDescend(self)

    __swig_destroy__ = _itkIPLCommonImageIOPython.delete_itkIPLCommonImageIO

    def cast(obj: 'itkLightObject') -> "itkIPLCommonImageIO *":
        """cast(itkLightObject obj) -> itkIPLCommonImageIO"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkIPLCommonImageIO *":
        """GetPointer(itkIPLCommonImageIO self) -> itkIPLCommonImageIO"""
        return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkIPLCommonImageIO

        Create a new object of the class itkIPLCommonImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIPLCommonImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIPLCommonImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIPLCommonImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIPLCommonImageIO.Clone = new_instancemethod(_itkIPLCommonImageIOPython.itkIPLCommonImageIO_Clone, None, itkIPLCommonImageIO)
itkIPLCommonImageIO.ModifyImageInformation = new_instancemethod(_itkIPLCommonImageIOPython.itkIPLCommonImageIO_ModifyImageInformation, None, itkIPLCommonImageIO)
itkIPLCommonImageIO.SortImageListByNameAscend = new_instancemethod(_itkIPLCommonImageIOPython.itkIPLCommonImageIO_SortImageListByNameAscend, None, itkIPLCommonImageIO)
itkIPLCommonImageIO.SortImageListByNameDescend = new_instancemethod(_itkIPLCommonImageIOPython.itkIPLCommonImageIO_SortImageListByNameDescend, None, itkIPLCommonImageIO)
itkIPLCommonImageIO.GetPointer = new_instancemethod(_itkIPLCommonImageIOPython.itkIPLCommonImageIO_GetPointer, None, itkIPLCommonImageIO)
itkIPLCommonImageIO_swigregister = _itkIPLCommonImageIOPython.itkIPLCommonImageIO_swigregister
itkIPLCommonImageIO_swigregister(itkIPLCommonImageIO)

def itkIPLCommonImageIO___New_orig__() -> "itkIPLCommonImageIO_Pointer":
    """itkIPLCommonImageIO___New_orig__() -> itkIPLCommonImageIO_Pointer"""
    return _itkIPLCommonImageIOPython.itkIPLCommonImageIO___New_orig__()

def itkIPLCommonImageIO_cast(obj: 'itkLightObject') -> "itkIPLCommonImageIO *":
    """itkIPLCommonImageIO_cast(itkLightObject obj) -> itkIPLCommonImageIO"""
    return _itkIPLCommonImageIOPython.itkIPLCommonImageIO_cast(obj)



