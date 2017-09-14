# Problem: Second Minimum Node in a Binary Tree
# (https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/)

class Solution(object):
    def dfs(self, root, n):
        if root == None:
            return -1
        if root.val > n:
            return root.val
        leftSmallest = self.dfs(root.left, n)
        rightSmallest = self.dfs(root.right, n)
        
        if leftSmallest != -1 and rightSmallest != -1:
            return min(leftSmallest, rightSmallest)
        return max(leftSmallest, rightSmallest)
        
        
    def findSecondMinimumValue(self, root):
        if root == None:
            return -1
        return self.dfs(root, root.val)
    