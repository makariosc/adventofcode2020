import re
from functools import reduce

def doCode():

    f = open("input", "r+")
    l = f.readlines()

    maxSeat = sorted(l, key=keyFunction)[-1]
    r, c = keyFunction(maxSeat)
    return r * 8 + c

def keyFunction(s):
    rowString = s[0:7]
    colString = s[7:]

    r = 0
    for n, x in enumerate(rowString):
        if x == "B":
            r += 64 / (2**n)

    c = 0
    for n, x in enumerate(colString):
        if x == "R":
            c += 4 / (2**n)

    return (r, c)



print(f"answer: {doCode()}")
