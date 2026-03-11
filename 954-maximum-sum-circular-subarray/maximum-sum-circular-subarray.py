class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        maxSum = nums[0]
        curMin = 0
        curMax = 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            maxSum = max(maxSum, curMax)

            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)
            total += n
        
        if total == minSum:
            return maxSum
        
        return max(maxSum, total - minSum)