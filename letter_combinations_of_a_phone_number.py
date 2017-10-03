# Problem: Letter Combinations of a Phone Number
# (https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

from collections import defaultdict

class Solution(object):
    def solve(self, digits, i, digitToLetters):
        if i == 0:
            return [[c] for c in digitToLetters[int(digits[i])]]
            
        prevWords = self.solve(digits, i - 1, digitToLetters)
        
        letters = digitToLetters[int(digits[i])]
        for word in prevWords:
            word.append(letters[0])
        
        ogLength = len(prevWords)
        for i in range(1, len(letters)):
            for j in range(ogLength):
                prevWords.append(prevWords[j][:])
                prevWords[-1][-1] = letters[i]
                
        return prevWords
            
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        digitToLetters = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        return ["".join(w) for w in self.solve(digits, len(digits) - 1, digitToLetters)]
        