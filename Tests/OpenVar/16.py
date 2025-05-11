from sys import setrecursionlimit
setrecursionlimit(10**6)

def F(n):
    if n >= 7025:
        return n
    if n < 7025:
        return n*2 + F(n+2)
    
print(F(82) - F(81))