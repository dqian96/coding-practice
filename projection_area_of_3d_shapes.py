# Problem: Projection Area of 3D Shapes
# (https://leetcode.com/contest/weekly-contest-96/problems/projection-area-of-3d-shapes/)

from collections import defaultdict

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_area = 0

        max_cols = defaultdict(int)
        for r in range(len(grid)):

            max_height = 0
            for c in range(len(grid[r])):
                if grid[r][c] != 0:
                    total_area += 1
                max_height = max(max_height, grid[r][c])

                max_cols[c] = max(max_cols[c], grid[r][c])

            total_area += max_height

        for k, v in max_cols.items():
            total_area += v

        return total_area
