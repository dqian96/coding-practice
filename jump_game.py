# Problem: Jump Game
# (https://leetcode.com/problems/jump-game/description/)

# Greedy
class Solution(object):
    def canJump(self, nums):
        farthestJumpIndex = 0
        for i in range(len(nums)):
            if i > farthestJumpIndex:
                return False
            farthestJumpIndex = max(farthestJumpIndex, i + nums[i])
            if farthestJumpIndex >= len(nums) - 1:
                return True
            