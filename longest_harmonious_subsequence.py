# Problem: Longest Harmonious Subsequence
# (https://leetcode.com/problems/longest-harmonious-subsequence/#/description)

from collections import defaultdict

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numPastOccurences = defaultdict(int)
        for num in nums:
            numPastOccurences[num] += 1
        lhs = 0
        for num, occurences in numPastOccurences.iteritems():
            lhs = max(lhs, 0 if (num + 1) not in numPastOccurences else (occurences + numPastOccurences[num + 1]))
        return lhs
