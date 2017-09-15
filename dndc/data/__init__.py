''' get data from folders, which are in the form of YAML files
'''
import os
import os.path as path


_ROOT = os.path.abspath(os.path.dirname(__file__))

class Resource:
    def get_path(self, path):
        return os.path.join(_ROOT, *path.split("."))

_R = Resource()

print(_R.get_path("item.some_thing_here"))
