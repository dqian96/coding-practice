# Problem: Convert BST To Greater Tree
# (https://leetcode.com/submissions/detail/102964159/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    accumulator = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder(root)
        return root
        
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.right)
        self.accumulator += root.val
        root.val = self.accumulator
        self.inorder(root.left)
        