# Problem: Repeated Substring Pattern
# (https://leetcode.com/problems/repeated-substring-pattern/)

# Idea:
# If you could recreate the string given using repeated appendings of some pattern substring,
# then naturally, the size of the string must be a multiple of the size of the pattern.
# Therefore, we check sizes 1 to len(str)/2. If we find an acceptable size,
# we check whether or not the pattern substring is indeed repeated throughout the string given.
# This given be done in place.

# Complexity: O(1) space, O(n^2) time

# Alternatively, we can use KMP to achieve O(n) time

class Solution(object):
    def repeatedSubstringPattern(self, str):
        for i in range(1, len(str)/2 + 1):
            if len(str) % i == 0:
                patternPosition = 0
                patternExists = True
                for character in str:
                    if character != str[patternPosition]:
                        patternExists = False
                        break
                    patternPosition = patternPosition + 1 if patternPosition != i - 1 else 0
                if patternExists:
                    return True
        return False
                