# Problem: Hamming Distance
# (https://leetcode.com/problems/hamming-distance/)

# Given two numbers, find their hamming distance.
# The hamming distance between 2 numbers x and y is the number
# of respective bits that differ.

# The naive way is to convert both of these numbers to a byte array
# and loop through them looking for differences.

# However, a much more elegant approach can be taken.
# First, we XOR x and y. This will result in a number z such that
# the ith bit of z is 1 if the ith bit of x and y differ, otherwise
# the ith bit of z is 0. Now, all we have to do is count the number
# of 1's in z. Once again, we still do not need a byte array.
# Second, to determine the number of 1's in z, all we have to do is
# check the 0th, 1st, 2nd, ...ith index by ANDing z with another
# number that is 0 at all bits but the ith bit that we want to test.
# The ith bit of this number must be 1. Thus, by ANDing this number
# (let's call it u), z & u will be 0 if the ith bit at z is 0
# or not 0 if the ith bit at z is 1. Thus, we can increase
# the hamming distance counter if z & u != 0.
# Test all the n bit positions of z by checking 2^0 (0th position)
# and all 2^i such that 2^i <= z.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        differentBits = x ^ y
        bitPosition = 0
        hammingDistance = 0
        while 2**bitPosition <= differentBits:
            if 2**bitPosition & differentBits != 0:
                hammingDistance += 1
            bitPosition += 1
        return hammingDistance