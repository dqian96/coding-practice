# Problem: Relative Ranks
# (https://leetcode.com/problems/relative-ranks/#/description)

from collections import defaultdict

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        placementTable = defaultdict(int)
        sortedNums = nums[:]
        sortedNums.sort(reverse=True)
        for index, num in enumerate(sortedNums):
            placementTable[num] = index + 1
        return list(map(lambda num: str(placementTable[num]) if placementTable[num] > 3 else medals[placementTable[num] - 1], nums))
        