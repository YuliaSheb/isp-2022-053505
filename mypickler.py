import sys
print(sys.path)
from serializer import Provider
from pathlib import Path

def deserialize(file):
    format = Path(file.name).suffix.lstrip('.')
    parser = Provider.create_serializer(format)
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
        '-cfg', '--config', type=argparse.FileType('r'), nargs=1, required=False, help='configuration file')
    args = parser.parse_args()

    if not args.file or not args.format:
        parser.print_help()
    else:
        obj = deserialize(args.file)
        serialize(obj, args.file, args.format)
