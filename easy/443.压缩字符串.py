#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def compress(chars: List[str]) -> int:
    idx = anchor = 0
    for i, c in enumerate(chars):
        if i + 1 == len(chars) or chars[i + 1] != c:
            chars[idx] = chars[anchor]
            idx += 1
            if i > anchor:
                for digit in str(i - anchor + 1):
                    chars[idx] = digit
                    idx += 1
            anchor = i + 1

    return idx






x = ["a","a","a","a","a","b"]

y = compress(x)
print(y)