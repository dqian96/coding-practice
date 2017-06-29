// Problem: Can Place Flowers
// (https://leetcode.com/problems/can-place-flowers/#/description)

// We know that the locations that the flowers are already placed at taken - we can do nothing about
// them. In addition, the adjacent locations near the planted flowers are also already taken.
// We can cut them out from our consideration entirely, and focus on the remaining valid spots.
// The remaining valid spots are all segments of '000...000's in which we can place a flower anywhere.
// How do we maximize our planting these segments?
// The idea is to start planting at the edges, since they invalidate the LEAST (1 instead of 2) places.
// For example 1x0000 vs x1x000.
// As long as we start planting at the left edge, we invalidate the least amount of spaces, and then
// proceed with the next valid location since all other moves are idential (i.e. all cross out one location).

func canPlaceFlowers(flowerbed []int, n int) bool {
    for i := 0; n != 0 && i < len(flowerbed); i++ {
        if flowerbed[i] == 1 || (i - 1 >= 0 && flowerbed[i - 1] == 1 || (i + 1 < len(flowerbed) && flowerbed[i + 1] == 1)) {
            continue
        }
        flowerbed[i] = 1
        n -= 1
    }
    return n == 0
}
