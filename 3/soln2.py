import re
from functools import reduce

def doCode():

    soln = 1
    pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    width = 31
    trees = [0, 0, 0, 0, 0]

    x = [0, 0, 0, 0, 0]
    y = 0 

    while True:
        try:
            i = input()

            for n, (right, down) in enumerate(pairs):
                if y % down == 0: 
                    if i[x[n]] == "#":
                        trees[n] += 1
                    x[n] += right
                    x[n] %= width

            y += 1

        except EOFError as error:
            return reduce(lambda x, y: x*y, trees, 1)

print(f"answer: {doCode()}")
