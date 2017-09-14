# Problem: Reverse Bits
# (https://leetcode.com/problems/reverse-bits/description/)

# Use AND to get each bit of n.
# Shift the bit by an appropriate number of times and accumulate it.

import math

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        reverseN = 0

        for i in range(32):
            bi = n & (2 ** i)
            if i < 16:
                reverseN += (bi << ((31 - i) - i))
            elif i >= 16:
                reverseN += (bi >> (i - (31 - i)))

        return reverseN
    