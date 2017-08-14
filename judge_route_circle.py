# Problem: Judge Route Circle
# (https://leetcode.com/problems/judge-route-circle/description/)

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        currLocation = [0, 0]
        for move in moves:
            if move == 'U':
                currLocation[1] -= 1
            elif move == 'D':
                currLocation[1] += 1
            elif move == 'L':
                currLocation[0] -= 1
            else:
                currLocation[0] += 1
        return True if currLocation == [0, 0] else False
