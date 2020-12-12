from copy import deepcopy
from time import time

d = {}

f = open("input", "r+")
lines = f.readlines()
for m, row in enumerate(lines):
    for n, col in enumerate(row.strip()):
        d[complex(m, n)] = col

directions = [1+1j, 1+0j, 1-1j,
              0+1j,       0-1j,
             -1+1j,-1+0j,-1-1j]
def one():
    g1 = {}
    g2 = deepcopy(d)

    def step(parity):

        if parity:
            receiver = g1
            stepMe = g2
        else:
            receiver = g2
            stepMe = g1
        
        for point in stepMe:
            currSeat = stepMe[point]
            if currSeat == '.':
                receiver[point] = '.'
            else:
                num = sum([stepMe.get(point + d, 0) == '#' for d in directions])
                if num == 0 and currSeat == 'L':
                    receiver[point] = '#'
                elif num >= 4 and currSeat == '#':
                    receiver[point] = 'L'
                else:
                    receiver[point] = currSeat

    p = True
    while g1 != g2:
        step(p)
        p = not p

    count = 0
    for i in g1.values():
        count += i == "#"

    return count

def getNum(grid, point):
    count = 0
    for d in directions:
        i = 1
        s = '.'
        while s == '.':
            s = grid.get(point+(d*i), '')
            i += 1
            count += s == '#'
    return count
                
def two():
    g1 = {}
    g2 = deepcopy(d)

    def step(parity):

        if parity:
            receiver = g1
            stepMe = g2
        else:
            receiver = g2
            stepMe = g1
        
        for point in stepMe:
            currSeat = stepMe[point]
            if currSeat == '.':
                receiver[point] = '.'
            else:
                num = getNum(stepMe, point)
                if num == 0 and currSeat == 'L':
                    receiver[point] = '#'
                elif num >= 5 and currSeat == '#':
                    receiver[point] = 'L'
                else:
                    receiver[point] = currSeat

    p = True
    while g1 != g2:
        step(p)
        p = not p

    count = 0
    for i in g1.values():
        count += i == "#"

    return count

print(f"one: {one()}")
print(f"two: {two()}")
