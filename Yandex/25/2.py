def DelCheck(num):
    result = set()
    for i in range(2,num**2):
        if num % i == 0 and i % 10 == 8:
            result.add(i)
            result.add(num//i)
    return sum(result)

for num in range(114578, 114616 +1):
    sum_del = DelCheck(num)
    if sum_del % 10 == 6:
        print(num, sum_del)