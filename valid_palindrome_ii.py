# Problem: Valid Palindrome II
# (https://leetcode.com/problems/valid-palindrome-ii/description/)

class Solution(object):
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s):
        p0 = 0
        p1 = len(s) - 1
        while p0 < p1:
            if s[p0] == s[p1]:
                p0 += 1
                p1 -= 1
                continue
            return self.isPalindrome(s, p0 + 1, p1) or self.isPalindrome(s, p0, p1 - 1)
        return True
    