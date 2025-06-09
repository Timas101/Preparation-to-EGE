def F(start, end):
    if start == end:
        return 1
    if start < end or start == 18:
        return 0
    if start % 2 == 0:
        return F(start / 2, end) + F(start - 2, end)
    else:
        return F(start - 2, end) + F(start - 3, end)
    
print(F(55, 3))