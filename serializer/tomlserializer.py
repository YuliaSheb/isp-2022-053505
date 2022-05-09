import tomli
import serializer.converterutil as util

class TomlSerializer:
    def dump(self, obj, fp):
        return tomli.dump(util.to_serializable(obj), fp)

    def dumps(self, obj):
        return tomli.dumps(util.to_serializable(obj))

    def load(self,fp):
        obj = tomli.load(fp)
        return util.from_serializable(obj)

    def loads(self,s):
        obj = tomli.loads(s)
        return util.from_serializable(obj)