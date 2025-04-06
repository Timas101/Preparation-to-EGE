aray = [int(x[:-1]) for x in open(r"26_7096.txt").readlines()]

aray.sort(reverse = True)

result = aray[0]
count = 1
for num in range(1, len(aray)):
    if result - aray[num] >= 11:
        count += 1
        result = aray[num]
print(count, result)

    