#!/usr/bin/python
#
# I wanted to find out how to open $EDITOR for input and use the content of
# that file in my program

import os
import subprocess
import tempfile

with tempfile.NamedTemporaryFile() as f:
    editor = os.environ['EDITOR']
    filename = f.name
    ret = subprocess.call([editor, filename])
    if ret == 0:
        content = f.read()
        print(content)
