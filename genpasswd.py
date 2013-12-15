#!/usr/bin/python

from string import ascii_lowercase, digits
from random import sample

def genpass(length=10, chars=(ascii_lowercase + digits)):
    """Generate random certain length password using specified characters.
    Default is 10 characters long and using ascii letters and digits."""
    passu = ''.join(sample(chars, length))
    return passu

print(genpass(15))
