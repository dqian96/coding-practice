# Problem: Maximum Product Subarray
# (https://leetcode.com/problems/maximum-product-subarray/description/)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSubproduct = nums[0]
        smallestSoFar = nums[0]
        biggestSoFar = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                biggestSoFar = max(nums[i], biggestSoFar * nums[i])
                smallestSoFar = min(nums[i], smallestSoFar * nums[i])
            else:
                temp = smallestSoFar
                smallestSoFar = min(biggestSoFar * nums[i], nums[i])
                biggestSoFar = max(temp * nums[i], nums[i])
            
            maxSubproduct = max(maxSubproduct, biggestSoFar)
            
        return maxSubproduct
    