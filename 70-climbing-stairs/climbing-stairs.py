class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def helper(s):
            if s == 1:
                return 1
            if s == 2:
                return 2
            return helper(s - 1) + helper(s - 2)
        return helper(n)