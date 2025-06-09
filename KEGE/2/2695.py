from itertools import *

def F(x, y, z, w):
    return (w or y) and (x <= (not z)) and (not w)

set_res = set()
for a in product([0, 1], repeat=5):
    table = ((a[0], 0, a[1], 0), 
             (1, a[2], a[3], a[4]), 
             (1, 1, 0, 0))
    if len(table) == len(set(table)):
        for i in permutations("xyzw"):
            if [F(**dict(zip(i, row))) for row in table] == [1, 1, 1]:
                set_res.add(i)

print(len(set_res))