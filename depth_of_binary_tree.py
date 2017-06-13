# Problem: Depth of Binary Tree
# (https://leetcode.com/problems/diameter-of-binary-tree/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    diameter = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.findDepth(root)
        return self.diameter
        
    def findDepth(self, root):
        if root == None:
            return 0
        leftDepth = self.findDepth(root.left) + (0 if root.left == None else 1)
        rightDepth = self.findDepth(root.right) + (0 if root.right == None else 1)
        self.diameter = max(self.diameter, leftDepth + rightDepth)
        return max(leftDepth, rightDepth)
