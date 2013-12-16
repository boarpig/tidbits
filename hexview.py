#!/usr/bin/python

from sys import argv
from os.path import isfile
from string import printable, whitespace

eight = []

if len(argv) == 2 and isfile(argv[1]):
    with open(argv[1], 'rb') as f:
        s = f.read()
    for i, item in enumerate(s):
        if (i+1)%16 == 0 and i != 0:
            print("{}: ".format(str(hex(i + 1 - 16))[2:].zfill(8).upper()), end='')
            eight.append(str(hex(item))[2:].zfill(2).upper())
            print("{}: ".format(' '.join(eight)), end='')
            for item in eight:
                char = chr(int(item, 16))
                if char in printable and char not in whitespace:
                    print(char, end='')
                else:
                    print('.', end='')
            print()
            eight = []
        else:
            eight.append(str(hex(item))[2:].zfill(2).upper())
    # TODO: make this print the last line number correctly
    print("{}: ".format(str(hex(i+1))[2:].zfill(8).upper()), end='')
    print("{} ".format(' '.join(eight)), end='')
    print("  " * (16 - len(eight)) + " " * (16 - len(eight) -1) + ": ", end='')
    for item in eight:
        char = chr(int(item, 16))
        if char in printable and char not in whitespace:
            print(char, end='')
        else:
            print('.', end='')
    print()
