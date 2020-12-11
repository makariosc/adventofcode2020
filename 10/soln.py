f = open("input", "r+")
lines = f.readlines()
lines = [int(l.strip()) for l in lines]
lines = sorted(lines)
lines.insert(0, 0)
lines.append(lines[-1] + 3)

def one(lines):

    d = {1:0, 3:0}

    for i in range(1,len(lines)):
        diff = lines[i] - lines[i-1]
        d[diff] += 1

    return d[1] * d[3]

def two(lines):
    
    d = {0:1}

    for i in range(1,len(lines)):
        curr = lines[i]
        p1 = lines[i-1]
        p2 = lines[i-2]
        p3 = lines[i-3]
        paths = 0
        if curr - p1 <= 3: paths += d.get(p1, 0)
        if curr - p2 <= 3: paths += d.get(p2, 0)
        if curr - p3 <= 3: paths += d.get(p3, 0)

        d[curr] = paths

    return d[max(lines)]

print(f"one: {one(lines)}")
print(f"two: {two(lines)}")
