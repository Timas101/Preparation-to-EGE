from itertools import *

def f(x, y, z, w):
    return ((not(x <= y)) or (z == w) or z)
for a in product([0, 1], repeat=8):
    table = [(0, 0, a[0], a[1]), (a[2], a[3], 1, a[5]), (a[6], 1, 0, a[7])]
    if len(set(table)) != 3:
        continue
    for i in permutations('xyzw'):
        if [f(**dict(zip(i,stroka))) for stroka in table] == [0,0,0]:
            print(i)





'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(x <= y) or (z == w) or z) == 0:
                    print(x, y, z, w)

'''