# Problem: Fizz Buzz
# (https://leetcode.com/problems/fizz-buzz/)


# NOTES:

# - given string representation of #'s 1-n
# - multiples of 3, output Fizz
# - multiples of 5, output Buzz
# - multiples of 3 and 5, output FizzBuzz

# FORMALIZE:

# Input: n E Z+
# Output: For all x E {1,..,n},
#         f(x) = "Fizz" <=> x % 3 == 0 && x % 5 != 0
#         f(x) = "Buzz" <=> x % 3 != 0 && x % 5 == 0
#         f(x) = "FizzBuzz" <=> x % 3 == 0 && x % 5 == 0
#         f(x) = str(x) else

# CATEGORIZE:
# numbers, int to string

# OPTIMAL SOLUTION:
# Loop from 1 to n. 4 if statements. Put FizzBuzz condition
# first because FizzBuzz will pass for other cases,
# but other cases will not pass for FizzBuzz. Done.

# ANALYSIS:
# O(n)

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
