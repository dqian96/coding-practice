# Problem: Max Increase to Keep City Skyline
# (https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/)

from collections import defaultdict

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        maxIncrease = 0
        d = defaultdict() # positive key => max in row, negative key => max in column
        for r in range(len(grid)):
            if r + 1 not in d:
                d[r + 1] = max(grid[r])
            for c in range(len(grid[0])):
                if -c - 1 not in d:
                    d[-c - 1] = max([grid[x][c] for x in range(len(grid))])
                maxIncrease += max(min(d[r + 1], d[-c - 1]) - grid[r][c], 0)
        return maxIncrease

