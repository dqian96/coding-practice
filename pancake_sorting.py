# Problem: Pankcake Sorting
# (https://leetcode.com/problems/pancake-sorting/submissions/)

# Done as part of contest 118

class Solution:
    def flip(self, A, j):
        i = 0
        while i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            j -= 1

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips = []

        for i in range(len(A)):
            # find max in 0 to len(A) - 1 - i
            largest, index = float('-inf'), -1

            for j in range(len(A) - i):
                if A[j] > largest:
                    largest = A[j]
                    index = j

            flips.append(index + 1)
            flips.append(len(A) - 1 - i + 1)

            self.flip(A, index)
            self.flip(A, len(A) - 1 - i)

        return flips

