import base64
from types import FunctionType, CodeType, MappingProxyType
import __main__

def from_code(code: CodeType):
    code_dict = {}
    code_dict["co_argcount"] = code.co_argcount
    code_dict["co_posonlyargcount"] = code.co_posonlyargcount
    code_dict["co_kwonlyargcount"] = code.co_kwonlyargcount
    code_dict["co_nlocals"] = code.co_nlocals
    code_dict["co_stacksize"] = code.co_stacksize
    code_dict["co_flags"] = code.co_flags
    s = base64.b64encode(code.co_code)
    code_dict["co_code"] = s.decode()
    code_dict["co_consts"] = code.co_consts
    code_dict["co_names"] = code.co_names
    code_dict["co_varnames"] = code.co_varnames
    code_dict["co_filename"] = code.co_filename
    code_dict["co_name"] = code.co_name
    code_dict["co_firstlineno"] = code.co_firstlineno
    s = base64.b64encode(code.co_lnotab)
    code_dict["co_lnotab"] = s.decode()
    code_dict["co_freevars"] = code.co_freevars
    code_dict["co_cellvars"] = code.co_cellvars
    return code_dict


def to_code(code_dict):
    s_code = code_dict["co_code"].encode()
    code = base64.b64decode(s_code)
    s_lnotab = code_dict["co_lnotab"].encode()
    lnotab = base64.b64decode(s_lnotab)
    return CodeType(
        code_dict["co_argcount"], code_dict["co_posonlyargcount"], code_dict["co_kwonlyargcount"],
        code_dict["co_nlocals"], code_dict["co_stacksize"], code_dict["co_flags"],
        code, tuple(code_dict["co_consts"]), tuple(code_dict["co_names"]),
        tuple(code_dict["co_varnames"]
              ), code_dict["co_filename"], code_dict["co_name"],
        code_dict["co_firstlineno"], lnotab,
        tuple(code_dict["co_freevars"]), tuple(code_dict["co_cellvars"])
    )
def to_serializable(obj):
    if (isinstance(obj, (str, int, float, bool, dict, list))):
        return obj
    if (isinstance(obj, (tuple))):
        return {"tuple": obj}
    if (isinstance(obj, (FunctionType))):
        return {"func": {"__code__":from_code(obj.__code__), "__name__": obj.__name__, "__defaults__":to_serializable(obj.__defaults__), "__closure__":to_serializable(obj.__closure__)}}
    if (isinstance(obj, (CodeType))):
        d = {}
        pub_attributes = list(filter(lambda item: not item.startswith('_'), dir(obj)))
        for attr in pub_attributes:
            d[attr] = to_serializable(obj.__getattribute__(attr))
        return {"code": d}
    if isinstance(obj, MappingProxyType):
        obj_dict = dict(obj)
        for key in obj_dict.keys():
            obj_dict[key] = to_serializable(obj_dict[key])
        return obj_dict
        # class definition (type) serialization
    if isinstance(obj, type):
        obj_dict = {
            "__class__": obj.__class__.__name__,
            "__module__": obj.__module__,
            "__name__": obj.__name__
        }
        attrs = dict(obj.__dict__)
        for key in attrs.keys():
            attrs[key] = to_serializable(attrs[key])
        return {"type": {"defs": obj_dict, "attrs": attrs}}
        # check that object is instance of class
    if hasattr(obj, '__dict__'):
        obj_type = to_serializable(type(obj))
        obj_dict = to_serializable(obj.__dict__)
        return {"obj": {"type": obj_type, "dict": obj_dict}}
    return None

def from_serializable(d):
    if isinstance(d, dict):
        for (k, v) in d.items():
            if k == 'type':
                globals().update(__main__.__dict__)
                defs = v['defs']
                attrs = v['attrs']
                obj_type = getattr(__main__, defs['__name__'], None)
                for i in attrs.keys():
                    attrs[i] = from_serializable(attrs[i])
                return type(defs['__name__'], (object, ), attrs)
            if k == "func":
                c = to_code(v["__code__"])
                fname = v["__name__"]
                fdefaults = v["__defaults__"]
                fclosure = v["__closure__"]
                return FunctionType(c, globals().copy(), fname, fdefaults, fclosure)
            if k == 'obj':
                obj_type = from_serializable(v['type'])
                obj_dict = from_serializable(v['dict'])
                try:
                    obj = object.__new__(obj_type)
                    obj.__dict__ = obj_dict
                    for (kk, vv) in obj_dict.items():
                        setattr(obj, kk, vv)
                except TypeError:
                    obj = None
                return obj
            if k == "tuple":
                return tuple(d.pop("tuple"))
    return d