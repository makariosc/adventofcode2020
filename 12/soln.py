from math import sin, cos, radians

f = open("input", "r+")
lines = [l.strip() for l in f.readlines()]

def rot(pos, angle):
    rad = radians(angle)
    x = cos(rad)*pos.real - sin(rad)*pos.imag
    y = cos(rad)*pos.imag + sin(rad)*pos.real
    return complex(x, y)

def one():
    pos = 0+0j
    angle = 0

    def case(x, pos, angle):
        return {
            'N': (pos + x, angle),
            'S': (pos - x, angle),
            'E': (pos + complex(0, x), angle),
            'W': (pos - complex(0, x), angle),
            'L': (pos, angle + x),
            'R': (pos, angle - x),
            'F': (pos + complex(sin(radians(angle))*x,cos(radians(angle))*x), angle)
        }

    for l in lines:
        d = l[0]
        n = int(l[1:])
        pos, angle = case(n, pos, angle)[d]

    return abs(pos.imag) + abs(pos.real)

def two():
    wpos = 10+1j
    pos = 0+0j

    def case(x, pos, wpos):
        return {
        'N': (pos, wpos + complex(0, x)),
        'S': (pos, wpos - complex(0, x)),
        'E': (pos, wpos + x),
        'W': (pos, wpos - x),
        'L': (pos, rot(wpos, x)),
        'R': (pos, rot(wpos, -x)), 
        'F': (pos + wpos*x, wpos)}

    for l in lines:
        d = l[0]
        n = int(l[1:])
        pos, wpos = case(n, pos, wpos)[d]

    return abs(pos.imag) + abs(pos.real)

print(f"answer: {one()}")
print(f"answer: {two()}")
