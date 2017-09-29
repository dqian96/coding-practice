# Problem: Search in Rotated Array
# (https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

class Solution(object):
    def binarySearch(self, A, lower, upper, target):
        if lower > upper:
            return -1
        mid = (lower + upper)/2
        if A[mid] == target:
            return mid
        
        if A[lower] <= A[mid]:
            if target >= A[lower] and target <= A[mid]:
                return self.binarySearch(A, lower, mid - 1, target)
            return self.binarySearch(A, mid + 1, upper, target)
        
        if target >= A[mid + 1] and target <= A[upper]:
            return self.binarySearch(A, mid + 1, upper, target)
        return self.binarySearch(A, lower, mid - 1, target)
        
    def search(self, nums, target):
        return self.binarySearch(nums, 0, len(nums) - 1, target)
    