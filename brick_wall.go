// Problem: Brick Wall
// (https://leetcode.com/problems/brick-wall/#/description)

func leastBricks(wall [][]int) int {
    width := 0
    holes := make([]map[int]bool, len(wall))
    allHoles := make(map[int]int)
    for index, layer := range wall {
        if holes[index] == nil {
            holes[index] = make(map[int]bool)
        }
        cracks := 0
        for _, brick := range layer[:len(layer) - 1] {
            cracks += brick
            holes[index][cracks] = true
            if _, ok := allHoles[cracks]; !ok {
                allHoles[cracks] = 0
            }
            allHoles[cracks] += 1
        }
        if width == 0 {
            cracks += layer[len(layer) - 1]
            width = cracks
        }
    }
    if len(allHoles) == 0 {
        return len(wall)
    }
    minBricks := 100001
    for _, num := range allHoles {
        bricks := len(wall) - num
        if bricks < minBricks {
            minBricks = bricks
        }
    }
    return minBricks
}

