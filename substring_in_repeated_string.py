# Problem: Repeated String Match
# (https://leetcode.com/problems/repeated-string-match/description/)

"""

Given two strings, A and B, return the minimum number of times A must be stated
such that B becomes a substring of the repeated string. If B can never be a substring of
the repeated A, return -1.

For example:

A = "abcd"
B = "cdabcdab"

returns 3

Solution: Find every character of A that matches the first character of B. Keep matching/repeating A
from said character to see if you can match until B's end, incrementing a counter every time
you start from A's first character again.

"""

class Solution(object):
    def match(self, A, B, i):
        # try to see if you can match A[i:] + A + A + ... with B
        num_times_replicated = 1
        p0 = i
        p1 = 0

        while 1:
            if p1 >= len(B):
                # all of B replicated
                return num_times_replicated

            if p0 >= len(A):
                # repeat A again
                p0 = 0
                num_times_replicated += 1
            
            if A[p0] != B[p1]:
                # not proper match
                return float("inf")

            p0 += 1
            p1 += 1

    def repeatedStringMatch(self, A, B):
        min_times_replication = float("inf")        # default value for improper match

        for i in range(len(A)):
            # iterate through A to find first candidate match
            if B[0] == A[i]:
                min_times_replication = min(min_times_replication, self.match(A, B, i))

        return -1 if min_times_replication == float("inf") else min_times_replication
