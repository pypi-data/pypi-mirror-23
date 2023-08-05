# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHDF5ImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkHDF5ImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkHDF5ImageIOPython')
    _itkHDF5ImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHDF5ImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkHDF5ImageIOPython
            return _itkHDF5ImageIOPython
        try:
            _mod = imp.load_module('_itkHDF5ImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkHDF5ImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHDF5ImageIOPython
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
import ITKCommonBasePython
import pyBasePython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython

def itkHDF5ImageIOFactory_New():
  return itkHDF5ImageIOFactory.New()


def itkHDF5ImageIO_New():
  return itkHDF5ImageIO.New()

class itkHDF5ImageIO(ITKIOImageBaseBasePython.itkStreamingImageIOBase):
    """Proxy of C++ itkHDF5ImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkHDF5ImageIO_Pointer"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkHDF5ImageIO self) -> itkHDF5ImageIO_Pointer"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIO_Clone(self)

    __swig_destroy__ = _itkHDF5ImageIOPython.delete_itkHDF5ImageIO

    def cast(obj):
        """cast(itkLightObject obj) -> itkHDF5ImageIO"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkHDF5ImageIO self) -> itkHDF5ImageIO"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHDF5ImageIO

        Create a new object of the class itkHDF5ImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHDF5ImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHDF5ImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHDF5ImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHDF5ImageIO.Clone = new_instancemethod(_itkHDF5ImageIOPython.itkHDF5ImageIO_Clone, None, itkHDF5ImageIO)
itkHDF5ImageIO.GetPointer = new_instancemethod(_itkHDF5ImageIOPython.itkHDF5ImageIO_GetPointer, None, itkHDF5ImageIO)
itkHDF5ImageIO_swigregister = _itkHDF5ImageIOPython.itkHDF5ImageIO_swigregister
itkHDF5ImageIO_swigregister(itkHDF5ImageIO)

def itkHDF5ImageIO___New_orig__():
    """itkHDF5ImageIO___New_orig__() -> itkHDF5ImageIO_Pointer"""
    return _itkHDF5ImageIOPython.itkHDF5ImageIO___New_orig__()

def itkHDF5ImageIO_cast(obj):
    """itkHDF5ImageIO_cast(itkLightObject obj) -> itkHDF5ImageIO"""
    return _itkHDF5ImageIOPython.itkHDF5ImageIO_cast(obj)

class itkHDF5ImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """Proxy of C++ itkHDF5ImageIOFactory class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkHDF5ImageIOFactory_Pointer"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory():
        """RegisterOneFactory()"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkHDF5ImageIOPython.delete_itkHDF5ImageIOFactory

    def cast(obj):
        """cast(itkLightObject obj) -> itkHDF5ImageIOFactory"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkHDF5ImageIOFactory self) -> itkHDF5ImageIOFactory"""
        return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkHDF5ImageIOFactory

        Create a new object of the class itkHDF5ImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHDF5ImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHDF5ImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHDF5ImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHDF5ImageIOFactory.GetPointer = new_instancemethod(_itkHDF5ImageIOPython.itkHDF5ImageIOFactory_GetPointer, None, itkHDF5ImageIOFactory)
itkHDF5ImageIOFactory_swigregister = _itkHDF5ImageIOPython.itkHDF5ImageIOFactory_swigregister
itkHDF5ImageIOFactory_swigregister(itkHDF5ImageIOFactory)

def itkHDF5ImageIOFactory___New_orig__():
    """itkHDF5ImageIOFactory___New_orig__() -> itkHDF5ImageIOFactory_Pointer"""
    return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory___New_orig__()

def itkHDF5ImageIOFactory_RegisterOneFactory():
    """itkHDF5ImageIOFactory_RegisterOneFactory()"""
    return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory_RegisterOneFactory()

def itkHDF5ImageIOFactory_cast(obj):
    """itkHDF5ImageIOFactory_cast(itkLightObject obj) -> itkHDF5ImageIOFactory"""
    return _itkHDF5ImageIOPython.itkHDF5ImageIOFactory_cast(obj)



