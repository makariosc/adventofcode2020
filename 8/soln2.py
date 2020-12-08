import re

matcher = re.compile("(nop|acc|jmp) ([+-]\d+)")

f = open("input", "r+")
insns = [l.strip() for l in f.readlines()]

def processInsns(i, seen, acc, iChanged):
    if i in seen:
        raise Exception("Loop")
    try:
        m = matcher.match(insns[i])
    except Exception:
        return acc

    insn = m.group(1)
    val = int(m.group(2))

    runInsn = { "acc": lambda t: processInsns(i+1, seen, acc+val, t),
                "nop": lambda t: processInsns(i+1, seen, acc, t),
                "jmp": lambda t: processInsns(i+val, seen, acc, t) }

    seen.add(i)
    if insn == "acc":
        return runInsn["acc"](iChanged)
    elif insn == "nop":
        if iChanged:
            return runInsn["nop"](iChanged)
        try:
            return runInsn["nop"](iChanged)
        except Exception:
            return runInsn["jmp"](True)
    elif insn == "jmp":
        if iChanged:
            return runInsn["jmp"](iChanged)
        try:
            return runInsn["jmp"](iChanged)
        except Exception:
            return runInsn["nop"](True)

    return acc
    
print(f"answer: {processInsns(0, set(), 0, False)}")
