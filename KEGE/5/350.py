def NumToResult(num):
    bin_num = bin(num)[2:]
    for _ in range(2):
        if bin_num.count('1') > bin_num.count('0'):
            bin_num = bin_num + '0'
        else:
            bin_num = '11' + bin_num
    return int(bin_num, 2)

for num in range(1, 1000):
    result = NumToResult(num)
    if result > 500:
        print(num)
        break