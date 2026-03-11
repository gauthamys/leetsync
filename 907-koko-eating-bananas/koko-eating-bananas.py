class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            res = 0
            for p in piles:
                res += math.ceil(p / speed)
            return res
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if canFinish(mid) > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
            