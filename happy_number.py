# Problem: Happy Number
# (https://leetcode.com/problems/happy-number/)

# To determine the sum of the square of the digits, keep on modding n by 10 to get the LSD.
# Then, divide n by 10 to shift the number to the right (rounding down is automatic to get rid of decimal).
# Continue until n == 0.

# Use a hash table to keep track of historic values. When arrive at a past value, we know there
# exists an infinite cycle.

class Solution(object):
    def getDigitSum(self, n):
        digitSum = 0
        while n != 0:
            digit = n % 10
            digitSum += digit**2
            n = n/10
        return digitSum
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = {}
        while (n not in history):
            history[n] = 1
            n = self.getDigitSum(n)
            if (n == 1):
                return True
        return False