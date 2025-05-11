string = str(open(r"E:\Preparation-to-EGE\KEGE\24\19149\24_19149.txt").readline())

max_len = 0
res_srtring = ''
len = 0
flag = False
right_match = True
last_simb = ''
for simb in string:
    if simb == '(':
        flag = True
        continue
    if flag:
        if simb == ')':
            if right_match:
                flag = False
                if eval(res_srtring) % 2 == 0:
                    max_len = max(len, max_len)
                    res_srtring = ''
                    len = 0
                len = 0
            else:
                len = 0
                res_srtring = ''
                flag = False
                right_match = True
            
        if simb == '+' and last_simb == '+':
            right_match = False
            len = 0
        else:
            last_simb = simb
            len += 1
            res_srtring += simb

print(max_len)