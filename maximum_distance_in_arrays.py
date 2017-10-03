# Problem: Maximum Distance In Arrays
# (https://leetcode.com/problems/maximum-distance-in-arrays/description/)

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        smallest = float("inf")
        largest = float("-inf")
        largestDist = -float("inf")
        for a in arrays:
            if len(a) == 0:
                continue
            if smallest == float("inf"):
                smallest = a[0]
                largest = a[-1]
                continue
            largestDist = max(largestDist, max(abs(a[-1] - smallest), abs(largest - a[0])))
            smallest = min(smallest, a[0])
            largest = max(largest, a[-1])
        
        return largestDist
            