# Problem: Minimum Absolute Difference in BST
# (https://leetcode.com/problems/minimum-absolute-difference-in-bst/#/description)

# It's a bst meaning in order traversal is basically "sorted"
# The smallest absolute difference of x to any other number
# is the number directly before or directly after it in the sorted list
# (in order traversal).

# We compare the differences between all adjacent numbers in the sorted list
# i.e. in order traversal to find the smallest difference possible

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    lastVal = float("inf")
    minDifference = float("inf")
    
    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        self.minDifference = min(self.minDifference, abs(self.lastVal - root.val)) if self.lastVal != float("inf") else self.minDifference
        self.lastVal = root.val
        self.inOrder(root.right)
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inOrder(root)
        return self.minDifference
