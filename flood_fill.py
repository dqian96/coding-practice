# Problem: Flood Fill
# (https://leetcode.com/problems/flood-fill/description/)

class Solution(object):
    def recursiveFill(self, image, replace, newColor, r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != replace:
            return
        image[r][c] = newColor
        self.recursiveFill(image, replace, newColor, r - 1, c)
        self.recursiveFill(image, replace, newColor, r + 1, c)
        self.recursiveFill(image, replace, newColor, r, c - 1)
        self.recursiveFill(image, replace, newColor, r, c + 1)

    def floodFill(self, image, sr, sc, newColor):
        replace = image[sr][sc]
        if replace == newColor:
            return image
        self.recursiveFill(image, replace, newColor, sr, sc)
        return image

