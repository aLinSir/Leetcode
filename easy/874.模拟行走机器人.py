#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def robotSim(commands: List[int], obstacles: List[List[int]]):
    x2y, y2x = {}, {}
    for a, b in obstacles:
        if a not in x2y:
            x2y[a] = [b]
        else:
            x2y[a].append(b)
        if b not in y2x:
            y2x[b] = [a]
        else:
            y2x[b].append(a)

    x, y = 0, 0
    x_c, y_c = 0, 1
    re = 0
    for c in commands:
        if c == -2:
            if x_c == 0 and y_c == 1:
                x_c, y_c = -1, 0
            elif x_c == -1 and y_c == 0:
                x_c, y_c = 0, -1
            elif x_c == 0 and y_c == -1:
                x_c, y_c = 1, 0
            elif x_c == 1 and y_c == 0:
                x_c, y_c = 0, 1
        elif c == -1:
            if x_c == 0 and y_c == 1:
                x_c, y_c = 1, 0
            elif x_c == 1 and y_c == 0:
                x_c, y_c = 0, -1
            elif x_c == 0 and y_c == -1:
                x_c, y_c = -1, 0
            elif x_c == -1 and y_c == 0:
                x_c, y_c = 0, 1
        else:
            tmp_x = x + x_c*c
            tmp_y = y + y_c*c

            if x_c == 0 and y_c == 1:
                if tmp_x in x2y:
                    for y_ in x2y[tmp_x]:
                        if y_ > y: tmp_y = min(tmp_y, y_ - 1)
            elif x_c == 1 and y_c == 0:
                if tmp_y in y2x:
                    for x_ in y2x[tmp_y]:
                        if x_ > x: tmp_x = min(tmp_x, x_ - 1)
            elif x_c == 0 and y_c == -1:
                if tmp_x in x2y:
                    for y_ in x2y[tmp_x]:
                        if y_ < y: tmp_y = max(tmp_y, y_ + 1)
            elif x_c == -1 and y_c == 0:
                if tmp_y in y2x:
                    for x_ in y2x[tmp_y]:
                        if x_ < x: tmp_x = max(tmp_x, x_ + 1)

            x, y = tmp_x, tmp_y
            re = max(re, x**2 + y**2)

    return re




commands = [-2,8,3,7,-1]
obstacles = [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]
a = robotSim(commands, obstacles)
print(a)