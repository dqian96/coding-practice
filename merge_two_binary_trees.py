# Problem: Merge Two Binary Trees
# (https://leetcode.com/problems/merge-two-binary-trees/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None: return None

        root = TreeNode(t1.val + t2.val if t1 != None and t2 != None else (t1.val if t1 != None else t2.val))
        root.left = self.mergeTrees(t1.left if t1 != None else None, t2.left if t2 != None else None)
        root.right = self.mergeTrees(t1.right if t1 != None else None, t2.right if t2 != None else None)
        return root
