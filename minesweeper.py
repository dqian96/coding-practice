# Problem: Minesweeper
# (https://leetcode.com/problems/minesweeper/#/description)

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'E':
            if self.numAdjacentBombs(click, board) == '0':
                # recursively reveal all
                board[click[0]][click[1]] = 'B'
                for i in range(click[0] - 1, click[0] + 2):
                    for j in range(click[1] - 1, click[1] + 2):
                        if i > -1 and i < len(board) and j > -1 and j < len(board[0]):
                            self.updateBoard(board, [i, j])
            else:
                # reveal digit
                board[click[0]][click[1]] = self.numAdjacentBombs(click, board)
        elif board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        # do nothing on B or digit
        return board

    def numAdjacentBombs(self, loc, board):
        numAdjacentBombs = 0
        for i in range(loc[0] - 1, loc[0] + 2):
            for j in range(loc[1] - 1, loc[1] + 2):
                if i > -1 and i < len(board) and j > -1 and j < len(board[0]):
                    if board[i][j] == 'M' or board[i][j] == 'X':
                        numAdjacentBombs += 1
        return str(numAdjacentBombs)