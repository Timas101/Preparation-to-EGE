from fnmatch import *

for num in range(0, 10**10, 1917):
    if fnmatch(str(num), '3?12?14*5'):
        print(num, num // 1917)