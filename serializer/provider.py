#import sys
#import os
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#from jsonserializer_new import JsonSerializer
#from yamlserializer import YamlSerializer
#from tomlserializer import TomlSerializer
import string
import serializer

class Provider:
    def create_serializer(format: string):
        if format.casefold() == 'JSON'.casefold():
            return serializer.jsonserializer.JsonSerializer()
        elif format.casefold() == 'YAML'.casefold():
            return serializer.YamlSerializer()
        elif format.casefold() == 'TOML'.casefold():
            return serializer.TomlSerializer()
        else:
            raise ValueError(format)