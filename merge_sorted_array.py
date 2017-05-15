# Problem: Merge Sorted Array
# (https://leetcode.com/problems/merge-sorted-array/#/description)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m - 1, -1, -1):
             nums1[m + n - 1 - (m - 1 - i)] = nums1[i]
        start = n
            
        p1 = start
        p2 = 0
        curr = 0
        while curr < m + n:
            if p1 >= m + n:
                nums1[curr] = nums2[p2]
                p2 += 1
            elif p2 >= n:
                nums1[curr] = nums1[p1]
                p1 += 1
            else:
                if nums1[p1] <= nums2[p2]:
                    nums1[curr] = nums1[p1]
                    p1 += 1
                else:
                    nums1[curr] = nums2[p2]
                    p2 += 1
            curr += 1
