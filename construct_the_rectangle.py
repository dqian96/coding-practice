# Problem: Construct the Rectangle
# (https://leetcode.com/problems/construct-the-rectangle/#/description)

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for w in range(int(math.sqrt(area)), 0, -1):
            if area % w == 0:
                return [area/w, w]
                