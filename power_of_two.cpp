/*
    Power of Two
    (https://leetcode.com/problems/power-of-two/)
*/

// Observe the following powers of of 2 (dec to binary)
// 2^0 = 1, 2^1 = 10, 2^2 = 100, ...
// We know that since 2^0 = 1 in binary, then if we shift it to the left by 1,
// it is equivalent to multiplying it by 2. 
// If we shift it by k, it is equivalent to multiplying it by 2, k times.
// Thus, all powers of 2 can be represented in binary by shifting 1 to the left 
// some k times, i.e. 1, 10, 100, 1000, 10000, ... , 100000...000 are all the 
// possible powers of 2.
// Thus, we notice that all the powers of two have one and only one 1 in the binary representation.
// Since the powers of twos can "span all the bits", we can therefore make the following statement:

// n is a power of 2 <=> the binary rep of n has only one bit set as 1

// We formulate our solution using the above thesis.

// One solution is two convert integer n into a 64-bitset and count the number of 1's directly.
// If there is only one 1, then obv n is a power of two.

// An alternate solution exists. If n is a power of two, then n-1 has a binary rep
// 000,...,0111111 if n = 000,...,1000000. In other words, if n is a power of two with 
// bi = 1 and bj = 0 for all j != i, then n-1's binary rep has bj = 1, j < i and all other bits 0.
// We notice that all bits higher than bi continue to be 0. But bi and all smaller bits
// are "inversed" such that there are no common 1's. Thus n&(n-1) = 0.
// Note that this "inverse" is only possible if only one bit is 1, as if more than one bit is 1,
// then the bi 1 will not be converted to 0 in the flip and their bitwise AND will yield 0.

// Be careful of the EDGE cases -2147483648 as n-1 causes overflow and n == 0 as the AND will yield 0
// regardless.

class Solution {
public:
    bool isPowerOfTwo(int n)  {

        return n != 0 && n != -2147483648 && (n&(n-1)) == 0;

        // Alternatively
        // bitset<64> value(n); 
        // return value.count() == 1;
    }
};

