# Problem: Remove Element
# (https://leetcode.com/problems/remove-element/)

# Given an array nums = n0,n1,n2,n3,...,nk-1
# Remove all ni if ni == val
# Or rather, move all ni == val to the back of the array
# such that ni,ni+1,ni+2,...,nk-1 == val
# and n0,n1,..,ni-1 != val

# We will use a two pointer approach. 
# Pointer 1 starts from the left, and pointer 2 from the right.
# We keep the following invariant:
# All ni strictly before pointer 1 != val.
# All ni strictly after pointer 2 == val.

# If we keep the invariant, then as soon as p1 > p2,
# we know that all values before p1 != val, and all
# values from p1 and onwards == val, so we return p1.
# This means that the array is "sorted". We return p1 as
# the num of elements != val.

# To do this, we advance p1 is it != val and decrement p2
# if it is val, i.e. both values are "correct."

# In the case where, p1 == val and p2 != val, we swap and
# then increment/decrement respectively as the invariant
# is still true,

# This goes on until we get to the middle. The following cases are:
# p1 == p2 == val, in which case p2 would decrease and end the loop
# which the correct invariant (before good, after good)

# Swap. obvious.

# p1 != val, p2 != val. Increment p1 till after p2. Loop ends.
# proper invariant.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:
            if nums[p1] == val and nums[p2] != val:
                nums[p1] = nums[p2]
                nums[p2] = val
                p1 += 1
                p2 -= 1
            else:
                if nums[p1] != val:
                    p1 += 1
                if nums[p2] == val:
                    p2 -= 1
        return p1