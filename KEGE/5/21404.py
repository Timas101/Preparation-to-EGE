def NtoR(n):
    n_four = ToFour(n)
    if n % 3 == 0:
        last = n_four[-1]
        start = n_four[0]
        n_ = n_four[:1]
        n_ = n_four[-1:]
        n_res =  last + n_ + start + '1'
    if n % 3 != 0:
        n_res = n_four + str(n % 3)
    
    return int(n_res, 4)

def ToFour(n):
    res = ''
    while n != 0:
        ost = str(n % 4)
        res = ost + res
        n = n // 4
    return res

res = 0
for n in range(1, 1000, 2):
    r  =  NtoR(n)
    if r <= 340:
        res = max(r, res)

print(res)