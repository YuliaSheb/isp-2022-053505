from serializer import Provider
from pathlib import Path
import configparser as cfg

def read_config(file):
    config = cfg.ConfigParser()
    config.read(file.name)
    return (config['DEFAULT']['file'],config['DEFAULT']['format'])

def deserialize(file, format: str):
    file_format = Path(file.name).suffix.lstrip('.')
    if (file_format == format):
        raise ValueError("File is already encoded in specified format")
    parser = Provider.create_serializer(file_format)
    if parser is not None:
        return parser.load(file)
    else:
        raise ValueError("Unknown file format")

def serialize(obj, file, format: str):
    file_new = Path(file.name).with_suffix('.'+format)
    parser = Provider.create_serializer(format)
    if parser is not None:
        with open(file_new, "w") as fl:
            parser.dump(obj, fl)
    else:
        raise ValueError("Unknown file format")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='Serialize or convert serialized files')
    parser.add_argument(
        'file', type=argparse.FileType('r'), help='file to be serialized')
    parser.add_argument(
        'format', help='format to which the file will be converted')
    parser.add_argument(
        '-cfg', '--config', type=argparse.FileType('r'), required=False, help='configuration file')
    args = parser.parse_args()

    if args.config:
        (file, format) = read_config(args.config)
    else:
        if not args.file or not args.format:
            parser.print_help()
            exit()
        else:
            file = args.file
            format = args.format
    obj = deserialize(file, format)
    serialize(obj, file, format)        