# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTransformIOBaseTemplatePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_itkTransformIOBaseTemplatePython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_itkTransformIOBaseTemplatePython')
    _itkTransformIOBaseTemplatePython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTransformIOBaseTemplatePython', [dirname(__file__)])
        except ImportError:
            import _itkTransformIOBaseTemplatePython
            return _itkTransformIOBaseTemplatePython
        try:
            _mod = imp.load_module('_itkTransformIOBaseTemplatePython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _itkTransformIOBaseTemplatePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTransformIOBaseTemplatePython
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
import itkTransformBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkOptimizerParametersPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkPointPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkVariableLengthVectorPython

def itkTransformIOBaseTemplateF_New():
  return itkTransformIOBaseTemplateF.New()

class itkTransformIOBaseTemplateF(ITKCommonBasePython.itkLightProcessObject):
    """Proxy of C++ itkTransformIOBaseTemplateF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetFileName(self, *args) -> "void":
        """
        SetFileName(itkTransformIOBaseTemplateF self, char const * _arg)
        SetFileName(itkTransformIOBaseTemplateF self, std::string const & _arg)
        """
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_SetFileName(self, *args)


    def GetFileName(self) -> "char const *":
        """GetFileName(itkTransformIOBaseTemplateF self) -> char const *"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetFileName(self)


    def Read(self) -> "void":
        """Read(itkTransformIOBaseTemplateF self)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_Read(self)


    def Write(self) -> "void":
        """Write(itkTransformIOBaseTemplateF self)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_Write(self)


    def CanReadFile(self, arg0: 'char const *') -> "bool":
        """CanReadFile(itkTransformIOBaseTemplateF self, char const * arg0) -> bool"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_CanReadFile(self, arg0)


    def CanWriteFile(self, arg0: 'char const *') -> "bool":
        """CanWriteFile(itkTransformIOBaseTemplateF self, char const * arg0) -> bool"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_CanWriteFile(self, arg0)


    def GetTransformList(self) -> "std::list< itkTransformBaseTemplateF_Pointer,std::allocator< itkTransformBaseTemplateF_Pointer > > &":
        """GetTransformList(itkTransformIOBaseTemplateF self) -> std::list< itkTransformBaseTemplateF_Pointer,std::allocator< itkTransformBaseTemplateF_Pointer > > &"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetTransformList(self)


    def GetReadTransformList(self) -> "std::list< itkTransformBaseTemplateF_Pointer,std::allocator< itkTransformBaseTemplateF_Pointer > > &":
        """GetReadTransformList(itkTransformIOBaseTemplateF self) -> std::list< itkTransformBaseTemplateF_Pointer,std::allocator< itkTransformBaseTemplateF_Pointer > > &"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetReadTransformList(self)


    def GetWriteTransformList(self) -> "std::list< itkTransformBaseTemplateF_ConstPointer,std::allocator< itkTransformBaseTemplateF_ConstPointer > > &":
        """GetWriteTransformList(itkTransformIOBaseTemplateF self) -> std::list< itkTransformBaseTemplateF_ConstPointer,std::allocator< itkTransformBaseTemplateF_ConstPointer > > &"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetWriteTransformList(self)


    def SetTransformList(self, transformList: 'std::list< itkTransformBaseTemplateF_ConstPointer,std::allocator< itkTransformBaseTemplateF_ConstPointer > > &') -> "void":
        """SetTransformList(itkTransformIOBaseTemplateF self, std::list< itkTransformBaseTemplateF_ConstPointer,std::allocator< itkTransformBaseTemplateF_ConstPointer > > & transformList)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_SetTransformList(self, transformList)


    def SetAppendMode(self, _arg: 'bool const') -> "void":
        """SetAppendMode(itkTransformIOBaseTemplateF self, bool const _arg)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_SetAppendMode(self, _arg)


    def GetAppendMode(self) -> "bool":
        """GetAppendMode(itkTransformIOBaseTemplateF self) -> bool"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetAppendMode(self)


    def AppendModeOn(self) -> "void":
        """AppendModeOn(itkTransformIOBaseTemplateF self)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_AppendModeOn(self)


    def AppendModeOff(self) -> "void":
        """AppendModeOff(itkTransformIOBaseTemplateF self)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_AppendModeOff(self)


    def CorrectTransformPrecisionType(arg0: 'std::string &') -> "std::string &":
        """CorrectTransformPrecisionType(std::string & arg0)"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_CorrectTransformPrecisionType(arg0)

    CorrectTransformPrecisionType = staticmethod(CorrectTransformPrecisionType)
    __swig_destroy__ = _itkTransformIOBaseTemplatePython.delete_itkTransformIOBaseTemplateF

    def cast(obj: 'itkLightObject') -> "itkTransformIOBaseTemplateF *":
        """cast(itkLightObject obj) -> itkTransformIOBaseTemplateF"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_cast(obj)

    cast = staticmethod(cast)

    def GetPointer(self) -> "itkTransformIOBaseTemplateF *":
        """GetPointer(itkTransformIOBaseTemplateF self) -> itkTransformIOBaseTemplateF"""
        return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetPointer(self)


    def New(*args, **kargs):
        """New() -> itkTransformIOBaseTemplateF

        Create a new object of the class itkTransformIOBaseTemplateF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformIOBaseTemplateF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformIOBaseTemplateF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformIOBaseTemplateF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTransformIOBaseTemplateF.SetFileName = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_SetFileName, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.GetFileName = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetFileName, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.Read = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_Read, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.Write = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_Write, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.CanReadFile = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_CanReadFile, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.CanWriteFile = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_CanWriteFile, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.GetTransformList = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetTransformList, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.GetReadTransformList = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetReadTransformList, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.GetWriteTransformList = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetWriteTransformList, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.SetTransformList = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_SetTransformList, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.SetAppendMode = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_SetAppendMode, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.GetAppendMode = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetAppendMode, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.AppendModeOn = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_AppendModeOn, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.AppendModeOff = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_AppendModeOff, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF.GetPointer = new_instancemethod(_itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_GetPointer, None, itkTransformIOBaseTemplateF)
itkTransformIOBaseTemplateF_swigregister = _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_swigregister
itkTransformIOBaseTemplateF_swigregister(itkTransformIOBaseTemplateF)

def itkTransformIOBaseTemplateF_CorrectTransformPrecisionType(arg0: 'std::string &') -> "std::string &":
    """itkTransformIOBaseTemplateF_CorrectTransformPrecisionType(std::string & arg0)"""
    return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_CorrectTransformPrecisionType(arg0)

def itkTransformIOBaseTemplateF_cast(obj: 'itkLightObject') -> "itkTransformIOBaseTemplateF *":
    """itkTransformIOBaseTemplateF_cast(itkLightObject obj) -> itkTransformIOBaseTemplateF"""
    return _itkTransformIOBaseTemplatePython.itkTransformIOBaseTemplateF_cast(obj)



