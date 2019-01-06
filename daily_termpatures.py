# Problem: Daily Temperatures
# (https://leetcode.com/problems/daily-temperatures/description/)

"""
    The idea is to for each data point, we need to find a higher temperature day in the future.
    For each temperature t, we could try to find if days with temperatures in range (t + 1, 100) exist.
    We can check this by simply iterating through an array with indicies representing temperatures and value
    representing the day they occurred at. Obviously, we choose the closest value/day. We also iterate right to left
    such that we only consider later days.

    Time: O(n)
    Space: O(1)
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        max_index = 30000
        temp_range = 71
        temps = [max_index] * temp_range

        for d in range(len(temperatures) - 1, -1, -1):
            t = temperatures[d]

            closest_day = max_index
            for warmer in range(t - 30 + 1, temp_range):
                closest_day = min(closest_day, temps[warmer])

            if closest_day == max_index:
                temperatures[d] = 0
            else:
                temperatures[d] = closest_day - d

            temps[t - 30] = d

        return temperatures
