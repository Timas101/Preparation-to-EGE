from sys import setrecursionlimit
setrecursionlimit(10**6)

def Calk(s_num, e_num):
    if s_num > e_num:
        return 0
    if s_num == e_num:
        return 1
    if s_num < e_num:
        return Calk(Delit(s_num), e_num) + Calk(s_num + 1, e_num)


def Delit(num):
    xyi = set()
    for deli in range(1, int(num ** 0.5) + 1):
        if num % deli == 0:
            xyi.add(deli)
            xyi.add(num // deli)
    return sum(xyi)
            

s_num = 2
e_num = 24
print(Calk(s_num, e_num))

