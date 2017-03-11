# find if a subsetSize-set of set A can sum to s
def isSubsetSum(A, subsetSize, subsetSum):
    n = len(A)
    if n == 1:        # only one element
        [A[0]] if A[0] == subsetSum else []

    p = reduce(lambda x, y: abs(x) + abs(y), A)     # sum of all abs(elements)
    T = [[[float("-inf") for k in range(0, subsetSize + 1)] for j in range(0, p + 1)] for i in range(0, n)]
    d = reduce(lambda x, y: min(0, x) + min(0, y), A) * -1      # absolute value of all negative elements

    # fill out base cases
    for i in range(0, n):
        for j in range(0, p + 1):
            if i == 0:
                T[0][j][1] = 1 if A[0] == j - d else 0
                for k in range(2, subsetSize + 1):
                    T[0][j][k] = 0
            if j == 0 + d:
                T[i][j][0] = 1
            else:
                T[i][j][0] = 0

    # fill out recrusive cases
    for i in range(1, n):
        for j in range(0, p + 1):
            for k in range(1, subsetSize + 1):
                if j-A[i] < 0 or j-A[i] > p:
                    T[i][j][k] = T[i-1][j][k]
                    assert(T[i-1][j][k] != float("-inf"))
                else:
                    T[i][j][k] = max(T[i-1][j][k], T[i-1][j-A[i]][k-1])
                    assert(max(T[i-1][j][k], T[i-1][j-A[i]][k-1]) != float("-inf"))
    
    # traceback for solution set
    subset = []
    if T[n-1][subsetSum + d][subsetSize] == 1:
        # traceback
        i = n-1
        j = subsetSum + d
        k = subsetSize
        while i >= 0:
            if i in range(1, n-1 + 1) and j in range(0, p + 1) and k in range(1, subsetSize + 1):
                # recursive case
                if T[i-1][j][k] == T[i][j][k]:
                    # ai not in B
                    pass
                else:
                    # ai in B
                    subset.append(A[i])
                    j = j - A[i]
                    k = k - 1
                i = i - 1
            else:
                # base case
                if T[i][j][k] == 1 and k == 1:
                    # base case where we determine if a0 is in the subset
                    subset.append(A[i])
                    break
    return subset


def main():
    import random

    SSIZE = 5
    for test in range(50):
        A = [random.randint(-50, 50) for i in range(SSIZE)]
        sum = reduce(lambda x, y: x + y, A)
        RAN = [random.randint(-50, 50) for i in range(random.randint(0, SSIZE*2))]
        A = A + RAN

        resSet = isSubsetSum(A, SSIZE, sum)
        resSum = reduce(lambda x, y: x + y, resSet)

        assert(len(resSet) == SSIZE)    # subset size must match
        assert(resSum == sum)       # subset sum must match
        print "TEST " + str(test + 1) + " OK!"


if __name__ == "__main__":
    main()