#!/usr/bin/python

stack = []

def plus():
    try:
        first = stack.pop()
        second = stack.pop()
        result = first + second
        stack.append(result)
        print(result)
    except IndexError:
        print("Not enough values in stack")
    
def minus():
    first = stack.pop()
    second = stack.pop()
    result = first + second
    stack.append(result)
    print(result)

operators = {'+':plus, '-':minus, '*':1, '/':1}

while True:
    cmdin = raw_input()
    if cmdin not in operators:
        try:
            stack.append(int(cmdin))
        except ValueError:
            print("Not a number.")
    else:
        operators[cmdin]()