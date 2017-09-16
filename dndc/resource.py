'''Used to get resources from the data folder
'''
import os
import os.path as path

import funcy as f
import yaml


YAML_EXTENSION = "dndc.yaml"
_ROOT = path.join(path.abspath(path.dirname(__file__)), "data")


class Resource:
    def __init__(self, root_path = _ROOT):
        self.root_path = root_path

    def get_path(self, *fpath):
        full_path = f.map(lambda s: s.split("."), fpath)
        full_path = f.flatten(full_path)
        return path.join(self.root_path, *full_path)

    def get_filepath(self, *fpath):
        full_path = self.get_path(*fpath)
        file_path = f"{full_path}.{YAML_EXTENSION}"
        return file_path

    def has(self, *fpath):
        file_path = self.get_filepath(*fpath)
        if not path.isfile(file_path):
            return False
        return True

    def get(self, *fpath):
        file_path = self.get_filepath(*fpath)

        if not self.has(*fpath):
            raise Exception(f"The file {file_path} does not exist")

        content = None
        with open(file_path, "r") as fhandle:
            content = fhandle.read()
        
        return yaml.load(content)

    def set(self, data, *fpath, **kwargs):
        file_path = self.get_filepath(*fpath)
        if not path.isdir(path.dirname(file_path)):
            try:
                os.makedirs(path.dirname(file_path))
            except:
                print(f"Failed to create directory: {path.dirname(file_path)}")

        if kwargs.get("force", False) and path.isfile(file_path):
            raise Exception(f"Cannot create {file_path}, file already exists")

        with open(file_path, "w") as fhandle:
            fhandle.write(yaml.dump(data))


def main():
    import sys
    from pprint import pprint
    argv = sys.argv[1:]

    if len(argv) <= 1:
        print("dndc-data <path...>")

    _R = Resource()
    pprint(_R.get(*argv))


if __name__ == "__main__":
    main()
