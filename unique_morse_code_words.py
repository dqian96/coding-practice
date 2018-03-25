# Unique Morse Code Words
# (https://leetcode.com/problems/unique-morse-code-words/)

class Solution(object):
    morseCodeEncoding = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words):
        transformations = set()
        for word in words:
            transformation = []
            for c in word:
                transformation.append(self.morseCodeEncoding[ord(c) - ord('a')])
            transformations.add(''.join(transformation))
        return len(transformations)

