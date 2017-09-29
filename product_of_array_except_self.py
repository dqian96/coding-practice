# Problem: Product of Array Except Self
# (https://leetcode.com/problems/product-of-array-except-self/description/)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftToRightProducts = [nums[0]]
        rightToleftProducts = [nums[-1]]
        for i in range(1, len(nums)):
            leftToRightProducts.append(leftToRightProducts[-1] * nums[i])
            rightToleftProducts.append(rightToleftProducts[-1] * nums[len(nums) - 1 - i])
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(rightToleftProducts[len(nums) - 2])
            elif i == len(nums) - 1:
                res.append(leftToRightProducts[len(nums) - 2])
            else:
                res.append(leftToRightProducts[i - 1] * rightToleftProducts[len(nums) - 1 - i - 1])
        return res
    