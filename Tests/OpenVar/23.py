def F(n, e):
    if n == e or n == 8:
        return 1
    if n >  e:
        return 0
    return F(n + 1, e) + F(n + 2, e) + F(n * 2, e)

print(F(3, 14) + F(14, 18))