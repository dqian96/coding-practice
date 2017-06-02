# Problem: Array Partition
# (https://leetcode.com/problems/array-partition-i/#/description)

# Question is to make pairs such that the sum of the min of each pair is the max.
# Since this is a maximizing question, we obviously want the biggest element.
# However, it is never them min of a pair. The next best alternative is to take
# the second max element, and we can use the max element so that it is the
# min (we can take). Reason inductively.

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([val for index, val in enumerate(nums) if index % 2 == 0])
