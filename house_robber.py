# Problem: House Robber
# (https://leetcode.com/problems/house-robber/)

class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        maxValueAtHouse = []
        for i in range(0, len(nums)):
            if i == 0:
                maxValueAtHouse.append(nums[i])
            elif i == 1:
                maxValueAtHouse.append(max(nums[i], maxValueAtHouse[-1]))
            else:
                maxValueAtHouse.append(max(nums[i] + maxValueAtHouse[-2], maxValueAtHouse[-1]))
        return maxValueAtHouse[-1]
        