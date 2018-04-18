# Problem: Partition Labels
# (https://leetcode.com/problems/partition-labels/description/)

from collections import defaultdict

class Solution(object):
    def findRightMostOccurences(self, S):
        d = defaultdict()
        for i in range(len(S)):
            d[S[i]] = i
        return d

    def partitionLabels(self, S):
        d = self.findRightMostOccurences(S)
        partitionSizes = []
        excRight = 0
        for i in range(len(S)):
            c = S[i]
            if i == excRight:
                partitionSizes.append(0)
            partitionSizes[-1] += max(excRight, (d[c] + 1)) - excRight
            excRight = max(excRight, d[c] + 1)

        return partitionSizes
