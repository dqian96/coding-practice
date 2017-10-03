# Problem: Unique Binary Search Trees II
# (https://leetcode.com/problems/unique-binary-search-trees-ii/description/)

from collections import defaultdict

class Solution(object):
    def copyAndShift(self, root, x):
        if root == None:
            return None
        newRoot = TreeNode(root.val + x)
        newRoot.left = self.copyAndShift(root.left, x)
        newRoot.right = self.copyAndShift(root.right, x)
        
        return newRoot
        
    def dp(self, low, high, ht):
        if (low, high) in ht:
            return ht[(low, high)]
        if low == high:
            ht[(low, high)] = [TreeNode(low)]
            return ht[(low, high)]
        if high < low or low > high:
            return [None]
        if low != 1:
            if (1, high - (low - 1)) not in ht:
                self.dp(1, high - (low - 1), ht)
            treeBasedAt1 = (1, high - (low - 1))
            ht[(low, high)] = []
            for tree in ht[treeBasedAt1]:
                ht[(low, high)].append(self.copyAndShift(tree, low - 1))
            return ht[(low, high)]        
        
        ht[(low, high)] = []
        for root in range(low, high + 1):
            leftSubtrees = self.dp(1, root - 1, ht)
            rightSubtrees = self.dp(root + 1, high, ht)
            for l in leftSubtrees:
                for r in rightSubtrees:
                    rt = TreeNode(root)
                    rt.left = l
                    rt.right = r
                    ht[(low, high)].append(rt)

        return ht[(low, high)]
            
    def generateTrees(self, n):
        if n == 0: return []
        ht = defaultdict(list)
        return self.dp(1, n, ht)
