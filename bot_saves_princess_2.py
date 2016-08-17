# Problem: Bot saves princess 2
# (https://www.hackerrank.com/challenges/saveprincess2)

# Same problem as Bot Saves Princess except that 
# we are given the location of M but not of P. O(n).

#!/bin/python
def nextMove(n,r,c,grid):
    
    # Find the location of P (O(n))
    locationOfP = [0,0]
    for rowIdx, row in enumerate(grid):
        for columnIdx, column in enumerate(row):
            if column == 'p':
                locationOfP = [rowIdx, columnIdx]
                break
    
    # Traverse to proper row
    if locationOfP[0] > r:
        print "DOWN"
    elif locationOfP[0] < r:
        print "UP"
    elif locationOfP[1] > c:
        print "RIGHT"
    elif locationOfP[1] < c:
        print "LEFT"
    
    return ""
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
