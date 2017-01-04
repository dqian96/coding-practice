# Problem: Find all numbers disappeared in an array
# (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

# We are given an array of size n. This array is expected to contain
# integers [1, n], however it does not. Some numbers occur only once
# (as expected), but some numbers appear twice. The numbers that appear
# twice take up the "spot" for another number, which does not appear.
# Thus, find the numbers in [1,n] that do not appear in the array.

# We can do this in O(n) using no extra space.
# There are several things we need to make note of.
# We cannot use mathematical approaches i.e. summation since
# we cannot disambiguate which number is missing since multiple numbers
# maybe missing.
# We need to somehow track what numbers have already appeared since it
# will be ambiguous otherwise.
# But we are not allowed extra sapce...
# However, we can use the array given to us.
# However, if we were to track information as we iterate through nums
# using nums, we might overwrite info we still need.
# nums itself is simply an array, how can we record enough information
# (i.e. no tuples)?

# Well, we do have INDICES in arrays. Notice how the indicies of array
# 0 to n-1 can be mapped to 1 to n, the numbers that we are supposed
# to be able to find in the array.

# In addition, we can still write information to the array without
# losing existing information by using negatives.
# Suppose nums[i] = -nums[i], then we still know what number
# belonged in that spot as well as know that nums[i] has been altered.

# So basically, the algorithm is:
# For each num in nums, record that we have "seen" num by
# setting nums[num - 1] to negative nums[num - 1]...That is,
# if a value at an index is negative, then we know that
# the number index + 1 has already been seen. We use indices and
# negatives to specify whether a number between 1 - n has been seen.
# This doesn't overwrite existing data, as if we get to a negative number,
# we can simply abs it to fetch the original data the array contained
# and proceed accordingly.

# We then iterate through the array looking for positive numbers,
# which implies the number index + 1 has never been seen, and that
# index + 1 is missing from the array.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(0, len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        return [i + 1 for i in range(0, len(nums)) if nums[i] > 0]

# Another solution with the idea of repeated swapping until
# all numbers are in the correct place or the best avaliable position.

# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(0, len(nums)):
#             while nums[i] != i + 1:
#                 temp = nums[i]
#                 nums[i] = nums[temp - 1]
#                 nums[temp - 1] = temp
#         res = []
#         for i in range(0, len(nums)):
#             if nums[i] != i + 1:
#                 res.append(i + 1)
#         return res
#         