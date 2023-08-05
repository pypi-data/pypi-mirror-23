# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkStimulateImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkStimulateImageIOPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkStimulateImageIOPython')
    _itkStimulateImageIOPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkStimulateImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkStimulateImageIOPython
            return _itkStimulateImageIOPython
        try:
            _mod = imp.load_module('_itkStimulateImageIOPython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkStimulateImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkStimulateImageIOPython
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

def itkStimulateImageIOFactory_New():
  return itkStimulateImageIOFactory.New()


def itkStimulateImageIO_New():
  return itkStimulateImageIO.New()

class itkStimulateImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """Proxy of C++ itkStimulateImageIO class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkStimulateImageIO_Pointer"""
        return _itkStimulateImageIOPython.itkStimulateImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self):
        """Clone(itkStimulateImageIO self) -> itkStimulateImageIO_Pointer"""
        return _itkStimulateImageIOPython.itkStimulateImageIO_Clone(self)


    def GetDisplayRange(self):
        """GetDisplayRange(itkStimulateImageIO self) -> float const *"""
        return _itkStimulateImageIOPython.itkStimulateImageIO_GetDisplayRange(self)


    def GetHighDisplayValue(self):
        """GetHighDisplayValue(itkStimulateImageIO self) -> float const &"""
        return _itkStimulateImageIOPython.itkStimulateImageIO_GetHighDisplayValue(self)


    def GetLowDisplayValue(self):
        """GetLowDisplayValue(itkStimulateImageIO self) -> float const &"""
        return _itkStimulateImageIOPython.itkStimulateImageIO_GetLowDisplayValue(self)

    __swig_destroy__ = _itkStimulateImageIOPython.delete_itkStimulateImageIO

    def cast(obj):
        """cast(itkLightObject obj) -> itkStimulateImageIO"""
        return _itkStimulateImageIOPython.itkStimulateImageIO_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkStimulateImageIO self) -> itkStimulateImageIO"""
        return _itkStimulateImageIOPython.itkStimulateImageIO_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkStimulateImageIO

        Create a new object of the class itkStimulateImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStimulateImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStimulateImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStimulateImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStimulateImageIO.Clone = new_instancemethod(_itkStimulateImageIOPython.itkStimulateImageIO_Clone, None, itkStimulateImageIO)
itkStimulateImageIO.GetDisplayRange = new_instancemethod(_itkStimulateImageIOPython.itkStimulateImageIO_GetDisplayRange, None, itkStimulateImageIO)
itkStimulateImageIO.GetHighDisplayValue = new_instancemethod(_itkStimulateImageIOPython.itkStimulateImageIO_GetHighDisplayValue, None, itkStimulateImageIO)
itkStimulateImageIO.GetLowDisplayValue = new_instancemethod(_itkStimulateImageIOPython.itkStimulateImageIO_GetLowDisplayValue, None, itkStimulateImageIO)
itkStimulateImageIO.GetPointer = new_instancemethod(_itkStimulateImageIOPython.itkStimulateImageIO_GetPointer, None, itkStimulateImageIO)
itkStimulateImageIO_swigregister = _itkStimulateImageIOPython.itkStimulateImageIO_swigregister
itkStimulateImageIO_swigregister(itkStimulateImageIO)

def itkStimulateImageIO___New_orig__():
    """itkStimulateImageIO___New_orig__() -> itkStimulateImageIO_Pointer"""
    return _itkStimulateImageIOPython.itkStimulateImageIO___New_orig__()

def itkStimulateImageIO_cast(obj):
    """itkStimulateImageIO_cast(itkLightObject obj) -> itkStimulateImageIO"""
    return _itkStimulateImageIOPython.itkStimulateImageIO_cast(obj)

class itkStimulateImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """Proxy of C++ itkStimulateImageIOFactory class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__():
        """__New_orig__() -> itkStimulateImageIOFactory_Pointer"""
        return _itkStimulateImageIOPython.itkStimulateImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory():
        """RegisterOneFactory()"""
        return _itkStimulateImageIOPython.itkStimulateImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkStimulateImageIOPython.delete_itkStimulateImageIOFactory

    def cast(obj):
        """cast(itkLightObject obj) -> itkStimulateImageIOFactory"""
        return _itkStimulateImageIOPython.itkStimulateImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self):
        """GetPointer(itkStimulateImageIOFactory self) -> itkStimulateImageIOFactory"""
        return _itkStimulateImageIOPython.itkStimulateImageIOFactory_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkStimulateImageIOFactory

        Create a new object of the class itkStimulateImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStimulateImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStimulateImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStimulateImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStimulateImageIOFactory.GetPointer = new_instancemethod(_itkStimulateImageIOPython.itkStimulateImageIOFactory_GetPointer, None, itkStimulateImageIOFactory)
itkStimulateImageIOFactory_swigregister = _itkStimulateImageIOPython.itkStimulateImageIOFactory_swigregister
itkStimulateImageIOFactory_swigregister(itkStimulateImageIOFactory)

def itkStimulateImageIOFactory___New_orig__():
    """itkStimulateImageIOFactory___New_orig__() -> itkStimulateImageIOFactory_Pointer"""
    return _itkStimulateImageIOPython.itkStimulateImageIOFactory___New_orig__()

def itkStimulateImageIOFactory_RegisterOneFactory():
    """itkStimulateImageIOFactory_RegisterOneFactory()"""
    return _itkStimulateImageIOPython.itkStimulateImageIOFactory_RegisterOneFactory()

def itkStimulateImageIOFactory_cast(obj):
    """itkStimulateImageIOFactory_cast(itkLightObject obj) -> itkStimulateImageIOFactory"""
    return _itkStimulateImageIOPython.itkStimulateImageIOFactory_cast(obj)



