# Problem: Subarray Sum Equals K
# (https://leetcode.com/problems/subarray-sum-equals-k/#/description)

# This can be done in O(n) by reducing it to the Two Sum question

class Solution(object):
    def subarraySum(self, nums, k):
        sumsFromStart = {}
        sum = 0
        sumsFromStart[0] = [-1]
        for i in range(len(nums)):
            sum += nums[i]
            if sum in sumsFromStart:
                sumsFromStart[sum].append(i)
            else:
                sumsFromStart[sum] = [i]
        sum = 0
        numsContinuousArrays = 0
        for i in range(len(nums)):
            sum += nums[i]
            difference = sum - k
            if difference in sumsFromStart:
                for j in sumsFromStart[difference]:
                    if j < i:
                        numsContinuousArrays += 1
        return numsContinuousArrays