# Problem: Third Maximum Number
# (https://leetcode.com/problems/third-maximum-number/description/)

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        topNums = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            for i in range(len(topNums)):
                if num == topNums[i]:
                    break
                if num > topNums[i]:
                    insert = num
                    for j in range(i, len(topNums)):
                        temp = topNums[j]
                        topNums[j] = insert
                        insert = temp
                    break

        if topNums[2] == float('-inf'):
            return topNums[0]
        return topNums[2]
