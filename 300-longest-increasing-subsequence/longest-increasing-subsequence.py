class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            cur = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = max(cur, 1 + dp[j])
            dp[i] = cur
        
        return max(dp)