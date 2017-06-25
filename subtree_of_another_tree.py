# Problem: Subtree of another Tree
# (https://leetcode.com/problems/subtree-of-another-tree/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.compareSubtree(s, t): return True
        if s == None: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def compareSubtree(self, s, t):
        if s == t: return True
        if s == None or t == None: return False
        if s.val != t.val: return False
        return self.compareSubtree(s.left, t.left) and self.compareSubtree(s.right, t.right)
        