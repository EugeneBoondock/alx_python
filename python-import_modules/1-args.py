#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if argv == 0:
        print("0 arguments.")
    else:
        for i in range (len(argv)):
            print("{} arguments: \n{}: {}".format(len(argv), i, argv[i]))
