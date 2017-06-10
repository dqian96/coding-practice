# Problem: Two Sum II - Input array is sorted
# (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description)

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p0 = 0
        p1 = len(numbers) - 1
        while True:
            val = numbers[p0] + numbers[p1]
            if val == target:
                return [p0 + 1, p1 + 1]
            if val < target:
                p0 += 1
            else:
                p1 -= 1
                