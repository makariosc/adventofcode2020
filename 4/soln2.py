import re
from functools import reduce

def doCode():

    m = re.compile("(\w+):(\S+)")
    soln = 0

    x = 0
    d = {}

    f = open("input", "r+")
    lines = f.readlines()

    for i in lines:
        if i.strip() == "":
            x += 1
            soln += checkValid(d)
            d = {}
            continue

        match = m.finditer(i)
        for i in match:
            f = i.group(1)
            v = i.group(2)
            d[f] = v

    return soln

def checkValid(d):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for f in fields:
        if f not in d:
            return False
        if not validateField(f, d):
            return False
    return True

def validateField(f, d):
    def vHeight(x):
        if re.fullmatch("(.)*cm", x):
            i = int(re.sub("[\D]", "", x))
            if 150 <= i <= 193:
                return True
        if re.fullmatch("(.)*in", x):
            i = int(re.sub("[\D]", "", x))
            if 59 <= i <= 76:
                return True
        return False

    options = { "byr": lambda x: 1920 <= int(x) <= 2002,
                "iyr": lambda x: 2010 <= int(x) <= 2020,
                "eyr": lambda x: 2020 <= int(x) <= 2030,
                "hgt": vHeight,
                "hcl": lambda x: re.fullmatch("#[0-9,a-f]{6}", x),
                "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
                "pid": lambda x: re.fullmatch("[0-9]{9}", x),
                "cid": True
              }

    return options[f](d[f])

    
print(f"answer: {doCode()}")
