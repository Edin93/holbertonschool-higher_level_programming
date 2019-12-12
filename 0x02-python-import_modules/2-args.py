#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    if len(argv) == 0:
        print("argument.")
    elif len(argv) == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
