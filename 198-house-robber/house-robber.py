class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            prev = dp[i - 1] if i >= 1 else 0
            prevSkip = dp[i - 2] if i >= 2 else 0
            dp[i] = max(prev, nums[i] + prevSkip)
        
        return dp[n - 1]
