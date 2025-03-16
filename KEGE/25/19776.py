from math import sqrt

def DelFound(num):
    delit = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            delit.add(i)
            delit.add(num // i)
    return sorted(delit)

count = 0
for num in range(23600000, 23601000):
    delit = DelFound(num)
    if len(delit) != 0:
        summ_delit = delit[0] + delit[-1]
        if summ_delit % 213 == 171:
            count += 1
            print(num, summ_delit)
            if count == 6:
                break