# Problem: Kth largest element in an array
# (https://leetcode.com/problems/kth-largest-element-in-an-array/#/description)


# This is just quick select - average O(n) (if using index calculations instead of partitions)

class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		if len(nums) == 1:
			return nums[0]
		pivot = nums[0]
		left = 1
		right = len(nums) - 1
		while left <= right:
			if nums[left] >= pivot:
				left += 1
			if nums[right] < pivot:
				right -= 1
			if left <= right and nums[left] < pivot and nums[right] >= pivot:
				temp = nums[left]
				nums[left] = nums[right]
				nums[right] = temp
		nums[0] = nums[right]
		nums[right] = pivot
		if right < k - 1:
			return self.findKthLargest(nums[right + 1:], k - (right + 1))
		elif right > k - 1:
			return self.findKthLargest(nums[:right], k)
		return nums[right]

