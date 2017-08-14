# Problem: Single Element in a Sorted Array
# (https://leetcode.com/problems/single-element-in-a-sorted-array/description/)

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binarySearch(0, len(nums), nums)
        
    def binarySearch(self, inclusiveLeft, exclusiveRight, nums):
        if inclusiveLeft == exclusiveRight - 1:
            return nums[inclusiveLeft] 
        mid = (inclusiveLeft + exclusiveRight)/2
        if mid % 2 == 0:
            # even sides
            if nums[mid] == nums[mid + 1]:
                return self.binarySearch(mid, exclusiveRight, nums)
            return self.binarySearch(inclusiveLeft, mid + 1, nums)
        # odd sides
        if nums[mid] == nums[mid - 1]:
            return self.binarySearch(mid + 1, exclusiveRight, nums)
        return self.binarySearch(inclusiveLeft, mid, nums)
        