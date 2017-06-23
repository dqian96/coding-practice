# Problem: Reverse Integer
# (https://leetcode.com/problems/reverse-integer/#/description)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = abs(x)
        reverse = 0
        while x != 0:
            reverse = reverse * 10 + x % 10
            x /= 10
        return -reverse if isNegative else reverse      
