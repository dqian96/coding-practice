# Problem: Keyboard Row
# (https://leetcode.com/problems/keyboard-row/#/description)

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lettersToRow = {}
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for index, row in enumerate(rows):
            for letter in row:
                lettersToRow[letter] = index
        res = []
        for word in words:
            lettersOnSameRow = True
            for letter in word:
                if lettersToRow[letter.lower()] != lettersToRow[word[0].lower()]:
                    lettersOnSameRow = False
                    break
            if lettersOnSameRow:
                res.append(word)
        return res
        