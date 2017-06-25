# Problem: Pascal's Traingle II
# (https://leetcode.com/problems/pascals-triangle-ii/#/description)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        while len(row) < rowIndex + 1:
            lastVal = 1
            for i in range(1, len(row)):
                tmp = row[i]
                row[i] += lastVal
                lastVal = tmp
            row.append(1)
        return row
        