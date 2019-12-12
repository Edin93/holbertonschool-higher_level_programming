#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    r = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
            r += int(argv[i])
    print("{}".format(r))
