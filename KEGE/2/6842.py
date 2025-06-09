from itertools import *

def f(x, y, z, w):
    return w and ((z or y) == (z and x))

for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    t = {(1, a1, 1, 0), (0, a2, a3, a4), (1, 1, 1, a5)}
    if len(t) != 3:
        continue
    
    for i in permutations("xywz"):
        if [f(**dict(zip(i, row))) for row in t] == [1, 1, 0]:
            print(*i)

