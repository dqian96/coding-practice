# Problem: Longest Palindrome
# (https://leetcode.com/problems/longest-palindrome/)

# We are given a string/character array.
# Essentially, a multi-set of characters. From this multiset,
# we want to determine the length of the longest palindrome
# we can possibly create.

# Let's first look at the properties of palindromes.
# If p = p0p1p2...pn-2pn-1 is a palindrome of length n,
# then by the properties of palindromes, we know that
# pi = pn-1-i for i E [0, (n-1)/2].
# In other words, if a character appears in the first half,
# then that character must occur in the second half.
# Characters in the palindrome must come in pairs - one in the first
# half, one in the second. Thus, all the occurence of any character
# in the palindrome is even, except the one in the middle in an
# odd length palindrome.

# This property of even occurence or occurence in PAIRS gives us an
# interesting insight.
# If we iterate through the array, and for each character c,
# we come across another instance of c in the character array, then
# we know automatically that both c's are part of the longest palindrome
# and the length of it automatically includes these 2.
# With that being said, we think of ways we can track occurences of characters
# as we iterate through the character array. The natural instinct is to go
# with a hashmap/set as it has O(1) lookup.
# So, if we encounter c in the char array, we add to the hash set if its not
# there. If it is in the set, we remove from it and add 1 to the count.
# Essentially, this means we count the pairs of characters.
# Every remove indicates that there must be two instances/a pair of the character
# c in the character array. As we iterate through it, we can count the number
# of pairs of the character. If the palindrome were even length, we would be done.
# However, the middle character of a palindrome need not have a pair.
# Therefore, at the end of the iteration, we look back in our set.
# If our set is not empty, we have an unpaired character which can serve
# as the middle character. Therefore, the length of the longest palindrome is
# numPairs*2 if set size is 0 or numPairs*2 + 1 if set size is not 0.
# This is O(n) time and O(n) space (assuming all chars distinct).

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        unpaired = set()
        numPairs = 0
        for c in s:
            if c in unpaired:
                unpaired.remove(c)
                numPairs += 1
            else:
                unpaired.add(c)
        if unpaired:
            # if unpaired is not empty
            return numPairs*2 + 1
        return numPairs*2

