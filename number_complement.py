# Problem: Number Complement
# (https://leetcode.com/problems/number-complement/)

# Let num be n bits.
# To invert every bit of num, all we have to do is apply bitwise
# XOR of 111...111 to num since:
# 1 XOR 1 -> 0
# 0 XOR 1 -> 1
# It inverts every bit

# Now, all we have to do is find what number 111....111 (n total bits)
# is.

# This is simple. Let's determine n first.
# floor(log2(num) + 1) will give us n.
# Now, if every bit is 1, then we will have
# 2^floor(log2(num) + 1) configurations, and since it starts at 0,
# the largest number n bits can make is 2^floor(log2(num) + 1) - 1.
# This largest number is also n bits where every bit is 1.

# Simply 2^floor(log2(num) + 1) - 1 XOR num to get the desired result.

# Constant time, no extra space.

class Solution(object):
    def findComplement(self, num):
        import math
        return 2**(int(math.floor(math.log(num, 2) + 1))) - 1 ^ num
