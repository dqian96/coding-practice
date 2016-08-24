# Problem: Best Time to Buy and Sell Stock
#(https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

# Explanation to follow later.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        curr = 0
        for x in range(1, len(prices)):
            curr += (prices[x] - prices[x-1])
            if curr < 0:
                curr = 0
            elif curr > max:
                max = curr
        return max
