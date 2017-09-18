# Problem: Sudoku Solver
# (https://leetcode.com/problems/sudoku-solver/description/)

class Solution(object):
    def check_row(self, board, row, num):
        for val in board[row]:
            if val == num:
                return True
        return False

    def check_col(self, board, col, num):
        for row in board:
            if row[col] == num:
                return True
        return False

    def check_subboard(self, board, row, col, num):
        box_row = row - (row % 3)
        box_col = col - (col % 3)

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return True
        return False

    def backtrack(self, board, row, col):
        if col >= 9:
            # exceeded max col
            return self.backtrack(board, row + 1, 0)
        if row >= 9:
            # exceeded max row
            return True
        if board[row][col] != '.':
            # already filled
            return self.backtrack(board, row, col + 1)
        
        for i in range(1, 10):
            if self.check_row(board, row, str(i)) or self.check_col(board, col, str(i)) or self.check_subboard(board, row, col, str(i)):
                continue

            board[row][col] = str(i)

            if self.backtrack(board, row, col + 1):
                # found a valid board
                return True

        board[row][col] = '.'
        return False
    
    def solveSudoku(self, board):
        self.backtrack(board, 0, 0)
