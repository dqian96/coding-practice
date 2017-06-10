# Problem: Range addition II
# (https://leetcode.com/problems/range-addition-ii/#/description)

# The element at the origin will be the max element
# Note that the max element is the one that every op increment on
# (and the origin is incremented on each one due to the constraints of the problem)
# In addition, the overlapped element between all the ops will be the max elements
# (and we know it must at least include the origin).
# Find the overlap (continuously shrink region, since it is always a rectangle
# starting at origin, so just take the min of the axis)

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        maxInteger = len(ops)
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m * n