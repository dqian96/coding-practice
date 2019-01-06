# Problem: Boats to Save People
# (https://leetcode.com/contest/weekly-contest-96/problems/boats-to-save-people/)

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        num_boats = 0

        l = 0
        r = len(people) - 1
        while l <= r:
            weight = people[l] + peoaple[r]
            if weight > limit:
                num_boats += 1
                r -= 1
                continue

            if weight <= limit:
                num_boats += 1
                r -= 1
                l += 1
                continue

        return num_boats
