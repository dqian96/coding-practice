# Problem: Combination Sum
# (https://leetcode.com/problems/combination-sum/description/)

# Backtracking
# Sort the candidates. From the smallest to largest candidate, recursively
# try/sum each candidate until sum is the same as target or too big.
# If it's too big, then at that level, the remaining larger candidates are unacceptable.
# This is an invalid solution. Backtrack one level and try the rest.
# There is never any need to go back and check smaller candidates, as previous searches
# already try all combinations with the smaller candidates.

class Solution(object):
    def backtrack(self, candidates, curr, res, attemptedCombo, currentSum, target):
        if currentSum == target:
            res.append(attemptedCombo[:])
            return True
        
        if currentSum >= target:
            return True

        for i in range(curr, len(candidates)):
            currentSum += candidates[i]
            attemptedCombo.append(candidates[i])

            isTooBig = self.backtrack(candidates, i, res, attemptedCombo, currentSum, target)

            currentSum -= candidates[i]
            attemptedCombo.pop()

            if isTooBig:
                break
                    
        return False
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.backtrack(candidates, 0, res, [], 0, target)
        return res
        