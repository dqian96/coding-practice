# Problem: Maximal Square
# (https://leetcode.com/problems/maximal-square/description/)

class Solution(object):
    def maximalSquare(self, matrix):
        T = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        m = 0
        for r in range(len(T) - 1, -1, -1):
            for c in range(len(T[0]) - 1, -1, -1):
                if matrix[r][c] == '0':
                    continue
                innerSquareLength = 0 if r + 1 >= len(matrix) or c + 1 >= len(matrix[0]) else T[r + 1][c + 1]
                top = 0 if r + 1 >= len(matrix) else T[r + 1][c]
                bot = 0 if c + 1 >= len(matrix[0]) else T[r][c + 1]
                T[r][c] = 1 +  min(min(top, bot), innerSquareLength)
                m = max(m, T[r][c])
        return m ** 2
    