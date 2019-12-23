#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    count = 0
    d = {}

    dominoes = [str(min(a, b)) + str(max(a, b)) for a, b in dominoes]

    for l in dominoes:
        if l in d:
            d[l] += 1
        else:
            d[l] = 1

    for n in list(d.values()):
        while n >= 2:
            n -= 1
            count += n

    return count



dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
y = numEquivDominoPairs(dominoes)
print(y)