import yaml
import serializer.converterutil as util
class YamlSerializer:
    def dump(self, obj, fp):
        return yaml.dump(util.to_serializable(obj), fp)
    def dumps(self, obj):
        return yaml.dump(util.to_serializable(obj))
    def load(self,fp):
        obj = yaml.load(fp, Loader=yaml.UnsafeLoader)
        return util.from_serializable(obj)
    def loads(self,s):
        obj = yaml.load(s, Loader=yaml.UnsafeLoader)
        return util.from_serializable(obj)