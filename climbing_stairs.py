# Problem: https://leetcode.com/problems/climbing-stairs/
# (https://leetcode.com/problems/climbing-stairs/)

# Note: The implementation presented may be optimized even further; it is left
# in the presented state for the sake of clarity and reinforcing the idea
# that it is indeed a RECURRENCE relation.

# There are several ways to go about solving this. We present two solutions.

# Solution 1: Counting the number of compositions of n using parts 1 or 2 using combinatorics (math)
# Given any n, we can counting the number of distinct, ordered ways that n can be composed
# using numbers 1 and 2 only using generating series.
# Consider the generating series for the set {1, 2}, that is the avaliable choices for each part,
# G(x) = x + x^2. This is the number of compositions of n using one part.
# Now, consider the compositions of n using any number of parts:
# G(x) = 1 + (x + x^2) + (x + x^2)^2 + (x + x^2)^3 + ...
# G(x) = 1/(1-x-x^2) = a0 + a1x + a2x^2 + ..., where a0, a1, a2, ... ak are the coefficients
# representing the # of ways where k can be composed.
# (a0 + a1x + a2x^2 + ...)(1-x-x^2) = 1. 
# This gives rise to the initial terms a0 = 1 and a1 =1 and the recurrence relation
# for any n, an = an-1 + an-2. Thus, any n can be composed of an distinct, ordered ways.
# This mathematical recurrence relation is impl as the soln.

# Solution 2: DP
# Consider stairs of "height n". The last step taken can either be
# a 1-step or 2-step.
# In other words, the second last level must be either:
# At level n-1, take 1-step
# At level n-2, take 2-step
# Since the last step must be either 1-step or 2-step (only two possible choices/cases), the
# total number of compositions N(n) can be partitioned into
# N(n) = N(n-1) + N(n-2). We arrive at the same recurrence relation as before.
# To explain this in more layman's terms, we know that the last step must either be a
# 1-step or 2-step. Therefore, to get to n, we can have "get to n-1 and take a 1-step" 
# or "get to n-2 and take a 2-step". There are N(n-1) to get to n-1 and N(n-2) to get
# to n-2, and so, there are N(n-1) + N(n-2) to get to n.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0 or n == 1):
            return 1
        aks1 = 1
        aks2 = 1
        ak = 2
        k = 2
        while k != n:
            aks2 = aks1
            aks1 = ak
            k += 1
            ak = aks1 + aks2
        return ak