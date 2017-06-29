// Problem: Heaters
// (https://leetcode.com/problems/heaters/#/description)

import "sort"

func findRadius(houses []int, heaters []int) int {
    maxHeaterRadius := 0
    sort.Ints(houses)
    sort.Ints(heaters)
    for _, house := range houses {
        index, closestHeaterRadius := binarySearch(heaters, house), 0
        fmt.Println(index, house)
        if index == len(heaters) {
            closestHeaterRadius = house - heaters[len(heaters) - 1]
        } else if heaters[index] != house {
            closestHeaterRadius = heaters[index] - house
            if index - 1 >= 0 && house - heaters[index - 1] < closestHeaterRadius {
                closestHeaterRadius = house - heaters[index - 1]
            }
        }
        if closestHeaterRadius > maxHeaterRadius {
            maxHeaterRadius = closestHeaterRadius
        }
    }
    return maxHeaterRadius
}

func binarySearch(array []int, target int) int {
    candidate := len(array)/2
    if array[candidate] < target {
        if candidate == len(array) - 1 {
            return len(array)
        }
        return candidate + 1 + binarySearch(array[(candidate + 1):], target)
    } else if array[candidate] > target {
        if candidate == 0 {
            return 0
        }
        return binarySearch(array[:candidate], target)
    }
    return candidate
}
