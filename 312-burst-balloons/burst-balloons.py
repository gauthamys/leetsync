class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dfs(l, r):
            if r - l < 0:
                return 0
            result = 0
            for i in range(l, r + 1):
                gain = nums[l - 1] * nums[i] * nums[r + 1]
                remaining = dfs(l, i - 1) + dfs(i + 1, r)
                result = max(result, remaining + gain)
            return result
        
        return dfs(1, len(nums) - 2)
            