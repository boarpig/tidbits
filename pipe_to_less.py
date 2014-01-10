#!/usr/bin/python

from subprocess import Popen, PIPE

less = Popen("less", stdin=PIPE)
less.communicate(bytes("Text I want to send to less", encoding='utf-8'))

