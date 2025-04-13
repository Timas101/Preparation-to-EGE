print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (x >= w) and not(y)
                if F:
                    print(x, w, z, y, F)