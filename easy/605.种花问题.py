#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    idxs = [i for i, v in enumerate(flowerbed) if v == 1]

    count = 0
    start = 0
    for i, idx in enumerate(idxs):
        tmp = flowerbed[start: idx]

        if i == 0 and len(tmp) >= 2:
            count += len(tmp) // 2
        elif len(tmp) >= 3:
            count += (len(tmp) - 1) // 3

        start = idx + 1

    if idxs:
        if len(flowerbed) - 1 > idxs[-1]:
            tmp2 = flowerbed[idxs[-1]: ]
            count += len(tmp2) // 2
    else:
        count += (len(flowerbed) + 1) // 2

    return n <= count


flowerbed = [1]
n = 1
a = canPlaceFlowers(flowerbed, n)
print(a)