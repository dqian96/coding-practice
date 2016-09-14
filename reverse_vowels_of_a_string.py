# Problem: Reverse Vowels of a string
# (https://leetcode.com/problems/reverse-vowels-of-a-string/)


# Let s\consonants = v0,v1,v2,...,vn
# It doesn't matter what the positions of the vowels are within the word s. All that matters
# is the relative position of the vowels with respect to each other. 
# So, we have to reverse the vowels. To reverse the vowels, all we have to do
# is keep track of 2 pointers in the word s. 
# One pointer starts from the left side and advanced to vowel vi. The right side vowel
# starts from the right side and advances to vowel vn-i. Swap.
# Do this for i E [0, floor(n/2))

import sets

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # as string are immutable in python, we explode the string in a single pass
        # more efficient 
        sList = list(s)
        vowels = sets.Set(['a','e','i','o','u'])

        pointer1 = 0
        pointer2 = len(sList) - 1
        while pointer2 > pointer1:
        	if sList[pointer1] not in vowels:
        		pointer1 += 1
        	if sList[pointer2] not in vowels:
        		pointer2 -= 1
        	if sList[pointer1] in vowels and sList[pointer2] in vowels:
        		sList[pointer1], sList[pointer2] = sList[pointer2], sList[pointer1]
        		pointer1 += 1
        		pointer2 -= 1

        return "".join(sList)