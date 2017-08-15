# Problem: Teemo Attacking
# (https://leetcode.com/problems/teemo-attacking/description/)

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        timeSeries.append(timeSeries[-1] + duration)
        
        nextUnpoisonedTime = timeSeries[0] + duration
        totalPoisonTime = 0
        for poisonTime in timeSeries:
            if poisonTime >= nextUnpoisonedTime:
                totalPoisonTime += duration
            else:
                totalPoisonTime += poisonTime - (nextUnpoisonedTime - duration)
            nextUnpoisonedTime = poisonTime + duration
        
        return totalPoisonTime
            