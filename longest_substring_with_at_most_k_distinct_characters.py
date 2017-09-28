# Problem: Longest Substring with At Most K Distinct Characters
# (https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)

from collections import defaultdict

class Solution(object):
    def findFirstCharToRemove(self, occurenceMap):
        smallestLastOccurence = float("inf")
        for char in occurenceMap.keys():
            if occurenceMap[char] < smallestLastOccurence:
                smallestLastOccurence = occurenceMap[char]
                charToRemove = char
        
        return charToRemove

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0: return 0
        
        letterToLastOccurence = defaultdict(int)
        
        longestSubstringLength = 0  # constraint: size <= k
        substringStart = 0
        
        for i, c in enumerate(s):
            if c not in letterToLastOccurence and len(letterToLastOccurence) == k:
                firstCharToRemove = self.findFirstCharToRemove(letterToLastOccurence)
                substringStart = letterToLastOccurence[firstCharToRemove] + 1
                letterToLastOccurence.pop(firstCharToRemove)

            letterToLastOccurence[c] = i
            
            longestSubstringLength = max(longestSubstringLength, i - substringStart + 1)
        
        return longestSubstringLength
            