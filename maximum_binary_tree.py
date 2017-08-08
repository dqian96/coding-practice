# Problem: Maximum Binary Tree
# (https://leetcode.com/problems/maximum-binary-tree/description/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createMaximumTree(0, len(nums), nums)
    
    def createMaximumTree(self, inclusiveLower, exclusiveUpper, nums):
        if inclusiveLower >= exclusiveUpper:
            return None
        maxValIndex = inclusiveLower
        for i in range(inclusiveLower, exclusiveUpper):
            maxValIndex = maxValIndex if nums[maxValIndex] > nums[i] else i
        root = TreeNode(nums[maxValIndex])
        root.left = self.createMaximumTree(inclusiveLower, maxValIndex, nums)
        root.right = self.createMaximumTree(maxValIndex + 1, exclusiveUpper, nums)
        return root
        