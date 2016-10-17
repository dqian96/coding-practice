# Problem: Add Strings
# (https://leetcode.com/problems/add-strings/)

# NOTES:
# Given STRING NON-NEGATIVE integers, num1 and num2
# return INTEGER num1 + num2


# FORMALIZE:
# Input: num1 : string, num2: string
# Output: num1 + num2 : integer

# CATEGORIZE:
# string manipulation, string-to-int conversion

# METHODS:
# 1. convert both num1 and num2 to integers by repeated modulation?
# FAILS due to integer overflow i.e. num1 cannot be computationally
# represented as int.
# 2. Convert matching digits (LSD to MSD) of num1 and num2, at a time, sum,
# and store their result in an array/string. We are essentially
# behaving like an adder. Convert the result as a string after.

# OPTIMAL SOLUTION:
# Have a while loop that iterates both num1 and num2 from LSD to MSD
# at the same time, 'adding' each corresponding digits. Append
# partial sums to resultant string as needed. Note that string appending
# is quadratic.

# ANALYSIS:
# Let n = maxLen(num1, num2). Assuming string appending is n,
# this is O(n).


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index = 0
        carry = 0
        res = ""
        while (index < max(len(num1), len(num2))):
            if ((index >= len(num1)) or (index >= len(num2))):
                if index >= len(num1):
                    int2 = ord(num2[len(num2) -1 - index]) - ord('0')
                    int1 = 0
                else:
                    int1 = ord(num1[len(num1) -1 - index]) - ord('0')
                    int2 = 0
            else:
                int1 = ord(num1[len(num1) -1 - index]) - ord('0')
                int2 = ord(num2[len(num2) -1 - index]) - ord('0')
            intSum = int1 + int2 + carry
            carry = 1 if intSum > 9 else 0
            digit = intSum % 10
            charDigit = chr(digit + ord('0'))
            res = charDigit + res
            index += 1
        if carry == 1:
            res = "1" + res
        return res
