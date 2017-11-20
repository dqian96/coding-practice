# Problem: Max Area of Island
# (https://leetcode.com/problems/max-area-of-island/)

class Solution(object):
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j - 1)
        if grid[i][j] == 0:
            return 0
        
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                maxArea = max(self.dfs(grid, i, j), maxArea)
        
        return maxArea
        