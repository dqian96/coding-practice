# Problem: Next Greater Element I
# (https://leetcode.com/submissions/detail/104679030/)


# O(mn) solution, where m <= n
# from collections import defaultdict

# class Solution(object):
#     def nextGreaterElement(self, findNums, nums):
#         """
#         :type findNums: List[int]
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         numToIndex = defaultdict(int)
#         for index, num in enumerate(nums):
#             numToIndex[num] = index
        
#         res = []
#         for i in range(len(findNums)):
#             for j in range(numToIndex[findNums[i]] + 1, len(nums)):
#                 if nums[j] > findNums[i]:
#                     res.append(nums[j])
#                     break
#             if len(res) < i + 1:
#                 res.append(-1)
                
#         return res

# O(2n + m) = O(n + m)
# Pattern recongition hurr durr
# Observe the monotonic decreasing sequence

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nextGreaterElement = {}

        stack = []

        for num in nums:
            if len(stack) != 0 and stack[-1] < num:
                while len(stack) != 0 and stack[-1] < num:
                    nextGreaterElement[stack[-1]] = num
                    stack.pop()
            stack.append(num)

        for num in stack:
            nextGreaterElement[num] = -1

        return map(lambda num: nextGreaterElement[num], findNums)
