from sys import setrecursionlimit
setrecursionlimit(10**6)

def F(start, end, countA):
    if start == end :
        return 0
    elif start > end + 2:
        return 0
    elif start == end and countA <= 2:
        return 1
    return F(start - 1, end, countA + 1) + F(start + 5, end, countA) + F(start * 2, end, countA)

print(F(5, 34, 0))