#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def hasGroupsSizeX(deck: List[int]) -> bool:
    s = set(deck)
    count_list = [deck.count(i) for i in s]
    min_count = min(count_list)
    has = False
    tmp_list = []
    for i in range(2, min_count + 1):
        if min_count % i == 0:
            tmp_list.append(i)

    for i in tmp_list:
        right = 0
        for c in count_list:
            if c % i != 0:
                break
            else:
                right += 1
        if right == len(count_list):
            has = True
            break
    return has


    # if not sum([deck.count(i) % 2 != 0 for i in s]):
    #     return True
    # elif not sum([deck.count(i) % 3 != 0 for i in s]):
    #     return True
    # elif not sum([deck.count(i) % 5 != 0 for i in s]):
    #     return True
    # else:
    #     return False

x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
y = hasGroupsSizeX(x)
print(y)