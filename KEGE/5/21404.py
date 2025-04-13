def NToR(n):
    n_bin = bin(n)[2:]
    if n_bin.count('1') % 2 == 0:
        n_bin = n_bin + '0'
        n_bin_res = '10' + n_bin[2:]
    else:
        n_bin = n_bin + '1'
        n_bin_res = '11' + n_bin[2:]
    return int(n_bin_res, 2)

for n in range(1, 1000):
    r = NToR(n)
    if r > 480:
        print(n)
        break
