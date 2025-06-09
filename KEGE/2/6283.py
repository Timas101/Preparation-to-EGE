from itertools import *

def F(x, y, w, z):
    return not((x <= (not w)) and z) and not(w <= z) and (x <= (not z))

count = 0
for a in product([0, 1], repeat=5):
    table = ((1, 0, a[0], 0), (1, 0, a[1], a[2]), (a[3], 1, a[4], 1)) 
    if len(table) != 3:
        continue
    for i in permutations("xyzw"):
        if [F(**dict(zip(i, row))) for row in table] == [1, 0, 0]:
            count += 1
print(count)