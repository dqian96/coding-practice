# Problem: Add Binary
# (https://leetcode.com/problems/add-binary/#/description)

class Solution(object):
    def addBinary(self, a, b):
        res = [''] * (max(len(a), len(b)) + 1)      # for possible extra carry
        carry = 0
        p1 = len(a) - 1
        p2 = len(b) - 1
        curr = len(res) - 1
        while curr >= 1:
            if p1 == -1:
                val = int(b[p2]) + carry
                p2 -= 1
            elif p2 == -1:
                val = int(a[p1]) + carry
                p1 -= 1
            else:
                val = int(a[p1]) + int(b[p2]) + carry
                p1 -= 1
                p2 -= 1
            if val == 0:
                carry = 0
                res[curr] = "0"
            elif val == 1:
                carry = 0
                res[curr] = "1"
            elif val == 2:
                carry = 1
                res[curr] = "0"
            else:
                carry = 1
                res[curr] = "1"
            curr -= 1
        if carry == 1:
            res[0] = "1"
        return ''.join(res)

