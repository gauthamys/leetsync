class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            cur = 0
            res = 1
            for w in weights:
                cur += w
                if cur > capacity:
                    res += 1
                    cur = w
            return res <= days
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l