# Problem: Self-Dividing Numbers
# (https://leetcode.com/problems/self-dividing-numbers/description/)

# O(k * 10^k) where k is the length of the largest number
class Solution(object):
    def isSelfDividing(self, num):
        prefix = num
        while prefix != 0:
            digit = prefix % 10
            if digit == 0 or num % digit != 0:
                return False
            prefix /= 10
        return True

    def selfDividingNumbers(self, left, right):
        res = []
        for d in range(left, right + 1):
            if self.isSelfDividing(d):
                res.append(d)
        return res

