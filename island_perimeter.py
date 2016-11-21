# Problem: Island Perimeter
# (https://leetcode.com/problems/island-perimeter/)


# NOTES:

# given a 2D array of integers, representing a map
# 1 represents land, 0 represnets water
# grid cells are connected horizontally/vertically but not dialognally
# grid is surrounded by water
# one island in map (one or more connected land cells)
# no lakes
# one cell is a square with side length 1

# determine perimeter of the island
# tldr; given a 2d array of integers representing a map
# and integer 1 representing land, such that horizontal
# and vertical adjacent 1's represents contiunous land, find the perimeter
# of the single island in the map

# CATEGORIZE:
# graph, array

# REASONING:

# Let's say we are at a particular index/position on land.
# How much perimeter does this contribute?
# If there is land above, then the upwards facing side does not
# contribute to the perfimeter.
# If there is land to the sides...
# If there is land to to the bottom...

# If the top/bottom/left/right indices are not 1, then we count the respective
# side length as part of the perimeter.
# Coincendetally, if that side is water, then there is no need to search it.

# After confirming the current position (i.e. adding to total perimeter for
# water-sides), we must:
# search the top/bottom/left/right positions if it is a 1/water.

# Here lies another question. How do we know whether or not we have searched
# a particular position? We can:
# -leave a marker i.e. make it 2
# -record its position in a hash map

# The first option is quicker.


# OPTIMAL SOLUTION:
# Traverse the map until we find the first 1.
# Recursively:
#   -replace the 1 in this position with 2 to symbolize that this is
#   traversed land
#   -add 1 to the total perimeter for each top/left/bottom/right
#   side that is 0 (i.e. that side of the island is part of the perimeter)
#   -recursively do this function for each side that is only 1
#   (i.e. 2 => already traversed, 0 => no point in traversing water
#   since will not add to perimeter and all land will be reached
#   by traversing through land)

# ANALYSIS:
# O(n)

"""

class Solution(object):
    def islandPerimeter(self, grid):
        def searchGrid(x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == 0:
                # water position, the calling function's position must be 1
                # (to call this function) and so that side is surrounded by water
                return 1
            elif grid[y][x] == 1:
                # search all sides
                grid[y][x] = 2
                return searchGrid(x, y-1) + searchGrid(x, y+1) + \
                    searchGrid(x-1, y) + searchGrid(x+1, y)
            else:
                # already traversed
                return 0

        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == 1:
                    return searchGrid(x, y)

"""

# Another way of solving this is iteratively.
# Simply iterate through the whole 2D array. If we arrive at 1,
# we check the surrounding left/right/bottom/top sides. If they are 0,
# then that side is on the perimeter and we add 1. Else we don't.
# We never go to the same position twice, since we are iterating
# in an uncyclic order. We are able to check every piece of land
# if it is on the perimeter and add the sides accordingly.


class Solution(object):
    def islandPerimeter(self, grid):
        totalPerimeter = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == 1:
                    if y-1 < 0 or grid[y-1][x] == 0:
                        totalPerimeter += 1
                    if y+1 == len(grid) or grid[y+1][x] == 0:
                        totalPerimeter += 1
                    if x-1 < 0 or grid[y][x-1] == 0:
                        totalPerimeter += 1
                    if x+1 == len(grid[0]) or grid[y][x+1] == 0:
                        totalPerimeter += 1
        return totalPerimeter
