import qtoml as toml_converter
import serializer.converterutil as util

class TomlSerializer:
    def dump(self, obj, fp):
        return toml_converter.dump(util.to_serializable(obj), fp, encode_none='None')
    def dumps(self, obj):
        return toml_converter.dumps(util.to_serializable(obj), encode_none='None')
    def load(self,fp):
        obj = toml_converter.load(fp)
        return util.from_serializable(obj)
    def loads(self,s):
        obj = toml_converter.loads(s)
        return util.from_serializable(obj)
