# Problem: Isomorphic Strings
# (https://leetcode.com/problems/isomorphic-strings/#/description)

from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        mapping = defaultdict(str)
        reverseMapping = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            if t[i] not in reverseMapping:
                reverseMapping[t[i]] = s[i]
            if mapping[s[i]] != t[i] or reverseMapping[t[i]] != s[i]: return False
        return True
        