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
        
        res = "sd"
        
