def Del(num):
    result = set()
    for delit in range(2, int(num ** 0.5) + 1):
        if num % delit == 0:
            result.add(delit)
            result.add(num // delit)
    return sorted(result)

for num in range(112500000, 112550000):
    delit = Del(num)
    if len(delit) >= 2:
        sum_max = delit[-1] + delit[-2]
    else:
        sum_max = 0
    if sum_max % 10000 == 1214:
        print(num)