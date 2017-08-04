# Problem: Brick Wall
# (https://leetcode.com/problems/brick-wall/description/)

from collections import defaultdict
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if len(wall) == 0 or len(wall[0]) == 0: return 0
        
        width = sum(wall[0])
        slits = defaultdict(int)
        if width == 1: return len(wall)
        
        for layer in wall:
            slit = 0
            for brick in layer:
                slit += brick
                if slit == width: break
                slits[slit] += 1
        return len(wall) - max(slits.values()) if len(slits) != 0 else len(wall)
        