# Problem: ZigZag Conversion
# (https://leetcode.com/problems/zigzag-conversion/)

# This question is all about finding patterns.
# We are given a string s. For example, let's say that
# s = PAYPALISHIRING.
# When is written in zigzag pattern with 4 rows, we have
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# We then read in the zigzag pattern, left to right,
# up to down and have the following
# z(s, 4) = PINALSIGYAHRPI
# The problem is to output z(s, n) given s and n.

# The best approah to these kinds of questions, with 
# a less rigorous input-output relationship
# is to write down a few examples and try to find patterns.

# After writing out some examples, we see that
# The verticals always contain n, and the diagonals
# contain n - 2. 
# Upon converting the characters to indices,
# we see that the top and bottom characters/indies
# are always multiples of n - 1.
# We see that the topmost chars are even multiples of n - 1.
# i.e. floor(i/(n - 1)) is even
# The bottommost chars are odd multiples of n - 1.
# So, we can state that even multiples of n - 1 go down
# and odd multiples go up. If there were some way to
# specifically descibe what row these numbers belong to, then
# we can use pattern finding and math to determine which 
# row each number would be as we iterate through the string.
# We know that the topmost index always goes to row 0, and
# coincendentally modding the topmost index by n - 1 always
# produces 0 since it's a multiple of n - 1. The ones that
# follow it increments, so that if we mod it by n - 1 we get
# the proper row as it grows incrementally.
# Therefore, if we have an index i that is an even multiple
# of n - 1, then the row = i mod (n - 1)
# Coincedentally, going up is the same thing but reversed.
# since the row is decrementing but by the same pattern.
# SO, if we the index i is an odd multiple of n - 1,
# then the row is row = numRows - (i mod (n - 1))


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [""]*numRows
        for i in range(0, len(s)):
            if (i/(numRows - 1)) % 2 == 0:
                rows[i % (numRows - 1)] += s[i]
            else:
                rows[numRows - 1 - (i % (numRows - 1))] += s[i]
        return "".join(rows)
        