#!/usr/bin/python3

if __name__ == "__main__":
    if len(argv) == 0:
        print("{}: argument.".format(len(argv)))
    else:
        for i in range (len(argv)):
            print("{} arguments: \n{}: {}".format(len(argv), argv[i], i))
