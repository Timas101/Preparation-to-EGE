def F(start, end):
    if start == end:
        return 1
    if start < end or start == 24:
        return 0
    return F(start - 1, end) + F(start - 4, end) + F(start // 2, end)

print(F(34, 30) * F(30, 20) * F(20, 9)) 