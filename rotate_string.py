# Problem: Rotate String
# (https://leetcode.com/problems/rotate-string/description/)

# O(n^2) time complexity, O(1) space complexity
# Can be done in linear time with KMP
class Solution(object):
    def rotateString(self, A, B):
        if len(A) != len(B): return False
        for i in range(len(A)):
            for j in range(len(B)):
                if A[(i + j) % len(A)] != B[j]:
                    break
                if j == len(B) - 1:
                    return True
        return False

