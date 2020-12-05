import re
from functools import reduce

def doCode():

    m = re.compile("(\w+):")
    soln = 0

    x = 0
    d = set()

    f = open("input", "r+")
    lines = f.readlines()

    for i in lines:
        if i.strip() == "":
            x += 1
            if not checkValid(d):
                print(f"invalid: {d}")
            else:
                print(f"  valid: {d}")
            soln += checkValid(d)
            d = set()
            continue

        match = m.finditer(i)
        for i in match:
            f = i.group(1)
            print(f)
            d.add(f)

def checkValid(d):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for f in fields:
        if f not in d:
            return False
    return True

print(f"answer: {doCode()}")
