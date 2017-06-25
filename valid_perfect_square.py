# Problem: Valid Perfect Square
# (https://leetcode.com/problems/valid-perfect-square/#/description)


# O(logn)

from math import sqrt

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 or num == 4: return True
        candidate = 0
        inclusiveStart = 1
        exclusiveEnd = num/2
        while inclusiveStart < exclusiveEnd:
            candidate = int(float(inclusiveStart/2) + float(exclusiveEnd/2))
            if candidate**2 == num: return True
            if candidate**2 < num: inclusiveStart = candidate + 1
            if candidate**2 > num: exclusiveEnd = candidate
        return False
        
# O(sqrt(n))

# class Solution(object):
#     def isPerfectSquare(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         square = 1
#         while square**2 <= num:
#             if num % square == 0 and square**2 == num: return True
#             square += 1
#         return False
        
