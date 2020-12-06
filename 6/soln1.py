from collections import Counter

def doCode():

    ret = 0
    s = set()

    f = open("input", "r+")
    lines = f.readlines()

    group = 0

    for l in lines:

        if l.strip() == "":
            ret += len(s)
            print(f"group {group}: {len(s)}")
            s = set()
            group += 1
            continue

        for c in l.strip():
            s.add(c)

    return ret

print(f"answer: {doCode()}")
