#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def numMagicSquaresInside(grid: List[List[int]]) -> int:

    def isHF(matrix):

        dial = matrix[0][0] + matrix[1][1] + matrix[2][2]

        if matrix[0][2] + matrix[1][1] + matrix[2][0] != dial: return False

        for rows in matrix:
            if sum(rows) != dial: return False

        for c in range(3):
            if matrix[0][c] + matrix[1][c] + matrix[2][c] != dial: return False

        tmp = []
        for i in range(3):
            for j in range(3):
                tmp.append(matrix[i][j])

        return min(tmp) == 1 and max(tmp) == 9


    count = 0
    row, col = len(grid), len(grid[0])

    for i in range(0, row - 3 + 1):
        for j in range(0, col - 3 + 1):

            tmp_grid = []
            tmp_grid.append(grid[i][j: j + 3])
            tmp_grid.append(grid[i + 1][j: j + 3])
            tmp_grid.append(grid[i + 2][j: j + 3])

            if isHF(tmp_grid): count += 1

    return count



x =  [[7,0,5],
      [2,4,6],
      [3,8,1]]
y = numMagicSquaresInside(x)
print(y)