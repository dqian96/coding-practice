# Problem: Jumping jack

"""

Jack is standing at the bottom of a flight of stairs. He is initially at floor/level 0.
Jack is given n moves. At each ith move (1-n), Jack can choose to move up i floors from
his current position OR choose to stay at the same position.abs

For example, if Jack is at floor 0, then for his first move, he can move to floor 1 or
stay at floor 0.

Find the maximum floor Jack can reach with n moves, assuming that he CAN'T step at floor k.

Solution: Greedy or DP

Originally, I thought of doing a DP solution. Using a table T[floor][numMove] of size (n + 1) * (maxFloor + 1).
Thus, T[i][j] = 1 or 0, representing whether or not he can validly step on floor i for the jth
move. The highest floor is just the largest i and j = n, such that T[i][j] = n.
However, this proved to be far too inefficient as it is O(n^3) time and space complexity.

The alternative is a greedy solution.

As Jack takes each move, the best/optimal/greedy strategy is to take a step, as that will allow
Jack to get the highest. Two options:

1. Jack takes every step and never lands on floor k
    -> Great, since we took the step at every move, this is the highest floor he can reachj

2. Jack takes all the i-1th steps and lands on floor k at step i
    -> i > 0 as if i == 0 => k == 0 => no solutions are possible because k will always be stepped on
       This would mean that in the optimal move set, Jack must have not taken some step.
       The least harmful step to not have taken is i = 1. This will impact Jack's highest possible
       floor the least. If Jack didn't take the first step, he would be at floor k-1 instead.
       Since i > 0, then the next step Jack takes must be at least i > 1. Thus, since Jack is one step
       away from k and the next move will take him up more than one, Jack can take steps for all the
       remaining moves as he won't land on k.

Thus, we have discovered that it's best to take all the steps possible. If taking all the steps
would lead to stepping on k, the optimal solution must not include a step. The best step to not
include is the first step. All the remaining moves can be taken with no worries as we would
not arrive at k.

This is O(k).

"""
def maxStep(n, k):
    floor = 0
    for step in range(1, n + 1):
        if floor > k:
            floor += int((n * (n+1))/2 - ((step - 1) * step)/2)
            break
        floor += step
        if floor == k:
            floor -= 1
    return floor


# def maxStep(n, k):
#     maxFloor = int(n*(n+1)/2)
#     maxFloorReached = 0

#     isValidState = [[0 for i in range(n + 1)] for j in range(maxFloor + 1)]
    
#     for i in range(n + 1):
#         # base case, 0th floor at any step i is valid
#         isValidState[0][i] = 1
    
#     for j in range(1, maxFloor + 1):
#         # base case, at any non-zero floor, at least one step must have been taken
#         isValidState[j][0] = 0

#     for floor in range(len(isValidState)):
#         if floor == k:
#             # base case, kth floor is invalid
#             continue
#         for numStep in range(len(isValidState[floor])):
#             if floor - numStep < 0:
#                 # base case, at a floor that is unreachable at that particular step
#                 isValidState[floor][numStep] = isValidState[floor][numStep - 1]
#             else:
#                 # recursive case, two possibilities to reach this floor at the numStep'th step
#                 isValidState[floor][numStep] = (isValidState[floor][numStep - 1] or
#                                                      isValidState[floor - numStep][numStep - 1]
#                                                 )
#             if isValidState[floor][numStep]:
#                 maxFloorReached = max(maxFloorReached, floor)

#     return maxFloorReached
