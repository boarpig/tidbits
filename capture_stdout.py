#!/usr/bin/python

import io
import sys

def func_that_prints():
    print("Something to print")

# Store current stdout
stdout = sys.stdout

# Replace stdout with your own StringIO
sys.stdout = s = io.StringIO()

func_that_prints()

# Restore the original stdout
sys.stdout = stdout

print(len(s.getvalue()), ''.join(reversed(s.getvalue())))
