# Problem: Sum of Square Numbers
# (https://leetcode.com/problems/sum-of-square-numbers/description/)

from math import sqrt

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a**2)
            if b % 1 == 0:
                return True
        return False    
        