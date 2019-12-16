#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def maxDistToClosest(seats: List[int]) -> int:
    count = 0
    dis = 0
    head = not seats[0]
    tail = not seats[-1]

    for s in seats:
        if s == 1:
            if head:
                dis = max(dis, count)
                head = False
            dis = max(dis, (count + 1) // 2)
            count = 0
        else:
            count += 1
    if tail: dis = max(dis, count)

    return dis




x = [1,0,0,0,0]
y = maxDistToClosest(x)
print(y)