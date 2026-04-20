class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        profit = 0
        for price in prices:
            if price < mn:
                mn = price
            else:
                profit = max(profit, price - mn)
        return profit