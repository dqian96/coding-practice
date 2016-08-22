# Problem: Intersection of Two Arrays
# (https://leetcode.com/problems/intersection-of-two-arrays/)


# Treat the arrays as matehatmical sets (i.e. reptitions of numbers are irrelevant). 
# We are looking for the COMMON elements (intersection).

# This question can be solved in multiple ways:
#   1. Create a hash table and iterate through both of the arrays at once, looking for collisions. (Space: O(n1 + n2) - not counting return list, Time: O(max(n1, n2)))
#   2. Sort the smaller array. Iterate through the bigger array, performing binary search
#      on the sorted array for each element of the smaller array. (Space: O(1), Time: O(n1logn1 + n2logn1))
#   3. Sort both arrays. Iterate through both using two pointers (i.e. advance the smaller pointed elem) O(n1logn1 + n2logn2)


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        collisionChecker = {}
        result = []

        for i in xrange(0, max(len(nums1), len(nums2))):
            # not done iterating thorough nums1
            if i < len(nums1):
                if nums1[i] in collisionChecker:
                    if collisionChecker[nums1[i]] == 2:
                        collisionChecker[nums1[i]] = 0
                        result.append(nums1[i])
                elif i < len(nums2):
                    collisionChecker[nums1[i]] = 1
            if i < len(nums2):
                if nums2[i] in collisionChecker:
                    if collisionChecker[nums2[i]] == 1:
                        collisionChecker[nums2[i]] = 0
                        result.append(nums2[i])
                elif i < len(nums1):
                    collisionChecker[nums2[i]] = 2            
        return result