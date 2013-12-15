#!/usr/bin/pypy

from collections import deque
from random import shuffle
from time import time

def merge(unsorted):
    if isinstance(unsorted, int):
        return [unsorted]
    else:
        length = len(unsorted)
    if length == 1:
        return unsorted
    elif length == 2:
        if unsorted[0] > unsorted[1]:
            return [unsorted[1], unsorted[0]]
        else:
            return unsorted
    else:
        if length == 3:
            first = [unsorted[0]]
            second = deque(merge(unsorted[(length / 2):]))
        else:
            first = deque(merge(unsorted[:(length / 2)]))
            second = deque(merge(unsorted[(length / 2):]))
        result = []
        while True:
            if first and second:
                if first[0] < second[0]:
                    result.append(first[0])
                    del first[0]
                elif second[0] < first[0]:
                    result.append(second[0])
                    del second[0]
                elif first[0] == second[0]:
                    result.append(first[0])
                    del first[0]
            elif first:
                result.extend(first)
                break
            elif second:
                result.extend(second)
                break
        return result

for i in range(10):
    test = range(100000)
    shuffle(test)

    start = time()
    merge(test)
    my = time() - start

    start = time()
    sorted(test)
    native = time() - start
    print(my / native)

