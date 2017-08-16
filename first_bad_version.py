# Problem: First Bad Version
# (https://leetcode.com/problems/first-bad-version/description/)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        inclusiveLeft = 1
        exclusiveRight = n + 1
        while exclusiveRight > inclusiveLeft + 1:
            mid = (inclusiveLeft + exclusiveRight)/2
            
            if isBadVersion(mid):
                exclusiveRight = mid
            else:
                inclusiveLeft = mid + 1
        
        return inclusiveLeft if isBadVersion(inclusiveLeft) else exclusiveRight
        