# Problem: Set MisMatch
# (https://leetcode.com/problems/set-mismatch/description/)

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sum(nums)
        i = 0
        while i != len(nums):
            if nums[i] != i + 1:
                t = nums[i] - 1
                if t + 1 == nums[t]:
                    dup = t + 1
                    break
                nums[i] = nums[t]
                nums[t] = t + 1
                continue
            i += 1
        n = float(len(nums))
        return [dup, int((n/2)*(n+1) - s + dup)]
        