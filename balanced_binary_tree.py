# Problem: Balanced Binary Tree
# (https://leetcode.com/problems/balanced-binary-tree/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# No state
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.findHeight(root)[1]
        
    def findHeight(self, root):
        if root == None: return (0, True)
        l = self.findHeight(root.left)
        if l[1] == False: return (0, False)
        r = self.findHeight(root.right)
        if r[1] == False: return (0, False)
        return (max(l[0], r[0]) + 1, False if abs(l[0] - r[0]) > 1 else True)
        


# class Solution(object):
#     isTreeBalanced = True
    
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         self.isTreeBalanced = True
#         self.findHeight(root)
#         return self.isTreeBalanced
        
#     def findHeight(self, root):
#         if root == None or not self.isTreeBalanced: return 0        # stop recursion asap discovered not balanced
#         leftSubtreeHeight = self.findHeight(root.left)
#         rightSubtreeHeight = self.findHeight(root.right)
#         if abs(leftSubtreeHeight - rightSubtreeHeight) > 1: self.isTreeBalanced = False
#         return max(leftSubtreeHeight, rightSubtreeHeight) + 1
#         