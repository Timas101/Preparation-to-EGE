from itertools import product, permutations

def f(x, y, z, w):
    return (not (x ==(w and(not z)))) and (y == (x and( not w)))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = {(a1, a2, 0, a3),
             (a4, 0, a5, 0),
             (0, a6, 1, 0)}
    for i in permutations("xywz"):
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]:
            print(*i)