class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            res = max(res, prices[i] - min_price)
        return res