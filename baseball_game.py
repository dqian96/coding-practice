# Problem: Baseball Game
# (https://leetcode.com/problems/baseball-game/description/)

from collections import deque

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = deque()
        total = 0
        for op in ops:
            if op == 'C':
                total -= stack.pop()
                continue
            if op == 'D':
                stack.append(2 * stack[-1])
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
            total += stack[-1]
        return total
    