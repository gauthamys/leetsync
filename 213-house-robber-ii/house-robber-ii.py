class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            dp = [0] * len(arr)
            for i in range(len(arr)):
                prev = 0 if i - 1 < 0 else dp[i - 1]
                prevSkip = 0 if i - 2 < 0 else dp[i - 2]
                dp[i] = max(prev, arr[i] + prevSkip)
            
            return 0 if not dp else dp[-1]
        
        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
            