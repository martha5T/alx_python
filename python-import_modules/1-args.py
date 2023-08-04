#!/usr/bin/python3
import sys


def main():
    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments and their values
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()

