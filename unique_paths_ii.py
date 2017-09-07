# Problem: Unique Paths II
# (https://leetcode.com/problems/unique-paths-ii/description/)

from collections import defaultdict

class Solution(object):
    def dp(self, x, y, matrix, mem):
        if (x, y) in mem:
            return mem[(x, y)]
        if x >= len(matrix[0]) or y >= len(matrix):
            return 0
        if matrix[y][x] == 1:
            mem[(x, y)] = 0
            return 0
        mem[(x, y)] = self.dp(x + 1, y, matrix, mem) + self.dp(x, y + 1, matrix, mem)
        return mem[(x, y)]
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        mem = defaultdict(int)
        mem[(len(obstacleGrid[0]) - 1, len(obstacleGrid) - 1)] = 1
        return self.dp(0, 0, obstacleGrid, mem)
    