#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argnum = len(argv) - 1

    if argnum == 0:
        print("{} arguments.".format(argnum))
    else:
        print("{} argument(s):".format(argnum))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
