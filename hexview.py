#!/usr/bin/python3

from sys import argv
from os.path import isfile
from string import printable, whitespace

eight = []

if len(argv) == 2 and isfile(argv[1]):
    with open(argv[1], 'rb') as f:
        s = f.read()
    for i, item in enumerate(s):
        if (i+1)%16 == 0 and i != 0:
            print("%s: " % (str(hex(i+1))[2:].zfill(8).upper()), end='')
            eight.append(str(hex(item))[2:].zfill(2).upper())
            print("%s: " % (' '.join(eight)), end='')
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
    for item in eight:
        char = chr(int(item, 16))
        if char in printable and char not in whitespace:
            print(char, end='')
        else:
            print('.', end='')
    print()
