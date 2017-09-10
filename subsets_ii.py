# Problem: Subsets II
# (https://leetcode.com/problems/subsets-ii/description/)

class Solution(object):
    def reduceAndConquer(self, n, nums, numSubsetsIncludeLastElement):
        if n == 1:
            numSubsetsIncludeLastElement[0] = 1
            return [[], [nums[0]]]
        
        lesserSubsets = self.reduceAndConquer(n - 1, nums, numSubsetsIncludeLastElement)
        
        subsetsToSkip = 0 if nums[n - 1] != nums[n - 2] else len(lesserSubsets) - numSubsetsIncludeLastElement[0]
        numSubsetsIncludeLastElement[0] = len(lesserSubsets) - subsetsToSkip

        for i in range(subsetsToSkip, len(lesserSubsets)):
            lesserSubsets.append(lesserSubsets[i][:])
            lesserSubsets[-1].append(nums[n - 1])
        return lesserSubsets
        
    def subsetsWithDup(self, nums):
        nums.sort()
        return self.reduceAndConquer(len(nums), nums, [0])
    