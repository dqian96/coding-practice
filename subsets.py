# Problem: Subsets
# (https://leetcode.com/problems/subsets/description/)

class Solution(object):
    def reduceAndConquer(self, n, nums):
        if n == 1:
            return [[nums[0]], []]
        
        lesserSubsets = self.reduceAndConquer(n - 1, nums)
        
        numLesserSubsets = len(lesserSubsets)
        for i in range(numLesserSubsets):
            lesserSubsets.append(lesserSubsets[i][:])
            lesserSubsets[-1].append(nums[n - 1])
        
        return lesserSubsets
        
    def subsets(self, nums):
        return self.reduceAndConquer(len(nums), nums)
        