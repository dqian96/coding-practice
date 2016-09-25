# Problem: Plus One
# (https://leetcode.com/problems/plus-one/)


# Assume we are given num = dn-1dn-2dn-3...d2d1d0
# Then, num + 1 is simply calculated by adding 1 to d0.
# If there exists a carry, then d0 = 9 must be true as the
# rest of the numbers will not result in a carry.
# Since d0 = 9, the "new" d0 in num + 1 must be a 0,
# since 9 + 1 = 10 is the only carry case.
# Then, this is simply a case of dn-1dn-2dn-3...d2d1 + 1
# The only case where dn-1 + 1 will have a carry is if
# all the digits are 9, because if they are not,
# the carry would have "died out" before. 
# In other words, the only case where we would have an
# increase in the amount of digits in num + 1 is if
# num = 999...999, in which case we just have to make dn-1 = 1
# and add a 0 after the last digit...

# Originally, I thought that if we had an "overflow" or
# a carry for the first digit, we would to add an element
# to the start of the array. Of course, adding to the
# start of an array is O(n). This can be clearly avoided
# if we note that we are simply adding a ONE to the number.
# The only overflow case is 999...999 and we can just make
# the first digit 1 and push back a 0.

# Picking up every detail of the question super important.
# EVERY DETAIL.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            # carry
            if digits[i] == 9:
                if i == 0:
                    digits[0] = 1
                    digits.append(0)
                    return digits
                else:
                    digits[i] = 0
            else:
                digits[i] += 1
                return digits