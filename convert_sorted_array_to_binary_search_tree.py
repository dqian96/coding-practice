# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return None
        return self.createBSTByDividingArray(0, len(nums), nums)

    def createBSTByDividingArray(self, inclusiveStart, exclusiveEnd, array):
        if inclusiveStart >= exclusiveEnd: return None
        midpoint = (inclusiveStart + exclusiveEnd)/2
        root = TreeNode(array[midpoint])
        root.left = self.createBSTByDividingArray(inclusiveStart, midpoint, array)
        root.right = self.createBSTByDividingArray(midpoint + 1, exclusiveEnd, array)
        return root
