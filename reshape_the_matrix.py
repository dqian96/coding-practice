# Problem: Reshape the matrix
# (https://leetcode.com/problems/reshape-the-matrix/#/description)

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return nums
        orgR = len(nums)
        orgC = len(nums[0])
        if orgR * orgC != r * c:
            return nums
        
        reshapedMatrix = []
        reshapedRow = []
        for row in nums:
            for val in row:
                if len(reshapedRow) == c:
                    reshapedMatrix.append(reshapedRow)
                    reshapedRow = []
                reshapedRow.append(val)
        reshapedMatrix.append(reshapedRow)
        return reshapedMatrix
        