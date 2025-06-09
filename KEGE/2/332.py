from itertools import *

def f(x, y, z, w):
    return (x or y (not z)) and (not w)

set_res = set()
table = ((1, 0, 0, 0),
            (0, 0, 1, 0),
            (0, 1, 0, 1))
if len(table) == len(set(table)):
    for i in permutations('xywz'):
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 0]:
            set_res.add(i)
print(len(set_res))
