from collections import Counter

def doCode():

    ret = 0
    g = []

    f = open("input", "r+")
    lines = f.readlines()

    for l in lines:

        if l.strip() == "":
            try:
                ret += len(set.intersection(*g))
            except TypeError as e:
                pass
            g = []
            continue

        s = set()
        for c in l.strip():
            s.add(c)
        g.append(s)

    return ret

print(f"answer: {doCode()}")
