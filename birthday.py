#!/usr/bin/python

#def birthday(amount=365):
#    n = 1
#    for i in range(1, amount):
#        n *= (1 - (float(i) / amount))
#        print("%i: %.2f" % (i, 100-(n*100)))

def fact(n):
    n = int(n)
    factorial = 1
    for number in range(1, n + 1):
        factorial *= number
    return factorial
        

def birthday(amount=22):
    days = 365
    return (fact(days) / (days**amount * fact(days - amount)))

if __name__ == '__main__':
    #for i in range(100):
    print(birthday())
