class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1

        for s in range(target + 1):
            for n in nums:
                if s - n >= 0:
                    dp[s] += dp[s - n]
                else:
                    break
        
        return dp[target]