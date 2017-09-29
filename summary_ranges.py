# Problem: Summary Ranges
# (https://leetcode.com/problems/summary-ranges/description/)

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        rangeStartIndex = 0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if rangeStartIndex == i - 1:
                    ranges.append(str(nums[rangeStartIndex]))
                else:
                    ranges.append(str(nums[rangeStartIndex]) + "->" + str(nums[i - 1]))
                rangeStartIndex = i
        return ranges
