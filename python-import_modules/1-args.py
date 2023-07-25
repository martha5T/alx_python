#!/usr/bin/python3
from sys import argv


def print_arguments():
    if __name__ == "__main__":
        num_arguments = len(argv) - 1
        if num_arguments == 0:
            print(num_arguments, "arguments.")
        elif num_arguments == 1:
            print(num_arguments, "argument:")
        else:
            print(num_arguments, "arguments:")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
print_arguments()

