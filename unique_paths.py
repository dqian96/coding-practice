# Problem: Unique Paths
# (https://leetcode.com/problems/unique-paths/description/)

from collections import defaultdict

class Solution(object):
    def dp(self, x, y, m, n, mem):
        if (x, y) in mem:
            return mem[(x, y)]
        if x >= m or y >= n:
            return 0
        mem[(x, y)] = self.dp(x + 1, y, m, n, mem) + self.dp(x, y + 1, m, n, mem)
        return mem[(x, y)]
    
    def uniquePaths(self, m, n):
        mem = defaultdict(int)
        mem[(m - 1, n - 1)] = 1
        return self.dp(0, 0, m, n, mem)
    