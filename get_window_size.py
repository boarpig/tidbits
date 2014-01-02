#!/usr/bin/python

import array, termios, fcntl

buf = array.array('h', [0, 0])
fcntl.ioctl(0, termios.TIOCGWINSZ, buf, 1)
print(*buf)

