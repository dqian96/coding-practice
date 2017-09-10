# Problem: Find all anagrams in a string
# (https://leetcode.com/problems/find-all-anagrams-in-a-string/)

from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        charCount = defaultdict(int)
        for c in p:
            charCount[c] += 1
        
        charsToMatch = len(p)
        for i in range(len(s)):
            c = s[i]
            if i <= len(p) - 1:
                if c in charCount:
                    if charCount[c] > 0:
                        charsToMatch -= 1
                    charCount[c] -= 1
            else:
                first = s[i - 1 - (len(p) - 1)]
                if first in charCount:
                    charCount[first] += 1
                    if charCount[first] > 0:
                        charsToMatch += 1
                if c in charCount:
                    if charCount[c] > 0:
                        charsToMatch -= 1
                    charCount[c] -= 1
            
            if charsToMatch == 0:
                res.append(i - (len(p) - 1))
                
        return res

# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         if len(p) > len(s):
#             return []

#         res = []
#         charDistr = {}
#         count = len(p)
#         for char in p:
#             if char not in charDistr.keys():
#                 charDistr[char] = 1
#             else:
#                 charDistr[char] += 1
#         for i in range(0, len(p)):
#             if s[i] in charDistr.keys():
#                 if charDistr[s[i]] > 0:
#                     count -= 1
#                 charDistr[s[i]] -= 1

#         leftBound = 0
#         rightBound = len(p) - 1
#         while rightBound < len(s) - 1:
#             if count == 0:
#                 res.append(leftBound)
#             if s[leftBound] in charDistr.keys():
#                 if charDistr[s[leftBound]] >= 0:
#                     count += 1
#                 charDistr[s[leftBound]] += 1
#             leftBound += 1
#             rightBound += 1
#             if s[rightBound] in charDistr.keys():
#                 if charDistr[s[rightBound]] > 0:
#                     count -= 1
#                 charDistr[s[rightBound]] -= 1
#         if count == 0:      
#             res.append(leftBound)

#         return res

