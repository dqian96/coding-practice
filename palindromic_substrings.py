# Problem: Palindromic Substrings
# (https://leetcode.com/problems/palindromic-substrings/description/)

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = 0
        for i in range(len(s)):
            noMoreOdds = False
            noMoreEvens = False
            for j in range(min(i, len(s) - 1 - i) + 1):
                if noMoreOdds and noMoreEvens:
                    break
                if not noMoreOdds and s[i-j] == s[i+j]:
                    count += 1
                else:
                    noMoreOdds = True
                if not noMoreEvens and i+j+1 <= len(s) - 1 and s[i-j] == s[i+j+1]:
                    count += 1
                else:
                    noMoreEvens = True
        return count
    