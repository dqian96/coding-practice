# Problem: Detect Capital
# (https://leetcode.com/problems/detect-capital/#/description)

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        
        isTailCapitalized = word[1].isupper()
        
        for c in word[2:]:
            if c.isupper() != isTailCapitalized:
                return False
        
        return not isTailCapitalized or (isTailCapitalized and word[0].isupper())
        