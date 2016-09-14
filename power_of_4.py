# Problem: Power of 4
# (https://leetcode.com/problems/power-of-four/)

# Any power of 4 is an EVEN power of 2: 4^x = (2*2)^x = (2^x)(2^x) = 2^(2x), x = 0,1,2,...
# Any even power of 2 is a power of 4: 2^(2x) = (2^x)(2^x) = 4^x

# Therefore: x is a power of 4 <=> x is an even power of 2
# In other words, the statements are logically equivalent and ALL powers of 4's will
# be strictly an even power of 2, and all even power of 2's will be a power of 4.
# 100% precision and recall. 

# Therefore, given any 32-bit integer x, we can affirm that it is a power of 4 by
# checking if:
# 1. x is positive
# 2. x is an even power of 2 
#	-> (2147483648 % num == 0 and math.log(num, 2) % 2 == 0) OR
#	-> (2147483648 % math.sqrt(num) == 0) 
#		-> i.e. square rooting any number will only and always produce a power of 2 if it is a power of 4 (even power of 2), and v.v.


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0 and num != 2 and 2147483648 % num == 0 and math.log(num, 2) % 2 == 0:
            return True
        return False
        