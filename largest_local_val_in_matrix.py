grid = [[7,2,9,4,1,6], [0,0,0,0,0,0], [1,2,3,4,5,6], [0,0,0,0,0,0],
        [0,0,0,0,0,0], [1,1,2,1,2,1]]

import numpy as np

grid = np.array(grid)
row, col = grid.shape[0], grid.shape[1]

top = 0
bottom = top + 2
left = 0
right = left + 2

op = np.zeros((row-2, col-2), dtype = int)

i = 0
j = 0

while bottom < row :
    while right < col :
        op[i][j] = grid[top:bottom + 1, left:right + 1].max()
        right += 1
        left += 1
        j += 1
    top += 1
    bottom += 1
    left = 0
    right = left + 2
    i += 1
    j = 0

print(op)
