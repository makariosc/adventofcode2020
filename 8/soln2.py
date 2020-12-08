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

    runInsn = { "acc": lambda t=iChanged: processInsns(i+1, seen, acc+val, t),
                "nop": lambda t=iChanged: processInsns(i+1, seen, acc, t),
                "jmp": lambda t=iChanged: processInsns(i+val, seen, acc, t) }

    runAltInsn = { "acc": lambda: runInsn["acc"](),
                   "nop": lambda: runInsn["jmp"](True),
                   "jmp": lambda: runInsn["nop"](True) }

    seen.add(i)
    if iChanged:
        return runInsn[insn]()
    try:
        return runInsn[insn]()
    except Exception:
        return runAltInsn[insn]()

    return acc
    
print(f"answer: {processInsns(0, set(), 0, False)}")
