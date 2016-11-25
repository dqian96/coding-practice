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
# reasoning, sorting, greedy

# REASONING:

# Ok, let's say we have a greed gi.
# Let's run through our matching options.
# Assume we have cookies ch, ci, and cj, such that
# ch < ci == gi < cj. (cj is any bigger cookie and ch is any smaller cookie)

# ch is impossible since we can't match a lower tiered cookie to a higher
# greed.

# We can match gi with ci or cj.

# 1. If both ci and cj exist:

# If we choose to match gi with cj. We create (cj, gi)
# for a confirmed +1 match.

# If we choose (ci, gi), then we could potentially use cj
# to match a bigger greed gj (potential (cj, gj), and we have
# have potentially +2 matches.

# Thus, (ci, gi) is the better match if both ci and cj exist.

# 2. If only ci exists, then (ci, gi) obviously.

# 3. If ci doesn't exist, then we could (cj, gi)
# producing a confirmed +1 match or we could match cj with a 
# potentially existing gj producing a potential +1 match.
# Clearly (cj, gi) is the better match.

# However, cj should be the next biggest cookie after ci to optimize
# the outcome.

# If cj was a bigger cookie but not the next (let's say cm is)
# then matching cj to gi is not optimal.

# Matching cj to gi: potentially +2
# (cj, gi), possibly (cm, gm)

# Matching cm to gi: confirmed +2
# (cm, gi), (cj, gm) 

# So, if ci doesn't exist, the best option is to match gi with
# the next biggest cookie cj.


# So, from the reasoning above, we can see that
# If ci exists, match gi with ci.
# If ci doesn't exist, match gi with cj (the next biggest cookie after ci).
# In short, this sums to: the order of preference to match gi
# is ci, ci+1, ci+2,.
# The best option is the smallest viable that exists.

# OPTIMAL SOLUTION:
# We can go through g and find ci == gi and then, if necessary, ci, ci+1, ci+2...
# Thus, we must find ci, ci+1,... in order and so this means
# that s should be sorted so we can iterate ci+1, ci+2,...easily
# since they are sequential to ci. Otherwisem we don't know if ci+1 exists
# and must check all possibilities until we reach the next biggest cookie.

# However, if we store it as an array, we will have difficulty
# finding if ci exists in s (must iterate to find starting point).
# However, if we sort g, then since every next gj is bigger than
# gi, we just continue checking from the next unmatched cookie in s
# since we know all smaller cookies are too small/already matched
# so they cannot be valid candidates for gj. 
# Thus, we can search for cj, cj+1,... etc. from (exclusive) the last
# matched ci, since ci is matched and all smaller cookies are already matched/
# too small for gi and gj >= gi and so those previous cookies cannot work.


# We sort both g and s.
# Find the first acceptable match for g0 (first acceptable is
# the best match since it would be the smallest viable since s
# is sorted i.e. c0, c1,...). Record this position ci.
# g1 >= g0  and since none of the cookies smaller than ci worked
# for g0, they won't work for g1 either. ci is already taken.
# Start the search for the next viable option after ci.
# Repeat and so on until we reach the end of s, in which
# case no more cookeis may match the >= greeds.

# ANALYSIS:
# Assume n = max(len(g), len(s))
# O(log(n) + n)
# O(n)


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
    