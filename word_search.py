# Problem: Word Search
# (https://leetcode.com/problems/word-search/description/)

class Solution(object):
    def backtrack(self, board, row, col, used, target, curr):
        if curr == len(target):
            # found word
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            # out of range - not a possible soln
            return False
        if (row, col) in used:
            # already used letter
            return False

        if (board[row][col] == target[curr]):
            used.add((row, col))        # add to used
            down = self.backtrack(board, row + 1, col, used, target, curr + 1)
            up = self.backtrack(board, row - 1, col, used, target, curr + 1)
            left = self.backtrack(board, row, col - 1, used, target, curr + 1)
            right = self.backtrack(board, row, col + 1, used, target, curr + 1)

            validSoln = down or up or left or right         # valid soln
            if validSoln:
                return True
            used.remove((row, col))     # not used anymore

        return False            # curr pos not matching or all future moves invalid

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                s = set()
                if self.backtrack(board, i, j, s, word, 0):
                    return True
        return False

