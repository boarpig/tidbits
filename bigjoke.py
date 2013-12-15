#!/usr/bin/python
#
# BIG/JOKE = 0,HAHAHA...
# (B, I, G, J, O, K, E, H, A)

from itertools import permutations
from math import floor

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for perm in permutations(numbers):
    big = 100 * perm[0] + 10 * perm[1] + perm[2]
    joke = 1000 * perm[3] + 100 * perm[4] + 10 * perm[5] + perm[6]
    ha = 10 * perm[7] + perm[8]
    if (big % ha) == 0:
        if (joke % 9) == 0:
            if floor((big / joke) * 10000) == 100 * ha + ha:
                print("{0}/{1} = 0,{2}{2}{2}...".format(big, joke, ha))
