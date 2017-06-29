# Problem: Guess Number Higher or Lower
# (https://leetcode.com/problems/guess-number-higher-or-lower/#/description)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        inclusiveStart, exclusiveEnd, g, candidate = 1, n + 1, -1, -1
        while g != 0:
            candidate = (inclusiveStart + exclusiveEnd)/2
            g = guess(candidate)
            if g < 0:
                exclusiveEnd = candidate
            elif g > 0:
                inclusiveStart = candidate + 1
        return candidate
