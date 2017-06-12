# Problem: Missing Number
# (https://leetcode.com/problems/missing-number/#/description)

# Use arithmetic series (expected value vs actual)

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int(len(nums) * (len(nums) + 1.0)/2 - sum(nums))
