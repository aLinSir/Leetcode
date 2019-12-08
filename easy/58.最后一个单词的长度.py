#!/usr/bin/python 
# -*- coding: utf-8 -*-

def lengthOfLastWord(s: str) -> int:
    last_word =s.strip().split(' ')[-1]
    return len(last_word)



s = " "
a = lengthOfLastWord(s)
print(a)


