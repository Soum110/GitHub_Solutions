class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stockinhand = prices[0]
        for i in range(1, len(prices)):
            curr = prices[i]
            if stockinhand > curr:
                stockinhand = curr
            elif stockinhand <= curr:
                profit += (curr-stockinhand)
                stockinhand = curr
        return profit
        