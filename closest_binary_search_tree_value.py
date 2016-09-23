# Problem: Closest Binary Search Tree Value
# (https://leetcode.com/problems/closest-binary-search-tree-value/)

# This can be solved in O(logn).
# Let's say we have target t and TreeNode root.
# If t == root.val, we know that the closest node to t is root.val.
# Without loss of generality, assume that t < root.val:
# Then, we know that t < root.val < for all x.val in nodes(root.right)
# Therefore, we need not consider the right subtree.
# Without consideration of the left subtree, the closest node to t is root.
# We know that for all x.val in nodes(root.left), x.val < root.val.
# However, diff(root.val, t) < diff(x.val, t) is possible. i.e. consider
# root.val = 5, root.left = 1, t.val = 4.
# So, for any root, the solution/closest node to t, is either root, or a node
# in the left subtree.
# We can iteratively/recurisvely go down each level of the tree to find the
# optimal solution, updating the closest node as we go.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
# class Solution(object):
#     def findClosestNode(self, closestValue, root, target):
#         if root is None:
#             return closestValue
#         elif root.val == target:
#             return target
#         elif abs(root.val - target) < abs(closestValue - target):
#             closestValue = root.val
#         if target < root.val:
#             return self.findClosestNode(closestValue, root.left, target)
#         else:
#             return self.findClosestNode(closestValue, root.right, target)

#     def closestValue(self, root, target):
#         """
#         :type root: TreeNode
#         :type target: float
#         :rtype: int
#         """
#         return self.findClosestNode(root.val, root, target)

# Iterative solution
class Solution(object):
    def closestValue(self, root, target):
        closestValue = root.val
        while root is not None:
            if target == root.val:
                return root.val
            elif abs(root.val - target) < abs(closestValue - target):
                closestValue = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closestValue
