# Problem: Path sum II
# (https://leetcode.com/problems/path-sum-ii/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.findPaths(root, sum, [], result)
        return result

    def findPaths(self, root, sum, stack, result):
        if root == None: return
        stack.append(root.val)
        if root.left == None and root.right == None and sum - root.val == 0:
            result.append(stack[:])
        else:
            self.findPaths(root.left, sum - root.val, stack, result)
            self.findPaths(root.right, sum - root.val, stack, result)
        stack.pop()
