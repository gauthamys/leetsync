class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + max(1, x % 2)
        while l <= r:
            mid = (l + r) // 2
            sq = mid ** 2
            if sq == x:
                return mid
            elif sq < x:
                l = mid + 1
            else:
                r = mid - 1
        return mid - 1 if mid ** 2 > x else mid