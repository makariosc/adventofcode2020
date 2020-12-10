from collections import deque

f = open("input", "r+")
lines = f.readlines()
lines = [int(l.strip()) for l in lines]

def getInvalid(lines):

    q = deque(maxlen = 25)
    for l in lines[0:25]:
        q.append(l)

    lines = lines[25:]
    for i in lines:
        if not any([(i - x in q) and (i - x != x) for x in q]):
            return i
        q.append(i)

    return 0

def getWeakness(lines):

    tgt = getInvalid(lines)

    s = sum(lines[0:2])
    
    q = deque()
    q.append(lines[0])
    q.append(lines[1])
    for i in lines[2:]:
        q.append(i)
        s += i

        while s > tgt and len(q) >= 2:
            i = q.popleft()
            s -= i
            
        if s == tgt:
            return max(q) + min(q)

print(f"part 1: {getInvalid(lines)}")
print(f"part 2: {getWeakness(lines)}")
