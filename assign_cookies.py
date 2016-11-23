# Problem: Assign Cookies
# (https://leetcode.com/problems/assign-cookies/)

# TODO: REDO EXPLANATION

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

# ci - 2 == gi (this cookie could satisfy even more matches! too good
# for it?)
# ...until...
# assign largest ci to a greed gi -- assign the best cookie possible
# to this greed?

# Alright, so now we figured out that some cookies have more "potential"
# or use than others. 

# However, consider the case where we have a cookie cj
# and a greed gi < gj == cj.

# Now should we assign cj to gj or gi? 
# In any case, we are still ending up with one match.
# Therefore, all we should consider is if there is another cookie
# ci that could satisfy gi. If there is, we could have 2 matches.
# If there isn't, then it doesn't matter if we assign cj to it.

# Ok, so let's say we're at some gi.
# If there is ci == gi, then we should assign ci to gi since
# this is the most optimal cookie (best used here, since can't match higher
# and not wasted to match lower).
# If there is not ci == gi, we check ci+1.
# If gi+1 exists, it doesn't make a difference if we match it with ci+1
# since we are creating one match in either case.
# If gi+1 doesn't exist, then this cookie must match downwards, and this
# cookie would be symmetrical candidates as any of the smaller cookies,
# creating a match.

# OPTIMAL SOLUTION:
# Assuming k cookies
# Assuming n kids/greed
# Create a hashmap of (ci, num(ci)) for O(1) lookup (O(k))
# for each children/greed O(n):
#   all cookies assigned? stop. (keep a counter for optimized termination)
#   find any match, starting from the optimal to the largest O(k/2) (on average half the cookies will be bigger)


# ANALYSIS:
# O(nk)



class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g) == 0 or len(s) == 0:
            return 0
        g.sort()
        s.sort()
        cookiePointer = 0
        matches = 0
        for greed in g:
            if cookiePointer == len(s):
                return matches
            while s[cookiePointer] < greed:
                cookiePointer += 1
                if cookiePointer == len(s):
                    return matches
            cookiePointer += 1
            matches += 1
        return matches
    