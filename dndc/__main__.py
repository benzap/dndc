""" Main entry point to 'dndc' commandline tool
"""
import sys

import dndc.db as db
from dndc.resource import Resource
_R = Resource()


def main(args=None):
    if args is None:
        args = sys.argv[1:]
        
    print("Starting app")
    print(_R.get_filepath("language.english"))
    print(_R.get("language.english"))


if __name__ == "__main__":
    main()
