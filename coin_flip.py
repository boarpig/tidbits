#!/usr/bin/pypy

from random import choice

coin = ("H", "T")

counts = []

for i in range(100000):
    count = -1
    flips = []
    while not(len(flips) >= 3 and flips[-3:] == ["H", "T", "H"]):
        count += 1
        flips.append(choice(coin))
    counts.append(count)
print(float(sum(counts)) / float(len(counts)))


