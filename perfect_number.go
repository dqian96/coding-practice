// Problem: Perfect Number
// (https://leetcode.com/problems/perfect-number/#/description)

// It is only necessary to go up to and including the square root of num
// to find all the divisiors of num.
// All pairs of divisors are unique until you go up to the sqrt,
// who's matching pair is itself.
// Following it, the pairs repeat in backwards order.

func checkPerfectNumber(num int) bool {
	if num <= 1 {
		return false
	}
	sum, i := 1, 2
	for i = 2; i * i < num; i++ {
		if num % i == 0 {
			sum += (i + num/i)
		}
	}
	if num == i * i {
	    sum += i
	}
	return sum == num
}
