#!/usr/bin/python

def addZero(n):
    return '0' + n

def addOne(n):
    return '1' + n

def gray(bits):
    if bits <= 1:
        return ('0', '1')
    else:
        firstHalf = gray(bits - 1)
        secondHalf = reversed(firstHalf)
        return list(map(addZero, firstHalf)) + list(map(addOne, secondHalf))

if __name__ == '__main__':
    for n in gray(4):
        print(n)
