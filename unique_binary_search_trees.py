# Problem: Unique Binary Search numTrees
# (https://leetcode.com/problems/unique-binary-search-trees/description/)

class Solution(object):
    def recurseNumTrees(self, n, T):
        if T[n-1] != -1:
            return T[n-1]
        if n == 1:
            return 1
        if n == 0:
            return 0
        numTrees = 0
        for i in range(1, n + 1):
            numTrees += max(self.recurseNumTrees(i - 1, T), 1) * max(self.recurseNumTrees(n - i, T), 1)
        T[n-1] = numTrees
        return numTrees
    
    def numTrees(self, n):
        T = [-1 for i in range(n)]
        return self.recurseNumTrees(n, T)
        