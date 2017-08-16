# Problem: Reverse Integer
# (https://leetcode.com/problems/reverse-integer/#/description)

# Problem: Reverse Integer
# (https://leetcode.com/problems/reverse-integer/description/)

# convert to string method
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = True if x < 0 else False
        x = abs(x)
        
        s = list(str(x))
        for i in range(len(s)/2):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
        s = "".join(s)
        x = int(s) * (-1 if isNegative else 1)
        return 0 if x > 2**31 - 1 or x < -2**31 else x

# bitshifts and build number method

# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         cap = 2**31 - 1 if x >= 0 else 2**31
#         x = abs(x)
#         s = 0
#         while x != 0:
#             lastDigit = x % 10
#             x /= 10
#             s *= 10
#             s += lastDigit
#             if s > cap:
#                 return 0
#         return s if cap == 2**31 - 1 else -s