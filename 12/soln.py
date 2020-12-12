from math import sin, cos, radians

f = open("input", "r+")
lines = [l.strip() for l in f.readlines()]

def one():
    pos = 0+0j
    angle = 0

    case = {'N': lambda x, pos, angle: (pos + x, angle),
            'S': lambda x, pos, angle: (pos - x, angle),
            'E': lambda x, pos, angle: (pos + complex(0, x), angle),
            'W': lambda x, pos, angle: (pos - complex(0, x), angle),
            'L': lambda x, pos, angle: (pos, angle + x),
            'R': lambda x, pos, angle: (pos, angle - x),
            'F': lambda x, pos, angle: (pos + complex(sin(radians(angle))*x,cos(radians(angle))*x), angle)}

    for l in lines:
        d = l[0]
        n = int(l[1:])
        pos, angle = case[d](n, pos, angle)

    return abs(pos.imag) + abs(pos.real)

def two():
    wpos = 10+1j
    pos = 0+0j

    case = {'N': lambda x, pos, wpos: (pos, wpos + complex(0, x)),
            'S': lambda x, pos, wpos: (pos, wpos - complex(0, x)),
            'E': lambda x, pos, wpos: (pos, wpos + x),
            'W': lambda x, pos, wpos: (pos, wpos - x),
            'L': lambda x, pos, wpos: (pos, complex(cos(radians(x))*wpos.real - sin(radians(x))*wpos.imag, 
                                                    cos(radians(x))*wpos.imag + sin(radians(x))*wpos.real)),
            'R': lambda x, pos, wpos: (pos, complex(cos(radians(-x))*wpos.real - sin(radians(-x))*wpos.imag,
                                                    cos(radians(-x))*wpos.imag + sin(radians(-x))*wpos.real)),
            'F': lambda x, pos, wpos: (pos + wpos*x, wpos)}

    for l in lines:
        d = l[0]
        n = int(l[1:])
        pos, wpos = case[d](n, pos, wpos)

    return abs(pos.imag) + abs(pos.real)

print(f"answer: {one()}")
print(f"answer: {two()}")
