def Del(num):
    result = set()
    for delit in range(2, int(num ** 0.5) + 1):
        if num % delit == 0:
            result.add(delit)
            result.add(num // delit)
    return sorted(result)

count = 0
for num in range(1200000, 1230000):
    delit = [i for i in Del(num) if len(Del(i)) == 0]
    if delit:
        max_del = max(delit)
        min_del = min(delit)
        sum_max_min = max_del + min_del
        if sum_max_min > 2000 and sum_max_min % 10 == 8:
            print(num, sum_max_min)
            count += 1
    if count == 5:
        break