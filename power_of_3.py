# Problem: Power of 3
# (https://leetcode.com/problems/power-of-three/)

# The naive solution to this problem is obvious -- keep on dividing n by 3 in a loop/recursion
# until you get to either 1 or 0. If you're able to get to 1, then it is a power of 3.
# Of course, this is a O(log3(n)) solution.

# We can do better -- we can solve this problem in constant time.
# Consider:
# Let 3^k = 3*3*3*3*3*...*3*3*3 be the biggest power of 3 under consideration in our question.
# In other words, this is the upper limit/highest possible power of 3 that the system will
# legally recognize. 
# Now, notice that for any power of 3 n, n must be a factor of 3^k. 
# If n = 3^x for any x s.t. x <= k, then 3^k/n = 3^k-x, where k-x is a non-negative integer.
# Therefore, all powers of 3 are factors of 3^k. i.e. n is a power of 3 => n is a factor of 3^k
# Similarly, since 3^k = 3*3*3*3*3*...*3*3*3 and 3 is a prime, then all factors of 3^k must
# be a power of 3. So, if n is a factor of 3^k, then n is a power of 3.

# Then we have, n is a power of 3 <=> 3^k mod n == 0 && n > 0

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 12157665459056928801 % n == 0