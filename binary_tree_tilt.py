# Problem: Binary Tree Tilt
# (https://leetcode.com/problems/binary-tree-tilt/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Find sum of each subtree, at the same time as finding tilt of each subtree

class Solution(object):
    tilt = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.findSum(root)
        return self.tilt
    
    def findSum(self, root):
        if root == None: return 0
        leftSum, rightSum = self.findSum(root.left), self.findSum(root.right)
        self.tilt += abs(leftSum - rightSum)
        return root.val + leftSum + rightSum
        