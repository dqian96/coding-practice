# Problem: Generate Parantheses
# (https://leetcode.com/problems/generate-parentheses/description/)

class Solution(object):
    def backtrack(self, res, temp, l, r, n):
        if l + r == n * 2:
            # sol
            res.append(''.join(temp))
            return
        
        if l < n:
            # more lefts
            temp.append('(')
            self.backtrack(res, temp, l + 1, r, n)
            temp.pop()
        if l > r:
            # able to add a right
            temp.append(')')
            self.backtrack(res, temp, l, r + 1, n)
            temp.pop()
        
    def generateParenthesis(self, n):
        res = []
        self.backtrack(res, [], 0, 0, n)
        return res
    