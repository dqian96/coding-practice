# Problem: Binary Tree Paths
# (https://leetcode.com/problems/binary-tree-paths/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, [], res)
        return res
    
    def dfs(self, root, stack, res):
        if root == None: return
        stack.append(str(root.val))
        if root.left == None and root.right == None:
            res.append("->".join(stack))
        else:
            self.dfs(root.left, stack, res)
            self.dfs(root.right, stack, res)
        stack.pop()
        