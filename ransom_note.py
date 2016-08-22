# Problem: Ransom Note
# (https://leetcode.com/problems/ransom-note/)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # list comprehension (i.e. append 0 according for 26 chars)
        letterTracker = [ 0 for i in xrange(0, 26) ]

        # magazine +1
        # ransom note -1
        # letterTracker has elem all non-negative - ransom note complete

        for i in xrange(0, max(len(ransomNote), len(magazine))):
            if i < len(ransomNote):
                letterTracker[ord(ransomNote[i]) - 97] -= 1
            if i < len(magazine):
                letterTracker[ord(magazine[i]) - 97] += 1
        for num in letterTracker:
            if num < 0:
                return False
        return True