# Problem: Search a 2D Matrix II
# (https://leetcode.com/problems/search-a-2d-matrix-ii/)

# Runtime: O(m + n)

class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        coord = [0, len(matrix) - 1]
        while coord[0] < len(matrix[0]) and coord[1] >= 0:
            if matrix[coord[1]][coord[0]] == target:
                return True
            if matrix[coord[1]][coord[0]] < target:
                coord[0] += 1
            else:
                coord[1] -= 1
        return False
        