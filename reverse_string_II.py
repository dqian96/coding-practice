# Problem: Reverse String II
# (https://leetcode.com/problems/reverse-string-ii/#/description)

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        sList = list(s)
        for i in range(0, len(sList), 2 * k):
            p0, p1 = i, (i + k - 1) if (i + k - 1) < len(sList) else len(sList) - 1
            while p0 < p1:
                temp = sList[p0]
                sList[p0] = sList[p1]
                sList[p1] = temp
                p0 += 1
                p1 -= 1
        return "".join(sList)
        