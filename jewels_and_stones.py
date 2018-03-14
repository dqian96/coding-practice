# Problem: Jewels and Stones
# (https://leetcode.com/problems/jewels-and-stones/description/)

# O(1) time and space due to finite upper bound on string length

class Solution(object):
    def numJewelsInStones(self, J, S):
        s = set()
        for c in J:
            s.add(c)
        return sum(c in s for c in S)
