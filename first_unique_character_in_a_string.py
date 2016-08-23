# Problem: First Unique Character in a String
# (https://leetcode.com/problems/first-unique-character-in-a-string/)

# Pretty simple. Iterate through it, using predetermined #s to keep track of 
# repetitions (-2)/never before seen (-1)/seen only once (index)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftMostUniqueChar = -1
        history = [-1]*26

        for i in xrange(0, len(s)):
            if history[ord(s[i]) - 97] >= 0:
                history[ord(s[i]) - 97] = -2
            elif history[ord(s[i]) - 97] == -1:
                history[ord(s[i]) - 97] = i

        for charIndex in history:
            if charIndex < 0:
                pass
            elif leftMostUniqueChar == -1:
                leftMostUniqueChar = charIndex
            elif charIndex < leftMostUniqueChar:
                leftMostUniqueChar = charIndex

        return leftMostUniqueChar
