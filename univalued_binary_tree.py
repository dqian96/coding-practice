# Problem: Univalued Binary Tree
# (https://leetcode.com/problems/univalued-binary-tree/submissions/)

# Done as part of contest 117

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None or (root.left == None and root.right == None):
            return True
        if (root.left is None or root.left.val == root.val) and \
            (root.right is None or root.right.val == root.val):
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return False
