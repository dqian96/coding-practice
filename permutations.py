# Problem: Permutations
# (https://leetcode.com/problems/permutations/description/)

class Solution(object):
    def permuteFirstN(self, nums, n):
        if n == 1:
            return [[nums[0]]]
        
        res = []
        perms = self.permuteFirstN(nums, n - 1)
        newNum = nums[n - 1]
        for perm in perms:
            for pos in range(len(perm) + 1):
                newPerm = perm[:pos]
                newPerm.append(newNum)
                newPerm += perm[pos:]
                res.append(newPerm)
        return res
            
    def permute(self, nums):
        return self.permuteFirstN(nums, len(nums))
    