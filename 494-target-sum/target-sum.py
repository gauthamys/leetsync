class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(start, curSum):
            if start == len(nums):
                return 1 if curSum == target else 0
            
            if (start, curSum) in dp:
                return dp[(start, curSum)]
            
            dp[(start, curSum)] = dfs(start + 1, curSum + nums[start]) + dfs(start + 1, curSum - nums[start])
            return dp[(start, curSum)]
        
        return dfs(0, 0)