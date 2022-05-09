import json
import serializer.converterutil as util

class JsonSerializer:
    def dump(self, obj, fp):
        return json.dump(util.to_serializable(obj), fp)

    def dumps(self, obj):
        return json.dumps(util.to_serializable(obj))

    def load(self,fp):
        obj = json.load(fp)
        return util.from_serializable(obj)

    def loads(self,s):
        obj = json.loads(s)
        return util.from_serializable(obj)