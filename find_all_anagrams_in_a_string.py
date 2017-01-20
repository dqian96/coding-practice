# Problem: Find all anagrams in a string
# (https://leetcode.com/problems/find-all-anagrams-in-a-string/)

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        res = []
        charDistr = {}
        count = len(p)
        for char in p:
            if char not in charDistr.keys():
                charDistr[char] = 1
            else:
                charDistr[char] += 1
        for i in range(0, len(p)):
            if s[i] in charDistr.keys():
                if charDistr[s[i]] > 0:
                    count -= 1
                charDistr[s[i]] -= 1

        leftBound = 0
        rightBound = len(p) - 1
        while rightBound < len(s) - 1:
            if count == 0:
                res.append(leftBound)
            if s[leftBound] in charDistr.keys():
                if charDistr[s[leftBound]] >= 0:
                    count += 1
                charDistr[s[leftBound]] += 1
            leftBound += 1
            rightBound += 1
            if s[rightBound] in charDistr.keys():
                if charDistr[s[rightBound]] > 0:
                    count -= 1
                charDistr[s[rightBound]] -= 1
        if count == 0:      
            res.append(leftBound)

        return res

