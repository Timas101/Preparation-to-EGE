alp = [chr(i) for i in range(ord('C'), ord('Z') + 1)]
alp_ = alp + ['0']
alp__ = alp + [hex(i)[2:].upper() for i in range(1, 12, 2)]
base_string = str(open(r"24_21421.txt").readline())

for letter in alp:
    base_string = base_string.replace(letter, ' ')
string_aray = base_string.split()

max_len = 0
for str_part in string_aray:
    while str_part[0] == '0':
        str_part = str_part[1:] 
        if len(str_part) == 0:
            break
    if str_part:
        str_part_ten = int(str_part, 12)
        if str_part_ten % 2 == 0:
            max_len = max(max_len, len(str_part))

print(max_len)
'''
FIND = 1
COUNT = 0

count = 0
max_count = 0
flag = FIND
for element in reversed(base_string):
    if flag == FIND:
        if element in alp__:
            continue
        else:
            i = COUNT
            count = 1
    if flag == COUNT:
        if element in alp_:
            i = FIND
            max_count = max(max_count, count)
            count = 0
        else:
            count += 1
print(max_count)

'''