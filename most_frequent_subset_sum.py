# Problem: Most frequent Subtree Sum
# (https://leetcode.com/problems/most-frequent-subtree-sum/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        subTreeSums = defaultdict(int)
        if root == None:
            return []
        self.findSubtreeSums(root, subTreeSums)
        maxNumOccurences = max(subTreeSums.values())
        return [x for x in subTreeSums.keys() if subTreeSums[x] == maxNumOccurences]

    def findSubtreeSums(self, root, subTreeSums):
        if root == None:
            return 0
        subTreeSum = self.findSubtreeSums(root.left, subTreeSums) + self.findSubtreeSums(root.right, subTreeSums) + root.val
        subTreeSums[subTreeSum] += 1
        return subTreeSum