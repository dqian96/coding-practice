# Problem: ZigZag Conversion
# (https://leetcode.com/problems/zigzag-conversion/)

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
        