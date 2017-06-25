# Problem: Implement strStr()
# (https://leetcode.com/problems/implement-strstr/#/description)

# An implementation of Rabin-Karp
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        needleHash, candidateNeedleHash = 0, 0
        for c in needle:
            needleHash += self.hashFunction(c)
        for i in range(len(haystack)):
            candidateNeedleHash += self.hashFunction(haystack[i])
            if i > len(needle) - 1: candidateNeedleHash -= self.hashFunction(haystack[(i - len(needle))])
            if candidateNeedleHash == needleHash and haystack[(i - (len(needle) - 1)):(i + 1)] == needle:
                return (i - (len(needle) - 1))
            
        return -1
        
    def hashFunction(self, char):
        return ord(char) * 105943
