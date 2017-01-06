# Problem: Binary Watch
# (https://leetcode.com/problems/binary-watch/)

# Given 4 bits to represent "hours" and 6 bits to represent
# "minutes", we are to enumerate all possible times given that
# there are num bits set to 1.

# Therefore, all we have to do is enumerate all possibilities such that
# there are num 1's. However, we have to do this intelligently i.e. via
# backtracking in order to avoid TLE. Backtracking is basically
# when a subtree/part of the search space is pruned because the program
# has realized that the state is already invalid and that there will be
# no solution following the path. The state is determined to be valid/invalid
# according to constraints/limitation/restrictions.

# In this question, there are hour bits and minute bits. 
# The constraints for the hour bits is that:
#   <= num bits are 1
#   <= 11
# The constraints for the minutes bits is that:
#   <= num bits are 1
#   <= 59

# I wrote a recursive procedure that for each possible bit,
# set it to either ONE or ZERO, and the procedure is called recursively
# for each possibility and the remaining bits. Each search path is terminated ASAP as we reached an invalid
# state (too many bits used or number is too big).
# Once we looked at all bits (leaves of the search tree/final states),
# we add the final states to a dictionary holding bits used to state.

# Basically, I calculated all the possible hour and minute options
# for 0-num bits used (this is necessary since the hour representation
# and the minute representation can both use 0,1,2,3,...num bits, so
# we have to look at all final states for 0-num bits used.

# Finally, I matched up valid minute-hour pairs based on their bits used.

class Solution(object):
    def enumerateValidStates(self, currVal, maxVal, currBitsUsed, maxBitsAllowed, totalBits, bitsUsedToValList):
        if currVal <= maxVal and currBitsUsed <= maxBitsAllowed:
            if totalBits == 0:
                if currBitsUsed not in bitsUsedToValList.keys():
                    bitsUsedToValList[currBitsUsed] = [str(currVal)]
                else:
                    bitsUsedToValList[currBitsUsed].append(str(currVal))
            else:
                self.enumerateValidStates(currVal + 2**(totalBits - 1), maxVal, currBitsUsed + 1, maxBitsAllowed, totalBits - 1, bitsUsedToValList)
                self.enumerateValidStates(currVal, maxVal, currBitsUsed, maxBitsAllowed, totalBits - 1, bitsUsedToValList)
    def readBinaryWatch(self, num):
        res = []
        bitsUsedToHoursList = {}
        self.enumerateValidStates(0, 11, 0, num, 4, bitsUsedToHoursList)
        bitsUsedToMinutesList = {}
        self.enumerateValidStates(0, 59, 0, num, 6, bitsUsedToMinutesList)
        for bitsUsed in bitsUsedToHoursList.keys():
            if num - bitsUsed in bitsUsedToMinutesList.keys():
                for hour in bitsUsedToHoursList[bitsUsed]:
                    for minute in bitsUsedToMinutesList[num - bitsUsed]:
                        if len(minute) == 1:
                            res.append(hour + ":0" + minute)
                        else:
                            res.append(hour + ":" + minute)
        return res

        