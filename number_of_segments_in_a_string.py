# Problem: Number of Segments in a String
# (https://leetcode.com/problems/number-of-segments-in-a-string/#/description)

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segments = 0
        for index, char in enumerate(s):
            if char != ' ' and (index == 0 or s[index - 1] == ' '):
                segments += 1
        return segments
        