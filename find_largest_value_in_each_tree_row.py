# Problem: Find Largest Value in Each Tree Row
# (https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        largestValues = []
        self.dfs(root, 0, largestValues)
        return largestValues
    
    def dfs(self, root, row, largestValues):
        if root == None:
            return
        if row > len(largestValues) - 1:
            largestValues.append(root.val)
        else:
            largestValues[row] = max(largestValues[row], root.val)
        self.dfs(root.left, row + 1, largestValues)
        self.dfs(root.right, row + 1, largestValues)
