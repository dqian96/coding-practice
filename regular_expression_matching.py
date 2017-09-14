# Problem: Regular Expression Matching
# (https://leetcode.com/problems/regular-expression-matching/discuss/)

class Solution(object):
    def backtrack(self, text, pattern, pt, pp):
        if pp == len(pattern):
            return True if pt == len(text) else False
        if pt == len(text):
            for i in range(pp, len(pattern)):
                if pattern[i] != '*' and (i + 1 == len(pattern) or pattern[i + 1] != '*'):
                    return False
            return True
        
        if pattern[pp] != '*' and pp + 1 < len(pattern) and pattern[pp + 1] == '*':
            pp += 1
            
        if pattern[pp].isalpha() and (pp == len(pattern) - 1 or pattern[pp + 1] != '*'):
            # character match
            return False if pattern[pp] != text[pt] else self.backtrack(text, pattern, pt + 1, pp + 1)
        
        if pattern[pp] == '.' and (pp == len(pattern) - 1 or pattern[pp + 1] != '*'):
            # single character match
            return False if pt == len(text) else self.backtrack(text, pattern, pt + 1, pp + 1)
        
        if pattern[pp] == '*':
            # match preceding 0 or as many times
            prec = pattern[pp - 1]
            for i in range(len(text) - pt + 1):
                if i != 0 and text[pt + i - 1] != prec and prec != '.':
                    break
                if self.backtrack(text, pattern, pt + i, pp + 1):
                    return True
            return False
        
    def isMatch(self, s, p):
        return self.backtrack(s, p, 0, 0)
        