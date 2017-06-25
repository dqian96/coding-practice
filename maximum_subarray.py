# Problem: Maximum Subarray
# (https://leetcode.com/problems/maximum-subarray/#/description)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float("-inf")
        candidateSum = 0
        for num in nums:
            candidateSum += num
            maxSum = max(candidateSum, maxSum)
            if candidateSum < 0: candidateSum = 0
        return maxSum
