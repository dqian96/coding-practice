# Problem: Unique Paths
# (https://leetcode.com/problems/unique-paths/description/)

from collections import defaultdict

class Solution(object):
    def uniquePaths(self, m, n):
        table = [[0 for i in range(m)] for j in range(n)]
        table[-1][-1] = 1
        for y in range(n - 1, -1, -1):
            for x in range(m - 1, -1, -1):
                if x == m - 1 and y == n - 1:
                    continue
                table[y][x] = (0 if y + 1 >= n else table[y + 1][x]) + (0 if x + 1 >= m else table[y][x + 1])
        return table[0][0]
    