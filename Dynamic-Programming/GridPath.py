# -*- coding: utf-8 -*-
"""
@author: Waleed

Calculates possible paths from top left a m*n grid to the bottom right provided only
down, right and left-down diagonal mocements are allowed.

"""

m,n = 3,3

grid = [[0 for x in range(m)] for y in range(n)]

for i in range(m):
    grid[i][0] = 1

for j in range(n):
    grid[0][j] = 1


for i in range(1,m):
    for j in range(n):
        
        grid[i][j] = grid[i-1][j] + grid[i][j-1] + grid[i-1][j-1]

print(grid[m-1][n-1])
