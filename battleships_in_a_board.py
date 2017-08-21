# Problem: Battleships in a Board
# (https://leetcode.com/problems/battleships-in-a-board/description/)

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        counter = 0        
        for row in range(len(board)):
            adjBattleship = False
            for space in range(len(board[0])):
                if board[row][space] == 'X' and not adjBattleship and (row == 0 or board[row-1][space] == '.'):
                    counter += 1
                    adjBattleship = True
                elif board[row][space] == '.':
                    adjBattleship = False
        return counter
                