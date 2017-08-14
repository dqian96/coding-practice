# Problem: Find All Duplicates in an Array
# (https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)

class Solution(object):
    def findDuplicates(self, nums):
        i = 0
        res = []
        while i != len(nums):
            if nums[i] == -1 or i == nums[i] - 1:
                i += 1
                continue
            temp = nums[nums[i] - 1]
            if temp == nums[i]:
                nums[nums[i] - 1] = -1
                nums[i] = -1
                res.append(temp)
                continue
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp
        return res
