# Problem: Search insert position
# (https://leetcode.com/problems/search-insert-position/#/description)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, 0, len(nums), target)
    
    def binarySearch(self, array, inclusiveStart, exclusiveEnd, target):
        midpoint = (inclusiveStart + exclusiveEnd)/2
        if inclusiveStart >= exclusiveEnd or array[midpoint] == target:
            return midpoint
        if target < array[midpoint]:
            return self.binarySearch(array, inclusiveStart, midpoint, target)
        return self.binarySearch(array, midpoint + 1, exclusiveEnd, target)


