def NtoR(n):
    n_bin = bin(n)[2:]
    for _ in range(2):
        ost = n_bin.count('1') % 2
        n_bin = n_bin + str(ost)
    return int(n_bin, 2)

for n in range(1, 100):
    if NtoR(n) > 253:
        print(n)
        break