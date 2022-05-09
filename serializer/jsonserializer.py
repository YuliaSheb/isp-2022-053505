#import json
import serializer.converterutil as util

class JsonSerializer:
    def dumps(self, item):
        """Serialize object, class or function to json."""
        def to_str(item):
            if isinstance(item, dict):
                strings = []
                for key, value in item.items():
                    strings.append(f'{to_str(key)}:{to_str(value)},')
                return f"{{{''.join(strings)[:-1]}}}"
            if isinstance(item, str):
                string = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return f"\"{string}\""
            if item is None:
                return 'null'

            return str(item)

        return to_str(util.to_serializable(item))

    def loads(self, string):
        """Deserialize object, class or function from json."""
        null = None
        return util.from_serializable(eval(string))

    # class JsonSerializer:
    #     def dump(self, obj, fp):
    #         return json.dump(util.to_serializable(obj), fp)
    #
    #     def dumps(self, obj):
    #         return json.dumps(util.to_serializable(obj))
    #
    #     def load(self, fp):
    #         obj = json.load(fp)
    #         return util.from_serializable(obj)
    #
    #     def loads(self, s):
    #         obj = json.loads(s)
    #         return util.from_serializable(obj)