// Problem: Maximum Product of Three Numbers
// (https://leetcode.com/problems/maximum-product-of-three-numbers/#/description)

// The maximum product is either positive, negative, or 0.

// In the case where it is positive, then there must be either 3 positive
// numbers or two negative numbers and one positive - there are no possible
// combinations for this case.
// Thus the maximum product is either the product of the 3 largest
// positive numbers (beats all other positive combos) or the smallest two negativers
// * largest positive (pick any and the product would be less).

// In the case where it is negative, then there:
// There are only negative numbers
// or there is only one negative number and two positive numbers
// In the case of all negative numbers, we pick the "3 largest ones",
// which are the ones closest to 0/smallest magnitude.
// In the other case, there are only 3 numbers, so we pick the 3 largest.

// In the case where it is 0, then there must be a one or more 0's
// and either all the rest are negatives, or there are two positives and one neg.
// In this case, picking the three largest (which includes 0) is ideal.

// The solution must be in one of the three cases. In every case, we see that
// the maximum product is the max of the three largest numbers of the
// largest * two smallest numbers

func maximumProduct(nums []int) int {
    largest, smallest := [3]int{-1001, -1001, -1001}, [2]int{1001, 1001}

    inject := func(array []int, injection int, index int) {
        for i := index; i < len(array); i++ {
            tmp := array[i]
            array[i] = injection
            injection = tmp
        }
    }
    
    for _, num := range nums {
        for i := 0; i < 3; i++ {
            if num > largest[i] {
                inject(largest[:], num, i)
                break
            }
        }
        for i := 0; i < 2; i++ {
            if num < smallest[i] {
                inject(smallest[:], num, i)
                break
            }
        }
    }
    ans := largest[0] * largest[1] * largest[2]
    cand := largest[0] * smallest[0] * smallest[1]
    if cand > ans {
        ans = cand
    }
    return ans
}
