# Problem: Number of Boomeranges
# (https://leetcode.com/problems/number-of-boomerangs/)

# NOTES:
# -given n points
# -each point is 2D i.e. (x, y)
# -find how many boomerangs there are?
# -a boomerang is a 3-tuple of points (i, j, k)
# -such that |i-j| == |i-k|, i.e. k is the same distance from i as j
# -ORDER matters i.e. capture PERMUTATIONS not combinations
# -we do not need to output the boomerang 3-tuples, just the number!!!

# CATEGORIZE:
# search - trying to find (i, j, k) in array A
# hash table - keep track of relevant information as we iterate the array

# REASONING:
# We have to look through every point at least once. There's no way to infer whether or
# not points not looked are part of a boomerang or not. Thus, O(n) at the least.
# The naive solution is O(n^3).
# The ideal solution probably is O(n) or O(n^2).

# Notice that j and k are symmetric...i..e if (i, j, k) is a boomerang than so is
# (i, k, j). This not true for i, which cannot be swapped with the other points
# and maintain a boomerang.

# Since the boomerang property is defined by the distance between j and k to i,
# we need to fix/pin some i and find j and k that satisfy the boomerang property.
# In other words, since a boomerang is defined by the relationship between some i
# and any other two points, we fix some i and search for the satisfying points.

# Therefore, we do a loop and fix each element in points as i.
# For each iteration of the loop, we have a fixed i.
# We must now search for j and k.
# j and k are defined by their distance to i. Therefore, any point with the same distance
# to i can be put in a set as potential candidates for j and k.
# So, we create a hash table mapping distance to number of points that are at those distance.
# j and k pairs must be both chosen from that set, at such distance (difference j and k
# contexts for difference distance).
# So, we do an iteration through points and fill our hashtable, ending up with
# knowing the number of points at particular distances.

# Now, how many ways can we pick j and k pairs from each distance set. Assuming each distance
# set has m points, there are exactly m*(m-1) ways to pick j and k pairs (ordered) from set.
# Iterate through the distance sets (which at most is n, since worst case is each point
# is its own distance), and add the number of j/k pairs to a global counter.

# We are done.

# ANALYSIS:
# O(n(n+worstcase(n)))
# O(n^2)


class Solution(object):
    def numberOfBoomerangs(self, points):
        import math
        numBoomerangs = 0
        for r in range(0, len(points)):
            distToNumPoints = {}
            for s in range(0, len(points)):
                if r == s:
                    continue
                distance = math.sqrt((points[r][0] - points[s][0])**2 + (points[r][1] - points[s][1])**2)
                if distance in distToNumPoints:
                    distToNumPoints[distance] += 1
                else:
                    distToNumPoints[distance] = 1
            for key in distToNumPoints:
                numBoomerangs += distToNumPoints[key]*(distToNumPoints[key]-1)
        return numBoomerangs
