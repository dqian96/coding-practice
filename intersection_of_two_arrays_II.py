# Problem: Intersection of Two Arrays II
# (https://leetcode.com/problems/intersection-of-two-arrays-ii/#/description)

# The method listed is O(n) time and O(n) space (n is max of lengths)

# Alternatively, if the lists were sorted, then the runtime would be
# O(n) with no extra space via a 2 pointers approach

from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shorterList = nums1 if len(nums1) < len(nums2) else nums2
        longerList = nums1 if shorterList != nums1 else nums2
        
        easyLookup = defaultdict(int)
        for num in shorterList:
            easyLookup[num] += 1
        
        intersection = []
        for num in longerList:
            if easyLookup[num] != 0:
                intersection.append(num)
                easyLookup[num] -= 1
        
        return intersection
        