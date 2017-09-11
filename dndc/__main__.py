""" Main entry point to 'dndc' commandline tool
"""
import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]
        
    print("Starting app")


if __name__ == "__main__":
    main()
