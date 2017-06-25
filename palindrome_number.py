# Problem: Palindrome Number
# (https://leetcode.com/problems/palindrome-number/#/description)

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        norm, rev = x, 0
        while x != 0:
            rev = rev*10 + x%10
            x /= 10
        return rev == norm

# from math import log

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0: return False
#         zeroesRemoved = 0
#         while x >= 10:
#             if zeroesRemoved == 0:
#                 numDigitsSub1 = int(log(x, 10))
#                 msd = x / (10 ** numDigitsSub1)
#                 x -= msd * (10 ** numDigitsSub1)
#                 if x >= 10: zeroesRemoved = numDigitsSub1 - int(log(x, 10)) - 1
#             else:
#                 msd = 0
#                 zeroesRemoved -= 1
#             lsd = x % 10
#             x /= 10
#             if msd != lsd: return False
#         return True if zeroesRemoved == 0 else False
