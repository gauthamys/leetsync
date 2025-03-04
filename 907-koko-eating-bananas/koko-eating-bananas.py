class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile / k)
            return res
        
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            if hours(mid) > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res