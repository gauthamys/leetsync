class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        maxSum = nums[0]
        total = sum(nums)
        curSum = 0
        curMin = 0
        
        for n in nums:
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)
        
        if total == minSum:
            return maxSum
        
        return max(maxSum, total - minSum)