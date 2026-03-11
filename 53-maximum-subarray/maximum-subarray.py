class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        res = curSum
        for n in nums[1:]:
            curSum = max(n, curSum + n)
            res = max(res, curSum)
        return res
        