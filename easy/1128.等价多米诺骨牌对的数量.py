#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    count = 0

    for i in range(len(dominoes) - 1):
        for j in range(i + 1, len(dominoes)):
            if (dominoes[i] == dominoes[j]) | (dominoes[i] == dominoes[j][::-1]):
                count +=1
            

    return count



dominoes = [[1,2],[2,1],[3,4],[5,6]]
y = numEquivDominoPairs(dominoes)
print(y)