# Problem: House Robber
# (https://leetcode.com/problems/house-robber/)

# Let H = [(h0, m0), (h1, m1), (h2, m2),...,(hn-1, mn-1)]
# be the ORDERED list of (house, money) pairs on the street.

# The goal of this is to pick a proper subset of H such that
# the sum of the money is the max of any possible subset.

# Problem formalization:

# In other words, let K be a proper subset of H and let P be any subset of H
# such that for any (x,y) in K (or P), there is no (a,b) that is adjacent in
# the list and sum(k[1]) >= sum(p[1]) for all k E K and p E P.

# Solution:
# Consider an ordered set of n houses H = {h0, h1, h2,..., hn-1}
# Let S(H) be the set of optimal houses to rob.
# Now consider H + hn = h0, h1, h2,...,hn-1, hn
# S(H + hn) either contains hn o


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.robDecomposition(nums)[0]

    def robDecomposition(self, nums):
        if len(nums) == 1:
            return (nums[0], 1)
        elif len(nums) == 2:
            if nums[1] >= nums[0]:
                return (nums[1], 1)
            else:
                return (nums[0], 0)
        a = self.robDecomposition(nums[0:-1])
        if a[1] == 0:
            return (a[0] + nums[-1], 1)
        else:
            return a[0]
