# Problem: Valid Sudoku
# (https://leetcode.com/problems/valid-sudoku/description/)

class Solution(object):
    def isValidSudoku(self, board):
        for diag in range(9):
            col, row, box = set(), set(), set()
            boxRow, boxCol = diag - (diag % 3), 3 * (diag % 3)
            for i in range(9):
                if board[diag][i] != '.' and board[diag][i] in row: return False
                if board[i][diag] != '.' and board[i][diag] in col: return False
                if board[boxRow + i/3][boxCol + i % 3] != '.' and board[boxRow + i/3][boxCol + i % 3] in box: return False
                box.add(board[boxRow + i/3][boxCol + i % 3])
                row.add(board[diag][i])
                col.add(board[i][diag])
        return True
            