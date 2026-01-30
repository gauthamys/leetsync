class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        def hours(k):
            res = 0
            for p in piles:
                res += math.ceil(p / k)
            return res
        
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l + r) // 2
            if hours(mid) <= h:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        
        return res