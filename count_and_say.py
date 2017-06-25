# Problem: Count and Say
# (https://leetcode.com/problems/count-and-say/#/description)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n - 1):
            tmp = []
            blockStart = 0
            for j in range(len(s) + 1):
                if j == len(s) or (s[j] != s[j - 1] and j != 0):
                    tmp.append(str(j - blockStart))
                    tmp.append(s[blockStart])
                    blockStart = j
            s = "".join(tmp)
        return s
                