# Problem: Max Consecutive Ones
# (https://leetcode.com/submissions/detail/104680938/)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxStreak = 0
        currentStreak = 0
        for bit in nums:
            if bit == 1:
                currentStreak += 1
            else:
                maxStreak = max(maxStreak, currentStreak)
                currentStreak = 0
        maxStreak = max(maxStreak, currentStreak)
        return maxStreak
        