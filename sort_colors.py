# Problem: Sort Colors
# (https://leetcode.com/problems/sort-colors/description/)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numRed = 0
        numWhite = 0
        numBlue = 0
        for color in nums:
            if color == 0:
                numRed += 1
            elif color == 1:
                numWhite += 1
            else:
                numBlue += 1
        
        for i in range(len(nums)):
            if numRed != 0:
                nums[i] = 0
                numRed -= 1
            elif numWhite != 0:
                nums[i] = 1
                numWhite -= 1
            else:
                nums[i] = 2
            