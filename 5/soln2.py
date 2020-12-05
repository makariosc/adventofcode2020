import re
from functools import reduce

def doCode():

    f = open("input", "r+")
    l = f.readlines()

    slm = [keyFunction(s) for s in sorted(l, key=keyFunction)]

    print(slm)

    # cmon, sorting was n log n anyways, what's a couple
    # lower order terms among friends?
    for n, i in enumerate(slm):
        if slm[n+1] != i + 1:
            return i+1



def keyFunction(s):

    # this is just a binary encoding LOL
    i = 0
    for n, x in enumerate(s):
        if x == "B" or x == "R":
            i += 512 / (2**n)

    return i


print(f"answer: {doCode()}")
