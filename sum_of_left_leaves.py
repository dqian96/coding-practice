# Problem: Sum of Left Leaves
# (https://leetcode.com/problems/sum-of-left-leaves/)

# NOTES:
# Given a binary tree.
# Find the sum of all left leaves.

# FORMALIZE:
# Each node of a binary tree has potentially a left child and/or a right child,
# and there are no cycles. 
# A left leave is a node with no children and it is the left child of its
# parent node.

# CATEGORIZE:
# Tree traversal

# METHODS:
# BFS or DFS

# NAIVE SOLUTION?
# ANALYSIS?

# OPTIMAL SOLUTION:
# Start from the root.
# If the root is not a leaf, then we apply the recursive
# procedure to the left and/or right child. For the left child, we
# pass in a left-child flag to indicate to the child that it is indeed
# a left child. We return the sum of the recursive procedure
# on the left child and the right child.
# If the root is a leaf, then we check if the left-child flag
# is true so that we know it is a left leaf. We return 1.

# ANALYSIS:
# This is O(n) run-time. This is optimal because we have to
# traverse every node of the tree to travel to the leaves
# and discover the number of left leaves, since we do not have a look ahead.
# Recursion might be a bit space heavy since we might be adding
# too much on the runtime stack, as each call pushes a stack frame on to it.
# DFS can also be done with a stack, using probably less memory.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(root, 0)]
        numLeftLeaves = 0
        while stack:
            nodeToTraverse = stack.pop()
            if nodeToTraverse[0].left is None and nodeToTraverse[0].right is None \
                and nodeToTraverse[1]:
                numLeftLeaves += nodeToTraverse[0].val
            else:
                if nodeToTraverse[0].right is not None:
                    stack.append((nodeToTraverse[0].right, 0))
                if nodeToTraverse[0].left is not None:
                    stack.append((nodeToTraverse[0].left, 1))
        return numLeftLeaves
