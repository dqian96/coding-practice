# Problem: Spiral Matrix
# (https://leetcode.com/problems/spiral-matrix/description/)

"""

You are given any 2D matrix (doesn't have to be a square). You are to print it out
in "spiral" order. That is, you are to print the outermost top, right, bottom, and left layer, then
the second outermost top, right, ... and so on.abs

For example, given:

1,2,3
4,5,6
7,8,9

You are to print 1,2,3,6,9,8,7,4,5

Input:

#rows,#columns
row0[0],row0[1],...
row1[0],row1[1],...
...

The solution is to iterate through every layer of the matrix by checking bounds.
If left <= right bound, then you have layers.
If the layer is 2D, for each layer, print the top, right, bottom, left by simply iterating from bounds.
If the layer is 1D, then just print the horizontal/vertix vertex.

"""

# import sys

# def read_input():
#     # build matrix
#     sys.stdin.readline()        # discard first line
#     matrix = []
#     for line in sys.stdin:
#         matrix.append(line.strip('\n').split(','))      # new row
#     return matrix

# def get_layer(matrix, spiral, min_x, max_x, min_y, max_y):
#     # get values for each "spiral" or "layer" of matrix
#     if min_y == max_y:
#         # 1D, horizontal
#         spiral += matrix[max_y][min_x:max_x + 1]
#         return
#     if min_x == max_x:
#         # 1D, vertical
#         spiral += [a[max_x] for a in matrix[min_y:max_y + 1]]
#         return

#     # not 1D, it's 2D => 4 sides
#     spiral += matrix[min_y][min_x:max_x]                        # top side
#     spiral += [a[max_x] for a in matrix[min_y:max_y]]           # right side
#     spiral += matrix[max_y][max_x:min_x:-1]                     # bottom side
#     spiral += [a[min_x] for a in matrix[max_y:min_y:-1]]        # left side

# def main():
#     matrix = read_input()
#     rows = len(matrix)
#     columns = len(matrix[0])

#     spiral = []
#     min_x = 0
#     max_x = columns - 1
#     min_y = 0
#     max_y = rows - 1
#     while min_x <= max_x and min_y <= max_y:
#         # iterate through each spiral
#         get_layer(matrix, spiral, min_x, max_x, min_y, max_y)
#         min_x += 1
#         max_x -= 1
#         min_y += 1
#         max_y -= 1

#     print(','.join(spiral))

# main()


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        layer = 0
        while len(res) < rows * cols:
            r = layer
            for c in range(layer, cols - layer):
                res.append(matrix[r][c])

            c = cols - 1 - layer
            for r in range(layer + 1, rows - layer):
                res.append(matrix[r][c])

            if rows - 1 - layer == layer:
                continue
            r = rows - 1 - layer
            for c in range(cols - 2 - layer, layer, -1):
                res.append(matrix[r][c])

            if cols - 1 - layer == layer:
                continue
            c = layer
            for r in range(rows - 1 - layer, layer, -1):
                res.append(matrix[r][c])

            layer += 1

        return res
