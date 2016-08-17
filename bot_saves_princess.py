# Problem: Bot Saves Princess
# (https://www.hackerrank.com/challenges/saveprincess)
# Simple problem. Find the locations of p and m. Then the shortest
# path is the path in which no steps are "wasted". Simply traverse
# to the proper row/column. This is O(n).

#!/bin/python
def displayPathtoPrincess(n,grid):
    # Find the starting location M (O(n))
    locationOfM = [0,0]
    for rowIdx, row in enumerate(grid):
        for columnIdx, column in enumerate(row):
            if column == 'm':
                locationOfM = [rowIdx, columnIdx]
                break
                
    # Find the destination location P (constant time)
    locationOfP = [0,0]
    if grid[0][0] == 'p':
        locationOfP = [0,0]
    elif grid[0][n-1] == 'p':
        locationOfP = [0, n-1]
    elif grid[n-1][0] == 'p':
        locationOfP = [n-1, 0]
    else:
        locationOfP = [n-1, n-1]

    step = ""
    # Traverse to proper row
    if locationOfM[0] > locationOfP[0]:
        step += "UP\n"*(locationOfM[0] - locationOfP[0])
    else:
        step += "DOWN\n"*(locationOfP[0] - locationOfM[0])
    
    # Traverse to proper column
    if locationOfM[1] > locationOfP[1]:
        step += "LEFT\n"*(locationOfM[1] - locationOfP[1])
    else:
        step += "RIGHT\n"*(locationOfP[1] - locationOfM[1])
    
    print step
    

        

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
    