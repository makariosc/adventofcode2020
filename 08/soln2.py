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

    run = { "acc": lambda t=iChanged: processInsns(i+1, seen, acc+val, t),
                "nop": lambda t=iChanged: processInsns(i+1, seen, acc, t),
                "jmp": lambda t=iChanged: processInsns(i+val, seen, acc, t) }

    runAlt = { "acc": lambda: run["acc"](),
                   "nop": lambda: run["jmp"](True),
                   "jmp": lambda: run["nop"](True) }

    seen.add(i)
    if iChanged:
        return run[insn]()
    try:
        return run[insn]()
    except Exception:
        return runAlt[insn]()

    return acc
    
print(f"answer: {processInsns(0, set(), 0, False)}")
