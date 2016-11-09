# Problem: Arranging Coins
# (https://leetcode.com/problems/arranging-coins/)

# NOTES:
# given n coints, form a stairwell/right triangle
# a complete row is defined as a row of the stairwell that is completely filled
# what is the max # of complete rows that can be formed?

# FORMALIZE:
# First, we determine what stairswells we can form with n coins that contain
# the maximum # of complete rows.
# There are two stairwells that are interesting:
# The smallest incomplete stairwell
# The largest complete stair well

# If we compare the largest complete stairwell with all smaller stairwells,
# we see that all of them are complete, but the largest complete stairwell
# has more complete rows.

# If we compare the smallest incomplete stairwell with all larger stairwells
# we see that even less rows will be filled for larger stairwells, so this
# is a better choice.

# Thus, the only possible answers are either the smallest incomplete stairwell
# or the largest complete stairwell. The stairwells are sequential to each other.
# Now, the smallest incomplete stairwell is simply the largest complete
# stairwell with an extra incomplete row...going by the arangement of coins
# that will lead to the maximum number of rows filled, that is fill
# the smallest rows first, then largest.

# So, we confirm that largest complete stairwell has the most complete
# rows possible.

# Assume this stairwell has a longest row of k coins.
# Then, this stairwell has k + (k - 1) + (k - 2) + ...+ 1 coins.
# Given n coins, k must be:
# k + (k - 1) + (k - 2) + ...+ 1 = n
# Solve using quadratic formula...this will yield the optimal k, which may
# not be whole. We must round down for the largest complete stairwell,
# as rounding up will lead to an incomplete stairwell.

# Thus, the largest complete stairwell will have k complete rows.

# CATEGORIZE:
# math, loops (construct stairwell), reasoning, binary search (to solve eqn)

# OPTIMAL SOLUTION:
# take note of implementation wrt floating point values

# ANALYSIS:
# O(1) space and time

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int((-1.0 + math.sqrt(4 + 8 * n))/2)
