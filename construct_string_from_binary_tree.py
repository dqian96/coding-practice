# Problem: Construct String from Binary Tree
# (https://leetcode.com/problems/construct-string-from-binary-tree/#/description)

# Appended to an array instead of string concatentation since each append is O(1)
# instead of O(n) concat

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2List(self, t, treeList):
        if t == None:
            return ""
        treeList.append(str(t.val))
        if t.left != None:
            treeList.append("(")
            self.tree2List(t.left, treeList)
            treeList.append(")")
        elif t.left == None and t.right != None:
            treeList.append("(")
            treeList.append(")")
        if t.right != None:
            treeList.append("(")
            self.tree2List(t.right, treeList)
            treeList.append(")")

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        treeList = []
        self.tree2List(t, treeList)
        return "".join(treeList)
