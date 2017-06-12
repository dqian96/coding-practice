# Problem: Best Time to Buy and Sell Stock II
# (https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        return sum(filter(lambda x: x >= 1, [(prices[i] - prices[i-1]) for i in range(1, len(prices))]))
