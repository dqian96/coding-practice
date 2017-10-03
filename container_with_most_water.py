# Problem: Container with Most Water
# (https://leetcode.com/problems/container-with-most-water/description/)

class Solution(object):
    def calcArea(self, x1, x2, h1, h2):
        return min(h1, h2) * (x2 - x1)
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(height) - 1
        maxArea = 0
        while p1 != p2:
            maxArea = max(maxArea, self.calcArea(p1, p2, height[p1], height[p2]))
            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxArea
                          