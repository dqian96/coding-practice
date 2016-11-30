# Problem: Minimum Moves to Equal Array Elements
# (https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

# NOTES:
# -given non-empty array of size n
# -a move is defined as incrementing any n-1 elements (all but 1) by 1
# -find min number of moves such that all array elements are the same

# CATEGORIZE:
# array, math

# REASONING:
# Ok, to solve this question, we will have to state a couple of axioms/truths and
# build our logic on top of those discoveries.


# 1. The specific values of elements in nums don't matter - only the relative differences
# do. This is because we are not focussed on getting the numbers to a SPECIFIC number,
# but rather, we try to get to a state in which the relative difference between each and
# every number is 0 (i.e. they're the same number) (closing the gap).
# Thus, solving nums is the same as nums* where for all x E nums => x - min(nums) E nums*.
# We are not losing any data critical to solving the problem. We are
# simply shifting the values relative to min(nums) whilst still persistig the relative differences.
# So, solving nums <=> solving nums*

# 2. Each and every move should be to increment all x E nums* except max(nums*).
# Why? Consider the following:
# Either a move includes max(nums*) or it doesn't:
# Assuming max(nums*) is included: the relative difference between each number is maintained
# except the number that is excluded in the increment set, whose relative difference
# to the base (0) will decrease by 1 if it is not min(nums*) but if the number excluded is min(nums*)
# then all relative differences with increase by 1 besides the base(0).
# Assuming max(nums*) is excluded: The relative difference between all the numbers will
# stay the same except max(nums*) which will decrease by 1.
# Since this is a binary option, we see that picking max(nums*) as the number to be excluded
# is definitely better (i.e. one number decrease in relative difference or everyone increase in relative
# difference except 1 OR one number always decrease in relative difference)
# Since we only choose 1 number to exclude, we always choose to exclude max(nums*).

# 3. Excluding max(nums*) is the same as decrementing max(nums*) in nums* while keeping all
# other element equal. Remember, we only care about the relative difference since each specific
# number doesn't matter and we are only seeking to resolve the gap i.e. nums* being 0, 0, 0,...0.
# Thus, when we increment all numbers by 1 and keeping max(nums*) unchanged,
# the relative difference between each number and min(nums*) (our base/reference point
# for the relative difference) will remain the same except for max(nums*), which has not been
# incremeneted and is now closer to min(nums*) thus the only element in nums* that
# should change is the decrement of max(nums*).

# 4. Since each and every move should be a decrement of max(nums*) (in actuality, incrementing all
# but max(nums*) but the relative different is captured by a singular decrement to it...)
# Then, eventually, we would have to decrement exactly max(nums*) time for that single element.
# When max(nums*) is no longer the biggest, we decrement secondMax(nums*). We then alternate
# back to max(nums*) when it is bigger again...i.e. each move decreases the current max...
# This means that eventually, we would have to decrement each element in nums* until it is 0.
# (since following our philosophy of decrementing the max, the only number that is ever changed
# in nums* with each move is the number that is decremented). So, eventually, we would have to 
# decrement each x in nums* x times...i.e. 0 requries 0 decrements, 1 requires 1 decrements,...
# and so on, until we will eventually have 0000000...0000 or not relative difference.
# This is when our goal is achieved and all our numbers in nums is equal.

# Conclusion:
# Create nums* by replacing each x with x - min(nums) or in other words,
# transform nums such that each element is replaced by its relative difference with
# min(nums) (make each number relative to min(nums)/frame of reference).
# Sum nums* -> this is the number of moves/iterations needed.


# ALGORITHM:
# We can do this in one pass. Simply go through nums and find min(nums) by keeping
# track of the smallest element seen. At the same time, sum nums.
# Now, making each element in nums relative to the smallest element is the same as
# subtracting each element by the min(nums). 
# This is a total value of min(nums) * len(nums) subtracted.
# Now sum(nums) - min(nums) * len(nums) is just the sum of the relative differences
# i.e. (n0 + n1 + n2 + ... nk) - (min(nums) + min(nums) + ... + min(nums))
# i.e. n0 - min(nums) + n1 - min(nums) + ... = sum of each element's relative difference to min(nums)

# ANALYSIS:
# O(n)

# O(n) time - single pass
"""
class Solution(object):
    def minMoves(self, nums):
        minNum = nums[0]
        sum = 0
        for n in nums:
            if n < minNum:
                minNum = n
            sum += n
        return sum - (minNum * len(nums))
"""

# O(n) time - multiple passes but functional

class Solution(object):
    def minMoves(self, nums):
        minNums = min(nums)
        return sum(map(lambda x: x - minNums, nums))
