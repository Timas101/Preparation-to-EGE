def NtoR(n):
    n_st = n * 2
    n_bin = bin(n)[2:]
    for _ in range(2):
        s_n = n_bin.count('1')
        n_bin = n_bin + str(int(s_n) % 2)
    return int(n_bin, 2)

for n in range(1000):
    if NtoR(n) > 1017:
        print(n)
        break

