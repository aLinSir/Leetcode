#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    import re
    word_list = re.findall(u'[a-z]+', paragraph.lower())

    from collections import Counter
    for word, _ in Counter(word_list).most_common():
        if word not in banned:
            return word






paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
y = mostCommonWord(paragraph, banned)
print(y)