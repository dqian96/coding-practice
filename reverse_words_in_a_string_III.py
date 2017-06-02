# Problem: Reverse Words in a String III
# (https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description)

# Love me some python one-liners

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda w: w[::-1], s.split()))
        