class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        def helper(s):
            if s in memo:
                return memo[s]
            memo[s] = helper(s - 1) + helper(s - 2)
            return memo[s]

        return helper(n)