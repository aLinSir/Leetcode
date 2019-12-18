#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    if x < 1 or  y < 1: return []

    import math
    nx = int(math.log(bound, x)) if x!= 1 else 1
    ny = int(math.log(bound, y)) if y!= 1 else 1

    answer = []
    for i in range(nx + 1):
        for j in range(ny + 1):
            sum = x ** i + y ** j
            if sum <= bound and sum not in answer:
                answer.append(sum)

    return answer



x = 2
y = 1
bound = 10
re = powerfulIntegers(x, y, bound)
print(re)