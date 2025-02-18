class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = float('inf')
        res = 0
        for i in range(len(prices)):
            curProfit = prices[i] - curMin
            curMin = min(curMin, prices[i])
            res = max(res, curProfit)
        
        return res