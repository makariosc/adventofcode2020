import re

matcher = re.compile("(nop|acc|jmp) ([+-]\d+)")


f = open("input", "r+")
insns = [l.strip() for l in f.readlines()]

def processInsns(i, seen, acc):
    m = matcher.match(insns[i])
    insn = m.group(1)
    val = int(m.group(2))

    if i in seen:
        return acc

    seen.add(i)
    if insn == "nop":
        return processInsns(i+1, seen, acc)
    elif insn == "acc":
        return processInsns(i+1, seen, acc+val)
    elif insn == "jmp":
        return processInsns(i + val, seen, acc)
    return 0

print(f"answer: {processInsns(0, set(), 0)}")
