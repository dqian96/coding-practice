# Problem: Decode numWays# ()
# (https://leetcode.com/problems/decode-ways/description/)

from collections import defaultdict

class Solution(object):
    def dp(self, s, i, ht):
        if i <= len(s) - 1 and s[i] == '0':
            return 0
        if i >= len(s) - 1:
            return 1
        if i in ht:
            return ht[i]
        numWays = 0
        for j in range(i, len(s)):
            decode = int(s[i:j + 1])
            if decode > 0 and decode <= 26:
                numWays += self.dp(s, j + 1, ht)
                continue
            break
        ht[i] = numWays
        return numWays
            
    def numDecodings(self, s):
        if len(s) == 0: return 0
        ht = defaultdict(int)
        return self.dp(s, 0, ht)
        