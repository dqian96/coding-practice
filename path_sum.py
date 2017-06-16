# Problem: Path Sum
# (https://leetcode.com/problems/path-sum/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """ 
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        if root.left == None and root.right == None: return True if sum - root.val == 0 else False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
