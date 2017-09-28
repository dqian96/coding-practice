# Problem: Binary Tree Longest Consecutive Sequence
# (https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/)

class Solution(object):
    def dfs(self, root):
        if root == None:
            return (0, 0)
        
        leftRes = self.dfs(root.left)
        rightRes = self.dfs(root.right)
        
        lcsFromRoot = 1
        if root.left is not None and root.left.val - root.val == 1:
            lcsFromRoot = leftRes[0] + 1
        if root.right is not None and root.right.val - root.val == 1:
            lcsFromRoot = max(lcsFromRoot, rightRes[0] + 1)
        
        maxLcs = max(lcsFromRoot, max(leftRes[1], rightRes[1]))
        
        return (lcsFromRoot, maxLcs)
        
        
    def longestConsecutive(self, root):
        return self.dfs(root)[1]
        