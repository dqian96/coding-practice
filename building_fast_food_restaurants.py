# Problem: Building fastfood restaurants

# # MacWendy's wishes to build fast food restaurants on a very long highway. There are n
# possible locations for restaurants, denoted by L1, . . . Ln. These values are positive integers
# which represent distances from the beginning of the highway. Associated with each possible
# location Li is an anticipated profit, denoted pi. We are also given a distance D, which is a
# positive integer, and a positive integer k <=  n. Thus a problem instance is defined by the list
# of values (L1, . . . , Ln, p1, . . . , pn, D, k).
# A feasible solution is a set of exactly k restaurant locations, such that each pair of locations is a
# distance at least D apart (MacWendy's does not want to build restaurants too close together).
# The optimal solution is the feasible solution that maximizes the total profit of the selected
# locations.

def getMaxProfit(L, P, D, k, n):
    if k == 0:
        return 0
    negativeInf = float("-inf")
    if n == 0:
        return negativeInf

    T = []
    S = []
    for i in range(0, n):
        s = []
        profitsAtIndex = []
        for j in range(0, k + 1):
            profitsAtIndex.append(0)
            s.append((0, -1))       # (take, prevLocation)
        T.append(profitsAtIndex)
        S.append(s)

    for i in range(0, n):
        if L[i] - L[0] < D:
            maxProfitIndex = 0
            maxProfit = P[0]
            for p in range(1, i + 1):
                if P[p] > maxProfit:
                    maxProfitIndex = p
                    maxProfit = P[p]
            T[i][1] = maxProfit

            ###
            p = maxProfitIndex
            S[p][1] = (1, -1)
            if S[i][1] != S[p][1]:
                S[i][1] = (0, p)

            for j in range(2, k + 1):
                T[i][j] = negativeInf
        else:
            h = 0
            for temp in range(i - 1, -1, -1):
                if L[i] - L[temp] >= D:
                    h = temp
                    break
            for j in range(1, k + 1):
                notTakeProfit = T[i - 1][j]
                takeProfit = T[h][j - 1] + P[i]

                if takeProfit >= notTakeProfit:
                    S[i][j] = (1, h)
                else:
                    S[i][j] = (0, i - 1)
                T[i][j] = max(notTakeProfit, takeProfit)
        
    optimalSubset = []
    index = n - 1
    numToTake = k
    sanityCheck = 0
    while S[index][numToTake][1] != -1:     # prev exists
        if S[index][numToTake][0] == 1: # take
            optimalSubset.append(L[index])
            sanityCheck += P[index]
            numToTake = numToTake - 1
        index = S[index][numToTake][1]

    if S[index][numToTake][0] == 1: # take
        optimalSubset.append(L[index])
        sanityCheck += P[index]

    print sanityCheck
    return (optimalSubset, T[n - 1][k])

L = [1, 3, 6, 8, 9, 11, 14, 16, 17, 18, 20]
P = [4, 10, 9, 6, 12, 5, 8, 10, 7, 11, 2]
D = 3
n = 11
k = 4

print getMaxProfit(L, P, D, k, n)


