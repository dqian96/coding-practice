# Problem: Length of Last Word
# (https://leetcode.com/problems/length-of-last-word/#/description)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        endOfWordIndex = -1
        for i in range(len(s) - 1, -1, -1):
            if endOfWordIndex == -1 and s[i] != ' ':
                endOfWordIndex = i
            elif endOfWordIndex != -1 and s[i] == ' ':
                return endOfWordIndex - i
        return endOfWordIndex + 1
        