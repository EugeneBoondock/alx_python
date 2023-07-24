#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argnum = len(argv) - 1

    if argnum == 0:
        print("{} arguments.".format(argnum))
    elif argnum == 1:
        print("{} argument:".format(argnum))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(argnum))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
