class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = float('inf')
        res = 0
        for i in range(len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
            curMax = prices[i] - curMin
            res = max(res, curMax)
        
        return res