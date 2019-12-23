#!/usr/bin/python
#-*- coding: utf-8 -*-

def trailingZeroes(n: int) -> int:
    answer = 1
    while n > 1:
        answer *= n
        n -= 1

    import re
    f = re.findall('[1-9]([0]*0$)', str(answer))
    if f:
        return len(f[0])
    else:
        return 0



x = 7
y = trailingZeroes(x)
print(y)



