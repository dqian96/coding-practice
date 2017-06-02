# Problem: Distribute Candies
# (https://leetcode.com/problems/distribute-candies/#/description)

# The reasoning is simple.
# All we have to do is find the number of distinct elements of the set.

# The sister's set should contain as many of the distinct elements as possible.
# If the distinct number of elements exceed n/2, the rest of the distinct elements
# spill over to the brother's set.
# If ihe distinct number of elements is less, then the rest will be the duplicates
# and the sister's set contain all the distinct elements.

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sistersCandies = set()
        for candy in candies:
            sistersCandies.add(candy)
        return len(sistersCandies) if len(sistersCandies) < len(candies)/2 else len(candies)/2