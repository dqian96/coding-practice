# Problem: 3Sum
# (https://leetcode.com/problems/3sum/)

# I will present two solutions to this problem.
# The first sol

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # create dictionary of (int, [indices]) KVPS for O(1) lookup
        intsAndTheirIndices = {}
        """
        {
            1: [0,2,3],
            2: [1,5,6]
        }
        """
        for i in range(0, len(nums)):
            if nums[i] not in intsAndTheirIndices:
                intsAndTheirIndices[nums[i]] = [i]
            else:
                intsAndTheirIndices[nums[i]].append(i)

        tripletSet = set()
        res = []
        for x in range(0, len(nums) - 2):
            # find b and c
            a = nums[x]
            for y in range(x + 1, len(nums) - 1):
                b = nums[y]
                c = -a - b
                if c in intsAndTheirIndices:
                    for index in intsAndTheirIndices[c]:
                        if index > y:
                            triplet = [a, b, c]
                            triplet.sort()
                            tripletTuple = (triplet[0], triplet[1], triplet[2])
                            if tripletTuple not in tripletSet:
                                tripletSet.add(tripletTuple)
                                res.append(triplet)
                            break
        return res
