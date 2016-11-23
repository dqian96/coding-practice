# Problem: Assign Cookies
# (https://leetcode.com/problems/assign-cookies/)


# NOTES:
# -set of cookies with size ci
# -set of children with each child have greed factor gi
# -can match a cookie to a child if ci >= gi
# -one cookie can only match to a child, and vice versa
# -find max # of matches

# FORMALIZATION:

# We are given a set of n+1 cookies C = {c0, c1, c2, ..., cn}
# We are given a set of k+1 greed factors G = {g0, g1, g2,..., gk}
# Let f be a injection (1 to 1) function f: C -> G where
# f(ci) = gi => ci >= gi
# Find max # of matchings for f.

# CATEGORIZE:
# matching, math, reasoning

# REASONING:
# The best match is where ci == gi (not potentially wasting a larger
# cookie which could be used on another kid and it is a valid match)

# The second best match is where ci - 1 == gi (not optimal assignment
# of cookie to kid since ci could be used on smaller greed kids)

# ci - 2 == gi (even better cookie, could satisfy more matches)
# ...until...
# assign largest ci to a greed gi.

# The best use of a cookie is the optimal match (ci == gi).
# The second best use is a match where (ci - 1 == gi).
# so on...



# OPTIMAL SOLUTION:

# ANALYSIS:
# O(n)



class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        