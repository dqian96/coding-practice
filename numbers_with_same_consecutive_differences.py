# Problem: Numbers with Same Consecutive Difference
# (https://leetcode.com/problems/numbers-with-same-consecutive-differences)

# Done as part of contest 117

class Solution(object):
    def backtrack(self, limit, current, answers, K):
        if len(current) == limit:
            answers.append(''.join(current))
            return

        for i in range(10):
            if len(current) == 0 and i == 0: continue
            if len(current) != 0:
                prev = int(current[-1])
                if abs(prev - i) != K:
                    continue
            current.append(str(i))
            self.backtrack(limit, current, answers, K)
            current.pop()

    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        answers = []
        current = []

        self.backtrack(N, current, answers, K)
        return [int(ans) for ans in answers]

