# Problem: Number of Paths in a Matrix

"""

You're given a mxn matrix. Each element in the matrix is either a 0 or 1.

1 represents an "open" position and 0 represents a "blocked" position.

If you're initially at position (0, 0), enumerate the total number of paths you can take
to position (m-1, n-1), given that you can only:

1. Move down and right
2. Move to open positions

Solution:

Eiter use DFS or DP.

DFS: Recursively search the tree from the starting position. Accumulate the number of paths
from the current position to the end position. This means at every node, return the number of paths from
the current node to the end position. Memoize this to avoid recaculating for the same node.

DP: At every position, there are a + b paths to get to it. There are a paths if the last position
was up and b paths if the last position was left. Recursively solve this from the end position.
The base case is the first position.

Tidbit: Apparently, recursion is not efficient enough and exceeds the max recursion depth since
M and N <= 1000. Thus, we can do DFS with a stack instead, using the matrix itself to keep
state.

"""
def numberOfPaths(a):
    if a[-1][-1] == 0 or a[0][0] == 0:
        return 0
    a[-1][-1] = -1
    stack = []
    stack.append((0, 0))
    while len(stack) != 0:
        pos = stack.pop()
        x = pos[0]
        y = pos[1]

        comeBack = False
        
        if x == len(a[0]) - 1 and y == len(a) - 1: 
            continue
        if x + 1 < len(a[0]) and a[y][x + 1] == 1:
            # right valid
            comeBack = True            
            stack.append(pos)
            stack.append((x + 1, y))
        if y + 1 < len(a) and a[y + 1][x] == 1:
            # left valid
            if not comeBack:
                stack.append(pos)
                comeBack = True
            stack.append((x, y + 1))

        if comeBack:
            continue

        a[y][x] = (0 if x + 1 >= len(a[0]) else a[y][x + 1]) + (0 if y + 1 >= len(a) else a[y + 1][x])

    return -a[0][0] % (10 ** 9 + 7)
