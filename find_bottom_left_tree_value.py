# Problem: Find Bottom Left Tree Value
# (https://leetcode.com/problems/find-bottom-left-tree-value/description/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getLeftMostValueAndDepth(root)[1]
        
    def getLeftMostValueAndDepth(self, root):
        # returns a tuple (tree depth, leftmost value)
        if root == None:
            return (-1, None)
            
        leftRes = self.getLeftMostValueAndDepth(root.left)
        rightRes = self.getLeftMostValueAndDepth(root.right)
        
        if (leftRes[0] == -1 and rightRes[0] == -1):
            return (0, root.val)
        
        if leftRes[0] >= rightRes[0]:
            return (leftRes[0] + 1, leftRes[1])
        return (rightRes[0] + 1, rightRes[1])
            
        
        