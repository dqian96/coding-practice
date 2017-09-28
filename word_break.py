# Problem: Word Break
# (https://leetcode.com/problems/word-break/description/)

# More efficient solution exists
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = set()
        for word in wordDict:
            d.add(word)
        
        T = [[False for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s) - 1, -1, -1):
            # row
            for j in range(len(s)):
                # col
                T[i][j] = s[i:j+1] in d
                if T[i][j] or i == j:
                    continue
                
                for k in range(i, j - 1 + 1):
                    if T[i][k] and T[k + 1][j]:
                        T[i][j] = True
                        break
                        
        return T[0][len(s) - 1]
    