#!/usr/bin/python

from string import ascii_lowercase, ascii_uppercase, digits
from random import sample
import argparse

def genpass(length=10, chars=(ascii_lowercase + digits)):
    """Generate random certain length password using specified characters.
    Default is 10 characters long and using ascii letters and digits."""
    passu = ''.join(sample(chars, length))
    return passu

def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument("-n", "--number", default=10, type=int,
            help="Number of characters in the password")
    parser.add_argument("-l", "--lowercase", default=True, action="store_true",
            help="Use lowercase chars in the password, default: %(default)s")
    parser.add_argument("-u", "--uppercase", default=False, action="store_true",
            help="Use uppercase chars in the password, default: %(default)s")
    parser.add_argument("-d", "--digits", default=True, action="store_true",
            help="Use numbers in the password, default: %(default)s")
    args = parser.parse_args()

    chars = ""
    if args.lowercase:
        chars += ascii_lowercase
    if args.uppercase:
        chars += ascii_uppercase
    if args.digits:
        chars += digits
    print(genpass(args.number, chars))

main()

