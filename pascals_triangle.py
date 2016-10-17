# Problem: Pascal's TriangleANAL
# (https://leetcode.com/problems/pascals-triangle/)


# NOTES:
# Given n, generate the 0th to n - 1 th row of the Pascal's Triangle.


# FORMALIZE:
# Pascal's Triangle has the following properties:
# -the ith row has i + 1 elements.
# -the first element (0) is always a 1
# -the last element, (i) is always a 1
# -any element k in the row is the sum of its direct parents

# CATEGORIZE:
# array, index calculation

# NAIVE SOLUTION? ANALYSIS?

# OPTIMAL SOLUTION:
# Using math might be easier, but the factorial function !
# will be extremely slow for bigger functions.
# Form each row of the tree from the 0th row to the n - 1 th row.
# We know the size of the row, as formalized above.
# We build the array/row by appending on at a time.
# i.e. append a 1 if appending first element, and a 1 if appending
# ith element.
# By going through examples, we see that every consecutive pair of
# element produce a child on the level below.
# For example, e0e1e2e3,...,ei, produces a sum for e0 and e1, e1, e2
# and so on. We can track of a moving window of size 2 to generate
# the proper elements on the level below.

# ANALYSIS:
# To generate a pascal's triangle with n rows, we have
# #elements = 1 + 2 + 3 + ... + n
# In other words, this is O(n^2)

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        res.append([1])

        while len(res) < numRows:
            row = [1]
            res.append(row)
            rowSize = len(res)
            windowSliderIndex = 0
            for i in range(1, rowSize - 1):
                element = res[len(res) - 2][windowSliderIndex] + \
                    res[len(res) - 2][windowSliderIndex + 1]
                res[-1].append(element)
                windowSliderIndex += 1
            res[-1].append(1)
        return res
