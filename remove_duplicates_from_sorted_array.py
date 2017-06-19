# Problem: Remove Duplicates From Sorted Array
# (https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)
        pos, count = 1, 1
        while count < len(nums):
            nums[pos] = nums[count]
            count += 1
            if nums[pos] != nums[pos - 1]: pos += 1
        return pos
        