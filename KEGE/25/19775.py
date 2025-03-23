def Del(num):
    result = set()
    for delit in range(2, int(num ** 0.5) + 1):
        if num % delit == 0:
            result.add(delit)
            result.add(num // delit)
    return sorted(result)

count = 0
for num in range(32500000, 32550000):
    delit = [i for i in Del(num) if len(Del(i)) == 0]
    sum_delit = sum(delit)
    if sum_delit != 0 and sum_delit % 145 == 0:
        count += 1
        print(num, sum_delit)
    if count >= 7:
        break